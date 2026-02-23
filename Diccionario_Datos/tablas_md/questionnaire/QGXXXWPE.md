# questionnaire.QGXXXWPE

> Wells Criteria for Pulmonary Embolism (PE)

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wells Criteria for Pulmonary Embolism (PE)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | 3 - Clinical signs and symptoms of deep vein throm... |
| Q02 | bit |  |  | SI | 3 - PE is number 1 Diagnosis, or equally likely |
| Q03 | bit |  |  | SI | 1.5 - Heart rate > 100 |
| Q04 | bit |  |  | SI | 1.5 - Immobilisation for at least 3 days, or surge... |
| Q05 | bit |  |  | SI | 1.5 - Previous, objectively diagnosed pulmonary em... |
| Q06 | bit |  |  | SI | 1 - Hemoptysis |
| Q07 | bit |  |  | SI | 1 - Malignancy on treatment, treated in the last 6... |
| Q08 | varchar |  |  | SI | 1 - 1.5: Low risk |
| Q09 | varchar |  |  | SI | 2 - 6: Moderate risk |
| Q10 | varchar |  |  | SI | 6.5 - 12.5: High risk |
| Q11 | varchar |  |  | SI | The Wells' Criteria for Pulmonary Embolism estimat... |
| Q12 | date |  |  | SI | Date |
| Q13 | time |  |  | SI | Time |
| Q14 | varchar |  |  | SI | Score |
| Q15 | varchar |  |  | SI | Classification |
| Q16 | varchar |  |  | SI | 1 - 1.5 |
| Q17 | varchar |  |  | SI | 2 - 6 |
| Q18 | varchar |  |  | SI | 6.5 - 12.5 |
| Q19 | varchar |  |  | SI | Low risk |
| Q20 | varchar |  |  | SI | Moderate risk |
| Q21 | varchar |  |  | SI | High risk |
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