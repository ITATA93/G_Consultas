# SQLUser.MRC_AderActions

**Schema:** SQLUser
**Columnas:** 188
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADERA_RowID | bigint | PK |  | NO | - |
| ADERA_Code | varchar |  |  | SI | Code |
| ADERA_CodeTableTags | varchar |  |  | SI | Code table tags |
| ADERA_CreatedDate | date |  |  | SI | Created Date |
| ADERA_CreatedTime | time |  |  | SI | Created Time |
| ADERA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADERA_DateFrom | date |  |  | SI | Date From |
| ADERA_DateTo | date |  |  | SI | Date To |
| ADERA_Desc | varchar |  |  | SI | Description |
| ADERA_Owner | varchar |  |  | SI | Owner |
| ADERA_UpdatedDate | date |  |  | SI | Updated Date |
| ADERA_UpdatedTime | time |  |  | SI | Updated Time |
| ADERA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ89DR | - |  |  | SI | Child Reference: Pulmonar |
| Q01 | - |  |  | SI | Fecha de ingreso |
| Q02 | - |  |  | SI | Hora de ingreso |
| Q03 | - |  |  | SI | Información entregada por |
| Q04 | - |  |  | SI | Procedencia del paciente |
| Q05 | - |  |  | SI | Procedencia, descripción |
| Q06 | - |  |  | SI | Contacto |
| Q07 | - |  |  | SI | Fono de contacto |
| Q08 | - |  |  | SI | Profesión / Actividad del paciente |
| Q09 | - |  |  | SI | Motivo de consulta |
| Q10 | - |  |  | SI | Anamnesis próxima |
| Q100 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q101 | - |  |  | SI | Abdomen, descripción |
| Q102 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q103 | - |  |  | SI | Región anogenital |
| Q104 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q105 | - |  |  | SI | Pene y escroto sin lesiones. Testículos de forma y... |
| Q106 | - |  |  | SI | Vulva y vagina sin hallazgos patológicos. Flujo (-... |
| Q107 | - |  |  | SI | Tacto rectal normal. |
| Q109 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q11 | - |  |  | SI | Síntomas generales |
| Q110 | - |  |  | SI | Extremidades, descripción |
| Q111 | - |  |  | SI | Extremidades de movilidad normal, sin lesiones. Ed... |
| Q113 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q114 | - |  |  | SI | Pulsos, descripción |
| Q115 | - |  |  | SI | Pulsos periféricos simétricos, de amplitud normal. |
| Q116 | - |  |  | SI | Examen neurológico |
| Q117 | - |  |  | SI | Resto del examen realizado, sin alteraciones. |
| Q118 | - |  |  | SI | Examen neurológico sin hallazgos. |
| Q119 | - |  |  | SI | Examenes de laboratorio |
| Q12 | - |  |  | SI | No refiere síntomas |
| Q120 | - |  |  | SI | Exámenes de imagenología |
| Q121 | - |  |  | SI | Conclusiones |
| Q122 | - |  |  | SI | Plan de manejo al ingreso |
| Q123 | - |  |  | SI | Profesional de Salud |
| Q124 | - |  |  | SI | Servicio Clínico |
| Q125 | - |  |  | SI | Paciente eupnéico, respiración tranquila. |
| Q126 | - |  |  | SI | Examen físico simple, descripción |
| Q128 | - |  |  | SI | Tórax / Cardiopulmonar |
| Q129 | - |  |  | SI | Ojos |
| Q13 | - |  |  | SI | Respiratorio |
| Q130 | - |  |  | SI | Examen físico y segmentario |
| Q131 | - |  |  | SI | Examen físico general |
| Q132 | - |  |  | SI | Revisión por Sistemas |
| Q133 | - |  |  | SI | Extremidades / pulsos periféricos |
| Q134 | - |  |  | SI | Anamnesis remota |
| Q14 | - |  |  | SI | no refiere síntomas |
| Q15 | - |  |  | SI | Cardiovascular |
| Q16 | - |  |  | SI | No refiere síntomas |
| Q17 | - |  |  | SI | Gastrointestinal |
| Q18 | - |  |  | SI | No refiere síntomas |
| Q19 | - |  |  | SI | Genitourinario |
| Q20 | - |  |  | SI | No refiere síntomas |
| Q21 | - |  |  | SI | Endocrino |
| Q22 | - |  |  | SI | No refiere síntomas |
| Q23 | - |  |  | SI | Neurológico |
| Q24 | - |  |  | SI | No refiere síntomas |
| Q25 | - |  |  | SI | Comentario |
| Q26 | - |  |  | SI | Comentario |
| Q27 | - |  |  | SI | Comentario |
| Q28 | - |  |  | SI | Comentario |
| Q29 | - |  |  | SI | Comentario |
| Q30 | - |  |  | SI | Comentario |
| Q31 | - |  |  | SI | Comentario |
| Q32 | - |  |  | SI | Condición funcional basal |
| Q33 | - |  |  | SI | Utilización de la red de salud |
| Q34 | - |  |  | SI | Medicamentos de uso crónico |
| Q35 | - |  |  | SI | Notas complementarias |
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
| Q54 | - |  |  | SI | Presión arterial sistólica (mmHg) |
| Q54ObsDR | - |  |  | SI | Presión arterial sistólica (mmHg) DR |
| Q55 | - |  |  | SI | Presión arterial diastólica |
| Q55ObsDR | - |  |  | SI | Presión arterial diastólica DR |
| Q56 | - |  |  | SI | Temperatura axilar (°C) |
| Q56ObsDR | - |  |  | SI | Temperatura axilar (°C) DR |
| Q57 | - |  |  | SI | Frecuencia cardíaca (lpm) |
| Q57ObsDR | - |  |  | SI | Frecuencia cardíaca (lpm) DR |
| Q58 | - |  |  | SI | Frecuencia respiratoria (rpm) |
| Q58ObsDR | - |  |  | SI | Frecuencia respiratoria (rpm) DR |
| Q59 | - |  |  | SI | Saturación de O2 (%) |
| Q59ObsDR | - |  |  | SI | Saturación de O2 (%) DR |
| Q60 | - |  |  | SI | FiO2 (%) |
| Q60ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q61 | - |  |  | SI | Escala de dolor (EVA) |
| Q61ObsDR | - |  |  | SI | Escala de dolor (EVA) DR |
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