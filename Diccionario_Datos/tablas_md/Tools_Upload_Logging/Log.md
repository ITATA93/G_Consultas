# Tools_Upload_Logging.Log

**Schema:** Tools_Upload_Logging
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| fileName | varchar |  |  | SI | - |
| lineInFile | integer |  |  | SI | - |
| lineInfo | varchar |  |  | SI | additional context to show report by e.g. specific... |
| link | varchar |  |  | SI | - |
| loadClass | varchar |  |  | SI | - |
| logDate | date |  |  | SI | - |
| logTime | time |  |  | SI | - |
| logType | varchar |  |  | SI | as "Msg + %TimeStamp" for Reporting;
LOG    for I... |
| loggingDate | integer |  |  | SI | - |
| message | varchar |  |  | SI | - |
| runType | varchar |  |  | SI | to Identify the RunType mainly for Reporting Filte... |
| startRun | varchar |  |  | SI | to Identify the Run or Session
defaulted to %sess... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*