# questionnaire.QTCEIEP

> Ingreso Enfermería Pediatría

**Schema:** questionnaire
**Columnas:** 324
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Enfermería Pediatría

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Motivo Ingreso |
| Q02 | varchar |  |  | SI | Acompañado por |
| Q03 | varchar |  |  | SI | Medio de Llegada |
| Q04 | varchar |  |  | SI | Otro Medio de Llegada |
| Q05 | varchar |  |  | SI | Nombre Contacto Emergencia |
| Q06 | numeric |  |  | SI | Teléfono Contacto Emergencia |
| Q07 | varchar |  |  | SI | Información Entregada por |
| Q08 | varchar |  |  | SI | Otro Información entregada  |
| Q09 | varchar |  |  | SI | Origen del Paciente |
| Q10 | varchar |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q100 | varchar |  |  | SI | Extremidades Superiores |
| Q100ObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q101 | varchar |  |  | SI | Extremidades Inferiores |
| Q101ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q102 | varchar |  |  | SI | Genito Urinario |
| Q102ObsDR | varchar |  | FK | SI | Genito Urinario DR |
| Q103 | varchar |  |  | SI | Ano |
| Q104 | varchar |  |  | SI | Diuresis |
| Q104ObsDR | varchar |  | FK | SI | Diuresis DR |
| Q105 | varchar |  |  | SI | Otro Diuresis |
| Q106 | varchar |  |  | SI | Deposiciones |
| Q106ObsDR | varchar |  | FK | SI | Deposiciones DR |
| Q107 | varchar |  |  | SI | Nombre Madre |
| Q108 | varchar |  |  | SI | Nombre Padre |
| Q109 | varchar |  |  | SI | Uso de  Tuto |
| Q11 | varchar |  |  | SI | Aislamiento |
| Q110 | varchar |  |  | SI | Comentario tuto |
| Q111 | varchar |  |  | SI | Uso de Chupete |
| Q112 | varchar |  |  | SI | comentario chupete |
| Q113 | varchar |  |  | SI | Uso de Mamaderas |
| Q114 | varchar |  |  | SI | comentario mamadera |
| Q115 | varchar |  |  | SI | Uso de Pañal |
| Q116 | varchar |  |  | SI | comentario pañal |
| Q117 | varchar |  |  | SI | Alimentación |
| Q118 | varchar |  |  | SI | Higiene |
| Q119 | varchar |  |  | SI | Vestuario |
| Q12 | varchar |  |  | SI | Comentario Aislamiento |
| Q120 | varchar |  |  | SI | Deambulación |
| Q121 | varchar |  |  | SI | Movilización |
| Q122 | varchar |  |  | SI | Comunicación |
| Q1221 | varchar |  |  | SI | Eliminación |
| Q123 | varchar |  |  | SI | Comentario 01 |
| Q124 | varchar |  |  | SI | comentario 02 |
| Q125 | varchar |  |  | SI | comentario 03 |
| Q126 | varchar |  |  | SI | comentario 04 |
| Q127 | varchar |  |  | SI | comentario 05 |
| Q128 | varchar |  |  | SI | comentario 06 |
| Q1281 | varchar |  |  | SI | Comentario Eliminación |
| Q129 | varchar |  |  | SI | Nombre de la Enfermera |
| Q13 | varchar |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q130 | varchar |  |  | SI | comentario 07 |
| Q131 | varchar |  |  | SI | Manejo de la Cama |
| Q132 | varchar |  |  | SI | comentario 08 |
| Q133 | varchar |  |  | SI | Uso del Timbre de Llamado |
| Q134 | varchar |  |  | SI | comentario 09 |
| Q135 | varchar |  |  | SI | Localización del Baño |
| Q136 | varchar |  |  | SI | comentario 10 |
| Q137 | varchar |  |  | SI | Horarios de Comidas |
| Q138 | varchar |  |  | SI | Comentario 11 |
| Q139 | varchar |  |  | SI | Horario de Visitas |
| Q14 | varchar |  |  | SI | Paciente Porta Brazalete Identificación |
| Q140 | varchar |  |  | SI | comentario 12 |
| Q141 | varchar |  |  | SI | Sistemas de Monitorización y Equipos |
| Q142 | varchar |  |  | SI | comentarios 13 |
| Q143 | varchar |  |  | SI | Nombre de Quién Recibe la Información |
| Q144 | varchar |  |  | SI | Tiempo Consumo Drogas |
| Q145 | varchar |  |  | SI | Peso |
| Q145ObsDR | varchar |  | FK | SI | Peso DR |
| Q146 | varchar |  |  | SI | comentario 1 |
| Q147 | varchar |  |  | SI | comentario 02 |
| Q148 | varchar |  |  | SI | comentario 03 |
| Q149 | varchar |  |  | SI | comentario 04 |
| Q15 | varchar |  |  | SI | Comentario 01 |
| Q150 | varchar |  |  | SI | comentario 05 |
| Q151 | varchar |  |  | SI | comentario 06 |
| Q152 | varchar |  |  | SI | comentario 07 |
| Q153 | varchar |  |  | SI | comentario 08 |
| Q154 | varchar |  |  | SI | comentario 09 |
| Q155 | varchar |  |  | SI | comentario 10 |
| Q156 | varchar |  |  | SI | comentario 11 |
| Q157 | varchar |  |  | SI | comentario 12 |
| Q158 | varchar |  |  | SI | comentario 13 |
| Q159 | varchar |  |  | SI | comentarios 14 |
| Q16 | varchar |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q160 | varchar |  |  | SI | comentarios 15 |
| Q161 | varchar |  |  | SI | comentarios 16 |
| Q162 | varchar |  |  | SI | comentarios 17 |
| Q163 | varchar |  |  | SI | comentarios 18 |
| Q164 | varchar |  |  | SI | comentarios 19 |
| Q165 | varchar |  |  | SI | comentarios 20 |
| Q166 | varchar |  |  | SI | comentarios 21 |
| Q167 | varchar |  |  | SI | comentarios 22 |
| Q168 | varchar |  |  | SI | Edema |
| Q168ObsDR | varchar |  | FK | SI | Edema DR |
| Q169 | varchar |  |  | SI | Comentarios 23 |
| Q17 | varchar |  |  | SI | Comentarios 02 |
| Q170 | varchar |  |  | SI | Profesional de Salud |
| Q171 | varchar |  |  | SI | Comentarios |
| Q172 | varchar |  |  | SI | LPP |
| Q172ObsDR | varchar |  | FK | SI | LPP DR |
| Q173 | varchar |  |  | SI | Grado LPP |
| Q173ObsDR | varchar |  | FK | SI | Grado LPP DR |
| Q174 | varchar |  |  | SI | Ubicación LPP |
| Q174ObsDR | varchar |  | FK | SI | Ubicación LPP DR |
| Q175 | varchar |  |  | SI | Lateralidad LPP |
| Q175ObsDR | varchar |  | FK | SI | Lateralidad LPP DR |
| Q176 | varchar |  |  | SI | Comentario LPP |
| Q177 | varchar |  |  | SI | Comentario G.LPP |
| Q178 | varchar |  |  | SI | Comentario U.LPP |
| Q179 | varchar |  |  | SI | Comentario L.LPP |
| Q18 | varchar |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q180 | varchar |  |  | SI | Comentarios |
| Q181 | varchar |  |  | SI | Estado Piel y Mucosas  |
| Q181ObsDR | varchar |  | FK | SI | Estado Piel y Mucosas  DR |
| Q182 | varchar |  |  | SI | Comentario  |
| Q183 | varchar |  |  | SI | Ojos |
| Q183ObsDR | varchar |  | FK | SI | Ojos DR |
| Q184 | varchar |  |  | SI | Nariz |
| Q184ObsDR | varchar |  | FK | SI | Nariz DR |
| Q185 | varchar |  |  | SI | Boca |
| Q185ObsDR | varchar |  | FK | SI | Boca DR |
| Q186 | varchar |  |  | SI | Oídos |
| Q186ObsDR | varchar |  | FK | SI | Oídos DR |
| Q187 | varchar |  |  | SI | Aleteo Nasal |
| Q187ObsDR | varchar |  | FK | SI | Aleteo Nasal DR |
| Q188 | varchar |  |  | SI | Retracción |
| Q188ObsDR | varchar |  | FK | SI | Retracción DR |
| Q189 | varchar |  |  | SI | Dorso |
| Q189ObsDR | varchar |  | FK | SI | Dorso DR |
| Q19 | varchar |  |  | SI | comentario 03 |
| Q190 | varchar |  |  | SI | Circunferencia Abdominal |
| Q190ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q191 | varchar |  |  | SI | Circunferencia Torácica |
| Q191ObsDR | varchar |  | FK | SI | Circunferencia Torácica DR |
| Q192 | varchar |  |  | SI | Comentario |
| Q193 | varchar |  |  | SI | Comentario |
| Q194 | varchar |  |  | SI | Comentario |
| Q195 | varchar |  |  | SI | Comentario |
| Q196 | varchar |  |  | SI | Comentario |
| Q197 | varchar |  |  | SI | Comentario |
| Q198 | varchar |  |  | SI | Comentario |
| Q20 | varchar |  |  | SI | Dispositivos Clínicos |
| Q21 | varchar |  |  | SI | Otro Dispositivo Clínico |
| Q211 | varchar |  |  | SI | Origen LPP |
| Q212 | varchar |  |  | SI | Comentarios O.LPP |
| Q213 | varchar |  |  | SI | Oxigenoterapia |
| Q213ObsDR | varchar |  | FK | SI | Oxigenoterapia DR |
| Q214 | varchar |  |  | SI | Flujo de Oxigeno |
| Q214ObsDR | varchar |  | FK | SI | Flujo de Oxigeno DR |
| Q215 | varchar |  |  | SI | Presión Arterial Media |
| Q216 | varchar |  |  | SI | Peso Ideal Hombre |
| Q217 | varchar |  |  | SI | Peso Ideal Mujer |
| Q218 | varchar |  |  | SI | IMC |
| Q219 | varchar |  |  | SI | Superficie Corporal |
| Q22 | varchar |  |  | SI | Dispositivos Artificiales |
| Q225 | varchar |  |  | SI | Parámetros Antropométricos |
| Q23 | varchar |  |  | SI | Otro dispositivo artificial |
| Q232 | varchar |  |  | SI | Acompañamiento Espiritual |
| Q24 | varchar |  |  | SI | Exámenes que Trae el Paciente |
| Q240 | varchar |  |  | SI | Antecedentes Generales |
| Q241 | varchar |  |  | SI | Aspectos Socio-Culturales Paciente |
| Q242 | varchar |  |  | SI | Aspectos Socio-Culturales Adulto Acompañante del P... |
| Q243 | varchar |  |  | SI | Examen Físico General |
| Q244 | varchar |  |  | SI | Signos Vitales |
| Q246 | varchar |  |  | SI | Inmunizaciones |
| Q247 | varchar |  |  | SI | Examen Segmentario |
| Q248 | varchar |  |  | SI | Habitos-Dependencia |
| Q249 | varchar |  |  | SI | Independencia Funcional |
| Q25 | varchar |  |  | SI | Otro Exámen |
| Q250 | varchar |  |  | SI | Instrucciones Generales y Obsevaciones Entregadas |
| Q26 | varchar |  |  | SI | Anamnesis Próxima |
| Q27 | varchar |  |  | SI | Consumo Alcohol |
| Q28 | varchar |  |  | SI | Tiempo Consumo Alcohol |
| Q29 | varchar |  |  | SI | Tabaquismo |
| Q30 | numeric |  |  | SI | N° Cigarrillos por día |
| Q31 | numeric |  |  | SI | N° Años de Consumo |
| Q32 | varchar |  |  | SI | Paquete Cigarrillos |
| Q33 | varchar |  |  | SI | Consumo de Drogas |
| Q34 | varchar |  |  | SI | Otra Droga |
| Q35 | varchar |  |  | SI | Tiempo Consumo Drogas |
| Q36 | varchar |  |  | SI | Nivel Educacional  |
| Q37 | varchar |  |  | SI | Discapacidad Física / Cognitiva (Vulnerabilidad) |
| Q38 | varchar |  |  | SI | Otra Vulnerabilidad |
| Q39 | varchar |  |  | SI | Nivel de Dependencia |
| Q40 | varchar |  |  | SI | Forma de Comunicación |
| Q41 | varchar |  |  | SI | Otra Forma de comunicación |
| Q42 | varchar |  |  | SI | Necesita Intérprete |
| Q43 | varchar |  |  | SI | comentario 04 |
| Q44 | varchar |  |  | SI | Religión |
| Q45 | varchar |  |  | SI | Otra Religión |
| Q46 | varchar |  |  | SI | Consumo de Alcohol |
| Q47 | varchar |  |  | SI | Tiempo Consumo Alcohol |
| Q48 | varchar |  |  | SI | Consumo de Tabaco |
| Q49 | numeric |  |  | SI | N° Cigarrillos por Día |
| Q50 | numeric |  |  | SI | N° de Años de Consumo |
| Q51 | varchar |  |  | SI | Paquete Cigarrillos / Año |
| Q52 | varchar |  |  | SI | Consumo de Drogas |
| Q53 | varchar |  |  | SI | Otra Droga |
| Q54 | varchar |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q55 | varchar |  |  | SI | Otra Vulnerabilidad |
| Q56 | varchar |  |  | SI | Nivel Dependencia |
| Q57 | varchar |  |  | SI | Nivel Educacional  |
| Q58 | varchar |  |  | SI | Forma de Comunicación |
| Q59 | varchar |  |  | SI | Otra forma de comunicacion |
| Q60 | varchar |  |  | SI | Necesita Intérprete |
| Q61 | varchar |  |  | SI | comentarios  05 |
| Q62 | varchar |  |  | SI | Estado General |
| Q63 | varchar |  |  | SI | Frecuencia Cardíaca |
| Q63ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca DR |
| Q64 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q64ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q65 | varchar |  |  | SI | Presión Arterial  Sistólica |
| Q65ObsDR | varchar |  | FK | SI | Presión Arterial  Sistólica DR |
| Q66 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q66ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q67 | varchar |  |  | SI | Temperatura Axilar |
| Q67ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q68 | varchar |  |  | SI | Temperatura Rectal |
| Q68ObsDR | varchar |  | FK | SI | Temperatura Rectal DR |
| Q69 | varchar |  |  | SI | Fio2 |
| Q69ObsDR | varchar |  | FK | SI | Fio2 DR |
| Q70 | varchar |  |  | SI | Saturación de Oxígeno |
| Q70ObsDR | varchar |  | FK | SI | Saturación de Oxígeno DR |
| Q71 | varchar |  |  | SI | HGT |
| Q71ObsDR | varchar |  | FK | SI | HGT DR |
| Q72 | varchar |  |  | SI | Valoración del Dolor |
| Q73 | varchar |  |  | SI | Ubicación Dolor |
| Q74 | varchar |  |  | SI | Imagen |
| Q75 | varchar |  |  | SI | Escala de Dolor (EVA) |
| Q75ObsDR | varchar |  | FK | SI | Escala de Dolor (EVA) DR |
| Q76 | varchar |  |  | SI | Razones Para no Evaluar Dolor |
| Q77 | varchar |  |  | SI | Otra Razón no Evaluado |
| Q78 | varchar |  |  | SI | Talla |
| Q78ObsDR | varchar |  | FK | SI | Talla DR |
| Q79 | varchar |  |  | SI | Circunferencia Craneana |
| Q79ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q81 | varchar |  |  | SI | Inmunizaciones |
| Q82 | varchar |  |  | SI | Otra Inmunización |
| Q83 | varchar |  |  | SI | Comentarios Examen Físico General |
| Q84 | varchar |  |  | SI | Estado Psíquico |
| Q84ObsDR | varchar |  | FK | SI | Estado Psíquico DR |
| Q85 | varchar |  |  | SI | Conciencia |
| Q85ObsDR | varchar |  | FK | SI | Conciencia DR |
| Q86 | varchar |  |  | SI | Piel |
| Q86ObsDR | varchar |  | FK | SI | Piel DR |
| Q87 | varchar |  |  | SI | Mucosas |
| Q87ObsDR | varchar |  | FK | SI | Mucosas DR |
| Q88 | varchar |  |  | SI | Cabeza - Cara |
| Q88ObsDR | varchar |  | FK | SI | Cabeza - Cara DR |
| Q89 | varchar |  |  | SI | Pupilas |
| Q890 | varchar |  |  | SI | RFM OD |
| Q890ObsDR | varchar |  | FK | SI | RFM OD DR |
| Q891 | varchar |  |  | SI | Comentario RFM OD |
| Q892 | varchar |  |  | SI | RFM OI |
| Q892ObsDR | varchar |  | FK | SI | RFM OI DR |
| Q893 | varchar |  |  | SI | Comentario RFM OI |
| Q894 | varchar |  |  | SI | R.Corneal OD |
| Q894ObsDR | varchar |  | FK | SI | R.Corneal OD DR |
| Q895 | varchar |  |  | SI | Comentario R.Corneal |
| Q896 | varchar |  |  | SI | R.Corneal OI |
| Q896ObsDR | varchar |  | FK | SI | R.Corneal OI DR |
| Q897 | varchar |  |  | SI | Comentario R.Corneal OI |
| Q89ObsDR | varchar |  | FK | SI | Pupilas DR |
| Q90 | varchar |  |  | SI | Conjuntivas |
| Q90ObsDR | varchar |  | FK | SI | Conjuntivas DR |
| Q91 | varchar |  |  | SI | Dentadura |
| Q910 | varchar |  |  | SI | Deglución |
| Q910ObsDR | varchar |  | FK | SI | Deglución DR |
| Q911 | varchar |  |  | SI | Comentario Deglución |
| Q91ObsDR | varchar |  | FK | SI | Dentadura DR |
| Q92 | varchar |  |  | SI | Lenguaje |
| Q93 | varchar |  |  | SI | Cuello |
| Q93ObsDR | varchar |  | FK | SI | Cuello DR |
| Q94 | varchar |  |  | SI | Vía Aérea |
| Q94ObsDR | varchar |  | FK | SI | Vía Aérea DR |
| Q95 | varchar |  |  | SI | Respiración |
| Q95ObsDR | varchar |  | FK | SI | Respiración DR |
| Q96 | varchar |  |  | SI | Tórax |
| Q96ObsDR | varchar |  | FK | SI | Tórax DR |
| Q97 | varchar |  |  | SI | Cardíaco |
| Q98 | varchar |  |  | SI | Ritmo Cardíaco |
| Q99 | varchar |  |  | SI | Abdomen |
| Q99ObsDR | varchar |  | FK | SI | Abdomen DR |
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