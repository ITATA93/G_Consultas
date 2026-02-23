# SQLUser.PAC_TransRejectReason

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANSREJR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date pathology attended |
| Q04 | - |  |  | SI | Overall health review |
| Q05 | - |  |  | SI | Other health review notes |
| Q06 | - |  |  | SI | Transplant site review |
| Q07 | - |  |  | SI | Wound description and action taken |
| Q08 | - |  |  | SI | Transplant site notes and actions taken if require... |
| Q09 | - |  |  | SI | Consent obtained to record photo on patient EPR |
| Q10 | - |  |  | SI | Review of medications |
| Q11 | - |  |  | SI | Medication notes |
| Q12 | - |  |  | SI | Skin review completed |
| Q13 | - |  |  | SI | Skin notes |
| Q14 | - |  |  | SI | Referrals required |
| Q15 | - |  |  | SI | Referrals notes |
| Q16 | - |  |  | SI | Other concerns |
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
| TRANSREJR_Code | varchar |  |  | NO | Code |
| TRANSREJR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRANSREJR_CreatedDate | date |  |  | SI | Created Date |
| TRANSREJR_CreatedTime | time |  |  | SI | Created Time |
| TRANSREJR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRANSREJR_DateFrom | date |  |  | SI | Date From |
| TRANSREJR_DateTo | date |  |  | SI | Date To |
| TRANSREJR_DefaultReason | varchar |  |  | SI | Default Reason  |
| TRANSREJR_Desc | varchar |  |  | NO | Description |
| TRANSREJR_Owner | varchar |  |  | SI | Owner |
| TRANSREJR_UpdatedDate | date |  |  | SI | Updated Date |
| TRANSREJR_UpdatedTime | time |  |  | SI | Updated Time |
| TRANSREJR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*