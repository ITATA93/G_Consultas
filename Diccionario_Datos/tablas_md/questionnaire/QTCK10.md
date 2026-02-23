# questionnaire.QTCK10

> Kessler Psychological Distress Scale

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Kessler Psychological Distress Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q02 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q03 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q04 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q05 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q06 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q07 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q08 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q09 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q10 | varchar |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q11 | varchar |  |  | SI | 10 - 19: Likely to be well |
| Q12 | varchar |  |  | SI | 20 - 24: Likely to have a mild disorder |
| Q13 | varchar |  |  | SI | 25 - 29: Likely to have a moderate disorder |
| Q14 | varchar |  |  | SI | 30 - 50: Likely to have a severe disorder |
| Q15 | varchar |  |  | SI | The Kessler Psychological Distress Scale (K10) is ... |
| Q16 | varchar |  |  | SI | 10 - 19: Likely to be well |
| Q17 | varchar |  |  | SI | 20 - 24: Likely to have a mild disorder |
| Q18 | varchar |  |  | SI | 25 - 29: Likely to have a moderate disorder |
| Q19 | varchar |  |  | SI | 30 - 50: Likely to have a severe disorder |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | varchar |  |  | SI | 10 - 19 |
| Q23 | varchar |  |  | SI | Likely to be well |
| Q24 | varchar |  |  | SI | 20 - 24 |
| Q25 | varchar |  |  | SI | Likely to have a mild disorder |
| Q26 | varchar |  |  | SI | 25 - 29 |
| Q27 | varchar |  |  | SI | Likely to have a moderate disorder |
| Q28 | varchar |  |  | SI | 30 - 50 |
| Q29 | varchar |  |  | SI | Likely to have a severe disorder |
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