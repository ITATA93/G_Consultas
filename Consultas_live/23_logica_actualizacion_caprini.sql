/*
=============================================================================
DOCUMENTACION DE LOGICA DE ACTUALIZACION: ALMA_Reportes.CAL_RiesgoETE
=============================================================================
Este proceso requiere dos pasos debido a que conecta dos servidores distintos:
1. IRIS (TrakCare): Extracción de datos.
2. SQL Server (SIDRA): Carga y Actualización (Upsert/Merge).

El script "21_sync_riesgo_ete_caprini.py" automatiza este puente.
*/

-- =========================================================================
-- PASO 1: CONSULTA DE EXTRACCION (Ejecutada en IRIS / LIVE-CLOV)
-- Busca formularios modificados en las últimas 24 horas
-- =========================================================================
SELECT 
    Q.ID,                        -- ID interno del formulario
    Pat.PAPMI_No,                -- RUN Paciente
    Pat.PAPMI_Name,              -- Nombre
    Pat.PAPMI_Name2,             -- Apellido
    Adm.PAADM_AdmNo,             -- Nº Episodio
    Adm.PAADM_AdmDate,           -- Fecha Admisión
    Adm.PAADM_AdmTime,           -- Hora Admisión
    Loc.CTLOC_Desc,              -- Ubicación
    Q.QUESDate,                  -- Fecha Formulario
    Q.QUESTime,                  -- Hora Formulario
    SSU.SSUSR_Name,              -- Usuario Responsable
    Q.Q01 AS Edad,
    Q.Q02 AS Tipo_Cirugia,
    Q.Q03 AS Evento_Reciente,
    Q.Q04 AS Enf_Venosa,
    Q.Q05 AS Movilidad,
    Q.Q06 AS Antecedentes_Otros,
    Q.QUESScore AS Score_Total, -- Corregido desde Q45
    NULL AS Clasificacion_Riesgo -- Corregido desde Q46
FROM questionnaire.QTCEEVRIEST Q
JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
LEFT JOIN SQLUser.CT_Loc Loc ON Adm.PAADM_DepCode_DR = Loc.CTLOC_RowId
LEFT JOIN SQLUser.SS_User SSU ON Q.QUESUserDR = SSU.SSUSR_RowId
WHERE Q.QUESDate >= (CURRENT_DATE - 1);


-- =========================================================================
-- PASO 2: LOGICA DE ACTUALIZACION (Ejecutada en SQL Server / SIDRA)
-- Usa MERGE para Insertar nuevos o Actualizar existentes
-- =========================================================================
/*
Nota: Los parámetros (?) son llenados dinámicamente por el script Python
con los datos extraídos en el Paso 1.
*/

MERGE ALMA_Reportes.CAL_RiesgoETE AS Target
USING (VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) 
    AS Source (
        ID_Row, Paciente_RUN, Paciente_Nombre, Episodio_Admision, Fecha_Admision, Ubicacion_Actual,
        Tiene_Caprini, Form_ID, Form_Fecha, Form_Usuario,
        Edad, Tipo_Cirugia, Evento_Reciente, Enf_Venosa_Coagulacion, Movilidad, Antecedentes_Otros,
        Score_Total, Clasificacion_Riesgo
    )
ON (Target.ID_Row = Source.ID_Row) -- Clave única: Episodio + ID Formulario

WHEN MATCHED THEN
    UPDATE SET
        Form_Fecha = Source.Form_Fecha,
        Score_Total = Source.Score_Total,
        Clasificacion_Riesgo = Source.Clasificacion_Riesgo,
        Fecha_Proceso = GETDATE()

WHEN NOT MATCHED THEN
    INSERT (
        ID_Row, Paciente_RUN, Paciente_Nombre, Episodio_Admision, Fecha_Admision, Ubicacion_Actual,
        Tiene_Caprini, Form_ID, Form_Fecha, Form_Usuario,
        Edad, Tipo_Cirugia, Evento_Reciente, Enf_Venosa_Coagulacion, Movilidad, Antecedentes_Otros,
        Score_Total, Clasificacion_Riesgo, Fecha_Proceso
    )
    VALUES (
        Source.ID_Row, Source.Paciente_RUN, Source.Paciente_Nombre, Source.Episodio_Admision, Source.Fecha_Admision, Source.Ubicacion_Actual,
        Source.Tiene_Caprini, Source.Form_ID, Source.Form_Fecha, Source.Form_Usuario,
        Source.Edad, Source.Tipo_Cirugia, Source.Evento_Reciente, Source.Enf_Venosa_Coagulacion, Source.Movilidad, Source.Antecedentes_Otros,
        Source.Score_Total, Source.Clasificacion_Riesgo, GETDATE()
    );
