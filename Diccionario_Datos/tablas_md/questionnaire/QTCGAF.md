# questionnaire.QTCGAF

> Global Assessment of Functioning (GAF) Scale

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Global Assessment of Functioning (GAF) Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Consider psychological, social, and occupational f... |
| Q02 | varchar |  |  | SI | Do not include impairment in functioning due to ph... |
| Q03 | varchar |  |  | SI | Rating scale |
| Q04 | varchar |  |  | SI | Superior functioning in a wide range of activities... |
| Q05 | varchar |  |  | SI | Absent or minimal symptoms (e.g., mild anxiety bef... |
| Q05B | varchar |  |  | SI | Socially effective, generally satisfied with life,... |
| Q06 | varchar |  |  | SI | If symptoms are present, they are transient and ex... |
| Q06B | varchar |  |  | SI | No more than slight impairment in social, occupati... |
| Q07 | varchar |  |  | SI | Some mild symptoms (e.g. depressed mood and mild i... |
| Q07B | varchar |  |  | SI | OR some difficulty in social, occupational, or sch... |
| Q07C | varchar |  |  | SI | (e.g., occasional truancy, or theft within the hou... |
| Q08 | varchar |  |  | SI | Moderate symptoms (e.g., flat affect and circumsta... |
| Q08B | varchar |  |  | SI | OR moderate difficulty in social, occupational, or... |
| Q09 | varchar |  |  | SI | Serious symptoms (e.g.. suicidal ideation, severe ... |
| Q09B | varchar |  |  | SI | OR any serious impairment in social, occupational,... |
| Q10 | varchar |  |  | SI | Some impairment in reality testing or communicatio... |
| Q10B | varchar |  |  | SI | OR major impairment in several areas, such as work... |
| Q10C | varchar |  |  | SI | (e.g., depressed man avoids friends, neglects fami... |
| Q11 | varchar |  |  | SI | Behaviour is considerably influenced by delusions ... |
| Q11B | varchar |  |  | SI | OR serious impairment in communication or judgment... |
| Q11C | varchar |  |  | SI | OR inability to function in almost all areas (e.g.... |
| Q12 | varchar |  |  | SI | Some danger of hurting self or others (e.g., suici... |
| Q12B | varchar |  |  | SI | OR occasionally fails to maintain minimal personal... |
| Q12C | varchar |  |  | SI | OR gross impairment in communication (e.g., largel... |
| Q13 | varchar |  |  | SI | Persistent danger of severely hurting self or othe... |
| Q13B | varchar |  |  | SI | OR persistent inability to maintain minimal person... |
| Q13C | varchar |  |  | SI | OR serious suicidal act with clear expectation of ... |
| Q14 | varchar |  |  | SI | Inadequate information |
| Q30 | varchar |  |  | SI | A higher number is associated with a higher degree... |
| Q31 | varchar |  |  | SI | The Global Assessment of Functioning (GAF) is a nu... |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | varchar |  |  | SI | 0 |
| Q35 | varchar |  |  | SI | 10 - 1 |
| Q36 | varchar |  |  | SI | 20 - 11 |
| Q37 | varchar |  |  | SI | 30 - 21 |
| Q38 | varchar |  |  | SI | 40 - 31 |
| Q39 | varchar |  |  | SI | 50 - 41 |
| Q40 | varchar |  |  | SI | 60 - 51 |
| Q41 | varchar |  |  | SI | 70 - 61 |
| Q42 | numeric |  |  | SI | Score |
| Q43 | varchar |  |  | SI | 80 - 71 |
| Q44 | varchar |  |  | SI | 90 - 81 |
| Q45 | varchar |  |  | SI | 100 - 91 |
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