# SQLUser.PA_RefPathwayStageEv

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EV_ParRef | varchar | PK |  | NO | PA_RefPathway Parent Reference |
| EV_Childsub | double |  |  | NO | Childsub |
| EV_Comments | varchar |  |  | SI | Comments |
| EV_DateComplete | date |  |  | SI | Date complete |
| EV_DateOwner | date |  |  | SI | Date Owner |
| EV_Desc | varchar |  |  | SI | Description |
| EV_Duration | double |  |  | SI | Duration |
| EV_Episode_DR | bigint |  | FK | SI | Episode DR |
| EV_EventAction | varchar |  |  | SI | Action |
| EV_EventDate | date |  |  | SI | EventDate |
| EV_EventTime | time |  |  | SI | EventTime |
| EV_Outcome | varchar |  |  | SI | Outcome |
| EV_ReasonBreach | varchar |  |  | SI | Reason for Breach |
| EV_RefTreatPathCompReason_DR | bigint |  | FK | SI | Complete Reason |
| EV_RefTreatPathReasonBreach_DR | bigint |  | FK | SI | Reason for Breach |
| EV_RowId | varchar |  |  | NO | - |
| EV_SequenceNumber | double |  |  | SI | Sequence Number |
| EV_StageOwner_DR | bigint |  | FK | SI | EVStageOwnerDR |
| EV_StageStatus_DR | bigint |  | FK | SI | Des Ref Stage Status |
| EV_StageTemplate_DR | bigint |  | FK | SI | Des Ref PACRefStageTemplate |
| EV_StartUponEndOf_DR | varchar |  | FK | SI | Start Upon End Of |
| EV_TimeComplete | time |  |  | SI | Time complete |
| EV_TimeOwner | time |  |  | SI | Time Owner |
| EV_Type_DR | bigint |  | FK | SI | Des Ref Type |
| EV_User_DR | bigint |  | FK | SI | UserDR |
| EV_WaitTimeExtServices_DR | bigint |  | FK | SI | WaitTimeExtServicesDR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*