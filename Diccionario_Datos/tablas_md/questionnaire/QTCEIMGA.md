# questionnaire.QTCEIMGA

> Ingreso Matrón(a) Ginecología Ambulatorio

**Schema:** questionnaire
**Columnas:** 200
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Matrón(a) Ginecología Ambulatorio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Motivo Consulta |
| Q02 | varchar |  |  | SI | Religión |
| Q03 | varchar |  |  | SI | Consumo de Alcohol |
| Q04 | varchar |  |  | SI | Tiempo de Consumo Alcohol |
| Q05 | varchar |  |  | SI | Tabaquismo |
| Q06 | numeric |  |  | SI | Cigarrillos por Día |
| Q07 | numeric |  |  | SI | Año de Consumo |
| Q08 | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q09 | varchar |  |  | SI | Consumo de Drogas |
| Q10 | varchar |  |  | SI | Otra Droga |
| Q100 | varchar |  |  | SI | Paredes Vaginales |
| Q100ObsDR | varchar |  | FK | SI | Paredes Vaginales DR |
| Q101 | varchar |  |  | SI | Comentario Paredes Vaginales |
| Q102 | varchar |  |  | SI | Características Macroscópicas del Cérvix |
| Q102ObsDR | varchar |  | FK | SI | Características Macroscópicas del Cérvix DR |
| Q103 | varchar |  |  | SI | comentarios macroscópicas del cérvix |
| Q104 | varchar |  |  | SI | Presencia Pólipo Cervical |
| Q104ObsDR | varchar |  | FK | SI | Presencia Pólipo Cervical DR |
| Q105 | varchar |  |  | SI | comentario presencia pólipo cervical |
| Q106 | numeric |  |  | SI | Número de Pólipos cervicales |
| Q107 | varchar |  |  | SI | Cantidad Flujo Vaginal |
| Q107ObsDR | varchar |  | FK | SI | Cantidad Flujo Vaginal DR |
| Q108 | varchar |  |  | SI | Comentarios cantidad flujo vaginal |
| Q109 | varchar |  |  | SI | Consistencia Flujo Vaginal |
| Q109ObsDR | varchar |  | FK | SI | Consistencia Flujo Vaginal DR |
| Q11 | varchar |  |  | SI | Discapacidad Física / Cognitiva (Vulnerabilidad) |
| Q110 | varchar |  |  | SI | comentario consistencia flujo vaginal |
| Q111 | varchar |  |  | SI | Color Flujo Vaginal |
| Q111ObsDR | varchar |  | FK | SI | Color Flujo Vaginal DR |
| Q112 | varchar |  |  | SI | comentario color flujo vaginal |
| Q113 | varchar |  |  | SI | Olor Flujo Vaginal |
| Q113ObsDR | varchar |  | FK | SI | Olor Flujo Vaginal DR |
| Q114 | varchar |  |  | SI | comentario olor flujo vaginal |
| Q115 | varchar |  |  | SI | Fecha PAP |
| Q115ObsDR | varchar |  | FK | SI | Fecha PAP DR |
| Q116 | varchar |  |  | SI | Diagnóstico Principal PAP |
| Q116ObsDR | varchar |  | FK | SI | Diagnóstico Principal PAP DR |
| Q116a | varchar |  |  | SI | Comentario diagn. principal PAP |
| Q118 | varchar |  |  | SI | Conclusiones  |
| Q119 | varchar |  |  | SI | Plan de Manejo al Ingreso |
| Q12 | varchar |  |  | SI | Nivel de Dependencia |
| Q13 | varchar |  |  | SI | Nivel Educacional |
| Q14 | varchar |  |  | SI | Forma de Comunicación |
| Q15 | varchar |  |  | SI | Otra |
| Q16 | varchar |  |  | SI | Ocupación |
| Q17 | varchar |  |  | SI | Anamnesis Próxima |
| Q18 | numeric |  |  | SI | Gestas |
| Q19 | numeric |  |  | SI | N° Partos |
| Q20 | numeric |  |  | SI | N° Abortos |
| Q21 | numeric |  |  | SI | N° Hijos Vivos |
| Q22 | numeric |  |  | SI | N° Mortinatos |
| Q23 | numeric |  |  | SI | N° Vaginal |
| Q24 | numeric |  |  | SI | N° Cesárea |
| Q25 | numeric |  |  | SI | N° Fórceps |
| Q26 | varchar |  |  | SI | Temporalidad entre Partos Vaginales |
| Q27 | varchar |  |  | SI | Edad del Primer Parto (años) |
| Q28 | numeric |  |  | SI | Edad Menarca |
| Q29 | numeric |  |  | SI | Edad Menopausia |
| Q30 | varchar |  |  | SI | Terapia de Reemplazo Hormonal |
| Q31 | varchar |  |  | SI | Ciclo |
| Q32 | numeric |  |  | SI | Frecuencia del ciclo (dias) |
| Q33 | numeric |  |  | SI | Duración |
| Q34 | date |  |  | SI | FUR |
| Q35 | varchar |  |  | SI | Alteración Intervalo/Duración |
| Q36 | varchar |  |  | SI | Alteración de la Cantidad |
| Q37 | varchar |  |  | SI | Otras Alteraciones |
| Q38 | varchar |  |  | SI | Desea agregar observaciones (Ciclo Menstrual) |
| Q38a | varchar |  |  | SI | Observaciones Ciclo Menstrual |
| Q39 | numeric |  |  | SI | Edad Inicio |
| Q40 | numeric |  |  | SI | Número de parejas sexuales |
| Q41 | varchar |  |  | SI | Actividad Actual |
| Q42 | varchar |  |  | SI | Método Anticonceptivo |
| Q43 | varchar |  |  | SI | Conducta sexual de riesgo |
| Q44 | varchar |  |  | SI | ¿Desea agregar observaciones? |
| Q45 | varchar |  |  | SI | Observaciones Actividad Sexual |
| Q47 | date |  |  | SI | Fecha último PAP |
| Q48 | varchar |  |  | SI | Resultado PAP |
| Q49 | varchar |  |  | SI | ¿Desea agregar observaciones? |
| Q50 | varchar |  |  | SI | Observaciones PAP |
| Q51 | date |  |  | SI | Fecha última mamografía |
| Q52 | varchar |  |  | SI | Resultado Mamografía |
| Q53 | varchar |  |  | SI | ¿Desea agregar observaciones (mamografía)? |
| Q54 | varchar |  |  | SI | Observaciones Mamografía |
| Q55 | varchar |  |  | SI | ¿Requirió ECO Mamaria complementaria? |
| Q56 | varchar |  |  | SI | Estado General |
| Q57 | varchar |  |  | SI | Frecuencia Cardíaca |
| Q57ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca DR |
| Q58 | varchar |  |  | SI | P.A Sistólica |
| Q58ObsDR | varchar |  | FK | SI | P.A Sistólica DR |
| Q59 | varchar |  |  | SI | P.A Diastólica |
| Q59ObsDR | varchar |  | FK | SI | P.A Diastólica DR |
| Q60 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q60ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q61 | varchar |  |  | SI | FiO2 |
| Q61ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q62 | varchar |  |  | SI | Sat. O2 |
| Q62ObsDR | varchar |  | FK | SI | Sat. O2 DR |
| Q63 | varchar |  |  | SI | Temperatura Axilar |
| Q63ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q64 | varchar |  |  | SI | Peso |
| Q64ObsDR | varchar |  | FK | SI | Peso DR |
| Q65 | varchar |  |  | SI | Talla |
| Q65ObsDR | varchar |  | FK | SI | Talla DR |
| Q66 | varchar |  |  | SI | Hemoglucotest |
| Q66ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q67 | varchar |  |  | SI | Valoración del dolor |
| Q68 | varchar |  |  | SI | Escala de dolor (EVA) |
| Q69 | varchar |  |  | SI | Ubicación dolor |
| Q70 | varchar |  |  | SI | Razones para no evaluar dolor |
| Q71 | varchar |  |  | SI | Especifique otra razón |
| Q72 | varchar |  |  | SI | Comentarios Examen Físico General |
| Q73 | varchar |  |  | SI | Mamas |
| Q73ObsDR | varchar |  | FK | SI | Mamas DR |
| Q74 | varchar |  |  | SI | Comentarios Mama |
| Q75 | varchar |  |  | SI | Sintomatología Mama |
| Q75ObsDR | varchar |  | FK | SI | Sintomatología Mama DR |
| Q76 | varchar |  |  | SI | Comentario sintomatología mama |
| Q77 | varchar |  |  | SI | Evaluación Tamaño Mama |
| Q77ObsDR | varchar |  | FK | SI | Evaluación Tamaño Mama DR |
| Q78 | varchar |  |  | SI | comentario tamaño mama |
| Q79 | varchar |  |  | SI | Simetría Mamas |
| Q79ObsDR | varchar |  | FK | SI | Simetría Mamas DR |
| Q80 | varchar |  |  | SI | Comentario simetría mamas |
| Q81 | varchar |  |  | SI | Otras Alteraciones mamas |
| Q81ObsDR | varchar |  | FK | SI | Otras Alteraciones mamas DR |
| Q81a | varchar |  |  | SI | otras alteraciones mamas |
| Q82 | varchar |  |  | SI | Pezón |
| Q82ObsDR | varchar |  | FK | SI | Pezón DR |
| Q83 | varchar |  |  | SI | comentario pezón |
| Q84 | varchar |  |  | SI | Fecha Mamografía |
| Q84ObsDR | varchar |  | FK | SI | Fecha Mamografía DR |
| Q85 | varchar |  |  | SI | Mamografía |
| Q85ObsDR | varchar |  | FK | SI | Mamografía DR |
| Q85a | varchar |  |  | SI | comentario mamografía |
| Q86 | varchar |  |  | SI | Inspección Genital |
| Q86ObsDR | varchar |  | FK | SI | Inspección Genital DR |
| Q86a | varchar |  |  | SI | Comentario inspección genital |
| Q87 | varchar |  |  | SI | Glándula de Bartolino |
| Q87ObsDR | varchar |  | FK | SI | Glándula de Bartolino DR |
| Q87a | varchar |  |  | SI | Comentario Glándula de Bartolino |
| Q88 | varchar |  |  | SI | Ubicación del Cuerpo Uterino |
| Q88ObsDR | varchar |  | FK | SI | Ubicación del Cuerpo Uterino DR |
| Q88a | varchar |  |  | SI | comentario ubicación del cuerpo uterino |
| Q89 | varchar |  |  | SI | Dolor de la movilización cuerpo uterino |
| Q89ObsDR | varchar |  | FK | SI | Dolor de la movilización cuerpo uterino DR |
| Q90 | varchar |  |  | SI | comentario dolor de movilización cuerpo uterino |
| Q91 | varchar |  |  | SI | Consistencia Pared Uterina |
| Q91ObsDR | varchar |  | FK | SI | Consistencia Pared Uterina DR |
| Q92 | varchar |  |  | SI | comentario consitencia pared uterina |
| Q93 | varchar |  |  | SI | Saco de Douglas |
| Q93ObsDR | varchar |  | FK | SI | Saco de Douglas DR |
| Q94 | varchar |  |  | SI | comentario saco de douglas |
| Q95 | varchar |  |  | SI | Alteraciones Mucosa Vaginal |
| Q95ObsDR | varchar |  | FK | SI | Alteraciones Mucosa Vaginal DR |
| Q96 | varchar |  |  | SI | comentario alteraciones mucosa vaginal |
| Q97 | varchar |  |  | SI | Presencia de Masa |
| Q97ObsDR | varchar |  | FK | SI | Presencia de Masa DR |
| Q98 | varchar |  |  | SI | comentario presencia de masa |
| Q99 | varchar |  |  | SI | Descripción Ubicación y Tamaño Masa |
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