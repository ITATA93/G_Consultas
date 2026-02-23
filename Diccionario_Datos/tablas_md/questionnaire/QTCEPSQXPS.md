# questionnaire.QTCEPSQXPS

> Lista de Chequeo para Seguridad en Cirugía: Salida (previa salida de quirófano)

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lista de Chequeo para Seguridad en Cirugía: Salida (previa salida de quirófano)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Se confirma que todos los miembros del equipo se h... |
| Q02 | varchar |  |  | SI | PERSONAL DEL PABELLÓN CONFIRMA VERBALMENTE CON EL ... |
| Q03 | varchar |  |  | SI | Nombre de Procedimiento Realizado |
| Q04 | varchar |  |  | SI | Conteo Instrumental Correcto |
| Q05 | varchar |  |  | SI | Conteo Agujas Correcto |
| Q06 | varchar |  |  | SI | Conteo de Compresas Correcto |
| Q07 | varchar |  |  | SI | Estado del Recuento Total |
| Q08 | varchar |  |  | SI | IDENTIFICACIÓN DE LAS MUESTRAS BIOLÓGICAS  |
| Q09 | varchar |  |  | SI | Nombre Completo del Paciente |
| Q10 | varchar |  |  | SI | RUT Del Paciente |
| Q11 | date |  |  | SI | Fecha de la Toma de Muestra |
| Q12 | varchar |  |  | SI | Identificación clara del tejido u órgano y localiz... |
| Q13 | varchar |  |  | SI | Comentarios |
| Q14 | varchar |  |  | SI | Numeración de la muestra en caso de haber más de u... |
| Q15 | varchar |  |  | SI | CHEQUEO SALIDA |
| Q16 | time |  |  | SI | Hora realización Chequeo  |
| Q17 | varchar |  |  | SI | Chequeo presencia brazalete de identificación |
| Q18 | varchar |  |  | SI | Chequeo brazalete de alergias |
| Q19 | varchar |  |  | SI | Chequeo de presencia de documentación intraoperato... |
| Q20 | varchar |  |  | SI | Chequeo egreso del paciente con todos los artículo... |
| Q22 | varchar |  |  | SI | Chequeo de devolución de productos sanguíneos u ot... |
| Q23 | varchar |  |  | SI | Profesional Responsable de la Medición  |
| Q24 | varchar |  |  | SI | Comentario |
| Q25 | varchar |  |  | SI | Comentario |
| Q26 | varchar |  |  | SI | Comentario |
| Q27 | varchar |  |  | SI | Comentario |
| Q28 | varchar |  |  | SI | Comentario |
| Q29 | varchar |  |  | SI | Comentario |
| Q30 | varchar |  |  | SI | Comentario |
| Q31 | varchar |  |  | SI | Comentario |
| Q32 | varchar |  |  | SI | Comentario |
| Q33 | varchar |  |  | SI | Comentario |
| Q34 | varchar |  |  | SI | Comentario |
| Q35 | varchar |  |  | SI | Comentario |
| Q36 | varchar |  |  | SI | Comentario |
| Q37 | varchar |  |  | SI | Comentario |
| Q38 | varchar |  |  | SI | Comentario |
| Q39 | varchar |  |  | SI | Comentario |
| Q40 | varchar |  |  | SI | Fecha de Toma de muestra |
| Q41 | varchar |  |  | SI | Comentario |
| Q42 | varchar |  |  | SI | Conteo de Gasas correcto |
| Q43 | varchar |  |  | SI | Comentario |
| Q44 | varchar |  |  | SI | ¿Existió algún problema con el instrumental o los ... |
| Q45 | varchar |  |  | SI | Comentario |
| Q46 | varchar |  |  | SI | Preocupaciones claves para la recuperación y manej... |
| Q47 | varchar |  |  | SI | Comentario |
| Q48 | varchar |  |  | SI | Destino del paciente  |
| Q49 | varchar |  |  | SI | Comentario |
| Q50 | varchar |  |  | SI | Cuidados especiales post-operatorios (posición, dr... |
| Q51 | varchar |  |  | SI | Comentario |
| Q52 | varchar |  |  | SI | ¿Existió algún problema con el instrumental a los ... |
| Q53 | varchar |  |  | SI | Comentario |
| Q54 | varchar |  |  | SI | Solicitud u orden de muestra Biológica |
| Q55 | varchar |  |  | SI | Comentario |
| Q56 | varchar |  |  | SI | Comentarios / Obervaciones |
| Q58 | varchar |  |  | SI | Cirugía / Procedimiento Principal |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*