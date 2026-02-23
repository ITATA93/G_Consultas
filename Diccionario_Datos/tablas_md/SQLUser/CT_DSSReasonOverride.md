# SQLUser.CT_DSSReasonOverride

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSSRFO_RowId | bigint | PK |  | NO | - |
| DSSRFO_Code | varchar |  |  | NO | Code |
| DSSRFO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSSRFO_CreatedDate | date |  |  | SI | Created Date |
| DSSRFO_CreatedTime | time |  |  | SI | Created Time |
| DSSRFO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSSRFO_DateFrom | date |  |  | SI | Date From |
| DSSRFO_DateTo | date |  |  | SI | Date To |
| DSSRFO_Desc | varchar |  |  | NO | Description |
| DSSRFO_Owner | varchar |  |  | SI | Owner |
| DSSRFO_UpdatedDate | date |  |  | SI | Updated Date |
| DSSRFO_UpdatedTime | time |  |  | SI | Updated Time |
| DSSRFO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edema Subglótico (Pseudosurco) |
| Q02 | - |  |  | SI | Obliteración del Ventrículo |
| Q03 | - |  |  | SI | Eritema / Hiperemia |
| Q04 | - |  |  | SI | Edema de Cuerda Vocal |
| Q05 | - |  |  | SI | Edema Laríngeo Difuso |
| Q06 | - |  |  | SI | Hipertrofia de Comisura Posterior |
| Q07 | - |  |  | SI | Granuloma / Tejido de Granulación |
| Q08 | - |  |  | SI | Moco Espeso Endofaríngeo |
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