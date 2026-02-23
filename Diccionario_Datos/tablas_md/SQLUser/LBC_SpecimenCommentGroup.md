# SQLUser.LBC_SpecimenCommentGroup

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSCG_RowID | bigint | PK |  | NO | - |
| LBCSCG_Code | varchar |  |  | SI | Code |
| LBCSCG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSCG_CreatedDate | date |  |  | SI | Created Date |
| LBCSCG_CreatedTime | time |  |  | SI | Created Time |
| LBCSCG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSCG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSCG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSCG_Desc | varchar |  |  | SI | Description |
| LBCSCG_Owner | varchar |  |  | SI | Owner |
| LBCSCG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSCG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSCG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Muestra de |
| Q02 | - |  |  | SI | Fecha Envío |
| Q03 | - |  |  | SI | N° de Ficha |
| Q04 | - |  |  | SI | N° de Bolsa |
| Q05 | - |  |  | SI | Apellido Paterno |
| Q06 | - |  |  | SI | Apellido Materno |
| Q07 | - |  |  | SI | Nombre del Paciente |
| Q08 | - |  |  | SI | RUT |
| Q09 | - |  |  | SI | Fecha de Nacimiento |
| Q10 | - |  |  | SI | Sexo |
| Q11 | - |  |  | SI | Teléfono |
| Q12 | - |  |  | SI | Dirección |
| Q13 | - |  |  | SI | Profesional Responsable |
| Q14 | - |  |  | SI | Establecimiento |
| Q15 | - |  |  | SI | Dirección |
| Q16 | - |  |  | SI | Ciudad |
| Q17 | - |  |  | SI | Fax |
| Q18 | - |  |  | SI | Teléfono |
| Q19 | - |  |  | SI | Servicio |
| Q20 | - |  |  | SI | Mail |
| Q21 | - |  |  | SI | Tipo de Muestra |
| Q22 | - |  |  | SI | Fecha Obtención |
| Q23 | - |  |  | SI | Hora Obtención |
| Q24 | - |  |  | SI | Previsión |
| Q25 | - |  |  | SI | Técnica Realizada |
| Q27 | - |  |  | SI | Otra (indique) |
| Q28 | - |  |  | SI | Lectura |
| Q29 | - |  |  | SI | Punto Corte |
| Q31 | - |  |  | SI | Lote |
| Q32 | - |  |  | SI | Antecedentes Clínicos/Epidemiológicos |
| Q33 | - |  |  | SI | Fecha Envío |
| Q34 | - |  |  | SI | Resultado |
| Q35 | - |  |  | SI | Marca Comercial |
| Q36 | - |  |  | SI | Edad |
| Q37 | - |  |  | SI | Tipo de Muestra |
| Q38 | - |  |  | SI | Técnica Realizada |
| Q39 | - |  |  | SI | Resultado |
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