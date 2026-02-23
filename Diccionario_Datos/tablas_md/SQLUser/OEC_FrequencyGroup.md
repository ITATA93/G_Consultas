# SQLUser.OEC_FrequencyGroup

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FRGRP_RowId | bigint | PK |  | NO | - |
| FRGRP_Code | varchar |  |  | NO | Code |
| FRGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FRGRP_CreatedDate | date |  |  | SI | Created Date |
| FRGRP_CreatedTime | time |  |  | SI | Created Time |
| FRGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FRGRP_DateFrom | date |  |  | SI | Date From |
| FRGRP_DateTo | date |  |  | SI | Date To |
| FRGRP_Desc | varchar |  |  | NO | Description |
| FRGRP_Owner | varchar |  |  | SI | Owner |
| FRGRP_UpdatedDate | date |  |  | SI | Updated Date |
| FRGRP_UpdatedTime | time |  |  | SI | Updated Time |
| FRGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Visual Acuity - Uncorrected |
| Q02 | - |  |  | SI | VA-Dt |
| Q03 | - |  |  | SI | VA-Dt 2 |
| Q04 | - |  |  | SI | VA-Dt 3 |
| Q05 | - |  |  | SI | VA-Nr |
| Q06 | - |  |  | SI | VA-Nr 2 |
| Q07 | - |  |  | SI | VA-Nr 3 |
| Q08 | - |  |  | SI | Notes |
| Q09 | - |  |  | SI | Right Eye |
| Q10 | - |  |  | SI | Left Eye |
| Q11 | - |  |  | SI | Both Eye |
| Q12 | - |  |  | SI | Visual Acuity - Corrected (Glasses Refraction) |
| Q13 | - |  |  | SI | Right Eye |
| Q14 | - |  |  | SI | Left Eye |
| Q15 | - |  |  | SI | Sph |
| Q16 | - |  |  | SI | Sph 2 |
| Q17 | - |  |  | SI | Cyl |
| Q18 | - |  |  | SI | Cyl 2 |
| Q19 | - |  |  | SI | Axis |
| Q20 | - |  |  | SI | Axis 2 |
| Q21 | - |  |  | SI | Add |
| Q22 | - |  |  | SI | VA-Dt |
| Q23 | - |  |  | SI | VA-Dt 2 |
| Q24 | - |  |  | SI | VA-Dt 3 |
| Q25 | - |  |  | SI | VA-Nr |
| Q26 | - |  |  | SI | VA-Nr 2 |
| Q27 | - |  |  | SI | VA-Nr 3 |
| Q28 | - |  |  | SI | Notes |
| Q29 | - |  |  | SI | Add 2 |
| Q30 | - |  |  | SI | Final Prescription Refraction |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | IPD |
| Q33 | - |  |  | SI | mm |
| Q34 | - |  |  | SI | Material |
| Q35 | - |  |  | SI | Right Eye |
| Q36 | - |  |  | SI | Left Eye |
| Q37 | - |  |  | SI | Sph |
| Q38 | - |  |  | SI | Sph2 |
| Q39 | - |  |  | SI | Both Eyes |
| Q40 | - |  |  | SI | Cyl |
| Q41 | - |  |  | SI | Cyl 2 |
| Q42 | - |  |  | SI | Axis |
| Q43 | - |  |  | SI | Axis 2 |
| Q44 | - |  |  | SI | Add |
| Q45 | - |  |  | SI | Add2 |
| Q46 | - |  |  | SI | VA-Dt |
| Q47 | - |  |  | SI | VA-Dt 2 |
| Q48 | - |  |  | SI | VA-Dt 3 |
| Q49 | - |  |  | SI | VA-Nr |
| Q50 | - |  |  | SI | VA-Nr 2 |
| Q51 | - |  |  | SI | VA-Nr 3 |
| Q52 | - |  |  | SI | Notes |
| Q53 | - |  |  | SI | Both Eyes |
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