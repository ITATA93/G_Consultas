# questionnaire.QTCECLAP2

**Schema:** questionnaire
**Columnas:** 161
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q100PE | varchar | PK |  | SI | Resultado Situación Psico - emocional |
| Q101EF | varchar | PK |  | SI | REsultado Exámen Físico |
| Q102TOT | varchar | PK |  | SI | Total Posible Riesgo |
| Q103EN | varchar | PK |  | SI | Estado Nutricional |
| Q103ENObsDR | varchar | PK | FK | SI | Estado Nutricional DR |
| Q104X | varchar | PK |  | SI | Resultado Hábitos / Consumo 2 |
| Q105X | varchar | PK |  | SI | Resultado Gineco-Urológico 2 |
| Q106X | varchar | PK |  | SI | Resultado Sexualidad 2 |
| Q107X | varchar | PK |  | SI | Resultado Situación Psico-Emocional 2 |
| Q108X | varchar | PK |  | SI | Resultado Examen Físico 2 |
| Q109 | date | PK |  | SI | Fecha Próximo Control |
| Q114HC | varchar | PK |  | SI | SUEÑO NORMAL |
| Q115HC | numeric | PK |  | SI | HORAS |
| Q116HC | varchar | PK |  | SI | ALIMENTACIÓN ADECUADA |
| Q117HC | numeric | PK |  | SI | COMIDAS POR DÍA CON FAMILIA |
| Q118HC | varchar | PK |  | SI | TABACO |
| Q119HC | numeric | PK |  | SI | EDAD DE INICIO AÑOS |
| Q120HC | numeric | PK |  | SI | NÚMERO CIGARRILLOS/DÍA |
| Q121HC | varchar | PK |  | SI | ALCOHOL (Frecuente) |
| Q122HC | numeric | PK |  | SI | EDAD DE INICIO |
| Q123HC | numeric | PK |  | SI | MESES |
| Q124HC | varchar | PK |  | SI | EPISODIOS DE ABUSO |
| Q125HC | varchar | PK |  | SI | OTRA/S SUSTANCIA/S |
| Q126HC | varchar | PK |  | SI | ¿CUÁL? ¿CUÁLES? |
| Q127HC | numeric | PK |  | SI | EDAD DE INICIO |
| Q128HC | numeric | PK |  | SI | MESES |
| Q129HC | varchar | PK |  | SI | REPERCUSIONES |
| Q130HC | varchar | PK |  | SI | CONDUCE VEHÍCULO |
| Q131HC | varchar | PK |  | SI | ¿CUÁL? |
| Q132HC | varchar | PK |  | SI | SEGURIDAD VIAL |
| Q133HC | varchar | PK |  | SI | Observaciones |
| Q134GU | numeric | PK |  | SI | MENARCA/ESPERMARCA (Años) |
| Q135GU | numeric | PK |  | SI | MESES |
| Q136GU | varchar | PK |  | SI | FECHA ÚLTIMA MENSTRUACIÓN |
| Q137GU | date | PK |  | SI | FECHA |
| Q138GU | varchar | PK |  | SI | CICLOS REGULARES |
| Q139GU | varchar | PK |  | SI | DISMENORREA |
| Q140GU | varchar | PK |  | SI | FLUJO PATOLÓGICO/SECRECIÓN PENEANA |
| Q141GU | varchar | PK |  | SI | ITS / VIH |
| Q142GU | varchar | PK |  | SI | ¿CUÁL? |
| Q143GU | varchar | PK |  | SI | TRATAMIENTO |
| Q144GU | varchar | PK |  | SI | BÚSQUEDA DE CONTACTOS |
| Q145GU | varchar | PK |  | SI | TRATAMIENTO DE CONTACTOS |
| Q146GU | varchar | PK |  | SI | EMBARAZOS |
| Q147GU | varchar | PK |  | SI | HIJOS |
| Q148GU | varchar | PK |  | SI | ABORTOS |
| Q149GU | varchar | PK |  | SI | Observaciones |
| Q150S | varchar | PK |  | SI | RELACIONES SEXUALES |
| Q151S | varchar | PK |  | SI | PAREJA SEXUAL |
| Q152S | numeric | PK |  | SI | EDAD INICIO REL.SEXUAL |
| Q153S | varchar | PK |  | SI | BAJO COERCIÓN |
| Q154S | varchar | PK |  | SI | DIFICULTADES EN REL.SEX. |
| Q155S | varchar | PK |  | SI | ANTICONCEPCIÓN (Uso habitual del condón) |
| Q156S | varchar | PK |  | SI | ACO Píldora |
| Q157S | varchar | PK |  | SI | INYECTABLE |
| Q159S | varchar | PK |  | SI | IMPLANTE |
| Q160S | varchar | PK |  | SI | INICIÓ MAC |
| Q161S | varchar | PK |  | SI | OTRO HORMONAL (Anillo, Vaginal, Parche, AE) |
| Q162S | varchar | PK |  | SI | OTRO MÉTODO DE BARRERA |
| Q164S | varchar | PK |  | SI | RITMO |
| Q165S | varchar | PK |  | SI | DIU |
| Q166S | varchar | PK |  | SI | EQV masc |
| Q167S | varchar | PK |  | SI | EQV fem |
| Q168S | varchar | PK |  | SI | CONSEJERÍA |
| Q169S | varchar | PK |  | SI | ACO DE EMERGENCIA |
| Q170S | varchar | PK |  | SI | Observaciones |
| Q171PE | varchar | PK |  | SI | IMAGEN CORPORAL |
| Q172PE | varchar | PK |  | SI | ESTADO DE ÁNIMO |
| Q173PE | varchar | PK |  | SI | REFERENTE AL ADULTO |
| Q174PE | varchar | PK |  | SI | VIDA CON PROYECTO |
| Q175PE | varchar | PK |  | SI | REDES SOCIALES DE APOYO |
| Q176PE | numeric | PK |  | SI | CELULAR |
| Q177PE | numeric | PK |  | SI | TELÉFONO |
| Q178PE | varchar | PK |  | SI | Observaciones |
| Q179EF | varchar | PK |  | SI | ASPECTO GENERAL |
| Q180EF | varchar | PK |  | SI | PESO (Kg) |
| Q180EFObsDR | varchar | PK | FK | SI | PESO (Kg) DR |
| Q181EF | varchar | PK |  | SI | TALLA (cm) |
| Q181EFObsDR | varchar | PK | FK | SI | TALLA (cm) DR |
| Q182EF | varchar | PK |  | SI | CENTIL PESO/EDAD |
| Q182EFObsDR | varchar | PK | FK | SI | CENTIL PESO/EDAD DR |
| Q183EF | varchar | PK |  | SI | CENTIL TALLA/EDAD |
| Q183EFObsDR | varchar | PK | FK | SI | CENTIL TALLA/EDAD DR |
| Q184EF | varchar | PK |  | SI | IMC |
| Q185EF | varchar | PK |  | SI | CENTIL IMC |
| Q185EFObsDR | varchar | PK | FK | SI | CENTIL IMC DR |
| Q186EF | varchar | PK |  | SI | PIEL, FANERAS Y MUCOSA |
| Q187EF | varchar | PK |  | SI | CABEZA |
| Q188EF | varchar | PK |  | SI | AGUDEZA VISUAL |
| Q189EF | varchar | PK |  | SI | AGUDEZA AUDITIVA |
| Q190EF | varchar | PK |  | SI | SALUD BUCAL |
| Q191EF | varchar | PK |  | SI | CUELLO Y TIROIDES |
| Q192EF | varchar | PK |  | SI | TORAX Y MAMAS |
| Q193EF | varchar | PK |  | SI | CARDIOPULMONAR |
| Q194EF | varchar | PK |  | SI | PRESIÓN SISTÓLICA |
| Q194EFObsDR | varchar | PK | FK | SI | PRESIÓN SISTÓLICA DR |
| Q195EF | varchar | PK |  | SI | PRESIÓN DIASTÓLICA |
| Q195EFObsDR | varchar | PK | FK | SI | PRESIÓN DIASTÓLICA DR |
| Q196EF | varchar | PK |  | SI | FRECUENCIA CARDIACA (latidos/min) |
| Q196EFObsDR | varchar | PK | FK | SI | FRECUENCIA CARDIACA (latidos/min) DR |
| Q197EF | varchar | PK |  | SI | ABDOMEN |
| Q198EF | varchar | PK |  | SI | GENITO-URINARIO |
| Q199EF | varchar | PK |  | SI | TANNER |
| Q200EF | varchar | PK |  | SI | COLUMNA |
| Q201EF | varchar | PK |  | SI | EXTREMIDADES |
| Q202EF | varchar | PK |  | SI | NEUROLÓGICO |
| Q203EF | varchar | PK |  | SI | Observaciones |
| Q205EF | varchar | PK |  | SI | IMPRESIÓN DIAGNOSTICA INTEGRAL |
| Q206EF | numeric | PK |  | SI | PERIMETRO CINTURA CADERA |
| Q207EF | numeric | PK |  | SI | PERCENTIL IMC |
| Q208EF | varchar | PK |  | SI | MAMAS  |
| Q208EFObsDR | varchar | PK | FK | SI | MAMAS  DR |
| Q209EF | varchar | PK |  | SI | VELLO PÚBICO |
| Q209EFObsDR | varchar | PK | FK | SI | VELLO PÚBICO DR |
| Q210EF | varchar | PK |  | SI | GENITALES |
| Q210EFObsDR | varchar | PK | FK | SI | GENITALES DR |
| Q210HC | numeric | PK |  | SI | COMIDAS POR DÍA |
| Q97HC | varchar | PK |  | SI | Resultado Hábitos y Consumo |
| Q98GU | varchar | PK |  | SI | Resultado Gineco-Urológico |
| Q99S | varchar | PK |  | SI | Resultado Sexualidad |
| QCPA | varchar | PK |  | SI | Clasificación Presión Arterial  |
| QCPAObsDR | varchar | PK | FK | SI | Clasificación Presión Arterial  DR |
| QIMAGEN | varchar | PK |  | SI | Tablas de Hipertensión |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*