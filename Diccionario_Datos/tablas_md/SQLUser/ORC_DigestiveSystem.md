# SQLUser.ORC_DigestiveSystem

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIGSYS_RowId | bigint | PK |  | NO | - |
| DIGSYS_Code | varchar |  |  | NO | Code |
| DIGSYS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIGSYS_Colonic | varchar |  |  | SI | Colonic   |
| DIGSYS_CreatedDate | date |  |  | SI | Created Date |
| DIGSYS_CreatedTime | time |  |  | SI | Created Time |
| DIGSYS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIGSYS_DateFrom | date |  |  | SI | Date From |
| DIGSYS_DateTo | date |  |  | SI | Date To |
| DIGSYS_Desc | varchar |  |  | NO | Description |
| DIGSYS_Gastric | varchar |  |  | SI | Gastric   |
| DIGSYS_Owner | varchar |  |  | SI | Owner |
| DIGSYS_UpdatedDate | date |  |  | SI | Updated Date |
| DIGSYS_UpdatedTime | time |  |  | SI | Updated Time |
| DIGSYS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Facial responses |
| Q04 | - |  |  | SI | Limb movements |
| Q05 | - |  |  | SI | Vocal expression of pain |
| Q06 | - |  |  | SI | Facial expression: determining the intensity of on... |
| Q07 | - |  |  | SI | Limb movements: determining the intensity of one o... |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | Classification |
| Q10 | - |  |  | SI | 0 - 2 |
| Q11 | - |  |  | SI | Considered a sign of NO pain |
| Q12 | - |  |  | SI | 3 - 10 |
| Q13 | - |  |  | SI | Considered a sign of pain |
| Q14 | - |  |  | SI | 0 - 2: Considered a sign of NO pain |
| Q15 | - |  |  | SI | 3 - 10: Considered a sign of pain |
| Q16 | - |  |  | SI | This scale scores pain from 0 to 10, where 0 is no... |
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