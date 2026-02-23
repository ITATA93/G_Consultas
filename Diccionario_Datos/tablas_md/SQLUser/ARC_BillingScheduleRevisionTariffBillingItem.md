# SQLUser.ARC_BillingScheduleRevisionTariffBillingItem

**Schema:** SQLUser
**Columnas:** 196
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRTBI_ParRef | varchar | PK |  | NO | Parent BillingScheduleRevisionTariff |
| ARCBSCRTBI_BillingItem_DR | bigint |  | FK | NO | Billing Item |
| ARCBSCRTBI_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRTBI_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRTBI_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRTBI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRTBI_Discount | double |  |  | SI | Discount |
| ARCBSCRTBI_EffectiveDate | date |  |  | SI | Effective date for the record |
| ARCBSCRTBI_IncludeServiceTax | varchar |  |  | SI | Including Service Tax |
| ARCBSCRTBI_Price | double |  |  | SI | Price |
| ARCBSCRTBI_RowID | varchar |  |  | NO | - |
| ARCBSCRTBI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRTBI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRTBI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antecedentes Laborales |
| Q02 | - |  |  | SI | Planta |
| Q03 | - |  |  | SI | Unidad |
| Q04 | - |  |  | SI | Cargo / Profesión |
| Q05 | - |  |  | SI | Antigüedad en la Institución (Año de entrada) |
| Q06 | - |  |  | SI | Antigüedad en el cargo Actual (Año de entrada) |
| Q07 | - |  |  | SI | Horario laboral |
| Q08 | - |  |  | SI | Horas / Turnos Extra |
| Q09 | - |  |  | SI | ¿Tiene otro trabajo? |
| Q10 | - |  |  | SI | Calidad Jurídica |
| Q100 | - |  |  | SI | Formaldehído |
| Q101 | - |  |  | SI | Citostáticos |
| Q102 | - |  |  | SI | Xilol o xileno |
| Q103 | - |  |  | SI | Biológicos |
| Q104 | - |  |  | SI | Referir a Salud Ocupacional: para educación o ingr... |
| Q105 | - |  |  | SI | n. Vacunación anti Hepatitis B (sólo expuestos a r... |
| Q106 | - |  |  | SI | ¿Tiene administradas las 3 dosis de vacuna anti He... |
| Q107 | - |  |  | SI | ¿Tiene comprobante? |
| Q108 | - |  |  | SI | ¿Cuál? |
| Q109 | - |  |  | SI | Verificar en registro local / Registrar en RNI / I... |
| Q11 | - |  |  | SI | Antecedentes de Salud |
| Q110 | - |  |  | SI | ñ. Vacunación anti Influenza |
| Q111 | - |  |  | SI | ¿Recibió la última vacuna anti Influenza? |
| Q112 | - |  |  | SI | Ante respuesta negativa, explorar motivos y educar |
| Q113 | - |  |  | SI | o. Alimentación |
| Q114 | - |  |  | SI | ¿Cuántas comidas realiza a diario? (excepto colaci... |
| Q115 | - |  |  | SI | ¿Se salta comidas o hay días que no come? |
| Q116 | - |  |  | SI | ¿Considera que su alimentación es saludable? |
| Q117 | - |  |  | SI | Consejería alimentación saludable |
| Q118 | - |  |  | SI | p. Actividad Física / Sedentarismo |
| Q119 | - |  |  | SI | ¿Realiza actividad física regularmente? (≥ 150 min... |
| Q12 | - |  |  | SI | a. Antecedentes Personales de Enfermedad Crónica N... |
| Q120 | - |  |  | SI | ¿Realiza pausas activas o ejercicios compensatorio... |
| Q121 | - |  |  | SI | Consejería sobre actividad física en el trabajo y ... |
| Q122 | - |  |  | SI | q. Trastornos del Sueño |
| Q123 | - |  |  | SI | ¿Presenta algún problema del sueño? |
| Q124 | - |  |  | SI | Tipo |
| Q125 | - |  |  | SI | Otro(s) |
| Q126 | - |  |  | SI | ¿Cuántas horas duerme diariamente (en promedio)? |
| Q127 | - |  |  | SI | Consejería sobre higiene del sueño |
| Q128 | - |  |  | SI | r. Consumo Riesgoso de Sustancias Adictivas (aplic... |
| Q129 | - |  |  | SI | ¿Consiente realizar ASSIST? |
| Q13 | - |  |  | SI | ¿Tiene usted una enfermedad crónica diagnosticada? |
| Q130 | - |  |  | SI | Realizar Cuestionario ASSIST V3.0 (Chile) (TCEASSI... |
| Q131 | - |  |  | SI | Derivación asistida a programa de salud mental (co... |
| Q132 | - |  |  | SI | s. Bienestar psicológico (GHQ12 adaptado) |
| Q133 | - |  |  | SI | Realizar Cuestionario de Salud de Goldberg (TCEGOL... |
| Q134 | - |  |  | SI | Observaciones / Hallazgos |
| Q135 | - |  |  | SI | Indicaciones / Derivaciones |
| Q136 | - |  |  | SI | Resultado Cuestionario de Salud de Goldberg |
| Q14 | - |  |  | SI | ¿Cuál(es)? |
| Q15 | - |  |  | SI | ¿Está en control y tratamiento actualmente? |
| Q16 | - |  |  | SI | ¿Dónde? |
| Q17 | - |  |  | SI | b. Antecedentes ECNTs - familiares directos: padre... |
| Q18 | - |  |  | SI | Hipertensión Arterial |
| Q19 | - |  |  | SI | Enfermedad Renal |
| Q20 | - |  |  | SI | Diabetes Mellitus |
| Q21 | - |  |  | SI | Cáncer |
| Q22 | - |  |  | SI | ¿Cuál(es)? |
| Q23 | - |  |  | SI | Dislipidemia |
| Q24 | - |  |  | SI | Evento Cardiovascular |
| Q25 | - |  |  | SI | ¿Cuál(es)? |
| Q26 | - |  |  | SI | c. Malnutrición por exceso |
| Q27 | - |  |  | SI | Peso (Kg) |
| Q27ObsDR | - |  |  | SI | Peso (Kg) DR |
| Q28 | - |  |  | SI | Talla (cm) |
| Q28ObsDR | - |  |  | SI | Talla (cm) DR |
| Q29 | - |  |  | SI | IMC (Kg/m2) |
| Q30 | - |  |  | SI | Circunferencia cintura (cm) |
| Q30ObsDR | - |  |  | SI | Circunferencia cintura (cm) DR |
| Q31 | - |  |  | SI | Sobrepeso (25-29,9) |
| Q32 | - |  |  | SI | Consejería EVS |
| Q33 | - |  |  | SI | Obesidad (≥30,0) |
| Q34 | - |  |  | SI | Consejería EVS/Referir a Nutricionista |
| Q35 | - |  |  | SI | Mujer ≥ 80 cm |
| Q36 | - |  |  | SI | Hombre ≥ 95 cm |
| Q37 | - |  |  | SI | Consejería EVS |
| Q38 | - |  |  | SI | d. Hipertensión arterial |
| Q39 | - |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q39ObsDR | - |  |  | SI | Presión Arterial Sistólica (mmHg) DR |
| Q40 | - |  |  | SI | PAS ≥ 140 mmHg |
| Q41 | - |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q41ObsDR | - |  |  | SI | Presión Arterial Diastólica (mmHg) DR |
| Q42 | - |  |  | SI | PAD ≥ 90 mmHg |
| Q43 | - |  |  | SI | Indicar control seriado de presión arterial / Refe... |
| Q44 | - |  |  | SI | e. Dislipidemia |
| Q45 | - |  |  | SI | Colesterol total (CT) (mg/dl) |
| Q46 | - |  |  | SI | CT ≥ 200 mg/dl |
| Q47 | - |  |  | SI | Consejería EVS/Referir a Nutricionista |
| Q48 | - |  |  | SI | CT ≥ 240 mg/dl |
| Q49 | - |  |  | SI | Referir a médico y nutricionista |
| Q50 | - |  |  | SI | Colesterol HDL (mg/dl) |
| Q51 | - |  |  | SI | Mujer&nbsp |
| Q52 | - |  |  | SI | Hombre&nbsp |
| Q53 | - |  |  | SI | Colesterol LDL (mg/dl) |
| Q54 | - |  |  | SI | LDL ≥ 130 mg/dl |
| Q55 | - |  |  | SI | Triglicéridos (TG) (mg/dl) |
| Q56 | - |  |  | SI | TG&nbsp |
| Q57 | - |  |  | SI | Consejería EVS / Referir a Nutricionista |
| Q58 | - |  |  | SI | TG&nbsp |
| Q59 | - |  |  | SI | Referir a médico y nutricionista |
| Q60 | - |  |  | SI | f. Diabetes Mellitus |
| Q61 | - |  |  | SI | Glicemia en ayunas* |
| Q62 | - |  |  | SI | *Glicemia &gt |
| Q63 | - |  |  | SI | Valor 100 - 125 mg/dl |
| Q64 | - |  |  | SI | Solicitar PTGO / Referir a confirmación diagnóstic... |
| Q65 | - |  |  | SI | Valor ≥ 126 mg/dl |
| Q66 | - |  |  | SI | Solicitar segunda glicemia en ayunas / Referir a c... |
| Q67 | - |  |  | SI | g. VIH y Sífilis |
| Q68 | - |  |  | SI | ¿Consiente realizarse exámenes? |
| Q69 | - |  |  | SI | Anticuerpos VIH |
| Q70 | - |  |  | SI | VDRL |
| Q71 | - |  |  | SI | Resultado alterado, derivar de acuerdo a normativa... |
| Q72 | - |  |  | SI | h. Tuberculosis |
| Q73 | - |  |  | SI | ¿Tiene tos productiva actualmente? |
| Q74 | - |  |  | SI | Resultado baciloscopía (BK) |
| Q75 | - |  |  | SI | Resultado BK positivo, derivar de acuerdo a normat... |
| Q76 | - |  |  | SI | i. Cáncer de Mamas |
| Q77 | - |  |  | SI | Mujeres &lt |
| Q78 | - |  |  | SI | Derivar con médico o matrona |
| Q79 | - |  |  | SI | Mujeres ≥ 40 años&nbsp |
| Q80 | - |  |  | SI | Solicitar mamografía si corresponde |
| Q81 | - |  |  | SI | Resultado de examen |
| Q82 | - |  |  | SI | Derivación a médico o matrona |
| Q83 | - |  |  | SI | j. Cáncer Cervicouterino (mujeres de 21 a 64 años)... |
| Q84 | - |  |  | SI | Fecha último PAP |
| Q85 | - |  |  | SI | ¿PAP vigente? |
| Q86 | - |  |  | SI | Resultado de PAP |
| Q87 | - |  |  | SI | Derivación a médico o matrona |
| Q88 | - |  |  | SI | k. Cáncer Colorrectal (mujeres y hombres desde los... |
| Q89 | - |  |  | SI | Sangre oculta en deposiciones |
| Q90 | - |  |  | SI | Resultado positivo, derivar con médico |
| Q91 | - |  |  | SI | l. Dolencias Musculoesqueléticas |
| Q92 | - |  |  | SI | ¿Ha presentado dolencias reiteradas o continuas, e... |
| Q93 | - |  |  | SI | ¿En qué zona(s) del cuerpo? |
| Q94 | - |  |  | SI | ¿Ha consultado con médico u otro profesional por e... |
| Q95 | - |  |  | SI | Referir con médico si procede |
| Q96 | - |  |  | SI | m. Exposición a Riesgos Ocupacionales Específicos |
| Q97 | - |  |  | SI | ¿Está usted expuesto a alguno de los siguientes ri... |
| Q98 | - |  |  | SI | Radiaciones ionizantes |
| Q99 | - |  |  | SI | Óxido de etileno |
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