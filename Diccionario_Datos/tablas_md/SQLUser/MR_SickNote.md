# SQLUser.MR_SickNote

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOT_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ04DR | - |  |  | SI | Child Reference: Laceration length |
| NOT_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| NOT_ChiefComplaints_DR | bigint |  | FK | SI | Des Ref ChiefComplaints |
| NOT_Childsub | double |  |  | NO | Childsub |
| NOT_Consult_DR | varchar |  | FK | SI | Des Consult |
| NOT_CreateDate | date |  |  | SI | CreateDate |
| NOT_CreateTime | time |  |  | SI | CreateTime |
| NOT_Diagnosis_DR | bigint |  | FK | SI | Des Ref Diagnosis |
| NOT_EndDate | date |  |  | SI | EndDate |
| NOT_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| NOT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| NOT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| NOT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| NOT_MedCertType_DR | bigint |  | FK | SI | Des Ref MedCertType |
| NOT_Remarks | varchar |  |  | SI | Remarks |
| NOT_RowId | varchar |  |  | NO | - |
| NOT_StartDate | date |  |  | SI | StartDate |
| NOT_Status | varchar |  |  | SI | Status |
| Q09 | - |  |  | SI | Vaccination status reviewed |
| Q09N | - |  |  | SI | Note |
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