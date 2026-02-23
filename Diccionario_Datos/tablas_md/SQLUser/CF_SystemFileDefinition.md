# SQLUser.CF_SystemFileDefinition

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FILE_RowId | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Administración de Medicamentos |
| FILE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FILE_Counter | double |  |  | SI | Counter |
| FILE_Desc | varchar |  |  | NO | Description |
| FILE_FileExtension | varchar |  |  | SI | File Extension |
| FILE_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| FILE_LabelPrefix | varchar |  |  | SI | Label Prefix |
| FILE_NewCounter | double |  |  | SI | New Counter |
| FILE_Owner | varchar |  |  | SI | Owner |
| FILE_Type | varchar |  |  | NO | Type |
| FILE_VirtualDirectory | varchar |  |  | SI | WEB Server Virtual Directory |
| Q01 | - |  |  | SI | Procedimiento Endoscópico |
| Q02 | - |  |  | SI | Detalles Procedimiento / Cirugía Menor a Realizar |
| Q03 | - |  |  | SI | Especialidad |
| Q04 | - |  |  | SI | Hora Inicio Programada |
| Q05 | - |  |  | SI | Hora Inicio Real |
| Q06 | - |  |  | SI | Hora Término |
| Q07 | - |  |  | SI | Paciente Acompañado |
| Q08 | - |  |  | SI | Nº Frascos |
| Q09 | - |  |  | SI | Test de Ureasa |
| Q10 | - |  |  | SI | Test de Lactasa |
| Q11 | - |  |  | SI | Comentarios |
| Q12 | - |  |  | SI | Comentarios |
| Q13 | - |  |  | SI | Otros Exámenes |
| Q14 | - |  |  | SI | Comentarios |
| Q15 | - |  |  | SI | Observaciones / Comentarios |
| Q16 | - |  |  | SI | Especialidad Cirugía / Procedimento |
| Q17 | - |  |  | SI | Biopsia |
| Q18 | - |  |  | SI | N° de Serie Equipo |
| Q19 | - |  |  | SI | Test de Fuga |
| Q20 | - |  |  | SI | Comentarios |
| Q22 | - |  |  | SI | Consulte la vista completa del Registro Procedimie... |
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