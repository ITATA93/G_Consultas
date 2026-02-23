# questionnaire.QTCEIMOB

> Ingreso Matrón(a) Gineco-Obstétrico

**Schema:** questionnaire
**Columnas:** 380
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Matrón(a) Gineco-Obstétrico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Motivo de Ingreso |
| Q02 | varchar |  |  | SI | Acompañado por: |
| Q03 | varchar |  |  | SI | Medio de LLegada |
| Q04 | varchar |  |  | SI | Nombre Contacto Emergencia |
| Q05 | varchar |  |  | SI | Teléfono Contacto Emergencia |
| Q06 | varchar |  |  | SI | Información Entregada por: |
| Q07 | varchar |  |  | SI | Otro |
| Q08 | varchar |  |  | SI | Origen del Paciente |
| Q09 | varchar |  |  | SI | Procedencia Otro Centro Asist: Tiempo de Estadía |
| Q10 | varchar |  |  | SI | Aislamiento |
| Q100 | varchar |  |  | SI | comentario 24 |
| Q101 | varchar |  |  | SI | comentario 25 |
| Q102 | varchar |  |  | SI | comentario 26 |
| Q103 | varchar |  |  | SI | comentario 27 |
| Q104 | varchar |  |  | SI | comentario 28 |
| Q105 | varchar |  |  | SI | comentario 29 |
| Q106 | varchar |  |  | SI | comentario 30 |
| Q107 | varchar |  |  | SI | comentario 31 |
| Q108 | varchar |  |  | SI | comentario 32 |
| Q109 | varchar |  |  | SI | comentario 33 |
| Q11 | varchar |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q110 | varchar |  |  | SI | comentario 34 |
| Q111 | varchar |  |  | SI | comentario 35 |
| Q112 | varchar |  |  | SI | comentario 36 |
| Q113 | varchar |  |  | SI | comentario 37 |
| Q114 | varchar |  |  | SI | comentario 38 |
| Q115 | varchar |  |  | SI | comentario 39 |
| Q116 | varchar |  |  | SI | comentario 40 |
| Q117 | varchar |  |  | SI | LCF Feto 1 |
| Q117ObsDR | varchar |  | FK | SI | LCF Feto 1 DR |
| Q118 | varchar |  |  | SI | LCF Feto 2 |
| Q118ObsDR | varchar |  | FK | SI | LCF Feto 2 DR |
| Q119 | varchar |  |  | SI | LCF Feto 3 |
| Q119ObsDR | varchar |  | FK | SI | LCF Feto 3 DR |
| Q12 | varchar |  |  | SI | Comentario 04 |
| Q120 | varchar |  |  | SI | Movimientos Fetales |
| Q120ObsDR | varchar |  | FK | SI | Movimientos Fetales DR |
| Q121 | varchar |  |  | SI | Presentación |
| Q121ObsDR | varchar |  | FK | SI | Presentación DR |
| Q122 | varchar |  |  | SI | Dorso Fetal |
| Q122ObsDR | varchar |  | FK | SI | Dorso Fetal DR |
| Q123 | varchar |  |  | SI | Plano |
| Q123ObsDR | varchar |  | FK | SI | Plano DR |
| Q124 | varchar |  |  | SI | Dilatación Cervical (cm) |
| Q124ObsDR | varchar |  | FK | SI | Dilatación Cervical (cm) DR |
| Q125 | varchar |  |  | SI | Altura Uterina |
| Q125ObsDR | varchar |  | FK | SI | Altura Uterina DR |
| Q126 | varchar |  |  | SI | Tono Uterino |
| Q126ObsDR | varchar |  | FK | SI | Tono Uterino DR |
| Q127 | varchar |  |  | SI | Dinámica Uterina |
| Q127ObsDR | varchar |  | FK | SI | Dinámica Uterina DR |
| Q128 | varchar |  |  | SI | N° de Contracciones (en 10 min) |
| Q128ObsDR | varchar |  | FK | SI | N° de Contracciones (en 10 min) DR |
| Q129 | varchar |  |  | SI | Desaceleraciones |
| Q129ObsDR | varchar |  | FK | SI | Desaceleraciones DR |
| Q13 | varchar |  |  | SI | Paciente Porta Brazalete Identificación |
| Q130 | varchar |  |  | SI | Líquido Amniótico |
| Q130ObsDR | varchar |  | FK | SI | Líquido Amniótico DR |
| Q131 | varchar |  |  | SI | Flujo Vaginal |
| Q131ObsDR | varchar |  | FK | SI | Flujo Vaginal DR |
| Q132 | varchar |  |  | SI | Membranas |
| Q132ObsDR | varchar |  | FK | SI | Membranas DR |
| Q133 | varchar |  |  | SI | Posición |
| Q133ObsDR | varchar |  | FK | SI | Posición DR |
| Q134 | varchar |  |  | SI | Consistencia Cuello |
| Q134ObsDR | varchar |  | FK | SI | Consistencia Cuello DR |
| Q135 | varchar |  |  | SI | Borramiento |
| Q135ObsDR | varchar |  | FK | SI | Borramiento DR |
| Q136 | varchar |  |  | SI | Dilatación (bishop) |
| Q136ObsDR | varchar |  | FK | SI | Dilatación (bishop) DR |
| Q137 | varchar |  |  | SI | Apoyo Cefálico |
| Q137ObsDR | varchar |  | FK | SI | Apoyo Cefálico DR |
| Q138 | varchar |  |  | SI | Comentarios Examen Segmentario |
| Q139 | varchar |  |  | SI | Nombre de la Enfermera/Matrona |
| Q14 | varchar |  |  | SI | Paciente Porta Brazalete con Datos Completos Legib... |
| Q140 | varchar |  |  | SI | Manejo de la Cama |
| Q141 | varchar |  |  | SI | Localización del Baño |
| Q142 | varchar |  |  | SI | Horarios de Comida |
| Q143 | varchar |  |  | SI | Horarios de Visitas |
| Q144 | varchar |  |  | SI | Nombre de quién recibe la información |
| Q145 | varchar |  |  | SI | comentario 41 |
| Q146 | varchar |  |  | SI | comentario 42 |
| Q147 | varchar |  |  | SI | comentario 43 |
| Q148 | varchar |  |  | SI | comentario 44 |
| Q149 | varchar |  |  | SI | comentario 45 |
| Q15 | varchar |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q150 | varchar |  |  | SI | comentario 46 |
| Q151 | varchar |  |  | SI | comentario 47 |
| Q152 | varchar |  |  | SI | comentario 48 |
| Q153 | varchar |  |  | SI | comentario 49 |
| Q154 | varchar |  |  | SI | comentario 50 |
| Q155 | varchar |  |  | SI | comentario 51 |
| Q156 | varchar |  |  | SI | comentario 52 |
| Q157 | varchar |  |  | SI | comentario 53 |
| Q158 | varchar |  |  | SI | comentario 54 |
| Q159 | varchar |  |  | SI | comentario 55 |
| Q16 | varchar |  |  | SI | Dispositivos Artificiales |
| Q160 | varchar |  |  | SI | comentario 56 |
| Q161 | varchar |  |  | SI | comentario 57 |
| Q162 | varchar |  |  | SI | comentario 58 |
| Q163 | varchar |  |  | SI | comentario 49 |
| Q164 | varchar |  |  | SI | comentario 50 |
| Q165 | varchar |  |  | SI | comentario 51 |
| Q166 | varchar |  |  | SI | comentario 52 |
| Q167 | varchar |  |  | SI | comentario 53 |
| Q168 | varchar |  |  | SI | comentario 54 |
| Q169 | varchar |  |  | SI | comentario 55 |
| Q17 | varchar |  |  | SI | Otro Dispositivo |
| Q170 | varchar |  |  | SI | comentario 56 |
| Q171 | varchar |  |  | SI | comentario 57 |
| Q172 | varchar |  |  | SI | comentario 58 |
| Q173 | numeric |  |  | SI | Indice Bishop |
| Q174 | varchar |  |  | SI | Semanas de Gestación |
| Q174ObsDR | varchar |  | FK | SI | Semanas de Gestación DR |
| Q175 | varchar |  |  | SI | Razones para no Evaluar Dolor |
| Q176 | varchar |  |  | SI | Especifique Otra Razón |
| Q177 | varchar |  |  | SI | Ubicación Dolor |
| Q178 | varchar |  |  | SI | Pluralidad |
| Q179 | numeric |  |  | SI | Número del Bebé |
| Q18 | varchar |  |  | SI | Comentario 01 |
| Q180 | varchar |  |  | SI | Presentación |
| Q181 | numeric |  |  | SI | Semandas de Gestación |
| Q182 | numeric |  |  | SI | Días de Gestación |
| Q183 | date |  |  | SI | Fecha de Naciminento |
| Q184 | time |  |  | SI | Hora de Nacimiento |
| Q185 | varchar |  |  | SI | Tipo de Parto |
| Q186 | varchar |  |  | SI | Indicación Cesárea |
| Q187 | varchar |  |  | SI | Resultado |
| Q188 | varchar |  |  | SI | Obstetra 1 |
| Q189 | varchar |  |  | SI | Obstetra 2 |
| Q19 | varchar |  |  | SI | Comentario 02 |
| Q190 | varchar |  |  | SI | Neonatólogo |
| Q191 | varchar |  |  | SI | Registro otros Profesionales |
| Q192 | varchar |  |  | SI | Sexo |
| Q193 | numeric |  |  | SI | Peso al nacer |
| Q194 | numeric |  |  | SI | Talla al Nacer |
| Q195 | numeric |  |  | SI | Circunferencia Craneana |
| Q196 | varchar |  |  | SI | Color Líquido Amniótico |
| Q197 | varchar |  |  | SI | Cordón Alrededor del Cuello |
| Q198 | varchar |  |  | SI | Inserción del Cordón |
| Q199 | varchar |  |  | SI | Vasos del Cordón |
| Q20 | varchar |  |  | SI | Comentario 03 |
| Q200 | varchar |  |  | SI | Enviada muestra de RN de madre RH Neg. |
| Q201 | date |  |  | SI | Inicio Trabajo de Parto |
| Q202 | time |  |  | SI | Hora de Inicio Trabajo de Parto |
| Q203 | date |  |  | SI | Rotura de Membrana |
| Q204 | time |  |  | SI | Hora Rotura de Membranas |
| Q205 | numeric |  |  | SI | Duración Rotura de Membranas |
| Q206 | varchar |  |  | SI | Analgésicos / Anestésicos |
| Q207 | varchar |  |  | SI | Periné |
| Q208 | varchar |  |  | SI | Episiotomía |
| Q209 | varchar |  |  | SI | Sangramiento |
| Q21 | varchar |  |  | SI | Comentario 05 |
| Q210 | varchar |  |  | SI | Transfusión Sanguínea |
| Q211 | varchar |  |  | SI | Complicaciones del Parto |
| Q212 | varchar |  |  | SI | Complicaciones del Puerperio Inmediato |
| Q213 | varchar |  |  | SI | Estado de la Madre Post Parto |
| Q214 | varchar |  |  | SI | Esterilización Post Parto |
| Q215 | varchar |  |  | SI | Matrona Jefe |
| Q216 | varchar |  |  | SI | Médico Jefe |
| Q217 | varchar |  |  | SI | Profesional de Salud |
| Q218 | varchar |  |  | SI | Comentarios Generales GO |
| Q219 | bit |  |  | SI | Resto del examen ginecológico realizado, sin alter... |
| Q22 | varchar |  |  | SI | Comentario 06 |
| Q220 | varchar |  |  | SI | Ispeccíon |
| Q221 | varchar |  |  | SI | Tacto Vaginal |
| Q222 | varchar |  |  | SI | Especuloscopia |
| Q223 | varchar |  |  | SI | Ex. Mamas |
| Q225 | varchar |  |  | SI | Ubicación |
| Q226 | varchar |  |  | SI | Sensibilidad1 |
| Q227 | varchar |  |  | SI | Tacto Vaginal Texto |
| Q228 | varchar |  |  | SI | tacto vaginal 2 |
| Q229 | varchar |  |  | SI | Tacto vaginal 3 |
| Q23 | varchar |  |  | SI | Comentario 07 |
| Q230 | varchar |  |  | SI | especuloscopia texto |
| Q231 | varchar |  |  | SI | Ex. Mama texto |
| Q232 | varchar |  |  | SI | Ispección Texto |
| Q233 | varchar |  |  | SI | Comentario |
| Q234 | varchar |  |  | SI | LPP |
| Q234ObsDR | varchar |  | FK | SI | LPP DR |
| Q235 | varchar |  |  | SI | Grado LPP |
| Q235ObsDR | varchar |  | FK | SI | Grado LPP DR |
| Q236 | varchar |  |  | SI | Ubicación LPP |
| Q236ObsDR | varchar |  | FK | SI | Ubicación LPP DR |
| Q237 | varchar |  |  | SI | Lateralidad LPP |
| Q237ObsDR | varchar |  | FK | SI | Lateralidad LPP DR |
| Q238 | varchar |  |  | SI | Comentario LPP |
| Q239 | varchar |  |  | SI | Comentario G.LPP |
| Q24 | varchar |  |  | SI | Comentario 08 |
| Q240 | varchar |  |  | SI | Comentario U.LPP |
| Q241 | varchar |  |  | SI | Comentario L.LPP |
| Q242 | date |  |  | SI | Fecha Inicio Control Prenatal |
| Q243 | varchar |  |  | SI | Edad Gestacional al Primer Control |
| Q244 | varchar |  |  | SI | Nombre Consultorio Control Prenatal |
| Q245 | numeric |  |  | SI | N° de Control(es) Prenatal(es) |
| Q246 | varchar |  |  | SI | Atención Nivel Secundario, Alto Riesgo Obstétrico |
| Q247 | varchar |  |  | SI | Nombre Lugar Controles ARO |
| Q248 | numeric |  |  | SI | N° de Controles |
| Q249 | varchar |  |  | SI | Diagnóstico de Derivación |
| Q25 | varchar |  |  | SI | Comentario 09 |
| Q250 | varchar |  |  | SI | Otra Patología |
| Q251 | varchar |  |  | SI | Visita Guiada (Chile Crece Contigo) |
| Q252 | varchar |  |  | SI | Aspectos Socio-Culturales relevantes Progenitor Ma... |
| Q253 | varchar |  |  | SI | Presión Arterial Media |
| Q254 | varchar |  |  | SI | Oxigenoterapia |
| Q254ObsDR | varchar |  | FK | SI | Oxigenoterapia DR |
| Q255 | varchar |  |  | SI | Flujo de Oxígeno |
| Q255ObsDR | varchar |  | FK | SI | Flujo de Oxígeno DR |
| Q256 | varchar |  |  | SI | Peso Ideal Hombre |
| Q257 | varchar |  |  | SI | Peso Ideal Mujer |
| Q258 | varchar |  |  | SI | IMC |
| Q259 | varchar |  |  | SI | Superficie Corporal |
| Q26 | varchar |  |  | SI | Comentarios 10 |
| Q260 | varchar |  |  | SI | Circunferencia Craneana |
| Q260ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q261 | varchar |  |  | SI | Circunferencia Torácica |
| Q261ObsDR | varchar |  | FK | SI | Circunferencia Torácica DR |
| Q262 | varchar |  |  | SI | Circunferencia Abdominal |
| Q262ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q263 | varchar |  |  | SI | Transfusiones |
| Q264 | varchar |  |  | SI | Transfusiones |
| Q265 | varchar |  |  | SI | ¿Cuando? |
| Q266 | varchar |  |  | SI | Hospitalizaciones |
| Q267 | varchar |  |  | SI | Hospitalizaciones |
| Q268 | varchar |  |  | SI | ¿Cuando? |
| Q269 | varchar |  |  | SI | Privada de libertad |
| Q27 | varchar |  |  | SI | Dispositivos Clínicos |
| Q270 | varchar |  |  | SI | Privada de libertad |
| Q271 | varchar |  |  | SI | Observaciones |
| Q272 | varchar |  |  | SI | Usuaria trae Plan de Parto |
| Q28 | varchar |  |  | SI | Otro Dispositivo |
| Q29 | varchar |  |  | SI | Exámenes que Trae el Paciente |
| Q30 | varchar |  |  | SI | Otro Examen |
| Q31 | varchar |  |  | SI | Anamnesis Próxima |
| Q32 | varchar |  |  | SI | Religión |
| Q33 | varchar |  |  | SI | Consumo de Alcohol |
| Q34 | varchar |  |  | SI | Tiempo de Consumo Alcohol |
| Q35 | varchar |  |  | SI | Tabaquismo |
| Q36 | numeric |  |  | SI | Cigarrillos por Día |
| Q37 | numeric |  |  | SI | Años de Consumo |
| Q38 | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q39 | varchar |  |  | SI | Consumo de Drogas |
| Q40 | varchar |  |  | SI | Otra Droga |
| Q41 | varchar |  |  | SI | Discapacidad Física / Cognitiva (Vulnerabilidad) |
| Q42 | varchar |  |  | SI | Nivel de Dependencia |
| Q43 | varchar |  |  | SI | Nivel Educacional |
| Q44 | varchar |  |  | SI | Forma de Comunicación |
| Q45 | varchar |  |  | SI | Otra |
| Q46 | varchar |  |  | SI | Necesita Intérprete |
| Q47 | varchar |  |  | SI | comentario 11 |
| Q48 | varchar |  |  | SI | Estado General |
| Q49 | varchar |  |  | SI | Frecuencia Cardíaca |
| Q49ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca DR |
| Q50 | varchar |  |  | SI | P. A. Sistólica |
| Q50ObsDR | varchar |  | FK | SI | P. A. Sistólica DR |
| Q51 | varchar |  |  | SI | P. A. Diastólica |
| Q51ObsDR | varchar |  | FK | SI | P. A. Diastólica DR |
| Q52 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q52ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q53 | varchar |  |  | SI | FiO2 |
| Q53ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q54 | varchar |  |  | SI | Sat. O2 |
| Q54ObsDR | varchar |  | FK | SI | Sat. O2 DR |
| Q55 | varchar |  |  | SI | Temperatura Axilar |
| Q55ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q56 | varchar |  |  | SI | Peso |
| Q56ObsDR | varchar |  | FK | SI | Peso DR |
| Q57 | varchar |  |  | SI | Talla |
| Q57ObsDR | varchar |  | FK | SI | Talla DR |
| Q58 | varchar |  |  | SI | Valoración del Dolor |
| Q59 | varchar |  |  | SI | Escala de Dolor (EVA) |
| Q59ObsDR | varchar |  | FK | SI | Escala de Dolor (EVA) DR |
| Q60 | varchar |  |  | SI | Hemoglucotest |
| Q60ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q61 | varchar |  |  | SI | Comentarios Examen Físico General |
| Q62 | varchar |  |  | SI | Estado Psíquico |
| Q62ObsDR | varchar |  | FK | SI | Estado Psíquico DR |
| Q63 | varchar |  |  | SI | Conciencia |
| Q63ObsDR | varchar |  | FK | SI | Conciencia DR |
| Q64 | varchar |  |  | SI | Piel |
| Q64ObsDR | varchar |  | FK | SI | Piel DR |
| Q65 | varchar |  |  | SI | Mucosas |
| Q65ObsDR | varchar |  | FK | SI | Mucosas DR |
| Q66 | varchar |  |  | SI | Cabeza - Cara |
| Q66ObsDR | varchar |  | FK | SI | Cabeza - Cara DR |
| Q67 | varchar |  |  | SI | Pupilas |
| Q67ObsDR | varchar |  | FK | SI | Pupilas DR |
| Q68 | varchar |  |  | SI | Conjuntivas |
| Q68ObsDR | varchar |  | FK | SI | Conjuntivas DR |
| Q69 | varchar |  |  | SI | Dentadura |
| Q69ObsDR | varchar |  | FK | SI | Dentadura DR |
| Q70 | varchar |  |  | SI | Lenguaje |
| Q70ObsDR | varchar |  | FK | SI | Lenguaje DR |
| Q71 | varchar |  |  | SI | Cuello |
| Q71ObsDR | varchar |  | FK | SI | Cuello DR |
| Q72 | varchar |  |  | SI | Via Aérea |
| Q72ObsDR | varchar |  | FK | SI | Via Aérea DR |
| Q73 | varchar |  |  | SI | Respiración |
| Q73ObsDR | varchar |  | FK | SI | Respiración DR |
| Q74 | varchar |  |  | SI | Tórax |
| Q74ObsDR | varchar |  | FK | SI | Tórax DR |
| Q75 | varchar |  |  | SI | Cardíaco |
| Q75ObsDR | varchar |  | FK | SI | Cardíaco DR |
| Q76 | varchar |  |  | SI | Ritmo Cardíaco |
| Q76ObsDR | varchar |  | FK | SI | Ritmo Cardíaco DR |
| Q77 | varchar |  |  | SI | Mamas |
| Q77ObsDR | varchar |  | FK | SI | Mamas DR |
| Q78 | varchar |  |  | SI | Pezones |
| Q78ObsDR | varchar |  | FK | SI | Pezones DR |
| Q79 | varchar |  |  | SI | Útero |
| Q79ObsDR | varchar |  | FK | SI | Útero DR |
| Q80 | varchar |  |  | SI | Abdomen |
| Q80ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q81 | varchar |  |  | SI | Extremidades Superiores |
| Q81ObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q82 | varchar |  |  | SI | Extremidades Inferiores |
| Q82ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q83 | varchar |  |  | SI | Edema |
| Q83ObsDR | varchar |  | FK | SI | Edema DR |
| Q84 | varchar |  |  | SI | Genito-Urinario |
| Q84ObsDR | varchar |  | FK | SI | Genito-Urinario DR |
| Q85 | varchar |  |  | SI | Ano |
| Q85ObsDR | varchar |  | FK | SI | Ano DR |
| Q86 | varchar |  |  | SI | Diuresis |
| Q86ObsDR | varchar |  | FK | SI | Diuresis DR |
| Q87 | varchar |  |  | SI | Deposiciones |
| Q87ObsDR | varchar |  | FK | SI | Deposiciones DR |
| Q88 | varchar |  |  | SI | Comentario 12 |
| Q89 | varchar |  |  | SI | comentario 13 |
| Q90 | varchar |  |  | SI | comentario 14 |
| Q91 | varchar |  |  | SI | comentario 15 |
| Q92 | varchar |  |  | SI | comentario 16 |
| Q93 | varchar |  |  | SI | comentario 17 |
| Q94 | varchar |  |  | SI | comentario 18 |
| Q95 | varchar |  |  | SI | comentario 19 |
| Q96 | varchar |  |  | SI | comentario 20 |
| Q97 | varchar |  |  | SI | comentario 21 |
| Q98 | varchar |  |  | SI | comentario 22 |
| Q99 | varchar |  |  | SI | comentario 23 |
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