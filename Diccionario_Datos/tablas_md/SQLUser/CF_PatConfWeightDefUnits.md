# SQLUser.CF_PatConfWeightDefUnits

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATCFWDU_RowId | bigint | PK |  | NO | - |
| PATCFWDU_AgeFrom | integer |  |  | SI | Age From |
| PATCFWDU_AgeTo | integer |  |  | SI | Age To |
| PATCFWDU_RefFrom | integer |  |  | SI | Reference Ranges From |
| PATCFWDU_RefTo | integer |  |  | SI | Reference Ranges To |
| PATCFWDU_UOM_DR | bigint |  | FK | SI | Default Unit |
| Q01 | - |  |  | SI | Tipo de Rescate |
| Q02 | - |  |  | SI | Detalle |
| Q03 | - |  |  | SI | Registro del Rescate |
| Q04 | - |  |  | SI | Acción |
| Q05 | - |  |  | SI | Resultado |
| Q06 | - |  |  | SI | Establecimiento |
| Q07 | - |  |  | SI | Tipo de Profesional |
| Q08 | - |  |  | SI | Rut Paciente |
| Q09 | - |  |  | SI | Nombre |
| Q10 | - |  |  | SI | Ap. Paterno |
| Q11 | - |  |  | SI | Ap. Materno |
| Q12 | - |  |  | SI | Edad |
| Q13 | - |  |  | SI | Programa de Salud |
| Q14 | - |  |  | SI | Profesional que Realizó Rescate (Llenar en caso de... |
| Q15 | - |  |  | SI | Rescate hecho por compra de servicios |
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