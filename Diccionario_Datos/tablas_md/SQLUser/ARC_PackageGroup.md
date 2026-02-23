# SQLUser.ARC_PackageGroup

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKGRP_RowId | bigint | PK |  | NO | - |
| ChildQ01DR | - |  |  | SI | Child Reference: Hipótesis Diagnóstica (Ejes) |
| PKGRP_Code | varchar |  |  | NO | Code |
| PKGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PKGRP_Comments | varchar |  |  | SI | Comments |
| PKGRP_CreatedDate | date |  |  | SI | Created Date |
| PKGRP_CreatedTime | time |  |  | SI | Created Time |
| PKGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKGRP_DateFrom | date |  |  | SI | Date From |
| PKGRP_DateTo | date |  |  | SI | Date To |
| PKGRP_Desc | varchar |  |  | NO | Description |
| PKGRP_FreeText1 | varchar |  |  | SI | Free Text 1 |
| PKGRP_Owner | varchar |  |  | SI | Owner |
| PKGRP_PackGroupSubType_DR | bigint |  | FK | SI | Des Ref ARCPackageGroupSubType |
| PKGRP_PackGroupType_DR | bigint |  | FK | SI | Des Ref ARCPackageGroupType |
| PKGRP_PackageReason_DR | bigint |  | FK | SI | Des Ref ARCPackageReason |
| PKGRP_UpdatedDate | date |  |  | SI | Updated Date |
| PKGRP_UpdatedTime | time |  |  | SI | Updated Time |
| PKGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | Profesional de Salud |
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