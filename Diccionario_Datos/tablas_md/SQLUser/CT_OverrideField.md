# SQLUser.CT_OverrideField

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLD_ParRef | bigint | PK |  | NO | - |
| FLD_Action | varchar |  |  | NO | Action Type
ADD: When adding new childs entries t... |
| FLD_LastUpdateDate | date |  |  | SI | Last Update Date |
| FLD_LastUpdateTime | time |  |  | SI | Last Update Time |
| FLD_OriginalValue | varchar |  |  | SI | Original Data from Edition/Core distribution
This... |
| FLD_PropertyClassName | varchar |  |  | SI | ClassName corresponding to the property
Only appl... |
| FLD_PropertyName | varchar |  |  | NO | Name of Property being overriden |
| FLD_PropertyRowID | varchar |  |  | SI | ID of the entry corresponding to the property
Onl... |
| FLD_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | AST concentration |
| Q04 | - |  |  | SI | IU/L |
| Q05 | - |  |  | SI | Upper limit of reference interval for AST concentr... |
| Q06 | - |  |  | SI | IU/L |
| Q07 | - |  |  | SI | Platelet count |
| Q08 | - |  |  | SI | 10⁹/L |
| Q09 | - |  |  | SI | AST to Platelet Ratio Index (APRI) |
| Q10 | - |  |  | SI | The thresholds below are from [1]. |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Interpretation |
| Q13 | - |  |  | SI | <0.7 |
| Q14 | - |  |  | SI | Low risk of significant hepatic fibrosis (npv 79%) |
| Q15 | - |  |  | SI | ≥0.7 |
| Q16 | - |  |  | SI | High risk of significant hepatic fibrosis (ppv 70%... |
| Q17 | - |  |  | SI | Significant fibrosis = stage 2 to 4 by the criteri... |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Interpretation |
| Q20 | - |  |  | SI | <1 |
| Q21 | - |  |  | SI | Low risk of severe hepatic fibrosis (npv 81%) |
| Q22 | - |  |  | SI | ≥1 |
| Q23 | - |  |  | SI | High risk of severe hepatic fibrosis (ppv 40%) |
| Q24 | - |  |  | SI | Severe fibrosis = stage 3 to 4 by the criteria of ... |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Interpretation |
| Q27 | - |  |  | SI | <2 |
| Q28 | - |  |  | SI | Low risk of cirrhosis (npv 63%) |
| Q29 | - |  |  | SI | ≥2 |
| Q30 | - |  |  | SI | High risk of cirrhosis (ppv 82%) |
| Q31 | - |  |  | SI | Cirrhosis = stage 4 by the criteria of METAVIR [2]... |
| Q32 | - |  |  | SI | npv, negative predictive value |
| Q33 | - |  |  | SI | ppv, positive predictive value |
| Q34 | - |  |  | SI | Caution. |
| Q35 | - |  |  | SI | The negative predictive and positive predictive va... |
| Q36 | - |  |  | SI | The combined prevalence of significant fibrosis, a... |
| Q37 | - |  |  | SI | 1. Lin Z-H, Xin Y-N, Dong Q-J, Wang Q, Jiang X-J, ... |
| Q38 | - |  |  | SI | An updated meta-analysis. Hepatology. 2011 Feb 11 |
| Q39 | - |  |  | SI | 2. Intraobserver and interobserver variations in l... |
| Q40 | - |  |  | SI | 3. Batts KP, Ludwig J. Chronic hepatitis. An updat... |
| Q41 | - |  |  | SI | 4. Scheuer PJ. Classification of chronic viral hep... |
| Q42 | - |  |  | SI | 5. Ishak K, Baptista A, Bianchi L, Callea F, De Gr... |
| Q43 | - |  |  | SI | Please find the details of the score interpretatio... |
| Q44 | - |  |  | SI | To determine the probability that a patient with c... |
| Q45 | - |  |  | SI | Please find the details of the score interpretatio... |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*