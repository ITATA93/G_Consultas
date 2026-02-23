# Report_Print_Process_Request.Context

**Schema:** Report_Print_Process_Request
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contexto**. Datos de contexto de sesión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %LastError | varchar |  |  | SI | This holds last exception |
| %LastFault | varchar |  |  | SI | This holds the last thrown fault |
| %Process | bigint |  |  | SI | This holds the reference to the process object |
| Iterator | varchar |  |  | SI | - |
| JReportServerAddress | varchar |  |  | SI | - |
| PrintServerID | varchar |  |  | SI | - |
| ProcessAvail | integer |  |  | SI | - |
| ProcessCount | integer |  |  | SI | - |
| REPID | varchar |  |  | SI | - |
| ReportType | varchar |  |  | SI | - |
| ReportsReturned | bit |  |  | SI | - |
| Results | bigint |  |  | SI | - |
| SaveToFilePath | varchar |  |  | SI | - |
| Signed | bit |  |  | SI | - |
| ThisResult | varchar |  |  | SI | - |
| UseMultiRenderServer | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*