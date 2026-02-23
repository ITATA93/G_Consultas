# epr.ChartBook

**Schema:** epr
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CTLCollapseTimeline | bit |  |  | SI | - |
| CTLDateFrom | varchar |  |  | SI | Chartbook Timeline Date From
Used to control the ... |
| CTLDateTimeSlot | varchar |  |  | SI | - |
| CTLDateTo | varchar |  |  | SI | Chartbook Timeline Date To
Used to control the de... |
| CTLEpisodeType | varchar |  |  | SI | - |
| CTLMaximumEncounter | integer |  |  | SI | - |
| CTLSelectAllRestriction | integer |  |  | SI | - |
| CTLShowInOneRow | bit |  |  | SI | - |
| CTLUDF | varchar |  |  | SI | - |
| DefaultPatSummaryChartDR | bigint |  | FK | SI | Default Patient Summary Chart |
| Deprecated | bit |  |  | SI | - |
| Description | varchar |  |  | NO | - |
| DisplayEnteredInErrorItems | bit |  |  | SI | Determines whether to display items that are marke... |
| EPRPrintOnlyShowLinkedMergedEps | bit |  |  | SI | If this property is set, when configured to show l... |
| EprReadOnly | bit |  |  | SI | If this property is set, all items in the ChartBoo... |
| HideIfNoData | bit |  |  | SI | Hides Tabs and Chart Items if they don't have data... |
| MaxTabsPerPage | integer |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReasonDeprecated | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| ShowPatSummChartFromAccessProfile | bit |  |  | SI | Show Patient Summary Chart From Access Profile |
| ShowTimeline | bit |  |  | SI | - |
| SmallTabs | bit |  |  | SI | - |
| SplitIntoPages | bit |  |  | SI | - |
| TimeChanged | varchar |  |  | SI | 75648 - require last date/time to calculate if reg... |
| TimeLinePrefs | varchar |  |  | SI | - |
| ZenVersion | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*