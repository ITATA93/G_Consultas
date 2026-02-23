# questionnaire.QTCGUGTB

> Get Up and Go Test (Falls Risk)

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Get Up and Go Test (Falls Risk)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI |  Following the steps described in the Guidelines. ... |
| Q04 | varchar |  |  | SI | Get Up and Go Test result |
| Q05 | varchar |  |  | SI | Normal indicates that the patient gave no evidence... |
| Q06 | varchar |  |  | SI | Severely abnormal indicates that the patient appea... |
| Q07 | varchar |  |  | SI | Intermediate grades reflect the presence of any of... |
| Q08 | varchar |  |  | SI | Instructions |
| Q09 | varchar |  |  | SI | Ask the patient to perform the following series of... |
| Q10 | varchar |  |  | SI | 1. Sit comfortably in a straight-backed chair. |
| Q11 | varchar |  |  | SI | 2. Rise from the chair. |
| Q12 | varchar |  |  | SI | 3. Stand still momentarily. |
| Q13 | varchar |  |  | SI | 4. Walk a short distance (approximately 3 meters). |
| Q14 | varchar |  |  | SI | 6. Walk back to the chair. |
| Q15 | varchar |  |  | SI | 7. Turn around. |
| Q16 | varchar |  |  | SI | 8. Sit down in the chair |
| Q17 | varchar |  |  | SI | Scoring |
| Q18 | varchar |  |  | SI | Normal indicates that the patient gave no evidence... |
| Q19 | varchar |  |  | SI | Severely abnormal indicates that the patient appea... |
| Q20 | varchar |  |  | SI | Intermediate grades reflect the presence of any of... |
| Q21 | varchar |  |  | SI | Result |
| Q22 | varchar |  |  | SI | A patient with a score of 3 or more on the Get-up ... |
| Q23 | varchar |  |  | SI | The Get Up and Go Test is used to measure balance ... |
| Q24 | varchar |  |  | SI | 5. Turn around. |
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