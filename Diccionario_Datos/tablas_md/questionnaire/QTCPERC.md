# questionnaire.QTCPERC

> Pulmonary Embolism Rule-Out Criteria (PERC)

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pulmonary Embolism Rule-Out Criteria (PERC)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Age ≥ 50 years |
| Q04 | varchar |  |  | SI | HR ≥ 100 bpm |
| Q05 | varchar |  |  | SI | Oxygen saturation on room air < 95% |
| Q06 | varchar |  |  | SI | Unilateral leg swelling |
| Q07 | varchar |  |  | SI | Hemoptysis |
| Q08 | varchar |  |  | SI | Recent surgery or trauma |
| Q09 | varchar |  |  | SI | Prior pulmonary embolism or deep vein thrombosis |
| Q10 | varchar |  |  | SI | Hormone use |
| Q11 | varchar |  |  | SI | Defintions |
| Q12 | varchar |  |  | SI | Recent surgery or trauma: |
| Q13 | varchar |  |  | SI | Surgery or trauma ≤ 4 weeks ago requiring treatmen... |
| Q14 | varchar |  |  | SI | Hormone use: |
| Q15 | varchar |  |  | SI | Oral contraceptives, hormone replacement or estrog... |
| Q16 | varchar |  |  | SI | When to Use: |
| Q17 | varchar |  |  | SI | The PERC rule should only be considered for use wh... |
| Q18 | varchar |  |  | SI | it should not be applied to all patients in whom a... |
| Q19 | varchar |  |  | SI | If one or more criteria are positive, pulmonary em... |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | varchar |  |  | SI | 1 - 8 |
| Q23 | varchar |  |  | SI | One or more positive criteria. Pulmonary embolism ... |
| Q24 | varchar |  |  | SI | 1 - 8: One or more positive criteria. Pulmonary em... |
| Q25 | varchar |  |  | SI | The PERC rule is used to rule out pulmonary emboli... |
| Q26 | varchar |  |  | SI | Requirements for this questionnaire have been comp... |
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