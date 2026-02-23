# SQLUser.MRC_SuppICD

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCSI_RowId | bigint | PK |  | NO | - |
| MRCSI_Code | varchar |  |  | NO | Supplementary ICD Code |
| MRCSI_CreatedDate | date |  |  | SI | Created Date |
| MRCSI_CreatedTime | time |  |  | SI | Created Time |
| MRCSI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRCSI_Desc | varchar |  |  | NO | Supplemenntary ICD Desc. |
| MRCSI_UpdatedDate | date |  |  | SI | Updated Date |
| MRCSI_UpdatedTime | time |  |  | SI | Updated Time |
| MRCSI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | Fecha ejecución |
| Q03 | - |  |  | SI | Hora Inicio |
| Q04 | - |  |  | SI | Hora término |
| Q05 | - |  |  | SI | Niveles Educacionales |
| Q06 | - |  |  | SI | Tipo de Profesional de la atención |
| Q07 | - |  |  | SI | N° Total Niñas atendidas |
| Q08 | - |  |  | SI | N° Total Niños atendidos |
| Q09 | - |  |  | SI | Observaciones de la atención grupal |
| Q10 | - |  |  | SI | Comentarios del establecimiento educacional |
| Q11 | - |  |  | SI | Nombre Usuario (logueado) |
| Q12 | - |  |  | SI | Establecimiento de Salud |
| Q13 | - |  |  | SI | Código Establecimiento de Salud |
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