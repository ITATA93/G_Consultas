# SQLUser.PAC_PrenatalProblems

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREPRO_RowId | bigint | PK |  | NO | - |
| ChildQ07DR | - |  |  | SI | Child Reference: Recovery / Improvement of autonom... |
| PREPRO_Code | varchar |  |  | NO | Code |
| PREPRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PREPRO_CreatedDate | date |  |  | SI | Created Date |
| PREPRO_CreatedTime | time |  |  | SI | Created Time |
| PREPRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PREPRO_DateFrom | date |  |  | SI | Date From |
| PREPRO_DateTo | date |  |  | SI | Date To |
| PREPRO_Desc | varchar |  |  | NO | Description |
| PREPRO_NationalCode | varchar |  |  | SI | National Code |
| PREPRO_Owner | varchar |  |  | SI | Owner |
| PREPRO_UpdatedDate | date |  |  | SI | Updated Date |
| PREPRO_UpdatedTime | time |  |  | SI | Updated Time |
| PREPRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Timing |
| Q02 | - |  |  | SI | Timing, notes |
| Q03 | - |  |  | SI | Goals planned |
| Q04 | - |  |  | SI | Transfer recovery planned? |
| Q06 | - |  |  | SI | Recovery / Improvement of autonomy in activities o... |
| Q08 | - |  |  | SI | Family / Social / Work reintegration (prescription... |
| Q10 | - |  |  | SI | Occupational therapist notes |
| Q11 | - |  |  | SI | Date |
| Q12 | - |  |  | SI | Time |
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