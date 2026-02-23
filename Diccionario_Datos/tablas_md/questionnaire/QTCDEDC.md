# questionnaire.QTCDEDC

> Diabetes Education Discharge Checklist

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Diabetes Education Discharge Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Discussed the rationale for chosen insulin regimen |
| Q11 | varchar |  |  | SI | Supplied with Blood Glucose (BG) monitor and educa... |
| Q12 | varchar |  |  | SI | Encouraged to verbalise feelings about diabetes |
| Q13 | varchar |  |  | SI | Discussed family's prior experience with diabetes |
| Q14 | varchar |  |  | SI | Discussed physiology of hypoglycaemia |
| Q15 | varchar |  |  | SI | Identify signs and symptoms of hypoglycaemia |
| Q16 | varchar |  |  | SI | Discussed treatments for hypoglycaemia (age approp... |
| Q17 | varchar |  |  | SI | Discussed sport and activity |
| Q18 | varchar |  |  | SI | Discussed and review technique of administering in... |
| Q19 | varchar |  |  | SI | Identified correct sites for insulin injections |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Discussed the importance of site rotation |
| Q21 | varchar |  |  | SI | Discussed storage of insulin |
| Q22 | varchar |  |  | SI | Discussed disposal of sharps |
| Q23 | varchar |  |  | SI | Identified target range for Blood Glucose Level (B... |
| Q24 | varchar |  |  | SI | Discussed correct technique for BG testing |
| Q25 | varchar |  |  | SI | Discussed importance of keeping a record book |
| Q26 | varchar |  |  | SI | Discussed hba1c and desired range (age appropriate... |
| Q27 | varchar |  |  | SI | Discussed complications of diabetes |
| Q28 | varchar |  |  | SI | Discussed physiology of ketones |
| Q29 | varchar |  |  | SI | Stated when to test for ketones |
| Q3 | date |  |  | SI | Date of discharge |
| Q30 | varchar |  |  | SI | Discussed Diabetic Ketoacidosis (DKA) |
| Q31 | varchar |  |  | SI | Discussed sick day management |
| Q32 | varchar |  |  | SI | Discussed severe hypoglycaemia |
| Q33 | varchar |  |  | SI | Demonstrated use of glucagen hypo kit |
| Q34 | varchar |  |  | SI | Equipment collected and follow up appointments mad... |
| Q35 | varchar |  |  | SI | Discussed daily living (returning to work / school... |
| Q36 | varchar |  |  | SI | Given contact details for diabetes service |
| Q37 | varchar |  |  | SI | Post Discharge Review |
| Q38 | varchar |  |  | SI | Outpatient within 1 week of discharge |
| Q39 | varchar |  |  | SI | School management plan if at school (needs to be u... |
| Q4 | varchar |  |  | SI | Diabetes education whilst in hospital? |
| Q40 | varchar |  |  | SI | In-Depth Education Phase |
| Q41 | varchar |  |  | SI | 4 - 6 weeks post discharge |
| Q42 | varchar |  |  | SI | Assessment / Reinforcement of current knowledge |
| Q43 | varchar |  |  | SI | Foot care |
| Q44 | varchar |  |  | SI | Complications / Screening |
| Q45 | varchar |  |  | SI | Good health for the future: - alcohol - smoking - ... |
| Q46 | varchar |  |  | SI | Travel / Employment choices |
| Q47 | varchar |  |  | SI | PLUS the following as appropriate |
| Q48 | varchar |  |  | SI | Puberty / Menstruation / Menopause |
| Q49 | varchar |  |  | SI | Contraception / Family planning / Pregnancy |
| Q5 | varchar |  |  | SI | Acute Education Phase |
| Q50 | varchar |  |  | SI | Sexual health / Erectile dysfunction |
| Q6 | varchar |  |  | SI | Discussed pathophysiology and aetiology of diabete... |
| Q7 | varchar |  |  | SI | Discussed Type 1 versus Type 2 diabetes |
| Q8 | varchar |  |  | SI | Identify symptoms of diabetes |
| Q9 | varchar |  |  | SI | Discussed insulin onset, peak and duration |
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