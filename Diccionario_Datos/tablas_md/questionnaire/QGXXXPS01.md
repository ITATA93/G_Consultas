# questionnaire.QGXXXPS01

> Psychological General Well-Being Index

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Psychological General Well-Being Index

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | How have you been feeling in general during the pa... |
| Q02 | varchar |  |  | SI | How often were you bothered by an illness, bodily ... |
| Q03 | varchar |  |  | SI | Did you feel depressed during the past month? |
| Q04 | varchar |  |  | SI | Have you been in firm control of your behaviour, t... |
| Q05 | varchar |  |  | SI | Have you been bothered by nervousness during the p... |
| Q06 | varchar |  |  | SI | How much energy, pep, or vitality did you have dur... |
| Q07 | varchar |  |  | SI | I felt downhearted and blue during the past month |
| Q08 | varchar |  |  | SI | Were you generally tense or did you feel any tensi... |
| Q09 | varchar |  |  | SI | How happy, satisfied, or pleased have you been wit... |
| Q10 | varchar |  |  | SI | Did you feel healthy enough to carry out the thing... |
| Q11 | varchar |  |  | SI | Have you felt so sad, discouraged, or hopeless or ... |
| Q12 | varchar |  |  | SI | I woke up feeling fresh and rested during the past... |
| Q13 | varchar |  |  | SI | Have you been concerned, worried or had any fears ... |
| Q14 | varchar |  |  | SI | Have you had any reason to wonder if you were losi... |
| Q15 | varchar |  |  | SI | My daily life was full of things that were interes... |
| Q16 | varchar |  |  | SI | Did you feel active, vigorous, or dull sluggish du... |
| Q17 | varchar |  |  | SI | Have you been anxious, worried, or upset during th... |
| Q18 | varchar |  |  | SI | I was emotionally stable and sure of myself during... |
| Q19 | varchar |  |  | SI | Did you feel relaxed, at ease or high strung, tigh... |
| Q20 | varchar |  |  | SI | I felt cheerful, lighthearted during the past mont... |
| Q21 | varchar |  |  | SI | I felt tired, used up or exhausted during the past... |
| Q22 | varchar |  |  | SI | Have you been under or felt you were under any str... |
| Q23 | varchar |  |  | SI | The Psychological General Well-Being Index is a se... |
| Q24 | varchar |  |  | SI | Each answer is scored on a scale value of 0 to 5, ... |
| Q25 | varchar |  |  | SI | The 22 item instrument includes six dimensions: An... |
| Q26 | varchar |  |  | SI | 0: poor quality of life |
| Q27 | varchar |  |  | SI | 110: good quality of life |
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