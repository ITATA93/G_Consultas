# questionnaire.QTCAPRI

> AST to Platelet Ratio Index (APRI)

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* AST to Platelet Ratio Index (APRI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | AST concentration |
| Q04 | varchar |  |  | SI | IU/L |
| Q05 | numeric |  |  | SI | Upper limit of reference interval for AST concentr... |
| Q06 | varchar |  |  | SI | IU/L |
| Q07 | numeric |  |  | SI | Platelet count  |
| Q08 | varchar |  |  | SI | 10⁹/L |
| Q09 | varchar |  |  | SI | AST to Platelet Ratio Index (APRI) |
| Q10 | varchar |  |  | SI | The thresholds below are from [1]. |
| Q11 | varchar |  |  | SI | Score |
| Q12 | varchar |  |  | SI | Interpretation |
| Q13 | varchar |  |  | SI | <0.7 |
| Q14 | varchar |  |  | SI | Low risk of significant hepatic fibrosis (npv 79%) |
| Q15 | varchar |  |  | SI | ≥0.7 |
| Q16 | varchar |  |  | SI | High risk of significant hepatic fibrosis (ppv 70%... |
| Q17 | varchar |  |  | SI | Significant fibrosis = stage 2 to 4 by the criteri... |
| Q18 | varchar |  |  | SI | Score |
| Q19 | varchar |  |  | SI | Interpretation |
| Q20 | varchar |  |  | SI | <1 |
| Q21 | varchar |  |  | SI | Low risk of severe hepatic fibrosis (npv 81%) |
| Q22 | varchar |  |  | SI | ≥1 |
| Q23 | varchar |  |  | SI | High risk of severe hepatic fibrosis (ppv 40%) |
| Q24 | varchar |  |  | SI | Severe fibrosis = stage 3 to 4 by the criteria of ... |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Interpretation |
| Q27 | varchar |  |  | SI | <2 |
| Q28 | varchar |  |  | SI | Low risk of cirrhosis (npv 63%) |
| Q29 | varchar |  |  | SI | ≥2 |
| Q30 | varchar |  |  | SI | High risk of cirrhosis (ppv 82%) |
| Q31 | varchar |  |  | SI | Cirrhosis = stage 4 by the criteria of METAVIR [2]... |
| Q32 | varchar |  |  | SI | npv, negative predictive value |
| Q33 | varchar |  |  | SI | ppv, positive predictive value |
| Q34 | varchar |  |  | SI | Caution.  |
| Q35 | varchar |  |  | SI | The negative predictive and positive predictive va... |
| Q36 | varchar |  |  | SI | The combined prevalence of significant fibrosis, a... |
| Q37 | varchar |  |  | SI | 1. Lin Z-H, Xin Y-N, Dong Q-J, Wang Q, Jiang X-J, ... |
| Q38 | varchar |  |  | SI | An updated meta-analysis. Hepatology. 2011 Feb 11;... |
| Q39 | varchar |  |  | SI | 2. Intraobserver and interobserver variations in l... |
| Q40 | varchar |  |  | SI | 3. Batts KP, Ludwig J. Chronic hepatitis. An updat... |
| Q41 | varchar |  |  | SI | 4. Scheuer PJ. Classification of chronic viral hep... |
| Q42 | varchar |  |  | SI | 5. Ishak K, Baptista A, Bianchi L, Callea F, De Gr... |
| Q43 | varchar |  |  | SI | Please find the details of the score interpretatio... |
| Q44 | varchar |  |  | SI | To determine the probability that a patient with c... |
| Q45 | varchar |  |  | SI | Please find the details of the score interpretatio... |
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