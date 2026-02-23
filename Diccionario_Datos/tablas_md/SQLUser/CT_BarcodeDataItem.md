# SQLUser.CT_BarcodeDataItem

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBDI_ParRef | bigint | PK |  | NO | Parent barcode system |
| CTBDI_BarcodeData_DR | bigint |  | FK | NO | Barcode Data |
| CTBDI_Barcode_DR | bigint |  | FK | SI | Contained Barcode |
| CTBDI_CodeTableTags | varchar |  |  | SI | List of code table tags |
| CTBDI_CreatedDate | date |  |  | SI | Created Date |
| CTBDI_CreatedTime | time |  |  | SI | Created Time |
| CTBDI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTBDI_EndPosition | numeric |  |  | SI | End Position |
| CTBDI_EntireBarcode | varchar |  |  | SI | Use entire barcode |
| CTBDI_RowID | varchar |  |  | NO | - |
| CTBDI_StartPosition | numeric |  |  | SI | Start Position |
| CTBDI_UpdatedDate | date |  |  | SI | Updated Date |
| CTBDI_UpdatedTime | time |  |  | SI | Updated Time |
| CTBDI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ02DR | - |  |  | SI | Child Reference: Lista de alumnos supervisados |
| Q01 | - |  |  | SI | Supervisado por |
| Q03 | - |  |  | SI | Tipo Profesional Filtro |
| Q04 | - |  |  | SI | Staff |
| Q05 | - |  |  | SI | Comentario |
| Q06 | - |  |  | SI | Flujo |
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