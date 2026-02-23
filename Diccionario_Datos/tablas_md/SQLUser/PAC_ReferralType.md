# SQLUser.PAC_ReferralType

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Staff introductions made |
| Q02 | - |  |  | SI | Medication history |
| Q03 | - |  |  | SI | Add to clinical documentation of Medication Histor... |
| Q04 | - |  |  | SI | Any changes to medication |
| Q05 | - |  |  | SI | Add to clinical documentation of Current Medicatio... |
| Q06 | - |  |  | SI | Notes |
| Q07 | - |  |  | SI | Health problems |
| Q08 | - |  |  | SI | Add to clinical documentation of Problems |
| Q09 | - |  |  | SI | Any concerns / safeguarding issues |
| Q10 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Do you experience any of the following |
| Q12 | - |  |  | SI | Discussed appropriateness of continued ring pessar... |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Vaginal epithelium intact |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Pessary re-fitted |
| Q17 | - |  |  | SI | Add pessary type to clinical documentation of Proc... |
| Q18 | - |  |  | SI | Notes |
| Q19 | - |  |  | SI | Pessary size |
| Q20 | - |  |  | SI | Pessary lot no |
| Q21 | - |  |  | SI | Notes |
| Q22 | - |  |  | SI | Chaperone |
| Q23 | - |  |  | SI | Notes |
| Q24 | - |  |  | SI | Medication history |
| Q25 | - |  |  | SI | Please ensure you add any relevant medication hist... |
| Q26 | - |  |  | SI | Any changes to medication |
| Q27 | - |  |  | SI | Please ensure you add any relevant medication to t... |
| Q28 | - |  |  | SI | Health problems |
| Q29 | - |  |  | SI | Please ensure you add any relevant past medical hi... |
| Q30 | - |  |  | SI | Pessary re-fitted |
| Q31 | - |  |  | SI | Please ensure you add any relevant pessary type to... |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
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
| REFT_Code | varchar |  |  | NO | Code |
| REFT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFT_CreatedDate | date |  |  | SI | Created Date |
| REFT_CreatedTime | time |  |  | SI | Created Time |
| REFT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFT_DateFrom | date |  |  | SI | Date From |
| REFT_DateTo | date |  |  | SI | Date To |
| REFT_Desc | varchar |  |  | NO | Description |
| REFT_NationalCode | varchar |  |  | SI | National Code |
| REFT_Owner | varchar |  |  | SI | Owner |
| REFT_RefStDateApptDate | varchar |  |  | SI | RefStDateApptDate |
| REFT_ReferralLength | double |  |  | SI | ReferralLength |
| REFT_ReferralPeriod | varchar |  |  | SI | ReferralPeriod |
| REFT_Subregion_DR | bigint |  | FK | SI | Subregion  |
| REFT_UpdatedDate | date |  |  | SI | Updated Date |
| REFT_UpdatedTime | time |  |  | SI | Updated Time |
| REFT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*