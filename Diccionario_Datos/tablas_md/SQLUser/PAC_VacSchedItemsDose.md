# SQLUser.PAC_VacSchedItemsDose

**Schema:** SQLUser
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOSE_ParRef | varchar | PK |  | NO | PAC_VacSchedItems Parent Reference |
| DOSE_Childsub | double |  |  | NO | Childsub |
| DOSE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOSE_CreatedDate | date |  |  | SI | Created Date |
| DOSE_CreatedTime | time |  |  | SI | Created Time |
| DOSE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOSE_DateFrom | date |  |  | SI | DateFrom |
| DOSE_DateTo | date |  |  | SI | DateTo |
| DOSE_Dosage | varchar |  |  | SI | Dosage  |
| DOSE_LowerAge | double |  |  | SI | LowerAge |
| DOSE_LowerAgePeriod | varchar |  |  | SI | LowerAgePeriod |
| DOSE_Offset | double |  |  | SI | Offset |
| DOSE_OffsetType | varchar |  |  | SI | OffsetType |
| DOSE_Period | varchar |  |  | SI | Period |
| DOSE_RowId | varchar |  |  | NO | - |
| DOSE_UpdatedDate | date |  |  | SI | Updated Date |
| DOSE_UpdatedTime | time |  |  | SI | Updated Time |
| DOSE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DOSE_UpperAge | double |  |  | SI | UpperAge |
| DOSE_UpperAgePeriod | varchar |  |  | SI | UpperAgePeriod |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient's Age |
| Q04 | - |  |  | SI | Gestation at birth |
| Q05 | - |  |  | SI | Gestation at birth |
| Q06 | - |  |  | SI | weeks |
| Q07 | - |  |  | SI | Gestation at birth (days) |
| Q08 | - |  |  | SI | days |
| Q09 | - |  |  | SI | Definition: Time elapsed between the first day of ... |
| Q10 | - |  |  | SI | If pregnancy was achieved using assisted reproduct... |
| Q11 | - |  |  | SI | Postmenstrual age |
| Q12 | - |  |  | SI | Postmenstrual age (weeks) |
| Q13 | - |  |  | SI | weeks |
| Q14 | - |  |  | SI | Postmenstrual age (days) |
| Q15 | - |  |  | SI | days |
| Q16 | - |  |  | SI | Definition: Gestational age plus chronological age |
| Q17 | - |  |  | SI | Postnatal age |
| Q18 | - |  |  | SI | Postnatal age - year |
| Q19 | - |  |  | SI | year |
| Q20 | - |  |  | SI | Patient age (postnatal) - months |
| Q21 | - |  |  | SI | months |
| Q22 | - |  |  | SI | Patient age (postnatal) - days |
| Q23 | - |  |  | SI | days |
| Q24 | - |  |  | SI | Definition: Time lapsed since birth |
| Q25 | - |  |  | SI | Corrected age |
| Q26 | - |  |  | SI | Corrected age - year |
| Q27 | - |  |  | SI | year |
| Q28 | - |  |  | SI | Patient age (postnatal) - months |
| Q29 | - |  |  | SI | months |
| Q30 | - |  |  | SI | Patient age (postnatal) - days |
| Q31 | - |  |  | SI | days |
| Q32 | - |  |  | SI | Definition: Chronological / Postnatal age reduced ... |
| Q33 | - |  |  | SI | Maternal risk factors |
| Q34 | - |  |  | SI | Maternal risk factor types |
| Q35 | - |  |  | SI | Other maternal risk factors |
| Q36 | - |  |  | SI | Neonatal risk factors |
| Q37 | - |  |  | SI | Neonatal risk factor types |
| Q38 | - |  |  | SI | Other neonatal risk factors |
| Q39 | - |  |  | SI | Haemoglobin level, if applicable (g/dl)) |
| Q40 | - |  |  | SI | Assessment |
| Q41 | - |  |  | SI | Right eye |
| Q42 | - |  |  | SI | Left eye |
| Q43 | - |  |  | SI | Stage of retinopathy of prematurity (ROP) |
| Q44 | - |  |  | SI | Stage of retinopathy of prematurity (ROP) - Right ... |
| Q45 | - |  |  | SI | Stage of retinopathy of prematurity (ROP) - Left e... |
| Q46 | - |  |  | SI | Plus disease |
| Q47 | - |  |  | SI | Plus disease - Right eye |
| Q48 | - |  |  | SI | Plus disease - Left eye |
| Q49 | - |  |  | SI | Annotated image |
| Q50 | - |  |  | SI | Notes |
| Q51 | - |  |  | SI | Plan |
| Q52 | - |  |  | SI | Planned action - as instructed in guidelines below |
| Q53 | - |  |  | SI | Cup/Disc ratio |
| Q54 | - |  |  | SI | Right |
| Q55 | - |  |  | SI | Left |
| Q56 | - |  |  | SI | Review required in (weeks) as instructed in guidel... |
| Q57 | - |  |  | SI | Notes |
| Q58 | - |  |  | SI | Guidelines |
| Q59 | - |  |  | SI | Eligibility for screening |
| Q60 | - |  |  | SI | * Birthweight < 1500 grams or |
| Q61 | - |  |  | SI | * Gestation < 30 weeks or |
| Q62 | - |  |  | SI | * selected infants that are larger or mor mature a... |
| Q63 | - |  |  | SI | Frequency of examination |
| Q64 | - |  |  | SI | 1 week or less follow-up |
| Q65 | - |  |  | SI | * Stage 1 or 2 ROP : zone I |
| Q66 | - |  |  | SI | * Stage 3 ROP : zone II |
| Q67 | - |  |  | SI | 1 to 2 week follow-up |
| Q68 | - |  |  | SI | * Immature vascularization, zone I, no ROP |
| Q69 | - |  |  | SI | * Stage 2 ROP : zone II |
| Q70 | - |  |  | SI | * Regressing ROP : zone I |
| Q71 | - |  |  | SI | 2 week follow-up |
| Q72 | - |  |  | SI | Stage 1 ROP : zone II |
| Q73 | - |  |  | SI | Regressing ROP : zone II |
| Q74 | - |  |  | SI | 2 to 3 week follow-up |
| Q75 | - |  |  | SI | * Immature vascularization: zone II, o ROP |
| Q76 | - |  |  | SI | * Stage 1 or 2 ROP : zone III |
| Q77 | - |  |  | SI | Regressing ROP : zone III |
| Q78 | - |  |  | SI | Guidelines for observation & treatment (source: Ea... |
| Q79 | - |  |  | SI | Observation to watch progression |
| Q80 | - |  |  | SI | * Zone 1 Stage 1 or 2 ROP without Plus disease. |
| Q81 | - |  |  | SI | * Zone 2 Stage 3 ROP without Plus disease. |
| Q82 | - |  |  | SI | * Zone 3 Stage 3 ROP without Plus disease. |
| Q83 | - |  |  | SI | Treatment laser ablation therapy |
| Q84 | - |  |  | SI | *  Zone 1 Stage 1 or 2 ROP with Plus disease |
| Q85 | - |  |  | SI | * Zone 1 Stage 3 ROP without Plus disease |
| Q86 | - |  |  | SI | * Zone 2 Stage 2 or 3 ROP with Plus disease. |
| Q87 | - |  |  | SI | * Zone 3 Stage 3 ROP with Plus disease. |
| Q88 | - |  |  | SI | Provenance Details |
| Q89 | - |  |  | SI | Jones JG, MacKinnon B, Good WV, Hardy RJ, Dobson V... |
| Q90 | - |  |  | SI | The early treatment for ROP (ETROP) randomized tri... |
| Q91 | - |  |  | SI | Right eye |
| Q92 | - |  |  | SI | Right eye |
| Q93 | - |  |  | SI | Left eye |
| Q94 | - |  |  | SI | Left eye |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*