# SQLUser.OEC_ResultDisplayGroup

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESDGRP_RowId | bigint | PK |  | NO | - |
| Q03 | - |  |  | SI | Rhonchi |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Rhonchi DR |
| Q05N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Other |
| Q08 | - |  |  | SI | Lung sound |
| Q08N | - |  |  | SI | Note |
| Q08ObsDR | - |  |  | SI | Lung sound DR |
| Q10 | - |  |  | SI | Chest |
| Q10N | - |  |  | SI | Note |
| Q10ObsDR | - |  |  | SI | Chest DR |
| Q12 | - |  |  | SI | Axilla |
| Q12N | - |  |  | SI | Note |
| Q12ObsDR | - |  |  | SI | Axilla DR |
| Q13 | - |  |  | SI | Other |
| Q15 | - |  |  | SI | Stridor |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Stridor DR |
| Q16 | - |  |  | SI | Rales |
| Q16N | - |  |  | SI | Note |
| Q16ObsDR | - |  |  | SI | Rales DR |
| Q17 | - |  |  | SI | Chest percussion |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Chest percussion DR |
| Q19 | - |  |  | SI | Chest appearance |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Chest appearance  DR |
| Q20 | - |  |  | SI | Wheezing |
| Q20ObsDR | - |  |  | SI | Wheezing DR |
| Q21 | - |  |  | SI | Chest scars |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Chest scars DR |
| Q22 | - |  |  | SI | Accessory muscle use |
| Q22N | - |  |  | SI | Note |
| Q22ObsDR | - |  |  | SI | Accessory muscle use DR |
| Q23 | - |  |  | SI | Intercostal recession |
| Q23N | - |  |  | SI | Note |
| Q23ObsDR | - |  |  | SI | Intercostal recession DR |
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
| RESDGRP_Code | varchar |  |  | NO | Code |
| RESDGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESDGRP_CreatedDate | date |  |  | SI | Created Date |
| RESDGRP_CreatedTime | time |  |  | SI | Created Time |
| RESDGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESDGRP_Desc | varchar |  |  | NO | Description |
| RESDGRP_DisplayName | varchar |  |  | SI | Display Name |
| RESDGRP_Owner | varchar |  |  | SI | Owner |
| RESDGRP_UpdatedDate | date |  |  | SI | Updated Date |
| RESDGRP_UpdatedTime | time |  |  | SI | Updated Time |
| RESDGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*