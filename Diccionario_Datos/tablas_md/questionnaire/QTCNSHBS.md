# questionnaire.QTCNSHBS

> House Brackmann Scale

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* House Brackmann Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please select one of the following |
| Q02 | varchar |  |  | SI | Normal facial function in all areas |
| Q02a | varchar |  |  | SI | Gross: slight weakness noticeable on close inspect... |
| Q02b | varchar |  |  | SI | At rest: normal symmetry and tone |
| Q02c | varchar |  |  | SI | Motion: forehead - moderate to good function; eye ... |
| Q03a | varchar |  |  | SI | Gross: obvious but not disfiguring difference betw... |
| Q03b | varchar |  |  | SI | At rest: normal symmetry and tone |
| Q03c | varchar |  |  | SI | Motion: forehead - slight to moderate movement; ey... |
| Q04a | varchar |  |  | SI | Gross: obvious weakness and/or disfiguring asymmet... |
| Q04b | varchar |  |  | SI | At rest: normal symmetry and tone |
| Q04c | varchar |  |  | SI | Motion: forehead - none; eye - incomplete closure;... |
| Q05a | varchar |  |  | SI | Gross: only barely perceptible motion |
| Q05b | varchar |  |  | SI | At rest: asymmetry |
| Q05c | varchar |  |  | SI | Motion: forehead - none; eye - incomplete closure;... |
| Q06a | varchar |  |  | SI | No movement |
| Q16 | varchar |  |  | SI | Grade I - Normal |
| Q17 | varchar |  |  | SI | Grade II - Slight dysfunction |
| Q18 | varchar |  |  | SI | Grade III - Moderate dysfunction |
| Q19 | varchar |  |  | SI | Grade IV - Moderate severe dysfunction |
| Q20 | varchar |  |  | SI | Grade V - Severe dysfunction |
| Q21 | varchar |  |  | SI | Grade VI - Total paralysis |
| Q22 | varchar |  |  | SI | The scale is simple, sensitive, accurate and relia... |
| Q23 | date |  |  | SI | Date |
| Q24 | time |  |  | SI | Time |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*