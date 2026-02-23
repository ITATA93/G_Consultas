# questionnaire.QTCIPSS

> International Prostate Symptom Score (I-PSS)

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* International Prostate Symptom Score (I-PSS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | In the past month |
| Q02 | varchar |  |  | SI | How often have you had the sensation of not emptyi... |
| Q03 | varchar |  |  | SI | How often have you had to urinate less than every ... |
| Q04 | varchar |  |  | SI | How often have you found you stopped and started a... |
| Q05 | varchar |  |  | SI | How often have you found it difficult to postpone ... |
| Q06 | varchar |  |  | SI | How often have you had a weak urinary stream? |
| Q07 | varchar |  |  | SI | How often have you had to strain to start urinatio... |
| Q08 | varchar |  |  | SI | How many times did you typically get up at night t... |
| Q09 | varchar |  |  | SI | If you were to spend the rest of your life with yo... |
| Q10 | varchar |  |  | SI | The International Prostate Symptom Score (I-PSS) q... |
| Q11 | varchar |  |  | SI | Score |
| Q12 | varchar |  |  | SI | Classification |
| Q13 | varchar |  |  | SI | 0 |
| Q14 | varchar |  |  | SI | No symptoms |
| Q15 | varchar |  |  | SI | 1 - 7 |
| Q16 | varchar |  |  | SI | Mild |
| Q17 | varchar |  |  | SI | 8 - 19 |
| Q18 | varchar |  |  | SI | Moderate |
| Q19 | varchar |  |  | SI | 20 - 35 |
| Q20 | varchar |  |  | SI | Severe |
| Q21 | varchar |  |  | SI | 0: No symptoms |
| Q22 | varchar |  |  | SI | 1 - 7: Mild |
| Q23 | varchar |  |  | SI | 8 - 19: Moderate |
| Q24 | varchar |  |  | SI | 20 - 35: Severe |
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