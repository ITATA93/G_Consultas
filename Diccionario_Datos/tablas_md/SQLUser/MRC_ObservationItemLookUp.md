# SQLUser.MRC_ObservationItemLookUp

**Schema:** SQLUser
**Columnas:** 226
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LU_ParRef | bigint | PK |  | NO | MRC_ObservationItem Parent Reference |
| LU_AgeFromDays | integer |  |  | SI | Age From (Days) |
| LU_AgeFromMonths | integer |  |  | SI | Age From (Months) |
| LU_AgeFromYears | integer |  |  | SI | Age From (Years) |
| LU_AgeToDays | integer |  |  | SI | Age To (Days) |
| LU_AgeToMonths | integer |  |  | SI | Age To (Months) |
| LU_AgeToYears | integer |  |  | SI | Age To (Years) |
| LU_Childsub | double |  |  | NO | Childsub |
| LU_Code | varchar |  |  | SI | Code |
| LU_CreatedDate | date |  |  | SI | Created Date |
| LU_CreatedTime | time |  |  | SI | Created Time |
| LU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LU_DateFrom | date |  |  | SI | - |
| LU_DateTo | date |  |  | SI | - |
| LU_Desc | varchar |  |  | SI | Description |
| LU_DisplayWarning | varchar |  |  | SI | Display Warning |
| LU_EWSRange_DR | bigint |  | FK | SI | Des Ref MRCEWSRange   |
| LU_EarlyWarningScoringSystem | bigint |  |  | SI | Early Warning Scoring System |
| LU_OutcomeScore | numeric |  |  | SI | Score for associating with an Observation Item Loo... |
| LU_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| LU_PregnancyEvent | varchar |  |  | SI | Applies to Pregnancy Event ONLY |
| LU_RowId | varchar |  |  | NO | - |
| LU_SequenceOrder | double |  |  | SI | Sequence Order |
| LU_Sex | bigint |  |  | SI | Sex |
| LU_UpdatedDate | date |  |  | SI | Updated Date |
| LU_UpdatedTime | time |  |  | SI | Updated Time |
| LU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Motivo Consulta |
| Q02 | - |  |  | SI | Religión |
| Q03 | - |  |  | SI | Consumo de Alcohol |
| Q04 | - |  |  | SI | Tiempo de Consumo Alcohol |
| Q05 | - |  |  | SI | Tabaquismo |
| Q06 | - |  |  | SI | Cigarrillos por Día |
| Q07 | - |  |  | SI | Año de Consumo |
| Q08 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q09 | - |  |  | SI | Consumo de Drogas |
| Q10 | - |  |  | SI | Otra Droga |
| Q100 | - |  |  | SI | Paredes Vaginales |
| Q100ObsDR | - |  |  | SI | Paredes Vaginales DR |
| Q101 | - |  |  | SI | Comentario Paredes Vaginales |
| Q102 | - |  |  | SI | Características Macroscópicas del Cérvix |
| Q102ObsDR | - |  |  | SI | Características Macroscópicas del Cérvix DR |
| Q103 | - |  |  | SI | comentarios macroscópicas del cérvix |
| Q104 | - |  |  | SI | Presencia Pólipo Cervical |
| Q104ObsDR | - |  |  | SI | Presencia Pólipo Cervical DR |
| Q105 | - |  |  | SI | comentario presencia pólipo cervical |
| Q106 | - |  |  | SI | Número de Pólipos cervicales |
| Q107 | - |  |  | SI | Cantidad Flujo Vaginal |
| Q107ObsDR | - |  |  | SI | Cantidad Flujo Vaginal DR |
| Q108 | - |  |  | SI | Comentarios cantidad flujo vaginal |
| Q109 | - |  |  | SI | Consistencia Flujo Vaginal |
| Q109ObsDR | - |  |  | SI | Consistencia Flujo Vaginal DR |
| Q11 | - |  |  | SI | Discapacidad Física / Cognitiva (Vulnerabilidad) |
| Q110 | - |  |  | SI | comentario consistencia flujo vaginal |
| Q111 | - |  |  | SI | Color Flujo Vaginal |
| Q111ObsDR | - |  |  | SI | Color Flujo Vaginal DR |
| Q112 | - |  |  | SI | comentario color flujo vaginal |
| Q113 | - |  |  | SI | Olor Flujo Vaginal |
| Q113ObsDR | - |  |  | SI | Olor Flujo Vaginal DR |
| Q114 | - |  |  | SI | comentario olor flujo vaginal |
| Q115 | - |  |  | SI | Fecha PAP |
| Q115ObsDR | - |  |  | SI | Fecha PAP DR |
| Q116 | - |  |  | SI | Diagnóstico Principal PAP |
| Q116ObsDR | - |  |  | SI | Diagnóstico Principal PAP DR |
| Q116a | - |  |  | SI | Comentario diagn. principal PAP |
| Q118 | - |  |  | SI | Conclusiones |
| Q119 | - |  |  | SI | Plan de Manejo al Ingreso |
| Q12 | - |  |  | SI | Nivel de Dependencia |
| Q13 | - |  |  | SI | Nivel Educacional |
| Q14 | - |  |  | SI | Forma de Comunicación |
| Q15 | - |  |  | SI | Otra |
| Q16 | - |  |  | SI | Ocupación |
| Q17 | - |  |  | SI | Anamnesis Próxima |
| Q18 | - |  |  | SI | Gestas |
| Q19 | - |  |  | SI | N° Partos |
| Q20 | - |  |  | SI | N° Abortos |
| Q21 | - |  |  | SI | N° Hijos Vivos |
| Q22 | - |  |  | SI | N° Mortinatos |
| Q23 | - |  |  | SI | N° Vaginal |
| Q24 | - |  |  | SI | N° Cesárea |
| Q25 | - |  |  | SI | N° Fórceps |
| Q26 | - |  |  | SI | Temporalidad entre Partos Vaginales |
| Q27 | - |  |  | SI | Edad del Primer Parto (años) |
| Q28 | - |  |  | SI | Edad Menarca |
| Q29 | - |  |  | SI | Edad Menopausia |
| Q30 | - |  |  | SI | Terapia de Reemplazo Hormonal |
| Q31 | - |  |  | SI | Ciclo |
| Q32 | - |  |  | SI | Frecuencia del ciclo (dias) |
| Q33 | - |  |  | SI | Duración |
| Q34 | - |  |  | SI | FUR |
| Q35 | - |  |  | SI | Alteración Intervalo/Duración |
| Q36 | - |  |  | SI | Alteración de la Cantidad |
| Q37 | - |  |  | SI | Otras Alteraciones |
| Q38 | - |  |  | SI | Desea agregar observaciones (Ciclo Menstrual) |
| Q38a | - |  |  | SI | Observaciones Ciclo Menstrual |
| Q39 | - |  |  | SI | Edad Inicio |
| Q40 | - |  |  | SI | Número de parejas sexuales |
| Q41 | - |  |  | SI | Actividad Actual |
| Q42 | - |  |  | SI | Método Anticonceptivo |
| Q43 | - |  |  | SI | Conducta sexual de riesgo |
| Q44 | - |  |  | SI | ¿Desea agregar observaciones? |
| Q45 | - |  |  | SI | Observaciones Actividad Sexual |
| Q47 | - |  |  | SI | Fecha último PAP |
| Q48 | - |  |  | SI | Resultado PAP |
| Q49 | - |  |  | SI | ¿Desea agregar observaciones? |
| Q50 | - |  |  | SI | Observaciones PAP |
| Q51 | - |  |  | SI | Fecha última mamografía |
| Q52 | - |  |  | SI | Resultado Mamografía |
| Q53 | - |  |  | SI | ¿Desea agregar observaciones (mamografía)? |
| Q54 | - |  |  | SI | Observaciones Mamografía |
| Q55 | - |  |  | SI | ¿Requirió ECO Mamaria complementaria? |
| Q56 | - |  |  | SI | Estado General |
| Q57 | - |  |  | SI | Frecuencia Cardíaca |
| Q57ObsDR | - |  |  | SI | Frecuencia Cardíaca DR |
| Q58 | - |  |  | SI | P.A Sistólica |
| Q58ObsDR | - |  |  | SI | P.A Sistólica DR |
| Q59 | - |  |  | SI | P.A Diastólica |
| Q59ObsDR | - |  |  | SI | P.A Diastólica DR |
| Q60 | - |  |  | SI | Frecuencia Respiratoria |
| Q60ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q61 | - |  |  | SI | FiO2 |
| Q61ObsDR | - |  |  | SI | FiO2 DR |
| Q62 | - |  |  | SI | Sat. O2 |
| Q62ObsDR | - |  |  | SI | Sat. O2 DR |
| Q63 | - |  |  | SI | Temperatura Axilar |
| Q63ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q64 | - |  |  | SI | Peso |
| Q64ObsDR | - |  |  | SI | Peso DR |
| Q65 | - |  |  | SI | Talla |
| Q65ObsDR | - |  |  | SI | Talla DR |
| Q66 | - |  |  | SI | Hemoglucotest |
| Q66ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q67 | - |  |  | SI | Valoración del dolor |
| Q68 | - |  |  | SI | Escala de dolor (EVA) |
| Q69 | - |  |  | SI | Ubicación dolor |
| Q70 | - |  |  | SI | Razones para no evaluar dolor |
| Q71 | - |  |  | SI | Especifique otra razón |
| Q72 | - |  |  | SI | Comentarios Examen Físico General |
| Q73 | - |  |  | SI | Mamas |
| Q73ObsDR | - |  |  | SI | Mamas DR |
| Q74 | - |  |  | SI | Comentarios Mama |
| Q75 | - |  |  | SI | Sintomatología Mama |
| Q75ObsDR | - |  |  | SI | Sintomatología Mama DR |
| Q76 | - |  |  | SI | Comentario sintomatología mama |
| Q77 | - |  |  | SI | Evaluación Tamaño Mama |
| Q77ObsDR | - |  |  | SI | Evaluación Tamaño Mama DR |
| Q78 | - |  |  | SI | comentario tamaño mama |
| Q79 | - |  |  | SI | Simetría Mamas |
| Q79ObsDR | - |  |  | SI | Simetría Mamas DR |
| Q80 | - |  |  | SI | Comentario simetría mamas |
| Q81 | - |  |  | SI | Otras Alteraciones mamas |
| Q81ObsDR | - |  |  | SI | Otras Alteraciones mamas DR |
| Q81a | - |  |  | SI | otras alteraciones mamas |
| Q82 | - |  |  | SI | Pezón |
| Q82ObsDR | - |  |  | SI | Pezón DR |
| Q83 | - |  |  | SI | comentario pezón |
| Q84 | - |  |  | SI | Fecha Mamografía |
| Q84ObsDR | - |  |  | SI | Fecha Mamografía DR |
| Q85 | - |  |  | SI | Mamografía |
| Q85ObsDR | - |  |  | SI | Mamografía DR |
| Q85a | - |  |  | SI | comentario mamografía |
| Q86 | - |  |  | SI | Inspección Genital |
| Q86ObsDR | - |  |  | SI | Inspección Genital DR |
| Q86a | - |  |  | SI | Comentario inspección genital |
| Q87 | - |  |  | SI | Glándula de Bartolino |
| Q87ObsDR | - |  |  | SI | Glándula de Bartolino DR |
| Q87a | - |  |  | SI | Comentario Glándula de Bartolino |
| Q88 | - |  |  | SI | Ubicación del Cuerpo Uterino |
| Q88ObsDR | - |  |  | SI | Ubicación del Cuerpo Uterino DR |
| Q88a | - |  |  | SI | comentario ubicación del cuerpo uterino |
| Q89 | - |  |  | SI | Dolor de la movilización cuerpo uterino |
| Q89ObsDR | - |  |  | SI | Dolor de la movilización cuerpo uterino DR |
| Q90 | - |  |  | SI | comentario dolor de movilización cuerpo uterino |
| Q91 | - |  |  | SI | Consistencia Pared Uterina |
| Q91ObsDR | - |  |  | SI | Consistencia Pared Uterina DR |
| Q92 | - |  |  | SI | comentario consitencia pared uterina |
| Q93 | - |  |  | SI | Saco de Douglas |
| Q93ObsDR | - |  |  | SI | Saco de Douglas DR |
| Q94 | - |  |  | SI | comentario saco de douglas |
| Q95 | - |  |  | SI | Alteraciones Mucosa Vaginal |
| Q95ObsDR | - |  |  | SI | Alteraciones Mucosa Vaginal DR |
| Q96 | - |  |  | SI | comentario alteraciones mucosa vaginal |
| Q97 | - |  |  | SI | Presencia de Masa |
| Q97ObsDR | - |  |  | SI | Presencia de Masa DR |
| Q98 | - |  |  | SI | comentario presencia de masa |
| Q99 | - |  |  | SI | Descripción Ubicación y Tamaño Masa |
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