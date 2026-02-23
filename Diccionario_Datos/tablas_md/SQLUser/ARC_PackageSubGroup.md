# SQLUser.ARC_PackageSubGroup

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKSUBGRP_RowId | bigint | PK |  | NO | - |
| PKSUBGRP_Code | varchar |  |  | NO | Code |
| PKSUBGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PKSUBGRP_CreatedDate | date |  |  | SI | Created Date |
| PKSUBGRP_CreatedTime | time |  |  | SI | Created Time |
| PKSUBGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKSUBGRP_DateFrom | date |  |  | SI | Date From |
| PKSUBGRP_DateTo | date |  |  | SI | Date To |
| PKSUBGRP_Desc | varchar |  |  | NO | Description |
| PKSUBGRP_Owner | varchar |  |  | SI | Owner |
| PKSUBGRP_UpdatedDate | date |  |  | SI | Updated Date |
| PKSUBGRP_UpdatedTime | time |  |  | SI | Updated Time |
| PKSUBGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Piramidal |
| Q02 | - |  |  | SI | Cerebelo |
| Q03 | - |  |  | SI | Tronco del encéfalo |
| Q04 | - |  |  | SI | Sensibilidad |
| Q05 | - |  |  | SI | Vejiga e intestino |
| Q06 | - |  |  | SI | Vejiga |
| Q07 | - |  |  | SI | Intestino |
| Q08 | - |  |  | SI | Visión |
| Q09 | - |  |  | SI | Funciones mentales |
| Q10 | - |  |  | SI | Interpretación |
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