# SQLUser.LBC_ObservationGroup

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCOBSG_RowID | bigint | PK |  | NO | - |
| LBCOBSG_Code | varchar |  |  | SI | Code |
| LBCOBSG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCOBSG_CreatedDate | date |  |  | SI | Created Date |
| LBCOBSG_CreatedTime | time |  |  | SI | Created Time |
| LBCOBSG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCOBSG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCOBSG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCOBSG_DepartmentRestrictions | varchar |  |  | SI | Lab Department Restrictions |
| LBCOBSG_Desc | varchar |  |  | SI | Description |
| LBCOBSG_Owner | varchar |  |  | SI | Owner |
| LBCOBSG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCOBSG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCOBSG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Discussed the rationale for chosen insulin regimen |
| Q11 | - |  |  | SI | Supplied with Blood Glucose (BG) monitor and educa... |
| Q12 | - |  |  | SI | Encouraged to verbalise feelings about diabetes |
| Q13 | - |  |  | SI | Discussed family's prior experience with diabetes |
| Q14 | - |  |  | SI | Discussed physiology of hypoglycaemia |
| Q15 | - |  |  | SI | Identify signs and symptoms of hypoglycaemia |
| Q16 | - |  |  | SI | Discussed treatments for hypoglycaemia (age approp... |
| Q17 | - |  |  | SI | Discussed sport and activity |
| Q18 | - |  |  | SI | Discussed and review technique of administering in... |
| Q19 | - |  |  | SI | Identified correct sites for insulin injections |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Discussed the importance of site rotation |
| Q21 | - |  |  | SI | Discussed storage of insulin |
| Q22 | - |  |  | SI | Discussed disposal of sharps |
| Q23 | - |  |  | SI | Identified target range for Blood Glucose Level (B... |
| Q24 | - |  |  | SI | Discussed correct technique for BG testing |
| Q25 | - |  |  | SI | Discussed importance of keeping a record book |
| Q26 | - |  |  | SI | Discussed hba1c and desired range (age appropriate... |
| Q27 | - |  |  | SI | Discussed complications of diabetes |
| Q28 | - |  |  | SI | Discussed physiology of ketones |
| Q29 | - |  |  | SI | Stated when to test for ketones |
| Q3 | - |  |  | SI | Date of discharge |
| Q30 | - |  |  | SI | Discussed Diabetic Ketoacidosis (DKA) |
| Q31 | - |  |  | SI | Discussed sick day management |
| Q32 | - |  |  | SI | Discussed severe hypoglycaemia |
| Q33 | - |  |  | SI | Demonstrated use of glucagen hypo kit |
| Q34 | - |  |  | SI | Equipment collected and follow up appointments mad... |
| Q35 | - |  |  | SI | Discussed daily living (returning to work / school... |
| Q36 | - |  |  | SI | Given contact details for diabetes service |
| Q37 | - |  |  | SI | Post Discharge Review |
| Q38 | - |  |  | SI | Outpatient within 1 week of discharge |
| Q39 | - |  |  | SI | School management plan if at school (needs to be u... |
| Q4 | - |  |  | SI | Diabetes education whilst in hospital? |
| Q40 | - |  |  | SI | In-Depth Education Phase |
| Q41 | - |  |  | SI | 4 - 6 weeks post discharge |
| Q42 | - |  |  | SI | Assessment / Reinforcement of current knowledge |
| Q43 | - |  |  | SI | Foot care |
| Q44 | - |  |  | SI | Complications / Screening |
| Q45 | - |  |  | SI | Good health for the future: - alcohol - smoking - ... |
| Q46 | - |  |  | SI | Travel / Employment choices |
| Q47 | - |  |  | SI | PLUS the following as appropriate |
| Q48 | - |  |  | SI | Puberty / Menstruation / Menopause |
| Q49 | - |  |  | SI | Contraception / Family planning / Pregnancy |
| Q5 | - |  |  | SI | Acute Education Phase |
| Q50 | - |  |  | SI | Sexual health / Erectile dysfunction |
| Q6 | - |  |  | SI | Discussed pathophysiology and aetiology of diabete... |
| Q7 | - |  |  | SI | Discussed Type 1 versus Type 2 diabetes |
| Q8 | - |  |  | SI | Identify symptoms of diabetes |
| Q9 | - |  |  | SI | Discussed insulin onset, peak and duration |
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