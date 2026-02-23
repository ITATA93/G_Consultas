# SQLUser.LBDR_BP

**Schema:** SQLUser
**Columnas:** 539
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRBP_RowID | bigint | PK |  | NO | - |
| ChildQ84DR | - |  |  | SI | Child Reference: Funciones Cognitivas |
| LBDRBP_BloodProduct | varchar |  |  | SI | Blood Product
The Blood Product Description |
| LBDRBP_BloodProductGroup | varchar |  |  | SI | Blood Product group
The Blood Product Group Descr... |
| LBDRBP_BloodProductGroupLabel | varchar |  |  | SI | Blood Product Group Label
The Text for 'Blood Pro... |
| LBDRBP_BloodProductLabel | varchar |  |  | SI | Blood Product Label
The Text for 'Blood Product' |
| LBDRBP_DeReservation | varchar |  |  | SI | De-Reservation Date and Time, default format
The ... |
| LBDRBP_DeReservationLabel | varchar |  |  | SI | De-Reservation Label
The Text for 'De-Reservation... |
| LBDRBP_HeaderText | varchar |  |  | SI | Table Header Text
The text to appear above the ta... |
| LBDRBP_NumberOfUnits | integer |  |  | SI | Number of Units Requested |
| LBDRBP_NumberOfUnitsLabel | varchar |  |  | SI | Number of Units Requested Label
The Text for 'Num... |
| LBDRBP_RequiredBy | varchar |  |  | SI | Required By
Date and Time, default format |
| LBDRBP_RequiredByLabel | varchar |  |  | SI | Required By Label
The Text for 'Required by' |
| LBDRBP_ReservationPeriod | varchar |  |  | SI | Reservation Period
The time allowed for the produ... |
| LBDRBP_ReservationPeriodLabel | varchar |  |  | SI | Reservation Period Label
The Text for 'Reservatio... |
| LBDRBP_UnitsLabel | varchar |  |  | SI | Units Header
The header text for the units table,... |
| Q01 | - |  |  | SI | Tipo de Ingreso |
| Q02 | - |  |  | SI | Tipo de Ingreso - Otro |
| Q03 | - |  |  | SI | Fecha de Ingreso a la Unidad |
| Q04 | - |  |  | SI | Fecha de Realización del Ingreso |
| Q05 | - |  |  | SI | Hora de Realización del Ingreso |
| Q06 | - |  |  | SI | Derivado Desde |
| Q07 | - |  |  | SI | Establecimiento |
| Q08 | - |  |  | SI | Motivo de Ingreso |
| Q09 | - |  |  | SI | Acompañado Por |
| Q10 | - |  |  | SI | Comentarios del acompañante |
| Q100 | - |  |  | SI | Sin limitaciones |
| Q100ObsDR | - |  |  | SI | Sin limitaciones DR |
| Q101 | - |  |  | SI | Realiza ejercicio físico |
| Q101ObsDR | - |  |  | SI | Realiza ejercicio físico DR |
| Q102 | - |  |  | SI | Sedentario |
| Q102ObsDR | - |  |  | SI | Sedentario DR |
| Q103 | - |  |  | SI | Realiza actividades de ocio |
| Q103ObsDR | - |  |  | SI | Realiza actividades de ocio DR |
| Q104 | - |  |  | SI | Duerme con problemas |
| Q104ObsDR | - |  |  | SI | Duerme con problemas DR |
| Q105 | - |  |  | SI | Sueño interrumpido |
| Q105ObsDR | - |  |  | SI | Sueño interrumpido DR |
| Q106 | - |  |  | SI | Despertar temprano |
| Q106ObsDR | - |  |  | SI | Despertar temprano DR |
| Q107 | - |  |  | SI | Somnolencia |
| Q107ObsDR | - |  |  | SI | Somnolencia DR |
| Q108 | - |  |  | SI | Pesadillas |
| Q108ObsDR | - |  |  | SI | Pesadillas DR |
| Q109 | - |  |  | SI | Problemas para conciliar el sueño |
| Q109ObsDR | - |  |  | SI | Problemas para conciliar el sueño DR |
| Q11 | - |  |  | SI | Tipo de Ingreso |
| Q110 | - |  |  | SI | Siestas |
| Q110ObsDR | - |  |  | SI | Siestas DR |
| Q111 | - |  |  | SI | Insomnio |
| Q111ObsDR | - |  |  | SI | Insomnio DR |
| Q112 | - |  |  | SI | Utiliza ayuda/fármaco para dormir |
| Q112ObsDR | - |  |  | SI | Utiliza ayuda/fármaco para dormir DR |
| Q113 | - |  |  | SI | Se levanta cansado |
| Q113ObsDR | - |  |  | SI | Se levanta cansado DR |
| Q114 | - |  |  | SI | Se levanta malhumorado |
| Q114ObsDR | - |  |  | SI | Se levanta malhumorado DR |
| Q115 | - |  |  | SI | Nivel de conciencia y actitud respecto al entorno |
| Q115ObsDR | - |  |  | SI | Nivel de conciencia y actitud respecto al entorno ... |
| Q116 | - |  |  | SI | Orientación - Reconoce |
| Q116ObsDR | - |  |  | SI | Orientación - Reconoce DR |
| Q117 | - |  |  | SI | Alteraciones Perceptivas |
| Q117ObsDR | - |  |  | SI | Alteraciones Perceptivas DR |
| Q118 | - |  |  | SI | Desesperanza |
| Q118ObsDR | - |  |  | SI | Desesperanza DR |
| Q119 | - |  |  | SI | Sentimientos de culpa |
| Q119ObsDR | - |  |  | SI | Sentimientos de culpa DR |
| Q12 | - |  |  | SI | Comentarios del Tipo de Ingreso |
| Q120 | - |  |  | SI | Sentimientos de soledad |
| Q120ObsDR | - |  |  | SI | Sentimientos de soledad DR |
| Q121 | - |  |  | SI | Agresivo/a |
| Q121ObsDR | - |  |  | SI | Agresivo/a DR |
| Q122 | - |  |  | SI | Angustia |
| Q122ObsDR | - |  |  | SI | Angustia DR |
| Q123 | - |  |  | SI | Ansiedad |
| Q123ObsDR | - |  |  | SI | Ansiedad DR |
| Q124 | - |  |  | SI | Depresión |
| Q124ObsDR | - |  |  | SI | Depresión DR |
| Q125 | - |  |  | SI | Presenta Cambios Frecuentes en Estados de Ánimo |
| Q125ObsDR | - |  |  | SI | Presenta Cambios Frecuentes en Estados de Ánimo DR |
| Q126 | - |  |  | SI | Conducta suicida |
| Q126ObsDR | - |  |  | SI | Conducta suicida DR |
| Q127 | - |  |  | SI | ¿Se siente solo? |
| Q127ObsDR | - |  |  | SI | ¿Se siente solo? DR |
| Q128 | - |  |  | SI | Pertenece a un grupo/asociaciones |
| Q128ObsDR | - |  |  | SI | Pertenece a un grupo/asociaciones DR |
| Q129 | - |  |  | SI | Conflictos familiares |
| Q129ObsDR | - |  |  | SI | Conflictos familiares DR |
| Q13 | - |  |  | SI | Medio de Llegada |
| Q130 | - |  |  | SI | Negación a una pérdida |
| Q130ObsDR | - |  |  | SI | Negación a una pérdida DR |
| Q131 | - |  |  | SI | Duelo anticipado |
| Q131ObsDR | - |  |  | SI | Duelo anticipado DR |
| Q132 | - |  |  | SI | Vive Solo |
| Q132ObsDR | - |  |  | SI | Vive Solo DR |
| Q133 | - |  |  | SI | Vive en familia |
| Q133ObsDR | - |  |  | SI | Vive en familia DR |
| Q134 | - |  |  | SI | Vive en casa de reposo |
| Q134ObsDR | - |  |  | SI | Vive en casa de reposo DR |
| Q135 | - |  |  | SI | Aceptación familiar |
| Q135ObsDR | - |  |  | SI | Aceptación familiar DR |
| Q136 | - |  |  | SI | Actividad sexual satisfactoria |
| Q136ObsDR | - |  |  | SI | Actividad sexual satisfactoria DR |
| Q137 | - |  |  | SI | Problemas de identidad sexual |
| Q137ObsDR | - |  |  | SI | Problemas de identidad sexual DR |
| Q138 | - |  |  | SI | Menstruación |
| Q138ObsDR | - |  |  | SI | Menstruación DR |
| Q139 | - |  |  | SI | Amenorrea |
| Q139ObsDR | - |  |  | SI | Amenorrea DR |
| Q14 | - |  |  | SI | Comentarios de la Forma de Ingreso |
| Q140 | - |  |  | SI | Menopausia |
| Q140ObsDR | - |  |  | SI | Menopausia DR |
| Q141 | - |  |  | SI | Medidas anticonceptivas |
| Q141ObsDR | - |  |  | SI | Medidas anticonceptivas DR |
| Q142 | - |  |  | SI | Prevención ETS |
| Q142ObsDR | - |  |  | SI | Prevención ETS DR |
| Q143 | - |  |  | SI | Control Ginecológico |
| Q143ObsDR | - |  |  | SI | Control Ginecológico DR |
| Q144 | - |  |  | SI | Tiene problemas para adaptarse a los cambios/crisi... |
| Q144ObsDR | - |  |  | SI | Tiene problemas para adaptarse a los cambios/crisi... |
| Q145 | - |  |  | SI | Historia de violencia física |
| Q145ObsDR | - |  |  | SI | Historia de violencia física DR |
| Q146 | - |  |  | SI | Historia de violencia psicológica |
| Q146ObsDR | - |  |  | SI | Historia de violencia psicológica DR |
| Q147 | - |  |  | SI | Historia de violencia sexual |
| Q147ObsDR | - |  |  | SI | Historia de violencia sexual DR |
| Q148 | - |  |  | SI | Está satisfecho con su vida |
| Q148ObsDR | - |  |  | SI | Está satisfecho con su vida DR |
| Q149 | - |  |  | SI | Estresado(a) |
| Q149ObsDR | - |  |  | SI | Estresado(a) DR |
| Q15 | - |  |  | SI | Nombre Contacto Emergencia |
| Q150 | - |  |  | SI | Agentes estresantes |
| Q150ObsDR | - |  |  | SI | Agentes estresantes DR |
| Q151 | - |  |  | SI | Utiliza fármacos para relajarse |
| Q151ObsDR | - |  |  | SI | Utiliza fármacos para relajarse DR |
| Q152 | - |  |  | SI | Realiza actividades de relajación |
| Q152ObsDR | - |  |  | SI | Realiza actividades de relajación DR |
| Q153 | - |  |  | SI | Tiene planes para el futuro |
| Q153ObsDR | - |  |  | SI | Tiene planes para el futuro DR |
| Q154 | - |  |  | SI | Otro |
| Q154ObsDR | - |  |  | SI | Otro DR |
| Q155 | - |  |  | SI | Nombre de la Enfermera/Matrona |
| Q156 | - |  |  | SI | Manejo de la cama |
| Q157 | - |  |  | SI | Localización del baño |
| Q158 | - |  |  | SI | Horarios de comida |
| Q159 | - |  |  | SI | Horarios de visitas |
| Q16 | - |  |  | SI | Parentesco |
| Q160 | - |  |  | SI | Nombre de quién recibe la información |
| Q161 | - |  |  | SI | Comentarios de la Enfermera/Matrona |
| Q162 | - |  |  | SI | Comentarios del manejo de la cama |
| Q163 | - |  |  | SI | Comentarios de la localización del baño |
| Q164 | - |  |  | SI | Comentarios de los horarios de comida |
| Q165 | - |  |  | SI | Comentarios del horario de visitas |
| Q166 | - |  |  | SI | Comentario de brazalete de alergias |
| Q167 | - |  |  | SI | Comentario de Aspecto General |
| Q168 | - |  |  | SI | Comentario de Higiene Corporal |
| Q169 | - |  |  | SI | Comentario de Higiene Bucal |
| Q17 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q170 | - |  |  | SI | Comentario de Conciencia o Conocimiento de su Enfe... |
| Q171 | - |  |  | SI | Comentario de Toma de Medicación |
| Q172 | - |  |  | SI | Comentario de Acude a Control Médico |
| Q173 | - |  |  | SI | Comentario de Apetito |
| Q174 | - |  |  | SI | Comentario de Ingesta Alimentaria Diaria |
| Q175 | - |  |  | SI | Comentario de Ingesta de Líquido Diaria |
| Q176 | - |  |  | SI | Comentario de Alteraciones Alimentarias |
| Q177 | - |  |  | SI | Comentario de Eliminación Intestinal |
| Q178 | - |  |  | SI | Comentario de Eliminación Vesical |
| Q179 | - |  |  | SI | Comentario de Posee Alteraciones de la Movilidad |
| Q18 | - |  |  | SI | Información Entregada Por |
| Q180 | - |  |  | SI | Comentario de Utiliza Sistema de Ayuda para Movili... |
| Q181 | - |  |  | SI | Comentario de Sin Limitaciones |
| Q182 | - |  |  | SI | Comentario de Realiza Ejercicio Físico |
| Q183 | - |  |  | SI | Comentario de Sedentario |
| Q184 | - |  |  | SI | Comentario de Realiza Actividades de Ocio |
| Q185 | - |  |  | SI | Comentario de Duerme con Problemas |
| Q186 | - |  |  | SI | Comentario de Sueño Interrumpido |
| Q187 | - |  |  | SI | Comentario de Despertar Temprano |
| Q188 | - |  |  | SI | Comentario de Somnolencia |
| Q189 | - |  |  | SI | Comentario de Pesadillas |
| Q19 | - |  |  | SI | Comentarios de la información entregada |
| Q190 | - |  |  | SI | Comentario de Problemas para Conciliar el Sueño |
| Q191 | - |  |  | SI | Comentario de Siestas |
| Q192 | - |  |  | SI | Comentario de Insomnio |
| Q193 | - |  |  | SI | Comentario de Utiliza Ayuda/Fármaco para Dormir |
| Q194 | - |  |  | SI | Comentario de Se Levanta Cansado |
| Q195 | - |  |  | SI | Comentario de Se Levanta Malhumorado |
| Q196 | - |  |  | SI | Comentario de Nivel de Conciencia y Actitud Respec... |
| Q197 | - |  |  | SI | Comentario de Orientación - Reconoce |
| Q198 | - |  |  | SI | Comentario de Alteraciones Perceptivas |
| Q199 | - |  |  | SI | Comentario de Desesperanza |
| Q20 | - |  |  | SI | Origen del Paciente |
| Q200 | - |  |  | SI | Comentario de Sentimientos de Culpa |
| Q201 | - |  |  | SI | Comentario de Sentimientos de Soledad |
| Q202 | - |  |  | SI | Comentario de Agresivo/a |
| Q203 | - |  |  | SI | Comentario de Angustia |
| Q204 | - |  |  | SI | Comentario de Ansiedad |
| Q205 | - |  |  | SI | Comentario de Depresión |
| Q206 | - |  |  | SI | Comentario de Presenta Cambios Frecuentes en Estad... |
| Q207 | - |  |  | SI | Comentario de Conducta Suicida |
| Q208 | - |  |  | SI | Comentario de ¿Se Siente Solo? |
| Q209 | - |  |  | SI | Comentario de Pertenece a un Grupo/Asociaciones |
| Q21 | - |  |  | SI | Comentarios del Origen del Paciente |
| Q210 | - |  |  | SI | Comentario de Conflictos Familiares |
| Q211 | - |  |  | SI | Comentario de Negación a una Pérdida |
| Q212 | - |  |  | SI | Comentario de Duelo Anticipado |
| Q213 | - |  |  | SI | Comentario de Vive Solo |
| Q214 | - |  |  | SI | Comentario de Vive en Familia |
| Q215 | - |  |  | SI | Comentario de Vive en Casa de Reposo |
| Q216 | - |  |  | SI | Comentario de Aceptación Familiar |
| Q217 | - |  |  | SI | Comentario de Actividad Sexual Satisfactoria |
| Q218 | - |  |  | SI | Comentario de Problemas de Identidad Sexual |
| Q219 | - |  |  | SI | Comentario de Menstruación |
| Q22 | - |  |  | SI | Primera Atención Salud Mental |
| Q220 | - |  |  | SI | Comentario de Amenorrea |
| Q221 | - |  |  | SI | Comentario de Menopausia |
| Q222 | - |  |  | SI | Comentario de Medidas Anticonceptivas |
| Q223 | - |  |  | SI | Comentario de Prevención ETS |
| Q224 | - |  |  | SI | Comentario de Control Ginecológico |
| Q225 | - |  |  | SI | Comentario de Tiene Problemas para Adaptarse a los... |
| Q226 | - |  |  | SI | Comentario de Historia de Violencia Física |
| Q227 | - |  |  | SI | Comentario de Historia de Violencia Psicológica |
| Q228 | - |  |  | SI | Comentario de Historia de Violencia Sexual |
| Q229 | - |  |  | SI | Comentario de Está Satisfecho con su Vida |
| Q23 | - |  |  | SI | Comentario de la Primera Atención de Salud Mental |
| Q230 | - |  |  | SI | Comentario de Estresado(a) |
| Q231 | - |  |  | SI | Comentario de Agentes Estresantes |
| Q232 | - |  |  | SI | Comentario de Utiliza Fármacos para Relajarse |
| Q233 | - |  |  | SI | Comentario de Realiza Actividades de Relajación |
| Q234 | - |  |  | SI | Comentario de Tiene Planes para el Futuro |
| Q235 | - |  |  | SI | Comentario de Otro |
| Q235a | - |  |  | SI | Entrevista Familia/Tutor |
| Q235b | - |  |  | SI | Diagnóstico de Enfermería |
| Q235c | - |  |  | SI | Plan de Cuidados de Enfermería |
| Q236 | - |  |  | SI | Profesional de Salud |
| Q237 | - |  |  | SI | Presión Arterial Media |
| Q238 | - |  |  | SI | Oxigenoterapia |
| Q238ObsDR | - |  |  | SI | Oxigenoterapia DR |
| Q239 | - |  |  | SI | Flujo de Oxígeno |
| Q239ObsDR | - |  |  | SI | Flujo de Oxígeno DR |
| Q24 | - |  |  | SI | Paciente Crónico Salud Mental |
| Q240 | - |  |  | SI | Peso Ideal Hombre |
| Q241 | - |  |  | SI | Peso Ideal Mujer |
| Q242 | - |  |  | SI | IMC |
| Q243 | - |  |  | SI | Superficie Corporal |
| Q244 | - |  |  | SI | Circunferencia Craneana |
| Q244ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q245 | - |  |  | SI | Circunferencia Torácica |
| Q245ObsDR | - |  |  | SI | Circunferencia Torácica DR |
| Q246 | - |  |  | SI | Circunferencia Abdominal |
| Q246ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q247 | - |  |  | SI | Escala del Dolor (EVA) |
| Q247ObsDR | - |  |  | SI | Escala del Dolor (EVA) DR |
| Q248 | - |  |  | SI | Razones para no Evaluar Dolor |
| Q249 | - |  |  | SI | Especifique |
| Q25 | - |  |  | SI | Comentario de Paciente Crónico |
| Q252 | - |  |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q26 | - |  |  | SI | Ingresos Previos |
| Q27 | - |  |  | SI | Comentario de Ingresos Previos |
| Q28 | - |  |  | SI | Comienzo y evolución de la enfermedad |
| Q28a | - |  |  | SI | Adherenia/Control Tratamiento (Check) |
| Q29 | - |  |  | SI | Comentarios Adherencia/Control Tratamiento |
| Q30 | - |  |  | SI | Situación laboral/Ocupación |
| Q31 | - |  |  | SI | Núcleo de Convivencia |
| Q32 | - |  |  | SI | Enfermedades Psiquiátricas Familiares |
| Q33 | - |  |  | SI | Comentario de Enfermedades Psiquiátricas Familiare... |
| Q333 | - |  |  | SI | Comentarios Patrón Percepción-Control de la Salud |
| Q333ObsDR | - |  |  | SI | Comentarios Patrón Percepción-Control de la Salud ... |
| Q334 | - |  |  | SI | Comentarios Patrón Nutricional/Metabólico |
| Q334ObsDR | - |  |  | SI | Comentarios Patrón Nutricional/Metabólico DR |
| Q335 | - |  |  | SI | Comentarios Patrón Eliminación |
| Q335ObsDR | - |  |  | SI | Comentarios Patrón Eliminación DR |
| Q336 | - |  |  | SI | Comentarios Patrón Actividad-Ejercicio |
| Q336ObsDR | - |  |  | SI | Comentarios Patrón Actividad-Ejercicio DR |
| Q337 | - |  |  | SI | Comentarios Patrón Sueño-Descanso |
| Q337ObsDR | - |  |  | SI | Comentarios Patrón Sueño-Descanso DR |
| Q338 | - |  |  | SI | Comentarios Patrón Cognitivo Perceptual |
| Q338ObsDR | - |  |  | SI | Comentarios Patrón Cognitivo Perceptual DR |
| Q339 | - |  |  | SI | Comentarios Patrón Autopercepción-Autoconcepto |
| Q339ObsDR | - |  |  | SI | Comentarios Patrón Autopercepción-Autoconcepto DR |
| Q34 | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q340 | - |  |  | SI | Comentarios Patrón de Rol-Relaciones |
| Q340ObsDR | - |  |  | SI | Comentarios Patrón de Rol-Relaciones DR |
| Q341 | - |  |  | SI | Comentarios Patrón de Sexualidad-Reproducción |
| Q341ObsDR | - |  |  | SI | Comentarios Patrón de Sexualidad-Reproducción DR |
| Q342 | - |  |  | SI | Comentarios Patrón de Adaptación-Tolerancia al Est... |
| Q342ObsDR | - |  |  | SI | Comentarios Patrón de Adaptación-Tolerancia al Est... |
| Q343 | - |  |  | SI | Comentarios Patrón de Valores y Creencias |
| Q343ObsDR | - |  |  | SI | Comentarios Patrón de Valores y Creencias DR |
| Q344 | - |  |  | SI | Datos Administrativos |
| Q345 | - |  |  | SI | Antecedentes Generales |
| Q346 | - |  |  | SI | Aspectos Socio-Culturales |
| Q347 | - |  |  | SI | Examenes Físico General |
| Q348 | - |  |  | SI | Examen Físico Segmentario |
| Q349 | - |  |  | SI | Examen Mental |
| Q35 | - |  |  | SI | Comentario del Brazalete de Identificación |
| Q350 | - |  |  | SI | Valoración de Enfermería por Patrones Funcionales ... |
| Q351 | - |  |  | SI | Patrón Percepción - Control De la Salud |
| Q352 | - |  |  | SI | Patrón Nutricional Metabólico |
| Q353 | - |  |  | SI | Patrón Eliminación |
| Q354 | - |  |  | SI | Patrón Actividad-Ejercicio |
| Q355 | - |  |  | SI | Patrón Sueño-Descanso |
| Q356 | - |  |  | SI | Patrón Cognitivo Perceptual |
| Q357 | - |  |  | SI | Patrón Autopercepción-Autoconcepto |
| Q358 | - |  |  | SI | Patrón Rol-Relaciones |
| Q359 | - |  |  | SI | Patrón de Sexualidad-Reproducción |
| Q36 | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q360 | - |  |  | SI | Patrón de Adaptación-Tolerancia al Estrés |
| Q361 | - |  |  | SI | Patrón de Valores y Creencias |
| Q362 | - |  |  | SI | Evaluación Familiar |
| Q363 | - |  |  | SI | Instrucciones Generales al paciente y su Familia |
| Q364 | - |  |  | SI | Signos Vitales |
| Q365 | - |  |  | SI | Parámetros Antropométricos |
| Q366 | - |  |  | SI | VI. Examen Mental |
| Q367 | - |  |  | SI | VII . Valoración de Enfermería por Patrones Funcio... |
| Q37 | - |  |  | SI | Comentario de Brazalete con Datos Completos y Legi... |
| Q38 | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q39 | - |  |  | SI | Dispositivos Artificiales |
| Q40 | - |  |  | SI | Comentario de Dispositivos Artificiales |
| Q41 | - |  |  | SI | Otro dispositivo |
| Q42 | - |  |  | SI | Dispositivos Clínicos |
| Q43 | - |  |  | SI | Comentario de Dispositivos Clínicos |
| Q44 | - |  |  | SI | Otro Dispositivo |
| Q45 | - |  |  | SI | Exámenes que Trae el Paciente |
| Q46 | - |  |  | SI | Comentario de los Exámenes |
| Q47 | - |  |  | SI | Otro Examen |
| Q48 | - |  |  | SI | Anamnesis Próxima |
| Q49 | - |  |  | SI | Religión |
| Q50 | - |  |  | SI | Consumo de Alcohol |
| Q51 | - |  |  | SI | Tiempo de Consumo de Alcohol |
| Q52 | - |  |  | SI | Tabaquismo |
| Q53 | - |  |  | SI | Cigarrillos por día |
| Q54 | - |  |  | SI | Años de Consumo |
| Q55 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q56 | - |  |  | SI | Consumo de Drogas |
| Q57 | - |  |  | SI | Otra Droga |
| Q58 | - |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q59 | - |  |  | SI | Nivel de Dependencia |
| Q60 | - |  |  | SI | Nivel Educacional |
| Q61 | - |  |  | SI | Forma de Comunicación |
| Q62 | - |  |  | SI | Otra forma de comunicación |
| Q63 | - |  |  | SI | Necesita Intérprete |
| Q64 | - |  |  | SI | Comentarios de necesidad de intérprete |
| Q65 | - |  |  | SI | Estado General |
| Q66 | - |  |  | SI | Frecuencia cardíaca |
| Q66ObsDR | - |  |  | SI | Frecuencia cardíaca DR |
| Q67 | - |  |  | SI | P.A. Sistólica |
| Q67ObsDR | - |  |  | SI | P.A. Sistólica DR |
| Q68 | - |  |  | SI | P.A. Diastólica |
| Q68ObsDR | - |  |  | SI | P.A. Diastólica DR |
| Q69 | - |  |  | SI | Frecuencia Respiratoria |
| Q69ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q70 | - |  |  | SI | FiO2 |
| Q70ObsDR | - |  |  | SI | FiO2 DR |
| Q71 | - |  |  | SI | Sat. O2 |
| Q71ObsDR | - |  |  | SI | Sat. O2 DR |
| Q72 | - |  |  | SI | Tempreatura Axilar |
| Q72ObsDR | - |  |  | SI | Tempreatura Axilar DR |
| Q73 | - |  |  | SI | Peso |
| Q73ObsDR | - |  |  | SI | Peso DR |
| Q74 | - |  |  | SI | Talla |
| Q74ObsDR | - |  |  | SI | Talla DR |
| Q75 | - |  |  | SI | Valoración del Dolor |
| Q76 | - |  |  | SI | Hemoglucotest |
| Q76ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q77 | - |  |  | SI | Comentarios Examen Físico General |
| Q77a | - |  |  | SI | Examen Segmentario |
| Q77ab | - |  |  | SI | Extremidades Inferiores |
| Q77abObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q77ac | - |  |  | SI | Edema |
| Q77acObsDR | - |  |  | SI | Edema DR |
| Q77ad | - |  |  | SI | Genito-Urinario |
| Q77adObsDR | - |  |  | SI | Genito-Urinario DR |
| Q77ae | - |  |  | SI | Ano |
| Q77aeObsDR | - |  |  | SI | Ano DR |
| Q77af | - |  |  | SI | Diuresis |
| Q77afObsDR | - |  |  | SI | Diuresis DR |
| Q77ag | - |  |  | SI | Deposición |
| Q77agObsDR | - |  |  | SI | Deposición DR |
| Q77b | - |  |  | SI | Tipo de Examen Físico |
| Q77bObsDR | - |  |  | SI | Tipo de Examen Físico DR |
| Q77c | - |  |  | SI | Estado Psíquico |
| Q77cObsDR | - |  |  | SI | Estado Psíquico DR |
| Q77d | - |  |  | SI | Conciencia |
| Q77dObsDR | - |  |  | SI | Conciencia DR |
| Q77e | - |  |  | SI | Piel |
| Q77eObsDR | - |  |  | SI | Piel DR |
| Q77f | - |  |  | SI | Mucosas |
| Q77fObsDR | - |  |  | SI | Mucosas DR |
| Q77g | - |  |  | SI | LPP |
| Q77gObsDR | - |  |  | SI | LPP DR |
| Q77h | - |  |  | SI | Grado LPP |
| Q77hObsDR | - |  |  | SI | Grado LPP DR |
| Q77i | - |  |  | SI | Ubicación LPP |
| Q77iObsDR | - |  |  | SI | Ubicación LPP DR |
| Q77j | - |  |  | SI | Lateralidad LPP |
| Q77jObsDR | - |  |  | SI | Lateralidad LPP DR |
| Q77k | - |  |  | SI | Cabeza - Cara |
| Q77kObsDR | - |  |  | SI | Cabeza - Cara DR |
| Q77l | - |  |  | SI | Pupilas |
| Q77lObsDR | - |  |  | SI | Pupilas DR |
| Q77m | - |  |  | SI | Conjuntivas |
| Q77mObsDR | - |  |  | SI | Conjuntivas DR |
| Q77n | - |  |  | SI | Dentadura |
| Q77nObsDR | - |  |  | SI | Dentadura DR |
| Q77o | - |  |  | SI | Lenguaje |
| Q77oObsDR | - |  |  | SI | Lenguaje DR |
| Q77p | - |  |  | SI | Cuello |
| Q77pObsDR | - |  |  | SI | Cuello DR |
| Q77q | - |  |  | SI | Vía Aérea |
| Q77qObsDR | - |  |  | SI | Vía Aérea DR |
| Q77r | - |  |  | SI | Respiración |
| Q77rObsDR | - |  |  | SI | Respiración DR |
| Q77s | - |  |  | SI | Tórax |
| Q77sObsDR | - |  |  | SI | Tórax DR |
| Q77t | - |  |  | SI | Cardíaco |
| Q77tObsDR | - |  |  | SI | Cardíaco DR |
| Q77u | - |  |  | SI | Ritmo Cardíaco |
| Q77uObsDR | - |  |  | SI | Ritmo Cardíaco DR |
| Q77v | - |  |  | SI | Descripció Mamas |
| Q77vObsDR | - |  |  | SI | Descripció Mamas DR |
| Q77w | - |  |  | SI | Descripción Pezones |
| Q77wObsDR | - |  |  | SI | Descripción Pezones DR |
| Q77x | - |  |  | SI | Útero |
| Q77xObsDR | - |  |  | SI | Útero DR |
| Q77y | - |  |  | SI | Abdomen |
| Q77yObsDR | - |  |  | SI | Abdomen DR |
| Q77z | - |  |  | SI | Extremidades Superiores |
| Q77zObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q79a | - |  |  | SI | Conducta Motora |
| Q79b | - |  |  | SI | Evaluación del Riesgo de Auto o Heterolesión |
| Q79c | - |  |  | SI | Agitación Psicomotora |
| Q79d | - |  |  | SI | ¿Cuales? (Agitacion) |
| Q79e | - |  |  | SI | Abandono Intempestivo |
| Q79f | - |  |  | SI | ¿Cuales? (abandono) |
| Q79g | - |  |  | SI | Autolesivo |
| Q79h | - |  |  | SI | ¿Cuales? (autolesivo) |
| Q79i | - |  |  | SI | Heteroagesivo |
| Q79j | - |  |  | SI | ¿Cuales? (heteroagresivo) |
| Q79k | - |  |  | SI | Caída |
| Q79l | - |  |  | SI | ¿Cuales? (caida) |
| Q79m | - |  |  | SI | Antecedentes de Caídas y/o Accidentes |
| Q79n | - |  |  | SI | ¿Cuales? (antecedentes caidas) |
| Q79o | - |  |  | SI | Comentarios (Conducta Motora) |
| Q80a | - |  |  | SI | Actitud y Conducta |
| Q80b | - |  |  | SI | Actitud y Conducta (checkbox) |
| Q80c | - |  |  | SI | Comentarios (Actitud y Conducta) |
| Q81a | - |  |  | SI | Lenguaje |
| Q81b | - |  |  | SI | Lenguaje (Checkbox) |
| Q81c | - |  |  | SI | ¿Comunicacion Fluida? |
| Q81d | - |  |  | SI | Comentarios (Lenguaje) |
| Q82a | - |  |  | SI | Ánimo |
| Q82b | - |  |  | SI | Ánimo (check) |
| Q82c | - |  |  | SI | Comentarios (Animo) |
| Q82d | - |  |  | SI | Afecto (check) |
| Q82e | - |  |  | SI | Comentarios (Afecto) |
| Q82f | - |  |  | SI | Comentarios (animo) |
| Q83a | - |  |  | SI | Estructura del Pensamiento |
| Q83b | - |  |  | SI | Estructura del Pensamiento (Checkbox) |
| Q83c | - |  |  | SI | Comentarios (Pensamiento) |
| Q83d | - |  |  | SI | 8. Contenido del Pensamiento |
| Q83e | - |  |  | SI | Alucinaciones |
| Q83f | - |  |  | SI | ¿Cuales? (alucionaciones) |
| Q83g | - |  |  | SI | Delirio |
| Q83h | - |  |  | SI | ¿Cuales? (delirio) |
| Q83i | - |  |  | SI | Megalomanía |
| Q83j | - |  |  | SI | ¿Cuales? (Megalomania) |
| Q83k | - |  |  | SI | Ideas Suicidas |
| Q83l | - |  |  | SI | ¿Cuales? (ideas suicidas) |
| Q83m | - |  |  | SI | Sin Alteraciones |
| Q83n | - |  |  | SI | Otros |
| Q83o | - |  |  | SI | Comentarios (contenido) |
| Q86 | - |  |  | SI | Aspecto General |
| Q86ObsDR | - |  |  | SI | Aspecto General DR |
| Q87 | - |  |  | SI | Higiene Corporal |
| Q87ObsDR | - |  |  | SI | Higiene Corporal DR |
| Q88 | - |  |  | SI | Higiene Bucal |
| Q88ObsDR | - |  |  | SI | Higiene Bucal DR |
| Q89 | - |  |  | SI | Conciencia o Conocimiento de su Enfermedad |
| Q89ObsDR | - |  |  | SI | Conciencia o Conocimiento de su Enfermedad DR |
| Q90 | - |  |  | SI | Toma de Medicación |
| Q90ObsDR | - |  |  | SI | Toma de Medicación DR |
| Q91 | - |  |  | SI | Acude a Control Médico |
| Q91ObsDR | - |  |  | SI | Acude a Control Médico DR |
| Q92 | - |  |  | SI | Apetito |
| Q92ObsDR | - |  |  | SI | Apetito DR |
| Q93 | - |  |  | SI | Ingesta Alimentaria Diaria |
| Q93ObsDR | - |  |  | SI | Ingesta Alimentaria Diaria DR |
| Q94 | - |  |  | SI | Ingesta de Líquido Diaria |
| Q94ObsDR | - |  |  | SI | Ingesta de Líquido Diaria DR |
| Q95 | - |  |  | SI | Alteraciones Alimentarias |
| Q95ObsDR | - |  |  | SI | Alteraciones Alimentarias DR |
| Q96 | - |  |  | SI | Eliminación Intestinal |
| Q96ObsDR | - |  |  | SI | Eliminación Intestinal DR |
| Q97 | - |  |  | SI | Eliminación Vesical |
| Q97ObsDR | - |  |  | SI | Eliminación Vesical DR |
| Q98 | - |  |  | SI | Posee alteraciones de la movilidad |
| Q98ObsDR | - |  |  | SI | Posee alteraciones de la movilidad DR |
| Q99 | - |  |  | SI | Utiliza sistema de ayuda para movilizarse |
| Q99ObsDR | - |  |  | SI | Utiliza sistema de ayuda para movilizarse DR |
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