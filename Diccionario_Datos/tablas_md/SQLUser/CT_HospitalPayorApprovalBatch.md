# SQLUser.CT_HospitalPayorApprovalBatch

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPPRBAT_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| PAPPRBAT_ApprovalRequestType | varchar |  |  | SI | Approval Request Type |
| PAPPRBAT_Childsub | double |  |  | NO | Childsub |
| PAPPRBAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAPPRBAT_CreatedDate | date |  |  | SI | Created Date |
| PAPPRBAT_CreatedTime | time |  |  | SI | Created Time |
| PAPPRBAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAPPRBAT_DateFrom | date |  |  | SI | Date From |
| PAPPRBAT_DateTo | date |  |  | SI | Date To |
| PAPPRBAT_EpisodeType | varchar |  |  | SI | Episode Type |
| PAPPRBAT_Rowid | varchar |  |  | NO | - |
| PAPPRBAT_UpdatedDate | date |  |  | SI | Updated Date |
| PAPPRBAT_UpdatedTime | time |  |  | SI | Updated Time |
| PAPPRBAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Does the child have any of these symptoms? Abnorma... |
| Q04 | - |  |  | SI | Does the child have any of these symptoms? Abnorma... |
| Q05 | - |  |  | SI | Does the child have any of these symptoms? Pallor |
| Q06 | - |  |  | SI | Consider the child to need immediate intervention ... |
| Q07 | - |  |  | SI | Further evaluation of the child is advised |
| Q08 | - |  |  | SI | Dieckmann RA, Brownstein D, Gausche-Hill M. The Pe... |
| Q09 | - |  |  | SI | Dietrich A, Widmeier K. Pediatric Assessment. In: ... |
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