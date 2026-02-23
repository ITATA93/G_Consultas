# questionnaire.QTCCA

> Concussion Assessment

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Concussion Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Current Sport(s) - Type |
| Q02 | varchar |  |  | SI | Current Sport - Level of participation |
| Q03 | numeric |  |  | SI | Years of experience at this level |
| Q04 | numeric |  |  | SI | Years of education completed |
| Q05 | varchar |  |  | SI | Repeated any school years |
| Q06 | varchar |  |  | SI | School History (tick all that apply) |
| Q07 | varchar |  |  | SI | Sports and school history comments |
| Q08 | varchar |  |  | SI | Impact Testing History |
| Q09 | date |  |  | SI | Baseline testing Date |
| Q10 | varchar |  |  | SI | Baseline testing place |
| Q11 | date |  |  | SI | Post Injury testing Date |
| Q12 | varchar |  |  | SI | Post Injury testing place |
| Q13 | varchar |  |  | SI | Memory Questions |
| Q14 | varchar |  |  | SI | Remember things that people just told you |
| Q15 | varchar |  |  | SI | Remember things that happened in the past |
| Q16 | varchar |  |  | SI | Remember to do things (keep appointments / take me... |
| Q17 | varchar |  |  | SI | Remember the day of the week	 |
| Q18 | varchar |  |  | SI | Concentrate |
| Q19 | varchar |  |  | SI | Think quickly |
| Q20 | varchar |  |  | SI | Solve everyday problems |
| Q21 | varchar |  |  | SI | Say the name of someone in front of you	 |
| Q22 | varchar |  |  | SI | Understand what is being said in a conversation wi... |
| Q23 | varchar |  |  | SI | Reply to questions	 |
| Q24 | varchar |  |  | SI | Correctly name objects	 |
| Q25 | varchar |  |  | SI | Participate in a conversation with a group of peop... |
| Q26 | varchar |  |  | SI | Call a person on the telephone, including selectin... |
| Q27 | varchar |  |  | SI |  Have you receive any treatment for symptoms since... |
| Q28 | varchar |  |  | SI | Treatment details	 |
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