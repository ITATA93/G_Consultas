# questionnaire.QTCPNRSTS

> Paediatric Nutritional Risk Screening Tool (STRONG kids)

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Paediatric Nutritional Risk Screening Tool (STRONG kids)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Assess the following items < 24h after admission a... |
| Q04 | varchar |  |  | SI | 1. Is there an underlying illness with risk for ma... |
| Q05 | varchar |  |  | SI | Diseases with risk of malnutrition |
| Q06 | varchar |  |  | SI | Use this list to answer Question 1. |
| Q07 | varchar |  |  | SI | It is optional to indicate which values are applic... |
| Q08 | varchar |  |  | SI | 2. Is the patient in a poor nutritional status jud... |
| Q09 | varchar |  |  | SI | 3. Is one of the following items present? |
| Q10 | varchar |  |  | SI | • Excessive diarrhea (≥5 per day) and/or vomiting ... |
| Q11 | varchar |  |  | SI | • Reduced food intake during the last 1-3 days |
| Q12 | varchar |  |  | SI | • Pre-existing nutritional intervention (e.g. ONS ... |
| Q13 | varchar |  |  | SI | • Inability to consume adequate nutritional intake... |
| Q14 | varchar |  |  | SI | 4. Is there weight loss (all ages) and/or no incre... |
| Q15 | varchar |  |  | SI | 4 - 5: High Risk |
| Q16 | varchar |  |  | SI | • Consult doctor and dietician for full diagnosis ... |
| Q17 | varchar |  |  | SI | • Check weight twice a week and evaluate nutrition... |
| Q18 | varchar |  |  | SI | • Evaluate the nutritional risk weekly |
| Q19 | varchar |  |  | SI | 1 - 3: Medium Risk |
| Q20 | varchar |  |  | SI | • Consider nutritional intervention |
| Q21 | varchar |  |  | SI | • Check weight twice a week |
| Q22 | varchar |  |  | SI | • Evaluate the nutritional risk weekly |
| Q23 | varchar |  |  | SI | 0: Low Risk |
| Q24 | varchar |  |  | SI | • No nutritional intervention necessary |
| Q25 | varchar |  |  | SI | • Check weight regularly (according to hospital po... |
| Q26 | varchar |  |  | SI | • Evaluate the nutritional risk weekly |
| Q27 | varchar |  |  | SI | List to item 1: Diseases with risk of malnutrition |
| Q28 | varchar |  |  | SI | It is optional to indicate which values are applic... |
| Q29 | varchar |  |  | SI | Score |
| Q30 | varchar |  |  | SI | Classification |
| Q31 | varchar |  |  | SI | 0 |
| Q32 | varchar |  |  | SI | Low Risk |
| Q33 | varchar |  |  | SI | 1 - 3 |
| Q34 | varchar |  |  | SI | Medium Risk |
| Q35 | varchar |  |  | SI | 4 - 5 |
| Q36 | varchar |  |  | SI | High Risk |
| Q37 | varchar |  |  | SI | 0: Low Risk |
| Q38 | varchar |  |  | SI | 1 - 3: Medium Risk |
| Q39 | varchar |  |  | SI | 4 - 5: High Risk |
| Q40 | varchar |  |  | SI | The STRONG kids is a nutritional risk screening to... |
| Q41 | varchar |  |  | SI | Please indicate which ones |
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