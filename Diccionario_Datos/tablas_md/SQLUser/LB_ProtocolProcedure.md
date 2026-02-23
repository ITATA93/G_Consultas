# SQLUser.LB_ProtocolProcedure

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBPTP_ParRef | bigint | PK |  | NO | Parent Reference |
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
| LBPTP_MacroscopicDissectionAssistant_DR | bigint |  | FK | SI | Macroscopic Dissection Assistant  |
| LBPTP_MacroscopicDissectionBy_DR | bigint |  | FK | SI | Macroscopic Dissection by |
| LBPTP_MicroscopyUser_DR | bigint |  | FK | SI | Microscopy User  |
| LBPTP_NoPiecesTaken | integer |  |  | SI | No of Pieces Taken  |
| LBPTP_Note | longvarchar |  |  | SI | Note
HTMLRichText |
| LBPTP_OtherNote | longvarchar |  |  | SI | Other Note
HTMLRichText |
| LBPTP_Pathologist | varchar |  |  | SI | Pathologist  |
| LBPTP_Planned | bit |  |  | SI | Planned
Is this procedure part of the configured ... |
| LBPTP_PlatedBy_DR | bigint |  | FK | SI | Plated by  |
| LBPTP_Procedure_DR | bigint |  | FK | SI | Procedure |
| LBPTP_RemainingPrimarySample | varchar |  |  | SI | Remaining Primary Sample  |
| LBPTP_ReportingPathologist_DR | bigint |  | FK | SI | Reporting Pathologist  |
| LBPTP_RowID | varchar |  |  | NO | - |
| LBPTP_Source_DR | varchar |  | FK | SI | Source Material  |
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
| Q01 | - |  |  | SI | Riesgo de Abandono |
| Q02 | - |  |  | SI | Alcoholismo |
| Q03 | - |  |  | SI | Sin Previsión |
| Q04 | - |  |  | SI | Vive Solo |
| Q05 | - |  |  | SI | Drogadicción |
| Q06 | - |  |  | SI | Abandonos Anteriores |
| Q07 | - |  |  | SI | Resultado Riesgo de Abandono |
| Q07ObsDR | - |  |  | SI | Resultado Riesgo de Abandono DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*