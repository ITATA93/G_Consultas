# questionnaire.QTCPODDMDT

> Podiatry Diabetes Outpatient MDT

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Podiatry Diabetes Outpatient MDT

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Informed consent?	 |
| Q02 | varchar |  |  | SI | Details of consent	 |
| Q03 | varchar |  |  | SI | Reason for referral	 |
| Q04 | varchar |  |  | SI | Patient complains of	 |
| Q05 | varchar |  |  | SI | Ulcer (right foot)	 |
| Q05b | varchar |  |  | SI | Ulcer (right foot) |
| Q06 | varchar |  |  | SI | Notes	 |
| Q07 | varchar |  |  | SI | Ulcer (left foot)	 |
| Q07b | varchar |  |  | SI | Ulcer (left foot) |
| Q08 | varchar |  |  | SI | Notes |
| Q09 | varchar |  |  | SI | Deformity (right foot)	 |
| Q09b | varchar |  |  | SI | Deformity (right foot) |
| Q10 | varchar |  |  | SI | Notes |
| Q11 | varchar |  |  | SI | Deformity (left foot)	 |
| Q11b | varchar |  |  | SI | Deformity (left foot) |
| Q12 | varchar |  |  | SI | Notes	 |
| Q13 | varchar |  |  | SI | Skin/Nail abnormalities (right foot)	 |
| Q13b | varchar |  |  | SI | Skin/Nail abnormalities (right foot) |
| Q14 | varchar |  |  | SI | Notes |
| Q15 | varchar |  |  | SI | Skin/Nail abnormalities (left foot)	 |
| Q15b | varchar |  |  | SI | Skin/Nail abnormalities (left foot) |
| Q16 | varchar |  |  | SI | Notes |
| Q17 | varchar |  |  | SI | Footwear assessed (right Foot)	 |
| Q17b | varchar |  |  | SI | Footwear assessed (right foot) |
| Q18 | varchar |  |  | SI | Notes |
| Q19 | varchar |  |  | SI | Footwear assessed (left foot)	 |
| Q19b | varchar |  |  | SI | Footwear assessed (left foot) |
| Q20 | varchar |  |  | SI | Notes |
| Q21 | varchar |  |  | SI | Charcot (right foot)	 |
| Q21b | varchar |  |  | SI | Charcot (right foot) |
| Q22 | varchar |  |  | SI | Notes |
| Q23 | varchar |  |  | SI | Charcot (left foot)	 |
| Q23b | varchar |  |  | SI | Charcot (left foot) |
| Q24 | varchar |  |  | SI | Notes |
| Q25 | varchar |  |  | SI | The number of sites 10mg monofilament was applied ... |
| Q26 | varchar |  |  | SI | The number of sites 10mg monofilament was applied ... |
| Q27 | varchar |  |  | SI | Dorsalis pedis palpable (right foot)	 |
| Q28 | varchar |  |  | SI | Dorsalis pedis palpable (left foot)	 |
| Q29 | varchar |  |  | SI | Dorsalis pedis doppler (right foot)	 |
| Q30 | varchar |  |  | SI | Dorsalis pedis doppler (left foot)	 |
| Q31 | varchar |  |  | SI | Notes |
| Q32 | varchar |  |  | SI | Posterior tibial palpable (right foot)	 |
| Q33 | varchar |  |  | SI | Posterior tibial palpable (left foot)	 |
| Q34 | varchar |  |  | SI | Posterior tibial doppler (right foot)	 |
| Q35 | varchar |  |  | SI | Posterior tibial doppler (left foot)	 |
| Q36 | varchar |  |  | SI | Notes |
| Q37 | date |  |  | SI | Date of 12 week classification	 |
| Q38 | date |  |  | SI | Date of 24 week classification	 |
| Q39 | varchar |  |  | SI | Site |
| Q40 | varchar |  |  | SI | Ischemia |
| Q41 | varchar |  |  | SI | Neuropathy	 |
| Q42 | varchar |  |  | SI | Bacterial Infection 	 |
| Q43 | varchar |  |  | SI | Area |
| Q44 | varchar |  |  | SI | Depth |
| Q45 | varchar |  |  | SI | Total score |
| Q46 | varchar |  |  | SI | Right / Left foot	 |
| Q47 | varchar |  |  | SI | Additional comments	 |
| Q48 | varchar |  |  | SI | Action |
| Q49 | varchar |  |  | SI | Plan |
| Q50 | varchar |  |  | SI | District nurse (Telephone number)	 |
| Q51 | varchar |  |  | SI | Notes |
| Q52 | varchar |  |  | SI | Treatment rooms	 |
| Q53 | varchar |  |  | SI | Notes |
| Q54 | varchar |  |  | SI | Community podiatry	 |
| Q55 | varchar |  |  | SI | Notes |
| Q56 | varchar |  |  | SI | Right / Left foot	 |
| Q67 | varchar |  |  | SI | Left Vibratip |
| Q68 | varchar |  |  | SI | Right Vibratip |
| Q69 | varchar |  |  | SI | Toe pressure right |
| Q70 | varchar |  |  | SI | Toe pressure left |
| Q71 | varchar |  |  | SI | Claudication right |
| Q72 | varchar |  |  | SI | Claudication left |
| Q73 | numeric |  |  | SI | 10g monofilament - 1A (right foot) |
| Q74 | numeric |  |  | SI | 10g monofilament - 1 (right foot) |
| Q75 | numeric |  |  | SI | 10g monofilament - 5 (right foot) |
| Q76 | numeric |  |  | SI | 10g monofilament - 1A (left foot) |
| Q77 | numeric |  |  | SI | 10g monofilament - 1 (left foot) |
| Q78 | numeric |  |  | SI | 10g monofilament - 5 (left foot) |
| Q79 | varchar |  |  | SI | Known neuropathy? |
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