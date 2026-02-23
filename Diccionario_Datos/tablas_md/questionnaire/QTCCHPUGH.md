# questionnaire.QTCCHPUGH

> The Child Pugh Score

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Child Pugh Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Bilirubin (total) |
| Q02 | varchar |  |  | SI | Albumin |
| Q03 | varchar |  |  | SI | INR |
| Q04 | varchar |  |  | SI | Ascites |
| Q05 | varchar |  |  | SI | Encephalopathy |
| Q06 | varchar |  |  | SI | Score Interpretation |
| Q07 | varchar |  |  | SI | • Child Class A |
| Q08 | varchar |  |  | SI | Life Expectancy : 15 - 20 years |
| Q09 | varchar |  |  | SI | Abdominal surgery peri-operative mortality: 10% |
| Q10 | varchar |  |  | SI | • Child Class B |
| Q11 | varchar |  |  | SI | Indication for transplant evaluation |
| Q12 | varchar |  |  | SI | Abdominal surgery peri-operative mortality: 30% |
| Q13 | varchar |  |  | SI | • Child Class C |
| Q14 | varchar |  |  | SI | Life Expectancy : 1 - 3 years |
| Q15 | varchar |  |  | SI | Abdominal surgery peri-operative mortality: 82% |
| Q16 | varchar |  |  | SI | Score |
| Q17 | varchar |  |  | SI | Classification |
| Q18 | varchar |  |  | SI | 5 – 6 |
| Q19 | varchar |  |  | SI | Child Class A - Life Expectancy: 15-20 years - Abd... |
| Q20 | varchar |  |  | SI | 7 – 9 |
| Q21 | varchar |  |  | SI | Child Class B - Indication for transplant evaluati... |
| Q22 | varchar |  |  | SI | 10 – 15 |
| Q23 | varchar |  |  | SI | Child Class C - Life Expectancy: 1 - 3 years - Abd... |
| Q24 | varchar |  |  | SI | 5 – 6: Child Class A - Life Expectancy: 15 - 20 ye... |
| Q25 | varchar |  |  | SI | 7 – 9: Child Class B - Indication for transplant e... |
| Q26 | varchar |  |  | SI | 10 – 15: Child Class C - Life Expectancy: 1 - 3 ye... |
| Q27 | date |  |  | SI | Date |
| Q28 | time |  |  | SI | Time |
| Q29 | varchar |  |  | SI | The Child-Pugh score is a system for assessing the... |
| Q30 | varchar |  |  | SI | It provides a forecast of the increasing severity ... |
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