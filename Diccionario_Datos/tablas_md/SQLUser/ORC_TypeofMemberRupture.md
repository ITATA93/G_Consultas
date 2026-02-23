# SQLUser.ORC_TypeofMemberRupture

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TYOFME_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Procedure start |
| Q04 | - |  |  | SI | Procedure start time |
| Q05 | - |  |  | SI | Procedure |
| Q06 | - |  |  | SI | Procedure note |
| Q07 | - |  |  | SI | Consent recorded |
| Q08 | - |  |  | SI | Consultant decision to proceed |
| Q09 | - |  |  | SI | Consent notes |
| Q10 | - |  |  | SI | Sedation |
| Q11 | - |  |  | SI | Sedation notes |
| Q12 | - |  |  | SI | Sedation clinician |
| Q13 | - |  |  | SI | Procedure end |
| Q14 | - |  |  | SI | Procedure end time |
| Q15 | - |  |  | SI | Procedure note |
| Q15TxtOnly | - |  |  | SI | Procedure note Plain Text Only |
| Q16 | - |  |  | SI | Ensure all orders are appropriately submitted |
| Q17 | - |  |  | SI | Post procedure follow up note |
| Q17TxtOnly | - |  |  | SI | Post procedure follow up note Plain Text Only |
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
| TYOFME_Code | varchar |  |  | NO | Code |
| TYOFME_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TYOFME_CreatedDate | date |  |  | SI | Created Date |
| TYOFME_CreatedTime | time |  |  | SI | Created Time |
| TYOFME_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TYOFME_DateFrom | date |  |  | SI | Date From |
| TYOFME_DateTo | date |  |  | SI | Date To |
| TYOFME_Desc | varchar |  |  | NO | Description |
| TYOFME_Owner | varchar |  |  | SI | Owner |
| TYOFME_UpdatedDate | date |  |  | SI | Updated Date |
| TYOFME_UpdatedTime | time |  |  | SI | Updated Time |
| TYOFME_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*