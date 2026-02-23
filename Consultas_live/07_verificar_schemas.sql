-- ============================================
-- VERIFICAR ESTRUCTURA COMPLETA ALMA EN SIDRA
-- Servidor: SIDRA (10.67.119.135)
-- Base de datos: DB_SIDRA_TEST
-- Fecha: 2026-01-30
-- ============================================

-- ===========================================
-- 1. RESUMEN DE SCHEMAS Y TABLAS
-- ===========================================
SELECT
    s.name AS [Schema],
    COUNT(t.name) AS Tablas
FROM sys.schemas s
LEFT JOIN sys.tables t ON s.schema_id = t.schema_id
WHERE s.name LIKE 'ALMA_%'
GROUP BY s.name
ORDER BY s.name;

-- ===========================================
-- 2. DETALLE POR SCHEMA
-- ===========================================

-- ALMA_Quirofano (25 tablas)
SELECT 'ALMA_Quirofano' AS [Schema], name AS Tabla
FROM sys.tables WHERE schema_id = SCHEMA_ID('ALMA_Quirofano')
ORDER BY name;

-- ALMA_Ordenes (25 tablas)
SELECT 'ALMA_Ordenes' AS [Schema], name AS Tabla
FROM sys.tables WHERE schema_id = SCHEMA_ID('ALMA_Ordenes')
ORDER BY name;

-- ALMA_Facturacion (25 tablas)
SELECT 'ALMA_Facturacion' AS [Schema], name AS Tabla
FROM sys.tables WHERE schema_id = SCHEMA_ID('ALMA_Facturacion')
ORDER BY name;

-- ALMA_Inventario (25 tablas)
SELECT 'ALMA_Inventario' AS [Schema], name AS Tabla
FROM sys.tables WHERE schema_id = SCHEMA_ID('ALMA_Inventario')
ORDER BY name;

-- ALMA_BancoSangre (25 tablas)
SELECT 'ALMA_BancoSangre' AS [Schema], name AS Tabla
FROM sys.tables WHERE schema_id = SCHEMA_ID('ALMA_BancoSangre')
ORDER BY name;

-- ALMA_RegistrosMedicos (25 tablas)
SELECT 'ALMA_RegistrosMedicos' AS [Schema], name AS Tabla
FROM sys.tables WHERE schema_id = SCHEMA_ID('ALMA_RegistrosMedicos')
ORDER BY name;

-- ===========================================
-- 3. QUERIES REGISTRADAS EN CFG_Queries
-- ===========================================
SELECT
    SchemaDestino,
    COUNT(*) AS Queries,
    STRING_AGG(TipoTabla, ', ') WITHIN GROUP (ORDER BY TipoTabla) AS Tipos
FROM ALMA_Meta.CFG_Queries
GROUP BY SchemaDestino
ORDER BY SchemaDestino;

-- ===========================================
-- 4. ESTADISTICAS GENERALES
-- ===========================================
SELECT
    'Schemas ALMA' AS Metrica,
    COUNT(DISTINCT s.name) AS Valor
FROM sys.schemas s
WHERE s.name LIKE 'ALMA_%'
UNION ALL
SELECT
    'Tablas totales',
    COUNT(*)
FROM sys.tables t
JOIN sys.schemas s ON t.schema_id = s.schema_id
WHERE s.name LIKE 'ALMA_%'
UNION ALL
SELECT
    'Queries en CFG_Queries',
    COUNT(*)
FROM ALMA_Meta.CFG_Queries;

-- ===========================================
-- 5. MUESTRA DE QUERIES POR SCHEMA NUEVO
-- ===========================================
SELECT TOP 3 SchemaDestino, TablaDestino, TablaOrigen, QueryExtraccion
FROM ALMA_Meta.CFG_Queries
WHERE SchemaDestino = 'ALMA_Quirofano';

SELECT TOP 3 SchemaDestino, TablaDestino, TablaOrigen, QueryExtraccion
FROM ALMA_Meta.CFG_Queries
WHERE SchemaDestino = 'ALMA_Ordenes';

SELECT TOP 3 SchemaDestino, TablaDestino, TablaOrigen, QueryExtraccion
FROM ALMA_Meta.CFG_Queries
WHERE SchemaDestino = 'ALMA_Facturacion';

-- ===========================================
-- NOMENCLATURA DE SCHEMAS
-- ===========================================
-- ALMA_RRHH           -> Recursos Humanos (usuarios, prestadores)
-- ALMA_Estructura     -> Organización (hospitales, departamentos)
-- ALMA_Clinico        -> Datos clínicos (CIE-10, medicamentos, alergias)
-- ALMA_Paciente       -> Demografía (países, comunas, previsión)
-- ALMA_Meta           -> Metadata (queries de extracción)
-- ALMA_Formularios    -> Formularios clínicos TrakCare
-- ALMA_Cuestionarios  -> Escalas y evaluaciones
-- ALMA_Admision       -> Admisión de pacientes
-- ALMA_Laboratorio    -> Laboratorio clínico
-- ALMA_Farmacia       -> Farmacia y medicamentos
-- ALMA_Quirofano      -> Pabellón quirúrgico (NUEVO)
-- ALMA_Ordenes        -> Órdenes médicas (NUEVO)
-- ALMA_Facturacion    -> Facturación (NUEVO)
-- ALMA_Inventario     -> Inventario/stock (NUEVO)
-- ALMA_BancoSangre    -> Hemoterapia (NUEVO)
-- ALMA_RegistrosMedicos -> Registros clínicos (NUEVO)
