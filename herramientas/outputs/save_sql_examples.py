"""
Save SQL examples to dictionary — LOCAL ONLY, no server queries.
"""
import sqlite3

DB = r"C:\_Repositorio\AG_Proyectos\AG_Consultas\Diccionario_Datos\diccionario.db"

SQL_EXAMPLES = {
    'PA_PatMas': "-- Datos maestros de pacientes\nSELECT TOP 20 p.PAPMI_RowId, p.PAPMI_No AS ficha, p.PAPMI_Name AS apellidos, p.PAPMI_Name2 AS nombres, p.PAPMI_DOB AS fecha_nac\nFROM SQLUser.PA_PatMas p\nORDER BY p.PAPMI_RowId DESC",
    'PA_Adm': "-- Episodios de admisión\nSELECT TOP 20 a.PAADM_RowId, a.PAADM_AdmNo AS num_admision, a.PAADM_Type AS tipo, a.PAADM_AdmDate AS fecha_adm, a.PAADM_DischgDate AS fecha_alta\nFROM SQLUser.PA_Adm a\nORDER BY a.PAADM_AdmDate DESC",
    'MR_Diagnos': "-- Diagnósticos CIE-10\nSELECT TOP 20 d.MRDIA_RowId, d.MRDIA_Date AS fecha, d.MRDIA_ICDCode_DR AS cod_cie10_id\nFROM SQLUser.MR_Diagnos d\nORDER BY d.MRDIA_Date DESC",
    'OE_OrdItem': "-- Items de órdenes médicas\nSELECT TOP 20 oi.OEOrdItem_RowId, oi.OEOrdItem_Desc AS descripcion, oi.OEOrdItem_Status AS estado, oi.OEOrdItem_Date AS fecha\nFROM SQLUser.OE_OrdItem oi\nORDER BY oi.OEOrdItem_Date DESC",
    'LB_Episode': "-- Episodios de laboratorio\nSELECT TOP 20 lb.LBEpi_RowId, lb.LBEpi_EpisodeNo AS num_episodio, lb.LBEpi_Date AS fecha\nFROM SQLUser.LB_Episode lb\nORDER BY lb.LBEpi_Date DESC",
    'LB_TestSetItem': "-- Resultados de laboratorio\nSELECT TOP 20 tsi.LBTSItem_RowId, tsi.LBTSItem_TestCode AS cod_examen, tsi.LBTSItem_Result AS resultado, tsi.LBTSItem_Units AS unidades\nFROM SQLUser.LB_TestSetItem tsi\nORDER BY tsi.LBTSItem_RowId DESC",
    'RB_Appointment': "-- Citas agendadas\nSELECT TOP 20 a.RBApp_RowId, a.RBApp_Date AS fecha, a.RBApp_Time AS hora, a.RBApp_Status AS estado\nFROM SQLUser.RB_Appointment a\nORDER BY a.RBApp_Date DESC",
    'ORC_Operation': "-- Operaciones quirúrgicas\nSELECT TOP 20 op.OPER_RowId, op.OPER_Desc AS procedimiento, op.OPER_Date AS fecha\nFROM SQLUser.ORC_Operation op\nORDER BY op.OPER_Date DESC",
    'CT_Loc': "-- Ubicaciones/servicios del hospital\nSELECT TOP 20 l.CTLOC_RowId, l.CTLOC_Code AS codigo, l.CTLOC_Desc AS descripcion, l.CTLOC_Active AS activo\nFROM SQLUser.CT_Loc l\nWHERE l.CTLOC_Active = 'Y'",
    'ARC_ItmMast': "-- Maestro de ítems facturables\nSELECT TOP 20 im.ARCIMDesc AS descripcion, im.ARCIMCode AS codigo\nFROM SQLUser.ARC_ItmMast im\nWHERE im.ARCIMActive = 'Y'",
    'QTCEEVRIEST': "-- Caprini/ETE (questionnaire)\nSELECT TOP 20 Q.QUESDate, Q.QUESScore, Pat.PAPMI_No AS ficha\nFROM questionnaire.QTCEEVRIEST Q\nJOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId\nJOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId\nORDER BY Q.QUESDate DESC",
    'QTCERIESGO': "-- Riesgo-Dependencia (questionnaire)\nSELECT TOP 20 Q.QUESDate, Q.QUESScore, Pat.PAPMI_No AS ficha\nFROM questionnaire.QTCERIESGO Q\nJOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId\nJOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId\nORDER BY Q.QUESDate DESC",
    'QCLXXMDI': "-- Dispositivos Invasivos (questionnaire)\nSELECT TOP 20 Q.QUESDate, Q.QUESScore, Pat.PAPMI_No AS ficha\nFROM questionnaire.QCLXXMDI Q\nJOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId\nJOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId\nORDER BY Q.QUESDate DESC",
    'MR_Allergy': "-- Alergias registradas\nSELECT TOP 20 a.ALG_RowId, a.ALG_Desc AS alergia, a.ALG_Status AS estado, a.ALG_Date AS fecha\nFROM SQLUser.MR_Allergy a\nORDER BY a.ALG_Date DESC",
}

conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute("SELECT id, nombre FROM tablas")
table_ids = {name: tid for tid, name in c.fetchall()}

added = 0
for table, sql in SQL_EXAMPLES.items():
    tid = table_ids.get(table)
    if tid:
        c.execute("UPDATE tablas SET ejemplo_sql = ? WHERE id = ? AND (ejemplo_sql IS NULL OR ejemplo_sql = '')", (sql, tid))
        if c.rowcount > 0:
            added += 1
            print(f"  + {table}")
        else:
            print(f"  = {table} (ya tenía)")

conn.commit()
c.execute("SELECT COUNT(*) FROM tablas WHERE ejemplo_sql IS NOT NULL AND ejemplo_sql != ''")
total_sql = c.fetchone()[0]
print(f"\nAgregados: {added} | Total con SQL: {total_sql}/11653")
conn.close()
