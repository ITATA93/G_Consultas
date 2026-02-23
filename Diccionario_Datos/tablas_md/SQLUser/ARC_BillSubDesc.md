# SQLUser.ARC_BillSubDesc

**Schema:** SQLUser
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DES_ParRef | varchar | PK |  | NO | ARC_BillSub Parent Reference |
| ChildQ108DR | - |  |  | SI | Child Reference: Extremidades |
| DES_Childsub | double |  |  | NO | Childsub |
| DES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DES_CreatedDate | date |  |  | SI | Created Date |
| DES_CreatedTime | time |  |  | SI | Created Time |
| DES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DES_Desc | varchar |  |  | SI | Description |
| DES_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| DES_RowId | varchar |  |  | NO | - |
| DES_UpdatedDate | date |  |  | SI | Updated Date |
| DES_UpdatedTime | time |  |  | SI | Updated Time |
| DES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q100 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q101 | - |  |  | SI | Abdomen, descripción |
| Q102 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q103 | - |  |  | SI | Región anogenital |
| Q104 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q105 | - |  |  | SI | Pene y escroto sin lesiones. Testículos de forma y... |
| Q106 | - |  |  | SI | Vulva y vagina sin hallazgos patológicos. Flujo (-... |
| Q107 | - |  |  | SI | Tacto rectal normal. |
| Q109 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q110 | - |  |  | SI | Extremidades, descripción |
| Q111 | - |  |  | SI | Extremidades de movilidad normal, sin lesiones. Ed... |
| Q113 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q114 | - |  |  | SI | Pulsos, descripción |
| Q115 | - |  |  | SI | Pulsos periféricos simétricos, de amplitud normal. |
| Q116 | - |  |  | SI | Examen neurológico |
| Q117 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q118 | - |  |  | SI | Examen neurológico sin hallazgos. |
| Q119 | - |  |  | SI | Examenes de laboratorio |
| Q120 | - |  |  | SI | Exámenes de imagenología |
| Q123 | - |  |  | SI | Profesional de Salud |
| Q124 | - |  |  | SI | Servicio Clínico |
| Q125 | - |  |  | SI | Paciente eupnéico, respiración tranquila. |
| Q126 | - |  |  | SI | Examen físico simple, descripción |
| Q36 | - |  |  | SI | Estado de conciencia |
| Q37 | - |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q38 | - |  |  | SI | Facie |
| Q39 | - |  |  | SI | Otra |
| Q40 | - |  |  | SI | Facie no característica |
| Q41 | - |  |  | SI | Posición y marcha |
| Q42 | - |  |  | SI | Posición en cama: Activa e indiferente |
| Q43 | - |  |  | SI | Posición de pie: Postura recta, firme y sin oscila... |
| Q44 | - |  |  | SI | Marcha regular y estable. Pasos y braceo coordinad... |
| Q45 | - |  |  | SI | Piel |
| Q47 | - |  |  | SI | Adenopatías |
| Q48 | - |  |  | SI | Adenopatías, descripción |
| Q49 | - |  |  | SI | No se palpan adenopatías. |
| Q50 | - |  |  | SI | Respiración |
| Q51 | - |  |  | SI | Respiración, descripción |
| Q52 | - |  |  | SI | Piel, descripción |
| Q53 | - |  |  | SI | Piel bien hidratada y perfundida, sin lesiones. No... |
| Q54 | - |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q54ObsDR | - |  |  | SI | Presión Arterial Sistólica (mmHg) DR |
| Q55 | - |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q55ObsDR | - |  |  | SI | Presión Arterial Diastólica (mmHg) DR |
| Q56 | - |  |  | SI | Temperatura Axilar (°C) |
| Q56ObsDR | - |  |  | SI | Temperatura Axilar (°C) DR |
| Q57 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q57ObsDR | - |  |  | SI | Frecuencia Cardíaca (lpm) DR |
| Q58 | - |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q58ObsDR | - |  |  | SI | Frecuencia Respiratoria (rpm) DR |
| Q59 | - |  |  | SI | Saturación de O2 (%) |
| Q59ObsDR | - |  |  | SI | Saturación de O2 (%) DR |
| Q60 | - |  |  | SI | FiO2 (%) |
| Q60ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q61 | - |  |  | SI | Escala de Dolor (EVA) |
| Q61ObsDR | - |  |  | SI | Escala de Dolor (EVA) DR |
| Q62 | - |  |  | SI | Peso (kg) |
| Q62ObsDR | - |  |  | SI | Peso (kg) DR |
| Q63 | - |  |  | SI | Talla (cms.) |
| Q63ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q64 | - |  |  | SI | Examen físico general, descripción |
| Q65 | - |  |  | SI | Cabeza y cuello, descripción |
| Q66 | - |  |  | SI | Ojos, descripción |
| Q67 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q70 | - |  |  | SI | Nariz |
| Q71 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q72 | - |  |  | SI | Nariz, descripción |
| Q73 | - |  |  | SI | Labios |
| Q74 | - |  |  | SI | Mucosa oral |
| Q75 | - |  |  | SI | Dentadura y encías |
| Q76 | - |  |  | SI | Faringe |
| Q77 | - |  |  | SI | Orofaringe, descripción |
| Q78 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q80 | - |  |  | SI | Oído, descripción |
| Q81 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q82 | - |  |  | SI | Cuello |
| Q83 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q84 | - |  |  | SI | Cuello, descripción |
| Q85 | - |  |  | SI | Cabeza normal. Ojos, oídos y orofaringe sin hallaz... |
| Q86 | - |  |  | SI | Tiroides normal. Carótidas sin soplos, pulsos norm... |
| Q87 | - |  |  | SI | Tórax |
| Q88 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q90 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q91 | - |  |  | SI | Pulmonar, descripción |
| Q92 | - |  |  | SI | Pulmonar: Murmullo pulmonar simétrico normal, sin ... |
| Q94 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q95 | - |  |  | SI | Cardíaco, descripción |
| Q96 | - |  |  | SI | Cardíaco: Ritmo regular en dos tiempos. No se ausc... |
| Q98 | - |  |  | SI | Mamas: Tejido glandular, pezón y areola sin hallaz... |
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
| Qa | - |  |  | SI | Tórax simétrico, sin deformaciones o lesiones. |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*