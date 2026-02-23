# questionnaire.QCLXXEFPED

> Examen Físico Pediátrico

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Pediátrico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q17 | varchar |  |  | SI | Estado psíquico |
| Q18 | varchar |  |  | SI | Estado de conciencia |
| Q19 | bit |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q20 | bit |  |  | SI | Hemodinamia estable, bien hidratado y perfundido. ... |
| Q21 | varchar |  |  | SI | Estado de la piel |
| Q22 | varchar |  |  | SI | Respiración |
| Q23 | varchar |  |  | SI | Descripción examen físico general |
| Q24 | varchar |  |  | SI | Talla (cms.) |
| Q24ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q25 | varchar |  |  | SI | Peso (kg.) |
| Q25ObsDR | varchar |  | FK | SI | Peso (kg.) DR |
| Q26 | varchar |  |  | SI | Temperatura axilar (°C) |
| Q26ObsDR | varchar |  | FK | SI | Temperatura axilar (°C) DR |
| Q27 | varchar |  |  | SI | Frecuencia cardíaca (lpm) |
| Q27ObsDR | varchar |  | FK | SI | Frecuencia cardíaca (lpm) DR |
| Q28 | varchar |  |  | SI | Frecuencia respiratoria (rpm) |
| Q28ObsDR | varchar |  | FK | SI | Frecuencia respiratoria (rpm) DR |
| Q29 | varchar |  |  | SI | Presión arterial sistólica (mmHg) |
| Q29ObsDR | varchar |  | FK | SI | Presión arterial sistólica (mmHg) DR |
| Q30 | varchar |  |  | SI | Presión arterial diastólica |
| Q30ObsDR | varchar |  | FK | SI | Presión arterial diastólica DR |
| Q31 | varchar |  |  | SI | Escala de dolor (EVA) |
| Q31ObsDR | varchar |  | FK | SI | Escala de dolor (EVA) DR |
| Q32 | varchar |  |  | SI | Saturación O2 (%) |
| Q32ObsDR | varchar |  | FK | SI | Saturación O2 (%) DR |
| Q33 | varchar |  |  | SI | FiO2 (%) |
| Q33ObsDR | varchar |  | FK | SI | FiO2 (%) DR |
| Q35 | bit |  |  | SI | Resto del examen realizado en ojos, sin alteracion... |
| Q37 | bit |  |  | SI | Resto del examen realizado en oídos, sin alteracio... |
| Q38 | varchar |  |  | SI | Orofaringe |
| Q39 | bit |  |  | SI | Resto del examen realizado en Orofaringe, sin alte... |
| Q40 | varchar |  |  | SI | Cuello |
| Q41 | bit |  |  | SI | Resto del examen realizado en Cuello, sin alteraci... |
| Q42 | bit |  |  | SI | Cabeza normal. Ojos, oídos y boca sin alteraciones... |
| Q43 | varchar |  |  | SI | Cabeza y cuello, descripción |
| Q44 | varchar |  |  | SI | Ojos, descripción |
| Q45 | varchar |  |  | SI | Oidos, descripción |
| Q46 | varchar |  |  | SI | Orofaringe, descripción |
| Q47 | varchar |  |  | SI | Cardíaco |
| Q48 | bit |  |  | SI | Resto del examen cardíaco realizado , sin alteraci... |
| Q49 | bit |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q50 | varchar |  |  | SI | Corazón, descripción |
| Q52 | bit |  |  | SI | Murmullo pulmonar simétrico normal, sin ruidos agr... |
| Q53 | bit |  |  | SI | Resto del examen realizado en pulmón, sin alteraci... |
| Q54 | varchar |  |  | SI | Pulmón, descripción |
| Q55 | varchar |  |  | SI | Tórax |
| Q56 | bit |  |  | SI | Tórax simétrico, sin lesiones. |
| Q57 | bit |  |  | SI | Resto del examen realizado en tórax Simétrico, sin... |
| Q59 | bit |  |  | SI | Resto del examen realizado en abdomen y dorso, sin... |
| Q60 | bit |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q61 | varchar |  |  | SI | Región Anogenital |
| Q62 | bit |  |  | SI | Resto del examen realizado en región anogenital, s... |
| Q63 | bit |  |  | SI | Región anogenital normal. |
| Q64 | varchar |  |  | SI | Abdomen y dorso, descripción |
| Q66 | bit |  |  | SI | Resto del examen realizado en extremidades, sin al... |
| Q67 | varchar |  |  | SI | Extremidades, descripción |
| Q68 | bit |  |  | SI | Extremidades normales. sin lesiones. Edema (-). Ar... |
| Q70 | bit |  |  | SI | Resto del examen realizado en pulsos periféricos, ... |
| Q71 | varchar |  |  | SI | Pulsos, descripción |
| Q72 | bit |  |  | SI | Pulsos simétricos, de amplitud normal. |
| Q73 | varchar |  |  | SI | Examen físico simple (campo único) |
| Q74 | varchar |  |  | SI | Exámenes de laboratorio |
| Q75 | varchar |  |  | SI | Exámenes de Imagenología |
| Q78 | varchar |  |  | SI | Anamnésis Próxima |
| Q79 | varchar |  |  | SI | Profesional de Salud |
| Q82 | varchar |  |  | SI | Neurológico |
| Q83 | bit |  |  | SI | Resto del examen neurológico realizado, sin altera... |
| Q84 | bit |  |  | SI | Examen neurológico normal, sin hallazgos patológic... |
| Q85 | bit |  |  | SI | Desarrollo psicomotor adecuado para la edad |
| Q86 | bit |  |  | SI | Mamas de desarrollo normal para la edad. No se pal... |
| Q87 | bit |  |  | SI | Desarrollo de genitales externos adecuado para la ... |
| Q88 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q89 | bit |  |  | SI | Curvaturas fisiológicas dentro de límites normales |
| Q90 | varchar |  |  | SI | Ex. Columna Vertebral |
| Q91 | bit |  |  | SI | Movimientos en amplitud adecuada |
| Q92 | bit |  |  | SI | Test de Schober sin hallazgos patológicos |
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