# SQLUser.CT_Barcode

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTB_RowID | bigint | PK |  | NO | - |
| CTB_BarcodeSystem_DR | bigint |  | FK | NO | Barcode System |
| CTB_CheckCharacterCalc_DR | bigint |  | FK | SI | Checksum Character Calculation |
| CTB_Code | varchar |  |  | NO | Code |
| CTB_CodeTableTags | varchar |  |  | SI | List of code table tags |
| CTB_CreatedDate | date |  |  | SI | Created Date |
| CTB_CreatedTime | time |  |  | SI | Created Time |
| CTB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTB_DataContentPrefix | varchar |  |  | SI | Data content prefix |
| CTB_DateFrom | date |  |  | SI | Effective date for the record |
| CTB_DateTo | date |  |  | SI | Last day the record is active |
| CTB_Desc | varchar |  |  | NO | Description |
| CTB_EndCode | varchar |  |  | SI | End Code |
| CTB_EndCodeOptional | varchar |  |  | SI | End Code Optional Flag
E.g. only used if barcode ... |
| CTB_NumberOfCharacters | numeric |  |  | SI | Number of characters between the start and end cod... |
| CTB_Owner | varchar |  |  | SI | Owner |
| CTB_StartCode | varchar |  |  | NO | Start Code |
| CTB_UpdatedDate | date |  |  | SI | Updated Date |
| CTB_UpdatedTime | time |  |  | SI | Updated Time |
| CTB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de Solicitud |
| Q02 | - |  |  | SI | Albúmina |
| Q03 | - |  |  | SI | Creatinina |
| Q04 | - |  |  | SI | VFG |
| Q05 | - |  |  | SI | Agente aislado |
| Q06 | - |  |  | SI | Cultivos tomados |
| Q07 | - |  |  | SI | Otro Cultivo |
| Q08 | - |  |  | SI | Indicación Médica |
| Q09 | - |  |  | SI | Tipo de Tratamiento |
| Q10 | - |  |  | SI | Días previos |
| Q11 | - |  |  | SI | Tipo de terapia |
| Q12 | - |  |  | SI | Lugar de infección |
| Q13 | - |  |  | SI | Comentarios |
| Q14 | - |  |  | SI | Nombre Médico Prescribe |
| Q15 | - |  |  | SI | Uso Exclusivo Responsable Autorización |
| Q16 | - |  |  | SI | Tratamiento |
| Q17 | - |  |  | SI | Uso adecuado de antimicrobianos |
| Q18 | - |  |  | SI | Paciente no encontrado |
| Q19 | - |  |  | SI | Sitio de infección |
| Q20 | - |  |  | SI | Comentarios |
| Q21 | - |  |  | SI | Nombre Médico Autoriza |
| Q22 | - |  |  | SI | Fecha registro |
| Q23 | - |  |  | SI | Fecha vigencia autorización |
| Q24 | - |  |  | SI | Creatinina (integración) |
| Q25 | - |  |  | SI | Agente aislado&nbsp |
| Q26 | - |  |  | SI | N total días de tratamiento solicitados |
| Q27 | - |  |  | SI | Datos de Contacto Solicitante |
| Q28 | - |  |  | SI | Paciente actualmente en diálisis |
| Q29 | - |  |  | SI | Diagnóstico asociado a la solicitud |
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