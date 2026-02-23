# questionnaire.QTCNAFLDS

> Non-alcoholic Fatty Liver Disease (NAFLD) Score

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Non-alcoholic Fatty Liver Disease (NAFLD) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Weight |
| Q03ObsDR | varchar |  | FK | SI | Weight DR |
| Q04 | varchar |  |  | SI | kg |
| Q05 | varchar |  |  | SI | Height |
| Q05ObsDR | varchar |  | FK | SI | Height DR |
| Q06 | varchar |  |  | SI | cm |
| Q07 | varchar |  |  | SI | BMI |
| Q08 | varchar |  |  | SI | Impaired fasting glucose or diabetes mellitus |
| Q09 | numeric |  |  | SI | Plasma AST concentration |
| Q10 | varchar |  |  | SI | U/L |
| Q11 | numeric |  |  | SI | Plasma ALT concentration |
| Q12 | varchar |  |  | SI | U/L |
| Q13 | numeric |  |  | SI | Platelet count |
| Q14 | numeric |  |  | SI | Albumin concentration |
| Q15 | varchar |  |  | SI | g/dL |
| Q16 | varchar |  |  | SI | NAFLD Score |
| Q17 | varchar |  |  | SI | NAFLD Score Interpretation |
| Q18 | varchar |  |  | SI | Advanced hepatic fibrosis = Stages 3 and 4 as desc... |
| Q19 | varchar |  |  | SI | Caution. |
| Q20 | varchar |  |  | SI | The negative predictive value of the lower thresho... |
| Q21 | varchar |  |  | SI | non-alcoholic fatty liver disease. |
| Q22 | varchar |  |  | SI | The prevalence of advanced fibrosis in the populat... |
| Q23 | varchar |  |  | SI | 1.Kleiner DE, Brunt EM, Van Natta M, Behling C, Co... |
| Q24 | varchar |  |  | SI | 2005;41(6):1313–21. |
| Q25 | varchar |  |  | SI | Low risk of advanced hepatic fibrosis (negative pr... |
| Q26 | varchar |  |  | SI | Indeterminate risk |
| Q27 | varchar |  |  | SI | High risk of advanced hepatic fibrosis (positive p... |
| Q28 | varchar |  |  | SI | Score |
| Q29 | varchar |  |  | SI | Interpretation |
| Q30 | varchar |  |  | SI | <-1.455 |
| Q31 | varchar |  |  | SI | Low risk of advanced hepatic fibrosis (negative pr... |
| Q32 | varchar |  |  | SI | ≥-1.455 to ≤0.676 |
| Q33 | varchar |  |  | SI | Indeterminate risk |
| Q34 | varchar |  |  | SI | >0.676 |
| Q35 | varchar |  |  | SI | 10 9/L |
| Q36 | varchar |  |  | SI | High risk of advanced hepatic fibrosis (positive p... |
| Q37 | varchar |  |  | SI | To determine the probability that a patient with n... |
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