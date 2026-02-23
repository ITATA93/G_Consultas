# SQLUser.MRC_CancerClassification

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANCL_RowId | bigint | PK |  | NO | - |
| CANCL_Code | varchar |  |  | NO | Code |
| CANCL_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CANCL_CreatedDate | date |  |  | SI | Created Date |
| CANCL_CreatedTime | time |  |  | SI | Created Time |
| CANCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANCL_DateFrom | date |  |  | SI | Date From |
| CANCL_DateTo | date |  |  | SI | Date To |
| CANCL_Desc | varchar |  |  | NO | Description |
| CANCL_InternalCode | varchar |  |  | SI | Internal Code |
| CANCL_Owner | varchar |  |  | SI | Code Table Owner |
| CANCL_UpdatedDate | date |  |  | SI | Updated Date |
| CANCL_UpdatedTime | time |  |  | SI | Updated Time |
| CANCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CANCL_Version | varchar |  |  | SI | Version |
| Q01 | - |  |  | SI | Nombre de la Enfermera/Matrona |
| Q02 | - |  |  | SI | Manejo de la Cama |
| Q03 | - |  |  | SI | Localización del Baño |
| Q04 | - |  |  | SI | Horarios de  Comidas |
| Q05 | - |  |  | SI | Horario de Visitas |
| Q06 | - |  |  | SI | Nombre de quién recibe la Información |
| Q07 | - |  |  | SI | Comentario Nombre de la Enfermera/Matrona |
| Q08 | - |  |  | SI | Comentario Manejo de la Cama |
| Q09 | - |  |  | SI | Comentario Localización del Baño |
| Q10 | - |  |  | SI | Comentario Horarios de Comidas |
| Q11 | - |  |  | SI | Comentario Horario de Visitas |
| Q12 | - |  |  | SI | Uso del Timbre de llamado |
| Q13 | - |  |  | SI | Comentarios Uso del Timbre de Llmado |
| Q14 | - |  |  | SI | Sistemas de Monitorización y Equipos |
| Q15 | - |  |  | SI | Comentario Sistemas de Monitorización y Equipos |
| Q16 | - |  |  | SI | Profesional de Salud |
| Q17 | - |  |  | SI | Rutina del Servicio |
| Q18 | - |  |  | SI | Comentario Rutina del Servicio |
| Q19 | - |  |  | SI | Normas de Ingreso |
| Q20 | - |  |  | SI | Lactancia |
| Q21 | - |  |  | SI | Comentario Lactancia |
| Q22 | - |  |  | SI | Comentario Normas de Ingreso |
| Q23 | - |  |  | SI | Extracción de Leche |
| Q24 | - |  |  | SI | Comentario Extracción de Leche |
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