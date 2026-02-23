# SQLUser.OR_AnaestComplicationOther

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANACO_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANACO_Childsub | double |  |  | NO | Childsub |
| ANACO_RowId | varchar |  |  | NO | - |
| ANACO_Type_DR | bigint |  | FK | SI | Des Ref ORCAnaestComplications |
| Q01 | - |  |  | SI | AST |
| Q02 | - |  |  | SI | U/L |
| Q03 | - |  |  | SI | ALT |
| Q04 | - |  |  | SI | U/L |
| Q05 | - |  |  | SI | Platelet count |
| Q06 | - |  |  | SI | FIB-4 Score |
| Q07 | - |  |  | SI | Guidelines to Interpretation |
| Q08 | - |  |  | SI | FIB-4 Score |
| Q09 | - |  |  | SI | Western patients with HIV/HCV co-infection [1] |
| Q10 | - |  |  | SI | North American patients with non-alcoholic fatty l... |
| Q11 | - |  |  | SI | South Korean patients with chronic hepatitis B [3] |
| Q12 | - |  |  | SI | Low risk of significant hepatic fibrosis |
| Q13 | - |  |  | SI | <1.45 |
| Q14 | - |  |  | SI | (90% npv) |
| Q15 | - |  |  | SI | <1.3 |
| Q16 | - |  |  | SI | (90% npv) |
| Q17 | - |  |  | SI | <1.0 |
| Q18 | - |  |  | SI | (93% npv) |
| Q19 | - |  |  | SI | Indeterminate risk of significant hepatic fibrosis |
| Q20 | - |  |  | SI | ≥1.45 to ≤3.25 |
| Q21 | - |  |  | SI | ≥1.3 to ≤2.67 |
| Q22 | - |  |  | SI | ≥1.0 to ≤2.65 |
| Q23 | - |  |  | SI | High risk of significant hepatic fibrosis |
| Q24 | - |  |  | SI | >3.25 |
| Q25 | - |  |  | SI | (65% ppv) |
| Q26 | - |  |  | SI | >2.67 |
| Q27 | - |  |  | SI | (80% ppv) |
| Q28 | - |  |  | SI | >2.65 |
| Q29 | - |  |  | SI | (95% ppv) |
| Q30 | - |  |  | SI | Significant hepatic fibrosis = Ishak [4] stage 4 t... |
| Q31 | - |  |  | SI | npv, negative predictive value |
| Q32 | - |  |  | SI | ppv, positive predictive value |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Time |
| Q35 | - |  |  | SI | The cutoff values shown above are those from the o... |
| Q36 | - |  |  | SI | Subsequent studies [2, 3] have shown that cutoff v... |
| Q37 | - |  |  | SI | In interpreting the FIB-4 ensure that you are usin... |
| Q38 | - |  |  | SI | The Fibrosis-4 score helps to estimate the amount ... |
| Q39 | - |  |  | SI | 10 9/L |
| Q40 | - |  |  | SI | 1. Sterling RK, Lissen E, Clumeck N, Sola R, Corre... |
| Q41 | - |  |  | SI | Hepatology. 2006 Jun |
| Q42 | - |  |  | SI | 2. Shah AG, Lydecker A, Murray K, Tetri BN, Contos... |
| Q43 | - |  |  | SI | Clinical Gastroenterology and Hepatology. 2009 Oct... |
| Q44 | - |  |  | SI | 3. Kim BK, Kim DY, Park JY, Ahn SH, Chon CY, Kim J... |
| Q45 | - |  |  | SI | Liver International. 2010 Apr |
| Q46 | - |  |  | SI | 4. Ishak K, Baptista A, Bianchi L, Callea F, De Gr... |
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