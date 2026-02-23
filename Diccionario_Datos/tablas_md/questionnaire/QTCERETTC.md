# questionnaire.QTCERETTC

> Registro Estresante o Test de Tolerancia a las Contracciones (RE / TTC)

**Schema:** questionnaire
**Columnas:** 195
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Estresante o Test de Tolerancia a las Contracciones (RE / TTC)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Examen |
| Q02 | varchar |  |  | SI | Motivo de Evaluación |
| Q03 | varchar |  |  | SI | Otro Motivo |
| Q04 | date |  |  | SI | FUR |
| Q05 | numeric |  |  | SI | EG por FUR |
| Q06 | numeric |  |  | SI | EG por FUR |
| Q07 | numeric |  |  | SI | EG por ECO |
| Q08 | numeric |  |  | SI | EGpor ECO |
| Q100 | varchar |  |  | SI | Comentarios Desaceleraciones Precoces Gemelo V |
| Q101 | varchar |  |  | SI | Variabilidad Gemelo II |
| Q102 | varchar |  |  | SI | Aceleraciones Gemelos II |
| Q103 | varchar |  |  | SI | Desaceleraciones Tardías Gemelo II |
| Q104 | varchar |  |  | SI | Desaceleraciones Precoces Gemelo II |
| Q105 | varchar |  |  | SI | Desaceleraciones Variables Gemelo II |
| Q106 | varchar |  |  | SI | Variabilidad Gemelo III |
| Q107 | varchar |  |  | SI | Aceleraciones Gemelo III |
| Q108 | varchar |  |  | SI | Desaceleraciones Tardías Gemelo III |
| Q109 | varchar |  |  | SI | Desaceleraciones Precoces Gemelo III |
| Q110 | varchar |  |  | SI | Desaceleraciones Variables Gemelo III |
| Q111 | varchar |  |  | SI | Variabilidad Gemelo IV |
| Q112 | varchar |  |  | SI | Aceleraciones Gemelo IV |
| Q113 | varchar |  |  | SI | Desaceleraciones Tardías Gemelo IV |
| Q114 | varchar |  |  | SI | Desaceleraciones Precoces Gemelo IV |
| Q115 | varchar |  |  | SI | Desaceleraciones Variables Gemelo IV |
| Q116 | varchar |  |  | SI | Variabilidad Gemelo V |
| Q117 | varchar |  |  | SI | Aceleraciones Gemelo V |
| Q118 | varchar |  |  | SI | Desaceleraciones Tardías Gemelo V |
| Q119 | varchar |  |  | SI | Desacleraciones Precoces Gemelo V |
| Q120 | varchar |  |  | SI | Desaceleraciones Variables Gemelo V |
| Q121 | varchar |  |  | SI | Presencia de Movimientos Fetales |
| Q122 | numeric |  |  | SI | Número de Movimiento Fetales |
| Q123 | numeric |  |  | SI | Número de Movimientos Fetales Minutos |
| Q124 | varchar |  |  | SI | Interpretación |
| Q125 | varchar |  |  | SI | Comentarios / Observaciones |
| Q126 | varchar |  |  | SI | / Minutos |
| Q127 | time |  |  | SI | Hora Inicio de Goteo Oxitócico |
| Q128 | varchar |  |  | SI | Desaceleraciones  |
| Q129 | numeric |  |  | SI | N° de Desaceleraciones Totales |
| Q130 | varchar |  |  | SI | Desaceleraciones  |
| Q131 | varchar |  |  | SI | Desaceleraciones |
| Q132 | varchar |  |  | SI | Desaceleraciones  |
| Q133 | varchar |  |  | SI | Desaceleraciones  |
| Q134 | varchar |  |  | SI | Desaceleraciones  |
| Q135 | numeric |  |  | SI | N° de Desaceleraciones Totales |
| Q136 | numeric |  |  | SI | N° de Desaceleraciones Totales |
| Q137 | numeric |  |  | SI | N° de Desaceleraciones Totales |
| Q138 | numeric |  |  | SI | N° de Desaceleraciones Totales |
| Q139 | numeric |  |  | SI | N° de Desaceleraciones Totales |
| Q140 | varchar |  |  | SI | Valoración de Dolor (EVA) |
| Q141 | numeric |  |  | SI | Escala de Dolor (EVA) |
| Q142 | varchar |  |  | SI | Características del dolor |
| Q143 | varchar |  |  | SI | Localización del Dolor |
| Q144 | varchar |  |  | SI | Otro  |
| Q145 | varchar |  |  | SI | Razones para no evaluar dolor |
| Q146 | varchar |  |  | SI | Especifique |
| Q147 | numeric |  |  | SI | N° de Contracciones Uterinas al Término del Examen |
| Q148 | varchar |  |  | SI | / 10 Minutos |
| Q149 | varchar |  |  | SI | / Minutos |
| Q150 | varchar |  |  | SI | / Minutos |
| Q151 | varchar |  |  | SI | Interpretación |
| Q151ObsDR | varchar |  | FK | SI | Interpretación DR |
| Q152 | varchar |  |  | SI | Lpm |
| Q153 | varchar |  |  | SI | Lpm |
| Q154 | varchar |  |  | SI | Lpm |
| Q155 | varchar |  |  | SI | Lpm |
| Q156 | varchar |  |  | SI | Lpm |
| Q157 | varchar |  |  | SI | Lpm |
| Q158 | varchar |  |  | SI | Profesional de Salud |
| Q160 | time |  |  | SI | Hora de registro |
| Q161 | date |  |  | SI | Fecha de Registro |
| Q162 | varchar |  |  | SI | RE Negativo: Sin desaceleraciones durante el regis... |
| Q163 | varchar |  |  | SI | RE Positivo: Desaceleraciones tardías en más del 5... |
| Q164 | varchar |  |  | SI | RE Sospechoso: Desaceleraciones tardías ocasionale... |
| Q165 | varchar |  |  | SI | RE Insatisfactorio: Menos de 3 contracciones en 10... |
| Q166 | varchar |  |  | SI | RE No Interpretable: Es aquel con Hiperestimulació... |
| Q21 | varchar |  |  | SI | Valoración de Dolor (EVA) |
| Q22 | numeric |  |  | SI | Escala de Dolor (EVA) |
| Q23 | varchar |  |  | SI | Características del Dolor |
| Q24 | varchar |  |  | SI | Localización del Dolor  |
| Q25 | varchar |  |  | SI | Razones para no evaluar dolor |
| Q26 | varchar |  |  | SI | Especifique |
| Q27 | time |  |  | SI | Hora Inicio del Registro |
| Q28 | time |  |  | SI | Hora Término del Registro |
| Q29 | varchar |  |  | SI | Dinámica Uterina Previo a TTC |
| Q30 | numeric |  |  | SI | Número de Contracciones  |
| Q31 | numeric |  |  | SI | Número de Contracciones Minutos |
| Q32 | varchar |  |  | SI | Alteraciones de la Dinámica Uterina |
| Q33 | varchar |  |  | SI | Otra alteración  Texto Libre |
| Q34 | varchar |  |  | SI | Embarazo |
| Q35 | varchar |  |  | SI | Número de Fetos |
| Q36 | varchar |  |  | SI | Evaluación Fetal |
| Q37 | numeric |  |  | SI | LCF |
| Q38 | varchar |  |  | SI | Comentarios |
| Q39 | varchar |  |  | SI | Descripción Frecuencia Cardiaca Fetal |
| Q40 | varchar |  |  | SI | Comentarios Descripción Frecuencia Cardiaca Fetal |
| Q41 | varchar |  |  | SI | Variabilidad |
| Q42 | varchar |  |  | SI | Comentarios Variabilidad |
| Q43 | varchar |  |  | SI | Aceleraciones |
| Q44 | varchar |  |  | SI | Comentarios Aceleraciones |
| Q45 | varchar |  |  | SI | Desaceleraciones Precoces (DIP I) |
| Q46 | varchar |  |  | SI | Comentarios Desaceleraciones Tardías |
| Q47 | varchar |  |  | SI | Desaceleraciones Tardias (DIP II) |
| Q48 | varchar |  |  | SI | Comentarios Desaceleraciones Precoces |
| Q49 | varchar |  |  | SI | Desaceleraciones Variables (DIP III) |
| Q50 | varchar |  |  | SI | Comentarios Desaceleraciones Variables |
| Q51 | numeric |  |  | SI | LCF Gemelo I |
| Q52 | varchar |  |  | SI | Comentarios Gemelo I |
| Q53 | varchar |  |  | SI | Descripción Frecuencia Cardiaca Fetal Gemelo I |
| Q54 | varchar |  |  | SI | Comentarios Descripción Frecuencia Cardiaca Fetal ... |
| Q55 | varchar |  |  | SI | Comentario Variabilidad Gemelo I |
| Q56 | varchar |  |  | SI | Variabilidad Gemelo I |
| Q57 | varchar |  |  | SI | Comentario Aceleraciones Gemelo I |
| Q58 | varchar |  |  | SI | Aceleraciones Gemelo I |
| Q59 | varchar |  |  | SI | Comentario Desaceleraciones Tardías Gemelo I |
| Q60 | varchar |  |  | SI | Desaceleraciones Tardias Gemelo I |
| Q61 | varchar |  |  | SI | Comentarios Desaceleraciones Precoces Gemelo I |
| Q62 | varchar |  |  | SI | Desaceleraciones Precoces Gemelo I |
| Q63 | varchar |  |  | SI | Comentarios Desaceleraciones Variables Gemelo I |
| Q64 | varchar |  |  | SI | Desaceleraciones Variables Gemelo I |
| Q65 | numeric |  |  | SI | LCF Gemelo II |
| Q66 | numeric |  |  | SI | LCF Gemelo III |
| Q67 | numeric |  |  | SI | LCF Gemelo IV |
| Q68 | varchar |  |  | SI | Comentarios Descripción Frecuencia Cardiaca Fetal ... |
| Q69 | varchar |  |  | SI | Comentarios Descripción Frecuencia Cardiaca Fetal ... |
| Q70 | varchar |  |  | SI | Comentarios Descripción Frecuencia Cardiaca Fetal ... |
| Q71 | numeric |  |  | SI | LCF Gemelo V |
| Q72 | varchar |  |  | SI | Comentarios Descripción Frecuencia Cardiaca Fetal ... |
| Q73 | varchar |  |  | SI | Descripción Frecuencia Cardiaca Fetal Gemelo II |
| Q74 | varchar |  |  | SI | Comentario LCF Gemelo II  |
| Q75 | varchar |  |  | SI | Comentario LCF Gemelo III |
| Q76 | varchar |  |  | SI | Comentario LCF Gemelo IV |
| Q77 | varchar |  |  | SI | Comentario LCF Gemelo V |
| Q78 | varchar |  |  | SI | Descripción Frecuencia Cardiaca Fetal Gemelo III |
| Q79 | varchar |  |  | SI | Descripción Frecuencia Cardiaca Fetal Gemelo IV |
| Q80 | varchar |  |  | SI | Descripción Frecuencia Cardiaca Fetal Gemelo V |
| Q81 | varchar |  |  | SI | Comentarios Desaceleraciones Variables Gemelo II |
| Q82 | varchar |  |  | SI | Comentarios Desaceleraciones Variables Gemelo III |
| Q83 | varchar |  |  | SI | Comentarios Desaceleraciones Variables Gemelo IV |
| Q84 | varchar |  |  | SI | Comentarios Desaceleraciones Variables Gemelo V |
| Q85 | varchar |  |  | SI | Comentarios Variabilidad Gemelo II |
| Q86 | varchar |  |  | SI | Comentarios Variabilidad Gemelo III |
| Q87 | varchar |  |  | SI | Comentarios Variabilidad Gemelo IV |
| Q88 | varchar |  |  | SI | Comentarios Variabilidad Gemelo V |
| Q89 | varchar |  |  | SI | Comentarios Aceleraciones Gemelo II |
| Q90 | varchar |  |  | SI | Comentarios Aceleraciones Gemelo III |
| Q91 | varchar |  |  | SI | Comentarios Aceleraciones Gemelo IV |
| Q92 | varchar |  |  | SI | Comentarios Aceleraciones Gemelo V |
| Q93 | varchar |  |  | SI | Comentarios Desaceleraciones Tardías Gemelo II |
| Q94 | varchar |  |  | SI | Comentarios Desaceleraciones Tardías Gemelo III |
| Q95 | varchar |  |  | SI | Comentarios Desaceleraciones Tardías Gemelo IV |
| Q96 | varchar |  |  | SI | Comentarios Desaceleraciones Tardías Gemelo V |
| Q97 | varchar |  |  | SI | Comentarios Desaceleraciones Precoces Gemelo II |
| Q98 | varchar |  |  | SI | Comentarios Desaceleraciones Precoces Gemelo III |
| Q99 | varchar |  |  | SI | Comentarios Desaceleraciones Precoces Gemelo IV |
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