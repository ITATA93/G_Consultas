# questionnaire.QTCFNOFPPC

> Fractured Neck of Femur Pre-Procedure Care Activities Checklist

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fractured Neck of Femur Pre-Procedure Care Activities Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Pre-operative care day |
| Q04 | varchar |  |  | SI | Patient referred to other members of the multidisc... |
| Q05 | varchar |  |  | SI | For example: Medical team, Anaesthetics, Orthopaed... |
| Q06 | varchar |  |  | SI | Variance |
| Q07 | varchar |  |  | SI | Patient reviewed by other members of the multidisc... |
| Q08 | varchar |  |  | SI | Variance |
| Q09 | varchar |  |  | SI | Patient has attended all required investigative pr... |
| Q10 | varchar |  |  | SI | Variance |
| Q11 | varchar |  |  | SI | Pharmacological venous thrombo-embolism prophylaxi... |
| Q12 | varchar |  |  | SI | Variance |
| Q13 | varchar |  |  | SI | All ordered blood tests taken and results reviewed |
| Q14 | varchar |  |  | SI | Variance |
| Q15 | varchar |  |  | SI | Patient has a valid group and hold available |
| Q16 | varchar |  |  | SI | Variance |
| Q17 | varchar |  |  | SI | Patient has signed consent form and understands pl... |
| Q18 | varchar |  |  | SI | Variance |
| Q19 | varchar |  |  | SI | Patient seen by the anaesthetist and anaesthetic a... |
| Q20 | varchar |  |  | SI | Variance |
| Q21 | varchar |  |  | SI | Patient is fasting, clear fluids to 2 hours pre op... |
| Q22 | varchar |  |  | SI | Variance |
| Q23 | varchar |  |  | SI | Alert and orientated |
| Q24 | varchar |  |  | SI | Variance |
| Q25 | varchar |  |  | SI | Patient monitored and assessed for delirium |
| Q26 | varchar |  |  | SI | Variance |
| Q27 | varchar |  |  | SI | Observations are within acceptable limits and stab... |
| Q28 | varchar |  |  | SI | Variance |
| Q29 | varchar |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q30 | varchar |  |  | SI | Variance |
| Q31 | varchar |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q32 | varchar |  |  | SI | Variance |
| Q33 | varchar |  |  | SI | Patient's regular medication prescribed and admini... |
| Q34 | varchar |  |  | SI | Variance |
| Q35 | varchar |  |  | SI | Patient has appropriate venous thrombosis therapy ... |
| Q36 | varchar |  |  | SI | Variance |
| Q37 | varchar |  |  | SI | Patient tolerating oral diet and fluids |
| Q38 | varchar |  |  | SI | Variance |
| Q39 | varchar |  |  | SI | Intravenous fluid therapy administered as prescrib... |
| Q40 | varchar |  |  | SI | Variance |
| Q41 | varchar |  |  | SI | Strict fluid balance chart maintained |
| Q42 | varchar |  |  | SI | Variance |
| Q43 | varchar |  |  | SI | Indwelling catheter inserted under aseptic conditi... |
| Q44 | varchar |  |  | SI | Variance |
| Q45 | varchar |  |  | SI | Urine output > 30 mLs per hour |
| Q46 | varchar |  |  | SI | Variance |
| Q47 | varchar |  |  | SI | Patient performed deep breathing and coughing exer... |
| Q48 | varchar |  |  | SI | Variance |
| Q49 | varchar |  |  | SI | Patient remained on strict rest in bed |
| Q50 | varchar |  |  | SI | Variance |
| Q51 | varchar |  |  | SI | Traction applied as clinically indicated and revie... |
| Q52 | varchar |  |  | SI | Variance |
| Q53 | varchar |  |  | SI | Patient has received regular pressure area care wi... |
| Q54 | varchar |  |  | SI | Variance |
| Q55 | varchar |  |  | SI | Patient skin remains intact and is free from press... |
| Q56 | varchar |  |  | SI | Variance |
| Q57 | varchar |  |  | SI | Personal hygiene attended |
| Q58 | varchar |  |  | SI | Variance |
| Q59 | varchar |  |  | SI | Patient received mouth and eye care as clinically ... |
| Q60 | varchar |  |  | SI | Variance |
| Q61 | varchar |  |  | SI | Document last bowel motion, regular bowel motions ... |
| Q62 | varchar |  |  | SI | Variance |
| Q63 | varchar |  |  | SI | All bowel motions documented |
| Q64 | varchar |  |  | SI | Variance |
| Q65 | varchar |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q66 | varchar |  |  | SI | Variance |
| Q67 | varchar |  |  | SI | Patient and family provided education on patient j... |
| Q68 | varchar |  |  | SI | Variance |
| Q69 | varchar |  |  | SI | Explain all interventions to patient / family |
| Q70 | varchar |  |  | SI | Variance |
| Q71 | varchar |  |  | SI | Patient referred to allied health services as clin... |
| Q72 | varchar |  |  | SI | Variance |
| Q73 | varchar |  |  | SI | Patient safety considered, i.e. bedside rails, pat... |
| Q74 | varchar |  |  | SI | Variance |
| Q75 | varchar |  |  | SI | Estimated date of discharge documented and discuss... |
| Q76 | varchar |  |  | SI | Variance |
| Q77 | varchar |  |  | SI | Commenced discharge planning |
| Q78 | varchar |  |  | SI | Variance |
| Q79 | varchar |  |  | SI | Continued discharge planning |
| Q80 | varchar |  |  | SI | Variance |
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