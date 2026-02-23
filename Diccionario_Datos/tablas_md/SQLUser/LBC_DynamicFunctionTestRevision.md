# SQLUser.LBC_DynamicFunctionTestRevision

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDFTR_RowID | bigint | PK |  | NO | - |
| LBCDFTR_AutoCloseTime | integer |  |  | SI | Time interval since DFT opened until it will be au... |
| LBCDFTR_Code | varchar |  |  | NO | Code |
| LBCDFTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDFTR_CreatedDate | date |  |  | SI | Created Date |
| LBCDFTR_CreatedTime | time |  |  | SI | Created Time |
| LBCDFTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDFTR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCDFTR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCDFTR_Desc | varchar |  |  | NO | Description |
| LBCDFTR_FooterText | longvarchar |  |  | SI | Layout Footer Text
The text to appear below the t... |
| LBCDFTR_HeaderText | longvarchar |  |  | SI | Layout Header Text
The text to appear above the t... |
| LBCDFTR_Number | varchar |  |  | NO | Revision Number |
| LBCDFTR_Owner | varchar |  |  | SI | Owner |
| LBCDFTR_ParRef | bigint |  |  | SI | - |
| LBCDFTR_RepeatTime | integer |  |  | SI | Repeat time
Time is stored in seconds |
| LBCDFTR_RevisionCode | varchar |  |  | SI | Revision Code |
| LBCDFTR_RevisionDesc | varchar |  |  | SI | Revision Description |
| LBCDFTR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDFTR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDFTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Peso |
| Q01ObsDR | - |  |  | SI | Peso DR |
| Q02 | - |  |  | SI | Talla |
| Q02ObsDR | - |  |  | SI | Talla DR |
| Q03 | - |  |  | SI | Edad Gestacional |
| Q03ObsDR | - |  |  | SI | Edad Gestacional DR |
| Q04 | - |  |  | SI | Estado Nutricional Actual |
| Q05 | - |  |  | SI | Diagnóstico Nutricional |
| Q06 | - |  |  | SI | Observaciones |
| Q07 | - |  |  | SI | Estado Nutricional al Primer Control de Embarazo |
| Q08 | - |  |  | SI | Peso al Primer Control de Embarazo |
| Q08ObsDR | - |  |  | SI | Peso al Primer Control de Embarazo DR |
| Q09 | - |  |  | SI | Edad Gestacional al Primer Control de Embarazo |
| Q09ObsDR | - |  |  | SI | Edad Gestacional al Primer Control de Embarazo DR |
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