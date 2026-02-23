# SQLUser.PAC_DischCondit

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISCON_RowId | bigint | PK |  | NO | - |
| DISCON_AutopsyReq | varchar |  |  | SI | AutopsyReq |
| DISCON_Code | varchar |  |  | NO | Code |
| DISCON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISCON_CreatedDate | date |  |  | SI | Created Date |
| DISCON_CreatedTime | time |  |  | SI | Created Time |
| DISCON_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISCON_DateFrom | date |  |  | SI | Date From |
| DISCON_DateTo | date |  |  | SI | Date To |
| DISCON_DeadFlag | varchar |  |  | SI | Dead Flag |
| DISCON_Desc | varchar |  |  | NO | Description |
| DISCON_EpisodeType | varchar |  |  | SI | Episode Type |
| DISCON_NationalCode | varchar |  |  | SI | National Code |
| DISCON_Owner | varchar |  |  | SI | Owner |
| DISCON_Subregion_DR | bigint |  | FK | SI | Subregion  |
| DISCON_UpdatedDate | date |  |  | SI | Updated Date |
| DISCON_UpdatedTime | time |  |  | SI | Updated Time |
| DISCON_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of test |
| Q02 | - |  |  | SI | Time of test |
| Q03 | - |  |  | SI | Test performed |
| Q04 | - |  |  | SI | Height of chair (cm) |
| Q05 | - |  |  | SI | Sit-to-stand repetitions completed in 30 seconds |
| Q06 | - |  |  | SI | Sit-to-stand repetitions completed in 1 minute |
| Q07 | - |  |  | SI | Time taken to complete five 5 repetitions of sit-t... |
| Q08 | - |  |  | SI | Comments |
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