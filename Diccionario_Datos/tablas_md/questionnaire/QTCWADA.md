# questionnaire.QTCWADA

> Wada Test Scoring Form

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wada Test Scoring Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Test date |
| Q02 | time |  |  | SI | Test time |
| Q03 | varchar |  |  | SI | A - Sedation Phase |
| Q04 | time |  |  | SI | Injection time |
| Q05 | varchar |  |  | SI | The expressive language score during counting |
| Q06 | varchar |  |  | SI | Memory registration |
| Q07 | varchar |  |  | SI | Token comprehension test score |
| Q08 | varchar |  |  | SI | Confrontation naming |
| Q09 | varchar |  |  | SI | Reading |
| Q10 | varchar |  |  | SI | B - Recovery and Recall Phase (10 min post-injecti... |
| Q11 | varchar |  |  | SI | If language impairment present, continue to test r... |
| Q12 | time |  |  | SI | Time of recovery |
| Q13 | varchar |  |  | SI | Demonstrate return of 5/5 power |
| Q14 | varchar |  |  | SI | Absence of pronator drift |
| Q15 | varchar |  |  | SI | Demonstrate normal language functions |
| Q16 | numeric |  |  | SI | Ask for spontaneous recall |
| Q17 | varchar |  |  | SI | /8 |
| Q18 | varchar |  |  | SI | Give clues |
| Q19 | varchar |  |  | SI | Conclusion |
| Q20 | varchar |  |  | SI | Repetition |
| Q21 | varchar |  |  | SI | A - Sedation Phase |
| Q22 | varchar |  |  | SI | The expressive language score during counting |
| Q23 | varchar |  |  | SI | Memory registration |
| Q24 | varchar |  |  | SI | Token comprehension test score |
| Q25 | varchar |  |  | SI | Confrontation Naming |
| Q26 | varchar |  |  | SI | Repetition |
| Q27 | varchar |  |  | SI | Reading |
| Q28 | varchar |  |  | SI | B- Recovery and Recall Phase (10 min post-injectio... |
| Q29 | varchar |  |  | SI | If language impairment present, continue to test r... |
| Q30 | time |  |  | SI | Time of recovery |
| Q31 | varchar |  |  | SI | Demonstrate return of 5/5 power |
| Q32 | varchar |  |  | SI | Absence of pronator drift |
| Q33 | varchar |  |  | SI | Demonstrate normal language functions |
| Q34 | numeric |  |  | SI | Ask for spontaneous recall |
| Q35 | varchar |  |  | SI | /8 |
| Q36 | varchar |  |  | SI | Give clues |
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