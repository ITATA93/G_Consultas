# SQLUser.PAC_RefugeeStatus

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFUGST_RowId | bigint | PK |  | NO | - |
| ChildQ05DR | - |  |  | SI | Child Reference: Last formula milk intake |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q06 | - |  |  | SI | Fasting times based on age on day of surgery |
| Q07 | - |  |  | SI | 6 months and under |
| Q08 | - |  |  | SI | Solids: 6 hours |
| Q09 | - |  |  | SI | Formula milk: 4 hours |
| Q10 | - |  |  | SI | Breast milk: 3 hours |
| Q11 | - |  |  | SI | Clear fluids: 1 hour |
| Q12 | - |  |  | SI | 7 months - 16 years |
| Q13 | - |  |  | SI | Solids: 6 hours |
| Q14 | - |  |  | SI | All milks: 6 hours |
| Q15 | - |  |  | SI | Clear fluids: 1 hour |
| Q16 | - |  |  | SI | 17 years and over |
| Q17 | - |  |  | SI | Solids: 6 hours |
| Q18 | - |  |  | SI | All milks: 6 hours |
| Q19 | - |  |  | SI | Clear fluids: 2 hours |
| Q20 | - |  |  | SI | This guide refers to time preceding anaesthesia th... |
| Q21 | - |  |  | SI | Include milk-containing drinks, white coffee, whit... |
| Q22 | - |  |  | SI | Include water, pulp-free fruit juice, clear oral r... |
| Q23 | - |  |  | SI | Paediatric patients ≤16 years may have no more tha... |
| Q24 | - |  |  | SI | Should be discouraged. If swallowed, a 6 hour fast... |
| Q25 | - |  |  | SI | May be taken with a sip of water less than 2 hours... |
| Q26 | - |  |  | SI | These fasting guidelines may not apply to patient ... |
| Q27 | - |  |  | SI | This includes patients having emergency procedures... |
| Q28 | - |  |  | SI | Patients who have had bariatric surgery (in partic... |
| Q30 | - |  |  | SI | Solids |
| Q31 | - |  |  | SI | Clear fluids |
| Q32 | - |  |  | SI | Chewing gum |
| Q33 | - |  |  | SI | Prescribed medications |
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
| REFUGST_Code | varchar |  |  | NO | Code |
| REFUGST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFUGST_CreatedDate | date |  |  | SI | Created Date |
| REFUGST_CreatedTime | time |  |  | SI | Created Time |
| REFUGST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFUGST_DateFrom | date |  |  | SI | Date From |
| REFUGST_DateTo | date |  |  | SI | Date To |
| REFUGST_Desc | varchar |  |  | NO | Description |
| REFUGST_Owner | varchar |  |  | SI | Owner |
| REFUGST_UpdatedDate | date |  |  | SI | Updated Date |
| REFUGST_UpdatedTime | time |  |  | SI | Updated Time |
| REFUGST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*