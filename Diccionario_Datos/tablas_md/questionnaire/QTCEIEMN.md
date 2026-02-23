# questionnaire.QTCEIEMN

> Ingreso Enf/Matrona Neonatología

**Schema:** questionnaire
**Columnas:** 354
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Enf/Matrona Neonatología

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Acompañado por |
| Q02 | varchar |  |  | SI | Medio de Llegada |
| Q03 | varchar |  |  | SI | Otro Medio de Llegada |
| Q04 | varchar |  |  | SI | Nombre de Contacto Emergencia |
| Q05 | varchar |  |  | SI | Teléfono Contacto Emergencia |
| Q06 | varchar |  |  | SI | Información Entregado por |
| Q07 | varchar |  |  | SI | Otro información entregada  |
| Q08 | varchar |  |  | SI | Origen del Paciente |
| Q09 | varchar |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q10 | varchar |  |  | SI | Aislamiento |
| Q100 | varchar |  |  | SI | comentario 12 |
| Q101 | varchar |  |  | SI | comentario 13 |
| Q102 | varchar |  |  | SI | comentario 14 |
| Q103 | varchar |  |  | SI | Otra Religión |
| Q104 | varchar |  |  | SI | Estado General |
| Q105 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q105ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q106 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q106ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q107 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q107ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q108 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q108ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q109 | varchar |  |  | SI | Temperatura Axilar |
| Q109ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q11 | varchar |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q110 | varchar |  |  | SI | Temperatura Rectal |
| Q110ObsDR | varchar |  | FK | SI | Temperatura Rectal DR |
| Q111 | varchar |  |  | SI | Fio2 |
| Q111ObsDR | varchar |  | FK | SI | Fio2 DR |
| Q112 | varchar |  |  | SI | Saturación de Oxigeno |
| Q112ObsDR | varchar |  | FK | SI | Saturación de Oxigeno DR |
| Q113 | varchar |  |  | SI | Otro |
| Q114 | varchar |  |  | SI | IMC |
| Q115 | varchar |  |  | SI | Superficie Corporal |
| Q116 | varchar |  |  | SI | Nombre de la Madre |
| Q117 | numeric |  |  | SI | Edad Materna |
| Q118 | varchar |  |  | SI | Gesta |
| Q119 | numeric |  |  | SI | Número de Partos |
| Q12 | varchar |  |  | SI | Paciente Porta Brazalete Identificación |
| Q120 | numeric |  |  | SI | Hijos Vivos |
| Q121 | varchar |  |  | SI | Grupo Sanguíneo Materno |
| Q122 | varchar |  |  | SI | Factor RH Materno |
| Q126 | varchar |  |  | SI | Patología del Embarazo |
| Q127 | varchar |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q128 | varchar |  |  | SI | Tipo de Parto  |
| Q129 | varchar |  |  | SI | Causa de Cesárea |
| Q13 | varchar |  |  | SI | Comentario 01 |
| Q130 | varchar |  |  | SI | Causa de Fórceps |
| Q132 | varchar |  |  | SI | Inducción del Parto |
| Q133 | varchar |  |  | SI | Tipo de Anestesia (Parto) |
| Q134 | varchar |  |  | SI | Otra Anestesia (Parto) |
| Q135 | varchar |  |  | SI | Líqudo Amniótico |
| Q136 | varchar |  |  | SI | Placenta |
| Q137 | varchar |  |  | SI | Otros (Placenta) |
| Q138 | varchar |  |  | SI | Circular de Cordón |
| Q14 | varchar |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q140 | varchar |  |  | SI | Complicaciones durante el Parto |
| Q141 | varchar |  |  | SI | Complicaciones Maternas |
| Q143 | varchar |  |  | SI | Complicaciones Fetales |
| Q144 | varchar |  |  | SI | Otras Complicaciones del Parto |
| Q145 | varchar |  |  | SI | 6. Babinsky |
| Q145ObsDR | varchar |  | FK | SI | 6. Babinsky DR |
| Q146 | date |  |  | SI | Fecha Nacimiento |
| Q147 | time |  |  | SI | Hora de Nacimiento |
| Q148 | varchar |  |  | SI | Sexo |
| Q149 | varchar |  |  | SI | Peso al Nacer |
| Q149ObsDR | varchar |  | FK | SI | Peso al Nacer DR |
| Q15 | varchar |  |  | SI | comentario 02 |
| Q150 | varchar |  |  | SI | Talla al Nacer |
| Q150ObsDR | varchar |  | FK | SI | Talla al Nacer DR |
| Q151 | varchar |  |  | SI | Circunferencia Craneana |
| Q151ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q152 | varchar |  |  | SI | Apego |
| Q153 | varchar |  |  | SI | Duración del Apego |
| Q154 | varchar |  |  | SI | Diuresis |
| Q155 | varchar |  |  | SI | Deposiciones |
| Q156 | varchar |  |  | SI | Lactancia Materna |
| Q157 | varchar |  |  | SI | Alimentación Complementaria |
| Q158 | varchar |  |  | SI | Administración Vitamina  K |
| Q159 | varchar |  |  | SI | Reanimación |
| Q16 | varchar |  |  | SI | Paciente Porta Brazalete de Alergías |
| Q160 | varchar |  |  | SI | Anomalía Congénita |
| Q161 | varchar |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q162 | numeric |  |  | SI | Semanas de Gestación 1 |
| Q163 | numeric |  |  | SI | Semanas de Gestación 2 |
| Q164 | varchar |  |  | SI | Morbilidad RN |
| Q165 | varchar |  |  | SI | Apgar 1 Minuto |
| Q166 | varchar |  |  | SI | Apgar 5 Minutos |
| Q167 | varchar |  |  | SI | Apgar 10 Minutos |
| Q168 | varchar |  |  | SI | Profilaxis Ocular |
| Q17 | varchar |  |  | SI | Comentario 03 |
| Q170 | varchar |  |  | SI | HGT |
| Q170ObsDR | varchar |  | FK | SI | HGT DR |
| Q171 | varchar |  |  | SI | Lugar del Parto |
| Q172 | varchar |  |  | SI | Otro Lugar de Parto |
| Q173 | varchar |  |  | SI | Especifique Otra Razón |
| Q174 | varchar |  |  | SI | Razones para no Evaluar Dolor |
| Q175 | varchar |  |  | SI | Escala del Dolor (EVA) |
| Q175ObsDR | varchar |  | FK | SI | Escala del Dolor (EVA) DR |
| Q176 | varchar |  |  | SI | Ubicación del Dolor |
| Q177 | varchar |  |  | SI | Valoración del Dolor |
| Q18 | varchar |  |  | SI | Dispositivos Clínicos |
| Q180 | varchar |  |  | SI | comentario 1 |
| Q181 | varchar |  |  | SI | comentario 2 |
| Q183 | varchar |  |  | SI | comentario 3 |
| Q184 | varchar |  |  | SI | comentario 4 |
| Q185 | varchar |  |  | SI | comentario 5 |
| Q186 | varchar |  |  | SI | comentario 6 |
| Q187 | varchar |  |  | SI | comentario 7 |
| Q188 | varchar |  |  | SI | comentario 8 |
| Q189 | varchar |  |  | SI | comentario 9 |
| Q19 | varchar |  |  | SI | Otro Dispositivo Clínico |
| Q190 | varchar |  |  | SI | comentario 10 |
| Q191 | varchar |  |  | SI | comentario 11 |
| Q192 | varchar |  |  | SI | comentario 12 |
| Q193 | varchar |  |  | SI | comentario 13 |
| Q194 | varchar |  |  | SI | comentario 14 |
| Q195 | varchar |  |  | SI | comentario 15 |
| Q196 | varchar |  |  | SI | comentario 16 |
| Q197 | varchar |  |  | SI | comentario 17 |
| Q198 | varchar |  |  | SI | comentario 18 |
| Q199 | varchar |  |  | SI | comentario 19 |
| Q20 | varchar |  |  | SI | Exámenes que Trae el Paciente |
| Q200 | varchar |  |  | SI | comentario 20 |
| Q201 | varchar |  |  | SI | comentario 21 |
| Q202 | varchar |  |  | SI | comentario 22 |
| Q203 | varchar |  |  | SI | comentario 23 |
| Q204 | varchar |  |  | SI | comentario 24 |
| Q205 | varchar |  |  | SI | comentario 25 |
| Q206 | varchar |  |  | SI | comentario 26 |
| Q207 | varchar |  |  | SI | comentario 27 |
| Q208 | varchar |  |  | SI | comentario 28 |
| Q209 | varchar |  |  | SI | comentario 29 |
| Q21 | varchar |  |  | SI | Otro Examen |
| Q210 | varchar |  |  | SI | comentario 30 |
| Q211 | varchar |  |  | SI | comentario 31 |
| Q212 | varchar |  |  | SI | comentario 32 |
| Q213 | varchar |  |  | SI | comentario 33 |
| Q214 | varchar |  |  | SI | comentario 34 |
| Q215 | varchar |  |  | SI | comentario 35 |
| Q216 | varchar |  |  | SI | comentario 36 |
| Q217 | varchar |  |  | SI | comentario 37 |
| Q218 | varchar |  |  | SI | comentario 38 |
| Q219 | varchar |  |  | SI | comentario 39 |
| Q22 | varchar |  |  | SI | Clínico |
| Q220 | varchar |  |  | SI | Profesional de Salud |
| Q221 | varchar |  |  | SI | Administración Vacuna BCG:  |
| Q222 | varchar |  |  | SI | Toma de PKU:  |
| Q225 | varchar |  |  | SI | LPP |
| Q225ObsDR | varchar |  | FK | SI | LPP DR |
| Q226 | varchar |  |  | SI | Grado LPP |
| Q226ObsDR | varchar |  | FK | SI | Grado LPP DR |
| Q227 | varchar |  |  | SI | Ubicación LPP |
| Q227ObsDR | varchar |  | FK | SI | Ubicación LPP DR |
| Q228 | varchar |  |  | SI | Lateralidad LPP |
| Q228ObsDR | varchar |  | FK | SI | Lateralidad LPP DR |
| Q229 | varchar |  |  | SI | Comentario LPP |
| Q23 | varchar |  |  | SI | Motivo de Ingreso |
| Q230 | varchar |  |  | SI | Otros Acompañantes |
| Q231 | varchar |  |  | SI | Comentario G.LPP |
| Q232 | varchar |  |  | SI | Comentario U.LPP |
| Q233 | varchar |  |  | SI | Comentario L.LPP |
| Q234 | varchar |  |  | SI | Origen UPP |
| Q234ObsDR | varchar |  | FK | SI | Origen UPP DR |
| Q235 | varchar |  |  | SI | Comentario OUPP |
| Q236 | varchar |  |  | SI | Antecedentes del Embarazo (RN Trasladado) |
| Q237 | varchar |  |  | SI | Fórmula Obstétrica |
| Q238 | varchar |  |  | SI | Antecedentes del Parto (RN Trasladado) |
| Q239 | varchar |  |  | SI | Nacimiento y Atención Inmediata (RN Trasladado) |
| Q24 | varchar |  |  | SI | Anamnesis Próxima |
| Q240 | varchar |  |  | SI | Presión Arterial Media |
| Q241 | varchar |  |  | SI | Oxigenoterapia |
| Q241ObsDR | varchar |  | FK | SI | Oxigenoterapia DR |
| Q242 | varchar |  |  | SI | Flujo de Oxígeno |
| Q242ObsDR | varchar |  | FK | SI | Flujo de Oxígeno DR |
| Q243 | varchar |  |  | SI | Circunferencia Torácica |
| Q243ObsDR | varchar |  | FK | SI | Circunferencia Torácica DR |
| Q244 | varchar |  |  | SI | Circunferencia Abdominal |
| Q244ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q245 | varchar |  |  | SI | Peso Ideal Hombre |
| Q246 | varchar |  |  | SI | Peso Ideal Mujer |
| Q247 | varchar |  |  | SI | Acompañamiento Espiritual |
| Q25 | varchar |  |  | SI | Religión |
| Q251 | varchar |  |  | SI | Obstetricia |
| Q252 | varchar |  |  | SI | Neomatología |
| Q253 | varchar |  |  | SI | Apgar |
| Q254 | varchar |  |  | SI | Antecedentes Generales |
| Q255 | varchar |  |  | SI | Aspectos Socio-Culturales de la Madre |
| Q256 | varchar |  |  | SI | Exámen Físico General |
| Q257 | varchar |  |  | SI | Examen Segmentario (Campos Especificos) |
| Q258 | varchar |  |  | SI | Instrucciones Generales y Observaciones |
| Q259 | varchar |  |  | SI | Signos Vitales |
| Q26 | varchar |  |  | SI | Consumo de Alcohol |
| Q260 | varchar |  |  | SI | Parámetros Antropométricos |
| Q262 | varchar |  |  | SI | Deposiciones |
| Q262ObsDR | varchar |  | FK | SI | Deposiciones DR |
| Q27 | varchar |  |  | SI | Tiempo Consumo Alcohol |
| Q28 | varchar |  |  | SI | Tabaquismo |
| Q29 | numeric |  |  | SI | N° Cigarrillos por Día |
| Q30 | numeric |  |  | SI | N° de años de Consumo |
| Q31 | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q32 | varchar |  |  | SI | Consumo de Droga |
| Q33 | varchar |  |  | SI | Otra Droga |
| Q34 | varchar |  |  | SI | Tiempo de Consumo Drogas |
| Q35 | varchar |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q36 | varchar |  |  | SI | Nivel de Dependencia |
| Q37 | varchar |  |  | SI | Nivel Educacional |
| Q38 | varchar |  |  | SI | Forma  de Comunicación |
| Q39 | varchar |  |  | SI | Otra Forma de Comunicación |
| Q40 | varchar |  |  | SI | Necesita Intérprete |
| Q41 | varchar |  |  | SI | Comentario 04 |
| Q42 | varchar |  |  | SI | Talla |
| Q42ObsDR | varchar |  | FK | SI | Talla DR |
| Q43 | varchar |  |  | SI | Peso |
| Q43ObsDR | varchar |  | FK | SI | Peso DR |
| Q44 | varchar |  |  | SI | IMC |
| Q44ObsDR | varchar |  | FK | SI | IMC DR |
| Q45 | varchar |  |  | SI | Superficie Corporal |
| Q45ObsDR | varchar |  | FK | SI | Superficie Corporal DR |
| Q46 | varchar |  |  | SI | Circunferencia Craneana |
| Q46ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q47 | varchar |  |  | SI | Comentario 05 |
| Q48 | varchar |  |  | SI | Adecuación |
| Q48ObsDR | varchar |  | FK | SI | Adecuación DR |
| Q49 | varchar |  |  | SI | Tono |
| Q49ObsDR | varchar |  | FK | SI | Tono DR |
| Q50 | varchar |  |  | SI | Actividad |
| Q50ObsDR | varchar |  | FK | SI | Actividad DR |
| Q51 | varchar |  |  | SI | 1. Moro |
| Q51ObsDR | varchar |  | FK | SI | 1. Moro DR |
| Q52 | varchar |  |  | SI | 2. Prehensión Palmar |
| Q52ObsDR | varchar |  | FK | SI | 2. Prehensión Palmar DR |
| Q53 | varchar |  |  | SI | 3. Prehesión Plantar |
| Q53ObsDR | varchar |  | FK | SI | 3. Prehesión Plantar DR |
| Q54 | varchar |  |  | SI | 4. Succión |
| Q54ObsDR | varchar |  | FK | SI | 4. Succión DR |
| Q55 | varchar |  |  | SI | 5. Marcha Automática |
| Q55ObsDR | varchar |  | FK | SI | 5. Marcha Automática DR |
| Q56 | varchar |  |  | SI | Llanto (sólo en RN con ventilación espontánea) |
| Q56ObsDR | varchar |  | FK | SI | Llanto (sólo en RN con ventilación espontánea) DR |
| Q57 | varchar |  |  | SI | Quejido |
| Q57ObsDR | varchar |  | FK | SI | Quejido DR |
| Q58 | varchar |  |  | SI | Movimiento |
| Q58ObsDR | varchar |  | FK | SI | Movimiento DR |
| Q59 | varchar |  |  | SI | Piel |
| Q59ObsDR | varchar |  | FK | SI | Piel DR |
| Q60 | varchar |  |  | SI | Mucosas |
| Q60ObsDR | varchar |  | FK | SI | Mucosas DR |
| Q61 | varchar |  |  | SI | Estado Piel y Mucosas |
| Q61ObsDR | varchar |  | FK | SI | Estado Piel y Mucosas DR |
| Q62 | varchar |  |  | SI | Cabeza - Cara |
| Q62ObsDR | varchar |  | FK | SI | Cabeza - Cara DR |
| Q63 | varchar |  |  | SI | Fontanela Anterior |
| Q63ObsDR | varchar |  | FK | SI | Fontanela Anterior DR |
| Q64 | varchar |  |  | SI | Fontanela Posterior |
| Q64ObsDR | varchar |  | FK | SI | Fontanela Posterior DR |
| Q65 | varchar |  |  | SI | Ojos |
| Q65ObsDR | varchar |  | FK | SI | Ojos DR |
| Q66 | varchar |  |  | SI | Secreción Ocular |
| Q66ObsDR | varchar |  | FK | SI | Secreción Ocular DR |
| Q67 | varchar |  |  | SI | Nariz |
| Q67ObsDR | varchar |  | FK | SI | Nariz DR |
| Q68 | varchar |  |  | SI | Boca |
| Q68ObsDR | varchar |  | FK | SI | Boca DR |
| Q69 | varchar |  |  | SI | Oídos |
| Q69ObsDR | varchar |  | FK | SI | Oídos DR |
| Q70 | varchar |  |  | SI | Vía Aérea |
| Q70ObsDR | varchar |  | FK | SI | Vía Aérea DR |
| Q71 | varchar |  |  | SI | Respiración |
| Q71ObsDR | varchar |  | FK | SI | Respiración DR |
| Q72 | varchar |  |  | SI | Aleteo Nasal |
| Q72ObsDR | varchar |  | FK | SI | Aleteo Nasal DR |
| Q73 | varchar |  |  | SI | Retracción |
| Q73ObsDR | varchar |  | FK | SI | Retracción DR |
| Q74 | varchar |  |  | SI | Ritmo Cardíaco (Frecuencia) |
| Q74ObsDR | varchar |  | FK | SI | Ritmo Cardíaco (Frecuencia) DR |
| Q75 | varchar |  |  | SI | Ritmo Cardíaco (Tipo) |
| Q75ObsDR | varchar |  | FK | SI | Ritmo Cardíaco (Tipo) DR |
| Q76 | varchar |  |  | SI | Tórax |
| Q76ObsDR | varchar |  | FK | SI | Tórax DR |
| Q77 | varchar |  |  | SI | Dorso |
| Q77ObsDR | varchar |  | FK | SI | Dorso DR |
| Q78 | varchar |  |  | SI | Abdomen |
| Q78ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q79 | varchar |  |  | SI | Cordón Umbilical |
| Q79ObsDR | varchar |  | FK | SI | Cordón Umbilical DR |
| Q80 | varchar |  |  | SI | Extremidades Superiores |
| Q80ObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q81 | varchar |  |  | SI | Genitales |
| Q81ObsDR | varchar |  | FK | SI | Genitales DR |
| Q82 | varchar |  |  | SI | Extremidades Inferiores |
| Q82ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q83 | varchar |  |  | SI | Ano |
| Q83ObsDR | varchar |  | FK | SI | Ano DR |
| Q84 | varchar |  |  | SI | Diuresis |
| Q84ObsDR | varchar |  | FK | SI | Diuresis DR |
| Q85 | varchar |  |  | SI | Deposiciones Dep |
| Q85ObsDR | varchar |  | FK | SI | Deposiciones Dep DR |
| Q86 | varchar |  |  | SI | Nombre Enfermera/o o Matrón/a |
| Q87 | varchar |  |  | SI | Comentario 06 |
| Q88 | varchar |  |  | SI | Rutinas del Servicio |
| Q89 | varchar |  |  | SI | comentario 07 |
| Q90 | varchar |  |  | SI | Normas de Ingreso |
| Q91 | varchar |  |  | SI | comentario 08 |
| Q92 | varchar |  |  | SI | Horario de Visitas |
| Q93 | varchar |  |  | SI | comentario 09 |
| Q94 | varchar |  |  | SI | Lactancia |
| Q95 | varchar |  |  | SI | comentario 10 |
| Q96 | varchar |  |  | SI | Extracción de Leche |
| Q97 | varchar |  |  | SI | comentario 11 |
| Q98 | varchar |  |  | SI | Sistemas de Monitorización y Equipos |
| Q99 | varchar |  |  | SI | Nombre de quién Recibe la Información |
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