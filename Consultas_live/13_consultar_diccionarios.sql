-- ============================================
-- CONSULTAS DE DICCIONARIOS LIVE -> SIDRA
-- Servidor LIVE: 10.63.180.25:51773 (LIVE-CLOV)
-- Servidor SIDRA: 10.67.119.135 (DB_SIDRA_TEST)
-- Fecha: 2026-01-31
-- ============================================
-- Ejecutar cada seccion por separado para no saturar

-- =============================================
-- PARTE 1: VERIFICAR ESTADO ACTUAL EN SIDRA
-- (Ejecutar en SQL Server - SIDRA)
-- =============================================

-- 1.1 Resumen de registros por diccionario
SELECT 'ALMA_RRHH.DIC_Especialidades' AS Tabla, COUNT(*) AS Registros FROM ALMA_RRHH.DIC_Especialidades UNION ALL
SELECT 'ALMA_RRHH.DIC_GruposSeguridad', COUNT(*) FROM ALMA_RRHH.DIC_GruposSeguridad UNION ALL
SELECT 'ALMA_RRHH.CFG_Perfiles', COUNT(*) FROM ALMA_RRHH.CFG_Perfiles UNION ALL
SELECT 'ALMA_Estructura.DIC_Hospitales', COUNT(*) FROM ALMA_Estructura.DIC_Hospitales UNION ALL
SELECT 'ALMA_Estructura.DIC_Departamentos', COUNT(*) FROM ALMA_Estructura.DIC_Departamentos UNION ALL
SELECT 'ALMA_Clinico.DIC_CIE10', COUNT(*) FROM ALMA_Clinico.DIC_CIE10 UNION ALL
SELECT 'ALMA_Clinico.DIC_CIE10Edicion', COUNT(*) FROM ALMA_Clinico.DIC_CIE10Edicion UNION ALL
SELECT 'ALMA_Clinico.DIC_Medicamentos', COUNT(*) FROM ALMA_Clinico.DIC_Medicamentos UNION ALL
SELECT 'ALMA_Clinico.DIC_CategoriaAlergia', COUNT(*) FROM ALMA_Clinico.DIC_CategoriaAlergia UNION ALL
SELECT 'ALMA_Clinico.DIC_SeveridadAlergia', COUNT(*) FROM ALMA_Clinico.DIC_SeveridadAlergia UNION ALL
SELECT 'ALMA_Clinico.DIC_ProcedimientoLab', COUNT(*) FROM ALMA_Clinico.DIC_ProcedimientoLab UNION ALL
SELECT 'ALMA_Paciente.DIC_Paises', COUNT(*) FROM ALMA_Paciente.DIC_Paises UNION ALL
SELECT 'ALMA_Paciente.DIC_Regiones', COUNT(*) FROM ALMA_Paciente.DIC_Regiones UNION ALL
SELECT 'ALMA_Paciente.DIC_Comunas', COUNT(*) FROM ALMA_Paciente.DIC_Comunas UNION ALL
SELECT 'ALMA_Paciente.DIC_Sexo', COUNT(*) FROM ALMA_Paciente.DIC_Sexo UNION ALL
SELECT 'ALMA_Paciente.DIC_EstadoCivil', COUNT(*) FROM ALMA_Paciente.DIC_EstadoCivil UNION ALL
SELECT 'ALMA_Paciente.DIC_Etnias', COUNT(*) FROM ALMA_Paciente.DIC_Etnias UNION ALL
SELECT 'ALMA_Paciente.DIC_Educacion', COUNT(*) FROM ALMA_Paciente.DIC_Educacion UNION ALL
SELECT 'ALMA_Paciente.DIC_Ocupaciones', COUNT(*) FROM ALMA_Paciente.DIC_Ocupaciones UNION ALL
SELECT 'ALMA_Paciente.DIC_Religiones', COUNT(*) FROM ALMA_Paciente.DIC_Religiones UNION ALL
SELECT 'ALMA_Paciente.DIC_Nacionalidades', COUNT(*) FROM ALMA_Paciente.DIC_Nacionalidades UNION ALL
SELECT 'ALMA_Paciente.DIC_Parentescos', COUNT(*) FROM ALMA_Paciente.DIC_Parentescos UNION ALL
SELECT 'ALMA_Paciente.DIC_GrupoSanguineo', COUNT(*) FROM ALMA_Paciente.DIC_GrupoSanguineo UNION ALL
SELECT 'ALMA_Paciente.DIC_Titulos', COUNT(*) FROM ALMA_Paciente.DIC_Titulos UNION ALL
SELECT 'ALMA_Paciente.DIC_Idiomas', COUNT(*) FROM ALMA_Paciente.DIC_Idiomas UNION ALL
SELECT 'ALMA_Paciente.DIC_TiposPrevision', COUNT(*) FROM ALMA_Paciente.DIC_TiposPrevision UNION ALL
SELECT 'ALMA_Paciente.DIC_CategoriasPrevision', COUNT(*) FROM ALMA_Paciente.DIC_CategoriasPrevision
ORDER BY Tabla;


-- =============================================
-- PARTE 2: CONSULTAS EN LIVE (TrakCare/IRIS)
-- (Ejecutar en IRIS Management Portal o DBeaver)
-- =============================================

-- =========================================
-- SCHEMA: ALMA_RRHH (Recursos Humanos)
-- =========================================

-- 2.1 DIC_Especialidades (CT_Spec)
SELECT CTSPC_RowId AS ID, CTSPC_Code AS Codigo, CTSPC_Desc AS Descripcion
FROM SQLUser.CT_Spec
ORDER BY CTSPC_Desc;

-- 2.2 DIC_GruposSeguridad (SS_Group)
SELECT SSGRP_RowId AS ID, SSGRP_Desc AS Descripcion
FROM SQLUser.SS_Group
ORDER BY SSGRP_Desc;

-- 2.3 CFG_Perfiles (SS_Profile)
SELECT SSP_RowID AS ID, SSP_Code AS Codigo, SSP_Desc AS Descripcion, SSP_DateFrom AS FechaDesde, SSP_DateTo AS FechaHasta
FROM SQLUser.SS_Profile
ORDER BY SSP_Desc;

-- =========================================
-- SCHEMA: ALMA_Estructura (Organizacion)
-- =========================================

-- 2.4 DIC_Hospitales (CT_Hospital)
SELECT HOSP_RowId AS ID, HOSP_Code AS Codigo, HOSP_Desc AS Descripcion
FROM SQLUser.CT_Hospital
ORDER BY HOSP_Desc;

-- 2.5 DIC_Departamentos (CT_Loc) - TOP 100 para no saturar
SELECT TOP 100 CTLOC_RowId AS ID, CTLOC_Code AS Codigo, CTLOC_Desc AS Descripcion, CTLOC_Type AS Tipo
FROM SQLUser.CT_Loc
ORDER BY CTLOC_Desc;

-- =========================================
-- SCHEMA: ALMA_Clinico (Datos Clinicos)
-- =========================================

-- 2.6 DIC_CIE10Edicion (MRC_ICDEdition)
SELECT ICDED_RowId AS ID, ICDED_Code AS Codigo, ICDED_Desc AS Descripcion, ICDED_DateFrom AS FechaDesde, ICDED_DateTo AS FechaHasta
FROM SQLUser.MRC_ICDEdition
ORDER BY ICDED_Code;

-- 2.7 DIC_CIE10 (MRC_ICDDx) - TOP 50 ejemplo
SELECT TOP 50 MRCID_RowId AS ID, MRCID_Code AS Codigo, MRCID_Desc AS Descripcion, MRCID_ShortDesc AS DescCorta
FROM SQLUser.MRC_ICDDx
WHERE MRCID_DateTo IS NULL
ORDER BY MRCID_Code;

-- 2.8 DIC_Medicamentos (PHC_DrgMast) - TOP 50 ejemplo
SELECT TOP 50 PHCD_RowId AS ID, PHCD_Code AS Codigo, PHCD_Name AS Nombre, PHCD_ProductName AS NombreProducto
FROM SQLUser.PHC_DrgMast
WHERE PHCD_DateTo IS NULL
ORDER BY PHCD_Name;

-- 2.9 DIC_CategoriaAlergia (PAC_AllergyCategory)
SELECT ALRGCAT_RowId AS ID, ALRGCAT_Code AS Codigo, ALRGCAT_Desc AS Descripcion, ALRGCAT_AllergySeverity_DR AS SeveridadID, ALRGCAT_IsSensitivity AS EsSensibilidad
FROM SQLUser.PAC_AllergyCategory
WHERE ALRGCAT_DateTo IS NULL
ORDER BY ALRGCAT_Desc;

-- 2.10 DIC_SeveridadAlergia (PAC_AllergySeverity)
SELECT ALRGSEV_RowId AS ID, ALRGSEV_Code AS Codigo, ALRGSEV_Desc AS Descripcion
FROM SQLUser.PAC_AllergySeverity
WHERE ALRGSEV_DateTo IS NULL
ORDER BY ALRGSEV_Desc;

-- 2.11 DIC_ProcedimientoLab (LBC_Procedure) - TOP 50 ejemplo
SELECT TOP 50 LBCPR_RowId AS ID, LBCPR_Code AS Codigo, LBCPR_Desc AS Descripcion
FROM SQLUser.LBC_Procedure
WHERE LBCPR_DateTo IS NULL
ORDER BY LBCPR_Code;

-- =========================================
-- SCHEMA: ALMA_Paciente (Demografia)
-- =========================================

-- 2.12 DIC_Paises (CT_Country)
SELECT CTCOU_RowId AS ID, CTCOU_Code AS Codigo, CTCOU_Desc AS Descripcion, CTCOU_Iso3166Alpha2Code AS ISO2, CTCOU_Iso3166Alpha3Code AS ISO3
FROM SQLUser.CT_Country
WHERE CTCOU_DateTo IS NULL
ORDER BY CTCOU_Desc;

-- 2.13 DIC_Regiones (CT_Region)
SELECT CTRG_RowId AS ID, CTRG_Code AS Codigo, CTRG_Desc AS Descripcion, CTRG_Country_DR AS PaisID
FROM SQLUser.CT_Region
WHERE CTRG_DateTo IS NULL
ORDER BY CTRG_Code;

-- 2.14 DIC_Comunas (CT_City) - TOP 100 para no saturar
SELECT TOP 100 CTCIT_RowId AS ID, CTCIT_Code AS Codigo, CTCIT_Desc AS Descripcion, CTCIT_NationalCode AS CodNacional, CTCIT_Region_DR AS RegionID
FROM SQLUser.CT_City
WHERE CTCIT_DateTo IS NULL
ORDER BY CTCIT_Code;

-- 2.15 DIC_Sexo (CT_Sex)
SELECT CTSEX_RowId AS ID, CTSEX_Code AS Codigo, CTSEX_Desc AS Descripcion
FROM SQLUser.CT_Sex
WHERE CTSEX_DateTo IS NULL
ORDER BY CTSEX_Code;

-- 2.16 DIC_EstadoCivil (CT_Marital)
SELECT CTMAR_RowId AS ID, CTMAR_Code AS Codigo, CTMAR_Desc AS Descripcion
FROM SQLUser.CT_Marital
WHERE CTMAR_DateTo IS NULL
ORDER BY CTMAR_Code;

-- 2.17 DIC_Etnias (CT_Ethnicity)
SELECT CTET_RowId AS ID, CTET_Code AS Codigo, CTET_Desc AS Descripcion
FROM SQLUser.CT_Ethnicity
ORDER BY CTET_Code;

-- 2.18 DIC_Educacion (CT_Education)
SELECT EDU_RowId AS ID, EDU_Code AS Codigo, EDU_Desc AS Descripcion
FROM SQLUser.CT_Education
WHERE EDU_DateTo IS NULL
ORDER BY EDU_Code;

-- 2.19 DIC_Ocupaciones (CT_Occupation) - TOP 50
SELECT TOP 50 CTOCC_RowId AS ID, CTOCC_Code AS Codigo, CTOCC_Desc AS Descripcion
FROM SQLUser.CT_Occupation
WHERE CTOCC_DateTo IS NULL
ORDER BY CTOCC_Code;

-- 2.20 DIC_Religiones (CT_Religion)
SELECT CTRLG_RowId AS ID, CTRLG_Code AS Codigo, CTRLG_Desc AS Descripcion
FROM SQLUser.CT_Religion
WHERE CTRLG_DateTo IS NULL
ORDER BY CTRLG_Code;

-- 2.21 DIC_Nacionalidades (CT_Nation)
SELECT CTNAT_RowId AS ID, CTNAT_Code AS Codigo, CTNAT_Desc AS Descripcion, CTNAT_Iso3166Alpha2Code AS ISO2, CTNAT_Iso3166Alpha3Code AS ISO3
FROM SQLUser.CT_Nation
WHERE CTNAT_DateTo IS NULL
ORDER BY CTNAT_Desc;

-- 2.22 DIC_Parentescos (CT_Relation)
SELECT CTRLT_RowId AS ID, CTRLT_Code AS Codigo, CTRLT_Desc AS Descripcion
FROM SQLUser.CT_Relation
WHERE CTRLT_DateTo IS NULL
ORDER BY CTRLT_Code;

-- 2.23 DIC_GrupoSanguineo (PAC_BloodType)
SELECT BLDT_RowId AS ID, BLDT_Code AS Codigo, BLDT_Desc AS Descripcion
FROM SQLUser.PAC_BloodType
WHERE BLDT_DateTo IS NULL
ORDER BY BLDT_Code;

-- 2.24 DIC_Titulos (CT_Title)
SELECT TTL_RowId AS ID, TTL_Code AS Codigo, TTL_Desc AS Descripcion
FROM SQLUser.CT_Title
WHERE TTL_DateTo IS NULL
ORDER BY TTL_Code;

-- 2.25 DIC_Idiomas (PAC_PreferredLanguage)
SELECT PREFL_RowId AS ID, PREFL_Code AS Codigo, PREFL_Desc AS Descripcion, PREFL_ISOCode AS CodigoISO
FROM SQLUser.PAC_PreferredLanguage
WHERE PREFL_DateTo IS NULL
ORDER BY PREFL_Code;

-- 2.26 DIC_TiposPrevision (ARC_InsuranceType)
SELECT INST_RowId AS ID, INST_Code AS Codigo, INST_Desc AS Descripcion, INST_CareType AS TipoCuidado
FROM SQLUser.ARC_InsuranceType
WHERE INST_DateTo IS NULL
ORDER BY INST_Code;

-- 2.27 DIC_CategoriasPrevision (ARC_InsuranceCategory)
SELECT INSC_RowId AS ID, INSC_Code AS Codigo, INSC_Desc AS Descripcion
FROM SQLUser.ARC_InsuranceCategory
WHERE INSC_DateTo IS NULL
ORDER BY INSC_Code;


-- =============================================
-- PARTE 3: CONTEO EN LIVE (resumen rapido)
-- (Ejecutar en IRIS para comparar)
-- =============================================
SELECT 'CT_Spec' AS Tabla, COUNT(*) AS Total FROM SQLUser.CT_Spec UNION ALL
SELECT 'SS_Group', COUNT(*) FROM SQLUser.SS_Group UNION ALL
SELECT 'SS_Profile', COUNT(*) FROM SQLUser.SS_Profile UNION ALL
SELECT 'CT_Hospital', COUNT(*) FROM SQLUser.CT_Hospital UNION ALL
SELECT 'CT_Loc', COUNT(*) FROM SQLUser.CT_Loc UNION ALL
SELECT 'MRC_ICDEdition', COUNT(*) FROM SQLUser.MRC_ICDEdition UNION ALL
SELECT 'MRC_ICDDx (activos)', COUNT(*) FROM SQLUser.MRC_ICDDx WHERE MRCID_DateTo IS NULL UNION ALL
SELECT 'PHC_DrgMast (activos)', COUNT(*) FROM SQLUser.PHC_DrgMast WHERE PHCD_DateTo IS NULL UNION ALL
SELECT 'PAC_AllergyCategory', COUNT(*) FROM SQLUser.PAC_AllergyCategory WHERE ALRGCAT_DateTo IS NULL UNION ALL
SELECT 'PAC_AllergySeverity', COUNT(*) FROM SQLUser.PAC_AllergySeverity WHERE ALRGSEV_DateTo IS NULL UNION ALL
SELECT 'LBC_Procedure (activos)', COUNT(*) FROM SQLUser.LBC_Procedure WHERE LBCPR_DateTo IS NULL UNION ALL
SELECT 'CT_Country', COUNT(*) FROM SQLUser.CT_Country WHERE CTCOU_DateTo IS NULL UNION ALL
SELECT 'CT_Region', COUNT(*) FROM SQLUser.CT_Region WHERE CTRG_DateTo IS NULL UNION ALL
SELECT 'CT_City', COUNT(*) FROM SQLUser.CT_City WHERE CTCIT_DateTo IS NULL UNION ALL
SELECT 'CT_Sex', COUNT(*) FROM SQLUser.CT_Sex WHERE CTSEX_DateTo IS NULL UNION ALL
SELECT 'CT_Marital', COUNT(*) FROM SQLUser.CT_Marital WHERE CTMAR_DateTo IS NULL UNION ALL
SELECT 'CT_Ethnicity', COUNT(*) FROM SQLUser.CT_Ethnicity UNION ALL
SELECT 'CT_Education', COUNT(*) FROM SQLUser.CT_Education WHERE EDU_DateTo IS NULL UNION ALL
SELECT 'CT_Occupation', COUNT(*) FROM SQLUser.CT_Occupation WHERE CTOCC_DateTo IS NULL UNION ALL
SELECT 'CT_Religion', COUNT(*) FROM SQLUser.CT_Religion WHERE CTRLG_DateTo IS NULL UNION ALL
SELECT 'CT_Nation', COUNT(*) FROM SQLUser.CT_Nation WHERE CTNAT_DateTo IS NULL UNION ALL
SELECT 'CT_Relation', COUNT(*) FROM SQLUser.CT_Relation WHERE CTRLT_DateTo IS NULL UNION ALL
SELECT 'PAC_BloodType', COUNT(*) FROM SQLUser.PAC_BloodType WHERE BLDT_DateTo IS NULL UNION ALL
SELECT 'CT_Title', COUNT(*) FROM SQLUser.CT_Title WHERE TTL_DateTo IS NULL UNION ALL
SELECT 'PAC_PreferredLanguage', COUNT(*) FROM SQLUser.PAC_PreferredLanguage WHERE PREFL_DateTo IS NULL UNION ALL
SELECT 'ARC_InsuranceType', COUNT(*) FROM SQLUser.ARC_InsuranceType WHERE INST_DateTo IS NULL UNION ALL
SELECT 'ARC_InsuranceCategory', COUNT(*) FROM SQLUser.ARC_InsuranceCategory WHERE INSC_DateTo IS NULL
ORDER BY Tabla;


-- =============================================
-- INSTRUCCIONES
-- =============================================
-- 1. Ejecutar PARTE 1 en SIDRA para ver estado actual
-- 2. Ejecutar PARTE 3 en LIVE para ver conteos
-- 3. Ejecutar consultas individuales de PARTE 2 segun necesites ver contenido
-- 4. Para sincronizar, ejecutar: python sync_alma_sidra.py
