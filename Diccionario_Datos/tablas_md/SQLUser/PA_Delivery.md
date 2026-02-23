# SQLUser.PA_Delivery

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEL_RowId | bigint | PK |  | NO | - |
| DEL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEL_Comments | varchar |  |  | SI | Comments |
| DEL_Date | date |  |  | SI | Date |
| DEL_DeliveredTo | varchar |  |  | SI | Delivered To |
| DEL_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| DEL_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| DEL_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| DEL_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| DEL_Method_DR | bigint |  | FK | SI | Des Ref Method |
| DEL_PADischargeSummary_DR | bigint |  | FK | SI | Des Ref PAAdmDischargeSummary |
| DEL_PALetter_DR | bigint |  | FK | SI | Des Ref PALetter |
| DEL_Time | time |  |  | SI | Time |
| DEL_User | varchar |  |  | SI | User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Sex |
| Q04 | - |  |  | SI | Age |
| Q05 | - |  |  | SI | Build or weight-for-height |
| Q06 | - |  |  | SI | Skin type or visual risk areas (you may select mor... |
| Q07 | - |  |  | SI | Continence |
| Q08 | - |  |  | SI | Mobility (you may select more than one response) |
| Q09 | - |  |  | SI | Has patient lost weight recently? |
| Q10 | - |  |  | SI | Weight loss score |
| Q11 | - |  |  | SI | Patient eating poorly or lack of appetite |
| Q12 | - |  |  | SI | Patient eating poorly or lack of appetite |
| Q13 | - |  |  | SI | Diabetes, Multiple Sclerosis (MS), Cerebrovascular... |
| Q14 | - |  |  | SI | Motor / Sensory	 |
| Q15 | - |  |  | SI | Paraplegia |
| Q16 | - |  |  | SI | Neurological Deficit |
| Q17 | - |  |  | SI | More than one option can be selected against the f... |
| Q18 | - |  |  | SI | Scores can be discounted after 48h provided patien... |
| Q19 | - |  |  | SI | Malnutrition Screening Tool (MST). If < 2 refer fo... |
| Q20 | - |  |  | SI | If < 2 refer for nutrition assessment / interventi... |
| Q21 | - |  |  | SI | The Waterlow Score was originally described in 198... |
| Q22 | - |  |  | SI | References |
| Q23 | - |  |  | SI | 1. Waterlow J. Pressure sores: a risk assessment c... |
| Q24 | - |  |  | SI | 2. Waterlow J. From costly treatment to cost-effec... |
| Q25 | - |  |  | SI | 3. Ferguson M, Capra S, Bauer J, Banks M. Developm... |
| Q26 | - |  |  | SI | Waterlow score |
| Q27 | - |  |  | SI | MST score |
| Q28 | - |  |  | SI | The Waterlow score gives an estimated risk for the... |
| Q29 | - |  |  | SI | Malnutrition Screening Tool (MST) |
| Q30 | - |  |  | SI | Nutrition is an extremely important contributory f... |
| Q31 | - |  |  | SI | Terminal cachexia |
| Q32 | - |  |  | SI | Multiple organ failure |
| Q33 | - |  |  | SI | Single organ failure (respiratory, renal, cardiac) |
| Q34 | - |  |  | SI | Peripheral vascular disease |
| Q35 | - |  |  | SI | Anaemia (Hb <8 g/dL) |
| Q36 | - |  |  | SI | Smoking |
| Q37 | - |  |  | SI | Orthopaedic or spinal surgery |
| Q38 | - |  |  | SI | On table >2 hours (within last 48 hours) |
| Q39 | - |  |  | SI | On table >6 hours (within last 48 hours) |
| Q40 | - |  |  | SI | Is receiving cytotoxics, long-term or high-dose st... |
| Q41 | - |  |  | SI | Single organ failure (respiratory, renal, cardiac) |
| Q42 | - |  |  | SI | Patient eating poorly or lack of appetite |
| Q43 | - |  |  | SI | Build or weight-for-height |
| Q44 | - |  |  | SI | Patient eating poorly or lack of appetite |
| Q45 | - |  |  | SI | Patient eating poorly or lack of appetite |
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