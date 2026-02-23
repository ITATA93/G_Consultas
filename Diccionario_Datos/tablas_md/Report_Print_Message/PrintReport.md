# Report_Print_Message.PrintReport

**Schema:** Report_Print_Message
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| JReportServerAddress | varchar |  |  | SI | - |
| PrintServerID | varchar |  |  | SI | - |
| ReportID | integer |  |  | SI | - |
| ReportProcesses | integer |  |  | SI | - |
| SaveToFilePath | varchar |  |  | SI | - |
| UseMultiRenderServer | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*