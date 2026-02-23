# questionnaire.QTCEARO

> Ingreso Prenatal Alto Riesgo Obstétrico

**Schema:** questionnaire
**Columnas:** 323
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Prenatal Alto Riesgo Obstétrico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre de la madre |
| Q02 | varchar |  |  | SI | RUT de la madre |
| Q03 | varchar |  |  | SI | Pasaporte de la madre |
| Q04 | varchar |  |  | SI | Dirección de la madre |
| Q05 | varchar |  |  | SI | Dirección de la madre (comuna) |
| Q06 | varchar |  |  | SI | Dirección de la madre (Otro) |
| Q07 | varchar |  |  | SI | Edad de la madre |
| Q08 | varchar |  |  | SI | Último curso realizado |
| Q09 | varchar |  |  | SI | Nivel educacional |
| Q10 | varchar |  |  | SI | Ocupación |
| Q100 | numeric |  |  | SI | Años de Consumo |
| Q101 | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q102 | varchar |  |  | SI | Consumo de Drogas |
| Q103 | varchar |  |  | SI | Otra Droga |
| Q104 | varchar |  |  | SI | Síntomas Presentes |
| Q105 | varchar |  |  | SI | Otro Síntoma |
| Q106 | varchar |  |  | SI | Observaciones/Comentarios |
| Q107 | varchar |  |  | SI | Estado General |
| Q108 | varchar |  |  | SI | Valoración del dolor |
| Q109 | varchar |  |  | SI | Estado Psíquico |
| Q109ObsDR | varchar |  | FK | SI | Estado Psíquico DR |
| Q11 | varchar |  |  | SI | Categoría ocupacional |
| Q110 | varchar |  |  | SI | Conciencia |
| Q110ObsDR | varchar |  | FK | SI | Conciencia DR |
| Q111 | varchar |  |  | SI | Piel |
| Q111ObsDR | varchar |  | FK | SI | Piel DR |
| Q112 | varchar |  |  | SI | Mucosas |
| Q112ObsDR | varchar |  | FK | SI | Mucosas DR |
| Q113 | varchar |  |  | SI | Cabeza-Cara |
| Q113ObsDR | varchar |  | FK | SI | Cabeza-Cara DR |
| Q114 | varchar |  |  | SI | Pupilas |
| Q114ObsDR | varchar |  | FK | SI | Pupilas DR |
| Q115 | varchar |  |  | SI | Conjuntivas |
| Q115ObsDR | varchar |  | FK | SI | Conjuntivas DR |
| Q116 | varchar |  |  | SI | Dentadura |
| Q116ObsDR | varchar |  | FK | SI | Dentadura DR |
| Q117 | varchar |  |  | SI | Lenguage |
| Q117ObsDR | varchar |  | FK | SI | Lenguage DR |
| Q118 | varchar |  |  | SI | Cuello |
| Q118ObsDR | varchar |  | FK | SI | Cuello DR |
| Q119 | varchar |  |  | SI | Vía Aérea |
| Q119ObsDR | varchar |  | FK | SI | Vía Aérea DR |
| Q12 | varchar |  |  | SI | Nombre del progenitor |
| Q120 | varchar |  |  | SI | Respiración |
| Q120ObsDR | varchar |  | FK | SI | Respiración DR |
| Q121 | varchar |  |  | SI | Tórax |
| Q121ObsDR | varchar |  | FK | SI | Tórax DR |
| Q122 | varchar |  |  | SI | Cardíaco |
| Q122ObsDR | varchar |  | FK | SI | Cardíaco DR |
| Q123 | varchar |  |  | SI | Ritmo Cardíaco |
| Q123ObsDR | varchar |  | FK | SI | Ritmo Cardíaco DR |
| Q124 | varchar |  |  | SI | Mamas |
| Q124ObsDR | varchar |  | FK | SI | Mamas DR |
| Q125 | varchar |  |  | SI | Pezones |
| Q125ObsDR | varchar |  | FK | SI | Pezones DR |
| Q126 | varchar |  |  | SI | Útero |
| Q126ObsDR | varchar |  | FK | SI | Útero DR |
| Q127 | varchar |  |  | SI | Abdomen |
| Q127ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q128 | varchar |  |  | SI | Extremidades Superiores |
| Q128ObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q129 | varchar |  |  | SI | Extremidades Inferiores |
| Q129ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q13 | varchar |  |  | SI | RUT / Pasaporte del progenitor |
| Q130 | varchar |  |  | SI | Edema |
| Q130ObsDR | varchar |  | FK | SI | Edema DR |
| Q131 | varchar |  |  | SI | Genito Urinario |
| Q131ObsDR | varchar |  | FK | SI | Genito Urinario DR |
| Q132 | varchar |  |  | SI | Ano |
| Q132ObsDR | varchar |  | FK | SI | Ano DR |
| Q133 | varchar |  |  | SI | Diuresis |
| Q133ObsDR | varchar |  | FK | SI | Diuresis DR |
| Q134 | varchar |  |  | SI | Deposiciones |
| Q134ObsDR | varchar |  | FK | SI | Deposiciones DR |
| Q135 | varchar |  |  | SI | Comentario (Estado) |
| Q136 | varchar |  |  | SI | Comentario (Conciencia) |
| Q137 | varchar |  |  | SI | Comentario (Piel) |
| Q138 | varchar |  |  | SI | Comentario (Mucosas) |
| Q139 | varchar |  |  | SI | Comentario (Cabeza) |
| Q14 | varchar |  |  | SI | Edad del progenitor |
| Q140 | varchar |  |  | SI | Comentario (Pupilas) |
| Q141 | varchar |  |  | SI | Comentario (Conjuntivas) |
| Q142 | varchar |  |  | SI | Comentario (Dentadura) |
| Q143 | varchar |  |  | SI | Comentario (Lenguage) |
| Q144 | varchar |  |  | SI | Comentario (Cuello) |
| Q145 | varchar |  |  | SI | Comentario (Via) |
| Q146 | varchar |  |  | SI | Comentario (Respiración) |
| Q147 | varchar |  |  | SI | Comentario (Toráx) |
| Q148 | varchar |  |  | SI | Comentario (Cardiaco) |
| Q149 | varchar |  |  | SI | Comentario (Ritmo) |
| Q15 | varchar |  |  | SI | Último curso realizado (progenitor) |
| Q150 | varchar |  |  | SI | Comentario (Mamas) |
| Q151 | varchar |  |  | SI | Comentario (Pezones) |
| Q152 | varchar |  |  | SI | Comentario (utero) |
| Q153 | varchar |  |  | SI | Comentario (Abdomen) |
| Q154 | varchar |  |  | SI | Comentario (ES) |
| Q155 | varchar |  |  | SI | Comentario (EI) |
| Q156 | varchar |  |  | SI | Comentario (Edema) |
| Q157 | varchar |  |  | SI | Comentario (GU) |
| Q158 | varchar |  |  | SI | Comentario (Ano) |
| Q159 | varchar |  |  | SI | Comentario (Diuresis) |
| Q16 | varchar |  |  | SI | Nivel educacional (progenitor) |
| Q160 | varchar |  |  | SI | Comentario (Deposiciones) |
| Q161 | varchar |  |  | SI | Comentarios Generales EO |
| Q162 | bit |  |  | SI | Resto del examen ginecológico realizado, sin alter... |
| Q163 | varchar |  |  | SI | Inspección CG |
| Q164 | varchar |  |  | SI | Tacto vaginal CG |
| Q165 | varchar |  |  | SI | Especuloscopía CG |
| Q166 | varchar |  |  | SI | Examen mamas CG |
| Q167 | varchar |  |  | SI | Inspección TA |
| Q168 | varchar |  |  | SI | Tacto vaginal TA |
| Q169 | varchar |  |  | SI | Especuloscopia TA |
| Q17 | varchar |  |  | SI | Ocupación (progenitor) |
| Q170 | varchar |  |  | SI | Exames mamas TA |
| Q172 | varchar |  |  | SI | Descripción |
| Q173 | varchar |  |  | SI | Tacto vaginal CG2 |
| Q174 | varchar |  |  | SI | Tacto Vaginal CG 3 |
| Q175 | varchar |  |  | SI | Grafico IMC |
| Q176 | varchar |  |  | SI | ¿Embarazo Deseado? |
| Q177 | varchar |  |  | SI | Religión |
| Q178 | varchar |  |  | SI | Religión |
| Q179 | numeric |  |  | SI | Cigarrilos por día |
| Q18 | varchar |  |  | SI | Categoría ocupacional (progenitor) |
| Q180 | numeric |  |  | SI | Años de Consumo |
| Q181 | varchar |  |  | SI | Otra Patología |
| Q182 | varchar |  |  | SI | Escala del Dolor |
| Q182ObsDR | varchar |  | FK | SI | Escala del Dolor DR |
| Q183 | varchar |  |  | SI | Razones para no Evaluar Dolor |
| Q184 | varchar |  |  | SI | Especifique |
| Q185 | varchar |  |  | SI | Ubicación del Dolor |
| Q186 | bit |  |  | SI | Labios mayores y menores de tamaño y aspecto norma... |
| Q187 | bit |  |  | SI | Clitoris de tamaño y aspecto normal |
| Q188 | bit |  |  | SI | Glándulas de Bartholino normales |
| Q189 | bit |  |  | SI | Paredes vaginales elásticas. Mucosa vaginal normal... |
| Q19 | varchar |  |  | SI | Dirección del progenitor (Calle, N°, comuna) |
| Q190 | bit |  |  | SI | Saco de Douglas libre |
| Q191 | bit |  |  | SI | Cuello uterino de consistencia y tamaño normal	 |
| Q192 | bit |  |  | SI | Útero en anteroversión, de tamaño y consistencia n... |
| Q193 | bit |  |  | SI | Flujo vaginal normal |
| Q194 | bit |  |  | SI | Anexos libres e indoloros |
| Q195 | bit |  |  | SI | Parametrios normales |
| Q196 | bit |  |  | SI | Vagina de elasticidad conservada |
| Q197 | bit |  |  | SI | Cuello central de coloración normal, sin lesiones ... |
| Q198 | bit |  |  | SI | Mamas de tamaño y desarrollo normal, simétricas |
| Q199 | bit |  |  | SI | No se palpan masas ni adenopatías locales |
| Q20 | varchar |  |  | SI | Pueblo originario |
| Q200 | bit |  |  | SI | Pezones sin lesiones ni secreción anormal |
| Q201 | varchar |  |  | SI | Movimientos Fetales  |
| Q201ObsDR | varchar |  | FK | SI | Movimientos Fetales  DR |
| Q202 | varchar |  |  | SI | Presentación  |
| Q202ObsDR | varchar |  | FK | SI | Presentación  DR |
| Q203 | varchar |  |  | SI | Dorso Fetal |
| Q203ObsDR | varchar |  | FK | SI | Dorso Fetal DR |
| Q204 | varchar |  |  | SI | Plano de Hodge  |
| Q204ObsDR | varchar |  | FK | SI | Plano de Hodge  DR |
| Q205 | varchar |  |  | SI | Altura Uterina (cms)  |
| Q205ObsDR | varchar |  | FK | SI | Altura Uterina (cms)  DR |
| Q206 | varchar |  |  | SI | Tono  Uterino |
| Q206ObsDR | varchar |  | FK | SI | Tono  Uterino DR |
| Q207 | varchar |  |  | SI | Dinámica Uterina  |
| Q207ObsDR | varchar |  | FK | SI | Dinámica Uterina  DR |
| Q208 | varchar |  |  | SI | Contracciones (Cada 10 min) |
| Q208ObsDR | varchar |  | FK | SI | Contracciones (Cada 10 min) DR |
| Q209 | varchar |  |  | SI | Desaceleraciones  |
| Q209ObsDR | varchar |  | FK | SI | Desaceleraciones  DR |
| Q21 | varchar |  |  | SI | Grupo cultural |
| Q210 | varchar |  |  | SI | Líquido Amniótico  |
| Q210ObsDR | varchar |  | FK | SI | Líquido Amniótico  DR |
| Q211 | varchar |  |  | SI | Flujo Vaginal  |
| Q211ObsDR | varchar |  | FK | SI | Flujo Vaginal  DR |
| Q212 | varchar |  |  | SI | Membranas  |
| Q212ObsDR | varchar |  | FK | SI | Membranas  DR |
| Q213 | varchar |  |  | SI | Consistencia Cuello |
| Q213ObsDR | varchar |  | FK | SI | Consistencia Cuello DR |
| Q214 | varchar |  |  | SI | Posición  |
| Q214ObsDR | varchar |  | FK | SI | Posición  DR |
| Q215 | varchar |  |  | SI | Borramiento |
| Q215ObsDR | varchar |  | FK | SI | Borramiento DR |
| Q216 | varchar |  |  | SI | Dilatación Cervical |
| Q216ObsDR | varchar |  | FK | SI | Dilatación Cervical DR |
| Q217 | varchar |  |  | SI | LCF Feto 1 (lpm) |
| Q217ObsDR | varchar |  | FK | SI | LCF Feto 1 (lpm) DR |
| Q218 | varchar |  |  | SI |  LCF Feto 2 (lpm) |
| Q218ObsDR | varchar |  | FK | SI |  LCF Feto 2 (lpm) DR |
| Q219 | varchar |  |  | SI | LCF Feto 3 (lpm) |
| Q219ObsDR | varchar |  | FK | SI | LCF Feto 3 (lpm) DR |
| Q22 | date |  |  | SI | Fecha de término del último embarazo  |
| Q220 | varchar |  |  | SI | Comentarios Examen Obstétrico |
| Q221 | numeric |  |  | SI | N° de Hijos Fallecidos Total |
| Q222 | varchar |  |  | SI | Plan de Ingreso |
| Q23 | date |  |  | SI | Fecha de inicio del control prenatal |
| Q24 | varchar |  |  | SI | Método anticonceptivo |
| Q25 | varchar |  |  | SI | ¿Embarazo planificado? |
| Q26 | varchar |  |  | SI | Causa de la última cesárea (si procede) |
| Q27 | numeric |  |  | SI | Peso habitual |
| Q28 | varchar |  |  | SI | Chequeo de antecedentes personales |
| Q29 | varchar |  |  | SI | Chequeo de antecedentes familiares |
| Q30 | varchar |  |  | SI | N° de gestaciones |
| Q31 | varchar |  |  | SI | N° de abortos no provocados |
| Q33 | varchar |  |  | SI | N° de partos |
| Q34 | varchar |  |  | SI | ¿Algún RN de peso inferior a 2.500 grs.? |
| Q35 | varchar |  |  | SI | ¿Alguna gesta de tres partos? |
| Q36 | varchar |  |  | SI | N° de partos vaginales |
| Q37 | numeric |  |  | SI | N° de partos por cesárea |
| Q38 | varchar |  |  | SI | N° de nacidos vivos |
| Q39 | varchar |  |  | SI | N° de mortinatos |
| Q40 | varchar |  |  | SI | N° de RN fallecido(s) a la 1era semana de vida |
| Q41 | varchar |  |  | SI | N° de RN fallecido(s) entre la 2da y 4ta semana de... |
| Q42 | varchar |  |  | SI | N° de hijos vivos actualmente |
| Q43 | varchar |  |  | SI | ¿Algún RN de peso superior a 4.000 grs.? |
| Q44 | varchar |  |  | SI | FUR (entregada por la paciente) |
| Q45 | varchar |  |  | SI | FUR (Operacional) |
| Q46 | varchar |  |  | SI | ¿Dudas en relación a la FUR? |
| Q47 | varchar |  |  | SI | Peso al ingreso |
| Q47ObsDR | varchar |  | FK | SI | Peso al ingreso DR |
| Q48 | varchar |  |  | SI | Talla al Ingreso |
| Q48ObsDR | varchar |  | FK | SI | Talla al Ingreso DR |
| Q49 | varchar |  |  | SI | Fecha probable de parto |
| Q50 | numeric |  |  | SI | Edad gestacional al ingreso |
| Q52 | varchar |  |  | SI | Grupo sanguíneo |
| Q53 | varchar |  |  | SI | Sensibilizada |
| Q55 | varchar |  |  | SI | Temperatura axilar (C°) |
| Q55ObsDR | varchar |  | FK | SI | Temperatura axilar (C°) DR |
| Q56 | varchar |  |  | SI | Presión arterial sistólica (mmHg) |
| Q56ObsDR | varchar |  | FK | SI | Presión arterial sistólica (mmHg) DR |
| Q57 | varchar |  |  | SI | Presión arterial diastólica (mmHg) |
| Q57ObsDR | varchar |  | FK | SI | Presión arterial diastólica (mmHg) DR |
| Q58 | varchar |  |  | SI | Altura uterina (cms.) |
| Q58ObsDR | varchar |  | FK | SI | Altura uterina (cms.) DR |
| Q59 | varchar |  |  | SI | Latidos cardiofetales feto 1 (lpm) |
| Q59ObsDR | varchar |  | FK | SI | Latidos cardiofetales feto 1 (lpm) DR |
| Q60 | varchar |  |  | SI | Latidos cardiofetales feto 2 (lpm) |
| Q60ObsDR | varchar |  | FK | SI | Latidos cardiofetales feto 2 (lpm) DR |
| Q61 | varchar |  |  | SI | Latidos cardiofetales feto 3 (lpm) |
| Q61ObsDR | varchar |  | FK | SI | Latidos cardiofetales feto 3 (lpm) DR |
| Q62 | varchar |  |  | SI | Patología materna al ingreso |
| Q63 | varchar |  |  | SI | Destino |
| Q64 | varchar |  |  | SI | Nombre del profesional |
| Q65 | varchar |  |  | SI | Tipo de profesional |
| Q66 | varchar |  |  | SI | Alfabeta |
| Q67 | varchar |  |  | SI | N° de abortos provocados |
| Q68 | numeric |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q69 | varchar |  |  | SI | Presión Arterial Media |
| Q70 | numeric |  |  | SI | Frecuencia Respiratoria |
| Q71 | numeric |  |  | SI | FIO2 % |
| Q72 | numeric |  |  | SI | Flujo de Oxígeno (Lt/Min) |
| Q73 | varchar |  |  | SI | Oxigenoterapia  |
| Q74 | numeric |  |  | SI | Saturación O2 (%) |
| Q75 | varchar |  |  | SI | Hemoglucotest (mg/dl) |
| Q76 | numeric |  |  | SI | Temperatura Rectal (°C) |
| Q77 | varchar |  |  | SI | Frecuencia Cardíaca (lpm)  |
| Q77ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca (lpm)  DR |
| Q78 | varchar |  |  | SI | Presión Arterial Media  |
| Q78ObsDR | varchar |  | FK | SI | Presión Arterial Media  DR |
| Q79 | varchar |  |  | SI | Frecuencia Respiratoria  |
| Q79ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria  DR |
| Q80 | varchar |  |  | SI | FIO2 %  |
| Q80ObsDR | varchar |  | FK | SI | FIO2 %  DR |
| Q81 | varchar |  |  | SI | Flujo de Oxígeno (Lt/Min)  |
| Q81ObsDR | varchar |  | FK | SI | Flujo de Oxígeno (Lt/Min)  DR |
| Q82 | varchar |  |  | SI | Oxigenoterapia  |
| Q82ObsDR | varchar |  | FK | SI | Oxigenoterapia  DR |
| Q83 | varchar |  |  | SI | Saturación O2 (%)  |
| Q83ObsDR | varchar |  | FK | SI | Saturación O2 (%)  DR |
| Q84 | varchar |  |  | SI | Hemoglucotest (mg/dl)  |
| Q84ObsDR | varchar |  | FK | SI | Hemoglucotest (mg/dl)  DR |
| Q85 | varchar |  |  | SI | Temperatura Rectal (°C) |
| Q85ObsDR | varchar |  | FK | SI | Temperatura Rectal (°C) DR |
| Q86 | varchar |  |  | SI | Anamnesis |
| Q87 | varchar |  |  | SI | Procedencia |
| Q88 | varchar |  |  | SI | Procedencia (otra) |
| Q89 | varchar |  |  | SI | Diagnósticos de Derivación |
| Q90 | varchar |  |  | SI | Otra Patología |
| Q91 | varchar |  |  | SI | Embarazo Planificado? |
| Q92 | varchar |  |  | SI | Sintomas Presentes |
| Q93 | varchar |  |  | SI | Otro Sintoma |
| Q94 | varchar |  |  | SI | Observaciones/Comentarios |
| Q95 | varchar |  |  | SI | Religión |
| Q96 | varchar |  |  | SI | Consumo de Alcohol |
| Q97 | varchar |  |  | SI | Tiempo de Consumo de Alcohol |
| Q98 | varchar |  |  | SI | Tabaquismo |
| Q99 | numeric |  |  | SI | Cigarrillos por día |
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