# SQLUser.ARC_InsTypeOrdItemApprDisItem

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISITM_ParRef | varchar | PK |  | NO | ARC_InsTypeOrdItemApproval Parent Reference |
| ChildQ78DR | - |  |  | SI | Child Reference: Aspecto Físico General |
| DISITM_ARCIM_DR | varchar |  | FK | SI | Des Ref to ARCItmMast |
| DISITM_Childsub | double |  |  | NO | Childsub |
| DISITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISITM_CreatedDate | date |  |  | SI | Created Date |
| DISITM_CreatedTime | time |  |  | SI | Created Time |
| DISITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISITM_RowId | varchar |  |  | NO | - |
| DISITM_UpdatedDate | date |  |  | SI | Updated Date |
| DISITM_UpdatedTime | time |  |  | SI | Updated Time |
| DISITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q235a | - |  |  | SI | Entrevista Familia/Tutor |
| Q236 | - |  |  | SI | Profesional de Salud |
| Q252 | - |  |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q79a | - |  |  | SI | Conducta Motora |
| Q79b | - |  |  | SI | Evaluación del Riesgo de Auto o Heterolesión |
| Q79c | - |  |  | SI | Agitación Psicomotora |
| Q79d | - |  |  | SI | ¿Cuales? (Agitacion) |
| Q79e | - |  |  | SI | Abandono Intempestivo |
| Q79f | - |  |  | SI | ¿Cuales? (abandono) |
| Q79g | - |  |  | SI | Autolesivo |
| Q79h | - |  |  | SI | ¿Cuales? (autolesivo) |
| Q79i | - |  |  | SI | Heteroagesivo |
| Q79j | - |  |  | SI | ¿Cuales? (heteroagresivo) |
| Q79k | - |  |  | SI | Caída |
| Q79l | - |  |  | SI | ¿Cuales? (caida) |
| Q79m | - |  |  | SI | Antecedentes de Caídas y/o Accidentes |
| Q79n | - |  |  | SI | ¿Cuales? (antecedentes caidas) |
| Q79o | - |  |  | SI | Comentarios (Conducta Motora) |
| Q80a | - |  |  | SI | Actitud y Conducta |
| Q80b | - |  |  | SI | Actitud y Conducta (checkbox) |
| Q80c | - |  |  | SI | Comentarios (Actitud y Conducta) |
| Q81a | - |  |  | SI | Lenguaje |
| Q81b | - |  |  | SI | Lenguaje (Checkbox) |
| Q81c | - |  |  | SI | ¿Comunicacion Fluida? |
| Q81d | - |  |  | SI | Comentarios (Lenguaje) |
| Q82a | - |  |  | SI | Ánimo |
| Q82b | - |  |  | SI | Ánimo (check) |
| Q82c | - |  |  | SI | Comentarios (Animo) |
| Q82d | - |  |  | SI | Afecto (check) |
| Q82e | - |  |  | SI | Comentarios (Afecto) |
| Q82f | - |  |  | SI | Comentarios (animo) |
| Q83a | - |  |  | SI | Estructura del Pensamiento |
| Q83b | - |  |  | SI | Estructura del Pensamiento (Checkbox) |
| Q83c | - |  |  | SI | Comentarios (Pensamiento) |
| Q83d | - |  |  | SI | 8. Contenido del Pensamiento |
| Q83e | - |  |  | SI | Alucinaciones |
| Q83f | - |  |  | SI | ¿Cuales? (alucionaciones) |
| Q83g | - |  |  | SI | Delirio |
| Q83h | - |  |  | SI | ¿Cuales? (delirio) |
| Q83i | - |  |  | SI | Megalomanía |
| Q83j | - |  |  | SI | ¿Cuales? (Megalomania) |
| Q83k | - |  |  | SI | Ideas Suicidas |
| Q83l | - |  |  | SI | ¿Cuales? (ideas suicidas) |
| Q83m | - |  |  | SI | Sin Alteraciones |
| Q83n | - |  |  | SI | Otros |
| Q83o | - |  |  | SI | Comentarios (contenido) |
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