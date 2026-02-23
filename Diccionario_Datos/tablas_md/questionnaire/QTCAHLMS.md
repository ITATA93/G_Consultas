# questionnaire.QTCAHLMS

> Lille Model Score

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lille Model Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | Age |
| Q04 | varchar |  |  | SI | years |
| Q05 | numeric |  |  | SI | Albumin |
| Q06 | varchar |  |  | SI | g/L |
| Q07 | numeric |  |  | SI | Bilirubin (initial) |
| Q08 | varchar |  |  | SI | mg/dL |
| Q09 | numeric |  |  | SI | Bilirubin (day 7) |
| Q10 | varchar |  |  | SI | mg/dL |
| Q11 | numeric |  |  | SI | Creatinine (Cr) |
| Q12 | varchar |  |  | SI | mg/dL |
| Q13 | numeric |  |  | SI | Prothrombin Time (PT) |
| Q14 | varchar |  |  | SI | sec |
| Q15 | varchar |  |  | SI | Score |
| Q16 | varchar |  |  | SI | Lille Score Item |
| Q17 | varchar |  |  | SI | Albumin |
| Q18 | varchar |  |  | SI | Bilirubin (initial) |
| Q19 | varchar |  |  | SI | Bilirubin (day 7) |
| Q20 | varchar |  |  | SI | Creatinine |
| Q21 | varchar |  |  | SI | Prothrombin Time |
| Q22 | varchar |  |  | SI | Normal Range |
| Q23 | varchar |  |  | SI | 35 - 55 |
| Q24 | varchar |  |  | SI | 0.3 - 1.9 |
| Q25 | varchar |  |  | SI | 0.3 - 1.9 |
| Q26 | varchar |  |  | SI | 0.7 - 1.3 |
| Q27 | varchar |  |  | SI | 11 – 13 |
| Q28 | varchar |  |  | SI | Unit of Measure |
| Q29 | varchar |  |  | SI | g/L |
| Q30 | varchar |  |  | SI | mg/dL |
| Q31 | varchar |  |  | SI | mg/dL |
| Q32 | varchar |  |  | SI | mg/dL |
| Q33 | varchar |  |  | SI | seconds |
| Q34 | varchar |  |  | SI | Score |
| Q35 | varchar |  |  | SI | Classification |
| Q36 | varchar |  |  | SI | ≤ 0.45 |
| Q37 | varchar |  |  | SI | > 0.45 |
| Q38 | varchar |  |  | SI | Predict a 6-month survival of 85% |
| Q39 | varchar |  |  | SI | Predict a 6-month survival of 25% |
| Q40 | varchar |  |  | SI | ≤ 0.45: Predict a 6-month survival of 85% |
| Q41 | varchar |  |  | SI | > 0.45: Predict a 6-month survival of 25% |
| Q42 | varchar |  |  | SI | The Lille Model Score risk stratifies patients alr... |
| Q43 | varchar |  |  | SI | It should be used for the identification of patien... |
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