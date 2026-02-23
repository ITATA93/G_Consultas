# questionnaire.QTCNSRMD

> Roland-Morris Low Back Pain and Disability Questionnaire

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Roland-Morris Low Back Pain and Disability Questionnaire

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | I stay at home most of the time because of my back |
| Q02 | varchar |  |  | SI | I change position frequently to try to get my back... |
| Q03 | varchar |  |  | SI | I walk more slowly than usual because of my back |
| Q04 | varchar |  |  | SI | Because of my back, I am not doing any jobs that I... |
| Q05 | varchar |  |  | SI | Because of my back, I use a handrail to get upstai... |
| Q06 | varchar |  |  | SI | Because of my back, I lie down to rest more often |
| Q07 | varchar |  |  | SI | Because of my back, I have to hold on to something... |
| Q08 | varchar |  |  | SI | Because of my back, I try to get other people to d... |
| Q09 | varchar |  |  | SI | I get dressed more slowly than usual because of my... |
| Q10 | varchar |  |  | SI | I only stand up for short periods of time because ... |
| Q11 | varchar |  |  | SI | Because of my back, I try not to bend or kneel dow... |
| Q12 | varchar |  |  | SI | I find it difficult to get out of a chair because ... |
| Q13 | varchar |  |  | SI | My back is painful almost all of the time |
| Q14 | varchar |  |  | SI | I find it difficult to turn over in bed because of... |
| Q15 | varchar |  |  | SI | My appetite is not very good because of my back |
| Q16 | varchar |  |  | SI | I have trouble putting on my sock (or stockings) b... |
| Q17 | varchar |  |  | SI | I can only walk short distances because of my back... |
| Q18 | varchar |  |  | SI | I sleep less well because of my back |
| Q19 | varchar |  |  | SI | Because of my back pain, I get dressed with the he... |
| Q20 | varchar |  |  | SI | I sit down for most of the day because of my back |
| Q21 | varchar |  |  | SI | I avoid heavy jobs around the house because of my ... |
| Q22 | varchar |  |  | SI | Because of back pain, I am more irritable and bad ... |
| Q23 | varchar |  |  | SI | Because of my back, I go upstairs more slowly than... |
| Q24 | varchar |  |  | SI | I stay in bed most of the time because of my back |
| Q25 | varchar |  |  | SI | The Roland-Morris Disability Questionnaire (RMDQ) ... |
| Q26 | varchar |  |  | SI | Questionnaire consists of 24 questions which are r... |
| Q27 | varchar |  |  | SI | Scores under 4 and over 20 may not show significan... |
| Q28 | varchar |  |  | SI | 0 - 11: No disability  |
| Q29 | varchar |  |  | SI | 12 - 17: Moderate disability  |
| Q30 | varchar |  |  | SI | 18 - 24: Maximum disability  |
| Q31 | varchar |  |  | SI | 0 = No Disability & 24 = Maximum Disability |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q34 | varchar |  |  | SI | Score |
| Q35 | varchar |  |  | SI | Classification |
| Q36 | varchar |  |  | SI | 0 - 11 |
| Q37 | varchar |  |  | SI | No disability |
| Q38 | varchar |  |  | SI | 12 - 17 |
| Q39 | varchar |  |  | SI | Moderate disability |
| Q40 | varchar |  |  | SI | 18 - 24 |
| Q41 | varchar |  |  | SI | Maximum disability |
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