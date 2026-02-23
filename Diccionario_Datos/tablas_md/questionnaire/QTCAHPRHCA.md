# questionnaire.QTCAHPRHCA

> Physiotherapy Casting Form

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapy Casting Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Physiotherapy - Casting Documentation |
| Q02 | varchar |  |  | SI | Cast Number |
| Q03 | varchar |  |  | SI | AIM/S OF CASTING |
| Q06 | varchar |  |  | SI | Staff / Family / Carer at appointment |
| Q09 | varchar |  |  | SI | PRECAUTIONS |
| Q10 | varchar |  |  | SI | Please circle |
| Q11 | varchar |  |  | SI | PLAN IF REQUIRED (e.g. Orthotics / wheelchair / ai... |
| Q12 | varchar |  |  | SI | STANDING, GAIT & FUNCTIONAL ASSESSMENT |
| Q13 | varchar |  |  | SI | RANGE OF MOVEMENT PRE CAST |
| Q14 | varchar |  |  | SI | Right |
| Q15 | varchar |  |  | SI | R1 |
| Q16 | varchar |  |  | SI | R2 |
| Q17 | varchar |  |  | SI | Left |
| Q18 | varchar |  |  | SI | R1 |
| Q19 | varchar |  |  | SI | R2 |
| Q20 | varchar |  |  | SI | Knee extension |
| Q21 | varchar |  |  | SI | Knee extension Right R1 |
| Q22 | varchar |  |  | SI | Knee extension Right R2 |
| Q23 | varchar |  |  | SI | Knee extension Left R1 |
| Q24 | varchar |  |  | SI | Knee extension Left R2 |
| Q25 | varchar |  |  | SI | Ankle DF (Knee 90°) |
| Q26 | varchar |  |  | SI | Ankle DF (Knee 90°) Right R1 |
| Q27 | varchar |  |  | SI | Ankle DF (Knee 90°) Right R2 |
| Q28 | varchar |  |  | SI | Ankle DF (Knee 90°) Left R1 |
| Q29 | varchar |  |  | SI | Ankle DF (Knee 90°) Left R2 |
| Q30 | varchar |  |  | SI | Ankle DF (Knee 0°) Right R1 |
| Q31 | varchar |  |  | SI | Ankle DF (Knee 0°) Right R2 |
| Q32 | varchar |  |  | SI | Ankle DF (Knee 0°) Left R1 |
| Q33 | varchar |  |  | SI | Ankle DF (Knee 0°) Left R2 |
| Q34 | varchar |  |  | SI | Other Measures |
| Q35 | varchar |  |  | SI | Strength Measuring Chair (SMC) |
| Q44 | varchar |  |  | SI | CAST APPLICATION |
| Q45 | varchar |  |  | SI | Under layer |
| Q46 | varchar |  |  | SI | Wrapping materials |
| Q47 | varchar |  |  | SI | Size |
| Q48 | bit |  |  | SI | Backslab |
| Q49 | varchar |  |  | SI | Backslab Description |
| Q50 | varchar |  |  | SI | POST CASTING REVIEW |
| Q51 | bit |  |  | SI | POP heel wedge |
| Q52 | varchar |  |  | SI | PLAN FOR CAST REMOVAL |
| Q53 | date |  |  | SI | Date |
| Q54 | varchar |  |  | SI | Plan Detail |
| Q55 | varchar |  |  | SI | Additional comments (e.g. AFOs/ Splints) |
| Q56 | varchar |  |  | SI | Review Plan |
| Q57 | varchar |  |  | SI | Ankle DF (Knee 0°) |
| Q58 | varchar |  |  | SI | Type of information provided to patient / parents |
| Q59 | varchar |  |  | SI | Comment |
| Q60 | date |  |  | SI | Date |
| Q61 | time |  |  | SI | Time |
| Q63 | varchar |  |  | SI | Knee extension |
| Q64 | varchar |  |  | SI | Ankle DF (Knee 90°) |
| Q65 | varchar |  |  | SI | Ankle DF (Knee 0°) |
| Q66 | varchar |  |  | SI | R1 |
| Q67 | varchar |  |  | SI | R1 |
| Q68 | varchar |  |  | SI | R1 |
| Q69 | varchar |  |  | SI | R1 |
| Q70 | varchar |  |  | SI | R1 |
| Q71 | varchar |  |  | SI | R1 |
| Q72 | varchar |  |  | SI | R2 |
| Q73 | varchar |  |  | SI | R2 |
| Q74 | varchar |  |  | SI | R2 |
| Q75 | varchar |  |  | SI | R2 |
| Q76 | varchar |  |  | SI | R2 |
| Q77 | varchar |  |  | SI | R2 |
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