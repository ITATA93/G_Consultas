# questionnaire.QTCAPACHEII

> APACHE II (Acute Physiology and Chronic Health Evaluation II)

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* APACHE II (Acute Physiology and Chronic Health Evaluation II)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | History of severe organ failure (heart failure cla... |
| Q02 | varchar |  |  | SI | Type of surgery |
| Q03 | varchar |  |  | SI | Age |
| Q04 | varchar |  |  | SI | Temperature, °C |
| Q05 | varchar |  |  | SI | Mean arterial pressure, mmHg |
| Q06 | varchar |  |  | SI | Heart rate, beats per minute |
| Q07 | varchar |  |  | SI | Respiratory rate, breaths per minute |
| Q08 | varchar |  |  | SI | Oxygenation (use PaO2 if FiO2 < 50%, otherwise use... |
| Q09 | varchar |  |  | SI | Arterial pH |
| Q10 | varchar |  |  | SI | Serum sodium, mmol/L |
| Q11 | varchar |  |  | SI | Serum potassium, mmol/L |
| Q12 | varchar |  |  | SI | Serum creatinine, mg/100 mL |
| Q13 | varchar |  |  | SI | Hematocrit, % |
| Q14 | varchar |  |  | SI | White blood count, total / cubic mm in 1000s |
| Q15 | varchar |  |  | SI | Glasgow Coma Scale (GCS) |
| Q16 | varchar |  |  | SI | Score |
| Q17 | varchar |  |  | SI | Classification |
| Q18 | varchar |  |  | SI | 0 - 4 |
| Q19 | varchar |  |  | SI | Nonoperative (4%) ; Postoperative (1%) |
| Q20 | varchar |  |  | SI | 5 - 9 |
| Q21 | varchar |  |  | SI | Nonoperative (8%) ; Postoperative (3%) |
| Q22 | varchar |  |  | SI | 10 - 14 |
| Q23 | varchar |  |  | SI | Nonoperative (15%) ; Postoperative (7%) |
| Q24 | varchar |  |  | SI | 15 - 19 |
| Q25 | varchar |  |  | SI | Nonoperative (25%) ; Postoperative (12%) |
| Q26 | varchar |  |  | SI | 20 - 24 |
| Q27 | varchar |  |  | SI | Nonoperative (40%) ; Postoperative (30%) |
| Q28 | varchar |  |  | SI | 25 - 29 |
| Q29 | varchar |  |  | SI | Nonoperative (55%) ; Postoperative (35%) |
| Q30 | varchar |  |  | SI | 30 - 34 |
| Q31 | varchar |  |  | SI | Nonoperative (73%) ; Postoperative (73%) |
| Q32 | varchar |  |  | SI | > 34 |
| Q33 | varchar |  |  | SI | Nonoperative (85%) ; Postoperative (88%) |
| Q34 | varchar |  |  | SI | 0 - 4: Nonoperative (4%) ; Postoperative (1%) |
| Q35 | varchar |  |  | SI | 5 - 9:  Nonoperative (8%) ; Postoperative (3%) |
| Q36 | varchar |  |  | SI | 10 - 14:  Nonoperative (15%) ; Postoperative (7%) |
| Q37 | varchar |  |  | SI | 15 - 19: Nonoperative (25%) ; Postoperative (12%) |
| Q38 | varchar |  |  | SI | 20 - 24: Nonoperative (40%) ; Postoperative (30%) |
| Q39 | varchar |  |  | SI | 25 - 29: Nonoperative (55%) ; Postoperative (35%) |
| Q40 | varchar |  |  | SI | 30 - 34: Nonoperative (73%) ; Postoperative (73%) |
| Q41 | varchar |  |  | SI | > 34: Nonoperative (85%) ; Postoperative (88%) |
| Q42 | varchar |  |  | SI | The APACHE II score was designed as a mortality pr... |
| Q43 | date |  |  | SI | Date |
| Q44 | time |  |  | SI | Time |
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