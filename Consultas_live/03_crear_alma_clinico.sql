-- ============================================
-- CREAR TABLAS CLINICAS EN ALMA_Clinico
-- Servidor: SIDRA (10.67.119.135)
-- Base de datos: DB_SIDRA_TEST
-- Fecha: 2026-01-30
-- ============================================

-- ===========================================
-- 1. DIC_CIE10 - Codigos de Diagnostico
-- ===========================================
CREATE TABLE ALMA_Clinico.DIC_CIE10 (
    ID BIGINT PRIMARY KEY,
    Codigo VARCHAR(20),
    Descripcion VARCHAR(500),
    DescripcionCorta VARCHAR(200),
    EdicionID BIGINT,
    Activo VARCHAR(1) DEFAULT 'Y'
);

-- ===========================================
-- 2. DIC_CIE10Edicion - Versiones de CIE
-- ===========================================
CREATE TABLE ALMA_Clinico.DIC_CIE10Edicion (
    ID BIGINT PRIMARY KEY,
    Codigo VARCHAR(20),
    Descripcion VARCHAR(200),
    FechaDesde DATE,
    FechaHasta DATE
);

-- ===========================================
-- 3. DIC_Medicamentos - Farmacos
-- ===========================================
CREATE TABLE ALMA_Clinico.DIC_Medicamentos (
    ID BIGINT PRIMARY KEY,
    Codigo VARCHAR(50),
    Nombre VARCHAR(500),
    NombreProducto VARCHAR(500),
    GenericoID BIGINT,
    Activo VARCHAR(1) DEFAULT 'Y'
);

-- ===========================================
-- 4. DIC_CategoriaAlergia - Tipos de Alergia
-- ===========================================
CREATE TABLE ALMA_Clinico.DIC_CategoriaAlergia (
    ID BIGINT PRIMARY KEY,
    Codigo VARCHAR(20),
    Descripcion VARCHAR(200),
    SeveridadID BIGINT,
    EsSensibilidad VARCHAR(1)
);

-- ===========================================
-- 5. DIC_SeveridadAlergia - Niveles de Severidad
-- ===========================================
CREATE TABLE ALMA_Clinico.DIC_SeveridadAlergia (
    ID BIGINT PRIMARY KEY,
    Codigo VARCHAR(20),
    Descripcion VARCHAR(200)
);

-- ===========================================
-- 6. DIC_ProcedimientoLab - Procedimientos Laboratorio
-- ===========================================
CREATE TABLE ALMA_Clinico.DIC_ProcedimientoLab (
    ID BIGINT PRIMARY KEY,
    Codigo VARCHAR(50),
    Descripcion VARCHAR(500),
    Notas VARCHAR(MAX),
    Activo VARCHAR(1) DEFAULT 'Y'
);

-- ===========================================
-- INSERTAR METADATA EN CFG_Queries
-- ===========================================
INSERT INTO ALMA_Meta.CFG_Queries
(SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen, BaseDatosOrigen, TablaOrigen, QueryExtraccion, Descripcion, FrecuenciaSinc)
VALUES
('ALMA_Clinico', 'DIC_CIE10', 'DIC', 'ALMA', 'LIVE-CLOV', 'MRC_ICDDx',
'SELECT MRCID_RowId, MRCID_Code, MRCID_Desc, MRCID_ShortDesc, MRCID_ICDEdition_DR, MRCID_Active FROM SQLUser.MRC_ICDDx',
'Codigos de diagnostico CIE-10', 'Semanal'),

('ALMA_Clinico', 'DIC_CIE10Edicion', 'DIC', 'ALMA', 'LIVE-CLOV', 'MRC_ICDEdition',
'SELECT ICDED_RowId, ICDED_Code, ICDED_Desc, ICDED_DateFrom, ICDED_DateTo FROM SQLUser.MRC_ICDEdition',
'Ediciones/versiones de CIE-10', 'Mensual'),

('ALMA_Clinico', 'DIC_Medicamentos', 'DIC', 'ALMA', 'LIVE-CLOV', 'PHC_DrgMast',
'SELECT PHCD_RowId, PHCD_Code, PHCD_Name, PHCD_ProductName, PHCD_Generic_DR, PHCD_Active FROM SQLUser.PHC_DrgMast',
'Catalogo de medicamentos/farmacos', 'Semanal'),

('ALMA_Clinico', 'DIC_CategoriaAlergia', 'DIC', 'ALMA', 'LIVE-CLOV', 'PAC_AllergyCategory',
'SELECT ALRGCAT_RowId, ALRGCAT_Code, ALRGCAT_Desc, ALRGCAT_AllergySeverity_DR, ALRGCAT_IsSensitivity FROM SQLUser.PAC_AllergyCategory WHERE ALRGCAT_DateTo IS NULL',
'Categorias de alergias', 'Mensual'),

('ALMA_Clinico', 'DIC_SeveridadAlergia', 'DIC', 'ALMA', 'LIVE-CLOV', 'PAC_AllergySeverity',
'SELECT ALRGSEV_RowId, ALRGSEV_Code, ALRGSEV_Desc FROM SQLUser.PAC_AllergySeverity WHERE ALRGSEV_DateTo IS NULL',
'Niveles de severidad de alergias', 'Mensual'),

('ALMA_Clinico', 'DIC_ProcedimientoLab', 'DIC', 'ALMA', 'LIVE-CLOV', 'LBC_Procedure',
'SELECT LBCPR_RowId, LBCPR_Code, LBCPR_Desc, LBCPR_Notes, LBCPR_Active FROM SQLUser.LBC_Procedure WHERE LBCPR_DateTo IS NULL',
'Procedimientos de laboratorio', 'Semanal');

-- ===========================================
-- VERIFICAR ESTRUCTURA
-- ===========================================
SELECT
    s.name AS [Schema],
    t.name AS Tabla,
    COUNT(c.column_id) AS Columnas
FROM sys.tables t
JOIN sys.schemas s ON t.schema_id = s.schema_id
LEFT JOIN sys.columns c ON t.object_id = c.object_id
WHERE s.name = 'ALMA_Clinico'
GROUP BY s.name, t.name
ORDER BY t.name;

-- Ver queries registradas
SELECT SchemaDestino, TablaDestino, TipoTabla, Descripcion, FrecuenciaSinc
FROM ALMA_Meta.CFG_Queries
WHERE SchemaDestino = 'ALMA_Clinico'
ORDER BY TablaDestino;
