# SQLUser.CT_BarcodeDataItemMap

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBDIM_ParRef | varchar | PK |  | NO | Parent barcode data item |
| CTBDIM_BarcodeValue | varchar |  |  | NO | Barcode Value |
| CTBDIM_CodeTableTags | varchar |  |  | SI | List of code table tags |
| CTBDIM_CodeTableValue_DR | varchar |  | FK | SI | Code Table Value |
| CTBDIM_CreatedDate | date |  |  | SI | Created Date |
| CTBDIM_CreatedTime | time |  |  | SI | Created Time |
| CTBDIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTBDIM_RowID | varchar |  |  | NO | - |
| CTBDIM_UpdatedDate | date |  |  | SI | Updated Date |
| CTBDIM_UpdatedTime | time |  |  | SI | Updated Time |
| CTBDIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTBDIM_Value | varchar |  |  | SI | Value |
| Q01a | - |  |  | SI | Nombre |
| Q01b | - |  |  | SI | Apellido Paterno |
| Q01c | - |  |  | SI | Apellido Materno |
| Q02 | - |  |  | SI | RUN |
| Q03 | - |  |  | SI | Domicilio |
| Q04 | - |  |  | SI | Teléfono |
| Q05 | - |  |  | SI | Procedencia |
| Q06 | - |  |  | SI | Edad |
| Q07 | - |  |  | SI | Muestra |
| Q08 | - |  |  | SI | 1a |
| Q09 | - |  |  | SI | 2a |
| Q10 | - |  |  | SI | Especificar |
| Q11 | - |  |  | SI | Examen solicitado para |
| Q12 | - |  |  | SI | Mes |
| Q13 | - |  |  | SI | Identifique Grupos Vulnerables |
| Q14 | - |  |  | SI | Otro grupo (especificar) |
| Q15 | - |  |  | SI | Fecha de Solicitud |
| Q16 | - |  |  | SI | Identificación del Solicitante |
| Q19 | - |  |  | SI | Fecha de Nacimiento |
| Q20 | - |  |  | SI | Sexo |
| Q21 | - |  |  | SI | Establecimiento |
| Q22 | - |  |  | SI | Unidad |
| Q23 | - |  |  | SI | Local (ambulatorio) |
| Q24 | - |  |  | SI | Nacionalidad |
| Q25 | - |  |  | SI | N° Mes |
| Q26 | - |  |  | SI | Antecedentes de Tratamiento |
| Q27 | - |  |  | SI | Señale el Tipo de Muestra |
| Q28 | - |  |  | SI | Otros líquidos o tejidos (especificar): |
| Q29 | - |  |  | SI | Otras poblaciones cerradas (especificar): |
| Q30 | - |  |  | SI | Fecha de Toma de Muestra |
| Q31 | - |  |  | SI | Responsable de Toma de Muestra |
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