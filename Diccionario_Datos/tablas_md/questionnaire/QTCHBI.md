# questionnaire.QTCHBI

> Harvey-Bradshaw Index (HBI) for Crohn's Disease

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Harvey-Bradshaw Index (HBI) for Crohn's Disease

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | General well-being: for the previous day, as repor... |
| Q04 | varchar |  |  | SI | Abdominal pain: for the previous day, as reported ... |
| Q05 | varchar |  |  | SI | Number of liquid / soft stools for the previous da... |
| Q06 | numeric |  |  | SI | Exact number of liquid / soft stools |
| Q07 | varchar |  |  | SI | Abdominal mass |
| Q08 | varchar |  |  | SI | Complications |
| Q09 | varchar |  |  | SI | Arthralgia |
| Q10 | varchar |  |  | SI | Uveitis |
| Q11 | varchar |  |  | SI | Erithema nodosum |
| Q12 | varchar |  |  | SI | Aphthous ulcers |
| Q13 | varchar |  |  | SI | Pyoderma gangrenosum |
| Q14 | varchar |  |  | SI | Anal fissures |
| Q15 | varchar |  |  | SI | New fistula |
| Q16 | varchar |  |  | SI | Abscess |
| Q17 | varchar |  |  | SI | Score |
| Q18 | varchar |  |  | SI | Classification |
| Q19 | varchar |  |  | SI | < 5 |
| Q20 | varchar |  |  | SI | Remission |
| Q21 | varchar |  |  | SI | 5 - 7 |
| Q22 | varchar |  |  | SI | Mild disease |
| Q23 | varchar |  |  | SI | 8 - 16 |
| Q24 | varchar |  |  | SI | Moderate disease |
| Q25 | varchar |  |  | SI | > 16 |
| Q26 | varchar |  |  | SI | Severe disease |
| Q27 | varchar |  |  | SI | < 5: Remission |
| Q28 | varchar |  |  | SI | 5 - 7: Mild disease |
| Q29 | varchar |  |  | SI | 8 - 16: Moderate disease |
| Q30 | varchar |  |  | SI | > 16: Severe disease |
| Q31 | varchar |  |  | SI | The Harvey Bradshaw Index (HBI) is a stratificatio... |
| Q32 | varchar |  |  | SI | Number of liquid / soft stools for the previous da... |
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