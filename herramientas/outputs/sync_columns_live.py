"""
Final deep dive:
1. INFORMATION_SCHEMA.COLUMNS for SQLUser — sync remaining column descriptions
2. websys.Configuration — system config (might have schema info)
3. Region_CLXX tables — Chilean customizations
"""
import sys
import sqlite3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\final_dive.md"
L = []
def p(s=""): L.append(s)

conn_iris = conectar_alma()
cur = conn_iris.cursor()
conn_local = sqlite3.connect(DB)
c = conn_local.cursor()

# ============================================================
# 1. Sync column descriptions from INFORMATION_SCHEMA.COLUMNS (SQLUser)
# ============================================================
p("=" * 60)
p("1. Syncing column DESC from INFORMATION_SCHEMA (SQLUser)")
p("=" * 60)

# Get table_id mapping from local DB
c.execute("SELECT t.id, t.nombre, s.nombre FROM tablas t JOIN schemas s ON t.schema_id = s.id WHERE s.nombre = 'SQLUser'")
table_ids = {name: tid for tid, name, schema in c.fetchall()}
p(f"Local SQLUser tables: {len(table_ids)}")

updated = 0
# Fetch all column descriptions from SQLUser in batches
cur.execute("""
    SELECT TABLE_NAME, COLUMN_NAME, DESCRIPTION
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'SQLUser'
    AND DESCRIPTION IS NOT NULL AND DESCRIPTION != ''
""")
rows = cur.fetchall()
p(f"LIVE columns with description: {len(rows)}")

for table_name, col_name, desc in rows:
    tid = table_ids.get(table_name)
    if tid and desc:
        c.execute("""UPDATE columnas SET descripcion = ?
                    WHERE tabla_id = ? AND nombre = ?
                    AND (descripcion IS NULL OR descripcion = '')""",
                  (desc, tid, col_name))
        if c.rowcount > 0:
            updated += 1
conn_local.commit()
p(f"Updated: {updated} column descriptions")

# ============================================================
# 2. Now do the same for questionnaire schema
# ============================================================
p("\n" + "=" * 60)
p("2. Syncing column DESC from INFORMATION_SCHEMA (questionnaire)")
p("=" * 60)

c.execute("SELECT t.id, t.nombre FROM tablas t JOIN schemas s ON t.schema_id = s.id WHERE s.nombre = 'questionnaire'")
q_table_ids = {name: tid for tid, name in c.fetchall()}
p(f"Local questionnaire tables: {len(q_table_ids)}")

# The questionnaire schema has 185K columns — need to fetch in blocks
updated_q = 0
offset = 0
batch_size = 10000
while True:
    cur.execute(f"""
        SELECT TOP {batch_size} TABLE_NAME, COLUMN_NAME, DESCRIPTION
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'questionnaire'
        AND DESCRIPTION IS NOT NULL AND DESCRIPTION != ''
        AND ORDINAL_POSITION > {offset}
        ORDER BY ORDINAL_POSITION
    """)
    rows = cur.fetchall()
    if not rows:
        break
    
    for table_name, col_name, desc in rows:
        tid = q_table_ids.get(table_name)
        if tid and desc:
            c.execute("""UPDATE columnas SET descripcion = ?
                        WHERE tabla_id = ? AND nombre = ?
                        AND (descripcion IS NULL OR descripcion = '')""",
                      (desc, tid, col_name))
            if c.rowcount > 0:
                updated_q += 1
    
    offset += batch_size
    p(f"  Processed {offset}... (+{updated_q} updates)")
    
    if len(rows) < batch_size:
        break

conn_local.commit()
p(f"Total questionnaire column updates: {updated_q}")

# ============================================================
# 3. Region_CLXX — Chilean customization schemas
# ============================================================
p("\n" + "=" * 60)
p("3. ALL Region_CLXX schemas and tables")
p("=" * 60)
try:
    cur.execute("""
        SELECT TABLE_SCHEMA, TABLE_NAME, DESCRIPTION
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA LIKE 'Region_CLXX%'
        ORDER BY TABLE_SCHEMA, TABLE_NAME
    """)
    for r in cur.fetchall():
        desc = (r[2] or '')[:50]
        p(f"  {r[0]:50} {r[1]:40} | {desc}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# Final stats
# ============================================================
p("\n" + "=" * 60)
p("FINAL COVERAGE")
p("=" * 60)

c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion IS NOT NULL AND descripcion != ''")
t_desc = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion_es IS NOT NULL AND descripcion_es != ''")
t_es = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas")
t_total = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM columnas WHERE descripcion IS NOT NULL AND descripcion != ''")
c_desc = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM columnas")
c_total = c.fetchone()[0]

p(f"TABLAS: {t_total}")
p(f"  Desc EN: {t_desc} ({100*t_desc/t_total:.1f}%)")
p(f"  Desc ES: {t_es} ({100*t_es/t_total:.1f}%)")
p(f"COLUMNAS: {c_total}")
p(f"  Desc EN: {c_desc} ({100*c_desc/c_total:.1f}%)")

cur.close()
conn_iris.close()
conn_local.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))
print(f"Done — {len(L)} lines")
