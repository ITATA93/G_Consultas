# SQLUser.PAC_LeaveType

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LEATYP_RowId | bigint | PK |  | NO | - |
| LEATYP_CCare | varchar |  |  | SI | CCare |
| LEATYP_Code | varchar |  |  | NO | Code |
| LEATYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LEATYP_CreatedDate | date |  |  | SI | Created Date |
| LEATYP_CreatedTime | time |  |  | SI | Created Time |
| LEATYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LEATYP_DateFrom | date |  |  | SI | Date From |
| LEATYP_DateTo | date |  |  | SI | Date To |
| LEATYP_Desc | varchar |  |  | NO | Description |
| LEATYP_Owner | varchar |  |  | SI | Owner |
| LEATYP_Psych | varchar |  |  | SI | [DEPRECATED]Replaced by mental health module in Tr... |
| LEATYP_UpdatedDate | date |  |  | SI | Updated Date |
| LEATYP_UpdatedTime | time |  |  | SI | Updated Time |
| LEATYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Weight |
| Q03ObsDR | - |  |  | SI | Weight DR |
| Q04 | - |  |  | SI | kg |
| Q05 | - |  |  | SI | Height |
| Q05ObsDR | - |  |  | SI | Height DR |
| Q06 | - |  |  | SI | cm |
| Q07 | - |  |  | SI | BMI |
| Q08 | - |  |  | SI | Impaired fasting glucose or diabetes mellitus |
| Q09 | - |  |  | SI | Plasma AST concentration |
| Q10 | - |  |  | SI | U/L |
| Q11 | - |  |  | SI | Plasma ALT concentration |
| Q12 | - |  |  | SI | U/L |
| Q13 | - |  |  | SI | Platelet count |
| Q14 | - |  |  | SI | Albumin concentration |
| Q15 | - |  |  | SI | g/dL |
| Q16 | - |  |  | SI | NAFLD Score |
| Q17 | - |  |  | SI | NAFLD Score Interpretation |
| Q18 | - |  |  | SI | Advanced hepatic fibrosis = Stages 3 and 4 as desc... |
| Q19 | - |  |  | SI | Caution. |
| Q20 | - |  |  | SI | The negative predictive value of the lower thresho... |
| Q21 | - |  |  | SI | non-alcoholic fatty liver disease. |
| Q22 | - |  |  | SI | The prevalence of advanced fibrosis in the populat... |
| Q23 | - |  |  | SI | 1.Kleiner DE, Brunt EM, Van Natta M, Behling C, Co... |
| Q24 | - |  |  | SI | 2005 |
| Q25 | - |  |  | SI | Low risk of advanced hepatic fibrosis (negative pr... |
| Q26 | - |  |  | SI | Indeterminate risk |
| Q27 | - |  |  | SI | High risk of advanced hepatic fibrosis (positive p... |
| Q28 | - |  |  | SI | Score |
| Q29 | - |  |  | SI | Interpretation |
| Q30 | - |  |  | SI | <-1.455 |
| Q31 | - |  |  | SI | Low risk of advanced hepatic fibrosis (negative pr... |
| Q32 | - |  |  | SI | ≥-1.455 to ≤0.676 |
| Q33 | - |  |  | SI | Indeterminate risk |
| Q34 | - |  |  | SI | >0.676 |
| Q35 | - |  |  | SI | 10 9/L |
| Q36 | - |  |  | SI | High risk of advanced hepatic fibrosis (positive p... |
| Q37 | - |  |  | SI | To determine the probability that a patient with n... |
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