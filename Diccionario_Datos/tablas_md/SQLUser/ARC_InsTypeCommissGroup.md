# SQLUser.ARC_InsTypeCommissGroup

**Schema:** SQLUser
**Columnas:** 201
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMGRP_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| COMGRP_Childsub | double |  |  | NO | Childsub |
| COMGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMGRP_CreatedDate | date |  |  | SI | Created Date |
| COMGRP_CreatedTime | time |  |  | SI | Created Time |
| COMGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMGRP_InsuranceType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| COMGRP_NationalCode | varchar |  |  | SI | National code |
| COMGRP_RowId | varchar |  |  | NO | - |
| COMGRP_UpdatedDate | date |  |  | SI | Updated Date |
| COMGRP_UpdatedTime | time |  |  | SI | Updated Time |
| COMGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ35DR | - |  |  | SI | Child Reference: Pulmonar |
| Q100 | - |  |  | SI | Pelvis osea normal |
| Q101 | - |  |  | SI | Útero en conformedad con el estagio del embarazo |
| Q102 | - |  |  | SI | Labios mayores y menores de tamaño y aspecto norma... |
| Q103 | - |  |  | SI | Clítoris de tamaño y aspecto normal. |
| Q104 | - |  |  | SI | Glándulas de Bartholino normales. |
| Q105 | - |  |  | SI | Paredes vaginales elásticas. Mucosa vaginal normal... |
| Q106 | - |  |  | SI | Saco de Douglas libre. |
| Q107 | - |  |  | SI | Cuello uterino de consistencia y tamaño normal. |
| Q108 | - |  |  | SI | Útero en anteroversión, de tamaño y consistencia n... |
| Q109 | - |  |  | SI | Flujo vaginal normal. |
| Q110 | - |  |  | SI | Anexos libres e indoloros. |
| Q111 | - |  |  | SI | Parametrios normales. |
| Q112 | - |  |  | SI | Vagina de elasticidad conservada. |
| Q113 | - |  |  | SI | Cuello central de coloración normal, sin lesiones ... |
| Q114 | - |  |  | SI | Mamas de tamaño y desarrollo normal, simétricas. |
| Q115 | - |  |  | SI | No se palpan masas ni adenopatías locales. |
| Q116 | - |  |  | SI | Pezones sin lesiones ni secreción anormal. |
| Q117 | - |  |  | SI | Inspección |
| Q118 | - |  |  | SI | Tacto vaginal |
| Q119 | - |  |  | SI | Especuloscopía |
| Q120 | - |  |  | SI | Ex. mamas |
| Q121 | - |  |  | SI | LCF Feto 1 (lpm) |
| Q121ObsDR | - |  |  | SI | LCF Feto 1 (lpm) DR |
| Q122 | - |  |  | SI | LCF Feto 2 (lpm) |
| Q122ObsDR | - |  |  | SI | LCF Feto 2 (lpm) DR |
| Q123 | - |  |  | SI | LCF Feto 3 (lpm) |
| Q123ObsDR | - |  |  | SI | LCF Feto 3 (lpm) DR |
| Q124 | - |  |  | SI | Movimientos fetales |
| Q124ObsDR | - |  |  | SI | Movimientos fetales DR |
| Q125 | - |  |  | SI | Presentación |
| Q125ObsDR | - |  |  | SI | Presentación DR |
| Q126 | - |  |  | SI | Dorso fetal |
| Q126ObsDR | - |  |  | SI | Dorso fetal DR |
| Q127 | - |  |  | SI | Plano de Hodge |
| Q127ObsDR | - |  |  | SI | Plano de Hodge DR |
| Q128 | - |  |  | SI | Altura uterina (cms.) |
| Q128ObsDR | - |  |  | SI | Altura uterina (cms.) DR |
| Q129 | - |  |  | SI | Tono uterino |
| Q129ObsDR | - |  |  | SI | Tono uterino DR |
| Q130 | - |  |  | SI | Dinámica uterina |
| Q130ObsDR | - |  |  | SI | Dinámica uterina DR |
| Q131 | - |  |  | SI | Contracciones (cada 10 min) |
| Q131ObsDR | - |  |  | SI | Contracciones (cada 10 min) DR |
| Q132 | - |  |  | SI | Desaceleraciones |
| Q132ObsDR | - |  |  | SI | Desaceleraciones DR |
| Q133 | - |  |  | SI | Líquido amniótico |
| Q133ObsDR | - |  |  | SI | Líquido amniótico DR |
| Q134 | - |  |  | SI | Flujo vaginal |
| Q134ObsDR | - |  |  | SI | Flujo vaginal DR |
| Q135 | - |  |  | SI | Membranas |
| Q135ObsDR | - |  |  | SI | Membranas DR |
| Q136 | - |  |  | SI | Consistencia cuello |
| Q136ObsDR | - |  |  | SI | Consistencia cuello DR |
| Q137 | - |  |  | SI | Posición |
| Q137ObsDR | - |  |  | SI | Posición DR |
| Q138 | - |  |  | SI | Borramiento |
| Q138ObsDR | - |  |  | SI | Borramiento DR |
| Q139 | - |  |  | SI | Dilatación cervical |
| Q139ObsDR | - |  |  | SI | Dilatación cervical DR |
| Q140 | - |  |  | SI | Comentarios examen obstétrico |
| Q141 | - |  |  | SI | Comentario Examen Ginecológico |
| Q19 | - |  |  | SI | P. Arterial Sistólica |
| Q19ObsDR | - |  |  | SI | P. Arterial Sistólica DR |
| Q20 | - |  |  | SI | P. Arterial Diastólica |
| Q20ObsDR | - |  |  | SI | P. Arterial Diastólica DR |
| Q21 | - |  |  | SI | Frecuencia cardíaca |
| Q21ObsDR | - |  |  | SI | Frecuencia cardíaca DR |
| Q22 | - |  |  | SI | Frecuencia Respiratoria |
| Q22ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q23 | - |  |  | SI | Temperatura axilar |
| Q23ObsDR | - |  |  | SI | Temperatura axilar DR |
| Q24 | - |  |  | SI | Saturación O2 (%) |
| Q24ObsDR | - |  |  | SI | Saturación O2 (%) DR |
| Q25 | - |  |  | SI | FiO2 (%) |
| Q25ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q26 | - |  |  | SI | Escala de dolor (EVA) |
| Q26ObsDR | - |  |  | SI | Escala de dolor (EVA) DR |
| Q27 | - |  |  | SI | Cabeza normal. Yugulares no ingurgitadas, pulso ca... |
| Q28 | - |  |  | SI | Cabeza y cuello |
| Q29 | - |  |  | SI | Descripción, cabeza y cuello |
| Q30 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q31 | - |  |  | SI | Auscultación |
| Q32 | - |  |  | SI | Descripción, cardiovascular |
| Q33 | - |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q34 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q36 | - |  |  | SI | Resto del examen realizado sin alteraciones |
| Q37 | - |  |  | SI | Murmullo pulmonar simétrico normal, sin ruidos agr... |
| Q38 | - |  |  | SI | Descripción, pulmonar |
| Q40 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q41 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q42 | - |  |  | SI | Descripción, abdomen |
| Q43 | - |  |  | SI | Mamas normales, axilas libres de empastamientos o ... |
| Q44 | - |  |  | SI | Descripción examen ginecológico |
| Q47 | - |  |  | SI | Extremidades normales, sin lesiones. Edema (-). Ar... |
| Q48 | - |  |  | SI | Descripción, extremidades |
| Q49 | - |  |  | SI | Exámenes de laboratorio |
| Q50 | - |  |  | SI | Exámenes de imagenología |
| Q51 | - |  |  | SI | Conclusión |
| Q52 | - |  |  | SI | Plan al Ingreso |
| Q53 | - |  |  | SI | Profesional de salud |
| Q54 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q55 | - |  |  | SI | Descripción examen físico general |
| Q56 | - |  |  | SI | Pulsos simétricos, amplitud normal. |
| Q57 | - |  |  | SI | Descripción Examen físico simple |
| Q58 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q59 | - |  |  | SI | Menarquia |
| Q60 | - |  |  | SI | Caracterísiticas del ciclo |
| Q61 | - |  |  | SI | Alteración Intervalo / Duración |
| Q62 | - |  |  | SI | FERTILIDAD |
| Q63 | - |  |  | SI | Edad menopausia (si corresponde) |
| Q65 | - |  |  | SI | BIOPSIAS |
| Q66 | - |  |  | SI | CIRUGÍAS |
| Q67 | - |  |  | SI | PRÁCTICAS PREVENTIVAS |
| Q68 | - |  |  | SI | FECHA DE LA ÚLTIMA REGLA - FUR |
| Q69 | - |  |  | SI | CRITERIO PARA DETERMINAR FUR |
| Q70 | - |  |  | SI | NÚMERO DE FETOS |
| Q71 | - |  |  | SI | EXÁMENES EN EL PRIMER TRIMESTRE |
| Q72 | - |  |  | SI | EXÁMENES EN EL SEGUNDO TRIMESTRE |
| Q73 | - |  |  | SI | EXÁMENES EN EL TERCER TRIMESTRE |
| Q74 | - |  |  | SI | COLO UTERINO(imagen) |
| Q75 | - |  |  | SI | COMPLICACIONES MATERNAS EN EL EMBARAZO |
| Q76 | - |  |  | SI | COMPLICACIONES FETALES |
| Q77 | - |  |  | SI | DESCRIPCIÓN DEL EXAMEN OBSTÉTRICO |
| Q78 | - |  |  | SI | Vulva normal, región inguinal sin adenopatias |
| Q79 | - |  |  | SI | Vagina elástica, residuo normal |
| Q80 | - |  |  | SI | Cuello uterino íntegro, bien epitelizado |
| Q81 | - |  |  | SI | Útero y anexos de tamaño y mobilidad normales. |
| Q83 | - |  |  | SI | RESIDUO VAGINAL |
| Q84 | - |  |  | SI | DESCRIPCIÓN DEL EXAMEN GINECOLÓGICO |
| Q85 | - |  |  | SI | TACTO VAGINAL |
| Q86 | - |  |  | SI | SUSTENTACIÓN |
| Q87 | - |  |  | SI | Resto del examen obstétrico realizado, sin alterac... |
| Q88 | - |  |  | SI | Resto del examen ginecológico realizado, sin alter... |
| Q89 | - |  |  | SI | Resto des examen respiratorio realizado, sin alter... |
| Q90 | - |  |  | SI | Vulva y Vagina |
| Q91 | - |  |  | SI | Pelvis ósea |
| Q92 | - |  |  | SI | Dilatación del cuello |
| Q92ObsDR | - |  |  | SI | Dilatación del cuello DR |
| Q93 | - |  |  | SI | Bishop |
| Q93ObsDR | - |  |  | SI | Bishop DR |
| Q94 | - |  |  | SI | Plan de De Lee |
| Q94ObsDR | - |  |  | SI | Plan de De Lee DR |
| Q95 | - |  |  | SI | Presentación |
| Q96 | - |  |  | SI | Latidos cardiacos fetales |
| Q96ObsDR | - |  |  | SI | Latidos cardiacos fetales DR |
| Q97 | - |  |  | SI | Reactividad LCF |
| Q98 | - |  |  | SI | Descripción |
| Q99 | - |  |  | SI | Vulva normal, vagina amplia y elástica. Residuo no... |
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