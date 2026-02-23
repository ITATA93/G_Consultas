# questionnaire.QCLXXEFMI

> Examen Físico Medicina

**Schema:** questionnaire
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Medicina

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q100 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q101 | varchar |  |  | SI | Abdomen, descripción |
| Q102 | bit |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q103 | varchar |  |  | SI | Región anogenital |
| Q104 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q105 | bit |  |  | SI | Pene y escroto sin lesiones. Testículos de forma y... |
| Q106 | bit |  |  | SI | Vulva y vagina sin hallazgos patológicos. Flujo (-... |
| Q107 | bit |  |  | SI | Tacto rectal normal. |
| Q109 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q110 | varchar |  |  | SI | Extremidades, descripción |
| Q111 | bit |  |  | SI | Extremidades de movilidad normal, sin lesiones. Ed... |
| Q113 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q114 | varchar |  |  | SI | Pulsos, descripción |
| Q115 | bit |  |  | SI | Pulsos periféricos simétricos, de amplitud normal. |
| Q116 | varchar |  |  | SI | Examen neurológico |
| Q117 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q118 | bit |  |  | SI | Examen neurológico sin hallazgos. |
| Q119 | varchar |  |  | SI | Examenes de laboratorio |
| Q120 | varchar |  |  | SI | Exámenes de imagenología |
| Q123 | varchar |  |  | SI | Profesional de Salud |
| Q124 | varchar |  |  | SI | Servicio Clínico |
| Q125 | bit |  |  | SI | Paciente eupnéico, respiración tranquila. |
| Q126 | varchar |  |  | SI | Examen físico simple, descripción |
| Q36 | varchar |  |  | SI | Estado de conciencia |
| Q37 | bit |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q38 | varchar |  |  | SI | Facie |
| Q39 | varchar |  |  | SI | Otra |
| Q40 | bit |  |  | SI | Facie no característica |
| Q41 | varchar |  |  | SI | Posición y marcha |
| Q42 | bit |  |  | SI | Posición en cama: Activa e indiferente |
| Q43 | bit |  |  | SI | Posición de pie: Postura recta, firme y sin oscila... |
| Q44 | bit |  |  | SI | Marcha regular y estable. Pasos y braceo coordinad... |
| Q45 | varchar |  |  | SI | Piel |
| Q47 | varchar |  |  | SI | Adenopatías |
| Q48 | varchar |  |  | SI | Adenopatías, descripción |
| Q49 | bit |  |  | SI | No se palpan adenopatías. |
| Q50 | varchar |  |  | SI | Respiración |
| Q51 | varchar |  |  | SI | Respiración, descripción |
| Q52 | varchar |  |  | SI | Piel, descripción |
| Q53 | bit |  |  | SI | Piel bien hidratada y perfundida, sin lesiones. No... |
| Q54 | varchar |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q54ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica (mmHg) DR |
| Q55 | varchar |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q55ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica (mmHg) DR |
| Q56 | varchar |  |  | SI | Temperatura Axilar (°C) |
| Q56ObsDR | varchar |  | FK | SI | Temperatura Axilar (°C) DR |
| Q57 | varchar |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q57ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca (lpm) DR |
| Q58 | varchar |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q58ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria (rpm) DR |
| Q59 | varchar |  |  | SI | Saturación de O2 (%) |
| Q59ObsDR | varchar |  | FK | SI | Saturación de O2 (%) DR |
| Q60 | varchar |  |  | SI | FiO2 (%) |
| Q60ObsDR | varchar |  | FK | SI | FiO2 (%) DR |
| Q61 | varchar |  |  | SI | Escala de Dolor (EVA) |
| Q61ObsDR | varchar |  | FK | SI | Escala de Dolor (EVA) DR |
| Q62 | varchar |  |  | SI | Peso (kg) |
| Q62ObsDR | varchar |  | FK | SI | Peso (kg) DR |
| Q63 | varchar |  |  | SI | Talla (cms.) |
| Q63ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q64 | varchar |  |  | SI | Examen físico general, descripción |
| Q65 | varchar |  |  | SI | Cabeza y cuello, descripción |
| Q66 | varchar |  |  | SI | Ojos, descripción |
| Q67 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q70 | varchar |  |  | SI | Nariz |
| Q71 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q72 | varchar |  |  | SI | Nariz, descripción |
| Q73 | varchar |  |  | SI | Labios |
| Q74 | varchar |  |  | SI | Mucosa oral |
| Q75 | varchar |  |  | SI | Dentadura y encías |
| Q76 | varchar |  |  | SI | Faringe |
| Q77 | varchar |  |  | SI | Orofaringe, descripción |
| Q78 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q80 | varchar |  |  | SI | Oído, descripción |
| Q81 | bit |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q82 | varchar |  |  | SI | Cuello |
| Q83 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q84 | varchar |  |  | SI | Cuello, descripción |
| Q85 | bit |  |  | SI | Cabeza normal. Ojos, oídos y orofaringe sin hallaz... |
| Q86 | bit |  |  | SI | Tiroides normal. Carótidas sin soplos, pulsos norm... |
| Q87 | varchar |  |  | SI | Tórax |
| Q88 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q90 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q91 | varchar |  |  | SI | Pulmonar, descripción |
| Q92 | bit |  |  | SI | Pulmonar: Murmullo pulmonar simétrico normal, sin ... |
| Q94 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q95 | varchar |  |  | SI | Cardíaco, descripción |
| Q96 | bit |  |  | SI | Cardíaco: Ritmo regular en dos tiempos. No se ausc... |
| Q98 | bit |  |  | SI | Mamas: Tejido glandular, pezón y areola sin hallaz... |
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
| Qa | bit |  |  | SI | Tórax simétrico, sin deformaciones o lesiones. |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*