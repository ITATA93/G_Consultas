# questionnaire.QTCACVDRC

> Atherosclerotic Cardiovascular Disease Risk Calculator

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Atherosclerotic Cardiovascular Disease Risk Calculator

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Age |
| Q04 | varchar |  |  | SI | Age must be between 20 to 79 |
| Q05 | varchar |  |  | SI | Sex |
| Q06 | varchar |  |  | SI | Race |
| Q07 | varchar |  |  | SI | Systolic blood pressure (mm Hg) |
| Q07ObsDR | varchar |  | FK | SI | Systolic blood pressure (mm Hg) DR |
| Q08 | varchar |  |  | SI | Value must be between 90 to 200 |
| Q09 | varchar |  |  | SI | Diastolic blood pressure (mm Hg) |
| Q09ObsDR | varchar |  | FK | SI | Diastolic blood pressure (mm Hg) DR |
| Q10 | varchar |  |  | SI | Value must be between 60 to 130 |
| Q11 | numeric |  |  | SI | Total cholesterol (mg/dL) |
| Q12 | varchar |  |  | SI | Value must be between 130 to 320 |
| Q13 | numeric |  |  | SI | HDL cholesterol (mg/dL) |
| Q14 | varchar |  |  | SI | Value must be between 20 to 100 |
| Q15 | numeric |  |  | SI | LDL cholesterol (mg/dL) |
| Q16 | varchar |  |  | SI | Value must be between 30 to 300 |
| Q17 | varchar |  |  | SI | History of diabetes? |
| Q18 | varchar |  |  | SI | Smoker? |
| Q19 | varchar |  |  | SI | How long ago did patient quit smoking? |
| Q20 | varchar |  |  | SI | On hypertension treatment? |
| Q21 | varchar |  |  | SI | On a statin? |
| Q22 | varchar |  |  | SI | On aspirin therapy? |
| Q23 | varchar |  |  | SI | https://tools.acc.org/ascvd-risk-estimator-plus/#!... |
| Q24 | numeric |  |  | SI | Current 10-year Atherosclerotic Cardiovascular Dis... |
| Q25 | numeric |  |  | SI | Lifetime Atherosclerotic Cardiovascular Disease Ri... |
| Q26 | numeric |  |  | SI | Optimal Atherosclerotic Cardiovascular Disease Ris... |
| Q27 | varchar |  |  | SI | The Atherosclerotic Cardiovascular Disease Risk Es... |
| Q28 | varchar |  |  | SI | making to optimize care and lower risk for atheros... |
| Q29 | varchar |  |  | SI | • Atherosclerotic Cardiovascular Disease (ASCVD) r... |
| Q30 | varchar |  |  | SI | • The atherosclerotic cardiovascular disease (ASCV... |
| Q31 | varchar |  |  | SI | Calculator should only be used for primary prevent... |
| Q32 | varchar |  |  | SI | Values entered in this field should be only values... |
| Q33 | varchar |  |  | SI | This value is only calculated for patients between... |
| Q34 | varchar |  |  | SI | Current 10-year ASCVD risk % as follow: The follow... |
| Q35 | numeric |  |  | SI | Current 10-year Atherosclerotic Cardiovascular Dis... |
| Q36 | numeric |  |  | SI | Lifetime Atherosclerotic Cardiovascular Disease Ri... |
| Q37 | numeric |  |  | SI | Optimal Atherosclerotic Cardiovascular Disease Ris... |
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