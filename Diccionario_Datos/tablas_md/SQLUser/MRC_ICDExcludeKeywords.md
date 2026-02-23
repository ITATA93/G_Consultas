# SQLUser.MRC_ICDExcludeKeywords

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICDEK_RowId | bigint | PK |  | NO | - |
| ICDEK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICDEK_CreatedDate | date |  |  | SI | Created Date |
| ICDEK_CreatedTime | time |  |  | SI | Created Time |
| ICDEK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICDEK_Owner | varchar |  |  | SI | Owner |
| ICDEK_Text | varchar |  |  | NO | Exclude Keyword |
| ICDEK_UpdatedDate | date |  |  | SI | Updated Date |
| ICDEK_UpdatedTime | time |  |  | SI | Updated Time |
| ICDEK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombres |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | Rut |
| Q05 | - |  |  | SI | Ocupación |
| Q06 | - |  |  | SI | Edad |
| Q07 | - |  |  | SI | Fecha Nacimiento |
| Q08 | - |  |  | SI | Sexo |
| Q09 | - |  |  | SI | Domicilio |
| Q10 | - |  |  | SI | Comuna |
| Q11 | - |  |  | SI | Diagnóstico |
| Q12 | - |  |  | SI | Signos y Síntomas Principales |
| Q13 | - |  |  | SI | Tipo de Contacto |
| Q14 | - |  |  | SI | Fecha de inicio de Síntomas |
| Q15 | - |  |  | SI | Tratamiento Antibiotico |
| Q16 | - |  |  | SI | Fecha Inicio del Tratamiento |
| Q17 | - |  |  | SI | Tipo de muestra |
| Q18 | - |  |  | SI | N° de muestra |
| Q19 | - |  |  | SI | Examen Solicitado |
| Q20 | - |  |  | SI | Suero |
| Q21 | - |  |  | SI | 1° muestra |
| Q22 | - |  |  | SI | ELISA |
| Q23 | - |  |  | SI | Sangre |
| Q24 | - |  |  | SI | 2° muestra |
| Q25 | - |  |  | SI | Otra |
| Q26 | - |  |  | SI | 3° muestra |
| Q27 | - |  |  | SI | MAT |
| Q28 | - |  |  | SI | Fecha de Toma |
| Q29 | - |  |  | SI | ELISA_REACTIVO USADO |
| Q30 | - |  |  | SI | MICROHEMAGLUTINACION_REACTIVO USADO |
| Q31 | - |  |  | SI | OTRO_REACTIVOUSADO |
| Q32 | - |  |  | SI | ELISA_N° DE LOTE |
| Q33 | - |  |  | SI | MICROHEMAGLUTINACION_N° DE LOTE |
| Q34 | - |  |  | SI | OTRO_N° DE LOTE |
| Q35 | - |  |  | SI | ELISA_RESULTADO |
| Q36 | - |  |  | SI | MICROHEMAGLUTINACION_RESULTADO |
| Q37 | - |  |  | SI | OTRO_RESULTADO |
| Q38 | - |  |  | SI | Dirección |
| Q39 | - |  |  | SI | Nombre del Establecimiento |
| Q40 | - |  |  | SI | Comuna |
| Q41 | - |  |  | SI | Profesional Responsable |
| Q42 | - |  |  | SI | Servicio de Salud |
| Q43 | - |  |  | SI | Ciudad/Localidad |
| Q44 | - |  |  | SI | Fono |
| Q45 | - |  |  | SI | FAX |
| Q46 | - |  |  | SI | Servicio Clínico |
| Q47 | - |  |  | SI | Observaciones |
| Q48 | - |  |  | SI | Solicitud de envio de resultados |
| Q49 | - |  |  | SI | Número |
| Q50 | - |  |  | SI | Registro de Laboratorio |
| Q51 | - |  |  | SI | Fecha de Recepción |
| Q52 | - |  |  | SI | N° de Muestra |
| Q53 | - |  |  | SI | Registro CSP |
| Q54 | - |  |  | SI | Con animales |
| Q55 | - |  |  | SI | Otro |
| Q56 | - |  |  | SI | Indicar |
| Q57 | - |  |  | SI | Región |
| Q58 | - |  |  | SI | Ciudad |
| Q59 | - |  |  | SI | Región |
| Q60 | - |  |  | SI | Observaciones |
| Q61 | - |  |  | SI | RUT |
| Q62 | - |  |  | SI | Ciudad/Localidad |
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