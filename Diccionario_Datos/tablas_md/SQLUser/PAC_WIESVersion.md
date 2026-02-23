# SQLUser.PAC_WIESVersion

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WIESV_RowId | bigint | PK |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | I wish I could have more respect for myself. |
| Q11 | - |  |  | SI | All in all, I am inclined to feel that I am a fail... |
| Q12 | - |  |  | SI | I take a positive attitude toward myself. |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification |
| Q15 | - |  |  | SI | 0 - 30 |
| Q16 | - |  |  | SI | A higher score implies better self esteem |
| Q17 | - |  |  | SI | 0 - 30:A higher score implies better self esteem |
| Q18 | - |  |  | SI | The scale is a ten item Likert scale with items an... |
| Q19 | - |  |  | SI | The original sample for which the scale was develo... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | 30 |
| Q21 | - |  |  | SI | High level of self esteem |
| Q3 | - |  |  | SI | On the whole, I am satisfied with myself |
| Q4 | - |  |  | SI | At times, I think I am no good at all. |
| Q5 | - |  |  | SI | I feel that I have a number of good qualities. |
| Q6 | - |  |  | SI | I am able to do things as well as most other peopl... |
| Q7 | - |  |  | SI | I feel I do not have much to be proud of. |
| Q8 | - |  |  | SI | I certainly feel useless at times |
| Q9 | - |  |  | SI | I feel that Im a person of worth, at least on an e... |
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
| WIESV_CareType | varchar |  |  | SI | CareType |
| WIESV_Code | varchar |  |  | NO | Code |
| WIESV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WIESV_ContractRole | varchar |  |  | SI | Contract Role |
| WIESV_CreatedDate | date |  |  | SI | Created Date |
| WIESV_CreatedTime | time |  |  | SI | Created Time |
| WIESV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WIESV_DRG | varchar |  |  | SI | DRG |
| WIESV_DateFrom | date |  |  | SI | Date From |
| WIESV_DateTo | date |  |  | SI | Date To |
| WIESV_Desc | varchar |  |  | NO | Description |
| WIESV_Owner | varchar |  |  | SI | Owner |
| WIESV_ProgramFundSource | varchar |  |  | SI | Program Fund Source |
| WIESV_UpdatedDate | date |  |  | SI | Updated Date |
| WIESV_UpdatedTime | time |  |  | SI | Updated Time |
| WIESV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*