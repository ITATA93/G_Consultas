# web_Msg.LBQueueList

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CTSRCH | varchar |  |  | SI | - |
| CareProviderIDList | varchar |  |  | SI | - |
| DepartmentIDList | varchar |  |  | SI | - |
| FailureType | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCQueueID | varchar |  |  | SI | - |
| OECPriorityIDList | varchar |  |  | SI | Priority ID for LBVerificationQueueGrid.List selec... |
| PatientLocationIDList | varchar |  |  | SI | - |
| PriorityIDList | varchar |  |  | SI | Priority ID for LBVerificationQueue.WorkBench sear... |
| QueueLabSiteIDList | varchar |  |  | SI | - |
| QueueTypeIDList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RefDoctorIDList | varchar |  |  | SI | - |
| SRCHMsgID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TestSetIDList | varchar |  |  | SI | - |
| TestSetLabSiteIDList | varchar |  |  | SI | - |
| TestSetStatusIDList | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| currentCTSRCH | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*