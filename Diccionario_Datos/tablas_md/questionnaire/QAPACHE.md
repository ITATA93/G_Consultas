# questionnaire.QAPACHE

> APACHE Acute Physiology and Chronic Health Evaluation

**Schema:** questionnaire
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* APACHE Acute Physiology and Chronic Health Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ01 | varchar |  |  | SI | - |
| CQ010 | varchar |  |  | SI | - |
| CQ011 | varchar |  |  | SI | - |
| CQ012 | varchar |  |  | SI | - |
| CQ013 | varchar |  |  | SI | - |
| CQ014 | varchar |  |  | SI | - |
| CQ015 | varchar |  |  | SI | - |
| CQ016 | varchar |  |  | SI | - |
| CQ017 | varchar |  |  | SI | - |
| CQ018 | varchar |  |  | SI | - |
| CQ019 | varchar |  |  | SI | - |
| CQ02 | varchar |  |  | SI | - |
| CQ020 | varchar |  |  | SI | - |
| CQ021 | varchar |  |  | SI | - |
| CQ022 | varchar |  |  | SI | - |
| CQ023 | varchar |  |  | SI | - |
| CQ024 | varchar |  |  | SI | - |
| CQ025 | varchar |  |  | SI | - |
| CQ026 | varchar |  |  | SI | - |
| CQ027 | varchar |  |  | SI | - |
| CQ028 | varchar |  |  | SI | - |
| CQ029 | varchar |  |  | SI | - |
| CQ03 | varchar |  |  | SI | - |
| CQ030 | varchar |  |  | SI | - |
| CQ031 | varchar |  |  | SI | - |
| CQ032 | varchar |  |  | SI | - |
| CQ033 | varchar |  |  | SI | - |
| CQ034 | varchar |  |  | SI | - |
| CQ04 | varchar |  |  | SI | - |
| CQ044 | varchar |  |  | SI | - |
| CQ05 | varchar |  |  | SI | - |
| CQ06 | varchar |  |  | SI | - |
| CQ07 | varchar |  |  | SI | - |
| CQ08 | varchar |  |  | SI | - |
| CQ09 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | Heart Rate Ventricular Response |
| Q010 | varchar |  |  | SI | PaCO2 |
| Q011 | varchar |  |  | SI | Urine output in L per day |
| Q012 | varchar |  |  | SI | Serum BUN in mg/dL |
| Q013 | varchar |  |  | SI | Serum Creatinine in mg/dL |
| Q014 | varchar |  |  | SI | Serum Amylase in IU |
| Q015 | varchar |  |  | SI | Serum Albumin in g/dL |
| Q016 | varchar |  |  | SI | Total Bilirubin in mg/dL |
| Q017 | varchar |  |  | SI | Alkaline Phosphate in IU |
| Q018 | varchar |  |  | SI | SGOT |
| Q019 | varchar |  |  | SI | Anergy by skin testing |
| Q02 | varchar |  |  | SI | Mean Arterial Pessure |
| Q020 | varchar |  |  | SI | Hematocrit in percent |
| Q021 | varchar |  |  | SI | WBC |
| Q022 | varchar |  |  | SI | Platelet count |
| Q023 | varchar |  |  | SI | Prothrombin time in secs greater than control |
| Q024 | varchar |  |  | SI | CSF positive culture |
| Q025 | varchar |  |  | SI | Blood Culture positive |
| Q026 | varchar |  |  | SI | Fungal Culture positive |
| Q027 | varchar |  |  | SI | Rectal temperature in C |
| Q028 | varchar |  |  | SI | Serum Calcium |
| Q029 | varchar |  |  | SI | Serum Glucose |
| Q03 | varchar |  |  | SI | Right Artial Pressure ot Central Venous Pressure |
| Q030 | varchar |  |  | SI | Serum Sodium |
| Q031 | varchar |  |  | SI | Serum Potassium |
| Q032 | varchar |  |  | SI | Serum Bicarbonate |
| Q033 | varchar |  |  | SI | Serum Osmolarity |
| Q034 | varchar |  |  | SI | Glasgow Coma Score |
| Q035 | varchar |  |  | SI | Cardiovascular Status |
| Q036 | varchar |  |  | SI | Respiratory Status |
| Q037 | varchar |  |  | SI | Renal Status |
| Q038 | varchar |  |  | SI | Gastrointestinal Status |
| Q039 | varchar |  |  | SI | Hematological Status |
| Q04 | varchar |  |  | SI | Evidence of Acute MI |
| Q040 | varchar |  |  | SI | Septic Status |
| Q041 | varchar |  |  | SI | Metabolic Status |
| Q042 | varchar |  |  | SI | Neurological Status |
| Q043 | varchar |  |  | SI | APACHE Score |
| Q044 | varchar |  |  | SI | Pre-Admission Health Status |
| Q045 | varchar |  |  | SI | D Severe restriction of activity due to disease; i... |
| Q046 | varchar |  |  | SI | C chronic disease producing serious but not incapc... |
| Q047 | varchar |  |  | SI | B mild to moderate limitation in activity because ... |
| Q048 | varchar |  |  | SI | A prior good heatlh with no functional limitations |
| Q05 | varchar |  |  | SI | ECG Arrhythmias |
| Q06 | varchar |  |  | SI | Serum lactate in mg/dL |
| Q07 | varchar |  |  | SI | Arterial pH |
| Q08 | varchar |  |  | SI | Respiratory Rate Nonventilated |
| Q09 | varchar |  |  | SI | P(A-a) O2 with FIO2 = 1.0 |
| Q49 | varchar |  |  | SI | The  Acute Physiology and Chronic Health Evaluatio... |
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