# SQLUser.PAC_JourneyBoardGroup

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| JBGRP_RowId | bigint | PK |  | NO | - |
| JBGRP_Code | varchar |  |  | NO | Code |
| JBGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| JBGRP_DateFrom | date |  |  | SI | Date From |
| JBGRP_DateTo | date |  |  | SI | Date To |
| JBGRP_Desc | varchar |  |  | NO | Description |
| JBGRP_GroupByAppt | varchar |  |  | SI | Group By Appointment |
| JBGRP_Owner | varchar |  |  | SI | Owner |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Criterion A |
| Q04 | - |  |  | SI | At least 1 lead with ≥1 mm of concordant ST-segmen... |
| Q05 | - |  |  | SI | Criterion B |
| Q06 | - |  |  | SI | At least 1 lead of V1-V3 with ≥1 mm of concordant ... |
| Q07 | - |  |  | SI | Criterion C |
| Q08 | - |  |  | SI | At least 1 lead anywhere with ≥1 mm ST-segment ele... |
| Q09 | - |  |  | SI | The performance characteristics of this test in th... |
| Q10 | - |  |  | SI | sensitivity 80% (68 to 92%), specificity 99% (98 t... |
| Q11 | - |  |  | SI | This test is designed to detect acute coronary occ... |
| Q12 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | Classification |
| Q14 | - |  |  | SI | 0 |
| Q15 | - |  |  | SI | Criteria for diagnosis of acute coronary occlusion... |
| Q16 | - |  |  | SI | ≥ 1 |
| Q17 | - |  |  | SI | Criteria for diagnosis of acute coronary occlusion... |
| Q18 | - |  |  | SI | 0: Criteria for diagnosis of acute coronary occlus... |
| Q19 | - |  |  | SI | ≥ 1: Criteria for diagnosis of acute coronary occl... |
| Q20 | - |  |  | SI | A tool to diagnose ST-segment elevation myocardial... |
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