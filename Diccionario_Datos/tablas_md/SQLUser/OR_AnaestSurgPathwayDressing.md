# SQLUser.OR_AnaestSurgPathwayDressing

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRSNG_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| DRSNG_Childsub | numeric |  |  | NO | Childsub |
| DRSNG_Dressing_DR | bigint |  | FK | NO |  Des Ref ORC_Dressing |
| DRSNG_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pre-operative care day |
| Q04 | - |  |  | SI | Patient referred to other members of the multidisc... |
| Q05 | - |  |  | SI | For example: Medical team, Anaesthetics, Orthopaed... |
| Q06 | - |  |  | SI | Variance |
| Q07 | - |  |  | SI | Patient reviewed by other members of the multidisc... |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Patient has attended all required investigative pr... |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | Pharmacological venous thrombo-embolism prophylaxi... |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | All ordered blood tests taken and results reviewed |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | Patient has a valid group and hold available |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | Patient has signed consent form and understands pl... |
| Q18 | - |  |  | SI | Variance |
| Q19 | - |  |  | SI | Patient seen by the anaesthetist and anaesthetic a... |
| Q20 | - |  |  | SI | Variance |
| Q21 | - |  |  | SI | Patient is fasting, clear fluids to 2 hours pre op... |
| Q22 | - |  |  | SI | Variance |
| Q23 | - |  |  | SI | Alert and orientated |
| Q24 | - |  |  | SI | Variance |
| Q25 | - |  |  | SI | Patient monitored and assessed for delirium |
| Q26 | - |  |  | SI | Variance |
| Q27 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q28 | - |  |  | SI | Variance |
| Q29 | - |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q30 | - |  |  | SI | Variance |
| Q31 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q32 | - |  |  | SI | Variance |
| Q33 | - |  |  | SI | Patient's regular medication prescribed and admini... |
| Q34 | - |  |  | SI | Variance |
| Q35 | - |  |  | SI | Patient has appropriate venous thrombosis therapy ... |
| Q36 | - |  |  | SI | Variance |
| Q37 | - |  |  | SI | Patient tolerating oral diet and fluids |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Intravenous fluid therapy administered as prescrib... |
| Q40 | - |  |  | SI | Variance |
| Q41 | - |  |  | SI | Strict fluid balance chart maintained |
| Q42 | - |  |  | SI | Variance |
| Q43 | - |  |  | SI | Indwelling catheter inserted under aseptic conditi... |
| Q44 | - |  |  | SI | Variance |
| Q45 | - |  |  | SI | Urine output > 30 mLs per hour |
| Q46 | - |  |  | SI | Variance |
| Q47 | - |  |  | SI | Patient performed deep breathing and coughing exer... |
| Q48 | - |  |  | SI | Variance |
| Q49 | - |  |  | SI | Patient remained on strict rest in bed |
| Q50 | - |  |  | SI | Variance |
| Q51 | - |  |  | SI | Traction applied as clinically indicated and revie... |
| Q52 | - |  |  | SI | Variance |
| Q53 | - |  |  | SI | Patient has received regular pressure area care wi... |
| Q54 | - |  |  | SI | Variance |
| Q55 | - |  |  | SI | Patient skin remains intact and is free from press... |
| Q56 | - |  |  | SI | Variance |
| Q57 | - |  |  | SI | Personal hygiene attended |
| Q58 | - |  |  | SI | Variance |
| Q59 | - |  |  | SI | Patient received mouth and eye care as clinically ... |
| Q60 | - |  |  | SI | Variance |
| Q61 | - |  |  | SI | Document last bowel motion, regular bowel motions ... |
| Q62 | - |  |  | SI | Variance |
| Q63 | - |  |  | SI | All bowel motions documented |
| Q64 | - |  |  | SI | Variance |
| Q65 | - |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q66 | - |  |  | SI | Variance |
| Q67 | - |  |  | SI | Patient and family provided education on patient j... |
| Q68 | - |  |  | SI | Variance |
| Q69 | - |  |  | SI | Explain all interventions to patient / family |
| Q70 | - |  |  | SI | Variance |
| Q71 | - |  |  | SI | Patient referred to allied health services as clin... |
| Q72 | - |  |  | SI | Variance |
| Q73 | - |  |  | SI | Patient safety considered, i.e. bedside rails, pat... |
| Q74 | - |  |  | SI | Variance |
| Q75 | - |  |  | SI | Estimated date of discharge documented and discuss... |
| Q76 | - |  |  | SI | Variance |
| Q77 | - |  |  | SI | Commenced discharge planning |
| Q78 | - |  |  | SI | Variance |
| Q79 | - |  |  | SI | Continued discharge planning |
| Q80 | - |  |  | SI | Variance |
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