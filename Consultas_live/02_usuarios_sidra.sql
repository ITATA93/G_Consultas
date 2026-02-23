-- ============================================
-- CONSULTA: Datos ALMA desde SIDRA
-- Servidor: SIDRA (10.67.119.135)
-- Base de datos: DB_SIDRA_TEST
-- Fecha: 2026-01-30
-- ============================================

-- ===========================================
-- ESTRUCTURA DE SCHEMAS
-- ===========================================
-- ALMA_RRHH        -> Recursos Humanos (usuarios, prestadores)
-- ALMA_Estructura  -> Organizacion (hospitales, departamentos)
-- ALMA_Clinico     -> Datos clinicos (CIE-10, medicamentos) [futuro]
-- ALMA_Meta        -> Metadata (queries de extraccion)

-- ===========================================
-- 1. USUARIOS COMPLETO CON JOINS
-- ===========================================
SELECT
    U.ID,
    U.RUT,
    U.Apellido,
    U.Nombre,
    U.NombreCompleto,
    U.GrupoSeguridad,
    U.Departamento,
    U.Hospital,
    U.CareProvider,
    U.Perfil,
    E.Descripcion AS Especialidad,
    U.Activo
FROM ALMA_RRHH.MAE_Usuarios U
LEFT JOIN ALMA_RRHH.MAE_CareProviders CP ON U.CareProviderID = CP.ID
LEFT JOIN ALMA_RRHH.DIC_Especialidades E ON CP.EspecialidadID = E.ID
ORDER BY U.Apellido, U.Nombre;

-- ===========================================
-- 2. CONTEO POR GRUPO DE SEGURIDAD
-- ===========================================
SELECT
    GrupoSeguridad,
    COUNT(*) AS Cantidad
FROM ALMA_RRHH.MAE_Usuarios
GROUP BY GrupoSeguridad
ORDER BY COUNT(*) DESC;

-- ===========================================
-- 3. USUARIOS POR DEPARTAMENTO
-- ===========================================
SELECT
    Departamento,
    COUNT(*) AS Cantidad
FROM ALMA_RRHH.MAE_Usuarios
GROUP BY Departamento
ORDER BY COUNT(*) DESC;

-- ===========================================
-- 4. USUARIOS POR PERFIL
-- ===========================================
SELECT
    Perfil,
    COUNT(*) AS Cantidad
FROM ALMA_RRHH.MAE_Usuarios
WHERE Perfil IS NOT NULL
GROUP BY Perfil
ORDER BY COUNT(*) DESC;

-- ===========================================
-- 5. PRESTADORES CON ESPECIALIDAD
-- ===========================================
SELECT
    CP.Descripcion AS Prestador,
    E.Descripcion AS Especialidad
FROM ALMA_RRHH.MAE_CareProviders CP
INNER JOIN ALMA_RRHH.DIC_Especialidades E ON CP.EspecialidadID = E.ID
ORDER BY E.Descripcion, CP.Descripcion;

-- ===========================================
-- 6. ESTADISTICAS GENERALES
-- ===========================================
SELECT 'MAE_Usuarios' AS Tabla, COUNT(*) AS Registros FROM ALMA_RRHH.MAE_Usuarios
UNION ALL
SELECT 'MAE_CareProviders', COUNT(*) FROM ALMA_RRHH.MAE_CareProviders
UNION ALL
SELECT 'DIC_Especialidades', COUNT(*) FROM ALMA_RRHH.DIC_Especialidades
UNION ALL
SELECT 'DIC_GruposSeguridad', COUNT(*) FROM ALMA_RRHH.DIC_GruposSeguridad
UNION ALL
SELECT 'CFG_Perfiles', COUNT(*) FROM ALMA_RRHH.CFG_Perfiles
UNION ALL
SELECT 'DIC_Hospitales', COUNT(*) FROM ALMA_Estructura.DIC_Hospitales
UNION ALL
SELECT 'DIC_Departamentos', COUNT(*) FROM ALMA_Estructura.DIC_Departamentos;

-- ===========================================
-- 7. QUERIES DE EXTRACCION (METADATA)
-- ===========================================
SELECT
    SchemaDestino,
    TablaDestino,
    TipoTabla,
    Descripcion,
    FrecuenciaSinc,
    UltimaSinc,
    Registros
FROM ALMA_Meta.CFG_Queries
ORDER BY SchemaDestino, TablaDestino;

-- ============================================
-- ESTRUCTURA DE TABLAS
-- ============================================
-- ALMA_RRHH.MAE_Usuarios
--   +-- GrupoID -----------> DIC_GruposSeguridad
--   +-- DepartamentoID ----> ALMA_Estructura.DIC_Departamentos
--   +-- HospitalID --------> ALMA_Estructura.DIC_Hospitales
--   +-- CareProviderID ----> MAE_CareProviders
--   |                           +-- EspecialidadID --> DIC_Especialidades
--   +-- PerfilID ----------> CFG_Perfiles

-- ============================================
-- NOMENCLATURA DE TABLAS
-- ============================================
-- MAE_ = Maestro (entidades principales)
-- DIC_ = Diccionario (catalogos/listas)
-- CFG_ = Configuracion (parametros)
-- EVT_ = Eventos (transacciones/logs)

-- ============================================
-- CONEXION
-- ============================================
-- Servidor: 10.67.119.135
-- Base de datos: DB_SIDRA_TEST
-- Usuario: sidra
