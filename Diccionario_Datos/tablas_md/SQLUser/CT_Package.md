# SQLUser.CT_Package

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKG_RowId | bigint | PK |  | NO | - |
| PKG_Code | varchar |  |  | NO | Code |
| PKG_CreatedDate | date |  |  | SI | Created Date |
| PKG_CreatedTime | time |  |  | SI | Created Time |
| PKG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKG_Desc | varchar |  |  | NO | Description |
| PKG_Excluded | bit |  |  | SI | Indicate if package is excluded from distribution |
| PKG_LastValidationResultMsg | varchar |  |  | SI | Last package validation status message |
| PKG_LicenseUnneeded | bit |  |  | SI | No license required |
| PKG_Owner | varchar |  |  | NO | Owner |
| PKG_Purpose | varchar |  |  | SI | Purpose |
| PKG_UpdatedDate | date |  |  | SI | Updated Date |
| PKG_UpdatedTime | time |  |  | SI | Updated Time |
| PKG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | codigo establecimiento de salud |
| Q03 | - |  |  | SI | RUN de quien Reclama |
| Q04 | - |  |  | SI | Sexo Paciente |
| Q05 | - |  |  | SI | Fecha de Reclamo |
| Q06 | - |  |  | SI | Fecha de Respuesta |
| Q07 | - |  |  | SI | Categoría de Reclamo |
| Q08 | - |  |  | SI | Comentarios |
| Q09 | - |  |  | SI | Paciente TRANS |
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