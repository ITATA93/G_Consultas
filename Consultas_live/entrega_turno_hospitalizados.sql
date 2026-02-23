-- ============================================================================
-- ENTREGA DE TURNO - Pacientes Hospitalizados Actualmente
-- Hospital Dr. Antonio Tirado Lanas - Ovalle
-- ============================================================================
-- Fuente: ALMA/TrakCare (InterSystems IRIS - LIVE-CLOV)
-- Autor: Equipo de Informatica Hospitalaria
-- Fecha: 2026-02-16
-- Uso: Entrega de turno medica y multidisciplinaria
-- Basado en formato Excel ENTREGA.xlsx (32 hojas: MQ1-MQ3, UTIs, UCI, etc.)
-- 
-- NOTA TECNICA:
--   - Fechas IRIS = formato Mumps horolog ($H): dias desde 1840-12-31
--   - Convertir con: DATEADD('dd', campo_fecha, '1840-12-31')
--   - DATEDIFF usa comillas: DATEDIFF('dd', fecha1, fecha2)
--   - Enlace Diagnosticos: PA_Adm -> MR_Adm -> MR_Diagnos
--   - Enlace Procedimientos: MR_Procedures -> MR_Adm -> PA_Adm
--   - Enlace Ordenes: OE_OrdItem -> OE_Order -> PA_Adm
--   - Unidad del censo = EPISODIO (PA_Adm). 1 fila por episodio.
--   - Diagnosticos se traen como scalar subquery (evita duplicados).
--
-- QUERIES:
--   Q1: Censo completo       Q8:  Cirugias/Procedimientos
--   Q2: Diagnosticos         Q9:  Ordenes pendientes
--   Q3: Resumen por servicio Q10: Ingresos del dia
--   Q4: Por medico           Q11: Fallecidos del dia
--   Q5: Urgencia             Q12: Operados en el turno
--   Q6: Altas del dia        Q13: Interconsultas internas
--   Q7: Filtro por servicio  Q14: Endoscopias pendientes
--   Q15: Enfermería completa Q16: Enfermería por servicio
--   Q17: Escala Caídas        Q18: Riesgo Dependencia
--   Q19: Dispositivos Invasivos
--
-- SEGURIDAD: Solo SELECT con TOP. No modifica datos.
-- VALIDADO: 2026-02-16 contra ALMA/IRIS en produccion.
-- ============================================================================


-- ============================================================================
-- QUERY 1: CENSO COMPLETO DE HOSPITALIZADOS
-- Un episodio (PA_Adm) = una fila. Sin duplicados.
-- Columnas del Excel: SALA | NOMBRE | CIRUJAN@ | RUT | EDAD | F.INGRESO |
--   F.P.ALTA | DH | DIAG.QUIRURGICO + datos extra de BD.
-- ============================================================================

SELECT TOP 500
    -- === COL A: SALA (servicio + cama) ===
    ward.CTLOC_Code                                             AS SERVICIO,
    ward.CTLOC_Desc                                             AS DESC_SERVICIO,
    adm.PAADM_CurrentRoom_DR                                    AS SALA,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    
    -- === COL B: NOMBRE ===
    pm.PAPMI_Name                                               AS NOMBRE_PACIENTE,
    
    -- === COL C: CIRUJAN@ / MEDICO TRATANTE ===
    doc_adm.CTPCP_Desc                                          AS MEDICO_TRATANTE,
    doc_adm.CTPCP_Code                                          AS COD_MEDICO,
    
    -- === COL D: RUT ===
    pm.PAPMI_ID                                                 AS RUT,
    pm.PAPMI_No                                                 AS NRO_FICHA,
    
    -- === COL E: EDAD ===
    DATEADD('dd', pm.PAPMI_DOB, '1840-12-31')                   AS FECHA_NACIMIENTO,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    sx.CTSEX_Desc                                               AS SEXO,
    
    -- === COL F: F. INGRESO ===
    DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31')              AS F_INGRESO,
    adm.PAADM_AdmTime                                           AS HORA_INGRESO,
    
    -- === COL G: F. PROBABLE ALTA ===
    DATEADD('dd', adm.PAADM_EstimDischargeDate, '1840-12-31')   AS F_PROBABLE_ALTA,
    adm.PAADM_EstDischConfirmed                                 AS ALTA_CONFIRMADA,
    
    -- === COL H: DH (Dias Hospitalizacion) ===
    DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE)                                           AS DIAS_HOSPITALIZACION,
    
    -- === COL I: DIAGNOSTICO PRINCIPAL (scalar subquery, sin duplicados) ===
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_PRINCIPAL,
    
    -- === DATOS ADICIONALES ===
    
    -- Tipo de admision y estado
    adm.PAADM_Type                                              AS TIPO_ADMISION,
    adm.PAADM_VisitStatus                                       AS ESTADO_VISITA,
    
    -- Alta medica
    DATEADD('dd', adm.PAADM_MedDischDate, '1840-12-31')         AS F_ALTA_MEDICA,
    adm.PAADM_MedicalDischarge                                  AS ALTA_MEDICA_FLAG,
    
    -- Datos adicionales del paciente
    pm.PAPMI_Allergy                                            AS ALERGIAS,
    pm.PAPMI_VIPFlag                                            AS VIP,
    pm.PAPMI_MobPhone                                           AS TELEFONO,
    
    -- Medico de referencia interna
    doc_ref.CTPCP_Desc                                          AS MEDICO_REFERENCIA,
    
    -- Ward padre (MQ1 -> Cirugia, etc.)
    parent.CTLOC_Code                                           AS SERVICIO_PADRE,
    parent.CTLOC_Desc                                           AS DESC_SERVICIO_PADRE,
    
    -- ID episodio
    adm.PAADM_RowID                                             AS ID_EPISODIO

FROM 
    SQLUser.PA_Adm adm

    -- Datos maestros paciente
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId

    -- Sexo
    LEFT JOIN SQLUser.CT_Sex sx 
        ON pm.PAPMI_Sex_DR = sx.CTSEX_RowId

    -- Servicio/Ward actual
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID

    -- Ward padre
    LEFT JOIN SQLUser.CT_Loc parent
        ON adm.PAADM_ParentWard_DR = parent.CTLOC_RowID

    -- Medico que admitio (= "Cirujano" en el Excel)
    LEFT JOIN SQLUser.CT_CareProv doc_adm 
        ON adm.PAADM_AdmDocCodeDR = doc_adm.CTPCP_RowId

    -- Medico referencia interna
    LEFT JOIN SQLUser.CT_CareProv doc_ref 
        ON adm.PAADM_InternalRefDoc_DR = doc_ref.CTPCP_RowId

WHERE
    -- Solo hospitalizados activos sin alta
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    
ORDER BY 
    ward.CTLOC_Code,
    adm.PAADM_CurrentRoom_DR,
    adm.PAADM_CurrentBed_DR
;


-- ============================================================================
-- QUERY 2: TODOS LOS DIAGNOSTICOS POR PACIENTE HOSPITALIZADO
-- Detalle completo: lista todos los Dx de cada episodio activo.
-- Usar junto con Q1 para ver el detalle de diagnosticos.
-- ============================================================================

SELECT TOP 1000
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_No                                                 AS FICHA,
    pm.PAPMI_Name                                               AS PACIENTE,
    
    -- Diagnostico
    diag.MRDIA_Prefix                                           AS TIPO_DX,
    diag.MRDIA_Desc                                             AS DIAGNOSTICO,
    diag.MRDIA_ICDCode_DR                                       AS COD_CIE,
    DATEADD('dd', diag.MRDIA_Date, '1840-12-31')                AS FECHA_DX,
    DATEADD('dd', diag.MRDIA_OnsetDate, '1840-12-31')           AS FECHA_INICIO,
    diag.MRDIA_Active                                           AS ACTIVO,
    diag.MRDIA_Suspicion                                        AS SOSPECHA

FROM 
    SQLUser.PA_Adm adm
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    INNER JOIN SQLUser.MR_Adm mradm 
        ON adm.PAADM_RowID = mradm.MRADM_ADM_DR
    INNER JOIN SQLUser.MR_Diagnos diag 
        ON mradm.MRADM_RowId = diag.MRDIA_MRADM_ParRef

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL

ORDER BY 
    ward.CTLOC_Code,
    adm.PAADM_CurrentBed_DR,
    diag.MRDIA_Prefix,
    diag.MRDIA_Date DESC
;


-- ============================================================================
-- QUERY 3: RESUMEN POR SERVICIO (hoja DIST del Excel)
-- ============================================================================

SELECT TOP 50
    ward.CTLOC_Code                                             AS COD_SERVICIO,
    ward.CTLOC_Desc                                             AS SERVICIO,
    COUNT(*)                                                    AS TOTAL_PACIENTES,
    AVG(DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE))                                          AS PROM_DIAS_ESTADIA,
    MAX(DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE))                                          AS MAX_DIAS_ESTADIA,
    DATEADD('dd', MIN(adm.PAADM_AdmDate), '1840-12-31')        AS INGRESO_MAS_ANTIGUO,
    DATEADD('dd', MAX(adm.PAADM_AdmDate), '1840-12-31')        AS INGRESO_MAS_RECIENTE

FROM 
    SQLUser.PA_Adm adm
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL

GROUP BY 
    ward.CTLOC_Code, ward.CTLOC_Desc

ORDER BY 
    TOTAL_PACIENTES DESC
;


-- ============================================================================
-- QUERY 4: DISTRIBUCION POR MEDICO (hoja CIRUJANO del Excel)
-- ============================================================================

SELECT TOP 100
    doc.CTPCP_Desc                                              AS MEDICO,
    doc.CTPCP_Code                                              AS COD_MEDICO,
    COUNT(*)                                                    AS TOTAL_PACIENTES,
    AVG(DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE))                                          AS PROM_DIAS,
    LIST(DISTINCT ward.CTLOC_Code)                              AS SERVICIOS

FROM 
    SQLUser.PA_Adm adm
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL

GROUP BY 
    doc.CTPCP_Desc, doc.CTPCP_Code

ORDER BY 
    TOTAL_PACIENTES DESC
;


-- ============================================================================
-- QUERY 5: PACIENTES EN URGENCIA (hoja URG del Excel)
-- ============================================================================

SELECT TOP 200
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS UBICACION,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    sx.CTSEX_Desc                                               AS SEXO,
    DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31')              AS F_INGRESO,
    adm.PAADM_AdmTime                                           AS HORA,
    DATEDIFF('hh',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE)                                           AS HORAS_EN_URG,
    doc.CTPCP_Desc                                              AS MEDICO,
    adm.PAADM_EmergencyStatus                                   AS ESTADO_URGENCIA,
    DATEADD('dd', adm.PAADM_TriageDate, '1840-12-31')           AS F_TRIAGE,
    adm.PAADM_LikelihoodAdmit                                   AS PROB_INGRESO,
    DATEADD('dd', adm.PAADM_InpatBedReqDate, '1840-12-31')      AS F_SOLICITUD_CAMA,
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_PRINCIPAL

FROM 
    SQLUser.PA_Adm adm
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Sex sx 
        ON pm.PAPMI_Sex_DR = sx.CTSEX_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    adm.PAADM_Type = 'E'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL

ORDER BY 
    adm.PAADM_AdmDate, adm.PAADM_AdmTime
;


-- ============================================================================
-- QUERY 6: ALTAS DEL DIA (hoja ALTAS del Excel)
-- ============================================================================

SELECT TOP 200
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31')              AS F_INGRESO,
    DATEADD('dd', adm.PAADM_DischgDate, '1840-12-31')           AS F_ALTA,
    adm.PAADM_DischgTime                                        AS H_ALTA,
    DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        DATEADD('dd', adm.PAADM_DischgDate, '1840-12-31'))      AS DIAS_ESTADIA,
    doc.CTPCP_Desc                                              AS MEDICO,
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_PRINCIPAL,
    adm.PAADM_DischComments                                     AS COMENTARIOS_ALTA

FROM 
    SQLUser.PA_Adm adm
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_DischgDate = 
        DATEDIFF('dd', '1840-12-31', CURRENT_DATE)              -- HOY en formato Mumps
    
ORDER BY 
    ward.CTLOC_Code, adm.PAADM_DischgTime DESC
;


-- ============================================================================
-- QUERY 7: FILTRO POR SERVICIO ESPECIFICO
-- Codigos verificados contra BD (ver Query 3 para lista completa):
--   1234TEST         = Medicina General HOV
--   CARD-HOV_105102  = Cardiologia Adulto HDATL
--   GINE-HOV_105102  = Ginecologia Adulto HDATL
--   ANES-HOV_105102  = Anestesiologia HDATL
--   CIRA-HOV_105102  = Cirugia Adulto HDATL
--   CINI-HOV_105102  = Cirugia Infantil HDATL
--   CIBU-HOV_105102  = Cirugia Bucal HDATL
--   MAXI-HOV_105102  = Box Maxilo Facial-HOV
--   MAMA-HOV_105102  = Mastologia HDATL
--   PCER-HOV_105102  = Patologia Cervical HDATL
--   CIVA-HOV_105102  = Cirugia Vascular Periferica HDATL
--   GAI-HOV_105102   = Gastroenterologia Infantil HDATL
-- ============================================================================

SELECT TOP 200
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_Name                                               AS PACIENTE,
    doc.CTPCP_Desc                                              AS MEDICO,
    pm.PAPMI_ID                                                 AS RUT,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31')              AS F_INGRESO,
    DATEADD('dd', adm.PAADM_EstimDischargeDate, '1840-12-31')   AS F_PROB_ALTA,
    DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE)                                           AS DH,
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_PRINCIPAL,
    pm.PAPMI_Allergy                                            AS ALERGIAS,
    adm.PAADM_MedicalDischarge                                  AS ALTA_MEDICA

FROM 
    SQLUser.PA_Adm adm
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    -- >>> CAMBIAR SERVICIO AQUI <<<
    AND ward.CTLOC_Code = '1234TEST'

ORDER BY 
    adm.PAADM_CurrentBed_DR
;


-- ============================================================================
-- QUERY 8: CIRUGIAS / PROCEDIMIENTOS REALIZADOS DURANTE HOSPITALIZACION
-- Muestra que cirugias se hicieron a cada paciente activo hospitalizado.
-- Tabla: MR_Procedures (via MR_Adm), descripcion en ORC_Operation.
-- ============================================================================

SELECT TOP 500
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEADD('dd', p.PROC_ProcDate, '1840-12-31')                AS FECHA_PROCEDIMIENTO,
    oper.OPER_Desc                                              AS PROCEDIMIENTO,
    oper.OPER_Code                                              AS COD_PROCEDIMIENTO,
    p.PROC_ProcedureNotes                                       AS NOTA_PROC,
    doc.CTPCP_Desc                                              AS CIRUJANO

FROM 
    SQLUser.MR_Procedures p
    INNER JOIN SQLUser.MR_Adm mradm 
        ON p.PROC_ParRef = mradm.MRADM_RowId
    INNER JOIN SQLUser.PA_Adm adm 
        ON mradm.MRADM_ADM_DR = adm.PAADM_RowID
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.ORC_Operation oper 
        ON p.PROC_Operation_DR = oper.OPER_RowId
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL

ORDER BY 
    p.PROC_ProcDate DESC,
    ward.CTLOC_Code,
    pm.PAPMI_Name
;


-- ============================================================================
-- QUERY 9: ORDENES PENDIENTES POR PACIENTE HOSPITALIZADO
-- Examenes de laboratorio, imagenes, endoscopias pendientes.
-- Tabla: OE_OrdItem (via OE_Order -> PA_Adm)
-- NOTA: OEORI_ItemStat_DR es un FK al estado (3=pendiente, 12=completado, etc.)
-- ============================================================================

SELECT TOP 500
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEADD('dd', oi.OEORI_SttDat, '1840-12-31')                AS FECHA_ORDEN,
    oi.OEORI_Categ_DR                                           AS COD_CATEGORIA,
    oi.OEORI_ItemStat_DR                                        AS COD_ESTADO,
    oi.OEORI_ItmMast_DR                                         AS COD_ITEM,
    oi.OEORI_BillDesc                                           AS DESC_FACTURACION

FROM 
    SQLUser.OE_OrdItem oi
    INNER JOIN SQLUser.OE_Order ord 
        ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
    INNER JOIN SQLUser.PA_Adm adm 
        ON ord.OEORD_Adm_DR = adm.PAADM_RowID
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    -- Solo ordenes no completadas (estado != 12)
    AND oi.OEORI_ItemStat_DR != 12

ORDER BY 
    oi.OEORI_SttDat DESC,
    ward.CTLOC_Code,
    pm.PAPMI_Name
;


-- ============================================================================
-- QUERY 10: INGRESOS DEL DIA
-- Pacientes que ingresaron hoy (para la seccion INGRESOS del imprimible)
-- ============================================================================

SELECT TOP 100
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    sx.CTSEX_Desc                                               AS SEXO,
    adm.PAADM_AdmTime                                           AS HORA_INGRESO,
    doc.CTPCP_Desc                                              AS MEDICO,
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_INGRESO

FROM 
    SQLUser.PA_Adm adm
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Sex sx 
        ON pm.PAPMI_Sex_DR = sx.CTSEX_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_AdmDate = 
        DATEDIFF('dd', '1840-12-31', CURRENT_DATE)              -- HOY en Mumps

ORDER BY 
    adm.PAADM_AdmTime DESC,
    ward.CTLOC_Code
;


-- ============================================================================
-- QUERY 11: FALLECIDOS DEL DIA
-- Pacientes dentro de hospitalizacion con condicion de fallecido.
-- Fuente: PA_PatMas.PAPMI_Deceased='Y' + PAPMI_Deceased_Date
-- NOTA: El catalogo PAC_DischCondit tiene RowId=1=Fallecido(FA), 
--       pero ese campo no siempre se llena. PAPMI_Deceased es mas confiable.
-- ============================================================================

SELECT TOP 50
    DATEADD('dd', pm.PAPMI_Deceased_Date, '1840-12-31')         AS F_DEFUNCION,
    pm.PAPMI_DeceasedTime                                       AS HORA_DEFUNCION,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    sx.CTSEX_Desc                                               AS SEXO,
    ward.CTLOC_Code                                             AS SERVICIO,
    doc.CTPCP_Desc                                              AS MEDICO,
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_DEFUNCION

FROM 
    SQLUser.PA_PatMas pm
    INNER JOIN SQLUser.PA_Adm adm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Sex sx 
        ON pm.PAPMI_Sex_DR = sx.CTSEX_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    pm.PAPMI_Deceased = 'Y'
    AND adm.PAADM_Type = 'I'
    -- >>> FILTRO: fallecidos de HOY. Cambiar para otro dia <<<
    AND pm.PAPMI_Deceased_Date = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)

ORDER BY 
    pm.PAPMI_Deceased_Date DESC,
    ward.CTLOC_Code
;


-- ============================================================================
-- QUERY 12: OPERADOS EN EL TURNO / DIA
-- Pacientes operados HOY. Incluye TODOS los origenes (I=Hosp, E=Urg, O=Amb).
-- Fuente: MR_Procedures + ORC_Operation (descripcion del procedimiento)
-- Detecta "operados de turno" = admision y cirugia el mismo dia o <= 8 horas
-- ============================================================================

SELECT TOP 200
    DATEADD('dd', p.PROC_ProcDate, '1840-12-31')                AS FECHA_CX,
    p.PROC_TimeStart                                            AS HORA_INICIO,
    p.PROC_TimeEnd                                              AS HORA_FIN,
    oper.OPER_Desc                                              AS PROCEDIMIENTO,
    oper.OPER_Code                                              AS COD_PROCEDIMIENTO,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    DATEDIFF('yy',
        DATEADD('dd', pm.PAPMI_DOB, '1840-12-31'),
        CURRENT_DATE)                                           AS EDAD,
    adm.PAADM_Type                                              AS ORIGEN,
    -- Si admision = dia cirugia => operado de turno (no estaba en tabla)
    CASE 
        WHEN adm.PAADM_AdmDate = p.PROC_ProcDate THEN 'TURNO'
        ELSE 'PROGRAMADO'
    END                                                         AS TIPO_OPERADO,
    ward.CTLOC_Code                                             AS SERVICIO,
    doc.CTPCP_Desc                                              AS MEDICO

FROM 
    SQLUser.MR_Procedures p
    INNER JOIN SQLUser.MR_Adm mradm 
        ON p.PROC_ParRef = mradm.MRADM_RowId
    INNER JOIN SQLUser.PA_Adm adm 
        ON mradm.MRADM_ADM_DR = adm.PAADM_RowID
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.ORC_Operation oper 
        ON p.PROC_Operation_DR = oper.OPER_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

WHERE
    -- >>> Cirugia HOY <<<
    p.PROC_ProcDate = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)

ORDER BY 
    p.PROC_TimeStart,
    ward.CTLOC_Code,
    pm.PAPMI_Name
;


-- ============================================================================
-- QUERY 13: INTERCONSULTAS INTERNAS RESPONDIDAS / EJECUTADAS EN EL TURNO
-- Fuente: OE_OrdItem + ARC_ItmMast (descripcion del item)
-- Filtra items cuya descripcion contiene "INTERCONSULTA%INTERNA"
-- Estado 12 = respondida/ejecutada, Estado 3 = pendiente
-- ============================================================================

SELECT TOP 200
    DATEADD('dd', oi.OEORI_SttDat, '1840-12-31')                AS FECHA,
    oi.OEORI_ItemStat_DR                                        AS COD_ESTADO,
    CASE oi.OEORI_ItemStat_DR
        WHEN 12 THEN 'RESPONDIDA'
        WHEN 3  THEN 'PENDIENTE'
        ELSE 'OTRO (' || CAST(oi.OEORI_ItemStat_DR AS VARCHAR) || ')'
    END                                                         AS ESTADO,
    itm.ARCIM_Desc                                              AS INTERCONSULTA,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    ward.CTLOC_Code                                             AS SERVICIO,
    doc.CTPCP_Desc                                              AS MEDICO_SOLICITANTE

FROM 
    SQLUser.OE_OrdItem oi
    INNER JOIN SQLUser.ARC_ItmMast itm 
        ON oi.OEORI_ItmMast_DR = itm.ARCIM_RowId
    INNER JOIN SQLUser.OE_Order ord 
        ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
    INNER JOIN SQLUser.PA_Adm adm 
        ON ord.OEORD_Adm_DR = adm.PAADM_RowID
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc 
        ON ord.OEORD_Doctor_DR = doc.CTPCP_RowId

WHERE
    itm.ARCIM_Desc LIKE '%INTERCONSULTA%INTERNA%'
    AND adm.PAADM_Type = 'I'
    -- >>> FILTRO: interconsultas de HOY <<<
    AND oi.OEORI_SttDat = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)

ORDER BY 
    oi.OEORI_ItemStat_DR,
    itm.ARCIM_Desc,
    pm.PAPMI_Name
;


-- ============================================================================
-- QUERY 14: ENDOSCOPIAS PENDIENTES DE HOSPITALIZADOS
-- Fuente: OE_OrdItem + ARC_ItmMast filtrando items con "ENDOSCOP" 
-- Solo ordenes pendientes (estado != 12) de hospitalizados activos
-- ============================================================================

SELECT TOP 100
    DATEADD('dd', oi.OEORI_SttDat, '1840-12-31')                AS FECHA_ORDEN,
    itm.ARCIM_Desc                                              AS EXAMEN,
    oi.OEORI_ItemStat_DR                                        AS COD_ESTADO,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUT,
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA

FROM 
    SQLUser.OE_OrdItem oi
    INNER JOIN SQLUser.ARC_ItmMast itm 
        ON oi.OEORI_ItmMast_DR = itm.ARCIM_RowId
    INNER JOIN SQLUser.OE_Order ord 
        ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
    INNER JOIN SQLUser.PA_Adm adm 
        ON ord.OEORD_Adm_DR = adm.PAADM_RowID
    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID

WHERE
    itm.ARCIM_Desc LIKE '%ENDOSCOP%'
    AND adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    AND oi.OEORI_ItemStat_DR != 12

ORDER BY 
    oi.OEORI_SttDat DESC,
    ward.CTLOC_Code,
    pm.PAPMI_Name
;


-- ============================================================================
-- QUERY 15: ENTREGA DE ENFERMERIA - DATOS CLINICOS POR PACIENTE
-- Equivalente SQL del reporte ZEN: 
--   Region.CLXX.Reports.ZEN.Hospitalizado.EntregaTurnoHosp
-- Incluye: identificación, signos vitales, dispositivos, balance hídrico,
--          dieta, alergias, dolor, questionnaires de enfermería.
-- Tablas: PA_Adm + PA_PatMas + MR_Adm + MR_ClncData + MR_InputOutput
--         + questionnaire.QCLXXEVARC (caídas)
--         + questionnaire.QTCERIESGO (riesgo-dependencia)
--         + questionnaire.QGXXXISS (insulina)
--
-- NOTA: Los questionnaires son tablas SQL normales (esquema questionnaire.*).
--   Se unen via QUESPAAdmDR → PA_Adm.PAADM_RowId, igual que Caprini.
--   Campos clínicos: Q01..Qnn (cada tabla tiene su mapeo propio).
-- ============================================================================

SELECT TOP 500
    -- === IDENTIFICACIÓN (cols 0-8 del ZEN) ===
    adm.PAADM_RowID                                             AS ID_EPISODIO,
    adm.PAADM_Type                                              AS SUBTIPO_EPISODIO,
    adm.PAADM_VisitStatus                                       AS ESTADO_EPISODIO,
    ward.CTLOC_Desc                                             AS SERVICIO_CLINICO,
    ward.CTLOC_Code                                             AS COD_SERVICIO,
    adm.PAADM_CurrentRoom_DR                                    AS SALA,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_ID                                                 AS RUN_PACIENTE,
    pm.PAPMI_No                                                 AS NRO_FICHA,
    pm.PAPMI_Name                                               AS NOMBRE_PACIENTE,
    sx.CTSEX_Desc                                               AS SEXO,

    -- === DIAGNÓSTICOS CONFIRMADOS (col 9 del ZEN) ===
    (SELECT LIST(d.MRDIA_Desc, ';')
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
       AND d.MRDIA_Prefix = 'C'
    )                                                           AS DX_CONFIRMADOS,

    -- === DIAGNÓSTICO PREOPERATORIO (col 10) - procedimientos pendientes ===
    (SELECT TOP 1 d.MRDIA_Desc
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID
       AND d.MRDIA_Prefix = 'P'
     ORDER BY d.MRDIA_Date DESC
    )                                                           AS DX_PREOPERATORIO,

    -- === DISPOSITIVOS INVASIVOS (cols 16-20 del ZEN) ===
    -- DrainTubes en MR_Adm (campo de referencia)
    mradm.MRADM_DrainTubes_DR                                  AS DISPOSITIVO_INVASIVO_DR,

    -- === SIGNOS VITALES - últimos registrados (cols 24-31 del ZEN) ===
    -- Desde MR_ClncData (tabla de signos vitales clínicos)
    (SELECT TOP 1 v.MRCLN_PulseRate
     FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC
    )                                                           AS FRECUENCIA_CARDIACA,

    (SELECT TOP 1 v.MRCLN_BldPressSyst
     FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC
    )                                                           AS PA_SISTOLICA,

    (SELECT TOP 1 v.MRCLN_BldPressDias
     FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC
    )                                                           AS PA_DIASTOLICA,

    (SELECT TOP 1 v.MRCLN_RespirationRate
     FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC
    )                                                           AS FRECUENCIA_RESPIRATORIA,

    (SELECT TOP 1 v.MRCLN_BodyTemp
     FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC
    )                                                           AS TEMPERATURA,

    -- Saturación O2 y HGT desde MR_Adm (último valor registrado)
    mradm.MRADM_OxygenSaturation                               AS SAT_O2,
    mradm.MRADM_BloodSugarTestResult                           AS HGT,
    mradm.MRADM_PainScore                                      AS EVA_DOLOR,

    -- === BALANCE HIDRICO (cols 21, 41-44 del ZEN) ===
    -- Último registro de MR_InputOutput
    (SELECT TOP 1 io.INPOUT_UrineOutput
     FROM SQLUser.MR_InputOutput io
     WHERE io.INPOUT_ParRef = mradm.MRADM_RowId
     ORDER BY io.INPOUT_Date DESC, io.INPOUT_Time DESC
    )                                                           AS EGRESO_DIURESIS,

    (SELECT TOP 1 io.INPOUT_Drainage
     FROM SQLUser.MR_InputOutput io
     WHERE io.INPOUT_ParRef = mradm.MRADM_RowId
     ORDER BY io.INPOUT_Date DESC, io.INPOUT_Time DESC
    )                                                           AS EGRESO_DRENAJE,

    (SELECT TOP 1 io.INPOUT_IOBalance
     FROM SQLUser.MR_InputOutput io
     WHERE io.INPOUT_ParRef = mradm.MRADM_RowId
     ORDER BY io.INPOUT_Date DESC, io.INPOUT_Time DESC
    )                                                           AS BALANCE_HIDRICO,

    -- === DIETA / RÉGIMEN (col 47 del ZEN) ===
    mradm.MRADM_DietComments                                   AS REGIMEN,

    -- === ALERGIAS (col 40 del ZEN) ===
    pm.PAPMI_Allergy                                            AS ALERGIAS,

    -- === MEDICAMENTOS ACTIVOS (col 39 del ZEN) ===
    -- Lista concatenada de medicamentos con orden activa
    (SELECT LIST(oi.OEORI_BillDesc || ' ' || 
                 DATEADD('dd', oi.OEORI_SttDat, '1840-12-31'), ';')
     FROM SQLUser.OE_OrdItem oi
     INNER JOIN SQLUser.OE_Order ord ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
     WHERE ord.OEORD_Adm_DR = adm.PAADM_RowID
       AND oi.OEORI_ItemStat_DR NOT IN (12, 5)
       AND oi.OEORI_Categ_DR = 2
    )                                                           AS MEDICAMENTOS,

    -- === LABORATORIO PENDIENTE (col 22 del ZEN) ===
    (SELECT LIST(itm.ARCIM_Desc, ';')
     FROM SQLUser.OE_OrdItem oi
     INNER JOIN SQLUser.ARC_ItmMast itm ON oi.OEORI_ItmMast_DR = itm.ARCIM_RowId
     INNER JOIN SQLUser.OE_Order ord ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
     WHERE ord.OEORD_Adm_DR = adm.PAADM_RowID
       AND oi.OEORI_ItemStat_DR != 12
       AND oi.OEORI_Categ_DR = 1
    )                                                           AS LAB_PENDIENTES,

    -- === IMAGENOLOGÍA PENDIENTE (col 23 del ZEN) ===
    (SELECT LIST(itm.ARCIM_Desc, ';')
     FROM SQLUser.OE_OrdItem oi
     INNER JOIN SQLUser.ARC_ItmMast itm ON oi.OEORI_ItmMast_DR = itm.ARCIM_RowId
     INNER JOIN SQLUser.OE_Order ord ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
     WHERE ord.OEORD_Adm_DR = adm.PAADM_RowID
       AND oi.OEORI_ItemStat_DR != 12
       AND oi.OEORI_Categ_DR = 5
    )                                                           AS IMG_PENDIENTES,

    -- === INTERCONSULTAS INTERNAS PENDIENTES (col 38 del ZEN) ===
    (SELECT LIST(itm.ARCIM_Desc, ';')
     FROM SQLUser.OE_OrdItem oi
     INNER JOIN SQLUser.ARC_ItmMast itm ON oi.OEORI_ItmMast_DR = itm.ARCIM_RowId
     INNER JOIN SQLUser.OE_Order ord ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
     WHERE ord.OEORD_Adm_DR = adm.PAADM_RowID
       AND itm.ARCIM_Desc LIKE '%INTERCONSULTA%INTERNA%'
       AND oi.OEORI_ItemStat_DR != 12
    )                                                           AS IC_INTERNAS_PENDIENTES,

    -- === ESCALA RIESGO DE CAIDAS - questionnaire.QCLXXEVARC (col 36 ZEN) ===
    -- Última evaluación de caídas del episodio
    (SELECT TOP 1 rc.Q01
     FROM questionnaire.QCLXXEVARC rc
     WHERE rc.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rc.QUESDate DESC, rc.QUESTime DESC
    )                                                           AS CAIDAS_FACTORES,
    (SELECT TOP 1 rc.QUESScore
     FROM questionnaire.QCLXXEVARC rc
     WHERE rc.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rc.QUESDate DESC, rc.QUESTime DESC
    )                                                           AS CAIDAS_SCORE,

    -- === RIESGO DEPENDENCIA - questionnaire.QTCERIESGO (cols 34-35 ZEN) ===
    -- Última categorización riesgo-dependencia
    (SELECT TOP 1 rd.Q17
     FROM questionnaire.QTCERIESGO rd
     WHERE rd.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rd.QUESDate DESC, rd.QUESTime DESC
    )                                                           AS RESULTADO_RIESGO,
    (SELECT TOP 1 rd.Q18
     FROM questionnaire.QTCERIESGO rd
     WHERE rd.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rd.QUESDate DESC, rd.QUESTime DESC
    )                                                           AS RESULTADO_DEPENDENCIA,
    (SELECT TOP 1 rd.Q19
     FROM questionnaire.QTCERIESGO rd
     WHERE rd.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rd.QUESDate DESC, rd.QUESTime DESC
    )                                                           AS RESULTADO_RIESGO_DEPENDENCIA,

    -- === INSULINA - questionnaire.QGXXXISS (cols 32-33 ZEN) ===
    -- Último protocolo de insulina del episodio
    (SELECT TOP 1 ins.Q01
     FROM questionnaire.QGXXXISS ins
     WHERE ins.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY ins.QUESDate DESC, ins.QUESTime DESC
    )                                                           AS INSULINA_TIPO,
    (SELECT TOP 1 ins.Q09
     FROM questionnaire.QGXXXISS ins
     WHERE ins.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY ins.QUESDate DESC, ins.QUESTime DESC
    )                                                           AS INSULINA_PROTOCOLO,

    -- === DATOS EXTRA DE ENFERMERÍA ===
    DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31')             AS F_INGRESO,
    DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE)                                           AS DIAS_HOSPITALIZACION,
    doc.CTPCP_Desc                                              AS MEDICO_TRATANTE,
    parent.CTLOC_Code                                           AS SERVICIO_PADRE

FROM 
    SQLUser.PA_Adm adm

    INNER JOIN SQLUser.PA_PatMas pm 
        ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId

    LEFT JOIN SQLUser.CT_Sex sx 
        ON pm.PAPMI_Sex_DR = sx.CTSEX_RowId

    LEFT JOIN SQLUser.CT_Loc ward 
        ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID

    LEFT JOIN SQLUser.CT_Loc parent
        ON adm.PAADM_ParentWard_DR = parent.CTLOC_RowID

    LEFT JOIN SQLUser.CT_CareProv doc 
        ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId

    -- MR_Adm para campos de enfermería (1 por episodio)
    LEFT JOIN SQLUser.MR_Adm mradm
        ON adm.PAADM_RowID = mradm.MRADM_ADM_DR

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL

ORDER BY 
    ward.CTLOC_Code,
    adm.PAADM_CurrentRoom_DR,
    adm.PAADM_CurrentBed_DR
;


-- ============================================================================
-- QUERY 16: ENTREGA ENFERMERIA - FILTRO POR SERVICIO FISICO
-- Misma query anterior pero filtrada y compacta por servicio.
-- Cambiar el código de servicio según necesidad.
-- Incluye questionnaires: caídas (QCLXXEVARC), riesgo-dependencia (QTCERIESGO),
-- insulina (QGXXXISS). Misma lógica que Q15 pero filtrada.
-- ============================================================================

-- >>> SERVICIO: Cambiar por el código deseado <<<
-- Servicios comunes: MQ1, MQ2, UCI, UTIA, PED, OBS, URG
-- Ejemplo: ward.CTLOC_Code LIKE '%MQ1%'

SELECT TOP 200
    adm.PAADM_CurrentBed_DR                                     AS CAMA,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUN,
    sx.CTSEX_Desc                                               AS SEXO,
    DATEDIFF('dd',
        DATEADD('dd', adm.PAADM_AdmDate, '1840-12-31'),
        CURRENT_DATE)                                           AS DH,
    (SELECT LIST(d.MRDIA_Desc, ';')
     FROM SQLUser.MR_Adm ma
     INNER JOIN SQLUser.MR_Diagnos d ON ma.MRADM_RowId = d.MRDIA_MRADM_ParRef
     WHERE ma.MRADM_ADM_DR = adm.PAADM_RowID AND d.MRDIA_Prefix = 'C'
    )                                                           AS DX_CONFIRMADOS,
    
    -- Signos vitales (último registro)
    (SELECT TOP 1 v.MRCLN_PulseRate FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC)             AS FC,
    (SELECT TOP 1 v.MRCLN_BldPressSyst FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC)             AS PA_S,
    (SELECT TOP 1 v.MRCLN_BldPressDias FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC)             AS PA_D,
    (SELECT TOP 1 v.MRCLN_RespirationRate FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC)             AS FR,
    (SELECT TOP 1 v.MRCLN_BodyTemp FROM SQLUser.MR_ClncData v
     WHERE v.MRCLN_MRADM_ParRef = mradm.MRADM_RowId
     ORDER BY v.MRCLN_Date DESC, v.MRCLN_Time DESC)             AS TEMP,
    mradm.MRADM_OxygenSaturation                                AS SAT_O2,
    mradm.MRADM_BloodSugarTestResult                            AS HGT,
    mradm.MRADM_PainScore                                       AS EVA,

    -- Balance hídrico (último)
    (SELECT TOP 1 io.INPOUT_UrineOutput FROM SQLUser.MR_InputOutput io
     WHERE io.INPOUT_ParRef = mradm.MRADM_RowId
     ORDER BY io.INPOUT_Date DESC, io.INPOUT_Time DESC)          AS DIURESIS,
    (SELECT TOP 1 io.INPOUT_Drainage FROM SQLUser.MR_InputOutput io
     WHERE io.INPOUT_ParRef = mradm.MRADM_RowId
     ORDER BY io.INPOUT_Date DESC, io.INPOUT_Time DESC)          AS DRENAJE,

    -- Dieta y alergias
    mradm.MRADM_DietComments                                    AS REGIMEN,
    pm.PAPMI_Allergy                                             AS ALERGIAS,

    -- Medicamentos activos
    (SELECT LIST(oi.OEORI_BillDesc || ' ' || 
                 DATEADD('dd', oi.OEORI_SttDat, '1840-12-31'), ';')
     FROM SQLUser.OE_OrdItem oi
     INNER JOIN SQLUser.OE_Order ord ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
     WHERE ord.OEORD_Adm_DR = adm.PAADM_RowID
       AND oi.OEORI_ItemStat_DR NOT IN (12, 5)
       AND oi.OEORI_Categ_DR = 2
    )                                                            AS MEDICAMENTOS,

    doc.CTPCP_Desc                                               AS MEDICO,

    -- Questionnaires (mismo patrón Q15)
    (SELECT TOP 1 rc.QUESScore FROM questionnaire.QCLXXEVARC rc
     WHERE rc.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rc.QUESDate DESC, rc.QUESTime DESC)                 AS CAIDAS_SCORE,
    (SELECT TOP 1 rd.Q19 FROM questionnaire.QTCERIESGO rd
     WHERE rd.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY rd.QUESDate DESC, rd.QUESTime DESC)                 AS RIESGO_DEP,
    (SELECT TOP 1 ins.Q01 FROM questionnaire.QGXXXISS ins
     WHERE ins.QUESPAAdmDR = adm.PAADM_RowID
     ORDER BY ins.QUESDate DESC, ins.QUESTime DESC)               AS INSULINA

FROM 
    SQLUser.PA_Adm adm
    INNER JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Sex sx ON pm.PAPMI_Sex_DR = sx.CTSEX_RowId
    LEFT JOIN SQLUser.CT_Loc ward ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.CT_CareProv doc ON adm.PAADM_AdmDocCodeDR = doc.CTPCP_RowId
    LEFT JOIN SQLUser.MR_Adm mradm ON adm.PAADM_RowID = mradm.MRADM_ADM_DR

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    -- >>> CAMBIAR SERVICIO AQUI <<<
    AND ward.CTLOC_Code LIKE '%MQ1%'

ORDER BY 
    adm.PAADM_CurrentBed_DR
;


-- ============================================================================
-- QUERY 17: ESCALA RIESGO DE CAIDAS POR EPISODIO
-- Tabla: questionnaire.QCLXXEVARC
-- Trae la última evaluación de riesgo de caídas por paciente hospitalizado.
-- Campos: Q01-Q21 mapean factores de riesgo individuales.
-- JOIN: QUESPAAdmDR → PA_Adm.PAADM_RowId (igual que Caprini)
-- ============================================================================

SELECT TOP 500
    adm.PAADM_RowID                                             AS ID_EPISODIO,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUN,
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,

    -- Datos del formulario
    DATEADD('dd', rc.QUESDate, '1840-12-31')                     AS FECHA_EVAL,
    ssu.SSUSR_Name                                              AS EVALUADOR,
    rc.QUESScore                                                AS SCORE_CAIDAS,

    -- Factores de riesgo individuales
    rc.Q01                                                      AS FACTORES_RIESGO,
    rc.Q02                                                      AS MAYOR_65_O_PEDIATRICO,
    rc.Q03                                                      AS CAIDAS_PREVIAS,
    rc.Q05                                                      AS ALT_NEUROLOGICAS,
    rc.Q07                                                      AS TRAST_PSIQUICOS,
    rc.Q11                                                      AS DEFECTOS_VISION_AUDICION,
    rc.Q13                                                      AS ALT_CONCIENCIA,
    rc.Q15                                                      AS USO_FARMACOS

FROM 
    questionnaire.QCLXXEVARC rc
    JOIN SQLUser.PA_Adm adm ON rc.QUESPAAdmDR = adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.SS_User ssu ON rc.QUESUserDR = ssu.SSUSR_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    -- Solo la última evaluación por episodio
    AND rc.ID = (
        SELECT TOP 1 rc2.ID 
        FROM questionnaire.QCLXXEVARC rc2 
        WHERE rc2.QUESPAAdmDR = adm.PAADM_RowID
        ORDER BY rc2.QUESDate DESC, rc2.QUESTime DESC
    )

ORDER BY 
    ward.CTLOC_Code, adm.PAADM_CurrentBed_DR
;


-- ============================================================================
-- QUERY 18: CATEGORIZACION RIESGO-DEPENDENCIA POR EPISODIO
-- Tabla: questionnaire.QTCERIESGO
-- Trae la última categorización riesgo-dependencia por paciente hospitalizado.
-- Campos clave: Q15 (Escala Dependencia), Q16 (Escala Riesgo),
--   Q17 (Resultado Riesgo), Q18 (Resultado Dependencia),
--   Q19 (Resultado Riesgo-Dependencia combinado)
-- JOIN: QUESPAAdmDR → PA_Adm.PAADM_RowId
-- ============================================================================

SELECT TOP 500
    adm.PAADM_RowID                                             AS ID_EPISODIO,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUN,
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,

    -- Datos del formulario
    DATEADD('dd', rd.QUESDate, '1840-12-31')                     AS FECHA_EVAL,
    ssu.SSUSR_Name                                              AS EVALUADOR,

    -- Cuidados individuales (Q01-Q14)
    rd.Q01                                                      AS CAMBIO_ROPA,
    rd.Q02                                                      AS MOVILIZACION,
    rd.Q03                                                      AS ALIMENTACION,
    rd.Q04                                                      AS ELIMINACION,
    rd.Q05                                                      AS APOYO_PSICOSOCIAL,
    rd.Q06                                                      AS VIGILANCIA,
    rd.Q07                                                      AS SIGNOS_VITALES,
    rd.Q08                                                      AS BALANCE_HIDRICO,
    rd.Q09                                                      AS OXIGENOTERAPIA,
    rd.Q10                                                      AS VIA_AEREA,
    rd.Q11                                                      AS INTERV_PROFESIONALES,
    rd.Q12                                                      AS PIEL_CURACIONES,
    rd.Q13                                                      AS TRATAMIENTO_FARM,
    rd.Q14                                                      AS ELEMENTOS_INVASIVOS,

    -- Resultados
    rd.Q15                                                      AS ESCALA_DEPENDENCIA,
    rd.Q16                                                      AS ESCALA_RIESGO,
    rd.Q17                                                      AS RESULTADO_RIESGO,
    rd.Q18                                                      AS RESULTADO_DEPENDENCIA,
    rd.Q19                                                      AS RESULTADO_RIESGO_DEP

FROM 
    questionnaire.QTCERIESGO rd
    JOIN SQLUser.PA_Adm adm ON rd.QUESPAAdmDR = adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.SS_User ssu ON rd.QUESUserDR = ssu.SSUSR_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    AND rd.ID = (
        SELECT TOP 1 rd2.ID 
        FROM questionnaire.QTCERIESGO rd2 
        WHERE rd2.QUESPAAdmDR = adm.PAADM_RowID
        ORDER BY rd2.QUESDate DESC, rd2.QUESTime DESC
    )

ORDER BY 
    ward.CTLOC_Code, adm.PAADM_CurrentBed_DR
;


-- ============================================================================
-- QUERY 19: DISPOSITIVOS INVASIVOS POR EPISODIO
-- Tabla principal: questionnaire.QCLXXMDI
-- Subtablas: QCLXXMDIQQ01 (VVP), QQ02 (CVC), QQ05 (Arterial),
--            QQ06 (Urinario), QQ07 (Vía Aérea), QQ08 (GI),
--            QQ10 (Drenajes), QQ12 (Neuromonitoreo)
-- 
-- NOTA: Las subtablas (QQnn) son tablas hijas con relación padre
--   via campo 'childsub'. Cada subtabla puede tener múltiples registros
--   por formulario padre. Esta query trae el resumen principal.
-- JOIN: QUESPAAdmDR → PA_Adm.PAADM_RowId
-- ============================================================================

SELECT TOP 500
    adm.PAADM_RowID                                             AS ID_EPISODIO,
    pm.PAPMI_Name                                               AS PACIENTE,
    pm.PAPMI_ID                                                 AS RUN,
    ward.CTLOC_Code                                             AS SERVICIO,
    adm.PAADM_CurrentBed_DR                                     AS CAMA,

    -- Datos del formulario MDI
    DATEADD('dd', mdi.QUESDate, '1840-12-31')                    AS FECHA_EVAL,
    ssu.SSUSR_Name                                              AS EVALUADOR,

    -- Comentarios generales
    mdi.Q03                                                     AS COMENTARIOS_VVP,
    mdi.Q04                                                     AS COMENTARIOS_CV,
    mdi.Q09                                                     AS COMENTARIOS_GI,
    mdi.Q11                                                     AS COMENTARIOS_DRENAJES,

    -- Conteo de dispositivos activos (subqueries a subtablas)
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ01 vvp
     WHERE vvp.childsub = mdi.ID)                                AS N_VVP,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ02 cvc
     WHERE cvc.childsub = mdi.ID)                                AS N_CVC,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ05 art
     WHERE art.childsub = mdi.ID)                                AS N_ARTERIAL,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ06 uri
     WHERE uri.childsub = mdi.ID)                                AS N_URINARIO,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ07 via
     WHERE via.childsub = mdi.ID)                                AS N_VIA_AEREA,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ08 gi
     WHERE gi.childsub = mdi.ID)                                 AS N_GI,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ10 drn
     WHERE drn.childsub = mdi.ID)                                AS N_DRENAJES,
    (SELECT COUNT(*) FROM questionnaire.QCLXXMDIQQ12 neu
     WHERE neu.childsub = mdi.ID)                                AS N_NEURO

FROM 
    questionnaire.QCLXXMDI mdi
    JOIN SQLUser.PA_Adm adm ON mdi.QUESPAAdmDR = adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas pm ON adm.PAADM_PAPMI_DR = pm.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc ward ON adm.PAADM_CurrentWard_DR = ward.CTLOC_RowID
    LEFT JOIN SQLUser.SS_User ssu ON mdi.QUESUserDR = ssu.SSUSR_RowId

WHERE
    adm.PAADM_Type = 'I'
    AND adm.PAADM_VisitStatus = 'A'
    AND adm.PAADM_DischgDate IS NULL
    AND mdi.ID = (
        SELECT TOP 1 mdi2.ID 
        FROM questionnaire.QCLXXMDI mdi2 
        WHERE mdi2.QUESPAAdmDR = adm.PAADM_RowID
        ORDER BY mdi2.QUESDate DESC, mdi2.QUESTime DESC
    )

ORDER BY 
    ward.CTLOC_Code, adm.PAADM_CurrentBed_DR
;
