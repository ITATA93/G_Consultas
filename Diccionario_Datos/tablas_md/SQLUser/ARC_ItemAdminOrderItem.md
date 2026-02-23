# SQLUser.ARC_ItemAdminOrderItem

**Schema:** SQLUser
**Columnas:** 190
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMOI_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ADMOI_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ADMOI_Childsub | double |  |  | NO | Childsub |
| ADMOI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMOI_CreatedDate | date |  |  | SI | Created Date |
| ADMOI_CreatedTime | time |  |  | SI | Created Time |
| ADMOI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMOI_DateFrom | date |  |  | NO | Date From |
| ADMOI_DateTo | date |  |  | SI | Date To |
| ADMOI_EpisodeType | varchar |  |  | SI | Episode Type |
| ADMOI_MainAdmixOrdItem | varchar |  |  | SI | Main Admixture Order Item |
| ADMOI_PerQuantity | varchar |  |  | SI | Per Quantity |
| ADMOI_RowId | varchar |  |  | NO | - |
| ADMOI_UpdatedDate | date |  |  | SI | Updated Date |
| ADMOI_UpdatedTime | time |  |  | SI | Updated Time |
| ADMOI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ113DR | - |  |  | SI | Child Reference: Sensibilidad |
| Q101 | - |  |  | SI | Movimientos involuntarios anormales |
| Q102 | - |  |  | SI | Movimientos involuntarios anorm comentarios |
| Q103 | - |  |  | SI | R. Bicipital derecho |
| Q104 | - |  |  | SI | R. Bicipital Izquierdo |
| Q105 | - |  |  | SI | R. Tricipital Derecho |
| Q106 | - |  |  | SI | R. Tricipital Izquierdo |
| Q107 | - |  |  | SI | R. Rotuliano Derecho |
| Q108 | - |  |  | SI | R. Rotuliano Izquierdo |
| Q109 | - |  |  | SI | R. Tibial Posterior Derecho |
| Q110 | - |  |  | SI | R. Tibial Posterior Izquierdo |
| Q111 | - |  |  | SI | R. Plantar Derecho |
| Q112 | - |  |  | SI | R. Plantar Izquierdo |
| Q114 | - |  |  | SI | Estereognosia |
| Q115 | - |  |  | SI | Grafoestesia |
| Q116 | - |  |  | SI | Discriminación de dos puntos |
| Q117 | - |  |  | SI | Sensibilidad comentarios |
| Q118 | - |  |  | SI | Test Índice - Nariz |
| Q119 | - |  |  | SI | Test Talón - Rodilla |
| Q12 | - |  |  | SI | Presión arterial sistólica (mmHg) |
| Q120 | - |  |  | SI | Diádococinesia |
| Q121 | - |  |  | SI | Coordinación comentarios |
| Q122 | - |  |  | SI | Signos meníngeos |
| Q123 | - |  |  | SI | Signos meníngeos comentarios |
| Q124 | - |  |  | SI | Paciente vigil y atento. Orientado en tiempo y esp... |
| Q125 | - |  |  | SI | Memoria sin alteraciones. Lenguaje apropiado, norm... |
| Q126 | - |  |  | SI | Pares craneanos sin alteraciones. |
| Q127 | - |  |  | SI | Marcha normal. Musculatura de fuerza, tono y trofi... |
| Q128 | - |  |  | SI | Reflejos osteotendíneos simétricos, normales. Sin ... |
| Q129 | - |  |  | SI | Sensibilidad primaria y secundaria conservada, nor... |
| Q12ObsDR | - |  |  | SI | Presión arterial sistólica (mmHg) DR |
| Q13 | - |  |  | SI | Presión arterial diastólica (mmHg) |
| Q130 | - |  |  | SI | Coordinación motora normal. Sin signos cerebelosos... |
| Q131 | - |  |  | SI | Sin signos meníngeos al examen. |
| Q132 | - |  |  | SI | Exámenes de laboratorio |
| Q133 | - |  |  | SI | Exámenes de Rayos X |
| Q134 | - |  |  | SI | Tomografía Axial Computada (TAC) |
| Q135 | - |  |  | SI | Resonancia Nuclear Magnética (RNM) |
| Q136 | - |  |  | SI | Electroencefalograma |
| Q139 | - |  |  | SI | Profesional de Salud |
| Q13ObsDR | - |  |  | SI | Presión arterial diastólica (mmHg) DR |
| Q14 | - |  |  | SI | Saturación de O2 (%) |
| Q140 | - |  |  | SI | Escala Glasgow |
| Q141 | - |  |  | SI | Esquema Dermatomas |
| Q14ObsDR | - |  |  | SI | Saturación de O2 (%) DR |
| Q15 | - |  |  | SI | Temperatura axilar (°C) |
| Q158 | - |  |  | SI | Circunferencia Craneana |
| Q158ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q15ObsDR | - |  |  | SI | Temperatura axilar (°C) DR |
| Q16 | - |  |  | SI | Escala de dolor (EVA) |
| Q161 | - |  |  | SI | Fondo de ojo (espec) |
| Q163 | - |  |  | SI | Diploscopía |
| Q164 | - |  |  | SI | Test de Colirios |
| Q16ObsDR | - |  |  | SI | Escala de dolor (EVA) DR |
| Q17 | - |  |  | SI | Peso (kg) |
| Q17ObsDR | - |  |  | SI | Peso (kg) DR |
| Q18 | - |  |  | SI | Talla (cms.) |
| Q18ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q19 | - |  |  | SI | Frecuencia cardíaca (lpm) |
| Q19ObsDR | - |  |  | SI | Frecuencia cardíaca (lpm) DR |
| Q20 | - |  |  | SI | Frecuencia respiratoria (rpm) |
| Q20ObsDR | - |  |  | SI | Frecuencia respiratoria (rpm) DR |
| Q21 | - |  |  | SI | FIO2 (%) |
| Q21ObsDR | - |  |  | SI | FIO2 (%) DR |
| Q22 | - |  |  | SI | Examen físico general |
| Q23 | - |  |  | SI | Conciencia normal |
| Q24 | - |  |  | SI | Conciencia alterado |
| Q25 | - |  |  | SI | Conciencia no evaluado |
| Q26 | - |  |  | SI | Conciencia comentarios |
| Q27 | - |  |  | SI | Estado cuantitativo de conciencia |
| Q28 | - |  |  | SI | Estado cualitativo de conciencia |
| Q36 | - |  |  | SI | Atención normal |
| Q37 | - |  |  | SI | Atención alterado |
| Q38 | - |  |  | SI | Atención no evaluado |
| Q39 | - |  |  | SI | Atención comentarios |
| Q40 | - |  |  | SI | Orientación normal |
| Q41 | - |  |  | SI | Orientación alterado |
| Q42 | - |  |  | SI | Orientación no evaluado |
| Q43 | - |  |  | SI | Orientación comentarios |
| Q44 | - |  |  | SI | Memoria normal |
| Q45 | - |  |  | SI | Memoria alterado |
| Q46 | - |  |  | SI | Memoria no evaluado |
| Q47 | - |  |  | SI | Memoria comentarios |
| Q48 | - |  |  | SI | Lenguaje normal |
| Q49 | - |  |  | SI | Lenguaje alterado |
| Q50 | - |  |  | SI | Lenguaje no evaluado |
| Q51 | - |  |  | SI | Lenguaje comentarios |
| Q52 | - |  |  | SI | Lenguaje espontáneo |
| Q53 | - |  |  | SI | Prosodia |
| Q54 | - |  |  | SI | Comprensión |
| Q55 | - |  |  | SI | Repetición |
| Q56 | - |  |  | SI | Nominación |
| Q57 | - |  |  | SI | Lecto-escritura |
| Q58 | - |  |  | SI | Olfatorio normal |
| Q59 | - |  |  | SI | Olfatorio alterado |
| Q60 | - |  |  | SI | Olfatorio no evaluado |
| Q61 | - |  |  | SI | Olfatorio comentarios |
| Q62 | - |  |  | SI | Óptico normal |
| Q63 | - |  |  | SI | Óptico alterado |
| Q64 | - |  |  | SI | Óptico no evaluado |
| Q65 | - |  |  | SI | Óptico comentarios |
| Q66 | - |  |  | SI | Agudeza visual |
| Q67 | - |  |  | SI | Campo visual |
| Q68 | - |  |  | SI | Fondo de ojo |
| Q69 | - |  |  | SI | Oculomotor normal |
| Q70 | - |  |  | SI | Oculomotor alterado |
| Q71 | - |  |  | SI | Oculomotor no evaluado |
| Q72 | - |  |  | SI | Oculomotor comentarios |
| Q74 | - |  |  | SI | Mirada conjugada |
| Q75 | - |  |  | SI | Trigémino normal |
| Q76 | - |  |  | SI | Trigémino alterado |
| Q77 | - |  |  | SI | Trigémino no evaluado |
| Q78 | - |  |  | SI | Trigémino comentarios |
| Q79 | - |  |  | SI | Facial normal |
| Q80 | - |  |  | SI | Facial alterado |
| Q81 | - |  |  | SI | Facial no evaluado |
| Q82 | - |  |  | SI | Facial comentarios |
| Q83 | - |  |  | SI | Acústico normal |
| Q84 | - |  |  | SI | Acústico alterado |
| Q85 | - |  |  | SI | Acústico no evaluado |
| Q86 | - |  |  | SI | Acústico comentarios |
| Q87 | - |  |  | SI | Glosovago normal |
| Q88 | - |  |  | SI | Glosovago alterado |
| Q89 | - |  |  | SI | Glosovago no evaluado |
| Q90 | - |  |  | SI | Glosovago comentarios |
| Q91 | - |  |  | SI | Espinal normal |
| Q92 | - |  |  | SI | Espinal alterado |
| Q93 | - |  |  | SI | Espinal no evaluado |
| Q94 | - |  |  | SI | Espinal comentarios |
| Q95 | - |  |  | SI | Hipogloso normal |
| Q96 | - |  |  | SI | Hipogloso alterado |
| Q97 | - |  |  | SI | Hipogloso no evaluado |
| Q98 | - |  |  | SI | Hipogloso comentarios |
| Q99 | - |  |  | SI | Marcha |
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