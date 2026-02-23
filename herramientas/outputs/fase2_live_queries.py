"""
Fase 2: Queries mínimas al LIVE para completar información faltante.

QUERIES SEGURAS:
- Solo INFORMATION_SCHEMA (metadatos, no datos clínicos)
- TOP 20 máximo
- Solo tablas que necesitan información
"""
import sys
import sqlite3
from pathlib import Path

# Setup path for db_config import
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\fase2_result.txt"

L = []
def p(s=""): L.append(s)

# ============================================================
# Connect to LIVE
# ============================================================
print("Conectando a ALMA LIVE...")
try:
    conn_iris = conectar_alma()
    cursor_iris = conn_iris.cursor()
    print("OK - Conectado a IRIS")
except Exception as e:
    print(f"ERROR conectando a IRIS: {e}")
    print("Abortando Fase 2")
    sys.exit(1)

conn_local = sqlite3.connect(DB)
c_local = conn_local.cursor()

p("=" * 70)
p("FASE 2: VERIFICACION LIVE — QUERIES MINIMAS")
p("=" * 70)

# ============================================================
# QUERY 1: Discover missing table names (RAD_, IN_, EP_)
# ============================================================
p("\n--- Q1: Tablas RAD_* en LIVE ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 TABLE_SCHEMA, TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME LIKE 'RAD_%'
        ORDER BY TABLE_NAME
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        p(f"  {r[0]}.{r[1]}")
    if not rows:
        p("  (ninguna encontrada)")
    print(f"Q1 RAD_: {len(rows)} tablas")
except Exception as e:
    p(f"  ERROR: {e}")
    print(f"Q1 ERROR: {e}")

p("\n--- Q2: Tablas CT_Nat*, CT_Mar* en LIVE ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'SQLUser' 
        AND (TABLE_NAME LIKE 'CT_Nat%' OR TABLE_NAME LIKE 'CT_Mar%')
        ORDER BY TABLE_NAME
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        p(f"  {r[0]}")
    if not rows:
        p("  (ninguna encontrada)")
    print(f"Q2 CT_Nat/Mar: {len(rows)} tablas")
except Exception as e:
    p(f"  ERROR: {e}")

p("\n--- Q3: Tablas AR_Pat*, ARC_Item* en LIVE ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'SQLUser' 
        AND (TABLE_NAME LIKE 'AR_Pat%' OR TABLE_NAME LIKE 'ARC_ItemC%')
        ORDER BY TABLE_NAME
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        p(f"  {r[0]}")
    if not rows:
        p("  (ninguna encontrada)")
    print(f"Q3 AR/ARC: {len(rows)} tablas")
except Exception as e:
    p(f"  ERROR: {e}")

p("\n--- Q4: Tablas IN_* (Inventario) en LIVE ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'SQLUser' 
        AND TABLE_NAME LIKE 'IN_%'
        ORDER BY TABLE_NAME
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        p(f"  {r[0]}")
    if not rows:
        p("  (ninguna encontrada)")
    print(f"Q4 IN_: {len(rows)} tablas")
except Exception as e:
    p(f"  ERROR: {e}")

p("\n--- Q5: Tablas PHC_Drug* en LIVE ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'SQLUser' 
        AND TABLE_NAME LIKE 'PHC_Drug%'
        ORDER BY TABLE_NAME
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        p(f"  {r[0]}")
    if not rows:
        p("  (ninguna encontrada)")
    print(f"Q5 PHC_Drug: {len(rows)} tablas")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# QUERY 6: Get questionnaire names from SS_UserDefWindow
# ============================================================
p("\n--- Q6: Nombres reales de questionnaires (primeros 20) ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 WIN_Code, WIN_Desc
        FROM SQLUser.SS_UserDefWindow
        WHERE WIN_Code IS NOT NULL AND WIN_Code != ''
        ORDER BY WIN_Code
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        p(f"  {r[0]:30} | {r[1] or 'sin desc'}")
    print(f"Q6 questionnaire names: {len(rows)} filas")
except Exception as e:
    p(f"  ERROR: {e}")
    print(f"Q6 ERROR: {e}")

# ============================================================
# QUERY 7: Count total questionnaires with names
# ============================================================
p("\n--- Q7: Total questionnaires con nombre en SS_UserDefWindow ---")
try:
    cursor_iris.execute("""
        SELECT TOP 1 COUNT(*) 
        FROM SQLUser.SS_UserDefWindow
        WHERE WIN_Code IS NOT NULL AND WIN_Code != ''
    """)
    count = cursor_iris.fetchone()[0]
    p(f"  Total: {count}")
    print(f"Q7 total questionnaires: {count}")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# QUERY 8: Get column descriptions for MR_Medication (largest gap)
# ============================================================
p("\n--- Q8: Columnas de MR_Medication (muestra TOP 20, tabla más grande sin desc) ---")
try:
    cursor_iris.execute("""
        SELECT TOP 20 COLUMN_NAME, DATA_TYPE, DESCRIPTION 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'SQLUser' AND TABLE_NAME = 'MR_Medication'
        ORDER BY ORDINAL_POSITION
    """)
    rows = cursor_iris.fetchall()
    for r in rows:
        desc = r[2] or ''
        p(f"  {r[0]:40} {r[1]:12} {desc[:50]}")
    print(f"Q8 MR_Medication cols: {len(rows)} filas")
except Exception as e:
    p(f"  ERROR: {e}")

# ============================================================
# QUERY 9: Questionnaires sin desc - get names from WIN
# ============================================================
p("\n--- Q9: Nombres de questionnaires sin descripcion (batch) ---")
# Get the codes from local DB that are missing descriptions
c_local.execute("""SELECT t.nombre FROM tablas t 
                   JOIN schemas s ON t.schema_id = s.id
                   WHERE s.nombre = 'questionnaire' 
                   AND (t.descripcion IS NULL OR t.descripcion = '')
                   LIMIT 20""")
missing_codes = [r[0] for r in c_local.fetchall()]

if missing_codes:
    # Build safe IN clause
    placeholders = ','.join([f"'{code}'" for code in missing_codes])
    try:
        cursor_iris.execute(f"""
            SELECT TOP 20 WIN_Code, WIN_Desc
            FROM SQLUser.SS_UserDefWindow
            WHERE WIN_Code IN ({placeholders})
        """)
        rows = cursor_iris.fetchall()
        found = 0
        for r in rows:
            p(f"  {r[0]:30} → {r[1] or 'sin desc'}")
            # Update local DB
            if r[1]:
                c_local.execute("UPDATE tablas SET descripcion = ? WHERE nombre = ? AND (descripcion IS NULL OR descripcion = '')",
                               (r[1], r[0]))
                found += 1
        conn_local.commit()
        p(f"  Actualizadas: {found}")
        print(f"Q9 questionnaire names matched: {found}/{len(missing_codes)}")
    except Exception as e:
        p(f"  ERROR: {e}")
        print(f"Q9 ERROR: {e}")

# ============================================================
# Summary
# ============================================================
p("\n" + "=" * 70)
p("RESUMEN FASE 2")
p("=" * 70)

# Recount coverage
c_local.execute("SELECT COUNT(*) FROM tablas WHERE descripcion IS NOT NULL AND descripcion != ''")
new_desc_count = c_local.fetchone()[0]
c_local.execute("SELECT COUNT(*) FROM tablas WHERE descripcion_es IS NOT NULL AND descripcion_es != ''")
new_es_count = c_local.fetchone()[0]
c_local.execute("SELECT COUNT(*) FROM tablas")
total = c_local.fetchone()[0]

p(f"Total tablas: {total}")
p(f"Con descripcion (EN): {new_desc_count} ({100*new_desc_count/total:.1f}%)")
p(f"Con descripcion (ES): {new_es_count} ({100*new_es_count/total:.1f}%)")

# Close connections
cursor_iris.close()
conn_iris.close()
conn_local.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))

print(f"\nOK — {len(L)} lineas en {OUT}")
