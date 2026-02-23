# SQLUser.ARC_ItemProcActivity

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROCAC_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| PROCAC_Childsub | double |  |  | NO | Childsub |
| PROCAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROCAC_CreatedDate | date |  |  | SI | Created Date |
| PROCAC_CreatedTime | time |  |  | SI | Created Time |
| PROCAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROCAC_DateFrom | date |  |  | SI | Date From |
| PROCAC_DateTo | date |  |  | SI | Date To |
| PROCAC_ProcActivity_DR | bigint |  | FK | SI | Des Ref ProcActivity |
| PROCAC_RowId | varchar |  |  | NO | - |
| PROCAC_UpdatedDate | date |  |  | SI | Updated Date |
| PROCAC_UpdatedTime | time |  |  | SI | Updated Time |
| PROCAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Semejanzas (Conceptualización) |
| Q02 | - |  |  | SI | Respuesta Semejanzas |
| Q03 | - |  |  | SI | 2. Fluidez Léxica (Flexibilidad Mental) |
| Q04 | - |  |  | SI | Respuesta Fluidez Léxica |
| Q05 | - |  |  | SI | Detalle Fluidez Léxica |
| Q06 | - |  |  | SI | 3. Secuencias Motoras (Programación) |
| Q07 | - |  |  | SI | Respuesta Secuencias Motoras |
| Q08 | - |  |  | SI | 4. Instrucciones Conflictivas (Sensibilidad a la I... |
| Q09 | - |  |  | SI | Respuesta Instrucciones Conflictivas |
| Q10 | - |  |  | SI | 5. Go-no Go (Control Inhibitorio) |
| Q11 | - |  |  | SI | Respuesta Go-no Go |
| Q12 | - |  |  | SI | 6. Conducta de Prehensión (Autonomía del Ambiente) |
| Q13 | - |  |  | SI | Respuesta Conducta de Prehensión |
| Q14 | - |  |  | SI | Puntaje de corte es 13.5 |
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