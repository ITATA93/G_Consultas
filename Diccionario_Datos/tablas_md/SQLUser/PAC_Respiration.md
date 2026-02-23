# SQLUser.PAC_Respiration

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESP_RowId | bigint | PK |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | In the last 12 months how often have you borrowed ... |
| Q11 | - |  |  | SI | In the last 12 months how often have you felt that... |
| Q12 | - |  |  | SI | In the last 12 months how often have you felt that... |
| Q13 | - |  |  | SI | In the last 12 months how often have you people cr... |
| Q14 | - |  |  | SI | In the last 12 months how often have you felt your... |
| Q15 | - |  |  | SI | In the last 12 months how often have you felt guil... |
| Q16 | - |  |  | SI | Provenance |
| Q17 | - |  |  | SI | 1.&nbsp |
| Q18 | - |  |  | SI | 2.&nbsp |
| Q19 | - |  |  | SI | The Problem Gambling Severity Index (PGSI) is the ... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Assessing where your client is now can help you ma... |
| Q21 | - |  |  | SI | This module can be self-administered by the client... |
| Q3 | - |  |  | SI | Instructions for Use |
| Q4 | - |  |  | SI | INTRODUCTION FOR CLIENT |
| Q5 | - |  |  | SI | Now Im going to ask you a series of questions in o... |
| Q6 | - |  |  | SI | Questions |
| Q7 | - |  |  | SI | In the last 12 months how often have you bet more ... |
| Q8 | - |  |  | SI | In the last 12 months how often have you needed to... |
| Q9 | - |  |  | SI | In the last 12 months how often have you gone back... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| RESP_Code | varchar |  |  | NO | Code |
| RESP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESP_CreatedDate | date |  |  | SI | Created Date |
| RESP_CreatedTime | time |  |  | SI | Created Time |
| RESP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESP_DateFrom | date |  |  | SI | Date From |
| RESP_DateTo | date |  |  | SI | Date To |
| RESP_Desc | varchar |  |  | NO | Description |
| RESP_NationalCode | varchar |  |  | SI | National Code |
| RESP_Owner | varchar |  |  | SI | Owner |
| RESP_UpdatedDate | date |  |  | SI | Updated Date |
| RESP_UpdatedTime | time |  |  | SI | Updated Time |
| RESP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*