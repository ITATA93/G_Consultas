# SQLUser.LB_EpisodeAlternateNumber

**Schema:** SQLUser
**Columnas:** 377
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPAN_ParRef | bigint | PK |  | NO | Parent |
| ChildQ224DR | - |  |  | SI | Child Reference: Inspección |
| LBEPAN_Department_DR | bigint |  | FK | SI | Department |
| LBEPAN_Function | varchar |  |  | SI | Function
Indicates the purpose of the number and ... |
| LBEPAN_LabSiteList | varchar |  |  | SI | Lab Site List |
| LBEPAN_Number | varchar |  |  | NO | Numner |
| LBEPAN_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Motivo de Ingreso |
| Q02 | - |  |  | SI | Acompañado por: |
| Q03 | - |  |  | SI | Medio de LLegada |
| Q04 | - |  |  | SI | Nombre Contacto Emergencia |
| Q05 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q06 | - |  |  | SI | Información Entregada por: |
| Q07 | - |  |  | SI | Otro |
| Q08 | - |  |  | SI | Origen del Paciente |
| Q09 | - |  |  | SI | Procedencia Otro Centro Asist: Tiempo de Estadía |
| Q10 | - |  |  | SI | Aislamiento |
| Q100 | - |  |  | SI | comentario 24 |
| Q101 | - |  |  | SI | comentario 25 |
| Q102 | - |  |  | SI | comentario 26 |
| Q103 | - |  |  | SI | comentario 27 |
| Q104 | - |  |  | SI | comentario 28 |
| Q105 | - |  |  | SI | comentario 29 |
| Q106 | - |  |  | SI | comentario 30 |
| Q107 | - |  |  | SI | comentario 31 |
| Q108 | - |  |  | SI | comentario 32 |
| Q109 | - |  |  | SI | comentario 33 |
| Q11 | - |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q110 | - |  |  | SI | comentario 34 |
| Q111 | - |  |  | SI | comentario 35 |
| Q112 | - |  |  | SI | comentario 36 |
| Q113 | - |  |  | SI | comentario 37 |
| Q114 | - |  |  | SI | comentario 38 |
| Q115 | - |  |  | SI | comentario 39 |
| Q116 | - |  |  | SI | comentario 40 |
| Q117 | - |  |  | SI | LCF Feto 1 |
| Q117ObsDR | - |  |  | SI | LCF Feto 1 DR |
| Q118 | - |  |  | SI | LCF Feto 2 |
| Q118ObsDR | - |  |  | SI | LCF Feto 2 DR |
| Q119 | - |  |  | SI | LCF Feto 3 |
| Q119ObsDR | - |  |  | SI | LCF Feto 3 DR |
| Q12 | - |  |  | SI | Comentario 04 |
| Q120 | - |  |  | SI | Movimientos Fetales |
| Q120ObsDR | - |  |  | SI | Movimientos Fetales DR |
| Q121 | - |  |  | SI | Presentación |
| Q121ObsDR | - |  |  | SI | Presentación DR |
| Q122 | - |  |  | SI | Dorso Fetal |
| Q122ObsDR | - |  |  | SI | Dorso Fetal DR |
| Q123 | - |  |  | SI | Plano |
| Q123ObsDR | - |  |  | SI | Plano DR |
| Q124 | - |  |  | SI | Dilatación Cervical (cm) |
| Q124ObsDR | - |  |  | SI | Dilatación Cervical (cm) DR |
| Q125 | - |  |  | SI | Altura Uterina |
| Q125ObsDR | - |  |  | SI | Altura Uterina DR |
| Q126 | - |  |  | SI | Tono Uterino |
| Q126ObsDR | - |  |  | SI | Tono Uterino DR |
| Q127 | - |  |  | SI | Dinámica Uterina |
| Q127ObsDR | - |  |  | SI | Dinámica Uterina DR |
| Q128 | - |  |  | SI | N° de Contracciones (en 10 min) |
| Q128ObsDR | - |  |  | SI | N° de Contracciones (en 10 min) DR |
| Q129 | - |  |  | SI | Desaceleraciones |
| Q129ObsDR | - |  |  | SI | Desaceleraciones DR |
| Q13 | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q130 | - |  |  | SI | Líquido Amniótico |
| Q130ObsDR | - |  |  | SI | Líquido Amniótico DR |
| Q131 | - |  |  | SI | Flujo Vaginal |
| Q131ObsDR | - |  |  | SI | Flujo Vaginal DR |
| Q132 | - |  |  | SI | Membranas |
| Q132ObsDR | - |  |  | SI | Membranas DR |
| Q133 | - |  |  | SI | Posición |
| Q133ObsDR | - |  |  | SI | Posición DR |
| Q134 | - |  |  | SI | Consistencia Cuello |
| Q134ObsDR | - |  |  | SI | Consistencia Cuello DR |
| Q135 | - |  |  | SI | Borramiento |
| Q135ObsDR | - |  |  | SI | Borramiento DR |
| Q136 | - |  |  | SI | Dilatación (bishop) |
| Q136ObsDR | - |  |  | SI | Dilatación (bishop) DR |
| Q137 | - |  |  | SI | Apoyo Cefálico |
| Q137ObsDR | - |  |  | SI | Apoyo Cefálico DR |
| Q138 | - |  |  | SI | Comentarios Examen Segmentario |
| Q139 | - |  |  | SI | Nombre de la Enfermera/Matrona |
| Q14 | - |  |  | SI | Paciente Porta Brazalete con Datos Completos Legib... |
| Q140 | - |  |  | SI | Manejo de la Cama |
| Q141 | - |  |  | SI | Localización del Baño |
| Q142 | - |  |  | SI | Horarios de Comida |
| Q143 | - |  |  | SI | Horarios de Visitas |
| Q144 | - |  |  | SI | Nombre de quién recibe la información |
| Q145 | - |  |  | SI | comentario 41 |
| Q146 | - |  |  | SI | comentario 42 |
| Q147 | - |  |  | SI | comentario 43 |
| Q148 | - |  |  | SI | comentario 44 |
| Q149 | - |  |  | SI | comentario 45 |
| Q15 | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q150 | - |  |  | SI | comentario 46 |
| Q151 | - |  |  | SI | comentario 47 |
| Q152 | - |  |  | SI | comentario 48 |
| Q153 | - |  |  | SI | comentario 49 |
| Q154 | - |  |  | SI | comentario 50 |
| Q155 | - |  |  | SI | comentario 51 |
| Q156 | - |  |  | SI | comentario 52 |
| Q157 | - |  |  | SI | comentario 53 |
| Q158 | - |  |  | SI | comentario 54 |
| Q159 | - |  |  | SI | comentario 55 |
| Q16 | - |  |  | SI | Dispositivos Artificiales |
| Q160 | - |  |  | SI | comentario 56 |
| Q161 | - |  |  | SI | comentario 57 |
| Q162 | - |  |  | SI | comentario 58 |
| Q163 | - |  |  | SI | comentario 49 |
| Q164 | - |  |  | SI | comentario 50 |
| Q165 | - |  |  | SI | comentario 51 |
| Q166 | - |  |  | SI | comentario 52 |
| Q167 | - |  |  | SI | comentario 53 |
| Q168 | - |  |  | SI | comentario 54 |
| Q169 | - |  |  | SI | comentario 55 |
| Q17 | - |  |  | SI | Otro Dispositivo |
| Q170 | - |  |  | SI | comentario 56 |
| Q171 | - |  |  | SI | comentario 57 |
| Q172 | - |  |  | SI | comentario 58 |
| Q173 | - |  |  | SI | Indice Bishop |
| Q174 | - |  |  | SI | Semanas de Gestación |
| Q174ObsDR | - |  |  | SI | Semanas de Gestación DR |
| Q175 | - |  |  | SI | Razones para no Evaluar Dolor |
| Q176 | - |  |  | SI | Especifique Otra Razón |
| Q177 | - |  |  | SI | Ubicación Dolor |
| Q178 | - |  |  | SI | Pluralidad |
| Q179 | - |  |  | SI | Número del Bebé |
| Q18 | - |  |  | SI | Comentario 01 |
| Q180 | - |  |  | SI | Presentación |
| Q181 | - |  |  | SI | Semandas de Gestación |
| Q182 | - |  |  | SI | Días de Gestación |
| Q183 | - |  |  | SI | Fecha de Naciminento |
| Q184 | - |  |  | SI | Hora de Nacimiento |
| Q185 | - |  |  | SI | Tipo de Parto |
| Q186 | - |  |  | SI | Indicación Cesárea |
| Q187 | - |  |  | SI | Resultado |
| Q188 | - |  |  | SI | Obstetra 1 |
| Q189 | - |  |  | SI | Obstetra 2 |
| Q19 | - |  |  | SI | Comentario 02 |
| Q190 | - |  |  | SI | Neonatólogo |
| Q191 | - |  |  | SI | Registro otros Profesionales |
| Q192 | - |  |  | SI | Sexo |
| Q193 | - |  |  | SI | Peso al nacer |
| Q194 | - |  |  | SI | Talla al Nacer |
| Q195 | - |  |  | SI | Circunferencia Craneana |
| Q196 | - |  |  | SI | Color Líquido Amniótico |
| Q197 | - |  |  | SI | Cordón Alrededor del Cuello |
| Q198 | - |  |  | SI | Inserción del Cordón |
| Q199 | - |  |  | SI | Vasos del Cordón |
| Q20 | - |  |  | SI | Comentario 03 |
| Q200 | - |  |  | SI | Enviada muestra de RN de madre RH Neg. |
| Q201 | - |  |  | SI | Inicio Trabajo de Parto |
| Q202 | - |  |  | SI | Hora de Inicio Trabajo de Parto |
| Q203 | - |  |  | SI | Rotura de Membrana |
| Q204 | - |  |  | SI | Hora Rotura de Membranas |
| Q205 | - |  |  | SI | Duración Rotura de Membranas |
| Q206 | - |  |  | SI | Analgésicos / Anestésicos |
| Q207 | - |  |  | SI | Periné |
| Q208 | - |  |  | SI | Episiotomía |
| Q209 | - |  |  | SI | Sangramiento |
| Q21 | - |  |  | SI | Comentario 05 |
| Q210 | - |  |  | SI | Transfusión Sanguínea |
| Q211 | - |  |  | SI | Complicaciones del Parto |
| Q212 | - |  |  | SI | Complicaciones del Puerperio Inmediato |
| Q213 | - |  |  | SI | Estado de la Madre Post Parto |
| Q214 | - |  |  | SI | Esterilización Post Parto |
| Q215 | - |  |  | SI | Matrona Jefe |
| Q216 | - |  |  | SI | Médico Jefe |
| Q217 | - |  |  | SI | Profesional de Salud |
| Q218 | - |  |  | SI | Comentarios Generales GO |
| Q219 | - |  |  | SI | Resto del examen ginecológico realizado, sin alter... |
| Q22 | - |  |  | SI | Comentario 06 |
| Q220 | - |  |  | SI | Ispeccíon |
| Q221 | - |  |  | SI | Tacto Vaginal |
| Q222 | - |  |  | SI | Especuloscopia |
| Q223 | - |  |  | SI | Ex. Mamas |
| Q225 | - |  |  | SI | Ubicación |
| Q226 | - |  |  | SI | Sensibilidad1 |
| Q227 | - |  |  | SI | Tacto Vaginal Texto |
| Q228 | - |  |  | SI | tacto vaginal 2 |
| Q229 | - |  |  | SI | Tacto vaginal 3 |
| Q23 | - |  |  | SI | Comentario 07 |
| Q230 | - |  |  | SI | especuloscopia texto |
| Q231 | - |  |  | SI | Ex. Mama texto |
| Q232 | - |  |  | SI | Ispección Texto |
| Q233 | - |  |  | SI | Comentario |
| Q234 | - |  |  | SI | LPP |
| Q234ObsDR | - |  |  | SI | LPP DR |
| Q235 | - |  |  | SI | Grado LPP |
| Q235ObsDR | - |  |  | SI | Grado LPP DR |
| Q236 | - |  |  | SI | Ubicación LPP |
| Q236ObsDR | - |  |  | SI | Ubicación LPP DR |
| Q237 | - |  |  | SI | Lateralidad LPP |
| Q237ObsDR | - |  |  | SI | Lateralidad LPP DR |
| Q238 | - |  |  | SI | Comentario LPP |
| Q239 | - |  |  | SI | Comentario G.LPP |
| Q24 | - |  |  | SI | Comentario 08 |
| Q240 | - |  |  | SI | Comentario U.LPP |
| Q241 | - |  |  | SI | Comentario L.LPP |
| Q242 | - |  |  | SI | Fecha Inicio Control Prenatal |
| Q243 | - |  |  | SI | Edad Gestacional al Primer Control |
| Q244 | - |  |  | SI | Nombre Consultorio Control Prenatal |
| Q245 | - |  |  | SI | N° de Control(es) Prenatal(es) |
| Q246 | - |  |  | SI | Atención Nivel Secundario, Alto Riesgo Obstétrico |
| Q247 | - |  |  | SI | Nombre Lugar Controles ARO |
| Q248 | - |  |  | SI | N° de Controles |
| Q249 | - |  |  | SI | Diagnóstico de Derivación |
| Q25 | - |  |  | SI | Comentario 09 |
| Q250 | - |  |  | SI | Otra Patología |
| Q251 | - |  |  | SI | Visita Guiada (Chile Crece Contigo) |
| Q252 | - |  |  | SI | Aspectos Socio-Culturales relevantes Progenitor Ma... |
| Q253 | - |  |  | SI | Presión Arterial Media |
| Q254 | - |  |  | SI | Oxigenoterapia |
| Q254ObsDR | - |  |  | SI | Oxigenoterapia DR |
| Q255 | - |  |  | SI | Flujo de Oxígeno |
| Q255ObsDR | - |  |  | SI | Flujo de Oxígeno DR |
| Q256 | - |  |  | SI | Peso Ideal Hombre |
| Q257 | - |  |  | SI | Peso Ideal Mujer |
| Q258 | - |  |  | SI | IMC |
| Q259 | - |  |  | SI | Superficie Corporal |
| Q26 | - |  |  | SI | Comentarios 10 |
| Q260 | - |  |  | SI | Circunferencia Craneana |
| Q260ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q261 | - |  |  | SI | Circunferencia Torácica |
| Q261ObsDR | - |  |  | SI | Circunferencia Torácica DR |
| Q262 | - |  |  | SI | Circunferencia Abdominal |
| Q262ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q27 | - |  |  | SI | Dispositivos Clínicos |
| Q28 | - |  |  | SI | Otro Dispositivo |
| Q29 | - |  |  | SI | Exámenes que Trae el Paciente |
| Q30 | - |  |  | SI | Otro Examen |
| Q31 | - |  |  | SI | Anamnesis Próxima |
| Q32 | - |  |  | SI | Religión |
| Q33 | - |  |  | SI | Consumo de Alcohol |
| Q34 | - |  |  | SI | Tiempo de Consumo Alcohol |
| Q35 | - |  |  | SI | Tabaquismo |
| Q36 | - |  |  | SI | Cigarrillos por Día |
| Q37 | - |  |  | SI | Años de Consumo |
| Q38 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q39 | - |  |  | SI | Consumo de Drogas |
| Q40 | - |  |  | SI | Otra Droga |
| Q41 | - |  |  | SI | Discapacidad Física / Cognitiva (Vulnerabilidad) |
| Q42 | - |  |  | SI | Nivel de Dependencia |
| Q43 | - |  |  | SI | Nivel Educacional |
| Q44 | - |  |  | SI | Forma de Comunicación |
| Q45 | - |  |  | SI | Otra |
| Q46 | - |  |  | SI | Necesita Intérprete |
| Q47 | - |  |  | SI | comentario 11 |
| Q48 | - |  |  | SI | Estado General |
| Q49 | - |  |  | SI | Frecuencia Cardíaca |
| Q49ObsDR | - |  |  | SI | Frecuencia Cardíaca DR |
| Q50 | - |  |  | SI | P. A. Sistólica |
| Q50ObsDR | - |  |  | SI | P. A. Sistólica DR |
| Q51 | - |  |  | SI | P. A. Diastólica |
| Q51ObsDR | - |  |  | SI | P. A. Diastólica DR |
| Q52 | - |  |  | SI | Frecuencia Respiratoria |
| Q52ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q53 | - |  |  | SI | FiO2 |
| Q53ObsDR | - |  |  | SI | FiO2 DR |
| Q54 | - |  |  | SI | Sat. O2 |
| Q54ObsDR | - |  |  | SI | Sat. O2 DR |
| Q55 | - |  |  | SI | Temperatura Axilar |
| Q55ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q56 | - |  |  | SI | Peso |
| Q56ObsDR | - |  |  | SI | Peso DR |
| Q57 | - |  |  | SI | Talla |
| Q57ObsDR | - |  |  | SI | Talla DR |
| Q58 | - |  |  | SI | Valoración del Dolor |
| Q59 | - |  |  | SI | Escala de Dolor (EVA) |
| Q59ObsDR | - |  |  | SI | Escala de Dolor (EVA) DR |
| Q60 | - |  |  | SI | Hemoglucotest |
| Q60ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q61 | - |  |  | SI | Comentarios Examen Físico General |
| Q62 | - |  |  | SI | Estado Psíquico |
| Q62ObsDR | - |  |  | SI | Estado Psíquico DR |
| Q63 | - |  |  | SI | Conciencia |
| Q63ObsDR | - |  |  | SI | Conciencia DR |
| Q64 | - |  |  | SI | Piel |
| Q64ObsDR | - |  |  | SI | Piel DR |
| Q65 | - |  |  | SI | Mucosas |
| Q65ObsDR | - |  |  | SI | Mucosas DR |
| Q66 | - |  |  | SI | Cabeza - Cara |
| Q66ObsDR | - |  |  | SI | Cabeza - Cara DR |
| Q67 | - |  |  | SI | Pupilas |
| Q67ObsDR | - |  |  | SI | Pupilas DR |
| Q68 | - |  |  | SI | Conjuntivas |
| Q68ObsDR | - |  |  | SI | Conjuntivas DR |
| Q69 | - |  |  | SI | Dentadura |
| Q69ObsDR | - |  |  | SI | Dentadura DR |
| Q70 | - |  |  | SI | Lenguaje |
| Q70ObsDR | - |  |  | SI | Lenguaje DR |
| Q71 | - |  |  | SI | Cuello |
| Q71ObsDR | - |  |  | SI | Cuello DR |
| Q72 | - |  |  | SI | Via Aérea |
| Q72ObsDR | - |  |  | SI | Via Aérea DR |
| Q73 | - |  |  | SI | Respiración |
| Q73ObsDR | - |  |  | SI | Respiración DR |
| Q74 | - |  |  | SI | Tórax |
| Q74ObsDR | - |  |  | SI | Tórax DR |
| Q75 | - |  |  | SI | Cardíaco |
| Q75ObsDR | - |  |  | SI | Cardíaco DR |
| Q76 | - |  |  | SI | Ritmo Cardíaco |
| Q76ObsDR | - |  |  | SI | Ritmo Cardíaco DR |
| Q77 | - |  |  | SI | Mamas |
| Q77ObsDR | - |  |  | SI | Mamas DR |
| Q78 | - |  |  | SI | Pezones |
| Q78ObsDR | - |  |  | SI | Pezones DR |
| Q79 | - |  |  | SI | Útero |
| Q79ObsDR | - |  |  | SI | Útero DR |
| Q80 | - |  |  | SI | Abdomen |
| Q80ObsDR | - |  |  | SI | Abdomen DR |
| Q81 | - |  |  | SI | Extremidades Superiores |
| Q81ObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q82 | - |  |  | SI | Extremidades Inferiores |
| Q82ObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q83 | - |  |  | SI | Edema |
| Q83ObsDR | - |  |  | SI | Edema DR |
| Q84 | - |  |  | SI | Genito-Urinario |
| Q84ObsDR | - |  |  | SI | Genito-Urinario DR |
| Q85 | - |  |  | SI | Ano |
| Q85ObsDR | - |  |  | SI | Ano DR |
| Q86 | - |  |  | SI | Diuresis |
| Q86ObsDR | - |  |  | SI | Diuresis DR |
| Q87 | - |  |  | SI | Deposiciones |
| Q87ObsDR | - |  |  | SI | Deposiciones DR |
| Q88 | - |  |  | SI | Comentario 12 |
| Q89 | - |  |  | SI | comentario 13 |
| Q90 | - |  |  | SI | comentario 14 |
| Q91 | - |  |  | SI | comentario 15 |
| Q92 | - |  |  | SI | comentario 16 |
| Q93 | - |  |  | SI | comentario 17 |
| Q94 | - |  |  | SI | comentario 18 |
| Q95 | - |  |  | SI | comentario 19 |
| Q96 | - |  |  | SI | comentario 20 |
| Q97 | - |  |  | SI | comentario 21 |
| Q98 | - |  |  | SI | comentario 22 |
| Q99 | - |  |  | SI | comentario 23 |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*