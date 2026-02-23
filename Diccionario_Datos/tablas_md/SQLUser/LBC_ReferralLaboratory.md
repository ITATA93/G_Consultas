# SQLUser.LBC_ReferralLaboratory

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRL_RowID | bigint | PK |  | NO | - |
| LBCRL_Address | varchar |  |  | SI | Street Address |
| LBCRL_City_DR | bigint |  | FK | SI | City |
| LBCRL_Code | varchar |  |  | SI | Code |
| LBCRL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRL_CreatedDate | date |  |  | SI | Created Date |
| LBCRL_CreatedTime | time |  |  | SI | Created Time |
| LBCRL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRL_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRL_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRL_Desc | varchar |  |  | SI | Description |
| LBCRL_DisplaySequence | double |  |  | SI | Display Sequence |
| LBCRL_Indicator | varchar |  |  | SI | Indicator for Doctor Report. |
| LBCRL_Owner | varchar |  |  | SI | Owner |
| LBCRL_Phones | varchar |  |  | SI | Phone Numbers |
| LBCRL_Province_DR | bigint |  | FK | SI | State |
| LBCRL_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRL_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCRL_Zip_DR | bigint |  | FK | SI | Zip |
| Q01 | - |  |  | SI | Se confirma que todos los miembros del equipo se h... |
| Q02 | - |  |  | SI | PERSONAL DEL PABELLÓN CONFIRMA VERBALMENTE CON EL ... |
| Q03 | - |  |  | SI | Nombre de Procedimiento Realizado |
| Q04 | - |  |  | SI | Conteo Instrumental Correcto |
| Q05 | - |  |  | SI | Conteo Agujas Correcto |
| Q06 | - |  |  | SI | Conteo de Compresas Correcto |
| Q07 | - |  |  | SI | Estado del Recuento Total |
| Q08 | - |  |  | SI | IDENTIFICACIÓN DE LAS MUESTRAS BIOLÓGICAS |
| Q09 | - |  |  | SI | Nombre Completo del Paciente |
| Q10 | - |  |  | SI | RUT Del Paciente |
| Q11 | - |  |  | SI | Fecha de la Toma de Muestra |
| Q12 | - |  |  | SI | Identificación clara del tejido u órgano y localiz... |
| Q13 | - |  |  | SI | Comentarios |
| Q14 | - |  |  | SI | Numeración de la muestra en caso de haber más de u... |
| Q15 | - |  |  | SI | CHEQUEO SALIDA |
| Q16 | - |  |  | SI | Hora realización Chequeo |
| Q17 | - |  |  | SI | Chequeo presencia brazalete de identificación |
| Q18 | - |  |  | SI | Chequeo brazalete de alergias |
| Q19 | - |  |  | SI | Chequeo de presencia de documentación intraoperato... |
| Q20 | - |  |  | SI | Chequeo egreso del paciente con todos los artículo... |
| Q22 | - |  |  | SI | Chequeo de devolución de productos sanguíneos u ot... |
| Q23 | - |  |  | SI | Profesional Responsable de la Medición |
| Q24 | - |  |  | SI | Comentario |
| Q25 | - |  |  | SI | Comentario |
| Q26 | - |  |  | SI | Comentario |
| Q27 | - |  |  | SI | Comentario |
| Q28 | - |  |  | SI | Comentario |
| Q29 | - |  |  | SI | Comentario |
| Q30 | - |  |  | SI | Comentario |
| Q31 | - |  |  | SI | Comentario |
| Q32 | - |  |  | SI | Comentario |
| Q33 | - |  |  | SI | Comentario |
| Q34 | - |  |  | SI | Comentario |
| Q35 | - |  |  | SI | Comentario |
| Q36 | - |  |  | SI | Comentario |
| Q37 | - |  |  | SI | Comentario |
| Q38 | - |  |  | SI | Comentario |
| Q39 | - |  |  | SI | Comentario |
| Q40 | - |  |  | SI | Fecha de Toma de muestra |
| Q41 | - |  |  | SI | Comentario |
| Q42 | - |  |  | SI | Conteo de Gasas correcto |
| Q43 | - |  |  | SI | Comentario |
| Q44 | - |  |  | SI | ¿Existió algún problema con el instrumental o los ... |
| Q45 | - |  |  | SI | Comentario |
| Q46 | - |  |  | SI | Preocupaciones claves para la recuperación y manej... |
| Q47 | - |  |  | SI | Comentario |
| Q48 | - |  |  | SI | Destino del paciente |
| Q49 | - |  |  | SI | Comentario |
| Q50 | - |  |  | SI | Cuidados especiales post-operatorios (posición, dr... |
| Q51 | - |  |  | SI | Comentario |
| Q52 | - |  |  | SI | ¿Existió algún problema con el instrumental a los ... |
| Q53 | - |  |  | SI | Comentario |
| Q54 | - |  |  | SI | Solicitud u orden de muestra Biológica |
| Q55 | - |  |  | SI | Comentario |
| Q56 | - |  |  | SI | Comentarios / Obervaciones |
| Q58 | - |  |  | SI | Cirugía / Procedimiento Principal |
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