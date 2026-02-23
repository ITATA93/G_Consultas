# questionnaire.QGXXXWATERL

> Waterlow Scale

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Waterlow Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Build / Weight for Height |
| Q02 | varchar |  |  | SI | Skin Type Visual Risk Areas |
| Q03 | varchar |  |  | SI | Continence |
| Q04 | varchar |  |  | SI | Age |
| Q05 | varchar |  |  | SI | Mobility |
| Q06 | varchar |  |  | SI | Appetite |
| Q07 | varchar |  |  | SI | Tissue malnutrition |
| Q08 | varchar |  |  | SI | Neurological deficit |
| Q09 | varchar |  |  | SI | Major Surgery / Trauma |
| Q10 | varchar |  |  | SI | Medication |
| Q11 | varchar |  |  | SI | 10+ At risk |
| Q12 | varchar |  |  | SI | 15+ High risk |
| Q13 | varchar |  |  | SI | 20+ Very high risk |
| Q14 | varchar |  |  | SI | The Waterlow scale gives an estimated risk for the... |
| Q15 | varchar |  |  | SI | Sex |
| Q16 | varchar |  |  | SI | Neurological deficit (score) |
| Q17 | date |  |  | SI | Date |
| Q18 | varchar |  |  | SI | Medication Score |
| Q18a | varchar |  |  | SI | Medication Score |
| Q21 | varchar |  |  | SI | Skin type visual risk areas |
| Q22 | time |  |  | SI | Time |
| Q23 | varchar |  |  | SI | Score |
| Q24 | varchar |  |  | SI | Classification |
| Q25 | varchar |  |  | SI | 0 - 9 |
| Q26 | varchar |  |  | SI | No risk |
| Q27 | varchar |  |  | SI | 10 - 14 |
| Q28 | varchar |  |  | SI | At risk |
| Q29 | varchar |  |  | SI | 15 - 19 |
| Q30 | varchar |  |  | SI | High risk |
| Q31 | varchar |  |  | SI | > 20 |
| Q32 | varchar |  |  | SI | Very high risk |
| Q33 | varchar |  |  | SI | 0 - 9: No risk |
| Q34 | varchar |  |  | SI | 10 - 14: At risk |
| Q35 | varchar |  |  | SI | 15 - 19: High Risk |
| Q36 | varchar |  |  | SI | > 20: Very high risk |
| Q37 | varchar |  |  | SI | Neurological deficit - Diabetes/ MS/ CVA/ motor/ s... |
| Q38 | varchar |  |  | SI | Medication - Cytotoxic, anti-inflammatory, long te... |
| Q9a | varchar |  |  | SI | Major Surgery / Trauma |
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