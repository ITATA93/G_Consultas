-- ============================================
-- CREAR SCHEMAS PARA REPORTES ALMA
-- Hospital Dr. Antonio Tirado Lanas - Ovalle
--
-- Servidor: SIDRA (10.67.119.135)
-- Base de datos: DB_SIDRA_TEST
--
-- Ejecutar en SIDRA antes de correr 19_sync_reportes_rem.py
-- ============================================

-- Schema para Reportes REM (Resumen Estadistico Mensual)
-- Contiene: 46 tablas QREM* desde questionnaire
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'ALMA_Reportes_REM')
    EXEC('CREATE SCHEMA ALMA_Reportes_REM');
GO

-- Schema para Reportes de Urgencias
-- Contiene: QCLXXBENEUR, QCLXXREPRAU, QCLXXSAMUR
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'ALMA_Reportes_Urgencias')
    EXEC('CREATE SCHEMA ALMA_Reportes_Urgencias');
GO

-- Schema para Reportes de Salud Mental
-- Contiene: QCLXXFISMUR
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'ALMA_Reportes_SaludMental')
    EXEC('CREATE SCHEMA ALMA_Reportes_SaludMental');
GO

-- Schema para Cuestionarios Clinicos Generales (futuro)
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'ALMA_Reportes_Clinicos')
    EXEC('CREATE SCHEMA ALMA_Reportes_Clinicos');
GO

-- Verificar schemas creados
SELECT name AS SchemaCreado
FROM sys.schemas
WHERE name LIKE 'ALMA_Reportes_%'
ORDER BY name;
