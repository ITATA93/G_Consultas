# SQLUser.CT_Spec

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPC_RowId | bigint | PK |  | NO | - |
| CTSPC_Code | varchar |  |  | NO | Spec Code |
| CTSPC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTSPC_CreatedDate | date |  |  | SI | Created Date |
| CTSPC_CreatedTime | time |  |  | SI | Created Time |
| CTSPC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTSPC_DateFrom | date |  |  | SI | Date From |
| CTSPC_DateTo | date |  |  | SI | Date To |
| CTSPC_Desc | varchar |  |  | NO | Spec Description |
| CTSPC_Owner | varchar |  |  | SI | Owner |
| CTSPC_UpdatedDate | date |  |  | SI | Updated Date |
| CTSPC_UpdatedTime | time |  |  | SI | Updated Time |
| CTSPC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1. Some of your symptoms are made by your mind. |
| Q04 | - |  |  | SI | 2. You are mentally well. |
| Q05 | - |  |  | SI | 3. You do not need medication. |
| Q06 | - |  |  | SI | 4. Your stay in the hospital is necessary. |
| Q07 | - |  |  | SI | 5. The doctor is right in prescribing medication f... |
| Q08 | - |  |  | SI | 6. You do not need to be seen by a doctor or psych... |
| Q09 | - |  |  | SI | 7. If someone said you have a nervous or mental il... |
| Q10 | - |  |  | SI | 8. None of the unusual things you are experiencing... |
| Q11 | - |  |  | SI | A higher score implies better insight |
| Q12 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | Classification |
| Q14 | - |  |  | SI | 0 - 16 |
| Q15 | - |  |  | SI | A self - report Insight Scale for psychosis: relia... |
| Q16 | - |  |  | SI | 0 - 16: A higher score implies better insight |
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