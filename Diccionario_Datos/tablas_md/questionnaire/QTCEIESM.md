# questionnaire.QTCEIESM

> Ingreso Enfermería Salud Mental

**Schema:** questionnaire
**Columnas:** 525
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Enfermería Salud Mental

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de Ingreso |
| Q02 | varchar |  |  | SI | Tipo de Ingreso - Otro |
| Q03 | date |  |  | SI | Fecha de Ingreso a la Unidad |
| Q04 | date |  |  | SI | Fecha de Realización del Ingreso |
| Q05 | time |  |  | SI | Hora de Realización del Ingreso |
| Q06 | varchar |  |  | SI | Derivado Desde |
| Q07 | varchar |  |  | SI | Establecimiento |
| Q08 | varchar |  |  | SI | Motivo de Ingreso |
| Q09 | varchar |  |  | SI | Acompañado Por |
| Q10 | varchar |  |  | SI | Comentarios del acompañante |
| Q100 | varchar |  |  | SI | Sin limitaciones |
| Q100ObsDR | varchar |  | FK | SI | Sin limitaciones DR |
| Q101 | varchar |  |  | SI | Realiza ejercicio físico |
| Q101ObsDR | varchar |  | FK | SI | Realiza ejercicio físico DR |
| Q102 | varchar |  |  | SI | Sedentario |
| Q102ObsDR | varchar |  | FK | SI | Sedentario DR |
| Q103 | varchar |  |  | SI | Realiza actividades de ocio |
| Q103ObsDR | varchar |  | FK | SI | Realiza actividades de ocio DR |
| Q104 | varchar |  |  | SI | Duerme con problemas |
| Q104ObsDR | varchar |  | FK | SI | Duerme con problemas DR |
| Q105 | varchar |  |  | SI | Sueño interrumpido |
| Q105ObsDR | varchar |  | FK | SI | Sueño interrumpido DR |
| Q106 | varchar |  |  | SI | Despertar temprano |
| Q106ObsDR | varchar |  | FK | SI | Despertar temprano DR |
| Q107 | varchar |  |  | SI | Somnolencia |
| Q107ObsDR | varchar |  | FK | SI | Somnolencia DR |
| Q108 | varchar |  |  | SI | Pesadillas |
| Q108ObsDR | varchar |  | FK | SI | Pesadillas DR |
| Q109 | varchar |  |  | SI | Problemas para conciliar el sueño |
| Q109ObsDR | varchar |  | FK | SI | Problemas para conciliar el sueño DR |
| Q11 | varchar |  |  | SI | Tipo de Ingreso |
| Q110 | varchar |  |  | SI | Siestas |
| Q110ObsDR | varchar |  | FK | SI | Siestas DR |
| Q111 | varchar |  |  | SI | Insomnio |
| Q111ObsDR | varchar |  | FK | SI | Insomnio DR |
| Q112 | varchar |  |  | SI | Utiliza ayuda/fármaco para dormir |
| Q112ObsDR | varchar |  | FK | SI | Utiliza ayuda/fármaco para dormir DR |
| Q113 | varchar |  |  | SI | Se levanta cansado |
| Q113ObsDR | varchar |  | FK | SI | Se levanta cansado DR |
| Q114 | varchar |  |  | SI | Se levanta malhumorado |
| Q114ObsDR | varchar |  | FK | SI | Se levanta malhumorado DR |
| Q115 | varchar |  |  | SI | Nivel de conciencia y actitud respecto al entorno |
| Q115ObsDR | varchar |  | FK | SI | Nivel de conciencia y actitud respecto al entorno ... |
| Q116 | varchar |  |  | SI | Orientación - Reconoce |
| Q116ObsDR | varchar |  | FK | SI | Orientación - Reconoce DR |
| Q117 | varchar |  |  | SI | Alteraciones Perceptivas |
| Q117ObsDR | varchar |  | FK | SI | Alteraciones Perceptivas DR |
| Q118 | varchar |  |  | SI | Desesperanza |
| Q118ObsDR | varchar |  | FK | SI | Desesperanza DR |
| Q119 | varchar |  |  | SI | Sentimientos de culpa |
| Q119ObsDR | varchar |  | FK | SI | Sentimientos de culpa DR |
| Q12 | varchar |  |  | SI | Comentarios del Tipo de Ingreso |
| Q120 | varchar |  |  | SI | Sentimientos de soledad |
| Q120ObsDR | varchar |  | FK | SI | Sentimientos de soledad DR |
| Q121 | varchar |  |  | SI | Agresivo/a |
| Q121ObsDR | varchar |  | FK | SI | Agresivo/a DR |
| Q122 | varchar |  |  | SI | Angustia |
| Q122ObsDR | varchar |  | FK | SI | Angustia DR |
| Q123 | varchar |  |  | SI | Ansiedad |
| Q123ObsDR | varchar |  | FK | SI | Ansiedad DR |
| Q124 | varchar |  |  | SI | Depresión |
| Q124ObsDR | varchar |  | FK | SI | Depresión DR |
| Q125 | varchar |  |  | SI | Presenta Cambios Frecuentes en Estados de Ánimo |
| Q125ObsDR | varchar |  | FK | SI | Presenta Cambios Frecuentes en Estados de Ánimo DR |
| Q126 | varchar |  |  | SI | Conducta suicida |
| Q126ObsDR | varchar |  | FK | SI | Conducta suicida DR |
| Q127 | varchar |  |  | SI | ¿Se siente solo? |
| Q127ObsDR | varchar |  | FK | SI | ¿Se siente solo? DR |
| Q128 | varchar |  |  | SI | Pertenece a un grupo/asociaciones |
| Q128ObsDR | varchar |  | FK | SI | Pertenece a un grupo/asociaciones DR |
| Q129 | varchar |  |  | SI | Conflictos familiares |
| Q129ObsDR | varchar |  | FK | SI | Conflictos familiares DR |
| Q13 | varchar |  |  | SI | Medio de Llegada |
| Q130 | varchar |  |  | SI | Negación a una pérdida |
| Q130ObsDR | varchar |  | FK | SI | Negación a una pérdida DR |
| Q131 | varchar |  |  | SI | Duelo anticipado |
| Q131ObsDR | varchar |  | FK | SI | Duelo anticipado DR |
| Q132 | varchar |  |  | SI | Vive Solo |
| Q132ObsDR | varchar |  | FK | SI | Vive Solo DR |
| Q133 | varchar |  |  | SI | Vive en familia |
| Q133ObsDR | varchar |  | FK | SI | Vive en familia DR |
| Q134 | varchar |  |  | SI | Vive en casa de reposo |
| Q134ObsDR | varchar |  | FK | SI | Vive en casa de reposo DR |
| Q135 | varchar |  |  | SI | Aceptación familiar |
| Q135ObsDR | varchar |  | FK | SI | Aceptación familiar DR |
| Q136 | varchar |  |  | SI | Actividad sexual satisfactoria |
| Q136ObsDR | varchar |  | FK | SI | Actividad sexual satisfactoria DR |
| Q137 | varchar |  |  | SI | Problemas de identidad sexual |
| Q137ObsDR | varchar |  | FK | SI | Problemas de identidad sexual DR |
| Q138 | varchar |  |  | SI | Menstruación |
| Q138ObsDR | varchar |  | FK | SI | Menstruación DR |
| Q139 | varchar |  |  | SI | Amenorrea |
| Q139ObsDR | varchar |  | FK | SI | Amenorrea DR |
| Q14 | varchar |  |  | SI | Comentarios de la Forma de Ingreso |
| Q140 | varchar |  |  | SI | Menopausia |
| Q140ObsDR | varchar |  | FK | SI | Menopausia DR |
| Q141 | varchar |  |  | SI | Medidas anticonceptivas |
| Q141ObsDR | varchar |  | FK | SI | Medidas anticonceptivas DR |
| Q142 | varchar |  |  | SI | Prevención ETS |
| Q142ObsDR | varchar |  | FK | SI | Prevención ETS DR |
| Q143 | varchar |  |  | SI | Control Ginecológico |
| Q143ObsDR | varchar |  | FK | SI | Control Ginecológico DR |
| Q144 | varchar |  |  | SI | Tiene problemas para adaptarse a los cambios/crisi... |
| Q144ObsDR | varchar |  | FK | SI | Tiene problemas para adaptarse a los cambios/crisi... |
| Q145 | varchar |  |  | SI | Historia de violencia física |
| Q145ObsDR | varchar |  | FK | SI | Historia de violencia física DR |
| Q146 | varchar |  |  | SI | Historia de violencia psicológica |
| Q146ObsDR | varchar |  | FK | SI | Historia de violencia psicológica DR |
| Q147 | varchar |  |  | SI | Historia de violencia sexual |
| Q147ObsDR | varchar |  | FK | SI | Historia de violencia sexual DR |
| Q148 | varchar |  |  | SI | Está satisfecho con su vida |
| Q148ObsDR | varchar |  | FK | SI | Está satisfecho con su vida DR |
| Q149 | varchar |  |  | SI | Estresado(a) |
| Q149ObsDR | varchar |  | FK | SI | Estresado(a) DR |
| Q15 | varchar |  |  | SI | Nombre Contacto Emergencia |
| Q150 | varchar |  |  | SI | Agentes estresantes |
| Q150ObsDR | varchar |  | FK | SI | Agentes estresantes DR |
| Q151 | varchar |  |  | SI | Utiliza fármacos para relajarse |
| Q151ObsDR | varchar |  | FK | SI | Utiliza fármacos para relajarse DR |
| Q152 | varchar |  |  | SI | Realiza actividades de relajación |
| Q152ObsDR | varchar |  | FK | SI | Realiza actividades de relajación DR |
| Q153 | varchar |  |  | SI | Tiene planes para el futuro |
| Q153ObsDR | varchar |  | FK | SI | Tiene planes para el futuro DR |
| Q154 | varchar |  |  | SI | Otro |
| Q154ObsDR | varchar |  | FK | SI | Otro DR |
| Q155 | varchar |  |  | SI | Nombre de la Enfermera/Matrona |
| Q156 | varchar |  |  | SI | Manejo de la cama |
| Q157 | varchar |  |  | SI | Localización del baño |
| Q158 | varchar |  |  | SI | Horarios de comida |
| Q159 | varchar |  |  | SI | Horarios de visitas |
| Q16 | varchar |  |  | SI | Parentesco |
| Q160 | varchar |  |  | SI | Nombre de quién recibe la información |
| Q161 | varchar |  |  | SI | Comentarios de la Enfermera/Matrona |
| Q162 | varchar |  |  | SI | Comentarios del manejo de la cama |
| Q163 | varchar |  |  | SI | Comentarios de la localización del baño |
| Q164 | varchar |  |  | SI | Comentarios de los horarios de comida |
| Q165 | varchar |  |  | SI | Comentarios del horario de visitas |
| Q166 | varchar |  |  | SI | Comentario de brazalete de alergias |
| Q167 | varchar |  |  | SI | Comentario de Aspecto General |
| Q168 | varchar |  |  | SI | Comentario de Higiene Corporal |
| Q169 | varchar |  |  | SI | Comentario de Higiene Bucal |
| Q17 | varchar |  |  | SI | Teléfono Contacto Emergencia |
| Q170 | varchar |  |  | SI | Comentario de Conciencia o Conocimiento de su Enfe... |
| Q171 | varchar |  |  | SI | Comentario de Toma de Medicación |
| Q172 | varchar |  |  | SI | Comentario de Acude a Control Médico |
| Q173 | varchar |  |  | SI | Comentario de Apetito |
| Q174 | varchar |  |  | SI | Comentario de Ingesta Alimentaria Diaria |
| Q175 | varchar |  |  | SI | Comentario de Ingesta de Líquido Diaria |
| Q176 | varchar |  |  | SI | Comentario de Alteraciones Alimentarias |
| Q177 | varchar |  |  | SI | Comentario de Eliminación Intestinal |
| Q178 | varchar |  |  | SI | Comentario de Eliminación Vesical |
| Q179 | varchar |  |  | SI | Comentario de Posee Alteraciones de la Movilidad |
| Q18 | varchar |  |  | SI | Información Entregada Por |
| Q180 | varchar |  |  | SI | Comentario de Utiliza Sistema de Ayuda para Movili... |
| Q181 | varchar |  |  | SI | Comentario de Sin Limitaciones |
| Q182 | varchar |  |  | SI | Comentario de Realiza Ejercicio Físico |
| Q183 | varchar |  |  | SI | Comentario de Sedentario |
| Q184 | varchar |  |  | SI | Comentario de Realiza Actividades de Ocio |
| Q185 | varchar |  |  | SI | Comentario de Duerme con Problemas |
| Q186 | varchar |  |  | SI | Comentario de Sueño Interrumpido |
| Q187 | varchar |  |  | SI | Comentario de Despertar Temprano |
| Q188 | varchar |  |  | SI | Comentario de Somnolencia |
| Q189 | varchar |  |  | SI | Comentario de Pesadillas |
| Q19 | varchar |  |  | SI | Comentarios de la información entregada |
| Q190 | varchar |  |  | SI | Comentario de Problemas para Conciliar el Sueño |
| Q191 | varchar |  |  | SI | Comentario de Siestas |
| Q192 | varchar |  |  | SI | Comentario de Insomnio |
| Q193 | varchar |  |  | SI | Comentario de Utiliza Ayuda/Fármaco para Dormir |
| Q194 | varchar |  |  | SI | Comentario de Se Levanta Cansado |
| Q195 | varchar |  |  | SI | Comentario de Se Levanta Malhumorado |
| Q196 | varchar |  |  | SI | Comentario de Nivel de Conciencia y Actitud Respec... |
| Q197 | varchar |  |  | SI | Comentario de Orientación - Reconoce |
| Q198 | varchar |  |  | SI | Comentario de Alteraciones Perceptivas |
| Q199 | varchar |  |  | SI | Comentario de Desesperanza |
| Q20 | varchar |  |  | SI | Origen del Paciente |
| Q200 | varchar |  |  | SI | Comentario de Sentimientos de Culpa |
| Q201 | varchar |  |  | SI | Comentario de Sentimientos de Soledad |
| Q202 | varchar |  |  | SI | Comentario de Agresivo/a |
| Q203 | varchar |  |  | SI | Comentario de Angustia |
| Q204 | varchar |  |  | SI | Comentario de Ansiedad |
| Q205 | varchar |  |  | SI | Comentario de Depresión |
| Q206 | varchar |  |  | SI | Comentario de Presenta Cambios Frecuentes en Estad... |
| Q207 | varchar |  |  | SI | Comentario de Conducta Suicida |
| Q208 | varchar |  |  | SI | Comentario de ¿Se Siente Solo? |
| Q209 | varchar |  |  | SI | Comentario de Pertenece a un Grupo/Asociaciones |
| Q21 | varchar |  |  | SI | Comentarios del Origen del Paciente |
| Q210 | varchar |  |  | SI | Comentario de Conflictos Familiares |
| Q211 | varchar |  |  | SI | Comentario de Negación a una Pérdida |
| Q212 | varchar |  |  | SI | Comentario de Duelo Anticipado |
| Q213 | varchar |  |  | SI | Comentario de Vive Solo |
| Q214 | varchar |  |  | SI | Comentario de Vive en Familia |
| Q215 | varchar |  |  | SI | Comentario de Vive en Casa de Reposo |
| Q216 | varchar |  |  | SI | Comentario de Aceptación Familiar |
| Q217 | varchar |  |  | SI | Comentario de Actividad Sexual Satisfactoria |
| Q218 | varchar |  |  | SI | Comentario de Problemas de Identidad Sexual |
| Q219 | varchar |  |  | SI | Comentario de Menstruación |
| Q22 | varchar |  |  | SI | Primera Atención Salud Mental |
| Q220 | varchar |  |  | SI | Comentario de Amenorrea |
| Q221 | varchar |  |  | SI | Comentario de Menopausia |
| Q222 | varchar |  |  | SI | Comentario de Medidas Anticonceptivas |
| Q223 | varchar |  |  | SI | Comentario de Prevención ETS |
| Q224 | varchar |  |  | SI | Comentario de Control Ginecológico |
| Q225 | varchar |  |  | SI | Comentario de Tiene Problemas para Adaptarse a los... |
| Q226 | varchar |  |  | SI | Comentario de Historia de Violencia Física |
| Q227 | varchar |  |  | SI | Comentario de Historia de Violencia Psicológica |
| Q228 | varchar |  |  | SI | Comentario de Historia de Violencia Sexual |
| Q229 | varchar |  |  | SI | Comentario de Está Satisfecho con su Vida |
| Q23 | varchar |  |  | SI | Comentario de la Primera Atención de Salud Mental |
| Q230 | varchar |  |  | SI | Comentario de Estresado(a) |
| Q231 | varchar |  |  | SI | Comentario de Agentes Estresantes |
| Q232 | varchar |  |  | SI | Comentario de Utiliza Fármacos para Relajarse |
| Q233 | varchar |  |  | SI | Comentario de Realiza Actividades de Relajación |
| Q234 | varchar |  |  | SI | Comentario de Tiene Planes para el Futuro |
| Q235 | varchar |  |  | SI | Comentario de Otro |
| Q235a | varchar |  |  | SI | Entrevista Familia/Tutor |
| Q235b | varchar |  |  | SI | Diagnóstico de Enfermería |
| Q235c | varchar |  |  | SI | Plan de Cuidados de Enfermería |
| Q236 | varchar |  |  | SI | Profesional de Salud |
| Q237 | varchar |  |  | SI | Presión Arterial Media |
| Q238 | varchar |  |  | SI | Oxigenoterapia |
| Q238ObsDR | varchar |  | FK | SI | Oxigenoterapia DR |
| Q239 | varchar |  |  | SI | Flujo de Oxígeno |
| Q239ObsDR | varchar |  | FK | SI | Flujo de Oxígeno DR |
| Q24 | varchar |  |  | SI | Paciente Crónico Salud Mental |
| Q240 | varchar |  |  | SI | Peso Ideal Hombre |
| Q241 | varchar |  |  | SI | Peso Ideal Mujer |
| Q242 | varchar |  |  | SI | IMC |
| Q243 | varchar |  |  | SI | Superficie Corporal |
| Q244 | varchar |  |  | SI | Circunferencia Craneana |
| Q244ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q245 | varchar |  |  | SI | Circunferencia Torácica |
| Q245ObsDR | varchar |  | FK | SI | Circunferencia Torácica DR |
| Q246 | varchar |  |  | SI | Circunferencia Abdominal |
| Q246ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q247 | varchar |  |  | SI | Escala del Dolor (EVA) |
| Q247ObsDR | varchar |  | FK | SI | Escala del Dolor (EVA) DR |
| Q248 | varchar |  |  | SI | Razones para no Evaluar Dolor |
| Q249 | varchar |  |  | SI | Especifique |
| Q25 | varchar |  |  | SI | Comentario de Paciente Crónico |
| Q252 | varchar |  |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q26 | varchar |  |  | SI | Ingresos Previos |
| Q27 | varchar |  |  | SI | Comentario de Ingresos Previos |
| Q28 | varchar |  |  | SI | Comienzo y evolución de la enfermedad |
| Q28a | varchar |  |  | SI | Adherenia/Control Tratamiento (Check) |
| Q29 | varchar |  |  | SI | Comentarios Adherencia/Control Tratamiento |
| Q30 | varchar |  |  | SI | Situación laboral/Ocupación |
| Q31 | varchar |  |  | SI | Núcleo de Convivencia |
| Q32 | varchar |  |  | SI | Enfermedades Psiquiátricas Familiares |
| Q33 | varchar |  |  | SI | Comentario de Enfermedades Psiquiátricas Familiare... |
| Q333 | varchar |  |  | SI | Comentarios Patrón Percepción-Control de la Salud |
| Q333ObsDR | varchar |  | FK | SI | Comentarios Patrón Percepción-Control de la Salud ... |
| Q334 | varchar |  |  | SI | Comentarios Patrón Nutricional/Metabólico |
| Q334ObsDR | varchar |  | FK | SI | Comentarios Patrón Nutricional/Metabólico DR |
| Q335 | varchar |  |  | SI | Comentarios Patrón Eliminación |
| Q335ObsDR | varchar |  | FK | SI | Comentarios Patrón Eliminación DR |
| Q336 | varchar |  |  | SI | Comentarios Patrón Actividad-Ejercicio |
| Q336ObsDR | varchar |  | FK | SI | Comentarios Patrón Actividad-Ejercicio DR |
| Q337 | varchar |  |  | SI | Comentarios Patrón Sueño-Descanso |
| Q337ObsDR | varchar |  | FK | SI | Comentarios Patrón Sueño-Descanso DR |
| Q338 | varchar |  |  | SI | Comentarios Patrón Cognitivo Perceptual |
| Q338ObsDR | varchar |  | FK | SI | Comentarios Patrón Cognitivo Perceptual DR |
| Q339 | varchar |  |  | SI | Comentarios Patrón Autopercepción-Autoconcepto |
| Q339ObsDR | varchar |  | FK | SI | Comentarios Patrón Autopercepción-Autoconcepto DR |
| Q34 | varchar |  |  | SI | Paciente Porta Brazalete Identificación |
| Q340 | varchar |  |  | SI | Comentarios Patrón de Rol-Relaciones |
| Q340ObsDR | varchar |  | FK | SI | Comentarios Patrón de Rol-Relaciones DR |
| Q341 | varchar |  |  | SI | Comentarios Patrón de Sexualidad-Reproducción |
| Q341ObsDR | varchar |  | FK | SI | Comentarios Patrón de Sexualidad-Reproducción DR |
| Q342 | varchar |  |  | SI | Comentarios Patrón de Adaptación-Tolerancia al Est... |
| Q342ObsDR | varchar |  | FK | SI | Comentarios Patrón de Adaptación-Tolerancia al Est... |
| Q343 | varchar |  |  | SI | Comentarios Patrón de Valores y Creencias |
| Q343ObsDR | varchar |  | FK | SI | Comentarios Patrón de Valores y Creencias DR |
| Q344 | varchar |  |  | SI | Datos Administrativos |
| Q345 | varchar |  |  | SI | Antecedentes Generales |
| Q346 | varchar |  |  | SI | Aspectos Socio-Culturales |
| Q347 | varchar |  |  | SI | Examenes Físico General |
| Q348 | varchar |  |  | SI | Examen Físico Segmentario |
| Q349 | varchar |  |  | SI | Examen Mental |
| Q35 | varchar |  |  | SI | Comentario del Brazalete de Identificación |
| Q350 | varchar |  |  | SI | Valoración de Enfermería por Patrones Funcionales ... |
| Q351 | varchar |  |  | SI | Patrón Percepción - Control De la Salud |
| Q352 | varchar |  |  | SI | Patrón Nutricional Metabólico |
| Q353 | varchar |  |  | SI | Patrón Eliminación |
| Q354 | varchar |  |  | SI | Patrón Actividad-Ejercicio |
| Q355 | varchar |  |  | SI | Patrón Sueño-Descanso |
| Q356 | varchar |  |  | SI | Patrón Cognitivo Perceptual |
| Q357 | varchar |  |  | SI | Patrón Autopercepción-Autoconcepto |
| Q358 | varchar |  |  | SI | Patrón Rol-Relaciones |
| Q359 | varchar |  |  | SI | Patrón de Sexualidad-Reproducción |
| Q36 | varchar |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q360 | varchar |  |  | SI | Patrón de Adaptación-Tolerancia al Estrés |
| Q361 | varchar |  |  | SI | Patrón de Valores y Creencias |
| Q362 | varchar |  |  | SI | Evaluación Familiar |
| Q363 | varchar |  |  | SI | Instrucciones Generales al paciente y su Familia |
| Q364 | varchar |  |  | SI | Signos Vitales |
| Q365 | varchar |  |  | SI | Parámetros Antropométricos |
| Q366 | varchar |  |  | SI | VI. Examen Mental |
| Q367 | varchar |  |  | SI | VII . Valoración de Enfermería por Patrones Funcio... |
| Q368 | varchar |  |  | SI | Acompañamiento Espiritual |
| Q37 | varchar |  |  | SI | Comentario de Brazalete con Datos Completos y Legi... |
| Q38 | varchar |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q39 | varchar |  |  | SI | Dispositivos Artificiales |
| Q40 | varchar |  |  | SI | Comentario de Dispositivos Artificiales |
| Q41 | varchar |  |  | SI | Otro dispositivo |
| Q42 | varchar |  |  | SI | Dispositivos Clínicos |
| Q43 | varchar |  |  | SI | Comentario de Dispositivos Clínicos |
| Q44 | varchar |  |  | SI | Otro Dispositivo |
| Q45 | varchar |  |  | SI | Exámenes que Trae el Paciente |
| Q46 | varchar |  |  | SI | Comentario de los Exámenes |
| Q47 | varchar |  |  | SI | Otro Examen |
| Q48 | varchar |  |  | SI | Anamnesis Próxima |
| Q49 | varchar |  |  | SI | Religión |
| Q50 | varchar |  |  | SI | Consumo de Alcohol |
| Q51 | varchar |  |  | SI | Tiempo de Consumo de Alcohol |
| Q52 | varchar |  |  | SI | Tabaquismo |
| Q53 | numeric |  |  | SI | Cigarrillos por día |
| Q54 | numeric |  |  | SI | Años de Consumo |
| Q55 | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q56 | varchar |  |  | SI | Consumo de Drogas |
| Q57 | varchar |  |  | SI | Otra Droga |
| Q58 | varchar |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q59 | varchar |  |  | SI | Nivel de Dependencia |
| Q60 | varchar |  |  | SI | Nivel Educacional |
| Q61 | varchar |  |  | SI | Forma de Comunicación |
| Q62 | varchar |  |  | SI | Otra forma de comunicación |
| Q63 | varchar |  |  | SI | Necesita Intérprete |
| Q64 | varchar |  |  | SI | Comentarios de necesidad de intérprete |
| Q65 | varchar |  |  | SI | Estado General |
| Q66 | varchar |  |  | SI | Frecuencia cardíaca |
| Q66ObsDR | varchar |  | FK | SI | Frecuencia cardíaca DR |
| Q67 | varchar |  |  | SI | P.A. Sistólica |
| Q67ObsDR | varchar |  | FK | SI | P.A. Sistólica DR |
| Q68 | varchar |  |  | SI | P.A. Diastólica |
| Q68ObsDR | varchar |  | FK | SI | P.A. Diastólica DR |
| Q69 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q69ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q70 | varchar |  |  | SI | FiO2 |
| Q70ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q71 | varchar |  |  | SI | Sat. O2 |
| Q71ObsDR | varchar |  | FK | SI | Sat. O2 DR |
| Q72 | varchar |  |  | SI | Tempreatura Axilar |
| Q72ObsDR | varchar |  | FK | SI | Tempreatura Axilar DR |
| Q73 | varchar |  |  | SI | Peso |
| Q73ObsDR | varchar |  | FK | SI | Peso DR |
| Q74 | varchar |  |  | SI | Talla |
| Q74ObsDR | varchar |  | FK | SI | Talla DR |
| Q75 | varchar |  |  | SI | Valoración del Dolor |
| Q76 | varchar |  |  | SI | Hemoglucotest |
| Q76ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q77 | varchar |  |  | SI | Comentarios Examen Físico General |
| Q77a | varchar |  |  | SI | Examen Segmentario |
| Q77ab | varchar |  |  | SI | Extremidades Inferiores |
| Q77abObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q77ac | varchar |  |  | SI | Edema |
| Q77acObsDR | varchar |  | FK | SI | Edema DR |
| Q77ad | varchar |  |  | SI | Genito-Urinario |
| Q77adObsDR | varchar |  | FK | SI | Genito-Urinario DR |
| Q77ae | varchar |  |  | SI | Ano |
| Q77aeObsDR | varchar |  | FK | SI | Ano DR |
| Q77af | varchar |  |  | SI | Diuresis |
| Q77afObsDR | varchar |  | FK | SI | Diuresis DR |
| Q77ag | varchar |  |  | SI | Deposición |
| Q77agObsDR | varchar |  | FK | SI | Deposición DR |
| Q77b | varchar |  |  | SI | Tipo de Examen Físico |
| Q77bObsDR | varchar |  | FK | SI | Tipo de Examen Físico DR |
| Q77c | varchar |  |  | SI | Estado Psíquico |
| Q77cObsDR | varchar |  | FK | SI | Estado Psíquico DR |
| Q77d | varchar |  |  | SI | Conciencia |
| Q77dObsDR | varchar |  | FK | SI | Conciencia DR |
| Q77e | varchar |  |  | SI | Piel |
| Q77eObsDR | varchar |  | FK | SI | Piel DR |
| Q77f | varchar |  |  | SI | Mucosas |
| Q77fObsDR | varchar |  | FK | SI | Mucosas DR |
| Q77g | varchar |  |  | SI | LPP |
| Q77gObsDR | varchar |  | FK | SI | LPP DR |
| Q77h | varchar |  |  | SI | Grado LPP |
| Q77hObsDR | varchar |  | FK | SI | Grado LPP DR |
| Q77i | varchar |  |  | SI | Ubicación LPP |
| Q77iObsDR | varchar |  | FK | SI | Ubicación LPP DR |
| Q77j | varchar |  |  | SI | Lateralidad LPP |
| Q77jObsDR | varchar |  | FK | SI | Lateralidad LPP DR |
| Q77k | varchar |  |  | SI | Cabeza - Cara |
| Q77kObsDR | varchar |  | FK | SI | Cabeza - Cara DR |
| Q77l | varchar |  |  | SI | Pupilas |
| Q77lObsDR | varchar |  | FK | SI | Pupilas DR |
| Q77m | varchar |  |  | SI | Conjuntivas |
| Q77mObsDR | varchar |  | FK | SI | Conjuntivas DR |
| Q77n | varchar |  |  | SI | Dentadura |
| Q77nObsDR | varchar |  | FK | SI | Dentadura DR |
| Q77o | varchar |  |  | SI | Lenguaje |
| Q77oObsDR | varchar |  | FK | SI | Lenguaje DR |
| Q77p | varchar |  |  | SI | Cuello |
| Q77pObsDR | varchar |  | FK | SI | Cuello DR |
| Q77q | varchar |  |  | SI | Vía Aérea |
| Q77qObsDR | varchar |  | FK | SI | Vía Aérea DR |
| Q77r | varchar |  |  | SI | Respiración |
| Q77rObsDR | varchar |  | FK | SI | Respiración DR |
| Q77s | varchar |  |  | SI | Tórax |
| Q77sObsDR | varchar |  | FK | SI | Tórax DR |
| Q77t | varchar |  |  | SI | Cardíaco |
| Q77tObsDR | varchar |  | FK | SI | Cardíaco DR |
| Q77u | varchar |  |  | SI | Ritmo Cardíaco |
| Q77uObsDR | varchar |  | FK | SI | Ritmo Cardíaco DR |
| Q77v | varchar |  |  | SI | Descripció Mamas |
| Q77vObsDR | varchar |  | FK | SI | Descripció Mamas DR |
| Q77w | varchar |  |  | SI | Descripción Pezones |
| Q77wObsDR | varchar |  | FK | SI | Descripción Pezones DR |
| Q77x | varchar |  |  | SI | Útero |
| Q77xObsDR | varchar |  | FK | SI | Útero DR |
| Q77y | varchar |  |  | SI | Abdomen |
| Q77yObsDR | varchar |  | FK | SI | Abdomen DR |
| Q77z | varchar |  |  | SI | Extremidades Superiores |
| Q77zObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q79a | varchar |  |  | SI | Conducta Motora |
| Q79b | varchar |  |  | SI | Evaluación del Riesgo de Auto o Heterolesión |
| Q79c | varchar |  |  | SI | Agitación Psicomotora |
| Q79d | varchar |  |  | SI | ¿Cuales? (Agitacion) |
| Q79e | varchar |  |  | SI | Abandono Intempestivo |
| Q79f | varchar |  |  | SI | ¿Cuales? (abandono) |
| Q79g | varchar |  |  | SI | Autolesivo |
| Q79h | varchar |  |  | SI | ¿Cuales? (autolesivo) |
| Q79i | varchar |  |  | SI | Heteroagesivo |
| Q79j | varchar |  |  | SI | ¿Cuales? (heteroagresivo) |
| Q79k | varchar |  |  | SI | Caída |
| Q79l | varchar |  |  | SI | ¿Cuales? (caida) |
| Q79m | varchar |  |  | SI | Antecedentes de Caídas y/o Accidentes |
| Q79n | varchar |  |  | SI | ¿Cuales? (antecedentes caidas) |
| Q79o | varchar |  |  | SI | Comentarios (Conducta Motora) |
| Q80a | varchar |  |  | SI | Actitud y Conducta |
| Q80b | varchar |  |  | SI | Actitud y Conducta (checkbox) |
| Q80c | varchar |  |  | SI | Comentarios (Actitud y Conducta) |
| Q81a | varchar |  |  | SI | Lenguaje |
| Q81b | varchar |  |  | SI | Lenguaje (Checkbox) |
| Q81c | varchar |  |  | SI | ¿Comunicacion Fluida? |
| Q81d | varchar |  |  | SI | Comentarios (Lenguaje) |
| Q82a | varchar |  |  | SI | Ánimo |
| Q82b | varchar |  |  | SI | Ánimo (check) |
| Q82c | varchar |  |  | SI | Comentarios (Animo) |
| Q82d | varchar |  |  | SI | Afecto (check) |
| Q82e | varchar |  |  | SI | Comentarios (Afecto) |
| Q82f | varchar |  |  | SI | Comentarios (animo) |
| Q83a | varchar |  |  | SI | Estructura del Pensamiento |
| Q83b | varchar |  |  | SI | Estructura del Pensamiento (Checkbox) |
| Q83c | varchar |  |  | SI | Comentarios (Pensamiento) |
| Q83d | varchar |  |  | SI | 8. Contenido del Pensamiento |
| Q83e | varchar |  |  | SI | Alucinaciones |
| Q83f | varchar |  |  | SI | ¿Cuales? (alucionaciones) |
| Q83g | varchar |  |  | SI | Delirio |
| Q83h | varchar |  |  | SI | ¿Cuales? (delirio) |
| Q83i | varchar |  |  | SI | Megalomanía |
| Q83j | varchar |  |  | SI | ¿Cuales? (Megalomania) |
| Q83k | varchar |  |  | SI | Ideas Suicidas |
| Q83l | varchar |  |  | SI | ¿Cuales? (ideas suicidas) |
| Q83m | bit |  |  | SI | Sin Alteraciones |
| Q83n | bit |  |  | SI | Otros |
| Q83o | varchar |  |  | SI | Comentarios (contenido) |
| Q86 | varchar |  |  | SI | Aspecto General |
| Q86ObsDR | varchar |  | FK | SI | Aspecto General DR |
| Q87 | varchar |  |  | SI | Higiene Corporal |
| Q87ObsDR | varchar |  | FK | SI | Higiene Corporal DR |
| Q88 | varchar |  |  | SI | Higiene Bucal |
| Q88ObsDR | varchar |  | FK | SI | Higiene Bucal DR |
| Q89 | varchar |  |  | SI | Conciencia o Conocimiento de su Enfermedad |
| Q89ObsDR | varchar |  | FK | SI | Conciencia o Conocimiento de su Enfermedad DR |
| Q90 | varchar |  |  | SI | Toma de Medicación |
| Q90ObsDR | varchar |  | FK | SI | Toma de Medicación DR |
| Q91 | varchar |  |  | SI | Acude a Control Médico |
| Q91ObsDR | varchar |  | FK | SI | Acude a Control Médico DR |
| Q92 | varchar |  |  | SI | Apetito |
| Q92ObsDR | varchar |  | FK | SI | Apetito DR |
| Q93 | varchar |  |  | SI | Ingesta Alimentaria Diaria |
| Q93ObsDR | varchar |  | FK | SI | Ingesta Alimentaria Diaria DR |
| Q94 | varchar |  |  | SI | Ingesta de Líquido Diaria |
| Q94ObsDR | varchar |  | FK | SI | Ingesta de Líquido Diaria DR |
| Q95 | varchar |  |  | SI | Alteraciones Alimentarias |
| Q95ObsDR | varchar |  | FK | SI | Alteraciones Alimentarias DR |
| Q96 | varchar |  |  | SI | Eliminación Intestinal |
| Q96ObsDR | varchar |  | FK | SI | Eliminación Intestinal DR |
| Q97 | varchar |  |  | SI | Eliminación Vesical |
| Q97ObsDR | varchar |  | FK | SI | Eliminación Vesical DR |
| Q98 | varchar |  |  | SI | Posee alteraciones de la movilidad |
| Q98ObsDR | varchar |  | FK | SI | Posee alteraciones de la movilidad DR |
| Q99 | varchar |  |  | SI | Utiliza sistema de ayuda para movilizarse |
| Q99ObsDR | varchar |  | FK | SI | Utiliza sistema de ayuda para movilizarse DR |
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