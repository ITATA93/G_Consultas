# Tools_LabSim_Metrics_Msg.ToolsLBSMPerformanceFindList

**Schema:** Tools_LabSim_Metrics_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas**. Utilidades y procesos de soporte.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AuthorisedByDR | bigint |  | FK | SI | - |
| CreateExportFile | varchar |  |  | SI | - |
| ExportFieldDelimiter | varchar |  |  | SI | - |
| ExportFileLocation | varchar |  |  | SI | - |
| ExtInterfaceQueueDR | bigint |  | FK | SI | - |
| ID | varchar |  |  | NO | - |
| PerformanceReport | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RefreshWorkfile | varchar |  |  | SI | - |
| ReportContextDate | date |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*