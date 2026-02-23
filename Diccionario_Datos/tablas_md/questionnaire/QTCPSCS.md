# questionnaire.QTCPSCS

> Pre Surgical Cognition Screen

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre Surgical Cognition Screen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Impaired cognition increases safety risks |
| Q04 | varchar |  |  | SI | Delirium is an indicator of serious underlying ill... |
| Q05 | varchar |  |  | SI | Commence for patient ≥16 years presenting to pre-a... |
| Q06 | varchar |  |  | SI | Delirium risks |
| Q07 | varchar |  |  | SI | Risks identified |
| Q08 | varchar |  |  | SI | Cognition Screen for All At Risk |
| Q09 | varchar |  |  | SI | Patient to wear glasses and hearing aid if needed |
| Q10 | varchar |  |  | SI | English first language |
| Q11 | varchar |  |  | SI | Preferred language |
| Q12 | varchar |  |  | SI | Explain reasons for questions - routine to check m... |
| Q13 | varchar |  |  | SI | I am going to show you 3 pictures that I want you ... |
| Q14 | varchar |  |  | SI | Verbal naming by clinician if person is visually i... |
| Q15 | varchar |  |  | SI | I'm going to give you some instructions, and I wan... |
| Q16 | varchar |  |  | SI | What time of the year is it now? Answers specific ... |
| Q17 | varchar |  |  | SI | What is the name of this place? (e.g. name of hosp... |
| Q18 | varchar |  |  | SI | What were the names of the three pictures I asked ... |
| Q19 | varchar |  |  | SI | Outcome of assessment |
| Q20 | varchar |  |  | SI | Specify reason unable to complete |
| Q21 | varchar |  |  | SI | Response Actions to Identified Cognition Risks |
| Q22 | varchar |  |  | SI | Advise family / Carer it would be helpful to have ... |
| Q23 | varchar |  |  | SI | Handover risk - observe for change |
| Q24 | varchar |  |  | SI | Dummy 1 |
| Q25 | varchar |  |  | SI | Inform anaesthetist of abnormal screen result for ... |
| Q26 | varchar |  |  | SI | Inform the person and family / Carer of increased ... |
| Q27 | varchar |  |  | SI | Dummy 2 |
| Q28 | varchar |  |  | SI | Interpreter used |
| Q29 | varchar |  |  | SI | Interpreter name |
| Q30 | varchar |  |  | SI | Interpreter contact |
| Q31 | varchar |  |  | SI | Provide family / Carer with delirium education mat... |
| Q32 | varchar |  |  | SI | Cognition screen is normal no further action is re... |
| Q33 | varchar |  |  | SI | Memory test |
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