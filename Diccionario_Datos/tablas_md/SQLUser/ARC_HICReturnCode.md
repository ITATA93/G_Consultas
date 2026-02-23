# SQLUser.ARC_HICReturnCode

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HICRC_RowId | bigint | PK |  | NO | - |
| ChildQ34DR | - |  |  | SI | Child Reference: Ojos |
| HICRC_Code | varchar |  |  | NO | Code |
| HICRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HICRC_CreatedDate | date |  |  | SI | Created Date |
| HICRC_CreatedTime | time |  |  | SI | Created Time |
| HICRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HICRC_DateFrom | date |  |  | SI | Date From |
| HICRC_DateTo | date |  |  | SI | Date To |
| HICRC_Desc | varchar |  |  | NO | Description |
| HICRC_Owner | varchar |  |  | SI | Owner |
| HICRC_UpdatedDate | date |  |  | SI | Updated Date |
| HICRC_UpdatedTime | time |  |  | SI | Updated Time |
| HICRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q17 | - |  |  | SI | Estado psíquico |
| Q18 | - |  |  | SI | Estado de conciencia |
| Q19 | - |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q20 | - |  |  | SI | Hemodinamia estable, bien hidratado y perfundido. ... |
| Q21 | - |  |  | SI | Estado de la piel |
| Q22 | - |  |  | SI | Respiración |
| Q23 | - |  |  | SI | Descripción examen físico general |
| Q24 | - |  |  | SI | Talla (cms.) |
| Q24ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q25 | - |  |  | SI | Peso (kg.) |
| Q25ObsDR | - |  |  | SI | Peso (kg.) DR |
| Q26 | - |  |  | SI | Temperatura axilar (°C) |
| Q26ObsDR | - |  |  | SI | Temperatura axilar (°C) DR |
| Q27 | - |  |  | SI | Frecuencia cardíaca (lpm) |
| Q27ObsDR | - |  |  | SI | Frecuencia cardíaca (lpm) DR |
| Q28 | - |  |  | SI | Frecuencia respiratoria (rpm) |
| Q28ObsDR | - |  |  | SI | Frecuencia respiratoria (rpm) DR |
| Q29 | - |  |  | SI | Presión arterial sistólica (mmHg) |
| Q29ObsDR | - |  |  | SI | Presión arterial sistólica (mmHg) DR |
| Q30 | - |  |  | SI | Presión arterial diastólica |
| Q30ObsDR | - |  |  | SI | Presión arterial diastólica DR |
| Q31 | - |  |  | SI | Escala de dolor (EVA) |
| Q31ObsDR | - |  |  | SI | Escala de dolor (EVA) DR |
| Q32 | - |  |  | SI | Saturación O2 (%) |
| Q32ObsDR | - |  |  | SI | Saturación O2 (%) DR |
| Q33 | - |  |  | SI | FiO2 (%) |
| Q33ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q35 | - |  |  | SI | Resto del examen realizado en ojos, sin alteracion... |
| Q37 | - |  |  | SI | Resto del examen realizado en oídos, sin alteracio... |
| Q38 | - |  |  | SI | Orofaringe |
| Q39 | - |  |  | SI | Resto del examen realizado en Orofaringe, sin alte... |
| Q40 | - |  |  | SI | Cuello |
| Q41 | - |  |  | SI | Resto del examen realizado en Cuello, sin alteraci... |
| Q42 | - |  |  | SI | Cabeza normal. Ojos, oídos y boca sin alteraciones... |
| Q43 | - |  |  | SI | Cabeza y cuello, descripción |
| Q44 | - |  |  | SI | Ojos, descripción |
| Q45 | - |  |  | SI | Oidos, descripción |
| Q46 | - |  |  | SI | Orofaringe, descripción |
| Q47 | - |  |  | SI | Cardíaco |
| Q48 | - |  |  | SI | Resto del examen cardíaco realizado , sin alteraci... |
| Q49 | - |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q50 | - |  |  | SI | Corazón, descripción |
| Q52 | - |  |  | SI | Murmullo pulmonar simétrico normal, sin ruidos agr... |
| Q53 | - |  |  | SI | Resto del examen realizado en pulmón, sin alteraci... |
| Q54 | - |  |  | SI | Pulmón, descripción |
| Q55 | - |  |  | SI | Tórax |
| Q56 | - |  |  | SI | Tórax simétrico, sin lesiones. |
| Q57 | - |  |  | SI | Resto del examen realizado en tórax Simétrico, sin... |
| Q59 | - |  |  | SI | Resto del examen realizado en abdomen y dorso, sin... |
| Q60 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q61 | - |  |  | SI | Región Anogenital |
| Q62 | - |  |  | SI | Resto del examen realizado en región anogenital, s... |
| Q63 | - |  |  | SI | Región anogenital normal. |
| Q64 | - |  |  | SI | Abdomen y dorso, descripción |
| Q66 | - |  |  | SI | Resto del examen realizado en extremidades, sin al... |
| Q67 | - |  |  | SI | Extremidades, descripción |
| Q68 | - |  |  | SI | Extremidades normales. sin lesiones. Edema (-). Ar... |
| Q70 | - |  |  | SI | Resto del examen realizado en pulsos periféricos, ... |
| Q71 | - |  |  | SI | Pulsos, descripción |
| Q72 | - |  |  | SI | Pulsos simétricos, de amplitud normal. |
| Q73 | - |  |  | SI | Examen físico simple (campo único) |
| Q74 | - |  |  | SI | Exámenes de laboratorio |
| Q75 | - |  |  | SI | Exámenes de Imagenología |
| Q78 | - |  |  | SI | Anamnésis Próxima |
| Q79 | - |  |  | SI | Profesional de Salud |
| Q82 | - |  |  | SI | Neurológico |
| Q83 | - |  |  | SI | Resto del examen neurológico realizado, sin altera... |
| Q84 | - |  |  | SI | Examen neurológico normal, sin hallazgos patológic... |
| Q85 | - |  |  | SI | Desarrollo psicomotor adecuado para la edad |
| Q86 | - |  |  | SI | Mamas de desarrollo normal para la edad. No se pal... |
| Q87 | - |  |  | SI | Desarrollo de genitales externos adecuado para la ... |
| Q88 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q89 | - |  |  | SI | Curvaturas fisiológicas dentro de límites normales |
| Q90 | - |  |  | SI | Ex. Columna Vertebral |
| Q91 | - |  |  | SI | Movimientos en amplitud adecuada |
| Q92 | - |  |  | SI | Test de Schober sin hallazgos patológicos |
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