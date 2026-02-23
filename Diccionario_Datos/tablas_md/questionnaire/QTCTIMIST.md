# questionnaire.QTCTIMIST

> TIMI Risk Score for STEMI

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* TIMI Risk Score for STEMI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Anterior ST-segment elevation or left bundle branc... |
| Q11 | varchar |  |  | SI | Time to treatment > 4 hours |
| Q12 | varchar |  |  | SI | Score |
| Q13 | varchar |  |  | SI | Classification |
| Q14 | varchar |  |  | SI | 0 |
| Q15 | varchar |  |  | SI | 1 |
| Q16 | varchar |  |  | SI | 2 |
| Q17 | varchar |  |  | SI | 3 |
| Q18 | varchar |  |  | SI | 4 |
| Q19 | varchar |  |  | SI | 5 |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | 6 |
| Q21 | varchar |  |  | SI | 7 |
| Q22 | varchar |  |  | SI | 8 |
| Q23 | varchar |  |  | SI | 9 - 14 |
| Q24 | varchar |  |  | SI | 0.8% risk of all-cause mortality at 30 days |
| Q25 | varchar |  |  | SI | 1.6% risk of all-cause mortality at 30 days |
| Q26 | varchar |  |  | SI | 2.2% risk of all-cause mortality at 30 days |
| Q27 | varchar |  |  | SI | 4.4% risk of all-cause mortality at 30 days |
| Q28 | varchar |  |  | SI | 7.3% risk of all-cause mortality at 30 days |
| Q29 | varchar |  |  | SI | 12.4% risk of all-cause mortality at 30 days |
| Q3 | varchar |  |  | SI | Patient age range |
| Q30 | varchar |  |  | SI | 16.1% risk of all-cause mortality at 30 days |
| Q31 | varchar |  |  | SI | 23.4% risk of all-cause mortality at 30 days |
| Q32 | varchar |  |  | SI | 26.8% risk of all-cause mortality at 30 days |
| Q33 | varchar |  |  | SI | 35.9% risk of all-cause mortality at 30 days |
| Q34 | varchar |  |  | SI | 0: 0.8% risk of all-cause mortality at 30 days |
| Q35 | varchar |  |  | SI | 1: 1.6% risk of all-cause mortality at 30 days |
| Q36 | varchar |  |  | SI | 2: 2.2% risk of all-cause mortality at 30 days |
| Q37 | varchar |  |  | SI | 3: 4.4% risk of all-cause mortality at 30 days |
| Q38 | varchar |  |  | SI | 4: 7.3% risk of all-cause mortality at 30 days |
| Q39 | varchar |  |  | SI | 5: 12.4% risk of all-cause mortality at 30 days |
| Q4 | varchar |  |  | SI | Diabetes, hypertension or angina |
| Q40 | varchar |  |  | SI | 6: 16.1% risk of all-cause mortality at 30 days |
| Q41 | varchar |  |  | SI | 7: 23.4% risk of all-cause mortality at 30 days |
| Q42 | varchar |  |  | SI | 8: 26.8% risk of all-cause mortality at 30 days |
| Q43 | varchar |  |  | SI | 9 - 14: 35.9% risk of all-cause mortality at 30 da... |
| Q44 | varchar |  |  | SI | The TIMI Risk Score for STEMI is a simple integer ... |
| Q45 | varchar |  |  | SI | with ST-elevation acute coronary syndromes. |
| Q5 | varchar |  |  | SI | Systolic BP < 100 mmHg |
| Q6 | varchar |  |  | SI | Heart rate > 100 b/min |
| Q7 | varchar |  |  | SI | Killip Class II-IV |
| Q8 | varchar |  |  | SI | Jugular Vein Distention (JVD) or any pulmonary exa... |
| Q9 | varchar |  |  | SI | Weight < 67kg (147.7 lbs) |
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