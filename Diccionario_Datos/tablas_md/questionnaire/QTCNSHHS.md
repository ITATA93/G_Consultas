# questionnaire.QTCNSHHS

> Hunt and Hess Scale

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hunt and Hess Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Signs / Symptoms |
| Q02 | varchar |  |  | SI | Please select one of the following |
| Q03 | varchar |  |  | SI | Score 1: Grade I (have an approximate 30% mortalit... |
| Q04 | varchar |  |  | SI | Score 2: Grade II (have an approximate 40% mortali... |
| Q05 | varchar |  |  | SI | Score 3: Grade III (have an approximate 50% mortal... |
| Q06 | varchar |  |  | SI | Score 4: Grade IV (have an approximate 80% mortali... |
| Q07 | varchar |  |  | SI | Score 5: Grade V (have an approximate 90% mortalit... |
| Q08 | varchar |  |  | SI | The scale is used to classify the severity of a su... |
| Q09 | varchar |  |  | SI | A higher grade predicts a poor outcome and lower l... |
| Q10 | varchar |  |  | SI | 1 |
| Q11 | varchar |  |  | SI | Grade I (have an approximate 30% mortality) |
| Q12 | varchar |  |  | SI | 2 |
| Q13 | varchar |  |  | SI | Grade II (have an approximate 40% mortality) |
| Q14 | varchar |  |  | SI | 3 |
| Q15 | varchar |  |  | SI | Grade III (have an approximate 50% mortality) |
| Q16 | varchar |  |  | SI | 4 |
| Q17 | varchar |  |  | SI | Grade IV (have an approximate 80% mortality) |
| Q18 | varchar |  |  | SI | 5 |
| Q19 | varchar |  |  | SI | Grade V (have an approximate 90% mortality) |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | date |  |  | SI | Date |
| Q23 | time |  |  | SI | Time |
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