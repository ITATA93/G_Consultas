# questionnaire.QTCAHOCCPST

> Pinch Strength Test

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pinch Strength Test

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Hand Strength Assessment |
| Q02 | varchar |  |  | SI | Jamar Dynamometer |
| Q03 | varchar |  |  | SI | Grip Strength (Left) No 1 |
| Q03ObsDR | varchar |  | FK | SI | Grip Strength (Left) No 1 DR |
| Q04 | varchar |  |  | SI | Grip Strength (Left) No 2 |
| Q04ObsDR | varchar |  | FK | SI | Grip Strength (Left) No 2 DR |
| Q05 | varchar |  |  | SI | Grip Strength (Left) No 3 |
| Q05ObsDR | varchar |  | FK | SI | Grip Strength (Left) No 3 DR |
| Q06 | varchar |  |  | SI | Grip Strength Average (Left)  |
| Q06ObsDR | varchar |  | FK | SI | Grip Strength Average (Left)  DR |
| Q07 | varchar |  |  | SI | Grip Strength Norm (Left) |
| Q07ObsDR | varchar |  | FK | SI | Grip Strength Norm (Left) DR |
| Q08 | varchar |  |  | SI | Grip Strength (Right) No 1 |
| Q08ObsDR | varchar |  | FK | SI | Grip Strength (Right) No 1 DR |
| Q09 | varchar |  |  | SI | Grip Strength (Right) No 2 |
| Q09ObsDR | varchar |  | FK | SI | Grip Strength (Right) No 2 DR |
| Q10 | varchar |  |  | SI | Grip Strength (Right) No 3 |
| Q10ObsDR | varchar |  | FK | SI | Grip Strength (Right) No 3 DR |
| Q11 | varchar |  |  | SI | Grip Strength Average (Right) |
| Q11ObsDR | varchar |  | FK | SI | Grip Strength Average (Right) DR |
| Q12 | varchar |  |  | SI | Grip Strength Norm (Right) |
| Q12ObsDR | varchar |  | FK | SI | Grip Strength Norm (Right) DR |
| Q13 | varchar |  |  | SI | Pinch Gauge |
| Q14 | varchar |  |  | SI | Lateral Pinch (Left) |
| Q14ObsDR | varchar |  | FK | SI | Lateral Pinch (Left) DR |
| Q15 | varchar |  |  | SI | Lateral Pinch (Right) |
| Q15ObsDR | varchar |  | FK | SI | Lateral Pinch (Right) DR |
| Q16 | varchar |  |  | SI | 3 Point Pinch (Left) |
| Q16ObsDR | varchar |  | FK | SI | 3 Point Pinch (Left) DR |
| Q17 | varchar |  |  | SI | 3 Point Pinch (Right) |
| Q17ObsDR | varchar |  | FK | SI | 3 Point Pinch (Right) DR |
| Q18 | varchar |  |  | SI | 2 Point Pinch (Left) |
| Q18ObsDR | varchar |  | FK | SI | 2 Point Pinch (Left) DR |
| Q19 | varchar |  |  | SI | 2 Point Pinch (Right) |
| Q19ObsDR | varchar |  | FK | SI | 2 Point Pinch (Right) DR |
| Q20 | varchar |  |  | SI | Note |
| Q21 | varchar |  |  | SI | Occupational Therapist Name |
| Q22 | date |  |  | SI | Date |
| Q23 | longvarbinary |  |  | SI | Signature |
| Q23UDt | date |  |  | SI | Signature Last Updated Date |
| Q23UTm | time |  |  | SI | Signature Last Updated Time |
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