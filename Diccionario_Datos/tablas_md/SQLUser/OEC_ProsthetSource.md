# SQLUser.OEC_ProsthetSource

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROSTSRC_RowId | bigint | PK |  | NO | - |
| PROSTSRC_Code | varchar |  |  | NO | Code |
| PROSTSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROSTSRC_CreatedDate | date |  |  | SI | Created Date |
| PROSTSRC_CreatedTime | time |  |  | SI | Created Time |
| PROSTSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROSTSRC_DateFrom | date |  |  | SI | DateFrom |
| PROSTSRC_DateTo | date |  |  | SI | DateTo |
| PROSTSRC_Desc | varchar |  |  | NO | Description |
| PROSTSRC_Owner | varchar |  |  | SI | Owner |
| PROSTSRC_UpdatedDate | date |  |  | SI | Updated Date |
| PROSTSRC_UpdatedTime | time |  |  | SI | Updated Time |
| PROSTSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Comprobación de Bomba y Jeringa |
| Q02 | - |  |  | SI | Comprobación de la Bomba |
| Q03 | - |  |  | SI | Cambio de Jeringa |
| Q04 | - |  |  | SI | Motivo |
| Q05 | - |  |  | SI | Cantidad Descartada |
| Q06 | - |  |  | SI | Cantidad UOM |
| Q07 | - |  |  | SI | Programa Cambiado |
| Q08 | - |  |  | SI | Motivo |
| Q10 | - |  |  | SI | Ingresó la cantidad descartada en el libro S8 |
| Q11 | - |  |  | SI | Comentarios |
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