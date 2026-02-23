# SQLUser.ARC_SurchEpisSubtype

**Schema:** SQLUser
**Columnas:** 380
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPIS_ParRef | bigint | PK |  | NO | ARC_SurchargeCode Parent Reference |
| ChildQ103DR | - |  |  | SI | Child Reference: Prendas |
| EPIS_Childsub | double |  |  | NO | Childsub |
| EPIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPIS_CreatedDate | date |  |  | SI | Created Date |
| EPIS_CreatedTime | time |  |  | SI | Created Time |
| EPIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPIS_DateFrom | date |  |  | SI | Date From |
| EPIS_DateTo | date |  |  | SI | Date To |
| EPIS_EpisSubtype_DR | bigint |  | FK | SI | Des Ref EpisSubtype |
| EPIS_FixedAmt | double |  |  | SI | Fixed Amount |
| EPIS_Perc | double |  |  | SI | % Charge |
| EPIS_RowId | varchar |  |  | NO | - |
| EPIS_UpdatedDate | date |  |  | SI | Updated Date |
| EPIS_UpdatedTime | time |  |  | SI | Updated Time |
| EPIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | A. Información General |
| Q02 | - |  |  | SI | Institución en la que realiza el examen |
| Q03 | - |  |  | SI | Ciudad del examen |
| Q04 | - |  |  | SI | Fecha del examen |
| Q05 | - |  |  | SI | Horas del examen |
| Q06 | - |  |  | SI | N° Documento de identidad |
| Q07 | - |  |  | SI | N° de Informe |
| Q08 | - |  |  | SI | Nombre del examinado |
| Q09 | - |  |  | SI | Apellido Paterno |
| Q10 | - |  |  | SI | Apellido Materno |
| Q100 | - |  |  | SI | Dónde se encuentran |
| Q101 | - |  |  | SI | Se dejan para estudio |
| Q102 | - |  |  | SI | Observaciones |
| Q104 | - |  |  | SI | 5. Examen Médico Forense |
| Q105 | - |  |  | SI | Peso |
| Q105ObsDR | - |  |  | SI | Peso DR |
| Q106 | - |  |  | SI | Talla |
| Q106ObsDR | - |  |  | SI | Talla DR |
| Q107 | - |  |  | SI | Signos vitales |
| Q108 | - |  |  | SI | P/A |
| Q108ObsDR | - |  |  | SI | P/A DR |
| Q109 | - |  |  | SI | Presión Sistólica |
| Q109ObsDR | - |  |  | SI | Presión Sistólica DR |
| Q11 | - |  |  | SI | Edad |
| Q110 | - |  |  | SI | FC |
| Q110ObsDR | - |  |  | SI | FC DR |
| Q111 | - |  |  | SI | FR |
| Q111ObsDR | - |  |  | SI | FR DR |
| Q112 | - |  |  | SI | Temp |
| Q112ObsDR | - |  |  | SI | Temp DR |
| Q113 | - |  |  | SI | 5.1 Aspecto General |
| Q114 | - |  |  | SI | 5.2 Descripción de hallazgos y recolección de evid... |
| Q115 | - |  |  | SI | Valoración de la zona subungueal |
| Q116 | - |  |  | SI | Presenta lesiones |
| Q117 | - |  |  | SI | En caso afirmativo describa |
| Q118 | - |  |  | SI | Describa el aspecto general 5.1 |
| Q119 | - |  |  | SI | Se recolecta evidencia física |
| Q12 | - |  |  | SI | Fecha de nacimiento |
| Q120 | - |  |  | SI | Cara, cabeza (cuero cabelludo, pelo), cuello: |
| Q121 | - |  |  | SI | Presenta Lesiones |
| Q122 | - |  |  | SI | En caso afirmativo describa |
| Q123 | - |  |  | SI | Se recolecta evidencia física |
| Q124 | - |  |  | SI | Cuál |
| Q125 | - |  |  | SI | Cavidad oral |
| Q126 | - |  |  | SI | Presenta Lesiones |
| Q127 | - |  |  | SI | En caso afirmativo describa |
| Q128 | - |  |  | SI | Se recolecta evidencia física |
| Q129 | - |  |  | SI | Cuál ? |
| Q13 | - |  |  | SI | Sexo |
| Q130 | - |  |  | SI | En niños y niñas describa tipo de dentinción |
| Q131 | - |  |  | SI | Fase inicial |
| Q132 | - |  |  | SI | Media |
| Q133 | - |  |  | SI | Completa |
| Q134 | - |  |  | SI | Tórax |
| Q135 | - |  |  | SI | Presenta Lesiones |
| Q136 | - |  |  | SI | En caso afirmativo describa |
| Q137 | - |  |  | SI | Se recolecta evidencia física |
| Q138 | - |  |  | SI | Cuál |
| Q139 | - |  |  | SI | Mamas |
| Q14 | - |  |  | SI | Dirección |
| Q140 | - |  |  | SI | Presenta Lesiones |
| Q141 | - |  |  | SI | En caso afirmativo describa |
| Q142 | - |  |  | SI | Se recolecta evidencia física |
| Q143 | - |  |  | SI | Cuál ? |
| Q144 | - |  |  | SI | En niñas y niños describa caracteres sexuales secu... |
| Q145 | - |  |  | SI | Abdomen |
| Q146 | - |  |  | SI | Presenta Lesiones |
| Q147 | - |  |  | SI | En caso afirmativo describa |
| Q148 | - |  |  | SI | Se recolecta evidencia física |
| Q149 | - |  |  | SI | Cuál ? |
| Q15 | - |  |  | SI | Teléfono contacto |
| Q150 | - |  |  | SI | Signos de embarazo |
| Q151 | - |  |  | SI | Describa |
| Q152 | - |  |  | SI | Espalda |
| Q153 | - |  |  | SI | Presenta Lesiones |
| Q154 | - |  |  | SI | En caso afirmativo describa |
| Q155 | - |  |  | SI | Se recolecta evidencia  física |
| Q156 | - |  |  | SI | Cuál ? |
| Q157 | - |  |  | SI | Región Glútea |
| Q158 | - |  |  | SI | Presenta Lesiones |
| Q159 | - |  |  | SI | En caso afirmativo describa |
| Q16 | - |  |  | SI | Estado civil |
| Q160 | - |  |  | SI | Se recolecta evidencia física |
| Q161 | - |  |  | SI | Cuál ? |
| Q162 | - |  |  | SI | Extremidades |
| Q163 | - |  |  | SI | Axilas: Presenta Lesiones |
| Q164 | - |  |  | SI | En caso afirmativo describa |
| Q165 | - |  |  | SI | Se recolecta evidencia física |
| Q166 | - |  |  | SI | Cuál ? |
| Q167 | - |  |  | SI | Miembros superiores: Presenta Lesiones |
| Q168 | - |  |  | SI | En caso afirmativo describa |
| Q169 | - |  |  | SI | Se recolecta evidencia física |
| Q17 | - |  |  | SI | Nivel educacional |
| Q170 | - |  |  | SI | Cuál ? |
| Q171 | - |  |  | SI | Miembros inferiores: Presenta Lesiones |
| Q172 | - |  |  | SI | En caso afirmativo describa |
| Q173 | - |  |  | SI | Se recolecta evidencia física |
| Q174 | - |  |  | SI | Cuál |
| Q175 | - |  |  | SI | Exámen genital |
| Q176 | - |  |  | SI | Genitales externos femeninos |
| Q177 | - |  |  | SI | Desarrollo Tanner |
| Q178 | - |  |  | SI | Posición para el exámen |
| Q179 | - |  |  | SI | Cuál ? |
| Q18 | - |  |  | SI | Actividad |
| Q180 | - |  |  | SI | Región púbica (vello púbico según Tanner) |
| Q181 | - |  |  | SI | Labios mayores |
| Q182 | - |  |  | SI | Horquilla vulvar |
| Q183 | - |  |  | SI | Clítoris |
| Q184 | - |  |  | SI | Meato urinario |
| Q185 | - |  |  | SI | Vagina |
| Q186 | - |  |  | SI | Periné |
| Q187 | - |  |  | SI | Región inguinal |
| Q188 | - |  |  | SI | Himen (forma, integridad, elasticidad) |
| Q189 | - |  |  | SI | Forma del himen |
| Q19 | - |  |  | SI | B. Consentimiento Informado Médico Forense |
| Q190 | - |  |  | SI | Estado del himen |
| Q191 | - |  |  | SI | Descripción bordes y desgarros himeneales (utiliza... |
| Q192 | - |  |  | SI | Toma de muestras |
| Q193 | - |  |  | SI | Describa |
| Q194 | - |  |  | SI | Genitales externos masculinos |
| Q195 | - |  |  | SI | Desarrollo: Tanner |
| Q196 | - |  |  | SI | Bolsa escrotal (bilateralmente) |
| Q197 | - |  |  | SI | Testículos según Tanner |
| Q198 | - |  |  | SI | Pene y prepucio |
| Q199 | - |  |  | SI | Frenillo |
| Q20 | - |  |  | SI | C. Abordaje del Caso |
| Q200 | - |  |  | SI | Surco balanoprepucial |
| Q201 | - |  |  | SI | Glande |
| Q202 | - |  |  | SI | Meato urinario |
| Q203 | - |  |  | SI | Toma de muestras |
| Q204 | - |  |  | SI | Describa |
| Q205 | - |  |  | SI | Examen anal y perianal |
| Q206 | - |  |  | SI | Posición para el examen |
| Q207 | - |  |  | SI | Cuál ? |
| Q208 | - |  |  | SI | Forma |
| Q209 | - |  |  | SI | Tono |
| Q21 | - |  |  | SI | 1. Información adicional al peritaje |
| Q210 | - |  |  | SI | Descripción de fisuras, edema, borramiento de plie... |
| Q211 | - |  |  | SI | Toma de muestras |
| Q212 | - |  |  | SI | En caso afirmativo describa |
| Q213 | - |  |  | SI | 5.3 Valoración de embriaguez por alcohol y otras s... |
| Q214 | - |  |  | SI | Se realiza examen clínico para determinar embriagu... |
| Q215 | - |  |  | SI | Olores asociados: Aliento alcohólico |
| Q216 | - |  |  | SI | Otros (describa) |
| Q217 | - |  |  | SI | Sensorio |
| Q218 | - |  |  | SI | Estado de conciencia |
| Q219 | - |  |  | SI | Orientación |
| Q22 | - |  |  | SI | 2. Exámen Médico Forense |
| Q220 | - |  |  | SI | Atención |
| Q221 | - |  |  | SI | Memoria |
| Q222 | - |  |  | SI | Lenguaje: Disartria |
| Q223 | - |  |  | SI | otras alteraciones |
| Q224 | - |  |  | SI | Cuáles? |
| Q225 | - |  |  | SI | Ojos |
| Q226 | - |  |  | SI | Congestión conjuntival |
| Q227 | - |  |  | SI | Pupilas |
| Q228 | - |  |  | SI | Observaciones o comentarios |
| Q229 | - |  |  | SI | Estudios solicitados |
| Q23 | - |  |  | SI | 2.1 Anamnesis: (breve relato/estado emocional) |
| Q230 | - |  |  | SI | Alcoholemia |
| Q231 | - |  |  | SI | Toxicológico en sangre |
| Q232 | - |  |  | SI | Toxicológico en Orina |
| Q233 | - |  |  | SI | Contenido gástrico |
| Q234 | - |  |  | SI | Contenido vaginal, vulvar y perivulvar |
| Q235 | - |  |  | SI | NUE |
| Q236 | - |  |  | SI | Destino |
| Q237 | - |  |  | SI | Contenido rectal |
| Q238 | - |  |  | SI | NUE |
| Q239 | - |  |  | SI | Destino |
| Q24 | - |  |  | SI | Información suministrada por |
| Q240 | - |  |  | SI | Contenido bucal |
| Q241 | - |  |  | SI | NUE |
| Q242 | - |  |  | SI | Destino |
| Q243 | - |  |  | SI | Contenido genital masculino |
| Q244 | - |  |  | SI | NUE |
| Q245 | - |  |  | SI | Destino |
| Q246 | - |  |  | SI | Estudio de ITS por PCR |
| Q247 | - |  |  | SI | NUE |
| Q248 | - |  |  | SI | Destino |
| Q249 | - |  |  | SI | BHCG para diagnóstico de embarazo |
| Q25 | - |  |  | SI | Nombre de acompañante que entrega datos |
| Q250 | - |  |  | SI | NUE |
| Q251 | - |  |  | SI | Destino |
| Q252 | - |  |  | SI | Estudio de manchas en ropas |
| Q253 | - |  |  | SI | NUE |
| Q254 | - |  |  | SI | Destino |
| Q255 | - |  |  | SI | Muestra lecho ungueal |
| Q256 | - |  |  | SI | NUE |
| Q257 | - |  |  | SI | Destino |
| Q258 | - |  |  | SI | Recolección de vello púbico |
| Q259 | - |  |  | SI | NUE |
| Q26 | - |  |  | SI | Relación con el paciente |
| Q260 | - |  |  | SI | Destino |
| Q261 | - |  |  | SI | Recolección de material extraño |
| Q262 | - |  |  | SI | NUE |
| Q263 | - |  |  | SI | Destino |
| Q264 | - |  |  | SI | Toma de muestra basal VIH |
| Q265 | - |  |  | SI | NUE |
| Q266 | - |  |  | SI | Destino |
| Q267 | - |  |  | SI | Muestra basal VDRL |
| Q268 | - |  |  | SI | NUE |
| Q269 | - |  |  | SI | Destino |
| Q27 | - |  |  | SI | Lugar de los hechos |
| Q270 | - |  |  | SI | Muestra basal antígeno de superficie Hepatitis B |
| Q271 | - |  |  | SI | NUE |
| Q272 | - |  |  | SI | Destino |
| Q273 | - |  |  | SI | Profilaxis ITS (Esquema indicado) |
| Q274 | - |  |  | SI | Profilaxis VIH (Esquema indicado) |
| Q275 | - |  |  | SI | Derivación para profilaxis (inmunización) Cuál? |
| Q276 | - |  |  | SI | Anticoncepción de emergencia |
| Q277 | - |  |  | SI | D. DOCUMENTACIÓN DE HALLAZGOS |
| Q278 | - |  |  | SI | Fotografías |
| Q279 | - |  |  | SI | Diagramas |
| Q28 | - |  |  | SI | Fecha de los hechos |
| Q280 | - |  |  | SI | Radiografías |
| Q281 | - |  |  | SI | Ecografías |
| Q282 | - |  |  | SI | Otros |
| Q283 | - |  |  | SI | E. MUESTRAS Y ELEMENTOS PARA ESTUDIO |
| Q284 | - |  |  | SI | F. INTERCONSULTAS |
| Q285 | - |  |  | SI | G. ANÁLISIS, INTERPRETACIÓN Y CONCLUSIONES |
| Q286 | - |  |  | SI | G. ANALISIS , INTERPRETACION Y CONCLUSIONES |
| Q287 | - |  |  | SI | H. SUGERENCIAS Y RECOMENDACIONES |
| Q288 | - |  |  | SI | 1. Interconsulta |
| Q289 | - |  |  | SI | 2. Solicitud de medida cautelar |
| Q29 | - |  |  | SI | Hora de los hechos |
| Q290 | - |  |  | SI | 3. Otras recomendaciones |
| Q291 | - |  |  | SI | I. NOMBRE, FIRMA, RUT Y CÓDIGO DEL MEDICO QUE REAL... |
| Q292 | - |  |  | SI | Nombre |
| Q293 | - |  |  | SI | RUT |
| Q294 | - |  |  | SI | Firma |
| Q295 | - |  |  | SI | J. INFORME (Denuncia) |
| Q296 | - |  |  | SI | 1. Informe a Fiscalía |
| Q297 | - |  |  | SI | Nombre de quién recibe la información |
| Q298 | - |  |  | SI | N° Identificación |
| Q299 | - |  |  | SI | Teléfono |
| Q30 | - |  |  | SI | 2.2 Presunto agresor |
| Q300 | - |  |  | SI | Reportado por (Nombre) |
| Q301 | - |  |  | SI | Fecha |
| Q302 | - |  |  | SI | Hora |
| Q303 | - |  |  | SI | 2. Policía o autoridad que soliicta el exámen médi... |
| Q304 | - |  |  | SI | Nombre del funcionario |
| Q305 | - |  |  | SI | N° Identificación |
| Q306 | - |  |  | SI | Institución |
| Q307 | - |  |  | SI | Teléfono contacto |
| Q308 | - |  |  | SI | Fecha |
| Q309 | - |  |  | SI | Hora |
| Q31 | - |  |  | SI | Sexo |
| Q310 | - |  |  | SI | Número de parte (si se encuentra con el ) |
| Q311 | - |  |  | SI | 3. Otro Cuál ? Describa |
| Q312 | - |  |  | SI | Cuál ? |
| Q313 | - |  |  | SI | Imagen cara cabeza |
| Q314 | - |  |  | SI | Imagen cavidad oral |
| Q315 | - |  |  | SI | Imagen cuerpo completo |
| Q316 | - |  |  | SI | Imagen genitales femeninos |
| Q317 | - |  |  | SI | Imagen genitales masculinos |
| Q318 | - |  |  | SI | Imagen anal y perianal |
| Q32 | - |  |  | SI | N° agresores |
| Q33 | - |  |  | SI | Relación con la víctima |
| Q34 | - |  |  | SI | Cantidad estimada de agresores |
| Q35 | - |  |  | SI | Métodos empleados por el agresor |
| Q36 | - |  |  | SI | Tipos de armas |
| Q37 | - |  |  | SI | Otras |
| Q38 | - |  |  | SI | El agresor se encontraba bajo el efecto del alcoho... |
| Q39 | - |  |  | SI | El agresor resultó lesionado en los hechos |
| Q40 | - |  |  | SI | Si resultó lesionado, describa el área del cuerpo ... |
| Q41 | - |  |  | SI | 2.3 Actos descritos por el paciente |
| Q42 | - |  |  | SI | Penetración del pene en |
| Q43 | - |  |  | SI | Penetración de objeto diferente al pene en |
| Q44 | - |  |  | SI | Eyaculación |
| Q45 | - |  |  | SI | Sitio de eyaculación |
| Q46 | - |  |  | SI | ¿Utilizó condón? |
| Q47 | - |  |  | SI | Uso de lubricantes |
| Q48 | - |  |  | SI | Otras maniobras |
| Q49 | - |  |  | SI | Otros (describa) |
| Q50 | - |  |  | SI | Utilización de alcohol o drogas |
| Q51 | - |  |  | SI | Describa |
| Q52 | - |  |  | SI | Durante los hechos resultó lesionada/o la víctima |
| Q53 | - |  |  | SI | Recibió atención médica previa a este examen |
| Q54 | - |  |  | SI | Dónde? Cuál? |
| Q55 | - |  |  | SI | 2.4 Actividades posteriores a los hechos (No aplic... |
| Q56 | - |  |  | SI | Orinó |
| Q57 | - |  |  | SI | Defecó |
| Q58 | - |  |  | SI | Ducha vaginal |
| Q59 | - |  |  | SI | Baño, ducha, lavado corporal |
| Q60 | - |  |  | SI | Vomitó |
| Q61 | - |  |  | SI | Ingirió alimentos o bebidas |
| Q62 | - |  |  | SI | Lavado de dientes |
| Q63 | - |  |  | SI | Uso enjuague bucal |
| Q64 | - |  |  | SI | Se cambió ropa |
| Q65 | - |  |  | SI | Insertó o retiró tampón/diafragma |
| Q66 | - |  |  | SI | Otro |
| Q67 | - |  |  | SI | Describe |
| Q68 | - |  |  | SI | 3. Antecedentes |
| Q69 | - |  |  | SI | Antecedentes Ginecológicos |
| Q70 | - |  |  | SI | Menarquia |
| Q71 | - |  |  | SI | Ciclos |
| Q72 | - |  |  | SI | Fecha última menstruación |
| Q73 | - |  |  | SI | Partos |
| Q74 | - |  |  | SI | Abortos |
| Q75 | - |  |  | SI | Vivos |
| Q76 | - |  |  | SI | Fecha de último parto |
| Q77 | - |  |  | SI | Cirugía ginecológica |
| Q78 | - |  |  | SI | En caso afirmativo, Cuál? |
| Q79 | - |  |  | SI | Método anticonceptivo |
| Q80 | - |  |  | SI | Cuál |
| Q81 | - |  |  | SI | Antecedentes Sexuales |
| Q82 | - |  |  | SI | Otras relaciones en las últimas 48 horas |
| Q83 | - |  |  | SI | En caso afirmativo |
| Q84 | - |  |  | SI | Vaginal |
| Q85 | - |  |  | SI | Cuándo? |
| Q86 | - |  |  | SI | Anal |
| Q87 | - |  |  | SI | Cuándo? |
| Q88 | - |  |  | SI | Oral |
| Q89 | - |  |  | SI | Cuándo? |
| Q90 | - |  |  | SI | Hubo eyaculación |
| Q91 | - |  |  | SI | En caso afirmativo, dónde? |
| Q92 | - |  |  | SI | Se usó condón? |
| Q93 | - |  |  | SI | Antecedentes médicos, quirúrgicos y urológicos |
| Q94 | - |  |  | SI | Alergias |
| Q95 | - |  |  | SI | Cuáles? |
| Q96 | - |  |  | SI | Inmunización |
| Q97 | - |  |  | SI | 4. Descripción de Prendas |
| Q98 | - |  |  | SI | Viste las prendas que usaba cuando ocurrieron los ... |
| Q99 | - |  |  | SI | Las trae al examen |
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