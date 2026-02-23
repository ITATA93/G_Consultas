# SQLUser.LB_Queue

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQ_RowID | bigint | PK |  | NO | - |
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
| LBQ_Queue_DR | bigint |  | FK | NO | The queue the test set is linked to by this transa... |
| LBQ_TestSet_DR | bigint |  | FK | NO | Parent TestSet DR |
| Q39Q1 | - |  |  | SI | Exámen Realizado |
| Q39Q2 | - |  |  | SI | Fecha |
| Q39Q3 | - |  |  | SI | Antígeno Usado |
| Q39Q4 | - |  |  | SI | Resultado |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*