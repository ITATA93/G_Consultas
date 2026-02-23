# SQLUser.CMC_BankMas

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Gestión de Casos**. Parámetros de case management.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CMCBM_RowId | bigint | PK |  | NO | - |
| CMCBM_Code | varchar |  |  | NO | Bank Master Code |
| CMCBM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CMCBM_Comp_DR | bigint |  | FK | SI | Des Ref to CTCO |
| CMCBM_CreatedDate | date |  |  | SI | Created Date |
| CMCBM_CreatedTime | time |  |  | SI | Created Time |
| CMCBM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CMCBM_DateFrom | date |  |  | SI | Date From |
| CMCBM_DateTo | date |  |  | SI | Date To |
| CMCBM_Desc | varchar |  |  | NO | Bank Master Description |
| CMCBM_Owner | varchar |  |  | SI | Owner |
| CMCBM_RcFlag | varchar |  |  | SI | Archived Flag |
| CMCBM_UpdatedDate | date |  |  | SI | Updated Date |
| CMCBM_UpdatedTime | time |  |  | SI | Updated Time |
| CMCBM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Calculador Utilizado |
| Q02 | - |  |  | SI | Otro (Texto libre) |
| Q03 | - |  |  | SI | Descripción 1 |
| Q04 | - |  |  | SI | Descripción 2 |
| Q05 | - |  |  | SI | Descripción 3 |
| Q06 | - |  |  | SI | Resultado 1 |
| Q07 | - |  |  | SI | Resultado 2 |
| Q08 | - |  |  | SI | Resultado 3 |
| Q09 | - |  |  | SI | Interpretación / Comentarios |
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