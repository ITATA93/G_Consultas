# questionnaire.QGXXXPSI

> Pneumonia Severity Index

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pneumonia Severity Index

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Over 50 years of age |
| Q06 | varchar |  |  | SI | Temperature <35°C or >=40°C |
| Q12 | varchar |  |  | SI | Did you answer Yes to any question above? |
| Q13 | varchar |  |  | SI | Sex |
| Q14 | varchar |  |  | SI | Age |
| Q15 | varchar |  |  | SI | Sex Points |
| Q16 | varchar |  |  | SI | Nursing home resident |
| Q17 | varchar |  |  | SI | Neoplastic disease |
| Q18 | varchar |  |  | SI | Liver disease |
| Q19 | varchar |  |  | SI | Congestive heart failure |
| Q20 | varchar |  |  | SI | Cerebrovascular disease |
| Q21 | varchar |  |  | SI | Renal disease |
| Q22 | varchar |  |  | SI | Altered mental status |
| Q23 | varchar |  |  | SI | Pulse >=125/minute |
| Q24 | varchar |  |  | SI | Respiratory rate >30/minute |
| Q25 | varchar |  |  | SI | Systolic blood pressure <90 mm Hg |
| Q26 | varchar |  |  | SI | Arterial pH <7.35 |
| Q27 | varchar |  |  | SI | Blood urea nitrogen >=30 mg/dl (9 mmol/liter) |
| Q28 | varchar |  |  | SI | Sodium <130 mmol/liter |
| Q29 | varchar |  |  | SI | Glucose >=250 mg/dl (14 mmol/liter) |
| Q30 | varchar |  |  | SI | Hematocrit <30% |
| Q31 | varchar |  |  | SI | Partial pressure of arterial O2 <60mmHg |
| Q32 | varchar |  |  | SI | Pleural effusion |
| Q33 | varchar |  |  | SI | 1 to 70: Risk Class II (30-day mortality 0.6%) |
| Q34 | varchar |  |  | SI | 71 to 90: Risk Class III (30-day mortality 0.9%) |
| Q35 | varchar |  |  | SI | 0: Risk Class I (30-day mortality 0.1%) |
| Q36 | varchar |  |  | SI | 91 to 130: Risk Class IV (30-day mortality 9.3%) |
| Q37 | varchar |  |  | SI | >130: Risk Class V (30-day mortality 27%) |
| Q38 | varchar |  |  | SI | Step 2: Stratify to Risk Class II vs III vs IV vs ... |
| Q39 | varchar |  |  | SI | Demographics |
| Q40 | varchar |  |  | SI | Step 1: Stratify to Risk Class I vs. Risk Classes ... |
| Q41 | varchar |  |  | SI | Laboratory and Radiographic Findings |
| Q43 | varchar |  |  | SI | Physical Exam Findings |
| Q44 | varchar |  |  | SI | Comorbidity and History of: |
| Q45 | date |  |  | SI | Date |
| Q46a | varchar |  |  | SI | The pneumonia severity index (PSI) is a clinical p... |
| Q46b | varchar |  |  | SI | in patients presenting to the emergency department... |
| Q47 | varchar |  |  | SI | Please proceed with Step 2  |
| Q48 | varchar |  |  | SI | Score |
| Q50 | varchar |  |  | SI | Sex |
| Q51agemale | varchar |  |  | SI | Age |
| Q52 | date |  |  | SI | Date |
| Q52femaleage | varchar |  |  | SI | Age |
| Q53 | time |  |  | SI | Time |
| Q54 | varchar |  |  | SI | Over 50 years of age |
| Q55 | varchar |  |  | SI | Temperature <35 °C or ≥40 °C |
| Q56 | varchar |  |  | SI | Nursing home resident |
| Q57 | varchar |  |  | SI | Neoplastic disease |
| Q58 | varchar |  |  | SI | Liver disease |
| Q59 | varchar |  |  | SI | Congestive heart failure |
| Q60 | varchar |  |  | SI | Cerebrovascular disease |
| Q61 | varchar |  |  | SI | Renal disease |
| Q62 | varchar |  |  | SI | Altered mental status |
| Q63 | varchar |  |  | SI | Pulse ≥125/minute |
| Q64 | varchar |  |  | SI | Respiratory rate ≥30/minute |
| Q65 | varchar |  |  | SI | Systolic blood pressure <90 mm Hg |
| Q66 | varchar |  |  | SI | Arterial pH <7.35 |
| Q67 | varchar |  |  | SI | Blood urea nitrogen ≥30 mg/dL (9 mmol/L) |
| Q68 | varchar |  |  | SI | Sodium <130 mmol/L |
| Q69 | varchar |  |  | SI | Glucose ≥250 mg/dL (14 mmol/L) |
| Q70 | varchar |  |  | SI | Hematocrit <30% |
| Q71 | varchar |  |  | SI | Partial pressure of arterial O2 <60 mm Hg (8 kPa)	 |
| Q72 | varchar |  |  | SI | Pleural effusion |
| Q73 | varchar |  |  | SI | Source: Fine MJ, Auble TE, Yealy DM, et al,. A Pre... |
| Q74 | varchar |  |  | SI | Temperature <35 °C or ≥40 °C |
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