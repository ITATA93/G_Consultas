# questionnaire.QTCENN

> Control Salud Integral Niños 0-4 años

**Schema:** questionnaire
**Columnas:** 195
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Control Salud Integral Niños 0-4 años

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ65 | varchar |  |  | SI | - |
| CQ69 | varchar |  |  | SI | - |
| CQ77 | varchar |  |  | SI | - |
| CQ79 | varchar |  |  | SI | - |
| CQNN024 | varchar |  |  | SI | - |
| CQNN027 | varchar |  |  | SI | - |
| CQNN033 | varchar |  |  | SI | - |
| CQNN034 | varchar |  |  | SI | - |
| CQNN038 | varchar |  |  | SI | - |
| CQNN061 | varchar |  |  | SI | - |
| CQNN062 | varchar |  |  | SI | - |
| CQREEDP | varchar |  |  | SI | - |
| CQRPB | varchar |  |  | SI | - |
| CQRPND | varchar |  |  | SI | - |
| CQRRMBN | varchar |  |  | SI | - |
| CQRRO | varchar |  |  | SI | - |
| CQRTEPSI | varchar |  |  | SI | - |
| CQregla | varchar |  |  | SI | - |
| Q105 | varchar |  |  | SI | EOA Realizado |
| Q106 | varchar |  |  | SI | Resultado EOA |
| Q107 | varchar |  |  | SI | Ecocardiograma Realizado |
| Q108 | varchar |  |  | SI | Resultado Ecocardiograma |
| Q109 | date |  |  | SI | Fecha última vacuna Hepatitis B |
| Q110 | varchar |  |  | SI | Material Educativo entregado |
| Q111 | varchar |  |  | SI | Digitación SDRN |
| Q63 | varchar |  |  | SI | Entrega de Material Educativo |
| Q64 | varchar |  |  | SI | Entrega de Material Educativo (Txt) |
| Q65 | varchar |  |  | SI | El Niño o Niña vive con: |
| Q67 | varchar |  |  | SI | Tipo Discapacidad Madre |
| Q68 | varchar |  |  | SI | ¿El niño o niña está afectado por alguna discapaci... |
| Q69 | varchar |  |  | SI | El Niño/a está afectado por alguna condición que i... |
| Q70 | bit |  |  | SI | Hijo/a de madre con adicción a las drogas, y/o alc... |
| Q71 | bit |  |  | SI | Niño/a afectado/a por maltrato infantil |
| Q72 | bit |  |  | SI | Niño/a afectado/a por malformaciones congénitas |
| Q73 | bit |  |  | SI | Niño/a afectado/a por enfermedad crónica |
| Q74 | varchar |  |  | SI | Otro (especifique cual) |
| Q75 | varchar |  |  | SI | ¿Asiste el niño/a a una sala cuna o jardín infanti... |
| Q76 | varchar |  |  | SI | ¿Está de acuerdo con integrarse a Visitas Domicili... |
| Q77 | varchar |  |  | SI | ¿Quién acompaña al niño/a en la atención? |
| Q78 | varchar |  |  | SI | Otro (Especificar) |
| Q79 | varchar |  |  | SI | La Madre o cuidador principal ¿Presenta alguna dis... |
| Q80 | varchar |  |  | SI | Tutor |
| Q88 | varchar |  |  | SI | ¿Existe otra situación de vulnerabilidad distinta ... |
| Q89 | varchar |  |  | SI | Otra situación de vulnerabilidad |
| Q90 | date |  |  | SI | Fecha de Egreso de Hospitalización |
| Q92 | varchar |  |  | SI | ¿Existe otra situación de vulnerabilidad distinta ... |
| QEC | varchar |  |  | SI | Edad Corregida |
| QECObsDR | varchar |  | FK | SI | Edad Corregida DR |
| QENI | varchar |  |  | SI | Estado Nutricional Infantil |
| QENIObsDR | varchar |  | FK | SI | Estado Nutricional Infantil DR |
| QEX1 | varchar |  |  | SI | Cabeza |
| QEX10 | varchar |  |  | SI | Comentario General |
| QEX11 | bit |  |  | SI | Con Observación de Alerta |
| QEX2 | varchar |  |  | SI | Cuello |
| QEX3 | varchar |  |  | SI | Tórax |
| QEX4 | varchar |  |  | SI | Exámen Cardiaco |
| QEX5 | varchar |  |  | SI | Exámen Pulmonar |
| QEX6 | varchar |  |  | SI | Abdomen |
| QEX7 | varchar |  |  | SI | Exámen Genital |
| QEX8 | varchar |  |  | SI | Columna |
| QEX9 | varchar |  |  | SI | Extremidades |
| QIIM | bit |  |  | SI | Ingresar Información Manualmente |
| QNN001 | varchar |  |  | SI | ¿Embarazo Controlado? |
| QNN002 | varchar |  |  | SI | ¿Patología durante el embarazo? |
| QNN003 | varchar |  |  | SI | Especificar ¿cuáles? |
| QNN005 | varchar |  |  | SI | Especificar lugar del parto |
| QNN006 | varchar |  |  | SI | Tipo de Parto |
| QNN007 | varchar |  |  | SI | ¿Estuvo presente el padre en el parto? |
| QNN008 | varchar |  |  | SI | Edad Gestacional al Nacer |
| QNN008ObsDR | varchar |  | FK | SI | Edad Gestacional al Nacer DR |
| QNN009 | varchar |  |  | SI | Relación Peso/Edad Nacimiento |
| QNN009ObsDR | varchar |  | FK | SI | Relación Peso/Edad Nacimiento DR |
| QNN010 | varchar |  |  | SI | Peso al Nacer |
| QNN010ObsDR | varchar |  | FK | SI | Peso al Nacer DR |
| QNN011 | varchar |  |  | SI | Talla al Nacer |
| QNN011ObsDR | varchar |  | FK | SI | Talla al Nacer DR |
| QNN012 | varchar |  |  | SI | Perímetro Craneano al Nacer |
| QNN012ObsDR | varchar |  | FK | SI | Perímetro Craneano al Nacer DR |
| QNN013 | numeric |  |  | SI | APGAR 1 Minuto |
| QNN014 | numeric |  |  | SI | APGAR 5 Minutos |
| QNN015 | date |  |  | SI | Fecha resultado fenilcetonuria e hipertiroidismo c... |
| QNN016 | varchar |  |  | SI | Resultado fenilcetonuria |
| QNN017 | varchar |  |  | SI | Resultado hipotiroidismo congénito |
| QNN018 | date |  |  | SI | Fecha vacuna BCG |
| QNN019 | varchar |  |  | SI | Índice de masa corporal (IMC) |
| QNN020 | varchar |  |  | SI | Hospitalización  |
| QNN021 | varchar |  |  | SI | Motivo(s) de Hospitalización |
| QNN022 | varchar |  |  | SI | Peso (Kg) |
| QNN022ObsDR | varchar |  | FK | SI | Peso (Kg) DR |
| QNN023 | varchar |  |  | SI | Talla (Cms) |
| QNN023ObsDR | varchar |  | FK | SI | Talla (Cms) DR |
| QNN024 | varchar |  |  | SI | Estadio de Tanner |
| QNN026 | varchar |  |  | SI | Perímetro craneano |
| QNN026ObsDR | varchar |  | FK | SI | Perímetro craneano DR |
| QNN027 | varchar |  |  | SI | Percentil perímetro craneano |
| QNN028 | varchar |  |  | SI | Fontanela Diametro |
| QNN0281 | varchar |  |  | SI | Fontanela Palpación |
| QNN029 | varchar |  |  | SI | Peso/Edad |
| QNN029ObsDR | varchar |  | FK | SI | Peso/Edad DR |
| QNN030 | varchar |  |  | SI | Peso/Talla |
| QNN030ObsDR | varchar |  | FK | SI | Peso/Talla DR |
| QNN031 | varchar |  |  | SI | Talla/Edad |
| QNN031ObsDR | varchar |  | FK | SI | Talla/Edad DR |
| QNN033 | varchar |  |  | SI | Calificación estado nutricional según IMC |
| QNN034 | varchar |  |  | SI | Diagnóstico nutricional integrado |
| QNN035 | varchar |  |  | SI | Presión arterial(mmHg) |
| QNN036 | varchar |  |  | SI | Clasificación  por percentil  presión arterial sis... |
| QNN037 | varchar |  |  | SI | Clasificación percentil presión arterial diastólic... |
| QNN038 | varchar |  |  | SI | Tipo de alimentación (Antiguo) |
| QNN039 | varchar |  |  | SI | Detalle de alimentación (otras comidas) |
| QNN040 | varchar |  |  | SI | Tiempo de lactancia materna exclusiva(meses) |
| QNN043 | varchar |  |  | SI | ¿Se entregó guía anticipatoria de prevención de ac... |
| QNN044 | varchar |  |  | SI | ¿Responde al inventario de conductas en la infanci... |
| QNN054 | varchar |  |  | SI | Resultado Riergo Morir de Bronconeumonía |
| QNN055 | varchar |  |  | SI | Resultado Score Riesgo de Obesidad   |
| QNN055ObsDR | varchar |  | FK | SI | Resultado Score Riesgo de Obesidad   DR |
| QNN056 | varchar |  |  | SI | Resultado Escala Massie-Campbel |
| QNN056ObsDR | varchar |  | FK | SI | Resultado Escala Massie-Campbel DR |
| QNN057 | varchar |  |  | SI | Resultado Escala Edimburgo |
| QNN058 | varchar |  |  | SI | Resultado Pauta Breve de Desarrollo Psicomotor |
| QNN058ObsDR | varchar |  | FK | SI | Resultado Pauta Breve de Desarrollo Psicomotor DR |
| QNN059 | varchar |  |  | SI | Resultado EEDP |
| QNN059ObsDR | varchar |  | FK | SI | Resultado EEDP DR |
| QNN060 | varchar |  |  | SI | Resultado TEPSI |
| QNN060ObsDR | varchar |  | FK | SI | Resultado TEPSI DR |
| QNN061 | varchar |  |  | SI | Visión ojo derecho |
| QNN062 | varchar |  |  | SI | Visión ojo izquierdo |
| QNN063 | date |  |  | SI | Fecha resultado RX de pelvis |
| QNN064 | varchar |  |  | SI | Resultado RX de pelvis |
| QNN065 | varchar |  |  | SI | Diagnóstico Protocolo de Neurodesarrollo |
| QNN065ObsDR | varchar |  | FK | SI | Diagnóstico Protocolo de Neurodesarrollo DR |
| QNN067 | varchar |  |  | SI | Calificación Perímetro Craneano |
| QNN090 | varchar |  |  | SI | Tipo de Lactancia |
| QNN090ObsDR | varchar |  | FK | SI | Tipo de Lactancia DR |
| QNN123 | varchar |  |  | SI | Estado Nutricional PNAC |
| QNN123ObsDR | varchar |  | FK | SI | Estado Nutricional PNAC DR |
| QNN124 | varchar |  |  | SI | Displasia Bronco-Pulmonar |
| QNN124ObsDR | varchar |  | FK | SI | Displasia Bronco-Pulmonar DR |
| QNNA01E | varchar |  |  | SI | Curso [REM] |
| QPNN | varchar |  |  | SI | Paciente NANEAS |
| QPREDIS | varchar |  |  | SI | Presion Arterial Diastólica (mmHg) |
| QPREDISObsDR | varchar |  | FK | SI | Presion Arterial Diastólica (mmHg) DR |
| QPRESIS | varchar |  |  | SI | Presion Arterial Sistólica (mmHg) |
| QPRESISObsDR | varchar |  | FK | SI | Presion Arterial Sistólica (mmHg) DR |
| QREEDP | varchar |  |  | SI | Resultado EEDP (Sólo Lectura) |
| QRPB | varchar |  |  | SI | Resultado Pauta Breve (Sólo Lectura) |
| QRPND | varchar |  |  | SI | Resultado Protocolo Neurodesarrollo (Solo Lectura) |
| QRRMBN | varchar |  |  | SI | Riesgo de Morir por Bronconeumonía (Sólo Lectura) |
| QRRO | varchar |  |  | SI | Riesgo de Obesidad (Sólo Lectura) |
| QRTEPSI | varchar |  |  | SI | Resultado TEPSI (Sólo Lectura) |
| QSEN | varchar |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
| QTAI | varchar |  |  | SI | Tipo de Alimentación Infantil |
| QTAIObsDR | varchar |  | FK | SI | Tipo de Alimentación Infantil DR |
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