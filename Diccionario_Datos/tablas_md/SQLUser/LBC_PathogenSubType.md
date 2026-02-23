# SQLUser.LBC_PathogenSubType

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAST_ParRef | bigint | PK |  | NO | LBCPathogen Parent Reference |
| LBCPAST_Code | varchar |  |  | SI | Code |
| LBCPAST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAST_CreatedDate | date |  |  | SI | Created Date |
| LBCPAST_CreatedTime | time |  |  | SI | Created Time |
| LBCPAST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPAST_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAST_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAST_Desc | varchar |  |  | SI | Description |
| LBCPAST_OrganismSubTypeGroup_DR | bigint |  | FK | SI | OrganismSubTypeGroup |
| LBCPAST_RowID | varchar |  |  | NO | - |
| LBCPAST_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPAST_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPAST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (deprecado) |
| Q02 | - |  |  | SI | Fecha de Intervención |
| Q03 | - |  |  | SI | Hora de Inicio |
| Q04 | - |  |  | SI | Edad Paciente |
| Q05 | - |  |  | SI | Sexo Paciente |
| Q06 | - |  |  | SI | Paciente Beneficiario |
| Q07 | - |  |  | SI | Tipo de Móvil |
| Q08 | - |  |  | SI | Causas de la Intervención |
| Q09 | - |  |  | SI | Código Establecimiento |
| Q10 | - |  |  | SI | Tipo de Intervención |
| Q11 | - |  |  | SI | Tiempos de llegada ( en minutos) |
| QHR | - |  |  | SI | Establecimiento de Salud (código y descripción) |
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