# questionnaire.QTCFIB4

> Fibrosis-4 (FIB-4) Score

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fibrosis-4 (FIB-4) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | AST |
| Q02 | varchar |  |  | SI | U/L |
| Q03 | numeric |  |  | SI | ALT |
| Q04 | varchar |  |  | SI | U/L |
| Q05 | numeric |  |  | SI | Platelet count |
| Q06 | varchar |  |  | SI | FIB-4 Score |
| Q07 | varchar |  |  | SI | Guidelines to Interpretation |
| Q08 | varchar |  |  | SI | FIB-4 Score |
| Q09 | varchar |  |  | SI | Western patients with HIV/HCV co-infection [1] |
| Q10 | varchar |  |  | SI | North American patients with non-alcoholic fatty l... |
| Q11 | varchar |  |  | SI | South Korean patients with chronic hepatitis B [3] |
| Q12 | varchar |  |  | SI | Low risk of significant hepatic fibrosis |
| Q13 | varchar |  |  | SI | <1.45 |
| Q14 | varchar |  |  | SI | (90% npv) |
| Q15 | varchar |  |  | SI | <1.3 |
| Q16 | varchar |  |  | SI | (90% npv) |
| Q17 | varchar |  |  | SI | <1.0 |
| Q18 | varchar |  |  | SI | (93% npv) |
| Q19 | varchar |  |  | SI | Indeterminate risk of significant hepatic fibrosis |
| Q20 | varchar |  |  | SI | ≥1.45 to ≤3.25 |
| Q21 | varchar |  |  | SI | ≥1.3 to ≤2.67 |
| Q22 | varchar |  |  | SI | ≥1.0 to ≤2.65 |
| Q23 | varchar |  |  | SI | High risk of significant hepatic fibrosis |
| Q24 | varchar |  |  | SI | >3.25 |
| Q25 | varchar |  |  | SI | (65% ppv) |
| Q26 | varchar |  |  | SI | >2.67 |
| Q27 | varchar |  |  | SI | (80% ppv) |
| Q28 | varchar |  |  | SI | >2.65 |
| Q29 | varchar |  |  | SI | (95% ppv) |
| Q30 | varchar |  |  | SI | Significant hepatic fibrosis = Ishak [4] stage 4 t... |
| Q31 | varchar |  |  | SI | npv, negative predictive value |
| Q32 | varchar |  |  | SI | ppv, positive predictive value |
| Q33 | date |  |  | SI | Date |
| Q34 | time |  |  | SI | Time |
| Q35 | varchar |  |  | SI | The cutoff values shown above are those from the o... |
| Q36 | varchar |  |  | SI | Subsequent studies [2, 3] have shown that cutoff v... |
| Q37 | varchar |  |  | SI | In interpreting the FIB-4 ensure that you are usin... |
| Q38 | varchar |  |  | SI | The Fibrosis-4 score helps to estimate the amount ... |
| Q39 | varchar |  |  | SI | 10 9/L |
| Q40 | varchar |  |  | SI | 1. Sterling RK, Lissen E, Clumeck N, Sola R, Corre... |
| Q41 | varchar |  |  | SI | Hepatology. 2006 Jun;43(6):1317–25. |
| Q42 | varchar |  |  | SI | 2. Shah AG, Lydecker A, Murray K, Tetri BN, Contos... |
| Q43 | varchar |  |  | SI | Clinical Gastroenterology and Hepatology. 2009 Oct... |
| Q44 | varchar |  |  | SI | 3. Kim BK, Kim DY, Park JY, Ahn SH, Chon CY, Kim J... |
| Q45 | varchar |  |  | SI | Liver International. 2010 Apr;30(4):546–53. |
| Q46 | varchar |  |  | SI | 4. Ishak K, Baptista A, Bianchi L, Callea F, De Gr... |
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