# questionnaire.QTCNBC

> Night Behavioural Chart

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Night Behavioural Chart

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Number of times out of bed |
| Q01ObsDR | varchar |  | FK | SI | Number of times out of bed DR |
| Q02 | varchar |  |  | SI | Incontinent |
| Q02ObsDR | varchar |  | FK | SI | Incontinent DR |
| Q02a | varchar |  |  | SI | Comments |
| Q03 | varchar |  |  | SI | Able to call for assistance |
| Q03ObsDR | varchar |  | FK | SI | Able to call for assistance DR |
| Q03a | varchar |  |  | SI | Comments |
| Q04 | varchar |  |  | SI | Wandering / Restless |
| Q04ObsDR | varchar |  | FK | SI | Wandering / Restless DR |
| Q04a | varchar |  |  | SI | Comments |
| Q05 | varchar |  |  | SI | Agitated |
| Q05ObsDR | varchar |  | FK | SI | Agitated DR |
| Q05a | varchar |  |  | SI | Comments |
| Q06 | varchar |  |  | SI | Settled with encouragement |
| Q06ObsDR | varchar |  | FK | SI | Settled with encouragement DR |
| Q06a | varchar |  |  | SI | Comments |
| Q07 | varchar |  |  | SI | Aggressive |
| Q07ObsDR | varchar |  | FK | SI | Aggressive DR |
| Q07a | varchar |  |  | SI | Comments |
| Q08 | varchar |  |  | SI | Tearful / Low in mood |
| Q08ObsDR | varchar |  | FK | SI | Tearful / Low in mood DR |
| Q08a | varchar |  |  | SI | Comments |
| Q09 | varchar |  |  | SI | Lying Awake |
| Q09ObsDR | varchar |  | FK | SI | Lying Awake DR |
| Q09a | varchar |  |  | SI | Comments |
| Q10 | varchar |  |  | SI | Hallucinating |
| Q10ObsDR | varchar |  | FK | SI | Hallucinating DR |
| Q10a | varchar |  |  | SI | Comments |
| Q11 | varchar |  |  | SI | Notes |
| Q12 | varchar |  |  | SI | Additional Notes |
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