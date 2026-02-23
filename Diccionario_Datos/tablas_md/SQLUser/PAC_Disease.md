# SQLUser.PAC_Disease

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACD_RowID | bigint | PK |  | NO | - |
| PACD_CareCatItem_DR | bigint |  | FK | SI | Preventative Care Item |
| PACD_Code | varchar |  |  | NO | Code |
| PACD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACD_CreatedDate | date |  |  | SI | Created Date |
| PACD_CreatedTime | time |  |  | SI | Created Time |
| PACD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACD_DateFrom | date |  |  | SI | Date From |
| PACD_DateTo | date |  |  | SI | Date To |
| PACD_Desc | varchar |  |  | NO | Description |
| PACD_Owner | varchar |  |  | SI | Owner |
| PACD_UpdatedDate | date |  |  | SI | Updated Date |
| PACD_UpdatedTime | time |  |  | SI | Updated Time |
| PACD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | In the 24 hours since chemotherapy, did you have a... |
| Q02 | - |  |  | SI | If you vomited in the 24 hours since chemotherapy,... |
| Q03 | - |  |  | SI | Notes |
| Q04 | - |  |  | SI | In the 24 hours since chemotherapy, did you have a... |
| Q05 | - |  |  | SI | If you had nausea, please select the number that m... |
| Q06 | - |  |  | SI | Notes |
| Q07 | - |  |  | SI | Did you vomit 24 hours or more after chemotherapy? |
| Q08 | - |  |  | SI | If you vomited during this period, how many times ... |
| Q09 | - |  |  | SI | Notes |
| Q10 | - |  |  | SI | Did you have any nausea 24 hours or more after che... |
| Q11 | - |  |  | SI | If you had nausea, please select the number that m... |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
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