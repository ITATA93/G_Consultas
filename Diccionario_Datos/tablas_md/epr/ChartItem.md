# epr.ChartItem

**Schema:** epr
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AcrossEpisodes | bit |  |  | SI | - |
| AdHocGraphLink | bit |  |  | SI | - |
| AddInInfoPaneSize | integer |  |  | SI | - |
| AlwaysShowIfNoData | bit |  |  | SI | - |
| ChartDR | bigint |  | FK | SI | To refer back to the parent Chart |
| ClinicalTimelineDR | bigint |  | FK | SI | - |
| Collapse | bit |  |  | SI | - |
| ColumnWidth | integer |  |  | SI | Log 39287 - AI - 02-10-2003 : New field Column Wid... |
| ConditionalExpression | varchar |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| DetailedPrint | bit |  |  | SI | - |
| DeviceSettings | varchar |  |  | SI | [DEPRECATED]Previously used by legacy TC Mobile fr... |
| DisplayAddButton | bit |  |  | SI | - |
| DisplayHeader | bit |  |  | SI | - |
| DisplayMultipleAddButton | bit |  |  | SI | - |
| DisplayRow | integer |  |  | SI | - |
| EPRPrintCustomReportDR | bigint |  | FK | SI | - |
| EmbedGraph | bigint |  |  | SI | a SINGLE graph that will ALWAYS be displayed upon ... |
| GraphDR | bigint |  | FK | SI | - |
| Graphs | varchar |  |  | SI | Bit of overkill, this one.... 
GraphDR is a DR to... |
| Heading | varchar |  |  | SI | - |
| HideChartItem | bit |  |  | SI | This is only available when QuickAdd is ticked so ... |
| Item | varchar |  |  | NO | Reference DR to epr.CTProfileParams |
| ItemType | varchar |  |  | NO | - |
| OnlyMarkedForDSReport | bit |  |  | SI | Log 55973 - PJC - 20-12-2005 : Add the "Only show ... |
| OpenAddInInfoPane | bit |  |  | SI | - |
| Owner | varchar |  |  | SI | - |
| QuickAdd | bit |  |  | SI | - |
| Sequence | varchar |  |  | SI | - |
| ShowCSOnly | bit |  |  | SI | - |
| SmartGraph | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*