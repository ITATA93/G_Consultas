# questionnaire.QTCMOCA

> Montreal Cognitive Assessment (MoCA) Version 8.1

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Montreal Cognitive Assessment (MoCA) Version 8.1

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Does patient have more than a 12th grade education... |
| Q02 | bigint |  |  | SI | Diagram |
| Q02TxtOnly | bigint |  |  | SI | Diagram Plain Text Only |
| Q03 | varchar |  |  | SI | Ask patient to trace the diagram in order |
| Q04 | bigint |  |  | SI | Cube |
| Q04TxtOnly | bigint |  |  | SI | Cube Plain Text Only |
| Q05 | varchar |  |  | SI | Ask patient to copy cube |
| Q06 | varchar |  |  | SI | Ask patient to draw a clock (ten past eleven) |
| Q07 | bigint |  |  | SI | Animal |
| Q07TxtOnly | bigint |  |  | SI | Animal Plain Text Only |
| Q08 | varchar |  |  | SI | Ask patient to name the first animal |
| Q09 | varchar |  |  | SI | Ask patient to name the second animal |
| Q10 | varchar |  |  | SI | Ask patient to name the third animal |
| Q11 | varchar |  |  | SI | Read Face, Velvet, Church, Daisy, Red, and ask pat... |
| Q12 | varchar |  |  | SI | Read list of digits (2, 1, 8, 5, 4) at 1 digit/sec... |
| Q13 | varchar |  |  | SI | Read list of digits (7, 4, 2) at 1 digit/sec and a... |
| Q14 | varchar |  |  | SI | Read list of letters and ask patient to tap with t... |
| Q15 | varchar |  |  | SI | F B A C M N A A J K L B A F A K D E A A A J A M O ... |
| Q16 | varchar |  |  | SI | Ask patient to do five serial 7 subtractions start... |
| Q17 | varchar |  |  | SI | Read and ask patient to repeat: ''I only know that... |
| Q18 | varchar |  |  | SI | Ask patient to name maximum number of words in 1 m... |
| Q19 | varchar |  |  | SI | Ask patient similarity between train and bicycle (... |
| Q20 | varchar |  |  | SI | Ask patient similarity between watch and ruler (e.... |
| Q21 | varchar |  |  | SI | Ask patient to recall the words with no cue from t... |
| Q22 | varchar |  |  | SI | Ask patient the date, month, year, day, place, and... |
| Q23 | varchar |  |  | SI | Score |
| Q24 | varchar |  |  | SI | Classification |
| Q25 | varchar |  |  | SI | <=25 |
| Q26 | varchar |  |  | SI | MoCA Score <=25 points is 90% sensitive for mild c... |
| Q27 | varchar |  |  | SI | Although the average MoCA score for Alzheimer pati... |
| Q28 | varchar |  |  | SI | such that the cutoff score is the same for both; t... |
| Q29 | varchar |  |  | SI | >=26 |
| Q30 | varchar |  |  | SI | Normal |
| Q31 | varchar |  |  | SI | <=25: points is 90% sensitive for mild cognitive i... |
| Q32 | varchar |  |  | SI | The Montreal Cognitive Assessment (MoCA) is a cogn... |
| Q33 | varchar |  |  | SI | >=26: Normal |
| Q34 | varchar |  |  | SI | Read and ask patient to repeat: The cat always hid... |
| Q35 | date |  |  | SI | Date |
| Q36 | time |  |  | SI | Time |
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