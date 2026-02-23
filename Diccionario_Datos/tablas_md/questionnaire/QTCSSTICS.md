# questionnaire.QTCSSTICS

> Subjective Scale to Investigate Cognition in Schizophrenia

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Subjective Scale to Investigate Cognition in Schizophrenia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Have you noticed any difficulty remembering things... |
| Q04 | varchar |  |  | SI | Do you have difficulty remembering information tha... |
| Q05 | varchar |  |  | SI | Do you have difficulty memorizing things, such as ... |
| Q06 | varchar |  |  | SI | Do you have difficulty remembering the names of yo... |
| Q07 | varchar |  |  | SI | Do you ever forget things, such as a date with a f... |
| Q08 | varchar |  |  | SI | Do you forget to take your medication? |
| Q09 | varchar |  |  | SI | Do you have difficulty remembering information tha... |
| Q10 | varchar |  |  | SI | Do you have difficulty doing household chores or r... |
| Q11 | varchar |  |  | SI | Do you have difficulty remembering how to get to t... |
| Q12 | varchar |  |  | SI | Do you have difficulty remembering the names of we... |
| Q13 | varchar |  |  | SI | Do you have difficulty remembering national capita... |
| Q14 | varchar |  |  | SI | Are you absent - minded or up in the clouds? For e... |
| Q15 | varchar |  |  | SI | Do you have difficulty being on the alert or react... |
| Q16 | varchar |  |  | SI | Do you have difficulty making out what’s important... |
| Q17 | varchar |  |  | SI | Are you unable to do two things at once? For examp... |
| Q18 | varchar |  |  | SI | Do you have trouble focusing your attention on the... |
| Q19 | varchar |  |  | SI | Do you have difficulty planning out your activitie... |
| Q20 | varchar |  |  | SI | Do you have difficulty coordinating your movements... |
| Q21 | varchar |  |  | SI | Do you have difficulty changing your movements, de... |
| Q22 | varchar |  |  | SI | Do you have difficulty finding your words, forming... |
| Q23 | varchar |  |  | SI | Do you have difficulty getting dressed or eating? ... |
| Q24 | varchar |  |  | SI | For example, the name of your medication or your n... |
| Q25 | varchar |  |  | SI | preparing meals, doing housework, doing laundry, u... |
| Q26 | varchar |  |  | SI | Score |
| Q27 | varchar |  |  | SI | Classification |
| Q28 | varchar |  |  | SI | 0 - 84 |
| Q29 | varchar |  |  | SI | 0 - 84: Higher the score, higher could be the cogn... |
| Q30 | varchar |  |  | SI | Subjective Scale to Investigate Cognition in Schiz... |
| Q31 | varchar |  |  | SI | Higher the score, higher could be the cognitive im... |
| Q32 | varchar |  |  | SI | The aim of the study is the validation of the Subj... |
| Q33 | varchar |  |  | SI | 0 - 84: Higher the score, higher could be the cogn... |
| Q34 | varchar |  |  | SI | Higher the score, higher could be the cognitive im... |
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