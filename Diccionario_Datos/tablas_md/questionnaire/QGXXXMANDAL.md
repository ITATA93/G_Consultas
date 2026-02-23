# questionnaire.QGXXXMANDAL

> Antenatal discussion and leaflets

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal discussion and leaflets

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | bit |  |  | SI | Trivalent seasonal influenza vaccine |
| Q03 | bit |  |  | SI | Pertussis (whooping cough) vaccine |
| Q04 | bit |  |  | SI | Healthy eating in pregnancy |
| Q05 | bit |  |  | SI | Folic acid |
| Q06 | bit |  |  | SI | Importance of iron and best dietary sources |
| Q07 | bit |  |  | SI | Vitamin D supplementation |
| Q08 | bit |  |  | SI | Food safety and hygiene |
| Q09 | bit |  |  | SI | Alcohol and caffeine current consumption recommend... |
| Q10 | bit |  |  | SI | Previous breast feeding experiences |
| Q11 | bit |  |  | SI | BCG vaccination |
| Q12 | bit |  |  | SI | Common pregnancy symptoms |
| Q13 | bit |  |  | SI | Exercise |
| Q14 | bit |  |  | SI | HIV |
| Q15 | bit |  |  | SI | Parenting classes |
| Q16 | bit |  |  | SI | Sex in pregnancy |
| Q17 | bit |  |  | SI | Other topics |
| Q18 | varchar |  |  | SI | Details |
| Q19 | bit |  |  | SI | Eligible for Health Start |
| Q20 | bit |  |  | SI | Accessed vitamin supplements |
| Q21 | bit |  |  | SI | Screening tests for you and your baby |
| Q22 | bit |  |  | SI | Amniocentesis |
| Q23 | bit |  |  | SI | Birth choices after a caesarian section |
| Q24 | bit |  |  | SI | Birth place choice |
| Q25 | bit |  |  | SI | Domestic abuse |
| Q26 | bit |  |  | SI | Folic acid - what all women should know |
| Q27 | bit |  |  | SI | FSA - eating while you are pregnant |
| Q28 | bit |  |  | SI | Home birth |
| Q29 | bit |  |  | SI | Breast feeding - off to the best start |
| Q30 | bit |  |  | SI | Other leaflets given |
| Q31 | varchar |  |  | SI | Details |
| Q32 | bit |  |  | SI | Medical examination by your GP |
| Q33 | bit |  |  | SI | Has a referral been made for GP medical examinatio... |
| Q34 | bit |  |  | SI | Certificate of pregnancy FW8 |
| Q35 | bit |  |  | SI | Certificate of expected confinement MatB1 |
| Q36 | bit |  |  | SI | Maternity allowances |
| Q37 | bit |  |  | SI | Other |
| Q38 | varchar |  |  | SI | Details |
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