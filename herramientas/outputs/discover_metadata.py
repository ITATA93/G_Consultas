"""
Extract descriptions from INFORMATION_SCHEMA (tables + columns) and websys.Dictionary.
These are accessible without special privileges.
"""
import sys
import sqlite3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\metadata_extract.txt"

L = []
def p(s=""): L.append(s)

conn_iris = conectar_alma()
cur = conn_iris.cursor()
conn_local = sqlite3.connect(DB)
c = conn_local.cursor()

# ============================================================
# 1. INFORMATION_SCHEMA.TABLES — Get DESCRIPTION for all tables
# ============================================================
p("=== 1. Table DESCRIPTIONS from INFORMATION_SCHEMA ===")
try:
    cur.execute("""
        SELECT TABLE_SCHEMA, TABLE_NAME, DESCRIPTION
        FROM INFORMATION_SCHEMA.TABLES
        WHERE DESCRIPTION IS NOT NULL AND DESCRIPTION != ''
        ORDER BY TABLE_SCHEMA, TABLE_NAME
    """)
    rows = cur.fetchall()
    p(f"Tables with DESCRIPTION: {len(rows)}")
    
    # Show first 20
    for r in rows[:20]:
        p(f"  {r[0]}.{r[1]:40} | {(r[2] or '')[:80]}")
    
    if len(rows) > 20:
        p(f"  ... ({len(rows) - 20} more)")
    
    # Update local DB
    updated_tables = 0
    for schema, table, desc in rows:
        if desc:
            c.execute("""UPDATE tablas SET descripcion = ? 
                        WHERE nombre = ? AND (descripcion IS NULL OR descripcion = '')
                        AND schema_id IN (SELECT id FROM schemas WHERE nombre = ?)""",
                      (desc, table, schema))
            if c.rowcount > 0:
                updated_tables += 1
    conn_local.commit()
    p(f"Updated local DB: {updated_tables} tables")
    
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 2. INFORMATION_SCHEMA.COLUMNS — Get ALL descriptions 
#    for tables that lack them locally
# ============================================================
p("\n=== 2. Column DESCRIPTIONS from INFORMATION_SCHEMA ===")
try:
    cur.execute("""
        SELECT TOP 1 COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE DESCRIPTION IS NOT NULL AND DESCRIPTION != ''
    """)
    total_with_desc = cur.fetchone()[0]
    
    cur.execute("SELECT TOP 1 COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS")
    total_cols = cur.fetchone()[0]
    
    p(f"Total columns in LIVE: {total_cols}")
    p(f"With DESCRIPTION: {total_with_desc} ({100*total_with_desc/total_cols:.1f}%)")
    
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 3. websys.Dictionary — UI labels/translations?
# ============================================================
p("\n=== 3. websys.Dictionary ===")
try:
    cur.execute("""
        SELECT TOP 5 COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'websys' AND TABLE_NAME = 'Dictionary'
        ORDER BY ORDINAL_POSITION
    """)
    cols = cur.fetchall()
    p("Columns:")
    for c2 in cols:
        p(f"  {c2[0]:30} {c2[1]}")
except Exception as e:
    p(f"  ERROR: {e}")

try:
    cur.execute("SELECT TOP 10 * FROM websys.Dictionary")
    rows = cur.fetchall()
    p(f"\nSample rows ({len(rows)}):")
    for r in rows:
        p(f"  {str(r)[:120]}")
except Exception as e:
    p(f"  Sample ERROR: {e}")

# ============================================================
# 4. websys.DictionaryClass — class-level dictionary
# ============================================================
p("\n=== 4. websys.DictionaryClass ===")
try:
    cur.execute("""
        SELECT TOP 5 COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'websys' AND TABLE_NAME = 'DictionaryClass'
        ORDER BY ORDINAL_POSITION
    """)
    for c2 in cur.fetchall():
        p(f"  {c2[0]:30} {c2[1]}")
except Exception as e:
    p(f"  ERROR: {e}")

try:
    cur.execute("SELECT TOP 10 * FROM websys.DictionaryClass")
    rows = cur.fetchall()
    p(f"\nSample ({len(rows)} rows):")
    for r in rows:
        p(f"  {str(r)[:120]}")
except Exception as e:
    p(f"  Sample ERROR: {e}")

# ============================================================
# 5. websys.DictionaryClassProperty — property-level dictionary
# ============================================================
p("\n=== 5. websys.DictionaryClassProperty ===")
try:
    cur.execute("""
        SELECT TOP 10 COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'websys' AND TABLE_NAME = 'DictionaryClassProperty'
        ORDER BY ORDINAL_POSITION
    """)
    for c2 in cur.fetchall():
        p(f"  {c2[0]:30} {c2[1]}")
except Exception as e:
    p(f"  ERROR: {e}")

try:
    cur.execute("SELECT TOP 10 * FROM websys.DictionaryClassProperty")
    rows = cur.fetchall()
    p(f"\nSample ({len(rows)} rows):")
    for r in rows:
        p(f"  {str(r)[:150]}")
except Exception as e:
    p(f"  Sample ERROR: {e}")

# ============================================================
# 6. CT_Dictionary — TrakCare's own dictionary?
# ============================================================
p("\n=== 6. CT_Dictionary ===")
try:
    cur.execute("""
        SELECT TOP 10 COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'SQLUser' AND TABLE_NAME = 'CT_Dictionary'
        ORDER BY ORDINAL_POSITION
    """)
    for c2 in cur.fetchall():
        p(f"  {c2[0]:30} {c2[1]}")
except Exception as e:
    p(f"  ERROR: {e}")

try:
    cur.execute("SELECT TOP 5 * FROM SQLUser.CT_Dictionary")
    rows = cur.fetchall()
    p(f"\nSample ({len(rows)} rows):")
    for r in rows:
        p(f"  {str(r)[:120]}")
except Exception as e:
    p(f"  Sample ERROR: {e}")

# ============================================================
# Summary
# ============================================================
p("\n=== RESUMEN FINAL ===")
c.execute("SELECT COUNT(*) FROM tablas WHERE descripcion IS NOT NULL AND descripcion != ''")
new_total = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM tablas")
total = c.fetchone()[0]
p(f"Descripcion EN despues de update: {new_total}/{total} ({100*new_total/total:.1f}%)")

cur.close()
conn_iris.close()
conn_local.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))
print(f"OK — {len(L)} lines")
