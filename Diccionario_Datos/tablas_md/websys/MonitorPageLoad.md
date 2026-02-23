# websys.MonitorPageLoad

**Schema:** websys
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BrowserMemoryUsage | integer |  |  | SI | Browser memory usage in bytes.<br>
Will be collec... |
| LogonGroupDR | bigint |  | FK | SI | - |
| LogonHospitalDR | bigint |  | FK | SI | - |
| LogonLocationDR | bigint |  | FK | SI | - |
| LogonProfileDR | bigint |  | FK | SI | - |
| LogonUserDR | bigint |  | FK | SI | - |
| MonitorDate | date |  |  | SI | - |
| MonitorTime | time |  |  | SI | - |
| pComponent | bigint |  |  | SI | - |
| pEventItem | varchar |  |  | SI | - |
| pLoadInterrupted | bit |  |  | SI | - |
| pLoadTime | double |  |  | SI | - |
| pMenu | bigint |  |  | SI | - |
| pSessionId | varchar |  |  | SI | - |
| pTPAGID | varchar |  |  | SI | - |
| pTimeStart | double |  |  | SI | Millisecond sequence time for user activity |
| pUrl | varchar |  |  | SI | - |
| pUrlParams | varchar |  |  | SI | - |
| pUserAgent | varchar |  |  | SI | - |
| pWorkflow | bigint |  |  | SI | - |
| pWorkflowItemIndex | integer |  |  | SI | - |
| pWorklist | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*