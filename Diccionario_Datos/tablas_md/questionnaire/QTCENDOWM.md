# questionnaire.QTCENDOWM

> Endocrinology Weight Management Review

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endocrinology Weight Management Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | numeric |  |  | SI | Body fat	 |
| Q03 | numeric |  |  | SI | Fat mass	 |
| Q04 | varchar |  |  | SI | Obesity related comorbidities	 |
| Q05 | varchar |  |  | SI | Diastolic BP	 |
| Q05ObsDR | varchar |  | FK | SI | Diastolic BP	 DR |
| Q06 | varchar |  |  | SI | Systolic BP	 |
| Q06ObsDR | varchar |  | FK | SI | Systolic BP	 DR |
| Q07 | varchar |  |  | SI | Past weight history	 |
| Q08 | varchar |  |  | SI | Name of slimming pills	 |
| Q09 | varchar |  |  | SI | Age of onset of weight problems	 |
| Q10 | varchar |  |  | SI | Eating habits	 |
| Q11 | varchar |  |  | SI | Binge eater	 |
| Q12 | varchar |  |  | SI | Comfort eater	 |
| Q13 | varchar |  |  | SI | Questionnaire received back from the patient	 |
| Q14 | varchar |  |  | SI | Notes |
| Q15 | varchar |  |  | SI | Lying Systolic |
| Q15ObsDR | varchar |  | FK | SI | Lying Systolic DR |
| Q16 | varchar |  |  | SI | Lying Diastolic |
| Q16ObsDR | varchar |  | FK | SI | Lying Diastolic DR |
| Q17 | varchar |  |  | SI | Standing Systolic |
| Q17ObsDR | varchar |  | FK | SI | Standing Systolic DR |
| Q18 | varchar |  |  | SI | Standing Diastolic |
| Q18ObsDR | varchar |  | FK | SI | Standing Diastolic DR |
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