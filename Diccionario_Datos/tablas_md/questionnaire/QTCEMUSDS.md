# questionnaire.QTCEMUSDS

> Epilepsy Monitoring and Seizure Detection Sheet

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Epilepsy Monitoring and Seizure Detection Sheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Assessment date |
| Q02 | time |  |  | SI | Assessment time |
| Q03 | date |  |  | SI | Seizure onset date |
| Q04 | numeric |  |  | SI | Seizure number |
| Q05 | time |  |  | SI | Seizure onset time |
| Q06 | varchar |  |  | SI | Seizure semiology |
| Q07 | varchar |  |  | SI | Pre-ictal (before seizure)(aura) |
| Q08 | varchar |  |  | SI | Warning sign |
| Q09 | varchar |  |  | SI | Description |
| Q10 | varchar |  |  | SI | Ictal stage (during seizure) |
| Q11 | varchar |  |  | SI | Description |
| Q12 | varchar |  |  | SI | Duration |
| Q13 | numeric |  |  | SI | Exact duration (minutes) |
| Q14 | varchar |  |  | SI | Preserve awareness |
| Q15 | varchar |  |  | SI | Seizure terminates spontaneously |
| Q16 | varchar |  |  | SI | Evaluation during seizure |
| Q17 | varchar |  |  | SI | Memory: ask the patient if he/she remembers |
| Q18 | varchar |  |  | SI | Number |
| Q19 | varchar |  |  | SI | Phrase |
| Q20 | varchar |  |  | SI | Language : |
| Q21 | varchar |  |  | SI | Ask patient about his/her name |
| Q22 | varchar |  |  | SI | Ask the patient to point to TV, window or any obje... |
| Q23 | varchar |  |  | SI | Post ictal evaluation (after seizure) |
| Q24 | varchar |  |  | SI | Memory |
| Q25 | varchar |  |  | SI | Patient able to recall given number and phrase |
| Q26 | varchar |  |  | SI | Vision, receptive, expressive language |
| Q27 | varchar |  |  | SI | Ask patient to name shown object (pen, watch...) |
| Q28 | varchar |  |  | SI | Ask patient to do a motor action on each side of t... |
| Q29 | varchar |  |  | SI | Point to ceiling, window, door.. |
| Q30 | varchar |  |  | SI | Trauma or injuries |
| Q31 | varchar |  |  | SI | Specify |
| Q32 | varchar |  |  | SI | Nurse name |
| Q33 | varchar |  |  | SI | Nurse ID number |
| Q34 | longvarbinary |  |  | SI | Signature |
| Q34UDt | date |  |  | SI | Signature Last Updated Date |
| Q34UTm | time |  |  | SI | Signature Last Updated Time |
| Q35 | varchar |  |  | SI | Attending nurse actions |
| Q36 | numeric |  |  | SI | Exact duration (seconds) |
| Q37 | varchar |  |  | SI | Ictal Stage |
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