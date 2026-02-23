# questionnaire.QCLXXEXMENF

> Examen Mental Enfermería

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Mental Enfermería

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q235a | varchar |  |  | SI | Entrevista Familia/Tutor |
| Q236 | varchar |  |  | SI | Profesional de Salud |
| Q252 | varchar |  |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q79a | varchar |  |  | SI | Conducta Motora |
| Q79b | varchar |  |  | SI | Evaluación del Riesgo de Auto o Heterolesión |
| Q79c | varchar |  |  | SI | Agitación Psicomotora |
| Q79d | varchar |  |  | SI | ¿Cuales? (Agitacion) |
| Q79e | varchar |  |  | SI | Abandono Intempestivo |
| Q79f | varchar |  |  | SI | ¿Cuales? (abandono) |
| Q79g | varchar |  |  | SI | Autolesivo |
| Q79h | varchar |  |  | SI | ¿Cuales? (autolesivo) |
| Q79i | varchar |  |  | SI | Heteroagesivo |
| Q79j | varchar |  |  | SI | ¿Cuales? (heteroagresivo) |
| Q79k | varchar |  |  | SI | Caída |
| Q79l | varchar |  |  | SI | ¿Cuales? (caida) |
| Q79m | varchar |  |  | SI | Antecedentes de Caídas y/o Accidentes |
| Q79n | varchar |  |  | SI | ¿Cuales? (antecedentes caidas) |
| Q79o | varchar |  |  | SI | Comentarios (Conducta Motora) |
| Q80a | varchar |  |  | SI | Actitud y Conducta |
| Q80b | varchar |  |  | SI | Actitud y Conducta (checkbox) |
| Q80c | varchar |  |  | SI | Comentarios (Actitud y Conducta) |
| Q81a | varchar |  |  | SI | Lenguaje |
| Q81b | varchar |  |  | SI | Lenguaje (Checkbox) |
| Q81c | varchar |  |  | SI | ¿Comunicacion Fluida? |
| Q81d | varchar |  |  | SI | Comentarios (Lenguaje) |
| Q82a | varchar |  |  | SI | Ánimo |
| Q82b | varchar |  |  | SI | Ánimo (check) |
| Q82c | varchar |  |  | SI | Comentarios (Animo) |
| Q82d | varchar |  |  | SI | Afecto (check) |
| Q82e | varchar |  |  | SI | Comentarios (Afecto) |
| Q82f | varchar |  |  | SI | Comentarios (animo) |
| Q83a | varchar |  |  | SI | Estructura del Pensamiento |
| Q83b | varchar |  |  | SI | Estructura del Pensamiento (Checkbox) |
| Q83c | varchar |  |  | SI | Comentarios (Pensamiento) |
| Q83d | varchar |  |  | SI | 8. Contenido del Pensamiento |
| Q83e | varchar |  |  | SI | Alucinaciones |
| Q83f | varchar |  |  | SI | ¿Cuales? (alucionaciones) |
| Q83g | varchar |  |  | SI | Delirio |
| Q83h | varchar |  |  | SI | ¿Cuales? (delirio) |
| Q83i | varchar |  |  | SI | Megalomanía |
| Q83j | varchar |  |  | SI | ¿Cuales? (Megalomania) |
| Q83k | varchar |  |  | SI | Ideas Suicidas |
| Q83l | varchar |  |  | SI | ¿Cuales? (ideas suicidas) |
| Q83m | bit |  |  | SI | Sin Alteraciones |
| Q83n | bit |  |  | SI | Otros |
| Q83o | varchar |  |  | SI | Comentarios (contenido) |
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