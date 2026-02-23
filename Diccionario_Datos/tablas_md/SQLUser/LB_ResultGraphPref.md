# SQLUser.LB_ResultGraphPref

**Schema:** SQLUser
**Columnas:** 356
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Resultados de Laboratorio**. Valores de exámenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRGP_RowID | bigint | PK |  | NO | - |
| ChildQ261DR | - |  |  | SI | Child Reference: Detalle LPP |
| LBRGP_ReportableTestItems | varchar |  |  | SI | Reportable Test Item |
| LBRGP_TestSet_DR | bigint |  | FK | SI | Ref to Test Set DR |
| Q01 | - |  |  | SI | Acompañado por |
| Q02 | - |  |  | SI | Medio de Llegada |
| Q03 | - |  |  | SI | Otro Medio de Llegada |
| Q04 | - |  |  | SI | Nombre de Contacto Emergencia |
| Q05 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q06 | - |  |  | SI | Información Entregado por |
| Q07 | - |  |  | SI | Otro información entregada |
| Q08 | - |  |  | SI | Origen del Paciente |
| Q09 | - |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q10 | - |  |  | SI | Aislamiento |
| Q100 | - |  |  | SI | comentario 12 |
| Q101 | - |  |  | SI | comentario 13 |
| Q102 | - |  |  | SI | comentario 14 |
| Q103 | - |  |  | SI | Otra Religión |
| Q104 | - |  |  | SI | Estado General |
| Q105 | - |  |  | SI | Frecuencia Cardiaca |
| Q105ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q106 | - |  |  | SI | Frecuencia Respiratoria |
| Q106ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q107 | - |  |  | SI | Presión Arterial Sistólica |
| Q107ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q108 | - |  |  | SI | Presión Arterial Diastólica |
| Q108ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q109 | - |  |  | SI | Temperatura Axilar |
| Q109ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q11 | - |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q110 | - |  |  | SI | Temperatura Rectal |
| Q110ObsDR | - |  |  | SI | Temperatura Rectal DR |
| Q111 | - |  |  | SI | Fio2 |
| Q111ObsDR | - |  |  | SI | Fio2 DR |
| Q112 | - |  |  | SI | Saturación de Oxigeno |
| Q112ObsDR | - |  |  | SI | Saturación de Oxigeno DR |
| Q113 | - |  |  | SI | Otro |
| Q114 | - |  |  | SI | IMC |
| Q115 | - |  |  | SI | Superficie Corporal |
| Q116 | - |  |  | SI | Nombre de la Madre |
| Q117 | - |  |  | SI | Edad Materna |
| Q118 | - |  |  | SI | Gesta |
| Q119 | - |  |  | SI | Número de Partos |
| Q12 | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q120 | - |  |  | SI | Hijos Vivos |
| Q121 | - |  |  | SI | Grupo Sanguíneo Materno |
| Q122 | - |  |  | SI | Factor RH Materno |
| Q126 | - |  |  | SI | Patología del Embarazo |
| Q127 | - |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q128 | - |  |  | SI | Tipo de Parto |
| Q129 | - |  |  | SI | Causa de Cesárea |
| Q13 | - |  |  | SI | Comentario 01 |
| Q130 | - |  |  | SI | Causa de Fórceps |
| Q132 | - |  |  | SI | Inducción del Parto |
| Q133 | - |  |  | SI | Tipo de Anestesia (Parto) |
| Q134 | - |  |  | SI | Otra Anestesia (Parto) |
| Q135 | - |  |  | SI | Líqudo Amniótico |
| Q136 | - |  |  | SI | Placenta |
| Q137 | - |  |  | SI | Otros (Placenta) |
| Q138 | - |  |  | SI | Circular de Cordón |
| Q14 | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q140 | - |  |  | SI | Complicaciones durante el Parto |
| Q141 | - |  |  | SI | Complicaciones Maternas |
| Q143 | - |  |  | SI | Complicaciones Fetales |
| Q144 | - |  |  | SI | Otras Complicaciones del Parto |
| Q145 | - |  |  | SI | 6. Babinsky |
| Q145ObsDR | - |  |  | SI | 6. Babinsky DR |
| Q146 | - |  |  | SI | Fecha Nacimiento |
| Q147 | - |  |  | SI | Hora de Nacimiento |
| Q148 | - |  |  | SI | Sexo |
| Q149 | - |  |  | SI | Peso al Nacer |
| Q149ObsDR | - |  |  | SI | Peso al Nacer DR |
| Q15 | - |  |  | SI | comentario 02 |
| Q150 | - |  |  | SI | Talla al Nacer |
| Q150ObsDR | - |  |  | SI | Talla al Nacer DR |
| Q151 | - |  |  | SI | Circunferencia Craneana |
| Q151ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q152 | - |  |  | SI | Apego |
| Q153 | - |  |  | SI | Duración del Apego |
| Q154 | - |  |  | SI | Diuresis |
| Q155 | - |  |  | SI | Deposiciones |
| Q156 | - |  |  | SI | Lactancia Materna |
| Q157 | - |  |  | SI | Alimentación Complementaria |
| Q158 | - |  |  | SI | Administración Vitamina  K |
| Q159 | - |  |  | SI | Reanimación |
| Q16 | - |  |  | SI | Paciente Porta Brazalete de Alergías |
| Q160 | - |  |  | SI | Anomalía Congénita |
| Q161 | - |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q162 | - |  |  | SI | Semanas de Gestación 1 |
| Q163 | - |  |  | SI | Semanas de Gestación 2 |
| Q164 | - |  |  | SI | Morbilidad RN |
| Q165 | - |  |  | SI | Apgar 1 Minuto |
| Q166 | - |  |  | SI | Apgar 5 Minutos |
| Q167 | - |  |  | SI | Apgar 10 Minutos |
| Q168 | - |  |  | SI | Profilaxis Ocular |
| Q17 | - |  |  | SI | Comentario 03 |
| Q170 | - |  |  | SI | HGT |
| Q170ObsDR | - |  |  | SI | HGT DR |
| Q171 | - |  |  | SI | Lugar del Parto |
| Q172 | - |  |  | SI | Otro Lugar de Parto |
| Q173 | - |  |  | SI | Especifique Otra Razón |
| Q174 | - |  |  | SI | Razones para no Evaluar Dolor |
| Q175 | - |  |  | SI | Escala del Dolor (EVA) |
| Q175ObsDR | - |  |  | SI | Escala del Dolor (EVA) DR |
| Q176 | - |  |  | SI | Ubicación del Dolor |
| Q177 | - |  |  | SI | Valoración del Dolor |
| Q18 | - |  |  | SI | Dispositivos Clínicos |
| Q180 | - |  |  | SI | comentario 1 |
| Q181 | - |  |  | SI | comentario 2 |
| Q183 | - |  |  | SI | comentario 3 |
| Q184 | - |  |  | SI | comentario 4 |
| Q185 | - |  |  | SI | comentario 5 |
| Q186 | - |  |  | SI | comentario 6 |
| Q187 | - |  |  | SI | comentario 7 |
| Q188 | - |  |  | SI | comentario 8 |
| Q189 | - |  |  | SI | comentario 9 |
| Q19 | - |  |  | SI | Otro Dispositivo Clínico |
| Q190 | - |  |  | SI | comentario 10 |
| Q191 | - |  |  | SI | comentario 11 |
| Q192 | - |  |  | SI | comentario 12 |
| Q193 | - |  |  | SI | comentario 13 |
| Q194 | - |  |  | SI | comentario 14 |
| Q195 | - |  |  | SI | comentario 15 |
| Q196 | - |  |  | SI | comentario 16 |
| Q197 | - |  |  | SI | comentario 17 |
| Q198 | - |  |  | SI | comentario 18 |
| Q199 | - |  |  | SI | comentario 19 |
| Q20 | - |  |  | SI | Exámenes que Trae el Paciente |
| Q200 | - |  |  | SI | comentario 20 |
| Q201 | - |  |  | SI | comentario 21 |
| Q202 | - |  |  | SI | comentario 22 |
| Q203 | - |  |  | SI | comentario 23 |
| Q204 | - |  |  | SI | comentario 24 |
| Q205 | - |  |  | SI | comentario 25 |
| Q206 | - |  |  | SI | comentario 26 |
| Q207 | - |  |  | SI | comentario 27 |
| Q208 | - |  |  | SI | comentario 28 |
| Q209 | - |  |  | SI | comentario 29 |
| Q21 | - |  |  | SI | Otro Examen |
| Q210 | - |  |  | SI | comentario 30 |
| Q211 | - |  |  | SI | comentario 31 |
| Q212 | - |  |  | SI | comentario 32 |
| Q213 | - |  |  | SI | comentario 33 |
| Q214 | - |  |  | SI | comentario 34 |
| Q215 | - |  |  | SI | comentario 35 |
| Q216 | - |  |  | SI | comentario 36 |
| Q217 | - |  |  | SI | comentario 37 |
| Q218 | - |  |  | SI | comentario 38 |
| Q219 | - |  |  | SI | comentario 39 |
| Q22 | - |  |  | SI | Clínico |
| Q220 | - |  |  | SI | Profesional de Salud |
| Q221 | - |  |  | SI | Administración Vacuna BCG: |
| Q222 | - |  |  | SI | Toma de PKU: |
| Q225 | - |  |  | SI | LPP |
| Q225ObsDR | - |  |  | SI | LPP DR |
| Q226 | - |  |  | SI | Grado LPP |
| Q226ObsDR | - |  |  | SI | Grado LPP DR |
| Q227 | - |  |  | SI | Ubicación LPP |
| Q227ObsDR | - |  |  | SI | Ubicación LPP DR |
| Q228 | - |  |  | SI | Lateralidad LPP |
| Q228ObsDR | - |  |  | SI | Lateralidad LPP DR |
| Q229 | - |  |  | SI | Comentario LPP |
| Q23 | - |  |  | SI | Motivo de Ingreso |
| Q230 | - |  |  | SI | Otros Acompañantes |
| Q231 | - |  |  | SI | Comentario G.LPP |
| Q232 | - |  |  | SI | Comentario U.LPP |
| Q233 | - |  |  | SI | Comentario L.LPP |
| Q234 | - |  |  | SI | Origen UPP |
| Q234ObsDR | - |  |  | SI | Origen UPP DR |
| Q235 | - |  |  | SI | Comentario OUPP |
| Q236 | - |  |  | SI | Antecedentes del Embarazo (RN Trasladado) |
| Q237 | - |  |  | SI | Fórmula Obstétrica |
| Q238 | - |  |  | SI | Antecedentes del Parto (RN Trasladado) |
| Q239 | - |  |  | SI | Nacimiento y Atención Inmediata (RN Trasladado) |
| Q24 | - |  |  | SI | Anamnesis Próxima |
| Q240 | - |  |  | SI | Presión Arterial Media |
| Q241 | - |  |  | SI | Oxigenoterapia |
| Q241ObsDR | - |  |  | SI | Oxigenoterapia DR |
| Q242 | - |  |  | SI | Flujo de Oxígeno |
| Q242ObsDR | - |  |  | SI | Flujo de Oxígeno DR |
| Q243 | - |  |  | SI | Circunferencia Torácica |
| Q243ObsDR | - |  |  | SI | Circunferencia Torácica DR |
| Q244 | - |  |  | SI | Circunferencia Abdominal |
| Q244ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q245 | - |  |  | SI | Peso Ideal Hombre |
| Q246 | - |  |  | SI | Peso Ideal Mujer |
| Q25 | - |  |  | SI | Religión |
| Q251 | - |  |  | SI | Obstetricia |
| Q252 | - |  |  | SI | Neomatología |
| Q253 | - |  |  | SI | Apgar |
| Q254 | - |  |  | SI | Antecedentes Generales |
| Q255 | - |  |  | SI | Aspectos Socio-Culturales de la Madre |
| Q256 | - |  |  | SI | Exámen Físico General |
| Q257 | - |  |  | SI | Examen Segmentario (Campos Especificos) |
| Q258 | - |  |  | SI | Instrucciones Generales y Observaciones |
| Q259 | - |  |  | SI | Signos Vitales |
| Q26 | - |  |  | SI | Consumo de Alcohol |
| Q260 | - |  |  | SI | Parámetros Antropométricos |
| Q262 | - |  |  | SI | Deposiciones |
| Q262ObsDR | - |  |  | SI | Deposiciones DR |
| Q27 | - |  |  | SI | Tiempo Consumo Alcohol |
| Q28 | - |  |  | SI | Tabaquismo |
| Q29 | - |  |  | SI | N° Cigarrillos por Día |
| Q30 | - |  |  | SI | N° de años de Consumo |
| Q31 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q32 | - |  |  | SI | Consumo de Droga |
| Q33 | - |  |  | SI | Otra Droga |
| Q34 | - |  |  | SI | Tiempo de Consumo Drogas |
| Q35 | - |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q36 | - |  |  | SI | Nivel de Dependencia |
| Q37 | - |  |  | SI | Nivel Educacional |
| Q38 | - |  |  | SI | Forma  de Comunicación |
| Q39 | - |  |  | SI | Otra Forma de Comunicación |
| Q40 | - |  |  | SI | Necesita Intérprete |
| Q41 | - |  |  | SI | Comentario 04 |
| Q42 | - |  |  | SI | Talla |
| Q42ObsDR | - |  |  | SI | Talla DR |
| Q43 | - |  |  | SI | Peso |
| Q43ObsDR | - |  |  | SI | Peso DR |
| Q44 | - |  |  | SI | IMC |
| Q44ObsDR | - |  |  | SI | IMC DR |
| Q45 | - |  |  | SI | Superficie Corporal |
| Q45ObsDR | - |  |  | SI | Superficie Corporal DR |
| Q46 | - |  |  | SI | Circunferencia Craneana |
| Q46ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q47 | - |  |  | SI | Comentario 05 |
| Q48 | - |  |  | SI | Adecuación |
| Q48ObsDR | - |  |  | SI | Adecuación DR |
| Q49 | - |  |  | SI | Tono |
| Q49ObsDR | - |  |  | SI | Tono DR |
| Q50 | - |  |  | SI | Actividad |
| Q50ObsDR | - |  |  | SI | Actividad DR |
| Q51 | - |  |  | SI | 1. Moro |
| Q51ObsDR | - |  |  | SI | 1. Moro DR |
| Q52 | - |  |  | SI | 2. Prehensión Palmar |
| Q52ObsDR | - |  |  | SI | 2. Prehensión Palmar DR |
| Q53 | - |  |  | SI | 3. Prehesión Plantar |
| Q53ObsDR | - |  |  | SI | 3. Prehesión Plantar DR |
| Q54 | - |  |  | SI | 4. Succión |
| Q54ObsDR | - |  |  | SI | 4. Succión DR |
| Q55 | - |  |  | SI | 5. Marcha Automática |
| Q55ObsDR | - |  |  | SI | 5. Marcha Automática DR |
| Q56 | - |  |  | SI | Llanto (sólo en RN con ventilación espontánea) |
| Q56ObsDR | - |  |  | SI | Llanto (sólo en RN con ventilación espontánea) DR |
| Q57 | - |  |  | SI | Quejido |
| Q57ObsDR | - |  |  | SI | Quejido DR |
| Q58 | - |  |  | SI | Movimiento |
| Q58ObsDR | - |  |  | SI | Movimiento DR |
| Q59 | - |  |  | SI | Piel |
| Q59ObsDR | - |  |  | SI | Piel DR |
| Q60 | - |  |  | SI | Mucosas |
| Q60ObsDR | - |  |  | SI | Mucosas DR |
| Q61 | - |  |  | SI | Estado Piel y Mucosas |
| Q61ObsDR | - |  |  | SI | Estado Piel y Mucosas DR |
| Q62 | - |  |  | SI | Cabeza - Cara |
| Q62ObsDR | - |  |  | SI | Cabeza - Cara DR |
| Q63 | - |  |  | SI | Fontanela Anterior |
| Q63ObsDR | - |  |  | SI | Fontanela Anterior DR |
| Q64 | - |  |  | SI | Fontanela Posterior |
| Q64ObsDR | - |  |  | SI | Fontanela Posterior DR |
| Q65 | - |  |  | SI | Ojos |
| Q65ObsDR | - |  |  | SI | Ojos DR |
| Q66 | - |  |  | SI | Secreción Ocular |
| Q66ObsDR | - |  |  | SI | Secreción Ocular DR |
| Q67 | - |  |  | SI | Nariz |
| Q67ObsDR | - |  |  | SI | Nariz DR |
| Q68 | - |  |  | SI | Boca |
| Q68ObsDR | - |  |  | SI | Boca DR |
| Q69 | - |  |  | SI | Oídos |
| Q69ObsDR | - |  |  | SI | Oídos DR |
| Q70 | - |  |  | SI | Vía Aérea |
| Q70ObsDR | - |  |  | SI | Vía Aérea DR |
| Q71 | - |  |  | SI | Respiración |
| Q71ObsDR | - |  |  | SI | Respiración DR |
| Q72 | - |  |  | SI | Aleteo Nasal |
| Q72ObsDR | - |  |  | SI | Aleteo Nasal DR |
| Q73 | - |  |  | SI | Retracción |
| Q73ObsDR | - |  |  | SI | Retracción DR |
| Q74 | - |  |  | SI | Ritmo Cardíaco (Frecuencia) |
| Q74ObsDR | - |  |  | SI | Ritmo Cardíaco (Frecuencia) DR |
| Q75 | - |  |  | SI | Ritmo Cardíaco (Tipo) |
| Q75ObsDR | - |  |  | SI | Ritmo Cardíaco (Tipo) DR |
| Q76 | - |  |  | SI | Tórax |
| Q76ObsDR | - |  |  | SI | Tórax DR |
| Q77 | - |  |  | SI | Dorso |
| Q77ObsDR | - |  |  | SI | Dorso DR |
| Q78 | - |  |  | SI | Abdomen |
| Q78ObsDR | - |  |  | SI | Abdomen DR |
| Q79 | - |  |  | SI | Cordón Umbilical |
| Q79ObsDR | - |  |  | SI | Cordón Umbilical DR |
| Q80 | - |  |  | SI | Extremidades Superiores |
| Q80ObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q81 | - |  |  | SI | Genitales |
| Q81ObsDR | - |  |  | SI | Genitales DR |
| Q82 | - |  |  | SI | Extremidades Inferiores |
| Q82ObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q83 | - |  |  | SI | Ano |
| Q83ObsDR | - |  |  | SI | Ano DR |
| Q84 | - |  |  | SI | Diuresis |
| Q84ObsDR | - |  |  | SI | Diuresis DR |
| Q85 | - |  |  | SI | Deposiciones Dep |
| Q85ObsDR | - |  |  | SI | Deposiciones Dep DR |
| Q86 | - |  |  | SI | Nombre Enfermera/o o Matrón/a |
| Q87 | - |  |  | SI | Comentario 06 |
| Q88 | - |  |  | SI | Rutinas del Servicio |
| Q89 | - |  |  | SI | comentario 07 |
| Q90 | - |  |  | SI | Normas de Ingreso |
| Q91 | - |  |  | SI | comentario 08 |
| Q92 | - |  |  | SI | Horario de Visitas |
| Q93 | - |  |  | SI | comentario 09 |
| Q94 | - |  |  | SI | Lactancia |
| Q95 | - |  |  | SI | comentario 10 |
| Q96 | - |  |  | SI | Extracción de Leche |
| Q97 | - |  |  | SI | comentario 11 |
| Q98 | - |  |  | SI | Sistemas de Monitorización y Equipos |
| Q99 | - |  |  | SI | Nombre de quién Recibe la Información |
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