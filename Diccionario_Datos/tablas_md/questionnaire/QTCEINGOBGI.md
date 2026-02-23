# questionnaire.QTCEINGOBGI

> INGRESO GINECOLOGIA Y OBSTETRICIA

**Schema:** questionnaire
**Columnas:** 207
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO GINECOLOGIA Y OBSTETRICIA

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de examen |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Información entregada por |
| Q04 | varchar |  |  | SI | Procedencia |
| Q05 | varchar |  |  | SI | ESTADO GENERAL |
| Q06 | varchar |  |  | SI | Anamnesis Próxima |
| Q07 | varchar |  |  | SI | Factores de Riesgo Quirúrgico |
| Q08 | varchar |  |  | SI | Condición funcional basal |
| Q09 | varchar |  |  | SI | Utiliza red de salud |
| Q10 | varchar |  |  | SI | Pérdida significativa de peso |
| Q100 | bit |  |  | SI | Pelvis osea normal |
| Q101 | bit |  |  | SI | Útero en conformedad con el estagio del embarazo |
| Q102 | bit |  |  | SI | Labios mayores y menores de tamaño y aspecto norma... |
| Q103 | bit |  |  | SI | Clítoris de tamaño y aspecto normal. |
| Q104 | bit |  |  | SI | Glándulas de Bartholino normales. |
| Q105 | bit |  |  | SI | Paredes vaginales elásticas. Mucosa vaginal normal... |
| Q106 | bit |  |  | SI | Saco de Douglas libre. |
| Q107 | bit |  |  | SI | Cuello uterino de consistencia y tamaño normal. |
| Q108 | bit |  |  | SI | Útero en anteroversión, de tamaño y consistencia n... |
| Q109 | bit |  |  | SI | Flujo vaginal normal. |
| Q11 | varchar |  |  | SI | Medicamentos de uso reciente |
| Q110 | bit |  |  | SI | Anexos libres e indoloros. |
| Q111 | bit |  |  | SI | Parametrios normales. |
| Q112 | bit |  |  | SI | Vagina de elasticidad conservada. |
| Q113 | bit |  |  | SI | Cuello central de coloración normal, sin lesiones ... |
| Q114 | bit |  |  | SI | Mamas de tamaño y desarrollo normal, simétricas. |
| Q115 | bit |  |  | SI | No se palpan masas ni adenopatías locales. |
| Q116 | bit |  |  | SI | Pezones sin lesiones ni secreción anormal. |
| Q117 | varchar |  |  | SI | Inspección |
| Q118 | varchar |  |  | SI | Tacto vaginal |
| Q119 | varchar |  |  | SI | Especuloscopía |
| Q12 | varchar |  |  | SI | Chequeo evaluación preoperatoria |
| Q120 | varchar |  |  | SI | Ex. mamas |
| Q121 | varchar |  |  | SI | LCF Feto 1 (lpm) |
| Q121ObsDR | varchar |  | FK | SI | LCF Feto 1 (lpm) DR |
| Q122 | varchar |  |  | SI | LCF Feto 2 (lpm) |
| Q122ObsDR | varchar |  | FK | SI | LCF Feto 2 (lpm) DR |
| Q123 | varchar |  |  | SI | LCF Feto 3 (lpm) |
| Q123ObsDR | varchar |  | FK | SI | LCF Feto 3 (lpm) DR |
| Q124 | varchar |  |  | SI | Movimientos fetales |
| Q124ObsDR | varchar |  | FK | SI | Movimientos fetales DR |
| Q125 | varchar |  |  | SI | Presentación |
| Q125ObsDR | varchar |  | FK | SI | Presentación DR |
| Q126 | varchar |  |  | SI | Dorso fetal |
| Q126ObsDR | varchar |  | FK | SI | Dorso fetal DR |
| Q127 | varchar |  |  | SI | Plano de Hodge |
| Q127ObsDR | varchar |  | FK | SI | Plano de Hodge DR |
| Q128 | varchar |  |  | SI | Altura uterina (cms.) |
| Q128ObsDR | varchar |  | FK | SI | Altura uterina (cms.) DR |
| Q129 | varchar |  |  | SI | Tono uterino |
| Q129ObsDR | varchar |  | FK | SI | Tono uterino DR |
| Q13 | varchar |  |  | SI | REVISIÓN |
| Q130 | varchar |  |  | SI | Dinámica uterina |
| Q130ObsDR | varchar |  | FK | SI | Dinámica uterina DR |
| Q131 | varchar |  |  | SI | Contracciones (cada 10 min) |
| Q131ObsDR | varchar |  | FK | SI | Contracciones (cada 10 min) DR |
| Q132 | varchar |  |  | SI | Desaceleraciones |
| Q132ObsDR | varchar |  | FK | SI | Desaceleraciones DR |
| Q133 | varchar |  |  | SI | Líquido amniótico |
| Q133ObsDR | varchar |  | FK | SI | Líquido amniótico DR |
| Q134 | varchar |  |  | SI | Flujo vaginal |
| Q134ObsDR | varchar |  | FK | SI | Flujo vaginal DR |
| Q135 | varchar |  |  | SI | Membranas |
| Q135ObsDR | varchar |  | FK | SI | Membranas DR |
| Q136 | varchar |  |  | SI | Consistencia cuello |
| Q136ObsDR | varchar |  | FK | SI | Consistencia cuello DR |
| Q137 | varchar |  |  | SI | Posición |
| Q137ObsDR | varchar |  | FK | SI | Posición DR |
| Q138 | varchar |  |  | SI | Borramiento |
| Q138ObsDR | varchar |  | FK | SI | Borramiento DR |
| Q139 | varchar |  |  | SI | Dilatación cervical |
| Q139ObsDR | varchar |  | FK | SI | Dilatación cervical DR |
| Q14 | varchar |  |  | SI | Estado psíquico |
| Q140 | varchar |  |  | SI | Comentarios examen obstétrico |
| Q141 | varchar |  |  | SI | Comentario Examen Ginecológico |
| Q15 | varchar |  |  | SI | Estado de conciencia |
| Q16 | bit |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q17 | bit |  |  | SI | Hemodinamia estable, bien hidratado y perfundido. ... |
| Q18 | varchar |  |  | SI | Piel |
| Q19 | varchar |  |  | SI | P. Arterial Sistólica |
| Q19ObsDR | varchar |  | FK | SI | P. Arterial Sistólica DR |
| Q20 | varchar |  |  | SI | P. Arterial Diastólica |
| Q20ObsDR | varchar |  | FK | SI | P. Arterial Diastólica DR |
| Q21 | varchar |  |  | SI | Frecuencia cardíaca |
| Q21ObsDR | varchar |  | FK | SI | Frecuencia cardíaca DR |
| Q22 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q22ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q23 | varchar |  |  | SI | Temperatura axilar |
| Q23ObsDR | varchar |  | FK | SI | Temperatura axilar DR |
| Q24 | varchar |  |  | SI | Saturación O2 (%) |
| Q24ObsDR | varchar |  | FK | SI | Saturación O2 (%) DR |
| Q25 | varchar |  |  | SI | FiO2 (%) |
| Q25ObsDR | varchar |  | FK | SI | FiO2 (%) DR |
| Q26 | varchar |  |  | SI | Escala de dolor (EVA) |
| Q26ObsDR | varchar |  | FK | SI | Escala de dolor (EVA) DR |
| Q27 | bit |  |  | SI | Cabeza normal. Yugulares no ingurgitadas, pulso ca... |
| Q28 | varchar |  |  | SI | Cabeza y cuello |
| Q29 | varchar |  |  | SI | Descripción, cabeza y cuello |
| Q30 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q31 | varchar |  |  | SI | Auscultación |
| Q32 | varchar |  |  | SI | Descripción, cardiovascular |
| Q33 | bit |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q34 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q36 | bit |  |  | SI | Resto del examen realizado sin alteraciones |
| Q37 | bit |  |  | SI | Murmullo pulmonar simétrico normal, sin ruidos agr... |
| Q38 | varchar |  |  | SI | Descripción, pulmonar |
| Q40 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q41 | bit |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q42 | varchar |  |  | SI | Descripción, abdomen |
| Q43 | bit |  |  | SI | Mamas normales, axilas libres de empastamientos o ... |
| Q44 | varchar |  |  | SI | Descripción examen ginecológico |
| Q47 | bit |  |  | SI | Extremidades normales, sin lesiones. Edema (-). Ar... |
| Q48 | varchar |  |  | SI | Descripción, extremidades |
| Q49 | varchar |  |  | SI | Exámenes de laboratorio |
| Q50 | varchar |  |  | SI | Exámenes de imagenología |
| Q51 | varchar |  |  | SI | Conclusión |
| Q52 | varchar |  |  | SI | Plan al Ingreso |
| Q53 | varchar |  |  | SI | Profesional de salud |
| Q54 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q55 | varchar |  |  | SI | Descripción examen físico general |
| Q56 | bit |  |  | SI | Pulsos simétricos, amplitud normal. |
| Q57 | varchar |  |  | SI | Descripción Examen físico simple |
| Q58 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q59 | varchar |  |  | SI | Menarquia |
| Q60 | varchar |  |  | SI | Caracterísiticas del ciclo  |
| Q61 | varchar |  |  | SI | Alteración Intervalo / Duración |
| Q62 | varchar |  |  | SI | FERTILIDAD |
| Q63 | varchar |  |  | SI | Edad menopausia (si corresponde) |
| Q65 | varchar |  |  | SI | BIOPSIAS |
| Q66 | varchar |  |  | SI | CIRUGÍAS |
| Q67 | varchar |  |  | SI | PRÁCTICAS PREVENTIVAS |
| Q68 | date |  |  | SI | FECHA DE LA ÚLTIMA REGLA - FUR |
| Q69 | varchar |  |  | SI | CRITERIO PARA DETERMINAR FUR |
| Q70 | varchar |  |  | SI | NÚMERO DE FETOS |
| Q71 | varchar |  |  | SI | EXÁMENES EN EL PRIMER TRIMESTRE |
| Q72 | varchar |  |  | SI | EXÁMENES EN EL SEGUNDO TRIMESTRE |
| Q73 | varchar |  |  | SI | EXÁMENES EN EL TERCER TRIMESTRE |
| Q74 | varchar |  |  | SI | COLO UTERINO(imagen) |
| Q75 | varchar |  |  | SI | COMPLICACIONES MATERNAS EN EL EMBARAZO |
| Q76 | varchar |  |  | SI | COMPLICACIONES FETALES |
| Q77 | varchar |  |  | SI | DESCRIPCIÓN DEL EXAMEN OBSTÉTRICO |
| Q78 | bit |  |  | SI | Vulva normal, región inguinal sin adenopatias |
| Q79 | bit |  |  | SI | Vagina elástica, residuo normal |
| Q80 | bit |  |  | SI | Cuello uterino íntegro, bien epitelizado |
| Q81 | bit |  |  | SI | Útero y anexos de tamaño y mobilidad normales. |
| Q83 | varchar |  |  | SI | RESIDUO VAGINAL |
| Q84 | varchar |  |  | SI | DESCRIPCIÓN DEL EXAMEN GINECOLÓGICO |
| Q85 | varchar |  |  | SI | TACTO VAGINAL |
| Q86 | varchar |  |  | SI | SUSTENTACIÓN |
| Q87 | bit |  |  | SI | Resto del examen obstétrico realizado, sin alterac... |
| Q88 | bit |  |  | SI | Resto del examen ginecológico realizado, sin alter... |
| Q89 | bit |  |  | SI | Resto des examen respiratorio realizado, sin alter... |
| Q90 | varchar |  |  | SI | Vulva y Vagina |
| Q91 | varchar |  |  | SI | Pelvis ósea |
| Q92 | varchar |  |  | SI | Dilatación del cuello |
| Q92ObsDR | varchar |  | FK | SI | Dilatación del cuello DR |
| Q93 | varchar |  |  | SI | Bishop |
| Q93ObsDR | varchar |  | FK | SI | Bishop DR |
| Q94 | varchar |  |  | SI | Plan de De Lee |
| Q94ObsDR | varchar |  | FK | SI | Plan de De Lee DR |
| Q95 | varchar |  |  | SI | Presentación |
| Q96 | varchar |  |  | SI | Latidos cardiacos fetales |
| Q96ObsDR | varchar |  | FK | SI | Latidos cardiacos fetales DR |
| Q97 | varchar |  |  | SI | Reactividad LCF |
| Q98 | varchar |  |  | SI | Descripción |
| Q99 | bit |  |  | SI | Vulva normal, vagina amplia y elástica. Residuo no... |
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