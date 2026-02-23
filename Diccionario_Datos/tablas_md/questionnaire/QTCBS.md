# questionnaire.QTCBS

> The Ballard Score

**Schema:** questionnaire
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Ballard Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Performing the Assessment of Neuromuscular Maturit... |
| Q02 | varchar |  |  | SI | Posture |
| Q03 | varchar |  |  | SI | Square Window (Wrist) |
| Q04 | varchar |  |  | SI | Arm recoil |
| Q05 | varchar |  |  | SI | Popliteal angle |
| Q06 | varchar |  |  | SI | Scarf sign |
| Q07 | varchar |  |  | SI | Heel to ear |
| Q08 | varchar |  |  | SI | Performing the Assessment of Physical Activity |
| Q09 | varchar |  |  | SI | Skin |
| Q10 | varchar |  |  | SI | Lanugo |
| Q11 | varchar |  |  | SI | Plantar surface |
| Q12 | varchar |  |  | SI | Breast |
| Q13 | varchar |  |  | SI | Eye / ear |
| Q14 | varchar |  |  | SI | Genitals (Male) |
| Q15 | varchar |  |  | SI | Genitals (Female) |
| Q16 | varchar |  |  | SI | Total Neuromuscular Maturity Score |
| Q17 | varchar |  |  | SI | Total Physical Maturity Score |
| Q18 | varchar |  |  | SI | Score |
| Q19 | varchar |  |  | SI | Gest. Age by Maturity Rating (weeks) |
| Q20 | time |  |  | SI | Time of exam |
| Q21 | date |  |  | SI | Date of exam |
| Q22 | numeric |  |  | SI | Age at exam (hours) |
| Q23 | numeric |  |  | SI | Gestation by dates (weeks) |
| Q24 | time |  |  | SI | Birth date (hour) |
| Q25 | numeric |  |  | SI | APGAR (1 min) |
| Q26 | numeric |  |  | SI | APGAR (5 min) |
| Q27 | varchar |  |  | SI | Maturity Ring |
| Q28 | varchar |  |  | SI | Total Score |
| Q29 | varchar |  |  | SI | -10 |
| Q30 | varchar |  |  | SI | -5 |
| Q31 | varchar |  |  | SI | 0 |
| Q32 | varchar |  |  | SI | 5 |
| Q33 | varchar |  |  | SI | 10 |
| Q34 | varchar |  |  | SI | 15 |
| Q35 | varchar |  |  | SI | 20 |
| Q36 | varchar |  |  | SI | 25 |
| Q37 | varchar |  |  | SI | 30 |
| Q38 | varchar |  |  | SI | 35 |
| Q39 | varchar |  |  | SI | 40 |
| Q40 | varchar |  |  | SI | 45 |
| Q41 | varchar |  |  | SI | 50 |
| Q42 | varchar |  |  | SI | Weeks |
| Q43 | varchar |  |  | SI | 20 |
| Q44 | varchar |  |  | SI | 22 |
| Q45 | varchar |  |  | SI | 24 |
| Q46 | varchar |  |  | SI | 26 |
| Q47 | varchar |  |  | SI | 28 |
| Q48 | varchar |  |  | SI | 30 |
| Q49 | varchar |  |  | SI | 32 |
| Q50 | varchar |  |  | SI | 34 |
| Q51 | varchar |  |  | SI | 36 |
| Q52 | varchar |  |  | SI | 38 |
| Q53 | varchar |  |  | SI | 40 |
| Q54 | varchar |  |  | SI | 42 |
| Q55 | varchar |  |  | SI | 44 |
| Q56 | date |  |  | SI | Date |
| Q57 | time |  |  | SI | Time |
| Q58 | varchar |  |  | SI | Ballard JL, Khoury JC, Wedig KL, Wang L, Eilers-Wa... |
| Q59 | varchar |  |  | SI | A system for estimating newborn gestational age by... |
| Q60 | varchar |  |  | SI | Total Score |
| Q61 | varchar |  |  | SI | -10 |
| Q62 | varchar |  |  | SI | -5 |
| Q63 | varchar |  |  | SI | 0 |
| Q64 | varchar |  |  | SI | 5 |
| Q65 | varchar |  |  | SI | 10 |
| Q66 | varchar |  |  | SI | 15 |
| Q67 | varchar |  |  | SI | 20 |
| Q68 | varchar |  |  | SI | 25 |
| Q69 | varchar |  |  | SI | 30 |
| Q70 | varchar |  |  | SI | 35 |
| Q71 | varchar |  |  | SI | 40 |
| Q72 | varchar |  |  | SI | 45 |
| Q73 | varchar |  |  | SI | 50 |
| Q74 | varchar |  |  | SI | Weeks |
| Q75 | varchar |  |  | SI | 20 |
| Q76 | varchar |  |  | SI | 22 |
| Q77 | varchar |  |  | SI | 24 |
| Q78 | varchar |  |  | SI | 26 |
| Q79 | varchar |  |  | SI | 28 |
| Q80 | varchar |  |  | SI | 30 |
| Q81 | varchar |  |  | SI | 32 |
| Q82 | varchar |  |  | SI | 34 |
| Q83 | varchar |  |  | SI | 36 |
| Q84 | varchar |  |  | SI | 38 |
| Q85 | varchar |  |  | SI | 40 |
| Q86 | varchar |  |  | SI | 42 |
| Q87 | varchar |  |  | SI | 44 |
| Q88 | varchar |  |  | SI | Please refer to the maturity ring score table in t... |
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