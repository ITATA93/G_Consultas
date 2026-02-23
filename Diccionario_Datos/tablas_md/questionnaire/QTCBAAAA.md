# questionnaire.QTCBAAAA

> Burn Area Assessment (All Ages)

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Burn Area Assessment (All Ages)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Burn type |
| Q04 | varchar |  |  | SI | Other burn type |
| Q05 | varchar |  |  | SI | Thermal burns |
| Q06 | varchar |  |  | SI | Other thermal burns |
| Q07 | varchar |  |  | SI | 0 - 1 year |
| Q08 | varchar |  |  | SI | 9.5 |
| Q09 | varchar |  |  | SI | 2.75 |
| Q10 | varchar |  |  | SI | 2.5 |
| Q11 | varchar |  |  | SI | 1 - 4 years |
| Q12 | varchar |  |  | SI | 8.5 |
| Q13 | varchar |  |  | SI | 3.25 |
| Q14 | varchar |  |  | SI | 2.5 |
| Q15 | varchar |  |  | SI | 5 - 9 years |
| Q16 | varchar |  |  | SI | 6.5 |
| Q17 | varchar |  |  | SI | 4 |
| Q18 | varchar |  |  | SI | 2.75 |
| Q19 | varchar |  |  | SI | 10 - 14 years |
| Q20 | varchar |  |  | SI | 5.5 |
| Q21 | varchar |  |  | SI | 4.5 |
| Q22 | varchar |  |  | SI | 3 |
| Q23 | varchar |  |  | SI | 15 - 18 years |
| Q24 | varchar |  |  | SI | 4.5 |
| Q25 | varchar |  |  | SI | 4.5 |
| Q26 | varchar |  |  | SI | 3.25 |
| Q27 | varchar |  |  | SI | Adults |
| Q28 | varchar |  |  | SI | 3.5 |
| Q29 | varchar |  |  | SI | 4.75 |
| Q30 | varchar |  |  | SI | 3.5 |
| Q31 | varchar |  |  | SI | Area % for all ages |
| Q32 | varchar |  |  | SI | Neck = 1 |
| Q33 | varchar |  |  | SI | Anterior Trunk = 13 |
| Q34 | varchar |  |  | SI | One anterior upper arm = 2 |
| Q35 | varchar |  |  | SI | One anterior lower arm = 1.5 |
| Q36 | varchar |  |  | SI | One anterior hand = 1.5 |
| Q37 | varchar |  |  | SI | One posterior upper arm = 2 |
| Q38 | varchar |  |  | SI | One posterior lower arm = 1.5 |
| Q39 | varchar |  |  | SI | One posterior hand = 1.5 |
| Q40 | varchar |  |  | SI | Buttock = 2.5 |
| Q41 | varchar |  |  | SI | Genitalia = 1 |
| Q42 | varchar |  |  | SI | Adult body map |
| Q43 | varchar |  |  | SI | Pediatric body map |
| Q44 | varchar |  |  | SI | Legend for Annotation |
| Q45 | varchar |  |  | SI | Dummy 1 = Superficial Burn |
| Q46 | varchar |  |  | SI | Dummy 2 = Deep Burn |
| Q47 | varchar |  |  | SI | Please confirm that you have completed the Lund an... |
| Q48 | varchar |  |  | SI | Injury to Area % |
| Q49 | numeric |  |  | SI | Head (A) |
| Q50 | numeric |  |  | SI | Neck |
| Q51 | numeric |  |  | SI | Anterior Trunk |
| Q52 | numeric |  |  | SI | Posterior Trunk |
| Q53 | numeric |  |  | SI | Right Arm |
| Q54 | numeric |  |  | SI | Left Arm |
| Q55 | numeric |  |  | SI | Buttocks |
| Q56 | numeric |  |  | SI | Genitalia |
| Q57 | numeric |  |  | SI | Right Upper Leg (B) |
| Q58 | numeric |  |  | SI | Right Lower Leg (C) |
| Q59 | numeric |  |  | SI | Left Upper Leg (B) |
| Q60 | numeric |  |  | SI | Left Lower Leg (C) |
| Q61 | varchar |  |  | SI | Total Burn Surface Area |
| Q62 | varchar |  |  | SI | Notes |
| Q63 | varchar |  |  | SI | A = 1/2 of head |
| Q64 | varchar |  |  | SI | B = 1/2 of one thigh |
| Q65 | varchar |  |  | SI | C = 1/2 of one lower leg |
| Q66 | varchar |  |  | SI | Area % by age |
| Q67 | varchar |  |  | SI | Posterior Trunk = 13 |
| Q68 | varchar |  |  | SI | Adult schema |
| Q69 | varchar |  |  | SI | Child schema |
| Q70 | numeric |  |  | SI | Head (A) |
| Q71 | numeric |  |  | SI | Neck |
| Q72 | numeric |  |  | SI | Anterior Trunk |
| Q73 | numeric |  |  | SI | Posterior Trunk |
| Q74 | numeric |  |  | SI | Right Arm |
| Q75 | numeric |  |  | SI | Left Arm |
| Q76 | numeric |  |  | SI | Buttocks |
| Q77 | numeric |  |  | SI | Genitalia |
| Q78 | numeric |  |  | SI | Right Upper Leg (B) |
| Q79 | numeric |  |  | SI | Right Lower Leg (C) |
| Q80 | numeric |  |  | SI | Left Upper Leg (B) |
| Q81 | numeric |  |  | SI | Left Lower Leg (C) |
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