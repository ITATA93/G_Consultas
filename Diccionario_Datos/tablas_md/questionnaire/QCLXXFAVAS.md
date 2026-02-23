# questionnaire.QCLXXFAVAS

> Formulario de Atencion de Victimas de Agresiones Sexuales

**Schema:** questionnaire
**Columnas:** 365
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Atencion de Victimas de Agresiones Sexuales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | A. Información General |
| Q02 | varchar |  |  | SI | Institución en la que realiza el examen |
| Q03 | varchar |  |  | SI | Ciudad del examen |
| Q04 | date |  |  | SI | Fecha del examen |
| Q05 | varchar |  |  | SI | Horas del examen |
| Q06 | varchar |  |  | SI | N° Documento de identidad |
| Q07 | varchar |  |  | SI | N° de Informe |
| Q08 | varchar |  |  | SI | Nombre del examinado |
| Q09 | varchar |  |  | SI | Apellido Paterno |
| Q10 | varchar |  |  | SI | Apellido Materno |
| Q100 | varchar |  |  | SI | Dónde se encuentran |
| Q101 | varchar |  |  | SI | Se dejan para estudio |
| Q102 | varchar |  |  | SI | Observaciones |
| Q104 | varchar |  |  | SI | 5. Examen Médico Forense |
| Q105 | varchar |  |  | SI | Peso |
| Q105ObsDR | varchar |  | FK | SI | Peso DR |
| Q106 | varchar |  |  | SI | Talla |
| Q106ObsDR | varchar |  | FK | SI | Talla DR |
| Q107 | varchar |  |  | SI | Signos vitales |
| Q108 | varchar |  |  | SI | P/A |
| Q108ObsDR | varchar |  | FK | SI | P/A DR |
| Q109 | varchar |  |  | SI | Presión Sistólica |
| Q109ObsDR | varchar |  | FK | SI | Presión Sistólica DR |
| Q11 | varchar |  |  | SI | Edad  |
| Q110 | varchar |  |  | SI | FC |
| Q110ObsDR | varchar |  | FK | SI | FC DR |
| Q111 | varchar |  |  | SI | FR |
| Q111ObsDR | varchar |  | FK | SI | FR DR |
| Q112 | varchar |  |  | SI | Temp |
| Q112ObsDR | varchar |  | FK | SI | Temp DR |
| Q113 | varchar |  |  | SI | 5.1 Aspecto General |
| Q114 | varchar |  |  | SI | 5.2 Descripción de hallazgos y recolección de evid... |
| Q115 | varchar |  |  | SI | Valoración de la zona subungueal |
| Q116 | varchar |  |  | SI | Presenta lesiones |
| Q117 | varchar |  |  | SI | En caso afirmativo describa |
| Q118 | varchar |  |  | SI | Describa el aspecto general 5.1 |
| Q119 | varchar |  |  | SI | Se recolecta evidencia física |
| Q12 | varchar |  |  | SI | Fecha de nacimiento |
| Q120 | varchar |  |  | SI | Cara, cabeza (cuero cabelludo, pelo), cuello: |
| Q121 | varchar |  |  | SI | Presenta Lesiones |
| Q122 | varchar |  |  | SI | En caso afirmativo describa |
| Q123 | varchar |  |  | SI | Se recolecta evidencia física |
| Q124 | varchar |  |  | SI | Cuál |
| Q125 | varchar |  |  | SI | Cavidad oral |
| Q126 | varchar |  |  | SI | Presenta Lesiones |
| Q127 | varchar |  |  | SI | En caso afirmativo describa |
| Q128 | varchar |  |  | SI | Se recolecta evidencia física |
| Q129 | varchar |  |  | SI | Cuál ? |
| Q13 | varchar |  |  | SI | Sexo |
| Q130 | varchar |  |  | SI | En niños y niñas describa tipo de dentinción |
| Q131 | varchar |  |  | SI | Fase inicial |
| Q132 | varchar |  |  | SI | Media |
| Q133 | varchar |  |  | SI | Completa |
| Q134 | varchar |  |  | SI | Tórax |
| Q135 | varchar |  |  | SI | Presenta Lesiones |
| Q136 | varchar |  |  | SI | En caso afirmativo describa |
| Q137 | varchar |  |  | SI | Se recolecta evidencia física |
| Q138 | varchar |  |  | SI | Cuál |
| Q139 | varchar |  |  | SI | Mamas |
| Q14 | varchar |  |  | SI | Dirección |
| Q140 | varchar |  |  | SI | Presenta Lesiones |
| Q141 | varchar |  |  | SI | En caso afirmativo describa |
| Q142 | varchar |  |  | SI | Se recolecta evidencia física |
| Q143 | varchar |  |  | SI | Cuál ? |
| Q144 | varchar |  |  | SI | En niñas y niños describa caracteres sexuales secu... |
| Q145 | varchar |  |  | SI | Abdomen |
| Q146 | varchar |  |  | SI | Presenta Lesiones |
| Q147 | varchar |  |  | SI | En caso afirmativo describa |
| Q148 | varchar |  |  | SI | Se recolecta evidencia física |
| Q149 | varchar |  |  | SI | Cuál ? |
| Q15 | numeric |  |  | SI | Teléfono contacto |
| Q150 | varchar |  |  | SI | Signos de embarazo |
| Q151 | varchar |  |  | SI | Describa |
| Q152 | varchar |  |  | SI | Espalda |
| Q153 | varchar |  |  | SI | Presenta Lesiones |
| Q154 | varchar |  |  | SI | En caso afirmativo describa |
| Q155 | varchar |  |  | SI | Se recolecta evidencia  física |
| Q156 | varchar |  |  | SI | Cuál ? |
| Q157 | varchar |  |  | SI | Región Glútea |
| Q158 | varchar |  |  | SI | Presenta Lesiones |
| Q159 | varchar |  |  | SI | En caso afirmativo describa |
| Q16 | varchar |  |  | SI | Estado civil |
| Q160 | varchar |  |  | SI | Se recolecta evidencia física |
| Q161 | varchar |  |  | SI | Cuál ? |
| Q162 | varchar |  |  | SI | Extremidades |
| Q163 | varchar |  |  | SI | Axilas: Presenta Lesiones |
| Q164 | varchar |  |  | SI | En caso afirmativo describa |
| Q165 | varchar |  |  | SI | Se recolecta evidencia física |
| Q166 | varchar |  |  | SI | Cuál ? |
| Q167 | varchar |  |  | SI | Miembros superiores: Presenta Lesiones |
| Q168 | varchar |  |  | SI | En caso afirmativo describa |
| Q169 | varchar |  |  | SI | Se recolecta evidencia física |
| Q17 | varchar |  |  | SI | Nivel educacional |
| Q170 | varchar |  |  | SI | Cuál ? |
| Q171 | varchar |  |  | SI | Miembros inferiores: Presenta Lesiones |
| Q172 | varchar |  |  | SI | En caso afirmativo describa |
| Q173 | varchar |  |  | SI | Se recolecta evidencia física |
| Q174 | varchar |  |  | SI | Cuál |
| Q175 | varchar |  |  | SI | Exámen genital |
| Q176 | varchar |  |  | SI | Genitales externos femeninos |
| Q177 | varchar |  |  | SI | Desarrollo Tanner |
| Q178 | varchar |  |  | SI | Posición para el exámen |
| Q179 | varchar |  |  | SI | Cuál ? |
| Q18 | varchar |  |  | SI | Actividad |
| Q180 | varchar |  |  | SI | Región púbica (vello púbico según Tanner) |
| Q181 | varchar |  |  | SI | Labios mayores |
| Q182 | varchar |  |  | SI | Horquilla vulvar |
| Q183 | varchar |  |  | SI | Clítoris |
| Q184 | varchar |  |  | SI | Meato urinario |
| Q185 | varchar |  |  | SI | Vagina |
| Q186 | varchar |  |  | SI | Periné |
| Q187 | varchar |  |  | SI | Región inguinal |
| Q188 | varchar |  |  | SI | Himen (forma, integridad, elasticidad) |
| Q189 | varchar |  |  | SI | Forma del himen |
| Q19 | varchar |  |  | SI | B. Consentimiento Informado Médico Forense |
| Q190 | varchar |  |  | SI | Estado del himen |
| Q191 | varchar |  |  | SI | Descripción bordes y desgarros himeneales (utiliza... |
| Q192 | varchar |  |  | SI | Toma de muestras |
| Q193 | varchar |  |  | SI | Describa |
| Q194 | varchar |  |  | SI | Genitales externos masculinos |
| Q195 | varchar |  |  | SI | Desarrollo: Tanner |
| Q196 | varchar |  |  | SI | Bolsa escrotal (bilateralmente) |
| Q197 | varchar |  |  | SI | Testículos según Tanner |
| Q198 | varchar |  |  | SI | Pene y prepucio |
| Q199 | varchar |  |  | SI | Frenillo |
| Q20 | varchar |  |  | SI | C. Abordaje del Caso |
| Q200 | varchar |  |  | SI | Surco balanoprepucial |
| Q201 | varchar |  |  | SI | Glande |
| Q202 | varchar |  |  | SI | Meato urinario |
| Q203 | varchar |  |  | SI | Toma de muestras |
| Q204 | varchar |  |  | SI | Describa |
| Q205 | varchar |  |  | SI | Examen anal y perianal |
| Q206 | varchar |  |  | SI | Posición para el examen |
| Q207 | varchar |  |  | SI | Cuál ? |
| Q208 | varchar |  |  | SI | Forma |
| Q209 | varchar |  |  | SI | Tono |
| Q21 | varchar |  |  | SI | 1. Información adicional al peritaje |
| Q210 | varchar |  |  | SI | Descripción de fisuras, edema, borramiento de plie... |
| Q211 | varchar |  |  | SI | Toma de muestras |
| Q212 | varchar |  |  | SI | En caso afirmativo describa |
| Q213 | varchar |  |  | SI | 5.3 Valoración de embriaguez por alcohol y otras s... |
| Q214 | varchar |  |  | SI | Se realiza examen clínico para determinar embriagu... |
| Q215 | varchar |  |  | SI | Olores asociados: Aliento alcohólico |
| Q216 | varchar |  |  | SI | Otros (describa) |
| Q217 | varchar |  |  | SI | Sensorio |
| Q218 | varchar |  |  | SI | Estado de conciencia |
| Q219 | varchar |  |  | SI | Orientación |
| Q22 | varchar |  |  | SI | 2. Exámen Médico Forense |
| Q220 | varchar |  |  | SI | Atención |
| Q221 | varchar |  |  | SI | Memoria |
| Q222 | varchar |  |  | SI | Lenguaje: Disartria |
| Q223 | varchar |  |  | SI | otras alteraciones |
| Q224 | varchar |  |  | SI | Cuáles? |
| Q225 | varchar |  |  | SI | Ojos |
| Q226 | varchar |  |  | SI | Congestión conjuntival |
| Q227 | varchar |  |  | SI | Pupilas |
| Q228 | varchar |  |  | SI | Observaciones o comentarios |
| Q229 | varchar |  |  | SI | Estudios solicitados |
| Q23 | varchar |  |  | SI | 2.1 Anamnesis: (breve relato/estado emocional) |
| Q230 | varchar |  |  | SI | Alcoholemia |
| Q231 | varchar |  |  | SI | Toxicológico en sangre |
| Q232 | varchar |  |  | SI | Toxicológico en Orina |
| Q233 | varchar |  |  | SI | Contenido gástrico |
| Q234 | varchar |  |  | SI | Contenido vaginal, vulvar y perivulvar |
| Q235 | varchar |  |  | SI | NUE |
| Q236 | varchar |  |  | SI | Destino |
| Q237 | varchar |  |  | SI | Contenido rectal |
| Q238 | varchar |  |  | SI | NUE |
| Q239 | varchar |  |  | SI | Destino |
| Q24 | varchar |  |  | SI | Información suministrada por |
| Q240 | varchar |  |  | SI | Contenido bucal |
| Q241 | varchar |  |  | SI | NUE |
| Q242 | varchar |  |  | SI | Destino |
| Q243 | varchar |  |  | SI | Contenido genital masculino |
| Q244 | varchar |  |  | SI | NUE |
| Q245 | varchar |  |  | SI | Destino |
| Q246 | varchar |  |  | SI | Estudio de ITS por PCR |
| Q247 | varchar |  |  | SI | NUE |
| Q248 | varchar |  |  | SI | Destino |
| Q249 | varchar |  |  | SI | BHCG para diagnóstico de embarazo |
| Q25 | varchar |  |  | SI | Nombre de acompañante que entrega datos |
| Q250 | varchar |  |  | SI | NUE |
| Q251 | varchar |  |  | SI | Destino |
| Q252 | varchar |  |  | SI | Estudio de manchas en ropas |
| Q253 | varchar |  |  | SI | NUE |
| Q254 | varchar |  |  | SI | Destino |
| Q255 | varchar |  |  | SI | Muestra lecho ungueal |
| Q256 | varchar |  |  | SI | NUE |
| Q257 | varchar |  |  | SI | Destino |
| Q258 | varchar |  |  | SI | Recolección de vello púbico |
| Q259 | varchar |  |  | SI | NUE |
| Q26 | varchar |  |  | SI | Relación con el paciente |
| Q260 | varchar |  |  | SI | Destino |
| Q261 | varchar |  |  | SI | Recolección de material extraño |
| Q262 | varchar |  |  | SI | NUE |
| Q263 | varchar |  |  | SI | Destino |
| Q264 | varchar |  |  | SI | Toma de muestra basal VIH |
| Q265 | varchar |  |  | SI | NUE |
| Q266 | varchar |  |  | SI | Destino |
| Q267 | varchar |  |  | SI | Muestra basal VDRL |
| Q268 | varchar |  |  | SI | NUE |
| Q269 | varchar |  |  | SI | Destino |
| Q27 | varchar |  |  | SI | Lugar de los hechos |
| Q270 | varchar |  |  | SI | Muestra basal antígeno de superficie Hepatitis B |
| Q271 | varchar |  |  | SI | NUE |
| Q272 | varchar |  |  | SI | Destino |
| Q273 | varchar |  |  | SI | Profilaxis ITS (Esquema indicado) |
| Q274 | varchar |  |  | SI | Profilaxis VIH (Esquema indicado) |
| Q275 | varchar |  |  | SI | Derivación para profilaxis (inmunización) Cuál? |
| Q276 | varchar |  |  | SI | Anticoncepción de emergencia |
| Q277 | varchar |  |  | SI | D. DOCUMENTACIÓN DE HALLAZGOS |
| Q278 | varchar |  |  | SI | Fotografías |
| Q279 | varchar |  |  | SI | Diagramas |
| Q28 | date |  |  | SI | Fecha de los hechos |
| Q280 | varchar |  |  | SI | Radiografías |
| Q281 | varchar |  |  | SI | Ecografías |
| Q282 | varchar |  |  | SI | Otros |
| Q283 | varchar |  |  | SI | E. MUESTRAS Y ELEMENTOS PARA ESTUDIO |
| Q284 | varchar |  |  | SI | F. INTERCONSULTAS |
| Q285 | varchar |  |  | SI | G. ANÁLISIS, INTERPRETACIÓN Y CONCLUSIONES |
| Q286 | varchar |  |  | SI | G. ANALISIS , INTERPRETACION Y CONCLUSIONES |
| Q287 | varchar |  |  | SI | H. SUGERENCIAS Y RECOMENDACIONES |
| Q288 | varchar |  |  | SI | 1. Interconsulta |
| Q289 | varchar |  |  | SI | 2. Solicitud de medida cautelar |
| Q29 | varchar |  |  | SI | Hora de los hechos |
| Q290 | varchar |  |  | SI | 3. Otras recomendaciones |
| Q291 | varchar |  |  | SI | I. NOMBRE, FIRMA, RUT Y CÓDIGO DEL MEDICO QUE REAL... |
| Q292 | varchar |  |  | SI | Nombre |
| Q293 | varchar |  |  | SI | RUT |
| Q294 | varchar |  |  | SI | Firma |
| Q295 | varchar |  |  | SI | J. INFORME (Denuncia) |
| Q296 | varchar |  |  | SI | 1. Informe a Fiscalía |
| Q297 | varchar |  |  | SI | Nombre de quién recibe la información |
| Q298 | varchar |  |  | SI | N° Identificación |
| Q299 | numeric |  |  | SI | Teléfono |
| Q30 | varchar |  |  | SI | 2.2 Presunto agresor |
| Q300 | varchar |  |  | SI | Reportado por (Nombre) |
| Q301 | date |  |  | SI | Fecha |
| Q302 | time |  |  | SI | Hora |
| Q303 | varchar |  |  | SI | 2. Policía o autoridad que soliicta el exámen médi... |
| Q304 | varchar |  |  | SI | Nombre del funcionario |
| Q305 | varchar |  |  | SI | N° Identificación |
| Q306 | varchar |  |  | SI | Institución |
| Q307 | numeric |  |  | SI | Teléfono contacto |
| Q308 | date |  |  | SI | Fecha |
| Q309 | time |  |  | SI | Hora |
| Q31 | varchar |  |  | SI | Sexo |
| Q310 | varchar |  |  | SI | Número de parte (si se encuentra con el ) |
| Q311 | varchar |  |  | SI | 3. Otro Cuál ? Describa |
| Q312 | varchar |  |  | SI | Cuál ? |
| Q313 | varchar |  |  | SI | Imagen cara cabeza |
| Q314 | varchar |  |  | SI | Imagen cavidad oral |
| Q315 | varchar |  |  | SI | Imagen cuerpo completo |
| Q316 | varchar |  |  | SI | Imagen genitales femeninos |
| Q317 | varchar |  |  | SI | Imagen genitales masculinos |
| Q318 | varchar |  |  | SI | Imagen anal y perianal |
| Q32 | numeric |  |  | SI | N° agresores |
| Q33 | varchar |  |  | SI | Relación con la víctima |
| Q34 | varchar |  |  | SI | Cantidad estimada de agresores |
| Q35 | varchar |  |  | SI | Métodos empleados por el agresor |
| Q36 | varchar |  |  | SI | Tipos de armas |
| Q37 | varchar |  |  | SI | Otras |
| Q38 | varchar |  |  | SI | El agresor se encontraba bajo el efecto del alcoho... |
| Q39 | varchar |  |  | SI | El agresor resultó lesionado en los hechos |
| Q40 | varchar |  |  | SI | Si resultó lesionado, describa el área del cuerpo ... |
| Q41 | varchar |  |  | SI | 2.3 Actos descritos por el paciente |
| Q42 | varchar |  |  | SI | Penetración del pene en |
| Q43 | varchar |  |  | SI | Penetración de objeto diferente al pene en  |
| Q44 | varchar |  |  | SI | Eyaculación |
| Q45 | varchar |  |  | SI | Sitio de eyaculación |
| Q46 | varchar |  |  | SI | ¿Utilizó condón? |
| Q47 | varchar |  |  | SI | Uso de lubricantes |
| Q48 | varchar |  |  | SI | Otras maniobras |
| Q49 | varchar |  |  | SI | Otros (describa) |
| Q50 | varchar |  |  | SI | Utilización de alcohol o drogas |
| Q51 | varchar |  |  | SI | Describa |
| Q52 | varchar |  |  | SI | Durante los hechos resultó lesionada/o la víctima |
| Q53 | varchar |  |  | SI | Recibió atención médica previa a este examen |
| Q54 | varchar |  |  | SI | Dónde? Cuál? |
| Q55 | varchar |  |  | SI | 2.4 Actividades posteriores a los hechos (No aplic... |
| Q56 | varchar |  |  | SI | Orinó |
| Q57 | varchar |  |  | SI | Defecó |
| Q58 | varchar |  |  | SI | Ducha vaginal |
| Q59 | varchar |  |  | SI | Baño, ducha, lavado corporal |
| Q60 | varchar |  |  | SI | Vomitó |
| Q61 | varchar |  |  | SI | Ingirió alimentos o bebidas |
| Q62 | varchar |  |  | SI | Lavado de dientes |
| Q63 | varchar |  |  | SI | Uso enjuague bucal |
| Q64 | varchar |  |  | SI | Se cambió ropa |
| Q65 | varchar |  |  | SI | Insertó o retiró tampón/diafragma |
| Q66 | varchar |  |  | SI | Otro |
| Q67 | varchar |  |  | SI | Describe |
| Q68 | varchar |  |  | SI | 3. Antecedentes |
| Q69 | varchar |  |  | SI | Antecedentes Ginecológicos |
| Q70 | varchar |  |  | SI | Menarquia |
| Q71 | varchar |  |  | SI | Ciclos |
| Q72 | date |  |  | SI | Fecha última menstruación |
| Q73 | numeric |  |  | SI | Partos |
| Q74 | numeric |  |  | SI | Abortos |
| Q75 | numeric |  |  | SI | Vivos |
| Q76 | date |  |  | SI | Fecha de último parto |
| Q77 | varchar |  |  | SI | Cirugía ginecológica |
| Q78 | varchar |  |  | SI | En caso afirmativo, Cuál? |
| Q79 | varchar |  |  | SI | Método anticonceptivo |
| Q80 | varchar |  |  | SI | Cuál |
| Q81 | varchar |  |  | SI | Antecedentes Sexuales |
| Q82 | varchar |  |  | SI | Otras relaciones en las últimas 48 horas |
| Q83 | varchar |  |  | SI | En caso afirmativo |
| Q84 | varchar |  |  | SI | Vaginal |
| Q85 | varchar |  |  | SI | Cuándo? |
| Q86 | varchar |  |  | SI | Anal |
| Q87 | varchar |  |  | SI | Cuándo? |
| Q88 | varchar |  |  | SI | Oral |
| Q89 | varchar |  |  | SI | Cuándo? |
| Q90 | varchar |  |  | SI | Hubo eyaculación |
| Q91 | varchar |  |  | SI | En caso afirmativo, dónde? |
| Q92 | varchar |  |  | SI | Se usó condón? |
| Q93 | varchar |  |  | SI | Antecedentes médicos, quirúrgicos y urológicos |
| Q94 | varchar |  |  | SI | Alergias |
| Q95 | varchar |  |  | SI | Cuáles? |
| Q96 | varchar |  |  | SI | Inmunización |
| Q97 | varchar |  |  | SI | 4. Descripción de Prendas |
| Q98 | varchar |  |  | SI | Viste las prendas que usaba cuando ocurrieron los ... |
| Q99 | varchar |  |  | SI | Las trae al examen |
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