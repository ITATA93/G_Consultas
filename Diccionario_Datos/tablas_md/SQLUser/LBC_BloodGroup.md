# SQLUser.LBC_BloodGroup

**Schema:** SQLUser
**Columnas:** 203
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBG_RowID | bigint | PK |  | NO | - |
| CQ65 | - |  |  | SI | (null) |
| CQ69 | - |  |  | SI | (null) |
| CQ77 | - |  |  | SI | (null) |
| CQ79 | - |  |  | SI | (null) |
| CQNN024 | - |  |  | SI | (null) |
| CQNN027 | - |  |  | SI | (null) |
| CQNN033 | - |  |  | SI | (null) |
| CQNN034 | - |  |  | SI | (null) |
| CQNN038 | - |  |  | SI | (null) |
| CQNN061 | - |  |  | SI | (null) |
| CQNN062 | - |  |  | SI | (null) |
| CQREEDP | - |  |  | SI | (null) |
| CQRPB | - |  |  | SI | (null) |
| CQRPND | - |  |  | SI | (null) |
| CQRRMBN | - |  |  | SI | (null) |
| CQRRO | - |  |  | SI | (null) |
| CQRTEPSI | - |  |  | SI | (null) |
| CQregla | - |  |  | SI | (null) |
| LBCBG_BloodType_DR | bigint |  | FK | SI | Blood Type |
| LBCBG_Code | varchar |  |  | NO | Code
The collation is an exception to cater for +... |
| LBCBG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCBG_CreatedDate | date |  |  | SI | Created Date |
| LBCBG_CreatedTime | time |  |  | SI | Created Time |
| LBCBG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBG_DateTo | date |  |  | SI | Last day the record is active |
| LBCBG_Desc | varchar |  |  | NO | Description
The collation is an exception to cate... |
| LBCBG_Owner | varchar |  |  | SI | Owner |
| LBCBG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCBG_Usage | varchar |  |  | NO | Blood Group Usage |
| Q63 | - |  |  | SI | Entrega de Material Educativo |
| Q64 | - |  |  | SI | Entrega de Material Educativo (Txt) |
| Q65 | - |  |  | SI | El Niño o Niña vive con: |
| Q67 | - |  |  | SI | Tipo Discapacidad Madre |
| Q68 | - |  |  | SI | ¿El niño o niña está afectado por alguna discapaci... |
| Q69 | - |  |  | SI | El Niño/a está afectado por alguna condición que i... |
| Q70 | - |  |  | SI | Hijo/a de madre con adicción a las drogas, y/o alc... |
| Q71 | - |  |  | SI | Niño/a afectado/a por maltrato infantil |
| Q72 | - |  |  | SI | Niño/a afectado/a por malformaciones congénitas |
| Q73 | - |  |  | SI | Niño/a afectado/a por enfermedad crónica |
| Q74 | - |  |  | SI | Otro (especifique cual) |
| Q75 | - |  |  | SI | ¿Asiste el niño/a a una sala cuna o jardín infanti... |
| Q76 | - |  |  | SI | ¿Está de acuerdo con integrarse a Visitas Domicili... |
| Q77 | - |  |  | SI | ¿Quién acompaña al niño/a en la atención? |
| Q78 | - |  |  | SI | Otro (Especificar) |
| Q79 | - |  |  | SI | La Madre o cuidador principal ¿Presenta alguna dis... |
| Q80 | - |  |  | SI | Tutor |
| Q88 | - |  |  | SI | ¿Existe otra situación de vulnerabilidad distinta ... |
| Q89 | - |  |  | SI | Otra situación de vulnerabilidad |
| Q90 | - |  |  | SI | Fecha de Egreso de Hospitalización |
| Q92 | - |  |  | SI | ¿Existe otra situación de vulnerabilidad distinta ... |
| QEC | - |  |  | SI | Edad Corregida |
| QECObsDR | - |  |  | SI | Edad Corregida DR |
| QENI | - |  |  | SI | Estado Nutricional Infantil |
| QENIObsDR | - |  |  | SI | Estado Nutricional Infantil DR |
| QEX1 | - |  |  | SI | Cabeza |
| QEX10 | - |  |  | SI | Comentario General |
| QEX11 | - |  |  | SI | Con Observación de Alerta |
| QEX2 | - |  |  | SI | Cuello |
| QEX3 | - |  |  | SI | Tórax |
| QEX4 | - |  |  | SI | Exámen Cardiaco |
| QEX5 | - |  |  | SI | Exámen Pulmonar |
| QEX6 | - |  |  | SI | Abdomen |
| QEX7 | - |  |  | SI | Exámen Genital |
| QEX8 | - |  |  | SI | Columna |
| QEX9 | - |  |  | SI | Extremidades |
| QIIM | - |  |  | SI | Ingresar Información Manualmente |
| QNN001 | - |  |  | SI | ¿Embarazo Controlado? |
| QNN002 | - |  |  | SI | ¿Patología durante el embarazo? |
| QNN003 | - |  |  | SI | Especificar ¿cuáles? |
| QNN005 | - |  |  | SI | Especificar lugar del parto |
| QNN006 | - |  |  | SI | Tipo de Parto |
| QNN007 | - |  |  | SI | ¿Estuvo presente el padre en el parto? |
| QNN008 | - |  |  | SI | Edad Gestacional al Nacer |
| QNN008ObsDR | - |  |  | SI | Edad Gestacional al Nacer DR |
| QNN009 | - |  |  | SI | Relación Peso/Edad Nacimiento |
| QNN009ObsDR | - |  |  | SI | Relación Peso/Edad Nacimiento DR |
| QNN010 | - |  |  | SI | Peso al Nacer |
| QNN010ObsDR | - |  |  | SI | Peso al Nacer DR |
| QNN011 | - |  |  | SI | Talla al Nacer |
| QNN011ObsDR | - |  |  | SI | Talla al Nacer DR |
| QNN012 | - |  |  | SI | Perímetro Craneano al Nacer |
| QNN012ObsDR | - |  |  | SI | Perímetro Craneano al Nacer DR |
| QNN013 | - |  |  | SI | APGAR 1 Minuto |
| QNN014 | - |  |  | SI | APGAR 5 Minutos |
| QNN015 | - |  |  | SI | Fecha resultado fenilcetonuria e hipertiroidismo c... |
| QNN016 | - |  |  | SI | Resultado fenilcetonuria |
| QNN017 | - |  |  | SI | Resultado hipotiroidismo congénito |
| QNN018 | - |  |  | SI | Fecha vacuna BCG |
| QNN019 | - |  |  | SI | Índice de masa corporal (IMC) |
| QNN020 | - |  |  | SI | Hospitalización |
| QNN021 | - |  |  | SI | Motivo(s) de Hospitalización |
| QNN022 | - |  |  | SI | Peso (Kg) |
| QNN022ObsDR | - |  |  | SI | Peso (Kg) DR |
| QNN023 | - |  |  | SI | Talla (Cms) |
| QNN023ObsDR | - |  |  | SI | Talla (Cms) DR |
| QNN024 | - |  |  | SI | Estadio de Tanner |
| QNN026 | - |  |  | SI | Perímetro craneano |
| QNN026ObsDR | - |  |  | SI | Perímetro craneano DR |
| QNN027 | - |  |  | SI | Percentil perímetro craneano |
| QNN028 | - |  |  | SI | Fontanela Diametro |
| QNN0281 | - |  |  | SI | Fontanela Palpación |
| QNN029 | - |  |  | SI | Peso/Edad |
| QNN029ObsDR | - |  |  | SI | Peso/Edad DR |
| QNN030 | - |  |  | SI | Peso/Talla |
| QNN030ObsDR | - |  |  | SI | Peso/Talla DR |
| QNN031 | - |  |  | SI | Talla/Edad |
| QNN031ObsDR | - |  |  | SI | Talla/Edad DR |
| QNN033 | - |  |  | SI | Calificación estado nutricional según IMC |
| QNN034 | - |  |  | SI | Diagnóstico nutricional integrado |
| QNN035 | - |  |  | SI | Presión arterial(mmHg) |
| QNN036 | - |  |  | SI | Clasificación  por percentil  presión arterial sis... |
| QNN037 | - |  |  | SI | Clasificación percentil presión arterial diastólic... |
| QNN038 | - |  |  | SI | Tipo de alimentación (Antiguo) |
| QNN039 | - |  |  | SI | Detalle de alimentación (otras comidas) |
| QNN040 | - |  |  | SI | Tiempo de lactancia materna exclusiva(meses) |
| QNN043 | - |  |  | SI | ¿Se entregó guía anticipatoria de prevención de ac... |
| QNN044 | - |  |  | SI | ¿Responde al inventario de conductas en la infanci... |
| QNN054 | - |  |  | SI | Resultado Riergo Morir de Bronconeumonía |
| QNN055 | - |  |  | SI | Resultado Score Riesgo de Obesidad |
| QNN055ObsDR | - |  |  | SI | Resultado Score Riesgo de Obesidad   DR |
| QNN056 | - |  |  | SI | Resultado Escala Massie-Campbel |
| QNN056ObsDR | - |  |  | SI | Resultado Escala Massie-Campbel DR |
| QNN057 | - |  |  | SI | Resultado Escala Edimburgo |
| QNN058 | - |  |  | SI | Resultado Pauta Breve de Desarrollo Psicomotor |
| QNN058ObsDR | - |  |  | SI | Resultado Pauta Breve de Desarrollo Psicomotor DR |
| QNN059 | - |  |  | SI | Resultado EEDP |
| QNN059ObsDR | - |  |  | SI | Resultado EEDP DR |
| QNN060 | - |  |  | SI | Resultado TEPSI |
| QNN060ObsDR | - |  |  | SI | Resultado TEPSI DR |
| QNN061 | - |  |  | SI | Visión ojo derecho |
| QNN062 | - |  |  | SI | Visión ojo izquierdo |
| QNN063 | - |  |  | SI | Fecha resultado RX de pelvis |
| QNN064 | - |  |  | SI | Resultado RX de pelvis |
| QNN065 | - |  |  | SI | Diagnóstico Protocolo de Neurodesarrollo |
| QNN065ObsDR | - |  |  | SI | Diagnóstico Protocolo de Neurodesarrollo DR |
| QNN067 | - |  |  | SI | Calificación Perímetro Craneano |
| QNN090 | - |  |  | SI | Tipo de Lactancia |
| QNN090ObsDR | - |  |  | SI | Tipo de Lactancia DR |
| QNN123 | - |  |  | SI | Estado Nutricional PNAC |
| QNN123ObsDR | - |  |  | SI | Estado Nutricional PNAC DR |
| QNN124 | - |  |  | SI | Displasia Bronco-Pulmonar |
| QNN124ObsDR | - |  |  | SI | Displasia Bronco-Pulmonar DR |
| QNNA01E | - |  |  | SI | Curso [REM] |
| QPNN | - |  |  | SI | Paciente NANEAS |
| QPREDIS | - |  |  | SI | Presion Arterial Diastólica (mmHg) |
| QPREDISObsDR | - |  |  | SI | Presion Arterial Diastólica (mmHg) DR |
| QPRESIS | - |  |  | SI | Presion Arterial Sistólica (mmHg) |
| QPRESISObsDR | - |  |  | SI | Presion Arterial Sistólica (mmHg) DR |
| QREEDP | - |  |  | SI | Resultado EEDP (Sólo Lectura) |
| QRPB | - |  |  | SI | Resultado Pauta Breve (Sólo Lectura) |
| QRPND | - |  |  | SI | Resultado Protocolo Neurodesarrollo (Solo Lectura) |
| QRRMBN | - |  |  | SI | Riesgo de Morir por Bronconeumonía (Sólo Lectura) |
| QRRO | - |  |  | SI | Riesgo de Obesidad (Sólo Lectura) |
| QRTEPSI | - |  |  | SI | Resultado TEPSI (Sólo Lectura) |
| QSEN | - |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
| QTAI | - |  |  | SI | Tipo de Alimentación Infantil |
| QTAIObsDR | - |  |  | SI | Tipo de Alimentación Infantil DR |
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
| Qregla | - |  |  | SI | regla |
| ReuseDummy | varchar |  |  | SI | Reuse 1
Depricated: Availabe for Emergency Issue |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*