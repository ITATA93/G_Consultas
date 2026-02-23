# SQLUser.MR_PresentIllness

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESI_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| PRESI_BodyPartSymSubs_DR | varchar |  | FK | SI | Des Ref BodyPartSymSubs |
| PRESI_BodyPartsSymp_DR | varchar |  | FK | SI | Des Ref BodyPartsSymp |
| PRESI_BodyParts_DR | bigint |  | FK | SI | Des Ref BodyParts |
| PRESI_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| PRESI_Category_DR | bigint |  | FK | SI | Category |
| PRESI_CauseOfDeath | varchar |  |  | SI | Cause of Death |
| PRESI_Childsub | double |  |  | NO | Childsub |
| PRESI_Comments | varchar |  |  | SI | Comments |
| PRESI_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| PRESI_Date | date |  |  | SI | Date |
| PRESI_DateOnset | date |  |  | SI | DateOnset |
| PRESI_Desc | varchar |  |  | SI | Description |
| PRESI_DiagnosStatus_DR | bigint |  | FK | SI | Des Ref DiagnosStatus |
| PRESI_EditCP_DR | varchar |  | FK | SI | Des Ref EditCP |
| PRESI_EndCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| PRESI_EndCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit] ... |
| PRESI_EndCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| PRESI_EndCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| PRESI_EndCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| PRESI_EndCalcDateBase | date |  |  | SI | date calculated date is based on |
| PRESI_EndDate | date |  |  | SI | EndDate |
| PRESI_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PRESI_ExternalId | varchar |  |  | SI | External Id |
| PRESI_ICDCode_DR | bigint |  | FK | SI | Des Ref ICDCode |
| PRESI_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PRESI_NoHistoryOf | varchar |  |  | SI | NoHistoryOf |
| PRESI_OnsetCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| PRESI_OnsetCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit] ... |
| PRESI_OnsetCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| PRESI_OnsetCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| PRESI_OnsetCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| PRESI_OnsetCalcDateBase | date |  |  | SI | date calculated date is based on |
| PRESI_RowId | varchar |  |  | NO | - |
| PRESI_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PRESI_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PRESI_Time | time |  |  | SI | Time |
| PRESI_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| PRESI_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| Q02 | - |  |  | SI | Urinary Catheter Insertion Date |
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