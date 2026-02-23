# SQLUser.PAC_CountryOfBirthSource

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COBSRC_RowId | bigint | PK |  | NO | - |
| COBSRC_Code | varchar |  |  | NO | Code |
| COBSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COBSRC_CreatedDate | date |  |  | SI | Created Date |
| COBSRC_CreatedTime | time |  |  | SI | Created Time |
| COBSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COBSRC_DateFrom | date |  |  | SI | DateFrom |
| COBSRC_DateTo | date |  |  | SI | DateTo |
| COBSRC_Desc | varchar |  |  | NO | Description |
| COBSRC_Owner | varchar |  |  | SI | Owner |
| COBSRC_UpdatedDate | date |  |  | SI | Updated Date |
| COBSRC_UpdatedTime | time |  |  | SI | Updated Time |
| COBSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Last menstrual period |
| Q01ObsDR | - |  |  | SI | Last menstrual period DR |
| Q02 | - |  |  | SI | Cycle day |
| Q03 | - |  |  | SI | Uterus position |
| Q04 | - |  |  | SI | Endometrial thickness (mm) |
| Q05 | - |  |  | SI | Any pathology |
| Q06 | - |  |  | SI | Right antral follicle count |
| Q07 | - |  |  | SI | Left antral follicle count |
| Q08 | - |  |  | SI | Right ovary any pathology |
| Q09 | - |  |  | SI | Left ovary any pathology |
| Q10 | - |  |  | SI | Right ovary any comments |
| Q11 | - |  |  | SI | Left ovary any comments |
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