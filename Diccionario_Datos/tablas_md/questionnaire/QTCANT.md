# questionnaire.QTCANT

> Adult Nutrition Tool (ANT)

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Adult Nutrition Tool (ANT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | 1. Do you think you have been eating enough food l... |
| Q04 | varchar |  |  | SI | 2. Do you think you have lost weight recently with... |
| Q05 | varchar |  |  | SI | Prompt: Ask the patient if they have been feeling ... |
| Q06 | varchar |  |  | SI | If Yes, how much weight do you think you have lost... |
| Q07 | varchar |  |  | SI | 3. Does the patient look frail or undernourished |
| Q08 | varchar |  |  | SI | Assess patient for signs of muscle wasting, poor s... |
| Q09 | varchar |  |  | SI | Reason for referral to dietitian |
| Q10 | varchar |  |  | SI | • Malnutrition (ANT score > 4) |
| Q11 | varchar |  |  | SI | • Enteral nutrition |
| Q12 | varchar |  |  | SI | • Parenteral nutrition |
| Q13 | varchar |  |  | SI | • Refeeding syndrome |
| Q14 | varchar |  |  | SI | • Burns > 10% |
| Q15 | varchar |  |  | SI | • Postoperative upper gastrointestinal (GI) surger... |
| Q16 | varchar |  |  | SI | • Severe life threatening food allergy |
| Q17 | varchar |  |  | SI | • Acute management of GI conditions e.g. Crohn’s, ... |
| Q18 | varchar |  |  | SI | • Pressure injuries |
| Q19 | varchar |  |  | SI | • Chronic disease requiring education e.g. new dia... |
| Q20 | varchar |  |  | SI | The Adult Nutrition Tool (ANT) is a validated tool... |
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