# questionnaire.QTCPGSI

> Problem Gambling Severity Index (PGSI)

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Problem Gambling Severity Index (PGSI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | In the last 12 months how often have you borrowed ... |
| Q11 | varchar |  |  | SI | In the last 12 months how often have you felt that... |
| Q12 | varchar |  |  | SI | In the last 12 months how often have you felt that... |
| Q13 | varchar |  |  | SI | In the last 12 months how often have you people cr... |
| Q14 | varchar |  |  | SI | In the last 12 months how often have you felt your... |
| Q15 | varchar |  |  | SI | In the last 12 months how often have you felt guil... |
| Q16 | varchar |  |  | SI | Provenance |
| Q17 | varchar |  |  | SI | 1.&nbsp;Ferris J, Wynne H, Single E.&nbsp;Canadian... |
| Q18 | varchar |  |  | SI | 2.&nbsp;Holtgraves T. Evaluating the Problem Gambl... |
| Q19 | varchar |  |  | SI | The Problem Gambling Severity Index (PGSI) is the ... |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Assessing where your client is now can help you ma... |
| Q21 | varchar |  |  | SI | This module can be self-administered by the client... |
| Q3 | varchar |  |  | SI | Instructions for Use |
| Q4 | varchar |  |  | SI | INTRODUCTION FOR CLIENT |
| Q5 | varchar |  |  | SI | Now Im going to ask you a series of questions in o... |
| Q6 | varchar |  |  | SI | Questions |
| Q7 | varchar |  |  | SI | In the last 12 months how often have you bet more ... |
| Q8 | varchar |  |  | SI | In the last 12 months how often have you needed to... |
| Q9 | varchar |  |  | SI | In the last 12 months how often have you gone back... |
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