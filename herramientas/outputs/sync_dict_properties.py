"""
Sync column display names from websys.DictionaryClassProperty to local DB.
Maps: questionnaireTable.SQLColumnName -> DisplayName
This enriches our local columnas table with human-readable Spanish names.
"""
import sys
import sqlite3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"

conn_iris = conectar_alma()
cur = conn_iris.cursor()
conn_local = sqlite3.connect(DB)
c = conn_local.cursor()

# Check local DB structure for columnas
c.execute("PRAGMA table_info(columnas)")
cols_info = c.fetchall()
col_names = [r[1] for r in cols_info]
print(f"Columnas table has: {', '.join(col_names)}")
has_desc_es = 'desc_es' in col_names

print(f"\nFetching websys.DictionaryClassProperty (174K+ entries)...")
cur.execute("""
    SELECT dc.SQLTableName, dcp.SQLColumnName, dcp.DisplayName
    FROM websys.DictionaryClassProperty dcp
    JOIN websys.DictionaryClass dc ON dcp.ParRef = dc.ID
    WHERE dcp.DisplayName IS NOT NULL AND dcp.DisplayName != ''
    AND dcp.SQLColumnName IS NOT NULL AND dcp.SQLColumnName != ''
""")
rows = cur.fetchall()
print(f"Fetched: {len(rows)} property entries")

# Build map: (table_name, column_name) -> display_name
prop_map = {}
for full_table, col_name, display_name in rows:
    # full_table is like "questionnaire.QTCEEVRIEST"
    schema_table = full_table.split('.')
    if len(schema_table) == 2:
        schema, table = schema_table
        prop_map[(table, col_name)] = display_name

print(f"Unique mappings: {len(prop_map)}")

# Get table_id -> table_name mapping from local DB
c.execute("SELECT id, nombre FROM tablas")
table_ids = {name: tid for tid, name in c.fetchall()}

# Update local columnas
if has_desc_es:
    updated = 0
    batch_size = 1000
    batch = []
    
    for (table_name, col_name), display_name in prop_map.items():
        tid = table_ids.get(table_name)
        if tid:
            batch.append((display_name, tid, col_name))
            if len(batch) >= batch_size:
                c.executemany("""UPDATE columnas SET desc_es = ? 
                               WHERE tabla_id = ? AND nombre = ?
                               AND (desc_es IS NULL OR desc_es = '')""", batch)
                updated += c.rowcount
                batch = []
    
    if batch:
        c.executemany("""UPDATE columnas SET desc_es = ?
                        WHERE tabla_id = ? AND nombre = ?
                        AND (desc_es IS NULL OR desc_es = '')""", batch)
        updated += c.rowcount
    
    conn_local.commit()
    print(f"\nUpdated desc_es: {updated} columns")
else:
    print("\nNo desc_es column in columnas table — updating descripcion instead")
    updated = 0
    for (table_name, col_name), display_name in prop_map.items():
        tid = table_ids.get(table_name)
        if tid:
            c.execute("""UPDATE columnas SET descripcion = ?
                        WHERE tabla_id = ? AND nombre = ?
                        AND (descripcion IS NULL OR descripcion = '')""",
                      (display_name, tid, col_name))
            updated += c.rowcount
    conn_local.commit()
    print(f"Updated descripcion: {updated} columns")

# Final stats
c.execute("SELECT COUNT(*) FROM columnas WHERE descripcion IS NOT NULL AND descripcion != ''")
desc_total = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM columnas")
col_total = c.fetchone()[0]

if has_desc_es:
    c.execute("SELECT COUNT(*) FROM columnas WHERE desc_es IS NOT NULL AND desc_es != ''")
    es_total = c.fetchone()[0]
    print(f"\n=== COLUMN COVERAGE ===")
    print(f"Total columnas: {col_total}")
    print(f"Con descripcion (EN): {desc_total} ({100*desc_total/col_total:.1f}%)")
    print(f"Con desc_es (ES): {es_total} ({100*es_total/col_total:.1f}%)")
else:
    print(f"\n=== COLUMN COVERAGE ===")
    print(f"Total columnas: {col_total}")
    print(f"Con descripcion: {desc_total} ({100*desc_total/col_total:.1f}%)")

# Show some enriched samples
print("\n=== Samples: Caprini (QTCEEVRIEST) columns ===")
tid = table_ids.get('QTCEEVRIEST')
if tid:
    target_col = 'desc_es' if has_desc_es else 'descripcion'
    c.execute(f"SELECT nombre, {target_col} FROM columnas WHERE tabla_id = ? AND {target_col} IS NOT NULL AND {target_col} != '' LIMIT 15", (tid,))
    for r in c.fetchall():
        print(f"  {r[0]:30} -> {r[1]}")

cur.close()
conn_iris.close()
conn_local.close()
