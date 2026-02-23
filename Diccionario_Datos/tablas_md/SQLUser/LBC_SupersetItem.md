# SQLUser.LBC_SupersetItem

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSSI_ParRef | bigint | PK |  | NO | Parent Superset DR |
| LBCSSI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSSI_DateFrom | date |  |  | SI | Date From
Effective date for the record |
| LBCSSI_DateTo | date |  |  | SI | Date To
Last day the record is active  |
| LBCSSI_DefaultSelected | varchar |  |  | SI | Default Selected
It is used when allow user to se... |
| LBCSSI_RowID | varchar |  |  | NO | - |
| LBCSSI_TestSet_DR | bigint |  | FK | NO | Test Set |
| Q01 | - |  |  | SI | Nombre del Paciente |
| Q02 | - |  |  | SI | Procedente de |
| Q03 | - |  |  | SI | Fecha de notificación |
| Q04 | - |  |  | SI | Lugar de notificación |
| Q05 | - |  |  | SI | Fecha de inicio del tratamiento |
| Q06 | - |  |  | SI | Diagnóstico o tipo de Tuberculosis |
| Q07 | - |  |  | SI | Órgano |
| Q08 | - |  |  | SI | Confirmación de la TBC con |
| Q09 | - |  |  | SI | Antecedentes del tratamiento |
| Q10 | - |  |  | SI | Teléfono de Establecimiento que recepciona |
| Q11 | - |  |  | SI | Establecimiento que recepciona |
| Q12 | - |  |  | SI | Fecha de recepción del paciente |
| Q13 | - |  |  | SI | Probable fecha de alta |
| Q14 | - |  |  | SI | Enfermero(a) que recepciona |
| Q15 | - |  |  | SI | Apellido Paterno Paciente |
| Q16 | - |  |  | SI | Apellido Materno Paciente |
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