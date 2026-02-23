-- ============================================
-- CREAR TABLAS DEMOGRAFICAS EN ALMA_Paciente
-- Servidor: SIDRA (10.67.119.135)
-- Base de datos: DB_SIDRA_TEST
-- Fecha: 2026-01-30
-- ============================================

-- Ya creado via Python, este archivo es documentacion

-- ===========================================
-- ESTRUCTURA ALMA_Paciente (16 tablas)
-- ===========================================
-- DIC_Paises           -> Paises (ISO 3166)
-- DIC_Regiones         -> Regiones de Chile
-- DIC_Comunas          -> Comunas de Chile
-- DIC_Sexo             -> Sexo biologico
-- DIC_EstadoCivil      -> Estado civil
-- DIC_Etnias           -> Pueblos originarios
-- DIC_Educacion        -> Nivel educacional
-- DIC_Ocupaciones      -> Profesiones/oficios
-- DIC_Religiones       -> Religiones
-- DIC_Nacionalidades   -> Nacionalidades
-- DIC_Parentescos      -> Relaciones familiares
-- DIC_GrupoSanguineo   -> Grupos ABO/Rh
-- DIC_Titulos          -> Titulos (Sr/Sra/Dr)
-- DIC_Idiomas          -> Idiomas preferidos
-- DIC_TiposPrevision   -> FONASA/ISAPRE
-- DIC_CategoriasPrevision -> Categorias A/B/C/D

-- ===========================================
-- CONSULTAS DE EJEMPLO
-- ===========================================

-- Listar todas las comunas de una region
SELECT c.Descripcion AS Comuna, r.Descripcion AS Region
FROM ALMA_Paciente.DIC_Comunas c
JOIN ALMA_Paciente.DIC_Regiones r ON c.RegionID = r.ID
WHERE r.Descripcion LIKE '%Coquimbo%'
ORDER BY c.Descripcion;

-- Tipos de prevision disponibles
SELECT Codigo, Descripcion, TipoCuidado
FROM ALMA_Paciente.DIC_TiposPrevision
ORDER BY Descripcion;

-- Etnias registradas
SELECT Codigo, Descripcion
FROM ALMA_Paciente.DIC_Etnias
ORDER BY Descripcion;

-- ===========================================
-- RELACIONES
-- ===========================================
-- DIC_Comunas.RegionID -> DIC_Regiones.ID
-- DIC_Regiones.PaisID  -> DIC_Paises.ID
