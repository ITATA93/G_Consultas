# questionnaire.QCLXXEMPSFU

> Examen de Medicina Preventiva - Salud Funcionaria

**Schema:** questionnaire
**Columnas:** 182
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen de Medicina Preventiva - Salud Funcionaria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Antecedentes Laborales |
| Q02 | varchar |  |  | SI | Planta |
| Q03 | varchar |  |  | SI | Unidad |
| Q04 | varchar |  |  | SI | Cargo / Profesión |
| Q05 | numeric |  |  | SI | Antigüedad en la Institución (Año de entrada) |
| Q06 | numeric |  |  | SI | Antigüedad en el cargo Actual (Año de entrada) |
| Q07 | varchar |  |  | SI | Horario laboral |
| Q08 | varchar |  |  | SI | Horas / Turnos Extra |
| Q09 | varchar |  |  | SI | ¿Tiene otro trabajo? |
| Q10 | varchar |  |  | SI | Calidad Jurídica |
| Q100 | varchar |  |  | SI | Formaldehído |
| Q101 | varchar |  |  | SI | Citostáticos |
| Q102 | varchar |  |  | SI | Xilol o xileno |
| Q103 | varchar |  |  | SI | Biológicos |
| Q104 | varchar |  |  | SI | Referir a Salud Ocupacional: para educación o ingr... |
| Q105 | varchar |  |  | SI | n. Vacunación anti Hepatitis B (sólo expuestos a r... |
| Q106 | varchar |  |  | SI | ¿Tiene administradas las 3 dosis de vacuna anti He... |
| Q107 | varchar |  |  | SI | ¿Tiene comprobante? |
| Q108 | varchar |  |  | SI | ¿Cuál? |
| Q109 | varchar |  |  | SI | Verificar en registro local / Registrar en RNI / I... |
| Q11 | varchar |  |  | SI | Antecedentes de Salud |
| Q110 | varchar |  |  | SI | ñ. Vacunación anti Influenza |
| Q111 | varchar |  |  | SI | ¿Recibió la última vacuna anti Influenza? |
| Q112 | varchar |  |  | SI | Ante respuesta negativa, explorar motivos y educar |
| Q113 | varchar |  |  | SI | o. Alimentación |
| Q114 | varchar |  |  | SI | ¿Cuántas comidas realiza a diario? (excepto colaci... |
| Q115 | varchar |  |  | SI | ¿Se salta comidas o hay días que no come? |
| Q116 | varchar |  |  | SI | ¿Considera que su alimentación es saludable? |
| Q117 | varchar |  |  | SI | Consejería alimentación saludable |
| Q118 | varchar |  |  | SI | p. Actividad Física / Sedentarismo |
| Q119 | varchar |  |  | SI | ¿Realiza actividad física regularmente? (≥ 150 min... |
| Q12 | varchar |  |  | SI | a. Antecedentes Personales de Enfermedad Crónica N... |
| Q120 | varchar |  |  | SI | ¿Realiza pausas activas o ejercicios compensatorio... |
| Q121 | varchar |  |  | SI | Consejería sobre actividad física en el trabajo y ... |
| Q122 | varchar |  |  | SI | q. Trastornos del Sueño |
| Q123 | varchar |  |  | SI | ¿Presenta algún problema del sueño? |
| Q124 | varchar |  |  | SI | Tipo |
| Q125 | varchar |  |  | SI | Otro(s) |
| Q126 | varchar |  |  | SI | ¿Cuántas horas duerme diariamente (en promedio)? |
| Q127 | varchar |  |  | SI | Consejería sobre higiene del sueño |
| Q128 | varchar |  |  | SI | r. Consumo Riesgoso de Sustancias Adictivas (aplic... |
| Q129 | varchar |  |  | SI | ¿Consiente realizar ASSIST? |
| Q13 | varchar |  |  | SI | ¿Tiene usted una enfermedad crónica diagnosticada? |
| Q130 | varchar |  |  | SI | Realizar Cuestionario ASSIST V3.0 (Chile) (TCEASSI... |
| Q131 | varchar |  |  | SI | Derivación asistida a programa de salud mental (co... |
| Q132 | varchar |  |  | SI | s. Bienestar psicológico (GHQ12 adaptado) |
| Q133 | varchar |  |  | SI | Realizar Cuestionario de Salud de Goldberg (TCEGOL... |
| Q134 | varchar |  |  | SI | Observaciones / Hallazgos |
| Q135 | varchar |  |  | SI | Indicaciones / Derivaciones |
| Q136 | varchar |  |  | SI | Resultado Cuestionario de Salud de Goldberg |
| Q14 | varchar |  |  | SI | ¿Cuál(es)? |
| Q15 | varchar |  |  | SI | ¿Está en control y tratamiento actualmente? |
| Q16 | varchar |  |  | SI | ¿Dónde? |
| Q17 | varchar |  |  | SI | b. Antecedentes ECNTs - familiares directos: padre... |
| Q18 | varchar |  |  | SI | Hipertensión Arterial |
| Q19 | varchar |  |  | SI | Enfermedad Renal |
| Q20 | varchar |  |  | SI | Diabetes Mellitus |
| Q21 | varchar |  |  | SI | Cáncer |
| Q22 | varchar |  |  | SI | ¿Cuál(es)? |
| Q23 | varchar |  |  | SI | Dislipidemia |
| Q24 | varchar |  |  | SI | Evento Cardiovascular |
| Q25 | varchar |  |  | SI | ¿Cuál(es)? |
| Q26 | varchar |  |  | SI | c. Malnutrición por exceso |
| Q27 | varchar |  |  | SI | Peso (Kg) |
| Q27ObsDR | varchar |  | FK | SI | Peso (Kg) DR |
| Q28 | varchar |  |  | SI | Talla (cm) |
| Q28ObsDR | varchar |  | FK | SI | Talla (cm) DR |
| Q29 | varchar |  |  | SI | IMC (Kg/m2) |
| Q30 | varchar |  |  | SI | Circunferencia cintura (cm) |
| Q30ObsDR | varchar |  | FK | SI | Circunferencia cintura (cm) DR |
| Q31 | varchar |  |  | SI | Sobrepeso (25-29,9) |
| Q32 | varchar |  |  | SI | Consejería EVS |
| Q33 | varchar |  |  | SI | Obesidad (≥30,0) |
| Q34 | varchar |  |  | SI | Consejería EVS/Referir a Nutricionista |
| Q35 | varchar |  |  | SI | Mujer ≥ 80 cm |
| Q36 | varchar |  |  | SI | Hombre ≥ 95 cm |
| Q37 | varchar |  |  | SI | Consejería EVS |
| Q38 | varchar |  |  | SI | d. Hipertensión arterial |
| Q39 | varchar |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q39ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica (mmHg) DR |
| Q40 | varchar |  |  | SI | PAS ≥ 140 mmHg |
| Q41 | varchar |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q41ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica (mmHg) DR |
| Q42 | varchar |  |  | SI | PAD ≥ 90 mmHg |
| Q43 | varchar |  |  | SI | Indicar control seriado de presión arterial / Refe... |
| Q44 | varchar |  |  | SI | e. Dislipidemia |
| Q45 | numeric |  |  | SI | Colesterol total (CT) (mg/dl) |
| Q46 | varchar |  |  | SI | CT ≥ 200 mg/dl |
| Q47 | varchar |  |  | SI | Consejería EVS/Referir a Nutricionista |
| Q48 | varchar |  |  | SI | CT ≥ 240 mg/dl |
| Q49 | varchar |  |  | SI | Referir a médico y nutricionista |
| Q50 | numeric |  |  | SI | Colesterol HDL (mg/dl) |
| Q51 | varchar |  |  | SI | Mujer&nbsp;HDL ≤ 50 mg/dl |
| Q52 | varchar |  |  | SI | Hombre&nbsp;HDL ≤ 40 mg/dl |
| Q53 | numeric |  |  | SI | Colesterol LDL (mg/dl) |
| Q54 | varchar |  |  | SI | LDL ≥ 130 mg/dl |
| Q55 | numeric |  |  | SI | Triglicéridos (TG) (mg/dl) |
| Q56 | varchar |  |  | SI | TG&nbsp;150 - 199 mg/dl |
| Q57 | varchar |  |  | SI | Consejería EVS / Referir a Nutricionista |
| Q58 | varchar |  |  | SI | TG&nbsp;≥ 200 mg/dl |
| Q59 | varchar |  |  | SI | Referir a médico y nutricionista |
| Q60 | varchar |  |  | SI | f. Diabetes Mellitus |
| Q61 | numeric |  |  | SI | Glicemia en ayunas* |
| Q62 | varchar |  |  | SI | *Glicemia &gt; 100 mg/dl, siempre referir a nutric... |
| Q63 | varchar |  |  | SI | Valor 100 - 125 mg/dl |
| Q64 | varchar |  |  | SI | Solicitar PTGO / Referir a confirmación diagnóstic... |
| Q65 | varchar |  |  | SI | Valor ≥ 126 mg/dl |
| Q66 | varchar |  |  | SI | Solicitar segunda glicemia en ayunas / Referir a c... |
| Q67 | varchar |  |  | SI | g. VIH y Sífilis |
| Q68 | varchar |  |  | SI | ¿Consiente realizarse exámenes? |
| Q69 | varchar |  |  | SI | Anticuerpos VIH |
| Q70 | varchar |  |  | SI | VDRL |
| Q71 | varchar |  |  | SI | Resultado alterado, derivar de acuerdo a normativa... |
| Q72 | varchar |  |  | SI | h. Tuberculosis |
| Q73 | varchar |  |  | SI | ¿Tiene tos productiva actualmente? |
| Q74 | varchar |  |  | SI | Resultado baciloscopía (BK) |
| Q75 | varchar |  |  | SI | Resultado BK positivo, derivar de acuerdo a normat... |
| Q76 | varchar |  |  | SI | i. Cáncer de Mamas |
| Q77 | varchar |  |  | SI | Mujeres &lt; 40 años&nbsp;¿presenta factores de ri... |
| Q78 | varchar |  |  | SI | Derivar con médico o matrona |
| Q79 | varchar |  |  | SI | Mujeres ≥ 40 años&nbsp;¿Mamografía vigente (3 años... |
| Q80 | varchar |  |  | SI | Solicitar mamografía si corresponde |
| Q81 | varchar |  |  | SI | Resultado de examen |
| Q82 | varchar |  |  | SI | Derivación a médico o matrona |
| Q83 | varchar |  |  | SI | j. Cáncer Cervicouterino (mujeres de 21 a 64 años)... |
| Q84 | date |  |  | SI | Fecha último PAP |
| Q85 | varchar |  |  | SI | ¿PAP vigente? |
| Q86 | varchar |  |  | SI | Resultado de PAP |
| Q87 | varchar |  |  | SI | Derivación a médico o matrona |
| Q88 | varchar |  |  | SI | k. Cáncer Colorrectal (mujeres y hombres desde los... |
| Q89 | varchar |  |  | SI | Sangre oculta en deposiciones |
| Q90 | varchar |  |  | SI | Resultado positivo, derivar con médico |
| Q91 | varchar |  |  | SI | l. Dolencias Musculoesqueléticas |
| Q92 | varchar |  |  | SI | ¿Ha presentado dolencias reiteradas o continuas, e... |
| Q93 | varchar |  |  | SI | ¿En qué zona(s) del cuerpo? |
| Q94 | varchar |  |  | SI | ¿Ha consultado con médico u otro profesional por e... |
| Q95 | varchar |  |  | SI | Referir con médico si procede |
| Q96 | varchar |  |  | SI | m. Exposición a Riesgos Ocupacionales Específicos |
| Q97 | varchar |  |  | SI | ¿Está usted expuesto a alguno de los siguientes ri... |
| Q98 | varchar |  |  | SI | Radiaciones ionizantes |
| Q99 | varchar |  |  | SI | Óxido de etileno |
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