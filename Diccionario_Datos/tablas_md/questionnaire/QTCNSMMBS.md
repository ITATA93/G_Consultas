# questionnaire.QTCNSMMBS

> Modified Massey Bedside Swallowing Screen

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified Massey Bedside Swallowing Screen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | To be completed prior to oral intake |
| Q02 | varchar |  |  | SI | Date of admission: |
| Q03 | date |  |  | SI | Date of screen: |
| Q04 | time |  |  | SI | Time of screen |
| Q05 | varchar |  |  | SI | If the answer is Yes to the questions 2-7, obtain ... |
| Q06 | varchar |  |  | SI | 1. Patient is alert (can follow commands) |
| Q07 | varchar |  |  | SI | 2. Does patient exhibit slurred or garbled speech? |
| Q08 | varchar |  |  | SI | 3. Does patient exhibit trouble speaking or unders... |
| Q09 | varchar |  |  | SI | 4. Does patient exhibit drooling? |
| Q10 | varchar |  |  | SI | 5. Does patient have a wet-sounding voice? |
| Q11 | varchar |  |  | SI | 6. Give patient a teaspoon of water – Do any of th... |
| Q12 | varchar |  |  | SI | 7. Give patient 60 mL of water (only if teaspoon o... |
| Q13 | varchar |  |  | SI | Make patient NPO (Nil Per Oral) and obtain order f... |
| Q14 | varchar |  |  | SI | Comments |
| Q15 | varchar |  |  | SI | Comment 2 |
| Q16 | varchar |  |  | SI | Comment 3 |
| Q17 | varchar |  |  | SI | Comment 4 |
| Q18 | varchar |  |  | SI | Comment 5 |
| Q19 | varchar |  |  | SI | Comment 6 |
| Q20 | varchar |  |  | SI | Comment 7 |
| Q21 | varchar |  |  | SI | If the answers are all NO to Questions 2-7, consid... |
| Q22 | varchar |  |  | SI | If only Questions 2, 3, and/or 4 is checked as YES... |
| Q23 | varchar |  |  | SI | Stop, make patient NPO (Nil Per Oral) and obtain o... |
| Q24 | varchar |  |  | SI | Stop, make patient NPO (Nil Per Oral) and obtain o... |
| Q25 | varchar |  |  | SI | Modified Massey Bedside Swallowing Screen is used ... |
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