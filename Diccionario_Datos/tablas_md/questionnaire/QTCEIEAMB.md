# questionnaire.QTCEIEAMB

> Ingreso de Enfermería AMB

**Schema:** questionnaire
**Columnas:** 232
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso de Enfermería AMB

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01a | varchar |  |  | SI | Motivo de Ingreso |
| Q02a | varchar |  |  | SI | Acompañado por: |
| Q03a | varchar |  |  | SI | Medio de Llegada |
| Q04a | varchar |  |  | SI | Otro Medio de Llegada |
| Q05a | varchar |  |  | SI | Nombre Contacto Emergencia |
| Q06a | varchar |  |  | SI | Teléfono Contacto Emergencia |
| Q07a | varchar |  |  | SI | Información Entregada Por |
| Q08a | varchar |  |  | SI | Información Entregada por Otro |
| Q09a | varchar |  |  | SI | Origen del Paciente |
| Q100a | varchar |  |  | SI | FiO2 |
| Q100aObsDR | varchar |  | FK | SI | FiO2 DR |
| Q101a | varchar |  |  | SI | Hemoglucotest |
| Q101aObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q102a | varchar |  |  | SI | Escala de Dolor (EVA) |
| Q102aObsDR | varchar |  | FK | SI | Escala de Dolor (EVA) DR |
| Q103a | varchar |  |  | SI | Comentarios Examen Físico General |
| Q104a | varchar |  |  | SI | Cardiaco |
| Q104aObsDR | varchar |  | FK | SI | Cardiaco DR |
| Q105a | varchar |  |  | SI | Ritmo Cardiaco |
| Q105aObsDR | varchar |  | FK | SI | Ritmo Cardiaco DR |
| Q106a | varchar |  |  | SI | Comentario OP |
| Q107a | varchar |  |  | SI | Comentario AI |
| Q108a | varchar |  |  | SI | Comentario DC |
| Q109a | varchar |  |  | SI | Comentario EX |
| Q10a | varchar |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q110a | varchar |  |  | SI | comentario Edema |
| Q111a | varchar |  |  | SI | comentario Extremidades Inferiores |
| Q112 | varchar |  |  | SI | Especifique |
| Q113 | varchar |  |  | SI | Razones para no evaluar dolor |
| Q114 | varchar |  |  | SI | Valoración del Dolor |
| Q115 | varchar |  |  | SI | Deposición |
| Q115ObsDR | varchar |  | FK | SI | Deposición DR |
| Q116 | varchar |  |  | SI | Ano |
| Q116ObsDR | varchar |  | FK | SI | Ano DR |
| Q117 | varchar |  |  | SI | Diuresis |
| Q117ObsDR | varchar |  | FK | SI | Diuresis DR |
| Q118 | varchar |  |  | SI | Comentarios Estado Psíquico |
| Q119 | varchar |  |  | SI | comentarios Genito-Urinario |
| Q11a | varchar |  |  | SI | Paciente Porta Brazalete Identificación |
| Q120 | varchar |  |  | SI | comentarios Ano |
| Q121 | varchar |  |  | SI | comentarios Diuresis |
| Q122 | varchar |  |  | SI | comentarios Deposición |
| Q123 | varchar |  |  | SI | Mamas |
| Q123ObsDR | varchar |  | FK | SI | Mamas DR |
| Q124 | varchar |  |  | SI | Pezones |
| Q124ObsDR | varchar |  | FK | SI | Pezones DR |
| Q125 | varchar |  |  | SI | Útero |
| Q125ObsDR | varchar |  | FK | SI | Útero DR |
| Q126 | varchar |  |  | SI | Comentarios Mamas |
| Q127 | varchar |  |  | SI | comentarios Pezones |
| Q128 | varchar |  |  | SI | comentarios Útero |
| Q129 | varchar |  |  | SI | Profesional de Salud |
| Q12a | varchar |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q130 | varchar |  |  | SI | Signos Vitales |
| Q13a | varchar |  |  | SI | Comentario 01 |
| Q141 | varchar |  |  | SI | Presión Arterial Media |
| Q142 | varchar |  |  | SI | Oxigenoterapia |
| Q142ObsDR | varchar |  | FK | SI | Oxigenoterapia DR |
| Q143 | varchar |  |  | SI | Flujo de Oxígeno |
| Q143ObsDR | varchar |  | FK | SI | Flujo de Oxígeno DR |
| Q144 | varchar |  |  | SI | Peso Ideal Hombre |
| Q145 | varchar |  |  | SI | Peso Ideal Mujer |
| Q146 | varchar |  |  | SI | IMC |
| Q147 | varchar |  |  | SI | Superficie Corporal |
| Q148 | varchar |  |  | SI | Circunferencia Craneana |
| Q148ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q149 | varchar |  |  | SI | Circunferencia Torácica |
| Q149ObsDR | varchar |  | FK | SI | Circunferencia Torácica DR |
| Q14a | varchar |  |  | SI | comentario 02 |
| Q150 | varchar |  |  | SI | Circunferencia Abdominal |
| Q150ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q15a | varchar |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q16a | varchar |  |  | SI | comentario 03 |
| Q17a | varchar |  |  | SI | Dispositivos Artificiales |
| Q18a | varchar |  |  | SI | Otro Dispositivo |
| Q19a | varchar |  |  | SI | Dispositivos Clínicos |
| Q200 | varchar |  |  | SI | Aspectos Socio-Culturales |
| Q201 | varchar |  |  | SI | Tipo Examen Físico |
| Q202 | varchar |  |  | SI | Signos Vitales |
| Q203 | varchar |  |  | SI | Parámetros Antropométricos |
| Q204 | varchar |  |  | SI | Examen Segmentario |
| Q205 | varchar |  |  | SI | Antecedentes Clínicos |
| Q206 | varchar |  |  | SI | Esquema de vacunas al día |
| Q207 | varchar |  |  | SI | Requiere licencia médica |
| Q208 | varchar |  |  | SI | Acompañamiento Espiritual |
| Q20a | varchar |  |  | SI | Otro Dispositivo Clínico |
| Q21a | varchar |  |  | SI | Exámenes que Trae el Paciente |
| Q22a | varchar |  |  | SI | Otro Examen |
| Q23a | varchar |  |  | SI | Anamnesis |
| Q24a | varchar |  |  | SI | Información Entregada por Otro |
| Q25a | varchar |  |  | SI | Otro Dispositivo 2 |
| Q26a | varchar |  |  | SI | Religión |
| Q27a | varchar |  |  | SI | Consumo de Alcohol |
| Q28a | varchar |  |  | SI | Tiempo de Consumo Alcohol |
| Q29a | varchar |  |  | SI | Tabaquismo |
| Q30a | numeric |  |  | SI | Cigarrillos por día |
| Q31a | numeric |  |  | SI | Años de consumo |
| Q32a | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q33a | varchar |  |  | SI | Consumo de Drogas |
| Q34a | varchar |  |  | SI | Otra Droga |
| Q35a | varchar |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q36a | varchar |  |  | SI | Nivel de Dependencia |
| Q37a | varchar |  |  | SI | Nivel Educacional |
| Q38a | varchar |  |  | SI | Forma de Comunicación |
| Q39a | varchar |  |  | SI | Otra Forma de Comunicación |
| Q40a | varchar |  |  | SI | Necesita Intérprete |
| Q41a | varchar |  |  | SI | Comentarios Necesita Intérprete |
| Q42a | varchar |  |  | SI | Tipo Examen Físico |
| Q43a | varchar |  |  | SI | Estado General |
| Q44a | varchar |  |  | SI | Estado Psíquico |
| Q44aObsDR | varchar |  | FK | SI | Estado Psíquico DR |
| Q45a | varchar |  |  | SI | Otro Estado Psíquico |
| Q46a | varchar |  |  | SI | Conciencia |
| Q46aObsDR | varchar |  | FK | SI | Conciencia DR |
| Q47a | varchar |  |  | SI | Piel |
| Q47aObsDR | varchar |  | FK | SI | Piel DR |
| Q48a | varchar |  |  | SI | Mucosas |
| Q48aObsDR | varchar |  | FK | SI | Mucosas DR |
| Q49a | varchar |  |  | SI | Cabeza - Cara |
| Q49aObsDR | varchar |  | FK | SI | Cabeza - Cara DR |
| Q50a | varchar |  |  | SI | Pupilas |
| Q50aObsDR | varchar |  | FK | SI | Pupilas DR |
| Q51a | varchar |  |  | SI | Conjuntivas |
| Q51aObsDR | varchar |  | FK | SI | Conjuntivas DR |
| Q52a | varchar |  |  | SI | Dentadura |
| Q52aObsDR | varchar |  | FK | SI | Dentadura DR |
| Q53a | varchar |  |  | SI | Lenguaje |
| Q53aObsDR | varchar |  | FK | SI | Lenguaje DR |
| Q54a | varchar |  |  | SI | Cuello |
| Q54aObsDR | varchar |  | FK | SI | Cuello DR |
| Q55a | varchar |  |  | SI | Vía Aérea |
| Q55aObsDR | varchar |  | FK | SI | Vía Aérea DR |
| Q56a | varchar |  |  | SI | Respiración |
| Q56aObsDR | varchar |  | FK | SI | Respiración DR |
| Q57a | varchar |  |  | SI | Tórax |
| Q57aObsDR | varchar |  | FK | SI | Tórax DR |
| Q58a | varchar |  |  | SI | Extremidades Superiores |
| Q58aObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q59a | varchar |  |  | SI | Abdomen |
| Q59aObsDR | varchar |  | FK | SI | Abdomen DR |
| Q60a | varchar |  |  | SI | Genito-Urinario |
| Q60aObsDR | varchar |  | FK | SI | Genito-Urinario DR |
| Q61a | varchar |  |  | SI | Extremidades Inferiores |
| Q61aObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q62a | varchar |  |  | SI | Edema |
| Q62aObsDR | varchar |  | FK | SI | Edema DR |
| Q63a | varchar |  |  | SI | Comentario Conciencia |
| Q64a | varchar |  |  | SI | Comentario Piel |
| Q65a | varchar |  |  | SI | Comentario Mucosas |
| Q66a | varchar |  |  | SI | Comentario Cabeza - Cara |
| Q67a | varchar |  |  | SI | Comentario Pupilas |
| Q68a | varchar |  |  | SI | Comentario Conjuntivas |
| Q69a | varchar |  |  | SI | Comentario Dentadura |
| Q70a | varchar |  |  | SI | Comentario Lenguaje |
| Q71a | varchar |  |  | SI | Comentario Cuello |
| Q72a | varchar |  |  | SI | Comentario Vía Aérea |
| Q73a | varchar |  |  | SI | Comentario Respiración |
| Q74a | varchar |  |  | SI | Comentario Tórax |
| Q75a | varchar |  |  | SI | Comentario Cardiaco |
| Q76a | varchar |  |  | SI | Comentario Ritmo Cardiaco |
| Q77a | varchar |  |  | SI | Comentario Abdomen |
| Q78a | varchar |  |  | SI | Comentario Extremidades Superiores |
| Q79a | varchar |  |  | SI | Nombre de la Enfermera/Matrona |
| Q80a | varchar |  |  | SI | Manejo de la Cama |
| Q81a | varchar |  |  | SI | Localización del Baño |
| Q82a | varchar |  |  | SI | Horarios de Comida |
| Q83a | varchar |  |  | SI | Horario de Visitas |
| Q84a | varchar |  |  | SI | Nombre de quién recibe la información |
| Q85a | varchar |  |  | SI | Comentario 01 |
| Q86a | varchar |  |  | SI | Comentario 02 |
| Q87a | varchar |  |  | SI | Comentario 03 |
| Q88a | varchar |  |  | SI | Comentario 04 |
| Q89a | varchar |  |  | SI | Comentario 05 |
| Q90a | varchar |  |  | SI | Aislamiento |
| Q91a | varchar |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q92a | varchar |  |  | SI | Presión Arterial Sistólica |
| Q92aObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q93a | varchar |  |  | SI | Presión Arterial Diastólica |
| Q93aObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q94a | varchar |  |  | SI | Peso |
| Q94aObsDR | varchar |  | FK | SI | Peso DR |
| Q95a | varchar |  |  | SI | Talla |
| Q95aObsDR | varchar |  | FK | SI | Talla DR |
| Q96 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q96ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q97a | varchar |  |  | SI | Frecuencia Respiratoria |
| Q97aObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q98a | varchar |  |  | SI | Temperatura |
| Q98aObsDR | varchar |  | FK | SI | Temperatura DR |
| Q99a | varchar |  |  | SI | Saturación de O2 |
| Q99aObsDR | varchar |  | FK | SI | Saturación de O2 DR |
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