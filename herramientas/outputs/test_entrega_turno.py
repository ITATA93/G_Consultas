"""Test Q11-Q14: Fallecidos, Operados turno, Interconsultas, Plan tto"""
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from herramientas.python.db_config import conectar_alma

def run(conn, name, sql):
    print(f"\n{'='*70}")
    print(f"TEST: {name}")
    print('='*70)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        cols = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        print(f"Cols: {len(cols)} | Filas: {len(rows)}")
        hdr = " | ".join(f"{c:28s}" for c in cols[:8])
        print(hdr)
        print("-" * min(len(hdr), 200))
        for row in rows[:12]:
            vals = [f"{str(v if v is not None else ''):28s}" for v in row[:8]]
            print(" | ".join(vals))
        if len(rows) > 12:
            print(f"  ... ({len(rows) - 12} filas mas)")
        cursor.close()
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

conn = conectar_alma()

# Q11: FALLECIDOS (altas con condicion=Fallecido, DeadFlag='D')
run(conn, "Q11: FALLECIDOS (DischCond_DR = 1 = Fallecido)", """
SELECT TOP 100
    DATEADD('dd', adm.PAADM_DischgDate, '1840-12-31') AS F_DEFUNCION,
    adm.PAADM_DischgTime AS HORA,
    pm.PAPMI_Name AS PACIENTE,
    pm.PAPMI_ID AS RUT,
    DATEDIFF('yy', DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'), CURRENT_DATE) AS EDAD,
    ward.CTLOC_Code AS SERVICIO,
    doc.CTPCP_Desc AS MEDICO,
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC) AS DX
FROM SQLUser.PA_Adm adm
INNER JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
LEFT JOIN SQLUser.CT_Loc ward ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
LEFT JOIN SQLUser.CT_CareProv doc ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId
WHERE adm.PAADM_Type = 'I'
AND adm.PAADM_DischCond_DR = 1
AND adm.PAADM_DischgDate >= (DATEDIFF('dd', '1840-12-31', CURRENT_DATE) - 30)
ORDER BY adm.PAADM_DischgDate DESC
""")

# Q12: OPERADOS EN EL TURNO (programados el mismo dia o 8h antes) 
# via MR_Procedures (mas confiable, tiene datos) + admison del mismo dia
run(conn, "Q12: OPERADOS HOY (MR_Procedures fecha = hoy)", """
SELECT TOP 100
    DATEADD('dd', p.PROC_ProcDate, '1840-12-31') AS FECHA_CX,
    p.PROC_TimeStart AS HORA_INICIO,
    p.PROC_TimeEnd AS HORA_FIN,
    oper.OPER_Desc AS PROCEDIMIENTO,
    oper.OPER_Code AS COD_PROC,
    pm.PAPMI_Name AS PACIENTE,
    pm.PAPMI_ID AS RUT,
    adm.PAADM_Type AS ORIGEN
FROM SQLUser.MR_Procedures p
INNER JOIN SQLUser.MR_Adm mradm ON p.PROC_ParRef = mradm.MRADM_RowId
INNER JOIN SQLUser.PA_Adm adm ON mradm.MRADM_ADM_DR = adm.PAADM_RowID
INNER JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
LEFT JOIN SQLUser.ORC_Operation oper ON p.PROC_Operation_DR = oper.OPER_RowId
WHERE p.PROC_ProcDate = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)
ORDER BY p.PROC_TimeStart
""")

# Q13: INTERCONSULTAS EJECUTADAS EN EL TURNO (Categ=6)
run(conn, "Q13: INTERCONSULTAS ejecutadas hoy", """
SELECT TOP 100
    DATEADD('dd', oi.OEORI_DateExecuted, '1840-12-31') AS F_EJECUTADA,
    pm.PAPMI_Name AS PACIENTE,
    pm.PAPMI_ID AS RUT,
    ward.CTLOC_Code AS SERVICIO,
    oi.OEORI_Categ_DR AS CATEGORIA,
    oi.OEORI_ItmMast_DR AS COD_ITEM,
    oi.OEORI_BillDesc AS DESCRIPCION,
    doc.CTPCP_Desc AS MEDICO_SOLICITANTE
FROM SQLUser.OE_OrdItem oi
INNER JOIN SQLUser.OE_Order ord ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
INNER JOIN SQLUser.PA_Adm adm ON ord.OEORD_Adm_DR = adm.PAADM_RowID
INNER JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
LEFT JOIN SQLUser.CT_Loc ward ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
LEFT JOIN SQLUser.CT_CareProv doc ON ord.OEORD_Doctor_DR = doc.CTPCP_RowId
WHERE oi.OEORI_Categ_DR = 6
AND oi.OEORI_ItemStat_DR = 12
AND adm.PAADM_Type = 'I'
AND oi.OEORI_DateExecuted = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)
ORDER BY oi.OEORI_DateExecuted DESC
""")

# Q14: PLAN DE TRATAMIENTO (QTCEPLANTC via QUESPAAdmDR)
run(conn, "Q14: Plan de Tratamiento Consensuado", """
SELECT TOP 10
    plan.QUESDate AS FECHA_PLAN,
    plan.QUESPAAdmDR AS ADM_ID,
    plan.QUESTextResultDR AS TEXT_RESULT,
    pm.PAPMI_Name AS PACIENTE
FROM SQLUser.QTCEPLANTC plan
INNER JOIN SQLUser.PA_Adm adm ON plan.QUESPAAdmDR = adm.PAADM_RowID
INNER JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
WHERE adm.PAADM_Type = 'I'
AND adm.PAADM_VisitStatus = 'A'
AND adm.PAADM_DischgDate IS NULL
ORDER BY plan.QUESDate DESC
""")

conn.close()
print("\n\nALL DONE")
