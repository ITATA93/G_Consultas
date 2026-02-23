# SQLUser.MRC_BodySystems

**Schema:** SQLUser
**Columnas:** 335
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BODS_RowId | bigint | PK |  | NO | - |
| BODS_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| BODS_Code | varchar |  |  | NO | Code |
| BODS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BODS_CreatedDate | date |  |  | SI | Created Date |
| BODS_CreatedTime | time |  |  | SI | Created Time |
| BODS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BODS_Desc | varchar |  |  | NO | Description |
| BODS_Owner | varchar |  |  | SI | Owner |
| BODS_UpdatedDate | date |  |  | SI | Updated Date |
| BODS_UpdatedTime | time |  |  | SI | Updated Time |
| BODS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ171DR | - |  |  | SI | Child Reference: Inspección TI |
| Q01 | - |  |  | SI | Nombre de la madre |
| Q02 | - |  |  | SI | RUT de la madre |
| Q03 | - |  |  | SI | Pasaporte de la madre |
| Q04 | - |  |  | SI | Dirección de la madre |
| Q05 | - |  |  | SI | Dirección de la madre (comuna) |
| Q06 | - |  |  | SI | Dirección de la madre (Otro) |
| Q07 | - |  |  | SI | Edad de la madre |
| Q08 | - |  |  | SI | Último curso realizado |
| Q09 | - |  |  | SI | Nivel educacional |
| Q10 | - |  |  | SI | Ocupación |
| Q100 | - |  |  | SI | Años de Consumo |
| Q101 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q102 | - |  |  | SI | Consumo de Drogas |
| Q103 | - |  |  | SI | Otra Droga |
| Q104 | - |  |  | SI | Síntomas Presentes |
| Q105 | - |  |  | SI | Otro Síntoma |
| Q106 | - |  |  | SI | Observaciones/Comentarios |
| Q107 | - |  |  | SI | Estado General |
| Q108 | - |  |  | SI | Valoración del dolor |
| Q109 | - |  |  | SI | Estado Psíquico |
| Q109ObsDR | - |  |  | SI | Estado Psíquico DR |
| Q11 | - |  |  | SI | Categoría ocupacional |
| Q110 | - |  |  | SI | Conciencia |
| Q110ObsDR | - |  |  | SI | Conciencia DR |
| Q111 | - |  |  | SI | Piel |
| Q111ObsDR | - |  |  | SI | Piel DR |
| Q112 | - |  |  | SI | Mucosas |
| Q112ObsDR | - |  |  | SI | Mucosas DR |
| Q113 | - |  |  | SI | Cabeza-Cara |
| Q113ObsDR | - |  |  | SI | Cabeza-Cara DR |
| Q114 | - |  |  | SI | Pupilas |
| Q114ObsDR | - |  |  | SI | Pupilas DR |
| Q115 | - |  |  | SI | Conjuntivas |
| Q115ObsDR | - |  |  | SI | Conjuntivas DR |
| Q116 | - |  |  | SI | Dentadura |
| Q116ObsDR | - |  |  | SI | Dentadura DR |
| Q117 | - |  |  | SI | Lenguage |
| Q117ObsDR | - |  |  | SI | Lenguage DR |
| Q118 | - |  |  | SI | Cuello |
| Q118ObsDR | - |  |  | SI | Cuello DR |
| Q119 | - |  |  | SI | Vía Aérea |
| Q119ObsDR | - |  |  | SI | Vía Aérea DR |
| Q12 | - |  |  | SI | Nombre del progenitor |
| Q120 | - |  |  | SI | Respiración |
| Q120ObsDR | - |  |  | SI | Respiración DR |
| Q121 | - |  |  | SI | Tórax |
| Q121ObsDR | - |  |  | SI | Tórax DR |
| Q122 | - |  |  | SI | Cardíaco |
| Q122ObsDR | - |  |  | SI | Cardíaco DR |
| Q123 | - |  |  | SI | Ritmo Cardíaco |
| Q123ObsDR | - |  |  | SI | Ritmo Cardíaco DR |
| Q124 | - |  |  | SI | Mamas |
| Q124ObsDR | - |  |  | SI | Mamas DR |
| Q125 | - |  |  | SI | Pezones |
| Q125ObsDR | - |  |  | SI | Pezones DR |
| Q126 | - |  |  | SI | Útero |
| Q126ObsDR | - |  |  | SI | Útero DR |
| Q127 | - |  |  | SI | Abdomen |
| Q127ObsDR | - |  |  | SI | Abdomen DR |
| Q128 | - |  |  | SI | Extremidades Superiores |
| Q128ObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q129 | - |  |  | SI | Extremidades Inferiores |
| Q129ObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q13 | - |  |  | SI | RUT / Pasaporte del progenitor |
| Q130 | - |  |  | SI | Edema |
| Q130ObsDR | - |  |  | SI | Edema DR |
| Q131 | - |  |  | SI | Genito Urinario |
| Q131ObsDR | - |  |  | SI | Genito Urinario DR |
| Q132 | - |  |  | SI | Ano |
| Q132ObsDR | - |  |  | SI | Ano DR |
| Q133 | - |  |  | SI | Diuresis |
| Q133ObsDR | - |  |  | SI | Diuresis DR |
| Q134 | - |  |  | SI | Deposiciones |
| Q134ObsDR | - |  |  | SI | Deposiciones DR |
| Q135 | - |  |  | SI | Comentario (Estado) |
| Q136 | - |  |  | SI | Comentario (Conciencia) |
| Q137 | - |  |  | SI | Comentario (Piel) |
| Q138 | - |  |  | SI | Comentario (Mucosas) |
| Q139 | - |  |  | SI | Comentario (Cabeza) |
| Q14 | - |  |  | SI | Edad del progenitor |
| Q140 | - |  |  | SI | Comentario (Pupilas) |
| Q141 | - |  |  | SI | Comentario (Conjuntivas) |
| Q142 | - |  |  | SI | Comentario (Dentadura) |
| Q143 | - |  |  | SI | Comentario (Lenguage) |
| Q144 | - |  |  | SI | Comentario (Cuello) |
| Q145 | - |  |  | SI | Comentario (Via) |
| Q146 | - |  |  | SI | Comentario (Respiración) |
| Q147 | - |  |  | SI | Comentario (Toráx) |
| Q148 | - |  |  | SI | Comentario (Cardiaco) |
| Q149 | - |  |  | SI | Comentario (Ritmo) |
| Q15 | - |  |  | SI | Último curso realizado (progenitor) |
| Q150 | - |  |  | SI | Comentario (Mamas) |
| Q151 | - |  |  | SI | Comentario (Pezones) |
| Q152 | - |  |  | SI | Comentario (utero) |
| Q153 | - |  |  | SI | Comentario (Abdomen) |
| Q154 | - |  |  | SI | Comentario (ES) |
| Q155 | - |  |  | SI | Comentario (EI) |
| Q156 | - |  |  | SI | Comentario (Edema) |
| Q157 | - |  |  | SI | Comentario (GU) |
| Q158 | - |  |  | SI | Comentario (Ano) |
| Q159 | - |  |  | SI | Comentario (Diuresis) |
| Q16 | - |  |  | SI | Nivel educacional (progenitor) |
| Q160 | - |  |  | SI | Comentario (Deposiciones) |
| Q161 | - |  |  | SI | Comentarios Generales EO |
| Q162 | - |  |  | SI | Resto del examen ginecológico realizado, sin alter... |
| Q163 | - |  |  | SI | Inspección CG |
| Q164 | - |  |  | SI | Tacto vaginal CG |
| Q165 | - |  |  | SI | Especuloscopía CG |
| Q166 | - |  |  | SI | Examen mamas CG |
| Q167 | - |  |  | SI | Inspección TA |
| Q168 | - |  |  | SI | Tacto vaginal TA |
| Q169 | - |  |  | SI | Especuloscopia TA |
| Q17 | - |  |  | SI | Ocupación (progenitor) |
| Q170 | - |  |  | SI | Exames mamas TA |
| Q172 | - |  |  | SI | Descripción |
| Q173 | - |  |  | SI | Tacto vaginal CG2 |
| Q174 | - |  |  | SI | Tacto Vaginal CG 3 |
| Q175 | - |  |  | SI | Grafico IMC |
| Q176 | - |  |  | SI | ¿Embarazo Deseado? |
| Q177 | - |  |  | SI | Religión |
| Q178 | - |  |  | SI | Religión |
| Q179 | - |  |  | SI | Cigarrilos por día |
| Q18 | - |  |  | SI | Categoría ocupacional (progenitor) |
| Q180 | - |  |  | SI | Años de Consumo |
| Q181 | - |  |  | SI | Otra Patología |
| Q182 | - |  |  | SI | Escala del Dolor |
| Q182ObsDR | - |  |  | SI | Escala del Dolor DR |
| Q183 | - |  |  | SI | Razones para no Evaluar Dolor |
| Q184 | - |  |  | SI | Especifique |
| Q185 | - |  |  | SI | Ubicación del Dolor |
| Q186 | - |  |  | SI | Labios mayores y menores de tamaño y aspecto norma... |
| Q187 | - |  |  | SI | Clitoris de tamaño y aspecto normal |
| Q188 | - |  |  | SI | Glándulas de Bartholino normales |
| Q189 | - |  |  | SI | Paredes vaginales elásticas. Mucosa vaginal normal... |
| Q19 | - |  |  | SI | Dirección del progenitor (Calle, N°, comuna) |
| Q190 | - |  |  | SI | Saco de Douglas libre |
| Q191 | - |  |  | SI | Cuello uterino de consistencia y tamaño normal	 |
| Q192 | - |  |  | SI | Útero en anteroversión, de tamaño y consistencia n... |
| Q193 | - |  |  | SI | Flujo vaginal normal |
| Q194 | - |  |  | SI | Anexos libres e indoloros |
| Q195 | - |  |  | SI | Parametrios normales |
| Q196 | - |  |  | SI | Vagina de elasticidad conservada |
| Q197 | - |  |  | SI | Cuello central de coloración normal, sin lesiones ... |
| Q198 | - |  |  | SI | Mamas de tamaño y desarrollo normal, simétricas |
| Q199 | - |  |  | SI | No se palpan masas ni adenopatías locales |
| Q20 | - |  |  | SI | Pueblo originario |
| Q200 | - |  |  | SI | Pezones sin lesiones ni secreción anormal |
| Q201 | - |  |  | SI | Movimientos Fetales |
| Q201ObsDR | - |  |  | SI | Movimientos Fetales  DR |
| Q202 | - |  |  | SI | Presentación |
| Q202ObsDR | - |  |  | SI | Presentación  DR |
| Q203 | - |  |  | SI | Dorso Fetal |
| Q203ObsDR | - |  |  | SI | Dorso Fetal DR |
| Q204 | - |  |  | SI | Plano de Hodge |
| Q204ObsDR | - |  |  | SI | Plano de Hodge  DR |
| Q205 | - |  |  | SI | Altura Uterina (cms) |
| Q205ObsDR | - |  |  | SI | Altura Uterina (cms)  DR |
| Q206 | - |  |  | SI | Tono  Uterino |
| Q206ObsDR | - |  |  | SI | Tono  Uterino DR |
| Q207 | - |  |  | SI | Dinámica Uterina |
| Q207ObsDR | - |  |  | SI | Dinámica Uterina  DR |
| Q208 | - |  |  | SI | Contracciones (Cada 10 min) |
| Q208ObsDR | - |  |  | SI | Contracciones (Cada 10 min) DR |
| Q209 | - |  |  | SI | Desaceleraciones |
| Q209ObsDR | - |  |  | SI | Desaceleraciones  DR |
| Q21 | - |  |  | SI | Grupo cultural |
| Q210 | - |  |  | SI | Líquido Amniótico |
| Q210ObsDR | - |  |  | SI | Líquido Amniótico  DR |
| Q211 | - |  |  | SI | Flujo Vaginal |
| Q211ObsDR | - |  |  | SI | Flujo Vaginal  DR |
| Q212 | - |  |  | SI | Membranas |
| Q212ObsDR | - |  |  | SI | Membranas  DR |
| Q213 | - |  |  | SI | Consistencia Cuello |
| Q213ObsDR | - |  |  | SI | Consistencia Cuello DR |
| Q214 | - |  |  | SI | Posición |
| Q214ObsDR | - |  |  | SI | Posición  DR |
| Q215 | - |  |  | SI | Borramiento |
| Q215ObsDR | - |  |  | SI | Borramiento DR |
| Q216 | - |  |  | SI | Dilatación Cervical |
| Q216ObsDR | - |  |  | SI | Dilatación Cervical DR |
| Q217 | - |  |  | SI | LCF Feto 1 (lpm) |
| Q217ObsDR | - |  |  | SI | LCF Feto 1 (lpm) DR |
| Q218 | - |  |  | SI | LCF Feto 2 (lpm) |
| Q218ObsDR | - |  |  | SI | LCF Feto 2 (lpm) DR |
| Q219 | - |  |  | SI | LCF Feto 3 (lpm) |
| Q219ObsDR | - |  |  | SI | LCF Feto 3 (lpm) DR |
| Q22 | - |  |  | SI | Fecha de término del último embarazo |
| Q220 | - |  |  | SI | Comentarios Examen Obstétrico |
| Q221 | - |  |  | SI | N° de Hijos Fallecidos Total |
| Q222 | - |  |  | SI | Plan de Ingreso |
| Q23 | - |  |  | SI | Fecha de inicio del control prenatal |
| Q24 | - |  |  | SI | Método anticonceptivo |
| Q25 | - |  |  | SI | ¿Embarazo planificado? |
| Q26 | - |  |  | SI | Causa de la última cesárea (si procede) |
| Q27 | - |  |  | SI | Peso habitual |
| Q28 | - |  |  | SI | Chequeo de antecedentes personales |
| Q29 | - |  |  | SI | Chequeo de antecedentes familiares |
| Q30 | - |  |  | SI | N° de gestaciones |
| Q31 | - |  |  | SI | N° de abortos no provocados |
| Q33 | - |  |  | SI | N° de partos |
| Q34 | - |  |  | SI | ¿Algún RN de peso inferior a 2.500 grs.? |
| Q35 | - |  |  | SI | ¿Alguna gesta de tres partos? |
| Q36 | - |  |  | SI | N° de partos vaginales |
| Q37 | - |  |  | SI | N° de partos por cesárea |
| Q38 | - |  |  | SI | N° de nacidos vivos |
| Q39 | - |  |  | SI | N° de mortinatos |
| Q40 | - |  |  | SI | N° de RN fallecido(s) a la 1era semana de vida |
| Q41 | - |  |  | SI | N° de RN fallecido(s) entre la 2da y 4ta semana de... |
| Q42 | - |  |  | SI | N° de hijos vivos actualmente |
| Q43 | - |  |  | SI | ¿Algún RN de peso superior a 4.000 grs.? |
| Q44 | - |  |  | SI | FUR (entregada por la paciente) |
| Q45 | - |  |  | SI | FUR (Operacional) |
| Q46 | - |  |  | SI | ¿Dudas en relación a la FUR? |
| Q47 | - |  |  | SI | Peso al ingreso |
| Q47ObsDR | - |  |  | SI | Peso al ingreso DR |
| Q48 | - |  |  | SI | Talla al Ingreso |
| Q48ObsDR | - |  |  | SI | Talla al Ingreso DR |
| Q49 | - |  |  | SI | Fecha probable de parto |
| Q50 | - |  |  | SI | Edad gestacional al ingreso |
| Q52 | - |  |  | SI | Grupo sanguíneo |
| Q53 | - |  |  | SI | Sensibilizada |
| Q55 | - |  |  | SI | Temperatura axilar (C°) |
| Q55ObsDR | - |  |  | SI | Temperatura axilar (C°) DR |
| Q56 | - |  |  | SI | Presión arterial sistólica (mmHg) |
| Q56ObsDR | - |  |  | SI | Presión arterial sistólica (mmHg) DR |
| Q57 | - |  |  | SI | Presión arterial diastólica (mmHg) |
| Q57ObsDR | - |  |  | SI | Presión arterial diastólica (mmHg) DR |
| Q58 | - |  |  | SI | Altura uterina (cms.) |
| Q58ObsDR | - |  |  | SI | Altura uterina (cms.) DR |
| Q59 | - |  |  | SI | Latidos cardiofetales feto 1 (lpm) |
| Q59ObsDR | - |  |  | SI | Latidos cardiofetales feto 1 (lpm) DR |
| Q60 | - |  |  | SI | Latidos cardiofetales feto 2 (lpm) |
| Q60ObsDR | - |  |  | SI | Latidos cardiofetales feto 2 (lpm) DR |
| Q61 | - |  |  | SI | Latidos cardiofetales feto 3 (lpm) |
| Q61ObsDR | - |  |  | SI | Latidos cardiofetales feto 3 (lpm) DR |
| Q62 | - |  |  | SI | Patología materna al ingreso |
| Q63 | - |  |  | SI | Destino |
| Q64 | - |  |  | SI | Nombre del profesional |
| Q65 | - |  |  | SI | Tipo de profesional |
| Q66 | - |  |  | SI | Alfabeta |
| Q67 | - |  |  | SI | N° de abortos provocados |
| Q68 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q69 | - |  |  | SI | Presión Arterial Media |
| Q70 | - |  |  | SI | Frecuencia Respiratoria |
| Q71 | - |  |  | SI | FIO2 % |
| Q72 | - |  |  | SI | Flujo de Oxígeno (Lt/Min) |
| Q73 | - |  |  | SI | Oxigenoterapia |
| Q74 | - |  |  | SI | Saturación O2 (%) |
| Q75 | - |  |  | SI | Hemoglucotest (mg/dl) |
| Q76 | - |  |  | SI | Temperatura Rectal (°C) |
| Q77 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q77ObsDR | - |  |  | SI | Frecuencia Cardíaca (lpm)  DR |
| Q78 | - |  |  | SI | Presión Arterial Media |
| Q78ObsDR | - |  |  | SI | Presión Arterial Media  DR |
| Q79 | - |  |  | SI | Frecuencia Respiratoria |
| Q79ObsDR | - |  |  | SI | Frecuencia Respiratoria  DR |
| Q80 | - |  |  | SI | FIO2 % |
| Q80ObsDR | - |  |  | SI | FIO2 %  DR |
| Q81 | - |  |  | SI | Flujo de Oxígeno (Lt/Min) |
| Q81ObsDR | - |  |  | SI | Flujo de Oxígeno (Lt/Min)  DR |
| Q82 | - |  |  | SI | Oxigenoterapia |
| Q82ObsDR | - |  |  | SI | Oxigenoterapia  DR |
| Q83 | - |  |  | SI | Saturación O2 (%) |
| Q83ObsDR | - |  |  | SI | Saturación O2 (%)  DR |
| Q84 | - |  |  | SI | Hemoglucotest (mg/dl) |
| Q84ObsDR | - |  |  | SI | Hemoglucotest (mg/dl)  DR |
| Q85 | - |  |  | SI | Temperatura Rectal (°C) |
| Q85ObsDR | - |  |  | SI | Temperatura Rectal (°C) DR |
| Q86 | - |  |  | SI | Anamnesis |
| Q87 | - |  |  | SI | Procedencia |
| Q88 | - |  |  | SI | Procedencia (otra) |
| Q89 | - |  |  | SI | Diagnósticos de Derivación |
| Q90 | - |  |  | SI | Otra Patología |
| Q91 | - |  |  | SI | Embarazo Planificado? |
| Q92 | - |  |  | SI | Sintomas Presentes |
| Q93 | - |  |  | SI | Otro Sintoma |
| Q94 | - |  |  | SI | Observaciones/Comentarios |
| Q95 | - |  |  | SI | Religión |
| Q96 | - |  |  | SI | Consumo de Alcohol |
| Q97 | - |  |  | SI | Tiempo de Consumo de Alcohol |
| Q98 | - |  |  | SI | Tabaquismo |
| Q99 | - |  |  | SI | Cigarrillos por día |
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