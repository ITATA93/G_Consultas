# websys.Monitor

> Page Performance Monitor.<br>Capture, Store and Display performance statistics

**Schema:** websys
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Page Performance Monitor.<br>Capture, Store and Display performance statistics

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| LogonGroupDR | bigint |  | FK | SI | - |
| LogonHospitalDR | bigint |  | FK | SI | - |
| LogonLocationDR | bigint |  | FK | SI | - |
| LogonProfileDR | bigint |  | FK | SI | - |
| LogonUserDR | bigint |  | FK | SI | - |
| MonitorDate | date |  |  | SI | - |
| MonitorTime | time |  |  | SI | - |
| ProcessID | varchar |  |  | SI | - |
| pClassQuery | varchar |  |  | SI | - |
| pGenericSort | bit |  |  | SI | - |
| pGlobalUpdates | numeric |  |  | SI | - |
| pGlobals | numeric |  |  | SI | - |
| pGlobalsStart | numeric |  |  | SI | - |
| pJournalEntries | numeric |  |  | SI | - |
| pLines | numeric |  |  | SI | - |
| pLinesStart | numeric |  |  | SI | - |
| pName | varchar |  |  | SI | - |
| pPrivateGlobalUpdates | numeric |  |  | SI | - |
| pQueryParams | varchar |  |  | SI | - |
| pSessionId | varchar |  |  | SI | - |
| pSortCol | varchar |  |  | SI | - |
| pTime | double |  |  | SI | - |
| pTimeStart | double |  |  | SI | - |
| pUserAgent | varchar |  |  | SI | - |
| pWQMGlobals | numeric |  |  | SI | - |
| pWQMGlobalsStart | numeric |  |  | SI | - |
| pWQMLines | numeric |  |  | SI | - |
| pWQMLinesStart | numeric |  |  | SI | - |
| pWorkflow | bigint |  |  | SI | - |
| websysLogID | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*