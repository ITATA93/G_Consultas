# questionnaire.QTCDBMH

> Dizziness and Balance Medical History

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dizziness and Balance Medical History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Characteristics of dizziness |
| Q02 | varchar |  |  | SI | Note |
| Q03 | varchar |  |  | SI | Tendency to fall |
| Q04 | varchar |  |  | SI | Loss of balance when walking and veering to which ... |
| Q05 | varchar |  |  | SI | Onset & Course |
| Q06 | varchar |  |  | SI | Type of vertigo |
| Q07 | varchar |  |  | SI | Note |
| Q08 | varchar |  |  | SI | Dizziness between episodes |
| Q09 | varchar |  |  | SI | Can anticipate the attack |
| Q10 | varchar |  |  | SI | First dizzy episode |
| Q11 | varchar |  |  | SI | Most recent episode |
| Q12 | varchar |  |  | SI | Duration of each episode (sec,min,hr,day) |
| Q13 | varchar |  |  | SI | Frequency of episodes |
| Q14 | varchar |  |  | SI | Occupation |
| Q15 | varchar |  |  | SI | Exacerbating Factors |
| Q15A | varchar |  |  | SI | Alleviation Factors |
| Q16 | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Relation between dizziness and stress or anxiety? |
| Q18 | varchar |  |  | SI | What causes an episode? |
| Q19 | varchar |  |  | SI | What makes the dizziness better? |
| Q20 | varchar |  |  | SI | Associated symptoms |
| Q21 | varchar |  |  | SI | Past / present medical history |
| Q22 | varchar |  |  | SI | Note |
| Q23 | varchar |  |  | SI | Note |
| Q24 | varchar |  |  | SI | Previous treatment for dizziness |
| Q25 | varchar |  |  | SI | Characteristics of Dizziness |
| Q26 | varchar |  |  | SI | Onset & Course |
| Q27 | varchar |  |  | SI | Personal & Social |
| Q28 | varchar |  |  | SI | Exacerbating & Remitting Factors |
| Q29 | varchar |  |  | SI | Associated Symptoms |
| Q30 | varchar |  |  | SI | Present / Past Medical History |
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