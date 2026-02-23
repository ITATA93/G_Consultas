# SQLUser.PAC_ConsCategGroups

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONSCATGRP_RowId | bigint | PK |  | NO | - |
| CONSCATGRP_Code | varchar |  |  | NO | Code |
| CONSCATGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONSCATGRP_CreatedDate | date |  |  | SI | Created Date |
| CONSCATGRP_CreatedTime | time |  |  | SI | Created Time |
| CONSCATGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONSCATGRP_DateFrom | date |  |  | SI | Date From |
| CONSCATGRP_DateTo | date |  |  | SI | Date To |
| CONSCATGRP_Desc | varchar |  |  | NO | Description |
| CONSCATGRP_Owner | varchar |  |  | SI | Owner |
| CONSCATGRP_UpdatedDate | date |  |  | SI | Updated Date |
| CONSCATGRP_UpdatedTime | time |  |  | SI | Updated Time |
| CONSCATGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Please rate the current (i.e., last 2 weeks) sever... |
| Q04 | - |  |  | SI | Difficulty falling asleep |
| Q05 | - |  |  | SI | Difficulty staying asleep |
| Q06 | - |  |  | SI | Problem waking up too early |
| Q07 | - |  |  | SI | How satisfied / dissatisfied are you with your cur... |
| Q08 | - |  |  | SI | To what extent do you consider your sleep problem ... |
| Q09 | - |  |  | SI | How noticeable to others do you think your sleepin... |
| Q10 | - |  |  | SI | How worried / distressed are you about your curren... |
| Q11 | - |  |  | SI | 0 to 7 |
| Q12 | - |  |  | SI | No clinically significant insomnia |
| Q13 | - |  |  | SI | 8 to 14 |
| Q14 | - |  |  | SI | Subtreshold insomnia |
| Q15 | - |  |  | SI | 15 to 21 |
| Q16 | - |  |  | SI | Clinical insomnia (moderate severity) |
| Q17 | - |  |  | SI | 22 to 28 |
| Q18 | - |  |  | SI | Clinical insomnia (severe) |
| Q19 | - |  |  | SI | The insomnia severity index (isi) is a 7-item self... |
| Q20 | - |  |  | SI | Source: morin c. insomnia: psychological assessmen... |
| Q21 | - |  |  | SI | The Insomnia Severity Index (ISI) is a 7-item self... |
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