# questionnaire.QTCRJCARF

> Revised Jones Criteria - Acute Rheumatic Fever (ARF) (Gewitz)

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Revised Jones Criteria - Acute Rheumatic Fever (ARF) (Gewitz)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | See Guidelines section for additional information ... |
| Q04 | varchar |  |  | SI | Is there evidence of preceding group A streptococc... |
| Q05 | varchar |  |  | SI | No evidence of preceding GAS infection; required c... |
| Q06 | varchar |  |  | SI | Please select the appropriate category for this pa... |
| Q07 | varchar |  |  | SI | Major criteria (low risk - no history) |
| Q08 | varchar |  |  | SI | Major criteria (low risk -  history) |
| Q09 | varchar |  |  | SI | Major criteria (moderate / high risk - no history) |
| Q10 | varchar |  |  | SI | Major criteria - moderate / high risk - history |
| Q11 | varchar |  |  | SI | Minor criteria (low risk - no history) |
| Q12 | varchar |  |  | SI | Minor criteria (low risk - history) |
| Q13 | varchar |  |  | SI | Minor criteria (high risk - no history) |
| Q14 | varchar |  |  | SI | Minor criteria (high risk - history) |
| Q15 | varchar |  |  | SI | Revised Jones Criteria (Gerwitz) |
| Q16 | varchar |  |  | SI | A. For all patient populations with evidence of pr... |
| Q17 | varchar |  |  | SI | Evidence of preceding GAS infection is determined ... |
| Q18 | varchar |  |  | SI | ● Increased or rising anti-streptolysin O titer or... |
| Q19 | varchar |  |  | SI | ● A positive rapid group A streptococcal (GAS) car... |
| Q20 | varchar |  |  | SI | ● A positive throat culture for group A β-haemolyt... |
| Q21 | varchar |  |  | SI | Diagnosis: Initial ARF 2 Major manifestations or 1... |
| Q22 | varchar |  |  | SI | B. Major criteria |
| Q23 | varchar |  |  | SI | Low-risk populations |
| Q24 | varchar |  |  | SI | Carditis (clinical and/or subclinical) |
| Q25 | varchar |  |  | SI | Arthritis (polyarthritis only) |
| Q26 | varchar |  |  | SI | Chorea |
| Q27 | varchar |  |  | SI | Erythema marginatum |
| Q28 | varchar |  |  | SI | Subcutaneous nodules |
| Q29 | varchar |  |  | SI | Moderate- and high - risk populations |
| Q30 | varchar |  |  | SI | Carditis (clinical and/or subclinical) |
| Q31 | varchar |  |  | SI | Arthritis (monoarthritis or polyarthritis; polyart... |
| Q32 | varchar |  |  | SI | Chorea |
| Q33 | varchar |  |  | SI | Erythema marginatum |
| Q34 | varchar |  |  | SI | Subcutaneous nodules |
| Q35 | varchar |  |  | SI | C. Minor criteria |
| Q36 | varchar |  |  | SI | Low - risk populations |
| Q37 | varchar |  |  | SI | Polyarthralgia |
| Q38 | varchar |  |  | SI | Fever (≥ 38.5°C) |
| Q39 | varchar |  |  | SI | ESR ≥ 60 mm in the first hour and/or CRP ≥ 3.0 mg/... |
| Q40 | varchar |  |  | SI | Prolonged PR interval, after accounting for age va... |
| Q41 | varchar |  |  | SI | Moderate- and high - risk populations |
| Q42 | varchar |  |  | SI | Monoarthralgia |
| Q43 | varchar |  |  | SI | Fever (≥ 38°C) |
| Q44 | varchar |  |  | SI | ESR ≥ 30 mm/h and/or CRP ≥ 3.0 mg/dL |
| Q45 | varchar |  |  | SI | Prolonged PR interval, after accounting for age va... |
| Q46 | varchar |  |  | SI | Notes regarding above criteria: |
| Q47 | varchar |  |  | SI | ● Low - risk populations are those with ARF incide... |
| Q48 | varchar |  |  | SI | ● Subclinical carditis indicates echocardiographic... |
| Q49 | varchar |  |  | SI | ● Polyarthralgia should only be considered as a ma... |
| Q50 | varchar |  |  | SI | ● Erythema marginatum and subcutaneous nodules are... |
| Q51 | varchar |  |  | SI | ● CRP value must be greater than upper  limit of n... |
| Q52 | varchar |  |  | SI | Abbreviations |
| Q53 | varchar |  |  | SI | ARF indicates acute rheumatic fever |
| Q54 | varchar |  |  | SI | CRP, C-reactive protein |
| Q55 | varchar |  |  | SI | ESR, erythrocyte sedimentation rate |
| Q56 | varchar |  |  | SI | GAS, group A streptococcal infection |
| Q57 | varchar |  |  | SI | Positive diagnosis of initial acute rheumatic feve... |
| Q58 | varchar |  |  | SI | Negative diagnosis of initial acute rheumatic feve... |
| Q59 | varchar |  |  | SI | Positive diagnosis of recurrent acute rheumatic fe... |
| Q60 | varchar |  |  | SI | Negative diagnosis of recurrent acute rheumatic fe... |
| Q61 | varchar |  |  | SI | The Jones Criteria is used to aid diagnosis of ini... |
| Q62 | varchar |  |  | SI | Additionally, joint manifestations can only be con... |
| Q63 | varchar |  |  | SI | Diagnosis: Recurrent ARF 2 Major or 1 major and 2 ... |
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