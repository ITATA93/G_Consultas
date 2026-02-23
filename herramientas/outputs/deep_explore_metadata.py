"""
Deep exploration of all remaining IRIS metadata sources:
1. websys.DictionaryClassProperty — column display names (Spanish)
2. websys.DictionaryTranslated — translations
3. INFORMATION_SCHEMA.COLUMNS — sync column descriptions to local DB
4. Any other websys.* tables
5. CacheDictionary from DataInspector
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\deep_explore.txt"
L = []
def p(s=""): L.append(s)

conn = conectar_alma()
cur = conn.cursor()

# ============================================================
# 1. websys.DictionaryClassProperty — HOW MANY total?
# ============================================================
p("=" * 70)
p("1. websys.DictionaryClassProperty — OVERVIEW")
p("=" * 70)
try:
    cur.execute("SELECT TOP 1 COUNT(*) FROM websys.DictionaryClassProperty")
    total = cur.fetchone()[0]
    p(f"Total entries: {total}")
    
    # Sample: questionnaire properties with Spanish names
    cur.execute("""
        SELECT TOP 20 dc.ClassName, dcp.PropertyName, dcp.DisplayName, dcp.SQLColumnName
        FROM websys.DictionaryClassProperty dcp
        JOIN websys.DictionaryClass dc ON dcp.ParRef = dc.ID
        WHERE dc.ClassName LIKE 'questionnaire.QTCEEVRIEST%'
        ORDER BY dcp.childsub
    """)
    rows = cur.fetchall()
    p(f"\nSample — QTCEEVRIEST (Caprini) columns:")
    for r in rows:
        p(f"  {r[2]:45} | SQL: {r[3]:25} | Prop: {r[1]}")
        
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 2. websys.DictionaryClassProperty — QTCERIESGO (Riesgo-Dependencia)
# ============================================================
p("\n" + "=" * 70)
p("2. QTCERIESGO (Riesgo-Dependencia) columns")
p("=" * 70)
try:
    cur.execute("""
        SELECT TOP 30 dcp.DisplayName, dcp.SQLColumnName, dcp.PropertyName
        FROM websys.DictionaryClassProperty dcp
        JOIN websys.DictionaryClass dc ON dcp.ParRef = dc.ID
        WHERE dc.ClassName = 'questionnaire.QTCERIESGO'
        ORDER BY dcp.childsub
    """)
    for r in cur.fetchall():
        p(f"  {r[0]:50} | {r[1]:25}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 3. websys.DictionaryClassProperty — QCLXXMDI (Dispositivos Invasivos)
# ============================================================
p("\n" + "=" * 70)
p("3. QCLXXMDI (Dispositivos Invasivos) columns")
p("=" * 70)
try:
    cur.execute("""
        SELECT TOP 30 dcp.DisplayName, dcp.SQLColumnName, dcp.PropertyName
        FROM websys.DictionaryClassProperty dcp
        JOIN websys.DictionaryClass dc ON dcp.ParRef = dc.ID
        WHERE dc.ClassName = 'questionnaire.QCLXXMDI'
        ORDER BY dcp.childsub
    """)
    for r in cur.fetchall():
        p(f"  {r[0]:50} | {r[1]:25}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 4. websys.DictionaryTranslated — Structure & sample
# ============================================================
p("\n" + "=" * 70)
p("4. websys.DictionaryTranslated")
p("=" * 70)
try:
    cur.execute("""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'websys' AND TABLE_NAME = 'DictionaryTranslated'
        ORDER BY ORDINAL_POSITION
    """)
    p("Columns:")
    for r in cur.fetchall():
        p(f"  {r[0]:30} {r[1]}")
    
    cur.execute("SELECT TOP 1 COUNT(*) FROM websys.DictionaryTranslated")
    p(f"\nTotal rows: {cur.fetchone()[0]}")
    
    cur.execute("SELECT TOP 10 * FROM websys.DictionaryTranslated")
    p("Sample:")
    for r in cur.fetchall():
        p(f"  {str(r)[:150]}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 5. ALL websys.* tables
# ============================================================
p("\n" + "=" * 70)
p("5. ALL websys.* tables")
p("=" * 70)
try:
    cur.execute("""
        SELECT TABLE_NAME, DESCRIPTION
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'websys'
        ORDER BY TABLE_NAME
    """)
    for r in cur.fetchall():
        desc = (r[1] or '')[:70]
        p(f"  {r[0]:40} | {desc}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 6. Region_CLXX_Utility_DataInspector.CacheDictionary
# ============================================================
p("\n" + "=" * 70)
p("6. CacheDictionary (DataInspector)")
p("=" * 70)
try:
    cur.execute("""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'Region_CLXX_Utility_DataInspector' 
        AND TABLE_NAME = 'CacheDictionary'
        ORDER BY ORDINAL_POSITION
    """)
    p("Columns:")
    for r in cur.fetchall():
        p(f"  {r[0]:30} {r[1]}")
    
    cur.execute("SELECT TOP 10 * FROM Region_CLXX_Utility_DataInspector.CacheDictionary")
    p("\nSample:")
    for r in cur.fetchall():
        p(f"  {str(r)[:200]}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 7. INFORMATION_SCHEMA.COLUMNS — coverage breakdown by schema
# ============================================================
p("\n" + "=" * 70)
p("7. INFORMATION_SCHEMA.COLUMNS — desc coverage by schema")
p("=" * 70)
try:
    cur.execute("""
        SELECT TABLE_SCHEMA, 
               COUNT(*) as total,
               SUM(CASE WHEN DESCRIPTION IS NOT NULL AND DESCRIPTION != '' THEN 1 ELSE 0 END) as with_desc
        FROM INFORMATION_SCHEMA.COLUMNS
        GROUP BY TABLE_SCHEMA
        ORDER BY total DESC
    """)
    for r in cur.fetchall():
        pct = 100 * r[2] / r[1] if r[1] > 0 else 0
        p(f"  {r[0]:40} {r[1]:8} cols | {r[2]:8} with desc ({pct:.0f}%)")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# 8. How many column descriptions could we sync?
# ============================================================
p("\n" + "=" * 70)
p("8. Column descriptions available to sync from SQLUser")
p("=" * 70)
try:
    cur.execute("""
        SELECT TOP 1 COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'SQLUser'
        AND DESCRIPTION IS NOT NULL AND DESCRIPTION != ''
    """)
    sqluser_with = cur.fetchone()[0]
    cur.execute("""
        SELECT TOP 1 COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'SQLUser'
    """)
    sqluser_total = cur.fetchone()[0]
    p(f"SQLUser columns: {sqluser_total}")
    p(f"With description: {sqluser_with} ({100*sqluser_with/sqluser_total:.1f}%)")
    
    # questionnaire columns
    cur.execute("""
        SELECT TOP 1 COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'questionnaire'
    """)
    q_total = cur.fetchone()[0]
    cur.execute("""
        SELECT TOP 1 COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'questionnaire'
        AND DESCRIPTION IS NOT NULL AND DESCRIPTION != ''
    """)
    q_with = cur.fetchone()[0]
    p(f"\nQuestionnaire columns: {q_total}")
    p(f"With description: {q_with} ({100*q_with/q_total:.1f}% — we have websys names instead)")
    
except Exception as e:
    p(f"  ERROR: {e}")

cur.close()
conn.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))
print(f"OK — {len(L)} lines -> {OUT}")
