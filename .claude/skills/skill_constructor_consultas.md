---
name: Constructor de Consultas SQL (TrakCare)
description: Skill para escribir consultas SQL seguras y eficientes para InterSystems IRIS.
---

# Skill: Constructor de Consultas Seguras

## 🎯 Misión
Traducir requerimientos a SQL **SEGURO** y **OPTIMIZADO** para el entorno hospitalario.

## 🛡️ Reglas de Oro (Checklist)
Antes de entregar CUALQUIER código SQL, verifica:
- [ ] **SOLO SELECT**: ¿Garantizas que no hay UPDATE/DELETE?
- [ ] **TOP N**: ¿Incluiste `TOP 100` (o similar) en el SELECT?
- [ ] **WHERE**: ¿Tienes filtros para tablas grandes (`PA_Adm`, `OE_Order`)?
- [ ] **NOLOCK**: (Opcional en IRIS, pero buena práctica si aplica)
- [ ] **Alias Claros**: ¿Usaste alias legibles (`PA` para `PA_Adm`)?

## 📝 Plantilla Maestra

```sql
-- =================================================================
-- CONSULTA: [Nombre Breve]
-- OBJETIVO: [Descripción]
-- AUTOR: Gemini/Antigravity
-- FECHA: [YYYY-MM-DD]
-- =================================================================

SELECT TOP 100
    -- Identificadores Clave
    PA.PAADM_ADMNo AS NumEpisodio,
    PM.PAPMI_No AS NumFicha,
    
    -- Datos Paciente
    P.PAPER_Name AS Nombre,
    P.PAPER_Name2 AS Apellido,
    
    -- Datos Específicos
    [COLUMNAS_ESPECIFICAS]

FROM SQLUser.PA_Adm AS PA

-- Joins Estándar
INNER JOIN SQLUser.PA_PatMas AS PM ON PA.PAADM_PAPMI_DR = PM.PAPMI_RowId
INNER JOIN SQLUser.PA_Person AS P  ON PM.PAPMI_PAPER_DR = P.PAPER_RowId
[OTROS_JOINS]

WHERE
    -- Filtros de Seguridad (Ej: Rango fechas, Estado activo)
    PA.PAADM_Date >= '2024-01-01'
    AND PA.PAADM_Type = 'I' -- Inpatient (Hospitalizado)
    [OTROS_FILTROS]

ORDER BY
    PA.PAADM_Date DESC
;
```

## 💡 Tips de Optimización
1.  **Fechas**: InterSystems guarda fechas como enteros o YYYY-MM-DD. Prefiere rangos (`>=` y `<`).
2.  **Índices**: Filtra siempre por columnas indexadas (comúnmente fechas, estados, IDs).
3.  **Evitar `SELECT *`**: Trae demasiada data innecesaria (long strings, streams) que pueden colgar la conexión JDBC.

## 🚫 Anti-Patrones (Lo que NO debes hacer)
*   `SELECT * FROM PA_Adm` (Sin TOP, Sin WHERE) -> **CRASH SEGURO**
*   Joins sin condiciones claras.
*   Subconsultas correlacionadas en el SELECT (Rendimiento pobre).
