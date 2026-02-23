# questionnaire.QTCTIMII

> Thrombolysis In Myocardial Infarction (TIMI) Risk Score for Unstable Angina/NSTEMI

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Thrombolysis In Myocardial Infarction (TIMI) Risk Score for Unstable Angina/NSTEMI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age >= 65 |
| Q02 | varchar |  |  | SI | >= 3 Coronary Artery Disease (CAD) risk factors  (... |
| Q03 | varchar |  |  | SI | Known CAD (stenosis >= 50%) |
| Q04 | varchar |  |  | SI | Acetylsalicylic Acid (ASA) e.g. Aspirin use in pas... |
| Q05 | varchar |  |  | SI | Severe angina (>= 2 episodes in 24 hrs) |
| Q06 | varchar |  |  | SI | EKG ST changes >= 0.5mm |
| Q07 | varchar |  |  | SI | Positive cardiac marker |
| Q08 | varchar |  |  | SI | Score |
| Q09 | varchar |  |  | SI | Classification |
| Q10 | varchar |  |  | SI | 0 - 1 |
| Q11 | varchar |  |  | SI | 5% risk at 14 days of: all-cause mortality, new or... |
| Q12 | varchar |  |  | SI | 2 |
| Q13 | varchar |  |  | SI | 8% risk at 14 days of: all-cause mortality, new or... |
| Q14 | varchar |  |  | SI | 3 |
| Q15 | varchar |  |  | SI | 13% risk at 14 days of: all-cause mortality, new o... |
| Q16 | varchar |  |  | SI | 4 |
| Q17 | varchar |  |  | SI | 20% risk at 14 days of: all-cause mortality, new o... |
| Q18 | varchar |  |  | SI | 5 |
| Q19 | varchar |  |  | SI | 26% risk at 14 days of: all-cause mortality, new o... |
| Q20 | varchar |  |  | SI | 6 - 7 |
| Q21 | varchar |  |  | SI | 41% risk at 14 days of: all-cause mortality, new o... |
| Q22 | varchar |  |  | SI | 0 - 1: 5% risk at 14 days of: all-cause mortality,... |
| Q23 | varchar |  |  | SI | 2: 8% risk at 14 days of: all-cause mortality, new... |
| Q24 | varchar |  |  | SI | 3: 13% risk at 14 days of: all-cause mortality, ne... |
| Q25 | varchar |  |  | SI | 4: 20% risk at 14 days of: all-cause mortality, ne... |
| Q26 | varchar |  |  | SI | 5: 26% risk at 14 days of: all-cause mortality, ne... |
| Q27 | varchar |  |  | SI | 6 - 7: 41% risk at 14 days of: all-cause mortality... |
| Q28 | varchar |  |  | SI | The TIMI (Thrombolysis In Myocardial Infarction) R... |
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