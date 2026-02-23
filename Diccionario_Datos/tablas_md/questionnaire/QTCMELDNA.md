# questionnaire.QTCMELDNA

> Model for End-stage Liver Disease (MELD-Na) Score

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Model for End-stage Liver Disease (MELD-Na) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Currently receiving renal replacement therapy |
| Q04 | numeric |  |  | SI | Serum creatinine |
| Q05 | varchar |  |  | SI | mg/dL |
| Q06 | numeric |  |  | SI | Serum total bilirubin |
| Q07 | varchar |  |  | SI | mg/dL |
| Q08 | numeric |  |  | SI | International Normalised Ratio (INR) |
| Q09 | numeric |  |  | SI | Sodium |
| Q10 | varchar |  |  | SI | mmol/L |
| Q11 | varchar |  |  | SI | MELD-Na Score |
| Q12 | varchar |  |  | SI | MELD Score |
| Q13 | varchar |  |  | SI | Score Interpretation |
| Q14 | varchar |  |  | SI | Meld-Na Score |
| Q15 | varchar |  |  | SI | Score Interpretation |
| Q16 | varchar |  |  | SI | Meld-Na Score |
| Q17 | varchar |  |  | SI | 90-day mortality |
| Q18 | varchar |  |  | SI | ≤14 |
| Q19 | varchar |  |  | SI | 15 - 16 |
| Q20 | varchar |  |  | SI | 17 - 20 |
| Q21 | varchar |  |  | SI | 21 - 22 |
| Q22 | varchar |  |  | SI | 23 - 26 |
| Q23 | varchar |  |  | SI | 27 - 31 |
| Q24 | varchar |  |  | SI | ≥ 32 |
| Q25 | varchar |  |  | SI | 1% |
| Q26 | varchar |  |  | SI | 1% - 2% |
| Q27 | varchar |  |  | SI | 3 - 4 % |
| Q28 | varchar |  |  | SI | 7 - 10% |
| Q29 | varchar |  |  | SI | 14 - 15% |
| Q30 | varchar |  |  | SI | 27 - 32% |
| Q31 | varchar |  |  | SI | 65 - 66% |
| Q32 | varchar |  |  | SI | This score was adapted for estimating the 90-day r... |
| Q33 | varchar |  |  | SI | MELD-Na Score Interpretation |
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