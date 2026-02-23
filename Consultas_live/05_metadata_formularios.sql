-- ============================================
-- INSERTAR METADATA DE CAT_Formularios EN CFG_Queries
-- Servidor: SIDRA (10.67.119.135)
-- Base de datos: DB_SIDRA_TEST
-- Fecha: 2026-01-30
-- ============================================

-- ===========================================
-- INSERTAR EN CFG_Queries
-- ===========================================
INSERT INTO ALMA_Meta.CFG_Queries
(SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen, BaseDatosOrigen, TablaOrigen, QueryExtraccion, Descripcion, FrecuenciaSinc)
VALUES
('ALMA_Clinico', 'CAT_Formularios', 'CAT', 'LOCAL', 'diccionario.db', 'questionnaire.QCLXX*',
'-- Catálogo generado desde diccionario local
-- Cada registro tiene su QueryExtraccion propia en la columna QueryExtraccion
-- Ejemplo: SELECT * FROM questionnaire.QCLXXMOCA',
'Catálogo de 320 formularios y cuestionarios TrakCare (76 en uso, 244 sin uso)', 'Manual');

-- ===========================================
-- VERIFICAR INSERCIÓN
-- ===========================================
SELECT SchemaDestino, TablaDestino, TipoTabla, Descripcion, FrecuenciaSinc
FROM ALMA_Meta.CFG_Queries
WHERE TablaDestino = 'CAT_Formularios';

-- ===========================================
-- ESTADÍSTICAS DE CAT_Formularios
-- ===========================================
SELECT
    Tipo,
    EnUso,
    COUNT(*) AS Cantidad
FROM ALMA_Clinico.CAT_Formularios
GROUP BY Tipo, EnUso
ORDER BY Tipo, EnUso;

-- ===========================================
-- FORMULARIOS EN USO (con registros)
-- ===========================================
SELECT
    Codigo,
    TablaALMA,
    Tipo,
    Registros,
    QueryExtraccion
FROM ALMA_Clinico.CAT_Formularios
WHERE EnUso = 'Y'
ORDER BY Tipo, Registros DESC;

-- ===========================================
-- RESUMEN GENERAL DE METADATA
-- ===========================================
SELECT
    SchemaDestino,
    COUNT(*) AS Tablas,
    STRING_AGG(TipoTabla, ', ') WITHIN GROUP (ORDER BY TipoTabla) AS Tipos
FROM ALMA_Meta.CFG_Queries
GROUP BY SchemaDestino
ORDER BY SchemaDestino;
