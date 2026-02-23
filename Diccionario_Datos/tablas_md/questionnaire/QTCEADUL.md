# questionnaire.QTCEADUL

> Ficha Salud General de la Mujer

**Schema:** questionnaire
**Columnas:** 237
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Salud General de la Mujer

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ159 | varchar |  |  | SI | - |
| CQ27 | varchar |  |  | SI | - |
| CQ30 | varchar |  |  | SI | - |
| CQ37 | varchar |  |  | SI | - |
| CQ51 | varchar |  |  | SI | - |
| CQ52 | varchar |  |  | SI | - |
| CQ55 | varchar |  |  | SI | - |
| CQ75 | varchar |  |  | SI | - |
| CQ93 | varchar |  |  | SI | - |
| CQregla | varchar |  |  | SI | - |
| Q1 | varchar |  |  | SI | Peso(kg) |
| Q10 | varchar |  |  | SI | ¿Realiza actividad fisica? |
| Q100 | bit |  |  | SI | Alergia al espermicida |
| Q101 | bit |  |  | SI | Cáncer cérvico-uterino |
| Q102 | bit |  |  | SI | Cáncer de la mama |
| Q103 | bit |  |  | SI | Complicaciones del embarazo con DIU |
| Q104 | bit |  |  | SI | Enfermedad inflamatoria pélvica aguda |
| Q105 | bit |  |  | SI | Enfermedad tromboembólica |
| Q106 | bit |  |  | SI | Enfermedades hepáticas |
| Q107 | bit |  |  | SI | Hipertensión arterial |
| Q108 | bit |  |  | SI | Infarto del miocardio |
| Q109 | bit |  |  | SI | Patología cardiovascular arterial |
| Q11 | varchar |  |  | SI | Edad inicio de actividad sexual (años) |
| Q110 | bit |  |  | SI | Perforación |
| Q111 | bit |  |  | SI | Alergia al látex |
| Q112 | bit |  |  | SI | Alteraciones del sangrado uterino |
| Q113 | bit |  |  | SI | Ánimo depresivo |
| Q114 | bit |  |  | SI | Aumento de peso |
| Q115 | bit |  |  | SI | Cansancio |
| Q116 | bit |  |  | SI | Cefalea |
| Q117 | bit |  |  | SI | Cloasma |
| Q118 | bit |  |  | SI | Disminucion de la libido |
| Q119 | bit |  |  | SI | Dolor |
| Q12 | varchar |  |  | SI | Clasificación de dependencia |
| Q120 | bit |  |  | SI | Dolor durante el coito |
| Q121 | bit |  |  | SI | Edema |
| Q122 | bit |  |  | SI | Flujo vaginal inespecífico |
| Q123 | bit |  |  | SI | Folículos persistentes o quistes foliculares |
| Q124 | bit |  |  | SI | Incrustación |
| Q125 | bit |  |  | SI | Infección |
| Q126 | bit |  |  | SI | Irritabilidad |
| Q127 | bit |  |  | SI | Mastalgia |
| Q128 | bit |  |  | SI | Náuseas |
| Q129 | bit |  |  | SI | Sangrado o goteo irregular (spotting) |
| Q12ObsDR | varchar |  | FK | SI | Clasificación de dependencia DR |
| Q13 | numeric |  |  | SI | Edad menarquia |
| Q130 | bit |  |  | SI | Sensibilidad en las mamas |
| Q131 | bit |  |  | SI | Tensión premenstrual |
| Q132 | bit |  |  | SI | Vómitos |
| Q133 | bit |  |  | SI | Accidente vascular cerebral |
| Q134 | bit |  |  | SI | Cambios metabólicos |
| Q135 | varchar |  |  | SI | Clasificación circunferencia de la cintura |
| Q135ObsDR | varchar |  | FK | SI | Clasificación circunferencia de la cintura DR |
| Q136 | varchar |  |  | SI | Puntaje |
| Q137 | varchar |  |  | SI | Piezas dentales presentes |
| Q139 | varchar |  |  | SI | ¿Se le entrego la  guía para la gestación y el nac... |
| Q14 | numeric |  |  | SI | Edad de la menopausia |
| Q140 | varchar |  |  | SI | Resultado Riesgo Psicosocial Abreviado |
| Q140ObsDR | varchar |  | FK | SI | Resultado Riesgo Psicosocial Abreviado DR |
| Q141 | varchar |  |  | SI | ¿Presenta algún riesgo psicosocial de acuerdo a la... |
| Q142 | varchar |  |  | SI | 1 |
| Q143 | varchar |  |  | SI | ¿Existe alguna situación de vulnerablidad social d... |
| Q144 | varchar |  |  | SI | 2 |
| Q145 | varchar |  |  | SI | ¿Está de acuerdo con integrarse a visitas dimicili... |
| Q146 | bit |  |  | SI | Fisiológico |
| Q147 | bit |  |  | SI | De alto riesgo |
| Q148 | varchar |  |  | SI | Continúa control ARO en |
| Q149 | bit |  |  | SI | ¿Quién la acompaña en el control ? |
| Q15 | numeric |  |  | SI | Edad espermarca (años) |
| Q150 | bit |  |  | SI | Acude sola al control |
| Q151 | bit |  |  | SI | Conyuge o pareja |
| Q152 | bit |  |  | SI | Madre de la gestante |
| Q153 | varchar |  |  | SI | Otro (especificar parentesco o relación con la ges... |
| Q156 | varchar |  |  | SI | Circunferencia Abdominal |
| Q156ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q157 | varchar |  |  | SI | Resultado de Escala de Edimburgo  |
| Q158 | varchar |  |  | SI | Método Anticonceptivo Preferido |
| Q158ObsDR | varchar |  | FK | SI | Método Anticonceptivo Preferido DR |
| Q159 | varchar |  |  | SI | Lactancia |
| Q16 | varchar |  |  | SI | En el inicio de su vida sexual ¿usó preservativo? |
| Q17 | varchar |  |  | SI | ¿Activo sexualmente? |
| Q18 | varchar |  |  | SI | ¿Cómo percibe su vida sexual actualmente? |
| Q19 | numeric |  |  | SI | Nº de parejas sexuales |
| Q1ObsDR | varchar |  | FK | SI | Peso(kg) DR |
| Q2 | varchar |  |  | SI | Talla (cms.) |
| Q20 | varchar |  |  | SI | ¿En los últimos 12 meses usó preservativo? |
| Q21 | date |  |  | SI | Fecha último embarazo |
| Q22 | numeric |  |  | SI | N° de gestas |
| Q23 | numeric |  |  | SI | N° de hijos vivos |
| Q24 | numeric |  |  | SI | N° de abortos |
| Q25 | varchar |  |  | SI | Rersultado examen físico de mamas |
| Q25ObsDR | varchar |  | FK | SI | Rersultado examen físico de mamas DR |
| Q26 | date |  |  | SI | Fecha resultado PAP |
| Q27 | varchar |  |  | SI | Resultado PAP |
| Q28 | date |  |  | SI | Fecha resultado flujo vaginal |
| Q29 | varchar |  |  | SI | Resultado flujo vaginal |
| Q29ObsDR | varchar |  | FK | SI | Resultado flujo vaginal DR |
| Q2ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q3 | varchar |  |  | SI | Índice de masa corporal (IMC) |
| Q30 | varchar |  |  | SI | Método anticonceptivo |
| Q31 | date |  |  | SI | Fecha inicio método anticonceptivo principal |
| Q32 | varchar |  |  | SI | ¿Efectos adversos? |
| Q34 | varchar |  |  | SI | Observacion de otros efectos adversos |
| Q35 | varchar |  |  | SI | ¿Se encuentra con terapia hormonal de reemplazo? |
| Q36 | date |  |  | SI | Fecha inicio terapia hormonal de reemplazo |
| Q37 | varchar |  |  | SI | ¿Qué método anticonceptivo utiliza con su pareja? |
| Q38 | varchar |  |  | SI | Clasificación presión arterial |
| Q39 | varchar |  |  | SI | Clasificacion glicemia venosa en ayunas |
| Q4 | varchar |  |  | SI | Calificación estado nutricional según IMC |
| Q40 | varchar |  |  | SI | Clasificacion sobrecarga de glucosa |
| Q41 | varchar |  |  | SI | ¿Se aplicó QUALIDIAB? |
| Q42 | date |  |  | SI | Fecha aplicación QUALIDIAB |
| Q43 | varchar |  |  | SI | ¿Se encuentra con tratamiento de insulina? |
| Q44 | varchar |  |  | SI | ¿Tiene úlcera activa en pie? |
| Q45 | varchar |  |  | SI | ¿Tiene úlcera activa tratada con manejo avanzado d... |
| Q46 | varchar |  |  | SI | ¿Amputación de pie debida a DM? |
| Q47 | varchar |  |  | SI | Grupo de Riesgo Ulceración |
| Q47ObsDR | varchar |  | FK | SI | Grupo de Riesgo Ulceración DR |
| Q48 | varchar |  |  | SI | Clasificación Colesterol |
| Q49 | varchar |  |  | SI | ¿Completó el módulo de actividad física? |
| Q4ObsDR | varchar |  | FK | SI | Calificación estado nutricional según IMC DR |
| Q5 | numeric |  |  | SI | Circunferencia de cintura (cm.) |
| Q50 | varchar |  |  | SI | Resultado evaluación de riesgo suicida (OKASHA) |
| Q50ObsDR | varchar |  | FK | SI | Resultado evaluación de riesgo suicida (OKASHA) DR |
| Q51 | varchar |  |  | SI | Clasificación discapacidad de causa psíquica |
| Q52 | varchar |  |  | SI | Resultado atención de salud mental |
| Q53 | varchar |  |  | SI | Resultado AUDIT |
| Q53ObsDR | varchar |  | FK | SI | Resultado AUDIT DR |
| Q54 | varchar |  |  | SI | Clasificación consumo de sustancias ilícitas |
| Q55 | varchar |  |  | SI | Resultado atención odontológica |
| Q56 | varchar |  |  | SI | Índice COP |
| Q57 | varchar |  |  | SI | Cariadas - N° sextante I |
| Q58 | varchar |  |  | SI | Cariadas - N° sextante II |
| Q59 | varchar |  |  | SI | Cariadas - N° sextante III |
| Q6 | varchar |  |  | SI | Diagnóstico nutricional |
| Q60 | varchar |  |  | SI | Cariadas - N° sextante IV |
| Q61 | varchar |  |  | SI | Cariadas - N° sextante V |
| Q62 | varchar |  |  | SI | Cariadas - N° sextante VI |
| Q63 | varchar |  |  | SI | Obturadas - N° sextante I |
| Q64 | varchar |  |  | SI | Obturadas - N° sextante II |
| Q65 | varchar |  |  | SI | Obturadas - N° sextante III |
| Q66 | varchar |  |  | SI | Obturadas - N° sextante IV |
| Q67 | varchar |  |  | SI | Obturadas - N° sextante V |
| Q68 | varchar |  |  | SI | Obturadas - N° sextante VI |
| Q69 | varchar |  |  | SI | Perdidas - N° sextante I |
| Q6ObsDR | varchar |  | FK | SI | Diagnóstico nutricional DR |
| Q7 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q70 | varchar |  |  | SI | Perdidas - N° sextante II |
| Q71 | varchar |  |  | SI | Perdidas - N° sextante III |
| Q72 | varchar |  |  | SI | Perdidas - N° sextante IV |
| Q73 | varchar |  |  | SI | Perdidas - N° sextante V |
| Q74 | varchar |  |  | SI | Perdidas - N° sextante VI |
| Q75 | varchar |  |  | SI | Derivacion a red asistencial |
| Q76 | date |  |  | SI | Fecha resultado glicemia venosa en ayunas |
| Q77 | varchar |  |  | SI | Resultado glicemia venosa en ayunas |
| Q77ObsDR | varchar |  | FK | SI | Resultado glicemia venosa en ayunas DR |
| Q78 | date |  |  | SI | Fecha resultado prueba sobrecarga a la glucosa |
| Q79 | varchar |  |  | SI | Resultado prueba de sobrecarga a la glucosa |
| Q7ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q8 | varchar |  |  | SI | Riesgo Cardiovascular |
| Q80 | date |  |  | SI | Fecha hemoglobina glicosilada |
| Q81 | varchar |  |  | SI | Resultado hemoglobina glicosilada |
| Q81ObsDR | varchar |  | FK | SI | Resultado hemoglobina glicosilada DR |
| Q82 | date |  |  | SI | Fecha resultado colesterol total |
| Q83 | varchar |  |  | SI | Resultado colesterol total |
| Q83ObsDR | varchar |  | FK | SI | Resultado colesterol total DR |
| Q84 | date |  |  | SI | Fecha resultado VDRL |
| Q85 | varchar |  |  | SI | Resultado VDRL |
| Q85ObsDR | varchar |  | FK | SI | Resultado VDRL DR |
| Q86 | date |  |  | SI | Fecha resultado RPR |
| Q87 | varchar |  |  | SI | Resultado RPR |
| Q87ObsDR | varchar |  | FK | SI | Resultado RPR DR |
| Q88 | date |  |  | SI | Fecha resultado test de ELISA |
| Q89 | varchar |  |  | SI | Resultado test de ELISA |
| Q89ObsDR | varchar |  | FK | SI | Resultado test de ELISA DR |
| Q8ObsDR | varchar |  | FK | SI | Riesgo Cardiovascular DR |
| Q9 | varchar |  |  | SI | Tabaquismo |
| Q90 | date |  |  | SI | Fecha resultado baciloscopía |
| Q91 | varchar |  |  | SI | Resultado baciloscopía |
| Q91ObsDR | varchar |  | FK | SI | Resultado baciloscopía DR |
| Q92 | date |  |  | SI | Fecha resultado antígeno prostático |
| Q93 | varchar |  |  | SI | Resultado antígeno prostático |
| Q94 | date |  |  | SI | Fecha resultado mamografía |
| Q95 | varchar |  |  | SI | Resultado mamografía |
| Q95ObsDR | varchar |  | FK | SI | Resultado mamografía DR |
| Q96 | date |  |  | SI | Fecha ecografía mamaria |
| Q97 | varchar |  |  | SI | Resultado ecografía mamaria |
| Q97ObsDR | varchar |  | FK | SI | Resultado ecografía mamaria DR |
| Q98 | varchar |  |  | SI | Indicar efecto(s) adverso(s): |
| Q99 | bit |  |  | SI | Acné |
| QMIM2 | varchar |  |  | SI | Mujer con Infante Menor de 2 Años |
| QMIM2ObsDR | varchar |  | FK | SI | Mujer con Infante Menor de 2 Años DR |
| QMPP | varchar |  |  | SI | Meses Post-Parto |
| QPAD | varchar |  |  | SI | Presión arterial diastólica (mmHg) |
| QPADObsDR | varchar |  | FK | SI | Presión arterial diastólica (mmHg) DR |
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
| Qregla | varchar |  |  | SI | regla |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*