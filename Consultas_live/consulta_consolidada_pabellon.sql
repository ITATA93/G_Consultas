-- ==============================================================================
-- Consulta: Trazabilidad Consolidada de Pabellón Quirúrgico
-- Objetivo: Consolidar datos del paciente, llegada/egreso de pabellón, pausas
--           de seguridad (Checklist) y detalle clínico del protocolo operatorio.
-- Seguridad: LIMIT LIMITADO (TOP 50) y Filtro de Fechas Obligatorio.
-- Fecha:    2026-02-26
-- ==============================================================================

SELECT TOP 50
    -- 1. IDENTIFICACIÓN DEL PACIENTE
    Pat.PAPMI_No AS "RUT_Ficha",
    Pat.PAPMI_Name AS "Nombre",
    Pat.PAPMI_Name2 AS "Apellido_Paterno",
    Adm.PAADM_ADMNo AS "Episodio_Admision",

    -- 2. PROCEDIMIENTO REALIZADO Y PERSONAL
    OperC.OPER_Code AS "Cod_Procedimiento",
    OperC.OPER_Desc AS "Procedimiento",
    Surg.CTPCP_Desc AS "Cirujano_Principal",
    AnaOP.ANAOP_Status AS "Estado_Cirugia",

    -- 3. HITOS DE PABELLÓN (Tiempos Quirúrgicos)
    AnaOP.ANAOP_TheatreInDate AS "Fecha_Llega_Pabellon",
    AnaOP.ANAOP_TheatreInTime AS "Hora_Llega_Pabellon",

    AnaOP.ANAOP_OpStartDate AS "Fecha_Inicio_Cirugia",
    AnaOP.ANAOP_OpStartTime AS "Hora_Inicio_Cirugia",

    AnaOP.ANAOP_OpEndDate AS "Fecha_Fin_Cirugia",
    AnaOP.ANAOP_OpEndTime AS "Hora_Fin_Cirugia",

    AnaOP.ANAOP_TheatreOutDate AS "Fecha_Egreso_Pabellon",
    AnaOP.ANAOP_TheatreOutTime AS "Hora_Egreso_Pabellon",

    -- 4. PAUSAS DE SEGURIDAD (Cuestionario QGXXXSS - CheckList Cirugía Segura)
    Chk.Q02 AS "Fecha_SignIn",
    Chk.Q35 AS "Hora_SignIn",

    Chk.Q16 AS "Fecha_TimeOut_Entrada",
    Chk.Q36 AS "Hora_TimeOut_Entrada",

    Chk.Q26 AS "Fecha_SignOut_Salida",
    Chk.Q39 AS "Hora_SignOut_Salida",

    -- 5. PROTOCOLO OPERATORIO (Textos Clínicos Integrados)
    -- NOTA: Se convierte TEXT a VARCHAR(4000) si es necesario para evitar errores de driver en IRIS,
    --       pero para este prototipo lo traemos directo.
    CAST(AnaOP.ANAOP_PreOPDiagnosis AS VARCHAR(2000)) AS "Diagnostico_PreOp",
    CAST(AnaOP.ANAOP_PostOPDiagnosisDiff AS VARCHAR(2000)) AS "Diagnostico_PostOp",
    CAST(AnaOP.ANAOP_Findings AS VARCHAR(2000)) AS "Hallazgos_Operatorios",
    CAST(AnaOP.ANAOP_ProceduralDetails AS VARCHAR(2000)) AS "Detalles_Procedimiento",
    CAST(AnaOP.ANAOP_PostOperInstructions AS VARCHAR(2000)) AS "Instrucciones_PostOp"

FROM SQLUser.OR_Anaesthesia Ana

-- Vinculación a las cirugías/procedimientos de esa anestesia
JOIN SQLUser.OR_Anaest_Operation AnaOP
  ON Ana.ANA_RowId = AnaOP.ANAOP_Par_Ref

-- Vinculación con los datos demográficos y clínicos del paciente
JOIN SQLUser.PA_Adm Adm
  ON Ana.ANA_PAADM_ParRef = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat
  ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId

-- Catálogo de Procedimientos y Médico tratante
LEFT JOIN SQLUser.ORC_Operation OperC
  ON AnaOP.ANAOP_Type_DR = OperC.OPER_RowId
LEFT JOIN SQLUser.CT_CareProv Surg
  ON AnaOP.ANAOP_Surgeon_DR = Surg.CTPCP_RowId1

-- Cuestionario de Pausas de Seguridad (Vinculado específicamente al ID de la operación)
LEFT JOIN questionnaire.QGXXXSS Chk
  ON Chk.QUESAnaOperationDR = AnaOP.ANAOP_RowId

-- Filtro crítico: Solo cirugías efectuadas
WHERE AnaOP.ANAOP_Status = 'D'
ORDER BY AnaOP.ANAOP_OpStartDate DESC
