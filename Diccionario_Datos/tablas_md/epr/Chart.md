# epr.Chart

**Schema:** epr
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Caption | varchar |  |  | SI | - |
| ChartColour | varchar |  |  | SI | - |
| ChartType | varchar |  |  | SI | - |
| CustomURLExpression | varchar |  |  | SI | - |
| Deprecated | bit |  |  | SI | - |
| DisplayConsultBanner | bit |  |  | SI | - |
| DisplayInTabs | varchar |  |  | SI | - |
| HideHeaderIfSingleChartItem | bit |  |  | SI | - |
| IconPath | varchar |  |  | SI | - |
| Name | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReasonDeprecated | varchar |  |  | SI | - |
| SELChartColour | varchar |  |  | SI | - |
| SELTextColour | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| ShortDescriptionText | varchar |  |  | SI | - |
| ShowNavTabs | bit |  |  | SI | - |
| TextColour | varchar |  |  | SI | - |
| TimeChanged | varchar |  |  | SI | 75648 - require last date/time to calculate if reg... |
| zIsHistoryPage | bit |  |  | SI | 'IsHistoryPage' is deprecated due to new property ... |
| zStudent | bit |  |  | SI | 'Student' is deprecated due to new property chartT... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*