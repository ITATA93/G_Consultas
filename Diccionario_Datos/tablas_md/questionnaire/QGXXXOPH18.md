# questionnaire.QGXXXOPH18

> Motility and Alignment

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Motility and Alignment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nystagmus |
| Q02 | varchar |  |  | SI | AHP |
| Q03 | varchar |  |  | SI | MOD1 |
| Q04 | varchar |  |  | SI | MOD2 |
| Q05 | varchar |  |  | SI | MOD3 |
| Q06 | varchar |  |  | SI | MOD4 |
| Q07 | varchar |  |  | SI | MOD5 |
| Q08 | varchar |  |  | SI | MOD6 |
| Q09 | varchar |  |  | SI | MOD6 |
| Q10 | varchar |  |  | SI | MOD7 |
| Q11 | varchar |  |  | SI | MOD8 |
| Q12 | varchar |  |  | SI | MOS1 |
| Q13 | varchar |  |  | SI | MOS2 |
| Q14 | varchar |  |  | SI | MOS3 |
| Q15 | varchar |  |  | SI | MOS4 |
| Q16 | varchar |  |  | SI | MOS5 |
| Q17 | varchar |  |  | SI | MOS5 |
| Q18 | varchar |  |  | SI | MOS7 |
| Q19 | varchar |  |  | SI | MOS8 |
| Q20 | varchar |  |  | SI | Notes |
| Q21 | varchar |  |  | SI | Simultaneous Cover Test |
| Q22 | varchar |  |  | SI | Distance |
| Q23 | varchar |  |  | SI | Near |
| Q24 | varchar |  |  | SI | Present Cover Test |
| Q25 | varchar |  |  | SI | Position |
| Q26 | varchar |  |  | SI | note |
| Q27 | varchar |  |  | SI | Distance |
| Q28 | varchar |  |  | SI | Near |
| Q29 | varchar |  |  | SI | Krimsky |
| Q30 | varchar |  |  | SI | Distance  |
| Q31 | varchar |  |  | SI | Near |
| Q32 | varchar |  |  | SI | Without correction |
| Q33 | varchar |  |  | SI | Sc2 |
| Q34 | varchar |  |  | SI | With correction / glasses |
| Q35 | varchar |  |  | SI | CC2 |
| Q36 | varchar |  |  | SI | Hirschberg's |
| Q37 | varchar |  |  | SI | Without correction |
| Q38 | varchar |  |  | SI | SC2 |
| Q39 | varchar |  |  | SI | With correction / glasses |
| Q40 | varchar |  |  | SI | CC2 |
| Q41 | varchar |  |  | SI | Stereoacuity |
| Q42 | varchar |  |  | SI | Worth 4-Dot Test |
| Q43 | varchar |  |  | SI | Distance |
| Q44 | varchar |  |  | SI | Near |
| Q45 | varchar |  |  | SI | Nine position of Gaze |
| Q46 | varchar |  |  | SI | PS1 |
| Q47 | varchar |  |  | SI | PS2 |
| Q48 | varchar |  |  | SI | PS3 |
| Q49 | varchar |  |  | SI | PS4 |
| Q50 | varchar |  |  | SI | PS5 |
| Q51 | varchar |  |  | SI | PS6 |
| Q52 | varchar |  |  | SI | PS7 |
| Q53 | varchar |  |  | SI | PS8 |
| Q54 | varchar |  |  | SI | PS9 |
| Q55 | varchar |  |  | SI | PD1 |
| Q56 | varchar |  |  | SI | PD2 |
| Q57 | varchar |  |  | SI | PD3 |
| Q58 | varchar |  |  | SI | PD4 |
| Q59 | varchar |  |  | SI | PD5 |
| Q60 | varchar |  |  | SI | PD6 |
| Q61 | varchar |  |  | SI | PD7 |
| Q62 | varchar |  |  | SI | PD8 |
| Q63 | varchar |  |  | SI | PD9 |
| Q64 | varchar |  |  | SI | Notes |
| Q65 | varchar |  |  | SI | Notes |
| Q66 | varchar |  |  | SI | Type |
| Q67 | varchar |  |  | SI | Distance |
| Q68 | varchar |  |  | SI | Near |
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