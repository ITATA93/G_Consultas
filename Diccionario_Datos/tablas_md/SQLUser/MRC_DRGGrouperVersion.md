# SQLUser.MRC_DRGGrouperVersion

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DGV_RowId | bigint | PK |  | NO | - |
| DGV_3MEncoderId | varchar |  |  | SI | 3M Encoder Identifier |
| DGV_BatchFile | varchar |  |  | SI | BatchFile |
| DGV_Code | varchar |  |  | NO | Code |
| DGV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DGV_CreatedDate | date |  |  | SI | Created Date |
| DGV_CreatedTime | time |  |  | SI | Created Time |
| DGV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DGV_DateFrom | date |  |  | SI | DateFrom |
| DGV_DateTo | date |  |  | SI | DateTo |
| DGV_Desc | varchar |  |  | NO | Description |
| DGV_Owner | varchar |  |  | SI | Owner |
| DGV_UpdatedDate | date |  |  | SI | Updated Date |
| DGV_UpdatedTime | time |  |  | SI | Updated Time |
| DGV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DGV_Version_DR | bigint |  | FK | SI | Des Ref Version |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | Código establecimiento de salud |
| Q03 | - |  |  | SI | Fecha de la Actividad |
| Q04 | - |  |  | SI | Cantidad de Hombres Asistentes |
| Q05 | - |  |  | SI | Cantidad de Mujeres Asistentes |
| Q06 | - |  |  | SI | Espacio / Instancia |
| Q07 | - |  |  | SI | Estrategias / Líneas de Acción |
| Q08 | - |  |  | SI | Tipo de Actividad |
| Q09 | - |  |  | SI | Tipo de Profesional que ejecuta la actividad |
| Q10 | - |  |  | SI | Comentarios |
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