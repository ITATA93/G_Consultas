-- ================================================================
-- PAQUETE DBA: Consultorias de Llamado — ALMA_Consultor
-- Autor: Unidad de Informatica Clinica
-- Fecha: 2026-02-26
-- ================================================================
--
-- Este paquete contiene todo lo necesario para implementar el
-- reporte de consultorias de llamado con cruce de cirugias.
--
-- CONTENIDO:
--   PARTE 1: Queries ALMA/IRIS (fuente de datos, solo lectura)
--   PARTE 2: DDL SIDRA-TEST (schema + tablas + vista)
--   PARTE 3: Queries de consulta SIDRA (reportes clinicos)
--
-- FLUJO:
--   ALMA (InterSystems IRIS) --[ETL lectura]--> SIDRA-TEST (SQL Server)
--   Las queries ALMA son SELECT puro, no modifican datos.
--
-- ================================================================


-- ////////////////////////////////////////////////////////////////
-- PARTE 1: QUERIES ALMA / IRIS (InterSystems Cache SQL)
-- Servidor: 10.63.180.25:51773 | Namespace: LIVE-CLOV
-- NOTA: Fechas en formato $HOROLOG (dias desde 1840-12-31)
--       Tiempos en $HOROLOG (segundos desde medianoche)
-- ////////////////////////////////////////////////////////////////

-- ============================================================
-- 1A. CONSULTORIAS DE LLAMADO (tabla principal)
-- Extrae ordenes de consultoria con datos del paciente,
-- estados, datos de contacto y profesional asignado.
-- Items filtrados: 13 codigos HOVA de consultoria de llamado.
-- ============================================================
/*
SELECT
    oi.OEORI_RowId                AS Orden_RowId,
    -- Paciente
    per.PAPER_ID                  AS RUN,
    per.PAPER_Name2               AS Nombres,
    per.PAPER_Name                AS Apellidos,
    per.PAPER_Dob                 AS Fecha_Nacimiento_H,
    -- Episodio
    adm.PAADM_RowId               AS Episodio_ID,
    adm.PAADM_AdmDate             AS Fecha_Admision_H,
    adm.PAADM_CurrentWard_DR      AS Servicio_DR,
    -- Orden
    oi.OEORI_ItmMast_DR           AS Item_DR,
    oi.OEORI_Date                 AS Fecha_Orden_H,
    oi.OEORI_TimeOrd              AS Hora_Orden_H,
    oi.OEORI_SttDat               AS Fecha_Inicio_Orden_H,
    oi.OEORI_DateExecuted          AS Fecha_Ejecutado_H,
    oi.OEORI_Doctor_DR            AS Medico_Solicitante_DR,
    -- Grupo receptor
    oi2.ITM2_Group_DR             AS Grupo_DR,
    -- Decorator regional (GES, numero IC, verificacion)
    clxx.COEORI_GES               AS GES,
    clxx.COEORI_No                AS Numero_IC,
    clxx.COEORI_Verified          AS Verificado,
    -- Ultimo estado de la orden
    st.ST_Status_DR               AS Estado_DR,
    st.ST_Date                    AS Fecha_Ultimo_Estado_H,
    st.ST_Time                    AS Hora_Ultimo_Estado_H,
    -- Datos de contacto (formulario IC)
    enq.ENQ_RowId                 AS Contacto_ID,
    enq.ENQ_Date                  AS Fecha_Contacto_H,
    enq.ENQ_Time                  AS Hora_Contacto_H,
    enq.ENQ_Duration              AS Duracion_Min,
    enq.ENQ_RequestStatus_DR      AS Estatus_Solicitud_DR,
    enq.ENQ_ContMethod_DR         AS Metodo_Contacto_DR,
    enq.ENQ_Hospital_DR           AS Hospital_DR,
    enq.ENQ_Location_DR           AS Local_DR,
    enq.ENQ_CTCP_DR               AS Profesional_DR,
    -- ID paciente para cruce posterior
    pmi.PAPMI_RowId               AS Paciente_ID
FROM SQLUser.OE_OrdItem oi
JOIN SQLUser.OE_Order ord       ON oi.OEORI_OEORD_ParRef = ord.OEORD_RowId
JOIN SQLUser.PA_Adm adm         ON ord.OEORD_Adm_DR = adm.PAADM_RowId
JOIN SQLUser.PA_PatMas pmi      ON adm.PAADM_PAPMI_DR = pmi.PAPMI_RowId
JOIN SQLUser.PA_Person per      ON pmi.PAPMI_PAPER_DR = per.PAPER_RowId
JOIN SQLUser.OE_OrdItem2 oi2    ON oi2.ITM2_RowId = oi.OEORI_RowId
LEFT JOIN Region_CLXX_Misc_User.OEOrdItem clxx
    ON clxx.COEORI_OEORI_DR = oi.OEORI_RowId
LEFT JOIN (
    SELECT ST_ParRef, MAX(ST_Childsub) AS MaxStep
    FROM SQLUser.OE_OrdStatus GROUP BY ST_ParRef
) last_st ON last_st.ST_ParRef = oi.OEORI_RowId
LEFT JOIN SQLUser.OE_OrdStatus st
    ON st.ST_ParRef = oi.OEORI_RowId AND st.ST_Childsub = last_st.MaxStep
LEFT JOIN SQLUser.PA_EnquiryContact enq
    ON enq.ENQ_OEOrdItem_DR = oi.OEORI_RowId
WHERE oi.OEORI_ItmMast_DR IN (
    '16630||1','16628||1','16632||1','10562||1','10563||1',
    '10564||1','10565||1','10566||1','10567||1','10568||1',
    '15927||1','15923||1','15925||1'
)
  AND oi.OEORI_Date >= {fecha_desde_horolog}
  AND oi.OEORI_Date <= {fecha_hasta_horolog}
ORDER BY oi.OEORI_Date DESC
*/

-- ============================================================
-- 1B. CIRUGIAS DE PABELLON (con codigos de operacion)
-- Incluye endoscopias y cirugias ambulatorias.
-- Rango: periodo IC + 2 dias (ventana 48h).
-- ============================================================
/*
SELECT
    adm2.PAADM_PAPMI_DR          AS Paciente_ID,
    rb.RBOP_RowId                 AS RBOP_RowId,
    rb.RBOP_PAADM_DR             AS Episodio_Cx,
    rb.RBOP_DateOper              AS Fecha_Operacion_H,
    rb.RBOP_TimeOper              AS Hora_Operacion_H,
    rb.RBOP_Surgeon_DR            AS Cirujano_DR,
    rb.RBOP_SurgeonAssist_DR      AS Ayudante_DR,
    rb.RBOP_Procedure             AS Procedimiento_Texto,
    rb.RBOP_Endoscopy             AS Endoscopia,
    rb.RBOP_DaySurgery            AS Cirugia_Ambulatoria,
    rb.RBOP_BookingType           AS Tipo_Booking,
    rb.RBOP_Status                AS Estado_Pabellon,
    -- Codigo FONASA del procedimiento principal
    oper.OPER_Code                AS Operacion_Cod,
    oper.OPER_Desc                AS Operacion_Desc
FROM SQLUser.RB_OperatingRoom rb
JOIN SQLUser.PA_Adm adm2
    ON rb.RBOP_PAADM_DR = adm2.PAADM_RowId
LEFT JOIN SQLUser.ORC_Operation oper
    ON rb.RBOP_Operation_DR = oper.OPER_RowId
WHERE rb.RBOP_DateOper >= {fecha_desde_horolog}
  AND rb.RBOP_DateOper <= {fecha_hasta_horolog} + 2
*/

-- ============================================================
-- 1C. PROCEDIMIENTOS SECUNDARIOS DE CIRUGIAS
-- Codigos adicionales por cirugia (hasta 3+ por operacion).
-- Se concatenan en campo Procedimientos_Sec.
-- ============================================================
/*
SELECT
    sp.SECPR_ParRef                AS RBOP_RowId,
    oper.OPER_Code                 AS Codigo,
    oper.OPER_Desc                 AS Descripcion
FROM SQLUser.RB_OperRoomSecondaryProc sp
JOIN SQLUser.RB_OperatingRoom rb
    ON sp.SECPR_ParRef = rb.RBOP_RowId
LEFT JOIN SQLUser.ORC_Operation oper
    ON sp.SECPR_Operation_DR = oper.OPER_RowId
WHERE rb.RBOP_DateOper >= {fecha_desde_horolog}
  AND rb.RBOP_DateOper <= {fecha_hasta_horolog} + 2
*/

-- ============================================================
-- 1D. PROCEDIMIENTOS MENORES (fuera de pabellon)
-- Tabla MR_Procedures, vinculados via MR_Adm -> PA_Adm.
-- ============================================================
/*
SELECT
    adm3.PAADM_PAPMI_DR          AS Paciente_ID,
    mra.MRADM_ADM_DR             AS Episodio_Proc,
    pr.PROC_Date                  AS Fecha_Proc_H,
    pr.PROC_CTCP_DR               AS Profesional_DR,
    pr.PROC_ProcedureNotes        AS Notas
FROM SQLUser.MR_Adm mra
JOIN SQLUser.MR_Procedures pr   ON pr.PROC_ParRef = mra.MRADM_RowId
JOIN SQLUser.PA_Adm adm3        ON mra.MRADM_ADM_DR = adm3.PAADM_RowId
WHERE pr.PROC_Date >= {fecha_desde_horolog}
  AND pr.PROC_Date <= {fecha_hasta_horolog} + 2
*/

-- ============================================================
-- 1E. TABLAS DE DICCIONARIOS (resolucion de nombres)
-- Estas se consultan para traducir IDs a descripciones.
-- ============================================================
/*
-- Profesionales:   SELECT CTPCP_RowId, CTPCP_Desc FROM SQLUser.CT_CareProv
-- Items orden:     SELECT ARCIM_RowId, ARCIM_Desc FROM SQLUser.ARC_ItmMast
-- Grupos:          SELECT SSGRP_RowId, SSGRP_Desc FROM SQLUser.SS_Group
-- Estados orden:   SELECT OECS_RowId, OECS_Desc FROM SQLUser.OEC_OrderStatus
-- Hospitales:      SELECT HOSP_RowId, HOSP_Desc FROM SQLUser.CT_Hospital
-- Locaciones:      SELECT CTLOC_RowID, CTLOC_Desc FROM SQLUser.CT_Loc
-- Servicios:       SELECT WARD_RowId, WARD_Desc FROM SQLUser.PAC_Ward
-- Est. solicitud:  SELECT REQST_RowId, REQST_Desc FROM SQLUser.PAC_RequestStatus
-- Met. contacto:   SELECT CONTM_RowId, CONTM_Desc FROM SQLUser.PAC_ContMethod
*/


-- ////////////////////////////////////////////////////////////////
-- PARTE 2: DDL SIDRA-TEST (SQL Server)
-- Servidor: 10.67.119.135:1433 | Base: DB_SIDRA_TEST
-- Ejecutar UNA VEZ para crear la estructura.
-- ////////////////////////////////////////////////////////////////

-- Schema
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'ALMA_Consultor')
    EXEC('CREATE SCHEMA ALMA_Consultor');
GO

-- ============================================================
-- Tabla 1: IC_Llamado (consultorias de llamado)
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.IC_Llamado', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.IC_Llamado;
GO

CREATE TABLE ALMA_Consultor.IC_Llamado (
    Orden_RowId            VARCHAR(30)   NOT NULL PRIMARY KEY,
    -- Paciente
    RUN                    VARCHAR(15),
    Nombres                NVARCHAR(80),
    Apellidos              NVARCHAR(80),
    Fecha_Nacimiento       DATE,
    -- Episodio / Admision
    Episodio_ID            INT,
    Fecha_Admision         DATE,
    Servicio_DR            INT,
    Servicio_Desc          NVARCHAR(100),
    -- Orden
    Item_DR                VARCHAR(30),
    Item_Desc              NVARCHAR(120),
    Fecha_Orden            DATE          NOT NULL,
    Hora_Orden             VARCHAR(5),
    Fecha_Inicio_Orden     DATE,
    Fecha_Ejecutado        DATE,
    Medico_Solicitante_DR  INT,
    Medico_Solicitante     NVARCHAR(100),
    -- Grupo receptor
    Grupo_DR               INT,
    Grupo_Desc             NVARCHAR(100),
    -- Decorator regional
    GES                    VARCHAR(5),
    Numero_IC              VARCHAR(20),
    Verificado             VARCHAR(5),
    -- Ultimo estado
    Estado_DR              INT,
    Estado_Desc            NVARCHAR(60),
    Fecha_Ultimo_Estado    DATE,
    Hora_Ultimo_Estado     VARCHAR(5),
    -- Datos de contacto
    Contacto_ID            INT,
    Fecha_Contacto         DATE,
    Hora_Contacto          VARCHAR(5),
    Duracion_Min           INT,
    Estatus_Solicitud_DR   INT,
    Estatus_Solicitud      NVARCHAR(60),
    Metodo_Contacto_DR     INT,
    Metodo_Contacto        NVARCHAR(60),
    Hospital_DR            INT,
    Hospital_Desc          NVARCHAR(100),
    Local_DR               INT,
    Local_Desc             NVARCHAR(100),
    Profesional_DR         INT,
    Profesional_Desc       NVARCHAR(100),
    -- Metadata
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);
GO

-- ============================================================
-- Tabla 2: Cx_Pabellon (cirugias en pabellon)
-- Criterio: Endoscopy <> 'Y' AND DaySurgery <> 'Y'
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Cx_Pabellon', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Cx_Pabellon;
GO

CREATE TABLE ALMA_Consultor.Cx_Pabellon (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    RBOP_RowId             INT,
    Episodio_Cx            INT,
    Fecha_Operacion        DATE,
    Hora_Operacion         VARCHAR(5),
    Operacion_Cod          VARCHAR(20),
    Operacion_Desc         NVARCHAR(200),
    Procedimientos_Sec     NVARCHAR(MAX),
    Cirujano_DR            INT,
    Cirujano_Desc          NVARCHAR(100),
    Ayudante_DR            INT,
    Ayudante_Desc          NVARCHAR(100),
    Procedimiento_Texto    NVARCHAR(250),
    Tipo_Booking           VARCHAR(5),
    Estado_Pabellon        VARCHAR(10),
    Estado_Pabellon_Desc   NVARCHAR(40),
    Rol_Medico_IC          VARCHAR(20),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);
GO

-- ============================================================
-- Tabla 3: Cx_Endoscopia (Endoscopy = 'Y')
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Cx_Endoscopia', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Cx_Endoscopia;
GO

CREATE TABLE ALMA_Consultor.Cx_Endoscopia (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    RBOP_RowId             INT,
    Episodio_Cx            INT,
    Fecha_Operacion        DATE,
    Hora_Operacion         VARCHAR(5),
    Operacion_Cod          VARCHAR(20),
    Operacion_Desc         NVARCHAR(200),
    Procedimientos_Sec     NVARCHAR(MAX),
    Cirujano_DR            INT,
    Cirujano_Desc          NVARCHAR(100),
    Ayudante_DR            INT,
    Ayudante_Desc          NVARCHAR(100),
    Procedimiento_Texto    NVARCHAR(250),
    Tipo_Booking           VARCHAR(5),
    Estado_Pabellon        VARCHAR(10),
    Estado_Pabellon_Desc   NVARCHAR(40),
    Rol_Medico_IC          VARCHAR(20),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);
GO

-- ============================================================
-- Tabla 4: Cx_Menor (DaySurgery = 'Y', ambulatorias)
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Cx_Menor', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Cx_Menor;
GO

CREATE TABLE ALMA_Consultor.Cx_Menor (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    RBOP_RowId             INT,
    Episodio_Cx            INT,
    Fecha_Operacion        DATE,
    Hora_Operacion         VARCHAR(5),
    Operacion_Cod          VARCHAR(20),
    Operacion_Desc         NVARCHAR(200),
    Procedimientos_Sec     NVARCHAR(MAX),
    Cirujano_DR            INT,
    Cirujano_Desc          NVARCHAR(100),
    Ayudante_DR            INT,
    Ayudante_Desc          NVARCHAR(100),
    Procedimiento_Texto    NVARCHAR(250),
    Tipo_Booking           VARCHAR(5),
    Estado_Pabellon        VARCHAR(10),
    Estado_Pabellon_Desc   NVARCHAR(40),
    Rol_Medico_IC          VARCHAR(20),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);
GO

-- ============================================================
-- Tabla 5: Procedimientos (MR_Procedures, fuera de pabellon)
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.Procedimientos', 'U') IS NOT NULL
    DROP TABLE ALMA_Consultor.Procedimientos;
GO

CREATE TABLE ALMA_Consultor.Procedimientos (
    ID                     INT           IDENTITY(1,1) PRIMARY KEY,
    Orden_RowId            VARCHAR(30)   NOT NULL,
    Episodio_Proc          INT,
    Fecha_Procedimiento    DATE,
    Profesional_DR         INT,
    Profesional_Desc       NVARCHAR(100),
    Notas                  NVARCHAR(500),
    Horas_Post_IC          INT,
    Fecha_Carga            DATETIME2     DEFAULT GETDATE()
);
GO

-- ============================================================
-- Vista clinica consolidada
-- ============================================================
IF OBJECT_ID('ALMA_Consultor.V_Resumen_Clinico', 'V') IS NOT NULL
    DROP VIEW ALMA_Consultor.V_Resumen_Clinico;
GO

CREATE VIEW ALMA_Consultor.V_Resumen_Clinico AS
SELECT
    -- === PACIENTE ===
    ic.RUN,
    ic.Apellidos + ', ' + ic.Nombres       AS Paciente,
    ic.Fecha_Nacimiento,
    DATEDIFF(YEAR, ic.Fecha_Nacimiento, ic.Fecha_Orden)  AS Edad,

    -- === INTERCONSULTA ===
    ic.Orden_RowId,
    ic.Episodio_ID,
    ic.Item_Desc                            AS Tipo_Consultoria,
    ic.Servicio_Desc                        AS Servicio_Origen,
    ic.Fecha_Orden,
    ic.Hora_Orden,
    ic.Estado_Desc                          AS Estado_IC,
    ic.Medico_Solicitante                   AS Medico_Solicitante,
    ic.Profesional_Desc                     AS Profesional_Contactado,
    ic.Metodo_Contacto,
    ic.Duracion_Min                         AS Duracion_Contacto_Min,

    -- === TIEMPOS CLINICOS ===
    ic.Fecha_Contacto,
    ic.Hora_Contacto,
    ic.Fecha_Ultimo_Estado,
    ic.Hora_Ultimo_Estado,
    -- Horas desde solicitud hasta contacto
    CASE WHEN ic.Fecha_Contacto IS NOT NULL AND ic.Hora_Contacto IS NOT NULL
              AND ic.Hora_Orden IS NOT NULL
         THEN DATEDIFF(HOUR,
                CAST(ic.Fecha_Orden AS DATETIME)
                    + CAST(ic.Hora_Orden + ':00' AS DATETIME),
                CAST(ic.Fecha_Contacto AS DATETIME)
                    + CAST(ic.Hora_Contacto + ':00' AS DATETIME))
         ELSE NULL
    END                                     AS Hrs_Solicitud_a_Contacto,
    -- Horas desde solicitud hasta ejecucion
    CASE WHEN ic.Fecha_Ejecutado IS NOT NULL
         THEN DATEDIFF(HOUR,
                CAST(ic.Fecha_Orden AS DATETIME),
                CAST(ic.Fecha_Ejecutado AS DATETIME))
         ELSE NULL
    END                                     AS Hrs_Solicitud_a_Ejecucion,

    -- === CIRUGIA EN PABELLON ===
    cx.Fecha_Operacion                      AS Cx_Fecha,
    cx.Hora_Operacion                       AS Cx_Hora,
    cx.Operacion_Cod                        AS Cx_Codigo,
    cx.Operacion_Desc                       AS Cx_Procedimiento,
    cx.Procedimientos_Sec                   AS Cx_Procedimientos_Secundarios,
    cx.Cirujano_Desc                        AS Cx_Cirujano,
    cx.Ayudante_Desc                        AS Cx_Ayudante,
    cx.Tipo_Booking                         AS Cx_Tipo_Booking,
    cx.Estado_Pabellon_Desc                 AS Cx_Estado,
    cx.Rol_Medico_IC                        AS Cx_Rol_Medico_IC,
    cx.Horas_Post_IC                        AS Cx_Horas_Post_IC,
    -- Horas desde solicitud hasta pabellon
    CASE WHEN cx.Fecha_Operacion IS NOT NULL AND cx.Hora_Operacion IS NOT NULL
              AND ic.Hora_Orden IS NOT NULL
         THEN DATEDIFF(HOUR,
                CAST(ic.Fecha_Orden AS DATETIME)
                    + CAST(ic.Hora_Orden + ':00' AS DATETIME),
                CAST(cx.Fecha_Operacion AS DATETIME)
                    + CAST(cx.Hora_Operacion + ':00' AS DATETIME))
         ELSE NULL
    END                                     AS Hrs_Solicitud_a_Pabellon,

    -- === ENDOSCOPIA ===
    endo.Fecha_Operacion                    AS Endo_Fecha,
    endo.Hora_Operacion                     AS Endo_Hora,
    endo.Operacion_Desc                     AS Endo_Procedimiento,
    endo.Cirujano_Desc                      AS Endo_Medico,
    endo.Horas_Post_IC                      AS Endo_Horas_Post_IC,

    -- === CIRUGIA MENOR ===
    cm.Fecha_Operacion                      AS CxMenor_Fecha,
    cm.Hora_Operacion                       AS CxMenor_Hora,
    cm.Operacion_Desc                       AS CxMenor_Procedimiento,
    cm.Cirujano_Desc                        AS CxMenor_Medico,
    cm.Horas_Post_IC                        AS CxMenor_Horas_Post_IC,

    -- === PROCEDIMIENTO ===
    pr.Fecha_Procedimiento                  AS Proc_Fecha,
    pr.Profesional_Desc                     AS Proc_Profesional,
    pr.Notas                                AS Proc_Notas,
    pr.Horas_Post_IC                        AS Proc_Horas_Post_IC,

    -- === FLAGS RESUMEN ===
    CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END       AS Tiene_Cirugia,
    CASE WHEN endo.ID IS NOT NULL THEN 1 ELSE 0 END     AS Tiene_Endoscopia,
    CASE WHEN cm.ID IS NOT NULL THEN 1 ELSE 0 END       AS Tiene_CxMenor,
    CASE WHEN pr.ID IS NOT NULL THEN 1 ELSE 0 END       AS Tiene_Procedimiento

FROM ALMA_Consultor.IC_Llamado ic
LEFT JOIN ALMA_Consultor.Cx_Pabellon cx
    ON cx.Orden_RowId = ic.Orden_RowId
LEFT JOIN ALMA_Consultor.Cx_Endoscopia endo
    ON endo.Orden_RowId = ic.Orden_RowId
LEFT JOIN ALMA_Consultor.Cx_Menor cm
    ON cm.Orden_RowId = ic.Orden_RowId
LEFT JOIN ALMA_Consultor.Procedimientos pr
    ON pr.Orden_RowId = ic.Orden_RowId;
GO


-- ////////////////////////////////////////////////////////////////
-- PARTE 3: QUERIES DE CONSULTA (ejecutar en SIDRA-TEST)
-- Estas funcionan sobre los datos ya cargados.
-- ////////////////////////////////////////////////////////////////

-- ============================================================
-- 3A. Resumen de datos cargados
-- ============================================================
SELECT 'IC_Llamado' AS Tabla, COUNT(*) AS Registros FROM ALMA_Consultor.IC_Llamado
UNION ALL
SELECT 'Cx_Pabellon', COUNT(*) FROM ALMA_Consultor.Cx_Pabellon
UNION ALL
SELECT 'Cx_Endoscopia', COUNT(*) FROM ALMA_Consultor.Cx_Endoscopia
UNION ALL
SELECT 'Cx_Menor', COUNT(*) FROM ALMA_Consultor.Cx_Menor
UNION ALL
SELECT 'Procedimientos', COUNT(*) FROM ALMA_Consultor.Procedimientos;

-- ============================================================
-- 3B. Vista clinica: IC con cirugia asociada (TOP 50)
-- ============================================================
SELECT TOP 50
    Paciente,
    RUN,
    Edad,
    Tipo_Consultoria,
    Servicio_Origen,
    Fecha_Orden,
    Hora_Orden,
    Estado_IC,
    Medico_Solicitante,
    Profesional_Contactado,
    Metodo_Contacto,
    Hrs_Solicitud_a_Contacto,
    Hrs_Solicitud_a_Ejecucion,
    Cx_Procedimiento,
    Cx_Codigo,
    Cx_Procedimientos_Secundarios,
    Cx_Cirujano,
    Cx_Ayudante,
    Cx_Rol_Medico_IC,
    Cx_Estado,
    Cx_Horas_Post_IC,
    Hrs_Solicitud_a_Pabellon
FROM ALMA_Consultor.V_Resumen_Clinico
WHERE Tiene_Cirugia = 1
ORDER BY Fecha_Orden DESC;

-- ============================================================
-- 3C. IC sin cirugia (solo consultoria pura)
-- ============================================================
SELECT TOP 50
    Paciente,
    Tipo_Consultoria,
    Servicio_Origen,
    Fecha_Orden,
    Hora_Orden,
    Estado_IC,
    Medico_Solicitante,
    Profesional_Contactado,
    Hrs_Solicitud_a_Contacto
FROM ALMA_Consultor.V_Resumen_Clinico
WHERE Tiene_Cirugia = 0
  AND Tiene_Procedimiento = 0
ORDER BY Fecha_Orden DESC;

-- ============================================================
-- 3D. Indicadores por servicio de origen
-- ============================================================
SELECT
    Servicio_Origen,
    COUNT(*)                              AS Total_IC,
    AVG(Hrs_Solicitud_a_Contacto)         AS Prom_Hrs_Contacto,
    AVG(Hrs_Solicitud_a_Pabellon)         AS Prom_Hrs_Pabellon,
    SUM(Tiene_Cirugia)                    AS Con_Cirugia,
    SUM(Tiene_Procedimiento)              AS Con_Procedimiento
FROM ALMA_Consultor.V_Resumen_Clinico
GROUP BY Servicio_Origen
ORDER BY Total_IC DESC;

-- ============================================================
-- 3E. Indicadores por especialidad (grupo receptor)
-- ============================================================
SELECT
    ic.Grupo_Desc                         AS Especialidad,
    COUNT(*)                              AS Total_IC,
    SUM(CASE WHEN ic.Estado_Desc = 'Ejecutado' THEN 1 ELSE 0 END) AS Ejecutados,
    SUM(CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END)           AS Con_Cirugia,
    AVG(DATEDIFF(HOUR, ic.Fecha_Orden, ic.Fecha_Contacto))       AS Prom_Hrs_Contacto
FROM ALMA_Consultor.IC_Llamado ic
LEFT JOIN ALMA_Consultor.Cx_Pabellon cx ON cx.Orden_RowId = ic.Orden_RowId
GROUP BY ic.Grupo_Desc
ORDER BY Total_IC DESC;

-- ============================================================
-- 3F. Detalle cirugias con codigos FONASA
-- ============================================================
SELECT
    cx.Orden_RowId,
    ic.Apellidos + ', ' + ic.Nombres  AS Paciente,
    ic.RUN,
    ic.Fecha_Orden,
    ic.Hora_Orden,
    cx.Fecha_Operacion,
    cx.Hora_Operacion,
    cx.Operacion_Cod                  AS Cod_FONASA,
    cx.Operacion_Desc                 AS Procedimiento_Principal,
    cx.Procedimientos_Sec             AS Procedimientos_Secundarios,
    cx.Cirujano_Desc,
    cx.Ayudante_Desc,
    cx.Estado_Pabellon_Desc,
    cx.Rol_Medico_IC,
    cx.Horas_Post_IC
FROM ALMA_Consultor.Cx_Pabellon cx
JOIN ALMA_Consultor.IC_Llamado ic ON cx.Orden_RowId = ic.Orden_RowId
ORDER BY cx.Fecha_Operacion DESC;

-- ============================================================
-- 3G. Procedimientos menores fuera de pabellon
-- ============================================================
SELECT
    pr.Orden_RowId,
    ic.Apellidos + ', ' + ic.Nombres  AS Paciente,
    ic.RUN,
    ic.Fecha_Orden                    AS Fecha_IC,
    pr.Fecha_Procedimiento,
    pr.Profesional_Desc,
    pr.Notas,
    pr.Horas_Post_IC
FROM ALMA_Consultor.Procedimientos pr
JOIN ALMA_Consultor.IC_Llamado ic ON pr.Orden_RowId = ic.Orden_RowId
ORDER BY pr.Fecha_Procedimiento DESC;

-- ============================================================
-- 3H. Top medicos consultores (por volumen de IC)
-- ============================================================
SELECT TOP 20
    ic.Profesional_Desc               AS Medico_Consultor,
    COUNT(*)                          AS Total_IC,
    SUM(CASE WHEN cx.ID IS NOT NULL THEN 1 ELSE 0 END)  AS Derivo_Cirugia,
    MIN(ic.Fecha_Orden)               AS Primera_IC,
    MAX(ic.Fecha_Orden)               AS Ultima_IC
FROM ALMA_Consultor.IC_Llamado ic
LEFT JOIN ALMA_Consultor.Cx_Pabellon cx ON cx.Orden_RowId = ic.Orden_RowId
WHERE ic.Profesional_Desc IS NOT NULL
GROUP BY ic.Profesional_Desc
ORDER BY Total_IC DESC;


-- ================================================================
-- LOGICA DE CRUCE (documentacion para el DBA)
-- ================================================================
-- El ETL cruza cirugias con IC usando esta logica:
--
-- 1. Mismo paciente: PAADM_PAPMI_DR del episodio de cirugia
--    = PAPMI_RowId del paciente de la IC
--
-- 2. Ventana temporal 48h: Fecha_Operacion entre
--    [Fecha_Orden, Fecha_Orden + 2 dias]
--
-- 3. Mismo medico: RBOP_Surgeon_DR o RBOP_SurgeonAssist_DR
--    = ENQ_CTCP_DR (profesional contactado en la IC)
--
-- 4. Clasificacion:
--    - RBOP_Endoscopy = 'Y'   -> Cx_Endoscopia
--    - RBOP_DaySurgery = 'Y'  -> Cx_Menor
--    - Otro                   -> Cx_Pabellon
--
-- 5. Estados pabellon:
--    A  = Agendado
--    B  = Reservado (Booked)
--    D  = Dado de alta
--    DP = Egresado de quirofano
--    P  = Pre-operatorio
--    R  = Recuperacion
--    X  = Cancelado
--
-- 6. Horas_Post_IC: diferencia en horas entre fecha+hora de la
--    orden IC y fecha+hora de la cirugia/procedimiento
--
-- 7. Conversion $HOROLOG:
--    Fecha: DATEADD(DAY, valor, '1840-12-31')
--    Hora:  DATEADD(SECOND, valor, '00:00:00')
-- ================================================================
