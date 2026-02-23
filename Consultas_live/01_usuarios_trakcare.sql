-- ============================================
-- CONSULTA: Usuarios del Sistema TrakCare
-- Servidor: LIVE-CLOV (10.63.180.25:51773)
-- Tablas: SS_User, SS_Group, SS_UserGroups, SS_UserLogin
-- Fecha: 2026-01-30
-- ============================================

-- ===========================================
-- 1. USUARIOS COMPLETO (todos los campos usados)
-- ===========================================
SELECT
    U.SSUSR_RowId AS ID,
    U.SSUSR_Initials AS RUT,
    U.SSUSR_Surname AS Apellido,
    U.SSUSR_GivenName AS Nombre,
    U.SSUSR_Name AS NombreCompleto,
    G.SSGRP_Desc AS GrupoSeguridad,
    D.CTLOC_Desc AS Departamento,
    H.HOSP_Desc AS Hospital,
    CP.CTPCP_Desc AS CareProvider,
    U.SSUSR_DateLastLogin AS UltimoLogin,
    U.SSUSR_Active AS Activo
FROM SQLUser.SS_User U
LEFT JOIN SQLUser.SS_Group G ON U.SSUSR_Group = G.SSGRP_RowId
LEFT JOIN SQLUser.CT_Loc D ON U.SSUSR_DefaultDept_DR = D.CTLOC_RowId
LEFT JOIN SQLUser.CT_Hospital H ON U.SSUSR_Hospital_DR = H.HOSP_RowId
LEFT JOIN SQLUser.CT_CareProv CP ON U.SSUSR_CareProv_DR = CP.CTPCP_RowId
WHERE U.SSUSR_Active = 'Y'
ORDER BY U.SSUSR_Surname, U.SSUSR_GivenName;

-- ===========================================
-- 2. CONTEO POR GRUPO DE SEGURIDAD
-- ===========================================
SELECT
    G.SSGRP_Desc AS Grupo,
    COUNT(*) AS Cantidad
FROM SQLUser.SS_User U
LEFT JOIN SQLUser.SS_Group G ON U.SSUSR_Group = G.SSGRP_RowId
WHERE U.SSUSR_Active = 'Y'
GROUP BY G.SSGRP_Desc
ORDER BY COUNT(*) DESC;

-- ===========================================
-- 3. HISTORIAL DE LOGINS (ultimos 30 dias)
-- ===========================================
SELECT TOP 100
    U.SSUSR_Name AS Usuario,
    L.LOG_LogonDate AS Fecha,
    L.LOG_LogonTime AS HoraEntrada,
    L.LOG_LogoffTime AS HoraSalida,
    L.LOG_ComputerName AS Equipo
FROM SQLUser.SS_UserLogin L
INNER JOIN SQLUser.SS_User U ON L.LOG_User_DR = U.SSUSR_RowId
WHERE L.LOG_LogonDate >= DATEADD('day', -30, CURRENT_DATE)
ORDER BY L.LOG_LogonDate DESC, L.LOG_LogonTime DESC;

-- ===========================================
-- 4. ESTADISTICAS GENERALES
-- ===========================================
SELECT COUNT(*) AS Total FROM SQLUser.SS_User;
-- Total: 1,973

SELECT SSUSR_Active, COUNT(*) FROM SQLUser.SS_User GROUP BY SSUSR_Active;
-- Y: 1,509 activos
-- N: 464 inactivos

-- ============================================
-- TABLAS RELACIONADAS CON USUARIOS
-- ============================================
-- SS_User              -> Usuario principal
-- SS_Group             -> Grupos de seguridad
-- SS_UserGroups        -> Grupos adicionales del usuario
-- SS_UserArea          -> Areas asignadas
-- SS_UserLogin         -> Historial de logins
-- SS_UserSettings      -> Configuraciones personales
-- SS_UserDepartFunction-> Funciones por departamento
-- SS_UserOrderCategory -> Categorias de ordenes permitidas

-- ============================================
-- NOTAS
-- ============================================
-- El campo SSUSR_Initials contiene el RUT en este hospital
-- Los flags DoctorFlag/NurseFlag no estan siendo usados
-- SSUSR_Group es el grupo PRINCIPAL del usuario
-- SS_UserGroups contiene grupos ADICIONALES
