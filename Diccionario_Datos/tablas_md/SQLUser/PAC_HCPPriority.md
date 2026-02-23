# SQLUser.PAC_HCPPriority

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HCPP_RowId | bigint | PK |  | NO | - |
| HCPP_Code | varchar |  |  | NO | Code |
| HCPP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HCPP_CreatedDate | date |  |  | SI | Created Date |
| HCPP_CreatedTime | time |  |  | SI | Created Time |
| HCPP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HCPP_Desc | varchar |  |  | NO | Description |
| HCPP_Owner | varchar |  |  | SI | Owner |
| HCPP_UpdatedDate | date |  |  | SI | Updated Date |
| HCPP_UpdatedTime | time |  |  | SI | Updated Time |
| HCPP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Does patient have more than a 12th grade education... |
| Q02 | - |  |  | SI | Diagram |
| Q02TxtOnly | - |  |  | SI | Diagram Plain Text Only |
| Q03 | - |  |  | SI | Ask patient to trace the diagram in order |
| Q04 | - |  |  | SI | Cube |
| Q04TxtOnly | - |  |  | SI | Cube Plain Text Only |
| Q05 | - |  |  | SI | Ask patient to copy cube |
| Q06 | - |  |  | SI | Ask patient to draw a clock (ten past eleven) |
| Q07 | - |  |  | SI | Animal |
| Q07TxtOnly | - |  |  | SI | Animal Plain Text Only |
| Q08 | - |  |  | SI | Ask patient to name the first animal |
| Q09 | - |  |  | SI | Ask patient to name the second animal |
| Q10 | - |  |  | SI | Ask patient to name the third animal |
| Q11 | - |  |  | SI | Read Face, Velvet, Church, Daisy, Red, and ask pat... |
| Q12 | - |  |  | SI | Read list of digits (2, 1, 8, 5, 4) at 1 digit/sec... |
| Q13 | - |  |  | SI | Read list of digits (7, 4, 2) at 1 digit/sec and a... |
| Q14 | - |  |  | SI | Read list of letters and ask patient to tap with t... |
| Q15 | - |  |  | SI | F B A C M N A A J K L B A F A K D E A A A J A M O ... |
| Q16 | - |  |  | SI | Ask patient to do five serial 7 subtractions start... |
| Q17 | - |  |  | SI | Read and ask patient to repeat: ''I only know that... |
| Q18 | - |  |  | SI | Ask patient to name maximum number of words in 1 m... |
| Q19 | - |  |  | SI | Ask patient similarity between train and bicycle (... |
| Q20 | - |  |  | SI | Ask patient similarity between watch and ruler (e.... |
| Q21 | - |  |  | SI | Ask patient to recall the words with no cue from t... |
| Q22 | - |  |  | SI | Ask patient the date, month, year, day, place, and... |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | Classification |
| Q25 | - |  |  | SI | <=25 |
| Q26 | - |  |  | SI | MoCA Score <=25 points is 90% sensitive for mild c... |
| Q27 | - |  |  | SI | Although the average MoCA score for Alzheimer pati... |
| Q28 | - |  |  | SI | such that the cutoff score is the same for both |
| Q29 | - |  |  | SI | >=26 |
| Q30 | - |  |  | SI | Normal |
| Q31 | - |  |  | SI | <=25: points is 90% sensitive for mild cognitive i... |
| Q32 | - |  |  | SI | The Montreal Cognitive Assessment (MoCA) is a cogn... |
| Q33 | - |  |  | SI | >=26: Normal |
| Q34 | - |  |  | SI | Read and ask patient to repeat: The cat always hid... |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*