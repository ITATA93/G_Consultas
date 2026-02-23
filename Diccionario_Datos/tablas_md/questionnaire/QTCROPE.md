# questionnaire.QTCROPE

> Retinopathy of Prematurity Evaluation

**Schema:** questionnaire
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Retinopathy of Prematurity Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient's Age |
| Q04 | varchar |  |  | SI | Gestation at birth |
| Q05 | varchar |  |  | SI | Gestation at birth |
| Q06 | varchar |  |  | SI | weeks |
| Q07 | varchar |  |  | SI | Gestation at birth (days) |
| Q08 | varchar |  |  | SI | days |
| Q09 | varchar |  |  | SI | Definition: Time elapsed between the first day of ... |
| Q10 | varchar |  |  | SI | If pregnancy was achieved using assisted reproduct... |
| Q11 | varchar |  |  | SI | Postmenstrual age |
| Q12 | numeric |  |  | SI | Postmenstrual age (weeks) |
| Q13 | varchar |  |  | SI | weeks |
| Q14 | numeric |  |  | SI | Postmenstrual age (days) |
| Q15 | varchar |  |  | SI | days |
| Q16 | varchar |  |  | SI | Definition: Gestational age plus chronological age... |
| Q17 | varchar |  |  | SI | Postnatal age |
| Q18 | numeric |  |  | SI | Postnatal age - year |
| Q19 | varchar |  |  | SI | year |
| Q20 | numeric |  |  | SI | Patient age (postnatal) - months |
| Q21 | varchar |  |  | SI | months |
| Q22 | numeric |  |  | SI | Patient age (postnatal) - days |
| Q23 | varchar |  |  | SI | days |
| Q24 | varchar |  |  | SI | Definition: Time lapsed since birth |
| Q25 | varchar |  |  | SI | Corrected age |
| Q26 | numeric |  |  | SI | Corrected age - year |
| Q27 | varchar |  |  | SI | year |
| Q28 | numeric |  |  | SI | Patient age (postnatal) - months |
| Q29 | varchar |  |  | SI | months |
| Q30 | numeric |  |  | SI | Patient age (postnatal) - days |
| Q31 | varchar |  |  | SI | days |
| Q32 | varchar |  |  | SI | Definition: Chronological / Postnatal age reduced ... |
| Q33 | varchar |  |  | SI | Maternal risk factors |
| Q34 | varchar |  |  | SI | Maternal risk factor types |
| Q35 | varchar |  |  | SI | Other maternal risk factors |
| Q36 | varchar |  |  | SI | Neonatal risk factors |
| Q37 | varchar |  |  | SI | Neonatal risk factor types |
| Q38 | varchar |  |  | SI | Other neonatal risk factors  |
| Q39 | numeric |  |  | SI | Haemoglobin level, if applicable (g/dl)) |
| Q40 | varchar |  |  | SI | Assessment |
| Q41 | varchar |  |  | SI | Right eye |
| Q42 | varchar |  |  | SI | Left eye |
| Q43 | varchar |  |  | SI | Stage of retinopathy of prematurity (ROP) |
| Q44 | varchar |  |  | SI | Stage of retinopathy of prematurity (ROP) - Right ... |
| Q45 | varchar |  |  | SI | Stage of retinopathy of prematurity (ROP) - Left e... |
| Q46 | varchar |  |  | SI | Plus disease |
| Q47 | varchar |  |  | SI | Plus disease - Right eye |
| Q48 | varchar |  |  | SI | Plus disease - Left eye |
| Q49 | varchar |  |  | SI | Annotated image |
| Q50 | varchar |  |  | SI | Notes |
| Q51 | varchar |  |  | SI | Plan |
| Q52 | varchar |  |  | SI | Planned action - as instructed in guidelines below |
| Q53 | varchar |  |  | SI | Cup/Disc ratio |
| Q54 | varchar |  |  | SI | Right |
| Q55 | varchar |  |  | SI | Left |
| Q56 | numeric |  |  | SI | Review required in (weeks) as instructed in guidel... |
| Q57 | varchar |  |  | SI | Notes |
| Q58 | varchar |  |  | SI | Guidelines |
| Q59 | varchar |  |  | SI | Eligibility for screening |
| Q60 | varchar |  |  | SI | * Birthweight < 1500 grams or |
| Q61 | varchar |  |  | SI | * Gestation < 30 weeks or |
| Q62 | varchar |  |  | SI | * selected infants that are larger or mor mature a... |
| Q63 | varchar |  |  | SI | Frequency of examination |
| Q64 | varchar |  |  | SI | 1 week or less follow-up |
| Q65 | varchar |  |  | SI | * Stage 1 or 2 ROP : zone I |
| Q66 | varchar |  |  | SI | * Stage 3 ROP : zone II |
| Q67 | varchar |  |  | SI | 1 to 2 week follow-up |
| Q68 | varchar |  |  | SI | * Immature vascularization, zone I, no ROP |
| Q69 | varchar |  |  | SI | * Stage 2 ROP : zone II |
| Q70 | varchar |  |  | SI | * Regressing ROP : zone I |
| Q71 | varchar |  |  | SI | 2 week follow-up |
| Q72 | varchar |  |  | SI | Stage 1 ROP : zone II |
| Q73 | varchar |  |  | SI | Regressing ROP : zone II |
| Q74 | varchar |  |  | SI | 2 to 3 week follow-up |
| Q75 | varchar |  |  | SI | * Immature vascularization: zone II, o ROP |
| Q76 | varchar |  |  | SI | * Stage 1 or 2 ROP : zone III |
| Q77 | varchar |  |  | SI | Regressing ROP : zone III |
| Q78 | varchar |  |  | SI | Guidelines for observation & treatment (source: Ea... |
| Q79 | varchar |  |  | SI | Observation to watch progression |
| Q80 | varchar |  |  | SI | * Zone 1 Stage 1 or 2 ROP without Plus disease. |
| Q81 | varchar |  |  | SI | * Zone 2 Stage 3 ROP without Plus disease. |
| Q82 | varchar |  |  | SI | * Zone 3 Stage 3 ROP without Plus disease. |
| Q83 | varchar |  |  | SI | Treatment laser ablation therapy |
| Q84 | varchar |  |  | SI | *  Zone 1 Stage 1 or 2 ROP with Plus disease |
| Q85 | varchar |  |  | SI | * Zone 1 Stage 3 ROP without Plus disease |
| Q86 | varchar |  |  | SI | * Zone 2 Stage 2 or 3 ROP with Plus disease. |
| Q87 | varchar |  |  | SI | * Zone 3 Stage 3 ROP with Plus disease. |
| Q88 | varchar |  |  | SI | Provenance Details |
| Q89 | varchar |  |  | SI | Jones JG, MacKinnon B, Good WV, Hardy RJ, Dobson V... |
| Q90 | varchar |  |  | SI | The early treatment for ROP (ETROP) randomized tri... |
| Q91 | varchar |  |  | SI | Right eye |
| Q92 | varchar |  |  | SI | Right eye |
| Q93 | varchar |  |  | SI | Left eye |
| Q94 | varchar |  |  | SI | Left eye |
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