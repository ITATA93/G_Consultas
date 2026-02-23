# questionnaire.QGXXXMANTP

> Antenatal tests - planning

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal tests - planning

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Booking bloods and MSU done |
| Q02 | date |  |  | SI | Spina Bifida screening due |
| Q03 | date |  |  | SI | Spina Bifida screening done |
| Q04 | date |  |  | SI | Down's syndrome screening due |
| Q05 | date |  |  | SI | Down's syndrome screening done |
| Q06 | date |  |  | SI | Edward's syndrome screening due |
| Q07 | date |  |  | SI | Edward's syndrome screening done |
| Q08 | varchar |  |  | SI | Chlamydia screening required |
| Q08ObsDR | varchar |  | FK | SI | Chlamydia screening required DR |
| Q09 | date |  |  | SI | Chlamydia screening done |
| Q10 | varchar |  |  | SI | Repeat blood group and Antibody check required |
| Q10ObsDR | varchar |  | FK | SI | Repeat blood group and Antibody check required DR |
| Q11 | date |  |  | SI | Repeat blood group and Antibody check due |
| Q12 | date |  |  | SI | Repeat blood group and Antibody check done |
| Q13 | varchar |  |  | SI | Repeat FBC required |
| Q13ObsDR | varchar |  | FK | SI | Repeat FBC required DR |
| Q14 | date |  |  | SI | Repeat FBC due |
| Q15 | date |  |  | SI | Repeat FBC done |
| Q16 | varchar |  |  | SI | Repeat random blood glucose required |
| Q16ObsDR | varchar |  | FK | SI | Repeat random blood glucose required DR |
| Q17 | date |  |  | SI | Repeat random blood glucose due |
| Q18 | date |  |  | SI | Repeat random blood glucose done |
| Q19 | varchar |  |  | SI | Haemoglobinopathy screening required |
| Q19ObsDR | varchar |  | FK | SI | Haemoglobinopathy screening required DR |
| Q20 | varchar |  |  | SI | Prophylactic Anti D required and discussed |
| Q20ObsDR | varchar |  | FK | SI | Prophylactic Anti D required and discussed DR |
| Q21 | date |  |  | SI | Prophylactic Anti D given |
| Q22 | numeric |  |  | SI | Prophylactic Anti D given - gestation |
| Q23 | numeric |  |  | SI | Prophylactic Anti D batch number |
| Q24 | numeric |  |  | SI | Anti D dose |
| Q25 | varchar |  |  | SI | Which tests were declined and for what reason |
| Q26 | varchar |  |  | SI | Test results - action |
| Q27 | varchar |  |  | SI | Midwife countersigning |
| Q28 | date |  |  | SI | Haemoglobinopathy screening done |
| Q29 | date |  |  | SI | Booking bloods and MSU due |
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