# web_Msg.LB_Queue

**Schema:** web_Msg
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQ_AddVerificationQueueWKFL_DR | varchar |  | FK | SI | Additional Verification Queue Workflow |
| LBQ_AllocationType | varchar |  |  | SI | The reason the test set was allocated to the queue... |
| LBQ_ClockStartDate | date |  |  | SI | The date that the clock starts |
| LBQ_ClockStartTime | time |  |  | SI | The time that the clock starts |
| LBQ_DecisionSupportEvent_DR | bigint |  | FK | SI | The VR rule that added the test set to the queue |
| LBQ_EpisodeReportInterfaces | varchar |  |  | SI | Episode Report Interfaces which are linked the que... |
| LBQ_InDate | date |  |  | SI | The date the test set was placed on the queue |
| LBQ_InTime | time |  |  | SI | The time the test set was placed on the queue |
| LBQ_InUser | bigint |  |  | SI | The user that placed the test set on queue |
| LBQ_LastScheduleDate | date |  |  | SI | The date that the last schedule was failed |
| LBQ_LastScheduleTime | time |  |  | SI | The time that the last schedule was failed |
| LBQ_OutDate | date |  |  | SI | The date that the test set was taken off the queue |
| LBQ_OutTime | time |  |  | SI | The time that the test set was taken off the queue |
| LBQ_OutUser | bigint |  |  | SI | The user that took the test set off the queue |
| LBQ_Queue_DR | bigint |  | FK | SI | The queue the test set is linked to by this transa... |
| LBQ_RowID | varchar |  |  | SI | - |
| LBQ_TestSet_DR | bigint |  | FK | SI | Parent TestSet DR
Required by User.LBQueue. |
| LBTestSetMsg_DR | varchar |  | FK | SI | Before LBTestSet gets created, link LBTestSet mess... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ToBeDeleted | varchar |  |  | SI | Mark as deleted for the real queue delete User.LBQ... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*