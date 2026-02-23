# SQLUser.CT_PayrollClassification

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYCLS_RowId | bigint | PK |  | NO | - |
| PAYCLS_Code | varchar |  |  | NO | Code |
| PAYCLS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAYCLS_CreatedDate | date |  |  | SI | Created Date |
| PAYCLS_CreatedTime | time |  |  | SI | Created Time |
| PAYCLS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAYCLS_DateFrom | date |  |  | SI | Date From |
| PAYCLS_DateTo | date |  |  | SI | Date To |
| PAYCLS_Desc | varchar |  |  | NO | Description |
| PAYCLS_Owner | varchar |  |  | SI | Owner |
| PAYCLS_UpdatedDate | date |  |  | SI | Updated Date |
| PAYCLS_UpdatedTime | time |  |  | SI | Updated Time |
| PAYCLS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿Con qué frecuencia consume alguna bebida alcohóli... |
| Q02 | - |  |  | SI | ¿Cuántos TRAGOS de alcohol suele beber en un día d... |
| Q03 | - |  |  | SI | ¿Con qué frecuencia toma  5 o más TRAGOS en una so... |
| Q04 | - |  |  | SI | Resultado AUDITC |
| Q04ObsDR | - |  |  | SI | Resultado AUDITC DR |
| Q05 | - |  |  | SI | Sexo |
| Q06 | - |  |  | SI | Intervención Mínima |
| Q07 | - |  |  | SI | Intervenciones |
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