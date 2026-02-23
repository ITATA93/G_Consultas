# SQLUser.PAC_NeonatalFeedingReport

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NATFR_RowId | bigint | PK |  | NO | - |
| NATFR_Code | varchar |  |  | SI | Code |
| NATFR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NATFR_CreatedDate | date |  |  | SI | Created Date |
| NATFR_CreatedTime | time |  |  | SI | Created Time |
| NATFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NATFR_Day0 | double |  |  | SI | Day0 |
| NATFR_Day1 | double |  |  | SI | Day1 |
| NATFR_Day2 | double |  |  | SI | Day2 |
| NATFR_Day3 | double |  |  | SI | Day3 |
| NATFR_Day4 | double |  |  | SI | Day4 |
| NATFR_Frequency | double |  |  | SI | Frequency |
| NATFR_HrsBetweenFeeding | double |  |  | SI | HrsBetweenFeeding |
| NATFR_Owner | varchar |  |  | SI | Owner |
| NATFR_UpdatedDate | date |  |  | SI | Updated Date |
| NATFR_UpdatedTime | time |  |  | SI | Updated Time |
| NATFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| NATFR_WeightFrom | double |  |  | SI | WeightFrom |
| NATFR_WeightTo | double |  |  | SI | WeightTo |
| Q01 | - |  |  | SI | Please select one of the following |
| Q02 | - |  |  | SI | Normal facial function in all areas |
| Q02a | - |  |  | SI | Gross: slight weakness noticeable on close inspect... |
| Q02b | - |  |  | SI | At rest: normal symmetry and tone |
| Q02c | - |  |  | SI | Motion: forehead - moderate to good function |
| Q03a | - |  |  | SI | Gross: obvious but not disfiguring difference betw... |
| Q03b | - |  |  | SI | At rest: normal symmetry and tone |
| Q03c | - |  |  | SI | Motion: forehead - slight to moderate movement |
| Q04a | - |  |  | SI | Gross: obvious weakness and/or disfiguring asymmet... |
| Q04b | - |  |  | SI | At rest: normal symmetry and tone |
| Q04c | - |  |  | SI | Motion: forehead - none |
| Q05a | - |  |  | SI | Gross: only barely perceptible motion |
| Q05b | - |  |  | SI | At rest: asymmetry |
| Q05c | - |  |  | SI | Motion: forehead - none |
| Q06a | - |  |  | SI | No movement |
| Q16 | - |  |  | SI | Grade I - Normal |
| Q17 | - |  |  | SI | Grade II - Slight dysfunction |
| Q18 | - |  |  | SI | Grade III - Moderate dysfunction |
| Q19 | - |  |  | SI | Grade IV - Moderate severe dysfunction |
| Q20 | - |  |  | SI | Grade V - Severe dysfunction |
| Q21 | - |  |  | SI | Grade VI - Total paralysis |
| Q22 | - |  |  | SI | The scale is simple, sensitive, accurate and relia... |
| Q23 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Time |
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