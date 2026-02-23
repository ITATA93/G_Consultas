# SQLUser.MRC_HDRGroup

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HDRG_RowId | bigint | PK |  | NO | - |
| HDRG_Code | varchar |  |  | SI | Code |
| HDRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HDRG_DateFrom | date |  |  | SI | DateFrom |
| HDRG_DateTo | date |  |  | SI | DateTo |
| HDRG_Desc | varchar |  |  | SI | Description |
| HDRG_Owner | varchar |  |  | SI | Owner |
| Q01 | - |  |  | SI | No Informe |
| Q02 | - |  |  | SI | Denuncia Presentada En |
| Q03 | - |  |  | SI | Juzgado |
| Q04 | - |  |  | SI | Ciudad |
| Q05 | - |  |  | SI | ROL |
| Q06 | - |  |  | SI | Denuncia |
| Q07 | - |  |  | SI | Violacion |
| Q08 | - |  |  | SI | Abuso Sexual |
| Q09 | - |  |  | SI | Outros |
| Q10 | - |  |  | SI | Nombres |
| Q11 | - |  |  | SI | Apellido Materno |
| Q12 | - |  |  | SI | Apellido Paterno |
| Q13 | - |  |  | SI | Sexo |
| Q14 | - |  |  | SI | Edad (Años) |
| Q15 | - |  |  | SI | Edad (Meses) |
| Q16 | - |  |  | SI | Cedula de Identidad |
| Q17 | - |  |  | SI | Estado Civil |
| Q18 | - |  |  | SI | Nivel Educacional |
| Q19 | - |  |  | SI | Actvidad Laboral |
| Q20 | - |  |  | SI | Domicilio |
| Q21 | - |  |  | SI | Fecha Del Examen |
| Q22 | - |  |  | SI | Hora Del Examen |
| Q23 | - |  |  | SI | Fecha Despacho Informe ao Tribunal |
| Q24 | - |  |  | SI | Describir Brevemente la Agresión |
| Q25 | - |  |  | SI | Fecha del Delito |
| Q26 | - |  |  | SI | Hora del Delito |
| Q27 | - |  |  | SI | Dia Ocurrenia del Delito |
| Q28 | - |  |  | SI | El Autor de La Agresion Fue |
| Q29 | - |  |  | SI | Día de Ocurrencia del Delito |
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