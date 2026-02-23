# questionnaire.QTCWPUPS

> Waterlow Score (2005)

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Waterlow Score (2005)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Sex |
| Q04 | varchar |  |  | SI | Age |
| Q05 | varchar |  |  | SI | Build or weight-for-height |
| Q06 | varchar |  |  | SI | Skin type or visual risk areas (you may select mor... |
| Q07 | varchar |  |  | SI | Continence |
| Q08 | varchar |  |  | SI | Mobility (you may select more than one response) |
| Q09 | varchar |  |  | SI | Has patient lost weight recently? |
| Q10 | varchar |  |  | SI | Weight loss score |
| Q11 | varchar |  |  | SI | Patient eating poorly or lack of appetite  |
| Q12 | varchar |  |  | SI | Patient eating poorly or lack of appetite |
| Q13 | varchar |  |  | SI | Diabetes, Multiple Sclerosis (MS), Cerebrovascular... |
| Q14 | varchar |  |  | SI | Motor / Sensory	 |
| Q15 | varchar |  |  | SI | Paraplegia |
| Q16 | varchar |  |  | SI | Neurological Deficit |
| Q17 | varchar |  |  | SI | More than one option can be selected against the f... |
| Q18 | varchar |  |  | SI | Scores can be discounted after 48h provided patien... |
| Q19 | varchar |  |  | SI | Malnutrition Screening Tool (MST). If < 2 refer fo... |
| Q20 | varchar |  |  | SI | If < 2 refer for nutrition assessment / interventi... |
| Q21 | varchar |  |  | SI | The Waterlow Score was originally described in 198... |
| Q22 | varchar |  |  | SI | References |
| Q23 | varchar |  |  | SI | 1. Waterlow J. Pressure sores: a risk assessment c... |
| Q24 | varchar |  |  | SI | 2. Waterlow J. From costly treatment to cost-effec... |
| Q25 | varchar |  |  | SI | 3. Ferguson M, Capra S, Bauer J, Banks M. Developm... |
| Q26 | varchar |  |  | SI | Waterlow score |
| Q27 | varchar |  |  | SI | MST score |
| Q28 | varchar |  |  | SI | The Waterlow score gives an estimated risk for the... |
| Q29 | varchar |  |  | SI | Malnutrition Screening Tool (MST) |
| Q30 | varchar |  |  | SI | Nutrition is an extremely important contributory f... |
| Q31 | varchar |  |  | SI | Terminal cachexia |
| Q32 | varchar |  |  | SI | Multiple organ failure |
| Q33 | varchar |  |  | SI | Single organ failure (respiratory, renal, cardiac) |
| Q34 | varchar |  |  | SI | Peripheral vascular disease |
| Q35 | varchar |  |  | SI | Anaemia (Hb <8 g/dL) |
| Q36 | varchar |  |  | SI | Smoking |
| Q37 | varchar |  |  | SI | Orthopaedic or spinal surgery |
| Q38 | varchar |  |  | SI | On table >2 hours (within last 48 hours) |
| Q39 | varchar |  |  | SI | On table >6 hours (within last 48 hours) |
| Q40 | varchar |  |  | SI | Is receiving cytotoxics, long-term or high-dose st... |
| Q41 | varchar |  |  | SI | Single organ failure (respiratory, renal, cardiac) |
| Q42 | varchar |  |  | SI | Patient eating poorly or lack of appetite |
| Q43 | varchar |  |  | SI | Build or weight-for-height |
| Q44 | varchar |  |  | SI | Patient eating poorly or lack of appetite |
| Q45 | varchar |  |  | SI | Patient eating poorly or lack of appetite |
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