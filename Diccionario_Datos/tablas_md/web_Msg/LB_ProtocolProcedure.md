# web_Msg.LB_ProtocolProcedure

**Schema:** web_Msg
**Columnas:** 56
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Description | varchar |  |  | SI | [ Internal ] Description
The calculated procedure... |
| Hierarchy | numeric |  |  | SI | [ Internal ] Structure Hierarchy
Used to store th... |
| ID | varchar |  |  | NO | - |
| LBPTP_AddOnBy_DR | bigint |  | FK | SI | User who add unplanned |
| LBPTP_AddOnDate | date |  |  | SI | Add-on Date
Date when procedure was added unplann... |
| LBPTP_AddOnTime | time |  |  | SI | Add-on Time
Time when procedure was added unplann... |
| LBPTP_AdditionalNote | longvarchar |  |  | SI | Additional Notes
HTMLRichText |
| LBPTP_AuthorisedBy_DR | bigint |  | FK | SI | User who completed |
| LBPTP_Autocomplete | varchar |  |  | SI | Autocomplete
Indicates that this procedure is aut... |
| LBPTP_Billable | varchar |  |  | SI | Billable Flag
Indicates that this procedure is bi... |
| LBPTP_CompletedDate | date |  |  | SI | Completed Date
Date when procedure was completed |
| LBPTP_CompletedTime | time |  |  | SI | Completed Time
Time when procedure was completed |
| LBPTP_CutUpBy_DR | bigint |  | FK | SI | Cut Up User  |
| LBPTP_Decalcification | varchar |  |  | SI | Decalcification |
| LBPTP_DecalcificationAdditionalNote | longvarchar |  |  | SI | Decalcification Additional Notes (HTML FT) |
| LBPTP_DecalcificationExpectedDuration | integer |  |  | SI | Decalcification Expected Duration (Days) |
| LBPTP_DecalcificationExpectedEndDate | date |  |  | SI | Decalcification Expected End Date  |
| LBPTP_EmbeddedOnEdge | varchar |  |  | SI | Embedded On Edge   |
| LBPTP_EmbeddingBy_DR | bigint |  | FK | SI | Embedding By |
| LBPTP_FrozenSection | varchar |  |  | SI | Frozen Section  |
| LBPTP_FrozenSectionCutBy_DR | bigint |  | FK | SI | Frozen Section Cut By  |
| LBPTP_FrozenSectionPreparedBy_DR | bigint |  | FK | SI | Frozen Section Prepared By  |
| LBPTP_IndicatedReportingPathologistBy_DR | bigint |  | FK | SI | Indicated Reporting Pathologist  |
| LBPTP_InsertAfterObservation_DR | varchar |  | FK | SI | Insert After Protocol Observation for user-added o... |
| LBPTP_InsertAfterObservation_DR_Msg | varchar |  |  | SI | - |
| LBPTP_MacroscopicDissectionAssistant_DR | bigint |  | FK | SI | Macroscopic Dissection Assistant  |
| LBPTP_MacroscopicDissectionBy_DR | bigint |  | FK | SI | Macroscopic Dissection by |
| LBPTP_MicroscopyUser_DR | bigint |  | FK | SI | Microscopy User  |
| LBPTP_NoPiecesTaken | integer |  |  | SI | No of Pieces Taken  |
| LBPTP_Note | longvarchar |  |  | SI | Note
HTMLRichText |
| LBPTP_OtherNote | longvarchar |  |  | SI | Other Note
HTMLRichText |
| LBPTP_ParRef | bigint |  |  | SI | Parent Reference |
| LBPTP_Pathologist | varchar |  |  | SI | Pathologist  |
| LBPTP_Planned | bit |  |  | SI | Planned
Is this procedure part of the configured ... |
| LBPTP_PlatedBy_DR | bigint |  | FK | SI | Plated by  |
| LBPTP_Procedure_DR | bigint |  | FK | SI | Procedure |
| LBPTP_RemainingPrimarySample | varchar |  |  | SI | Remaining Primary Sample  |
| LBPTP_ReportingPathologist_DR | bigint |  | FK | SI | Reporting Pathologist  |
| LBPTP_RowID | varchar |  |  | SI | - |
| LBPTP_Source_DR | varchar |  | FK | SI | Source Material  |
| LBPTP_Source_DR_Msg | varchar |  |  | SI | Source Procedure Message Object  |
| LBPTP_Status | varchar |  |  | SI | Status |
| LBPTP_SupervisingPathologist_DR | bigint |  | FK | SI | Supervising Pathologist   |
| LBPTP_TissueRemaining | varchar |  |  | SI | Tissue Remaining  |
| LBPTP_TurnaroundTimeConfig | varchar |  |  | SI | Turnaround Time Config  |
| LBPTP_TurnaroundTimeElapsed | integer |  |  | SI | Turnaround Time Elapsed |
| LBPTP_TurnaroundTimeFlag | varchar |  |  | SI | Turnaround Time Flag
Standard Type=LabTestSetTurn... |
| LBPTP_ValidUntilDate | date |  |  | SI | Valid Until Date |
| LBPTP_WorkloadAdjustment | integer |  |  | SI | Workload Adjustment  |
| ProtocolSequence | numeric |  |  | SI | Used to store the sequence protocol items are disp... |
| ReadOnly | bit |  |  | SI | - |
| Sequence | numeric |  |  | SI | [ Internal ] Structure Sequence
Used to store the... |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*