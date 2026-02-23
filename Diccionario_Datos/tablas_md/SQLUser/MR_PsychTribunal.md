# SQLUser.MR_PsychTribunal

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRIB_ParRef | varchar | PK |  | NO | MR_PsychDetails Parent Reference |
| ChildQ33DR | - |  |  | SI | Child Reference: CUSTOM PROTOCOL |
| Q01 | - |  |  | SI | Insulin Type |
| Q02 | - |  |  | SI | Brand: |
| Q03 | - |  |  | SI | Brand: |
| Q04 | - |  |  | SI | Name: |
| Q05 | - |  |  | SI | If Glucose Level is lower than 3.33 mmol/L (60 mg/... |
| Q06 | - |  |  | SI | If Glucose Level is equal to or higher than 18.1 m... |
| Q07 | - |  |  | SI | If potassium is lower than 3,5 mEq/L, Call M.D. |
| Q08 | - |  |  | SI | Frequency of cheking: |
| Q09 | - |  |  | SI | Type of Protocol: |
| Q10 | - |  |  | SI | BG (mmol/L) |
| Q11 | - |  |  | SI | Dose (Units) |
| Q12 | - |  |  | SI | 00.0 - 04.0 mmol/L |
| Q13 | - |  |  | SI | 04.1 - 06.9 mmol/L |
| Q14 | - |  |  | SI | 07.0 - 09.7 mmol/L |
| Q15 | - |  |  | SI | 09.8 - 12.4 mmol/L |
| Q16 | - |  |  | SI | 12.5 - 15.3 mmol/L |
| Q17 | - |  |  | SI | 15.4 - 18.0 mmol/L |
| Q18 | - |  |  | SI | ≥ 18.1 mmol/L |
| Q19 | - |  |  | SI | 0 Units |
| Q20 | - |  |  | SI | 2 Units |
| Q21 | - |  |  | SI | 3 Units |
| Q22 | - |  |  | SI | 4 Units |
| Q23 | - |  |  | SI | 5 Units |
| Q24 | - |  |  | SI | 7 Units |
| Q25 | - |  |  | SI | Call M.D. |
| Q26 | - |  |  | SI | 00.0 - 04.0 mmol/L |
| Q27 | - |  |  | SI | 04.1 - 06.9 mmol/L |
| Q28 | - |  |  | SI | 07.0 - 09.7 mmol/L |
| Q29 | - |  |  | SI | 09.8 - 12.4 mmol/L |
| Q30 | - |  |  | SI | 12.5 - 15.3 mmol/L |
| Q31 | - |  |  | SI | 15.4 - 18.0 mmol/L |
| Q32 | - |  |  | SI | Frequency of Checking: Before Breakfast, Before Lu... |
| Q34 | - |  |  | SI | Notes: |
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
| TRIB_AppealStatus | varchar |  |  | SI | AppealStatus |
| TRIB_AppealType_DR | varchar |  | FK | SI | Des Ref AppealType |
| TRIB_Appeal_DR | bigint |  | FK | SI | Des Ref Appeal |
| TRIB_Applicant_DR | bigint |  | FK | SI | Des Ref Applicant |
| TRIB_Childsub | double |  |  | NO | Childsub |
| TRIB_CoOrdinator | varchar |  |  | SI | CoOrdinator |
| TRIB_Comments | varchar |  |  | SI | Comments |
| TRIB_DateHearing | date |  |  | SI | DateHearing |
| TRIB_DateMedical | date |  |  | SI | DateMedical |
| TRIB_DateNrsReport | date |  |  | SI | DateNrsReport |
| TRIB_DateReferral | date |  |  | SI | DateReferral |
| TRIB_DateReport | date |  |  | SI | DateReport |
| TRIB_DateSocial | date |  |  | SI | DateSocial |
| TRIB_DateStatement | date |  |  | SI | DateStatement |
| TRIB_DateSubReport | date |  |  | SI | DateSubReport |
| TRIB_Decision_DR | bigint |  | FK | SI | Des Ref Decision |
| TRIB_PatAttend | varchar |  |  | SI | PatAttend |
| TRIB_ReportSent | varchar |  |  | SI | ReportSent |
| TRIB_RowId | varchar |  |  | NO | - |
| TRIB_Solicitor | varchar |  |  | SI | Solicitor |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*