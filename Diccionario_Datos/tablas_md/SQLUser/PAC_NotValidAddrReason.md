# SQLUser.PAC_NotValidAddrReason

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NVAREA_RowId | bigint | PK |  | NO | - |
| NVAREA_Code | varchar |  |  | NO | Code |
| NVAREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NVAREA_CreatedDate | date |  |  | SI | Created Date |
| NVAREA_CreatedTime | time |  |  | SI | Created Time |
| NVAREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NVAREA_DateFrom | date |  |  | SI | DateFrom |
| NVAREA_DateTo | date |  |  | SI | DateTo |
| NVAREA_Desc | varchar |  |  | NO | Description |
| NVAREA_Owner | varchar |  |  | SI | Owner |
| NVAREA_UpdatedDate | date |  |  | SI | Updated Date |
| NVAREA_UpdatedTime | time |  |  | SI | Updated Time |
| NVAREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Chief Complaint Details |
| Q02 | - |  |  | SI | Onset |
| Q03 | - |  |  | SI | Location |
| Q04 | - |  |  | SI | Characteristics |
| Q05 | - |  |  | SI | Aggravating Factors |
| Q05A | - |  |  | SI | Other Aggravating Factors |
| Q06 | - |  |  | SI | Alleviating Factors |
| Q06A | - |  |  | SI | Other Alleviating Factors |
| Q09 | - |  |  | SI | Pain Score |
| Q09A | - |  |  | SI | Pain Assessment |
| Q09ObsDR | - |  |  | SI | Pain Score DR |
| Q10 | - |  |  | SI | Pain Location |
| Q11 | - |  |  | SI | Leg Pain |
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