# SQLUser.MRC_RiskParamCritEval

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVAL_ParRef | varchar | PK |  | NO | MRC_RiskEvalParamCriteria Parent Reference |
| EVAL_Childsub | double |  |  | NO | Childsub |
| EVAL_Code | varchar |  |  | NO | Code |
| EVAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EVAL_CreatedDate | date |  |  | SI | Created Date |
| EVAL_CreatedTime | time |  |  | SI | Created Time |
| EVAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EVAL_Desc | varchar |  |  | NO | Description |
| EVAL_RowId | varchar |  |  | NO | - |
| EVAL_UpdatedDate | date |  |  | SI | Updated Date |
| EVAL_UpdatedTime | time |  |  | SI | Updated Time |
| EVAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edad |
| Q02 | - |  |  | SI | Antecedentes de Caídas Previas |
| Q03 | - |  |  | SI | Antecedentes del Paciente |
| Q04 | - |  |  | SI | Compromiso de Conciencia |
| Q05 | - |  |  | SI | Grado |
| Q05ObsDR | - |  |  | SI | Grado DR |
| Q06 | - |  |  | SI | Etiqueta Alto riesgo |
| Q07 | - |  |  | SI | Etiqueta Mediano Riesgo |
| Q08 | - |  |  | SI | Etiqueta Bajo Riesgo |
| Q09 | - |  |  | SI | Información a familiar (Primer Contacto) |
| Q10 | - |  |  | SI | Fecha de información a familia |
| Q11 | - |  |  | SI | Aceptación de Medidas |
| Q12 | - |  |  | SI | Nombre del Familiar |
| Q13 | - |  |  | SI | Nombre Responsable |
| Q16 | - |  |  | SI | Antecedentes |
| Q17 | - |  |  | SI | Seleccionar Antecedentes |
| Q18 | - |  |  | SI | Se realizan medidas según riesgo evaluado |
| Q19 | - |  |  | SI | Razón de No Realización |
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