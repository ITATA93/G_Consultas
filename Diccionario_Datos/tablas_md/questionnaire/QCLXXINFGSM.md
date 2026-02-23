# questionnaire.QCLXXINFGSM

> Información General de Ingreso Salud Mental

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Información General de Ingreso Salud Mental

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q09 | varchar |  |  | SI | Acompañado Por |
| Q10 | varchar |  |  | SI | Comentarios del acompañante |
| Q11 | varchar |  |  | SI | Tipo de Ingreso |
| Q12 | varchar |  |  | SI | Comentarios del Tipo de Ingreso |
| Q13 | varchar |  |  | SI | Medio de Llegada |
| Q14 | varchar |  |  | SI | Comentarios de la Forma de Ingreso |
| Q15 | varchar |  |  | SI | Nombre Contacto Emergencia |
| Q16 | varchar |  |  | SI | Parentesco |
| Q166 | varchar |  |  | SI | Comentario de brazalete de alergias |
| Q17 | varchar |  |  | SI | Teléfono Contacto Emergencia |
| Q18 | varchar |  |  | SI | Información Entregada Por |
| Q19 | varchar |  |  | SI | Comentarios de la información entregada |
| Q20 | varchar |  |  | SI | Origen del Paciente |
| Q21 | varchar |  |  | SI | Comentarios del Origen del Paciente |
| Q22 | varchar |  |  | SI | Primera Atención Salud Mental |
| Q23 | varchar |  |  | SI | Comentario de la Primera Atención de Salud Mental |
| Q236 | varchar |  |  | SI | Profesional de Salud |
| Q24 | varchar |  |  | SI | Paciente Crónico Salud Mental |
| Q25 | varchar |  |  | SI | Comentario de Paciente Crónico |
| Q26 | varchar |  |  | SI | Ingresos Previos |
| Q27 | varchar |  |  | SI | Comentario de Ingresos Previos |
| Q28 | varchar |  |  | SI | Comienzo y evolución de la enfermedad |
| Q28a | varchar |  |  | SI | Adherenia/Control Tratamiento (Check) |
| Q29 | varchar |  |  | SI | Comentarios Adherencia/Control Tratamiento |
| Q30 | varchar |  |  | SI | Situación laboral/Ocupación |
| Q31 | varchar |  |  | SI | Núcleo de Convivencia |
| Q32 | varchar |  |  | SI | Enfermedades Psiquiátricas Familiares |
| Q33 | varchar |  |  | SI | Comentario de Enfermedades Psiquiátricas Familiare... |
| Q34 | varchar |  |  | SI | Paciente Porta Brazalete Identificación |
| Q35 | varchar |  |  | SI | Comentario del Brazalete de Identificación |
| Q36 | varchar |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q37 | varchar |  |  | SI | Comentario de Brazalete con Datos Completos y Legi... |
| Q38 | varchar |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q39 | varchar |  |  | SI | Dispositivos Artificiales |
| Q40 | varchar |  |  | SI | Comentario de Dispositivos Artificiales |
| Q41 | varchar |  |  | SI | Otro dispositivo |
| Q42 | varchar |  |  | SI | Dispositivos Clínicos |
| Q43 | varchar |  |  | SI | Comentario de Dispositivos Clínicos |
| Q44 | varchar |  |  | SI | Otro Dispositivo |
| Q45 | varchar |  |  | SI | Exámenes que Trae el Paciente |
| Q46 | varchar |  |  | SI | Comentario de los Exámenes |
| Q47 | varchar |  |  | SI | Otro Examen |
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