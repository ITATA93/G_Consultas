# questionnaire.QTCPIPP

> Premature Infant Pain Profile

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Premature Infant Pain Profile

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Gestational age |
| Q02 | varchar |  |  | SI | Alertness |
| Q03 | varchar |  |  | SI | Heart rate maximum |
| Q04 | varchar |  |  | SI | Oxygen saturation minimum |
| Q05 | varchar |  |  | SI | Brow bulge |
| Q06 | varchar |  |  | SI | Eye squeeze |
| Q07 | varchar |  |  | SI | Nasolabial furrow |
| Q08 | varchar |  |  | SI | Minimum score : 0 |
| Q09 | varchar |  |  | SI | Maximum score : 21 |
| Q10 | varchar |  |  | SI | Score above 6 indicates pain |
| Q11 | varchar |  |  | SI | Premature Infant Pain Profile (PIPP) is used to as... |
| Q12 | varchar |  |  | SI | Absent: is defined as 0% to 9% of the observation ... |
| Q13 | varchar |  |  | SI | Minimal: 10% to 39% of the time |
| Q14 | varchar |  |  | SI | Moderate: 40% to 69% of the time |
| Q15 | varchar |  |  | SI | Maximal: 70% or more of the time |
| Q16 | date |  |  | SI | Date |
| Q17 | time |  |  | SI | Time |
| Q18 | varchar |  |  | SI | Score |
| Q19 | varchar |  |  | SI | Classification |
| Q20 | varchar |  |  | SI | ≤ 6 |
| Q21 | varchar |  |  | SI | Minimal or no pain |
| Q22 | varchar |  |  | SI | 7 - 12 |
| Q23 | varchar |  |  | SI | Slight to moderate pain |
| Q24 | varchar |  |  | SI | ≥ 13 |
| Q25 | varchar |  |  | SI | Severe pain |
| Q26 | varchar |  |  | SI | ≤ 6: Minimal or no pain |
| Q27 | varchar |  |  | SI | 7 - 12: Slight to moderate pain |
| Q28 | varchar |  |  | SI | ≥ 13: Severe pain |
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