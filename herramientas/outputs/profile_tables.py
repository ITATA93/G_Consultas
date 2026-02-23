"""
Phase 3: Lightweight table profiling + SQL examples
STRATEGY: SELECT TOP 1 1 (instant, no full scan)
Only checks if table has data (yes/no), never counts.
Adds 0.5s delay between queries.
"""
import sys
import time
import sqlite3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import conectar_alma

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"
OUT = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\herramientas\outputs\table_profile.md"

KEY_TABLES = {
    'PA_Person': 'SQLUser', 'PA_PatMas': 'SQLUser', 'PA_Adm': 'SQLUser',
    'PA_PatInsur': 'SQLUser', 'PA_AdmInsur': 'SQLUser',
    'MR_Adm': 'SQLUser', 'MR_Diagnos': 'SQLUser', 'MR_Allergy': 'SQLUser',
    'MR_Procedures': 'SQLUser', 'MR_DrgOrd': 'SQLUser',
    'OE_Order': 'SQLUser', 'OE_OrdItem': 'SQLUser', 'OE_OrdExec': 'SQLUser',
    'LB_Episode': 'SQLUser', 'LB_TestSet': 'SQLUser', 'LB_TestSetItem': 'SQLUser',
    'PHC_DrgForm': 'SQLUser', 'PHC_AdministrationRoute': 'SQLUser',
    'ORC_Operation': 'SQLUser', 'OR_Anaesthesia': 'SQLUser',
    'RB_Appointment': 'SQLUser', 'RB_Resource': 'SQLUser',
    'ARC_ItmMast': 'SQLUser', 'ARC_ItemCat': 'SQLUser',
    'CT_Loc': 'SQLUser', 'CT_CareProv': 'SQLUser', 'CT_CarSpc': 'SQLUser',
    'CT_Nation': 'SQLUser', 'CT_Marital': 'SQLUser', 'CT_Hospital': 'SQLUser',
    'SS_User': 'SQLUser', 'SS_UserDefWindow': 'SQLUser',
    'INC_Itm': 'SQLUser', 'INC_ItmLoc': 'SQLUser',
    'QTCEEVRIEST': 'questionnaire', 'QTCERIESGO': 'questionnaire',
    'QCLXXMDI': 'questionnaire', 'QCLXXEVARC': 'questionnaire',
    'QGXXXISS': 'questionnaire',
}

SQL_EXAMPLES = {
    'PA_PatMas': """-- Datos maestros de pacientes
SELECT TOP 20 
  p.PAPMI_RowId, p.PAPMI_No AS ficha,
  p.PAPMI_Name AS apellidos, p.PAPMI_Name2 AS nombres,
  p.PAPMI_DOB AS fecha_nac
FROM SQLUser.PA_PatMas p
ORDER BY p.PAPMI_RowId DESC""",

    'PA_Adm': """-- Episodios de admisión
SELECT TOP 20
  a.PAADM_RowId, a.PAADM_AdmNo AS num_admision,
  a.PAADM_Type AS tipo, a.PAADM_AdmDate AS fecha_adm,
  a.PAADM_DischgDate AS fecha_alta
FROM SQLUser.PA_Adm a
ORDER BY a.PAADM_AdmDate DESC""",

    'MR_Diagnos': """-- Diagnósticos CIE-10
SELECT TOP 20
  d.MRDIA_RowId, d.MRDIA_Date AS fecha,
  d.MRDIA_ICDCode_DR AS cod_cie10_id
FROM SQLUser.MR_Diagnos d
ORDER BY d.MRDIA_Date DESC""",

    'OE_OrdItem': """-- Items de órdenes médicas
SELECT TOP 20
  oi.OEOrdItem_RowId, oi.OEOrdItem_Desc AS descripcion,
  oi.OEOrdItem_Status AS estado, oi.OEOrdItem_Date AS fecha
FROM SQLUser.OE_OrdItem oi
ORDER BY oi.OEOrdItem_Date DESC""",

    'LB_Episode': """-- Episodios de laboratorio
SELECT TOP 20
  lb.LBEpi_RowId, lb.LBEpi_EpisodeNo AS num_episodio,
  lb.LBEpi_Date AS fecha
FROM SQLUser.LB_Episode lb
ORDER BY lb.LBEpi_Date DESC""",

    'LB_TestSetItem': """-- Resultados de laboratorio
SELECT TOP 20
  tsi.LBTSItem_RowId, tsi.LBTSItem_TestCode AS cod_examen,
  tsi.LBTSItem_Result AS resultado, tsi.LBTSItem_Units AS unidades
FROM SQLUser.LB_TestSetItem tsi
ORDER BY tsi.LBTSItem_RowId DESC""",

    'RB_Appointment': """-- Citas agendadas
SELECT TOP 20
  a.RBApp_RowId, a.RBApp_Date AS fecha,
  a.RBApp_Time AS hora, a.RBApp_Status AS estado
FROM SQLUser.RB_Appointment a
ORDER BY a.RBApp_Date DESC""",

    'ORC_Operation': """-- Operaciones quirúrgicas
SELECT TOP 20
  op.OPER_RowId, op.OPER_Desc AS procedimiento,
  op.OPER_Date AS fecha
FROM SQLUser.ORC_Operation op
ORDER BY op.OPER_Date DESC""",

    'CT_Loc': """-- Ubicaciones/servicios del hospital
SELECT TOP 20
  l.CTLOC_RowId, l.CTLOC_Code AS codigo,
  l.CTLOC_Desc AS descripcion, l.CTLOC_Active AS activo
FROM SQLUser.CT_Loc l
WHERE l.CTLOC_Active = 'Y'""",

    'ARC_ItmMast': """-- Maestro de ítems facturables
SELECT TOP 20
  im.ARCIMDesc AS descripcion, im.ARCIMCode AS codigo
FROM SQLUser.ARC_ItmMast im
WHERE im.ARCIMActive = 'Y'""",

    'QTCEEVRIEST': """-- Caprini/ETE (questionnaire)
SELECT TOP 20
  Q.QUESDate, Q.QUESScore,
  Pat.PAPMI_No AS ficha
FROM questionnaire.QTCEEVRIEST Q
JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
ORDER BY Q.QUESDate DESC""",

    'QTCERIESGO': """-- Riesgo-Dependencia (questionnaire)
SELECT TOP 20
  Q.QUESDate, Q.QUESScore,
  Pat.PAPMI_No AS ficha
FROM questionnaire.QTCERIESGO Q
JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
ORDER BY Q.QUESDate DESC""",

    'QCLXXMDI': """-- Dispositivos Invasivos (questionnaire)
SELECT TOP 20
  Q.QUESDate, Q.QUESScore,
  Pat.PAPMI_No AS ficha
FROM questionnaire.QCLXXMDI Q
JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
ORDER BY Q.QUESDate DESC""",

    'MR_Allergy': """-- Alergias registradas
SELECT TOP 20
  a.ALG_RowId, a.ALG_Desc AS alergia,
  a.ALG_Status AS estado, a.ALG_Date AS fecha
FROM SQLUser.MR_Allergy a
ORDER BY a.ALG_Date DESC""",
}

L = []
def p(s=""): L.append(s)

conn_iris = conectar_alma()
cur = conn_iris.cursor()
conn_local = sqlite3.connect(DB)
c = conn_local.cursor()

# ============================================================
# 1. LIGHTWEIGHT CHECK: SELECT TOP 1 1 (has data yes/no)
# ============================================================
p("=" * 60)
p("PHASE 3: LIGHTWEIGHT TABLE PROFILING")
p("Strategy: SELECT TOP 1 1 (instant, no full scan)")
p("=" * 60)

has_data = {}
for table, schema in KEY_TABLES.items():
    try:
        cur.execute(f"SELECT TOP 1 1 FROM {schema}.{table}")
        row = cur.fetchone()
        has_data[table] = row is not None
        status = "✅ DATOS" if row else "⚫ VACÍA"
        p(f"  {status}  {schema}.{table}")
    except Exception as e:
        has_data[table] = None
        p(f"  ❌ ERROR  {schema}.{table}: {str(e)[:50]}")
    time.sleep(0.5)  # no saturar

with_data = sum(1 for v in has_data.values() if v is True)
empty = sum(1 for v in has_data.values() if v is False)
errors = sum(1 for v in has_data.values() if v is None)
p(f"\nResultado: {with_data} con datos, {empty} vacías, {errors} errores")

# ============================================================
# 2. UPDATE DICTIONARY (only empty fields)
# ============================================================
p("\n" + "=" * 60)
p("UPDATING DICTIONARY")
p("=" * 60)

c.execute("SELECT id, nombre FROM tablas")
table_ids = {name: tid for tid, name in c.fetchall()}

# Update uso_clinico
for table, estado in has_data.items():
    tid = table_ids.get(table)
    if tid and estado is not None:
        label = "Tabla con datos en producción" if estado else "Tabla vacía en producción"
        c.execute("""UPDATE tablas SET uso_clinico = ?
                    WHERE id = ? AND (uso_clinico IS NULL OR uso_clinico = '')""",
                  (label, tid))

# Update SQL examples
sql_added = 0
for table, sql in SQL_EXAMPLES.items():
    tid = table_ids.get(table)
    if tid:
        c.execute("""UPDATE tablas SET ejemplo_sql = ?
                    WHERE id = ? AND (ejemplo_sql IS NULL OR ejemplo_sql = '')""",
                  (sql, tid))
        if c.rowcount > 0:
            sql_added += 1
            p(f"  📝 {table}: SQL example added")
        else:
            p(f"  ⏭️  {table}: already has SQL")

conn_local.commit()
p(f"\nSQL examples added: {sql_added}")

# ============================================================
# 3. FINAL STATS
# ============================================================
p("\n" + "=" * 60)
p("FINAL STATS")
p("=" * 60)
c.execute("SELECT COUNT(*) FROM tablas")
total = c.fetchone()[0]
for field, label in [
    ('descripcion', 'Desc EN'), ('descripcion_es', 'Desc ES'),
    ('ejemplo_sql', 'SQL Example'), ('uso_clinico', 'Uso clínico')
]:
    c.execute(f"SELECT COUNT(*) FROM tablas WHERE {field} IS NOT NULL AND {field} != ''")
    n = c.fetchone()[0]
    p(f"  {label:15} {n:>6}/{total} ({100*n/total:.1f}%)")

c.execute("SELECT COUNT(*) FROM columnas WHERE descripcion IS NOT NULL AND descripcion != ''")
cd = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM columnas")
ct = c.fetchone()[0]
p(f"  {'Col Desc':15} {cd:>6}/{ct} ({100*cd/ct:.1f}%)")

cur.close()
conn_iris.close()
conn_local.close()

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("\n".join(L))
print(f"Done — {len(L)} lines")
