# SQLUser.MR_SubFind

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRSUB_MRADM_ParRef | bigint | PK |  | NO | Des Ref to MRADM |
| ChildQ06DR | - |  |  | SI | Child Reference: Laceration repair |
| MRSUB_BodyAreaProbSubp_DR | varchar |  | FK | SI | Des Ref MRCBodyAreaProblemsSubp |
| MRSUB_BodyAreaProb_DR | varchar |  | FK | SI | Des Ref MRCBodyAreaProblems |
| MRSUB_BodyArea_DR | bigint |  | FK | SI | Des Ref BodyArea |
| MRSUB_BodyPartSymSubs | varchar |  |  | SI | Des Ref to BodyPartSymSubs |
| MRSUB_BodyPartsSymp_DR | varchar |  | FK | SI | Des Ref to MRCBodyPartsSymp |
| MRSUB_BodyParts_DR | bigint |  | FK | SI | Des Ref to MRCBodyParts |
| MRSUB_Childsub | numeric |  |  | NO | MRSUB Childsub (NewKey) |
| MRSUB_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| MRSUB_Date | date |  |  | SI | Date |
| MRSUB_DateStarted | date |  |  | SI | Date Started |
| MRSUB_Desc | varchar |  |  | SI | Description of Subjective Findings |
| MRSUB_DocCode_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| MRSUB_DurationDays | double |  |  | SI | Duration in Days |
| MRSUB_DurationMonth | double |  |  | SI | Duration in Months |
| MRSUB_DurationYear | double |  |  | SI | Duration in Years |
| MRSUB_EditCP_DR | varchar |  | FK | SI | Des Ref EditCP |
| MRSUB_EndDate | date |  |  | SI | EndDate |
| MRSUB_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| MRSUB_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| MRSUB_RTFNotes | varchar |  |  | SI | RTF Notes |
| MRSUB_RowId | varchar |  |  | NO | - |
| MRSUB_Time | time |  |  | SI | Time |
| MRSUB_TriageComplaint | varchar |  |  | SI | TriageComplaint |
| MRSUB_UpdateDate | date |  |  | SI | Update Date |
| MRSUB_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| MRSUB_UpdateTime | time |  |  | SI | Update Time |
| MRSUB_UserUpdate | bigint |  |  | SI | Des Ref User |
| Q02 | - |  |  | SI | Location on body map |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*