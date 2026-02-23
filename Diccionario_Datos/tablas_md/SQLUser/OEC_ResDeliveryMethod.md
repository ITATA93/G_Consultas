# SQLUser.OEC_ResDeliveryMethod

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RDM_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Over 50 years of age |
| Q06 | - |  |  | SI | Temperature <35°C or >=40°C |
| Q12 | - |  |  | SI | Did you answer Yes to any question above? |
| Q13 | - |  |  | SI | Sex |
| Q14 | - |  |  | SI | Age |
| Q15 | - |  |  | SI | Sex Points |
| Q16 | - |  |  | SI | Nursing home resident |
| Q17 | - |  |  | SI | Neoplastic disease |
| Q18 | - |  |  | SI | Liver disease |
| Q19 | - |  |  | SI | Congestive heart failure |
| Q20 | - |  |  | SI | Cerebrovascular disease |
| Q21 | - |  |  | SI | Renal disease |
| Q22 | - |  |  | SI | Altered mental status |
| Q23 | - |  |  | SI | Pulse >=125/minute |
| Q24 | - |  |  | SI | Respiratory rate >30/minute |
| Q25 | - |  |  | SI | Systolic blood pressure <90 mm Hg |
| Q26 | - |  |  | SI | Arterial pH <7.35 |
| Q27 | - |  |  | SI | Blood urea nitrogen >=30 mg/dl (9 mmol/liter) |
| Q28 | - |  |  | SI | Sodium <130 mmol/liter |
| Q29 | - |  |  | SI | Glucose >=250 mg/dl (14 mmol/liter) |
| Q30 | - |  |  | SI | Hematocrit <30% |
| Q31 | - |  |  | SI | Partial pressure of arterial O2 <60mmHg |
| Q32 | - |  |  | SI | Pleural effusion |
| Q33 | - |  |  | SI | 1 to 70: Risk Class II (30-day mortality 0.6%) |
| Q34 | - |  |  | SI | 71 to 90: Risk Class III (30-day mortality 0.9%) |
| Q35 | - |  |  | SI | 0: Risk Class I (30-day mortality 0.1%) |
| Q36 | - |  |  | SI | 91 to 130: Risk Class IV (30-day mortality 9.3%) |
| Q37 | - |  |  | SI | >130: Risk Class V (30-day mortality 27%) |
| Q38 | - |  |  | SI | Step 2: Stratify to Risk Class II vs III vs IV vs ... |
| Q39 | - |  |  | SI | Demographics |
| Q40 | - |  |  | SI | Step 1: Stratify to Risk Class I vs. Risk Classes ... |
| Q41 | - |  |  | SI | Laboratory and Radiographic Findings |
| Q43 | - |  |  | SI | Physical Exam Findings |
| Q44 | - |  |  | SI | Comorbidity and History of: |
| Q45 | - |  |  | SI | Date |
| Q46a | - |  |  | SI | The pneumonia severity index (PSI) is a clinical p... |
| Q46b | - |  |  | SI | in patients presenting to the emergency department... |
| Q47 | - |  |  | SI | Please proceed with Step 2 |
| Q48 | - |  |  | SI | Score |
| Q50 | - |  |  | SI | Sex |
| Q51agemale | - |  |  | SI | Age |
| Q52 | - |  |  | SI | Date |
| Q52femaleage | - |  |  | SI | Age |
| Q53 | - |  |  | SI | Time |
| Q54 | - |  |  | SI | Over 50 years of age |
| Q55 | - |  |  | SI | Temperature <35 °C or ≥40 °C |
| Q56 | - |  |  | SI | Nursing home resident |
| Q57 | - |  |  | SI | Neoplastic disease |
| Q58 | - |  |  | SI | Liver disease |
| Q59 | - |  |  | SI | Congestive heart failure |
| Q60 | - |  |  | SI | Cerebrovascular disease |
| Q61 | - |  |  | SI | Renal disease |
| Q62 | - |  |  | SI | Altered mental status |
| Q63 | - |  |  | SI | Pulse ≥125/minute |
| Q64 | - |  |  | SI | Respiratory rate ≥30/minute |
| Q65 | - |  |  | SI | Systolic blood pressure <90 mm Hg |
| Q66 | - |  |  | SI | Arterial pH <7.35 |
| Q67 | - |  |  | SI | Blood urea nitrogen ≥30 mg/dL (9 mmol/L) |
| Q68 | - |  |  | SI | Sodium <130 mmol/L |
| Q69 | - |  |  | SI | Glucose ≥250 mg/dL (14 mmol/L) |
| Q70 | - |  |  | SI | Hematocrit <30% |
| Q71 | - |  |  | SI | Partial pressure of arterial O2 <60 mm Hg (8 kPa)	 |
| Q72 | - |  |  | SI | Pleural effusion |
| Q73 | - |  |  | SI | Source: Fine MJ, Auble TE, Yealy DM, et al,. A Pre... |
| Q74 | - |  |  | SI | Temperature <35 °C or ≥40 °C |
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
| RDM_Code | varchar |  |  | NO | Code |
| RDM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RDM_CreatedDate | date |  |  | SI | Created Date |
| RDM_CreatedTime | time |  |  | SI | Created Time |
| RDM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RDM_Desc | varchar |  |  | NO | Description |
| RDM_Owner | varchar |  |  | SI | Owner |
| RDM_UpdatedDate | date |  |  | SI | Updated Date |
| RDM_UpdatedTime | time |  |  | SI | Updated Time |
| RDM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*