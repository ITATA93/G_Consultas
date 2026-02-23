# SQLUser.ARC_RemittanceAdviceStatus

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REMADVST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Nombre Paciente |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | Edad del Paciente |
| Q05 | - |  |  | SI | RUN |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Teléfono Contacto |
| Q08 | - |  |  | SI | Tutor Legal |
| Q09 | - |  |  | SI | Motivo de Consulta |
| Q10 | - |  |  | SI | Descripción situación que genera la Hospitalizació... |
| Q11 | - |  |  | SI | Examen Mental al Ingreso |
| Q12 | - |  |  | SI | Diagnóstico |
| Q13 | - |  |  | SI | Lista de Diagnóstico |
| Q14 | - |  |  | SI | Riesgo Conducta autolesivas |
| Q15 | - |  |  | SI | Riesgo Conducta Heteroagresiva |
| Q16 | - |  |  | SI | Riesgo de Abandono |
| Q16a | - |  |  | SI | Indicaciones |
| Q17 | - |  |  | SI | Fecha Ingreso |
| Q18 | - |  |  | SI | Hora Ingreso |
| Q19 | - |  |  | SI | Profesional |
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
| REMADVST_AllowModified | varchar |  |  | SI | Allow Modified |
| REMADVST_Code | varchar |  |  | NO | Code |
| REMADVST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REMADVST_CreatedDate | date |  |  | SI | Created Date |
| REMADVST_CreatedTime | time |  |  | SI | Created Time |
| REMADVST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REMADVST_DateFrom | date |  |  | SI | Date From |
| REMADVST_DateTo | date |  |  | SI | Date To |
| REMADVST_Desc | varchar |  |  | NO | Description |
| REMADVST_Initial | varchar |  |  | SI | Initial |
| REMADVST_Owner | varchar |  |  | SI | Owner |
| REMADVST_Process | varchar |  |  | SI | Process |
| REMADVST_UpdatedDate | date |  |  | SI | Updated Date |
| REMADVST_UpdatedTime | time |  |  | SI | Updated Time |
| REMADVST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*