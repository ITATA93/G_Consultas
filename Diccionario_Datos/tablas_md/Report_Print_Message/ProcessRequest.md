# Report_Print_Message.ProcessRequest

**Schema:** Report_Print_Message
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| JReportServerAddress | varchar |  |  | SI | - |
| PrintServerID | varchar |  |  | SI | - |
| ReportProcesses | integer |  |  | SI | - |
| ReportType | varchar |  |  | SI | - |
| SaveToFilePath | varchar |  |  | SI | - |
| Status | varchar |  |  | SI | - |
| UseMultiRenderServer | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*