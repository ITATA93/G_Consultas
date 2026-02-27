-- ============================================================
-- DEMO: ALMA_Consultor en SIDRA-TEST
-- Schema ya creado y cargado con datos de 3 meses
-- Ejecutar estas queries en SSMS contra DB_SIDRA_TEST
-- ============================================================

-- 1. Resumen de datos cargados
SELECT 'IC_Llamado' AS Tabla, COUNT(*) AS Registros FROM ALMA_Consultor.IC_Llamado
UNION ALL
SELECT 'Cx_Pabellon', COUNT(*) FROM ALMA_Consultor.Cx_Pabellon
UNION ALL
SELECT 'Cx_Endoscopia', COUNT(*) FROM ALMA_Consultor.Cx_Endoscopia
UNION ALL
SELECT 'Cx_Menor', COUNT(*) FROM ALMA_Consultor.Cx_Menor
UNION ALL
SELECT 'Procedimientos', COUNT(*) FROM ALMA_Consultor.Procedimientos;


-- 2. Vista clinica consolidada (muestra 20 registros con cirugia)
SELECT TOP 20
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
    -- Tiempos clinicos
    Hrs_Solicitud_a_Contacto,
    Hrs_Solicitud_a_Ejecucion,
    -- Cirugia asociada
    Cx_Procedimiento,
    Cx_Codigo,
    Cx_Cirujano,
    Cx_Ayudante,
    Cx_Rol_Medico_IC,
    Cx_Estado,
    Cx_Horas_Post_IC,
    Hrs_Solicitud_a_Pabellon
FROM ALMA_Consultor.V_Resumen_Clinico
WHERE Tiene_Cirugia = 1
ORDER BY Fecha_Orden DESC;


-- 3. IC sin cirugia ni procedimiento (solo consultoria)
SELECT TOP 20
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


-- 4. Tiempos promedio por servicio de origen
SELECT
    Servicio_Origen,
    COUNT(*)                              AS Total_IC,
    AVG(Hrs_Solicitud_a_Contacto)         AS Promedio_Hrs_Contacto,
    AVG(Hrs_Solicitud_a_Pabellon)         AS Promedio_Hrs_Pabellon,
    SUM(Tiene_Cirugia)                    AS Con_Cirugia,
    SUM(Tiene_Procedimiento)              AS Con_Procedimiento
FROM ALMA_Consultor.V_Resumen_Clinico
GROUP BY Servicio_Origen
ORDER BY Total_IC DESC;


-- 5. Detalle cirugias: codigos FONASA y procedimientos secundarios
SELECT
    cx.Orden_RowId,
    ic.Apellidos + ', ' + ic.Nombres  AS Paciente,
    ic.Fecha_Orden,
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


-- 6. Procedimientos menores fuera de pabellon
SELECT
    pr.Orden_RowId,
    ic.Apellidos + ', ' + ic.Nombres  AS Paciente,
    ic.Fecha_Orden                    AS Fecha_IC,
    pr.Fecha_Procedimiento,
    pr.Profesional_Desc,
    pr.Notas,
    pr.Horas_Post_IC
FROM ALMA_Consultor.Procedimientos pr
JOIN ALMA_Consultor.IC_Llamado ic ON pr.Orden_RowId = ic.Orden_RowId
ORDER BY pr.Fecha_Procedimiento DESC;


-- ============================================================
-- NOTA PARA DBA:
-- Los datos se cargan via ETL Python (ALMA -> SIDRA-TEST).
-- Para automatizar, opciones:
--   A) Programar el script Python como tarea (6 seg ejecucion)
--   B) Sincronizar tablas ALMA a SIDRA y crear stored procedure
--
-- Tablas ALMA requeridas para opcion B:
--   OE_OrdItem, OE_Order, OE_OrdItem2, OE_OrdStatus
--   PA_Adm, PA_PatMas, PA_Person, PA_EnquiryContact
--   RB_OperatingRoom, RB_OperRoomSecondaryProc, ORC_Operation
--   MR_Adm, MR_Procedures
--   Region_CLXX_Misc_User.OEOrdItem
--   ARC_ItmMast, SS_Group, CT_CareProv, OEC_OrderStatus
--   PAC_RequestStatus, PAC_ContMethod, CTHospital, CTLoc, PAC_Ward
-- ============================================================
