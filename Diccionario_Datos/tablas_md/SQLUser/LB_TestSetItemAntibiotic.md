# SQLUser.LB_TestSetItemAntibiotic

**Schema:** SQLUser
**Columnas:** 203
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSIANT_ParRef | varchar | PK |  | NO | LBTestSet Parent Reference |
| LBTSIANT_AntibioticPanel_DR | bigint |  | FK | SI | Antibiotic Panel DR |
| LBTSIANT_Antibiotic_DR | bigint |  | FK | SI | Antibiotics Code |
| LBTSIANT_Default | varchar |  |  | SI | Marks that Record was inserted due to Code Table D... |
| LBTSIANT_Instrument_DR | bigint |  | FK | SI | Instrument DR |
| LBTSIANT_Reportable | varchar |  |  | SI | Reportable |
| LBTSIANT_Restricted | varchar |  |  | SI | Restricted |
| LBTSIANT_ResultETest | varchar |  |  | SI | Result E Test |
| LBTSIANT_ResultETest_DR | bigint |  | FK | SI | Sensitivity ETest |
| LBTSIANT_ResultMIC | varchar |  |  | SI | Result MIC |
| LBTSIANT_ResultMICIntermediate | varchar |  |  | SI | Result MIC Intermediate Point |
| LBTSIANT_ResultMICResistant | varchar |  |  | SI | Result MIC Resistant Point |
| LBTSIANT_ResultMICSensitive | varchar |  |  | SI | Result MIC Sensitive Point |
| LBTSIANT_ResultMIC_DR | bigint |  | FK | SI | Sensitivity MIC |
| LBTSIANT_Result_DR | bigint |  | FK | SI | Des Ref Sensitivity table |
| LBTSIANT_Resultmm | varchar |  |  | SI | Result mm |
| LBTSIANT_Resultmm_DR | bigint |  | FK | SI | Sensitivity mm |
| LBTSIANT_RowID | varchar |  |  | NO | - |
| LBTSIANT_Sequence | double |  |  | SI | Sequence |
| Q01 | - |  |  | SI | OFA |
| Q02 | - |  |  | SI | Praxias BLF |
| Q03 | - |  |  | SI | Audición |
| Q04 | - |  |  | SI | Funciones Estomatognáticas |
| Q05 | - |  |  | SI | Habilidades Prelinguísticas |
| Q06 | - |  |  | SI | Ritmo |
| Q07 | - |  |  | SI | Velocidad |
| Q08 | - |  |  | SI | Inteligibilidad |
| Q09 | - |  |  | SI | Articulación |
| Q10 | - |  |  | SI | Nivel Fonológico |
| Q100 | - |  |  | SI | ReflejosPatológicos Orales |
| Q101 | - |  |  | SI | Ausculturación Cervical |
| Q102 | - |  |  | SI | Deglución en seco |
| Q103 | - |  |  | SI | SpO2 |
| Q104 | - |  |  | SI | FiO2 |
| Q105 | - |  |  | SI | Oximetría Previa |
| Q106 | - |  |  | SI | Consistencia Líquida |
| Q107 | - |  |  | SI | Consistencia Pastosa |
| Q108 | - |  |  | SI | Consistencia Sólida |
| Q109 | - |  |  | SI | Fase Preparatoria Oral |
| Q11 | - |  |  | SI | Nivel Semántico |
| Q110 | - |  |  | SI | Fase Oral |
| Q111 | - |  |  | SI | Fase Faríngea |
| Q112 | - |  |  | SI | Observaciones |
| Q113 | - |  |  | SI | TECAL |
| Q114 | - |  |  | SI | TEPROSIF-R |
| Q115 | - |  |  | SI | STSG Expresivo |
| Q116 | - |  |  | SI | STSG Receptivo |
| Q117 | - |  |  | SI | TAR |
| Q118 | - |  |  | SI | Protocolo Pragmático de Prutting |
| Q119 | - |  |  | SI | Protocolo Pragmático de Luis Martinez |
| Q12 | - |  |  | SI | Nivel Morfosintáctico |
| Q120 | - |  |  | SI | Otro? Cuales? |
| Q121 | - |  |  | SI | RESULTADOS Y OBSERVACIONES |
| Q122 | - |  |  | SI | Test de Boston |
| Q123 | - |  |  | SI | Protocolo de Lenguaje para pacientes afásicos (Gon... |
| Q124 | - |  |  | SI | Mini Protocolo para Pacientes afásicos |
| Q125 | - |  |  | SI | Token Test |
| Q126 | - |  |  | SI | Otro(s) ¿Cuales? |
| Q127 | - |  |  | SI | RESULTADOS Y OBSERVACIONES |
| Q128 | - |  |  | SI | Protocolos de Evaluación de Habla (Gonzalez, R &To... |
| Q129 | - |  |  | SI | Protocolo de Disartria |
| Q13 | - |  |  | SI | Nivel Pragmático |
| Q130 | - |  |  | SI | Otro(s) ¿Cuál(es)? |
| Q131 | - |  |  | SI | RESULTADOS Y OBSERVACIONES |
| Q132 | - |  |  | SI | Pauta de evaluación Cognitiva- Linguística (Gonzal... |
| Q133 | - |  |  | SI | Mini Mental State Examination (MMSE) |
| Q134 | - |  |  | SI | Test de la Figura Compleja del Rey |
| Q135 | - |  |  | SI | Test de Wisconsin |
| Q136 | - |  |  | SI | Test  de Barcelona |
| Q137 | - |  |  | SI | Test del Vaso de Agua |
| Q138 | - |  |  | SI | Pauta de evaluación Clínica de la Deglución (Gonza... |
| Q139 | - |  |  | SI | NFC Laríngea directa |
| Q14 | - |  |  | SI | Observaciones |
| Q140 | - |  |  | SI | NFC Laríngea Indirecta |
| Q141 | - |  |  | SI | Otros(s) ¿Cuál(es)? |
| Q142 | - |  |  | SI | SÍNTESIS O CONCLUSIONES |
| Q143 | - |  |  | SI | INDICACIONES |
| Q15 | - |  |  | SI | 0 |
| Q16 | - |  |  | SI | 1 |
| Q17 | - |  |  | SI | 2 |
| Q18 | - |  |  | SI | 3 |
| Q19 | - |  |  | SI | 4 |
| Q20 | - |  |  | SI | 5 |
| Q21 | - |  |  | SI | Discurso Oral |
| Q22 | - |  |  | SI | Fluidez Oral |
| Q23 | - |  |  | SI | Contenido (Información) |
| Q24 | - |  |  | SI | Parafásias |
| Q25 | - |  |  | SI | Forma Gramatical |
| Q26 | - |  |  | SI | Lenguaje Automático |
| Q27 | - |  |  | SI | Lenguaje Repetido |
| Q28 | - |  |  | SI | Lenguaje Denominativo |
| Q29 | - |  |  | SI | Fluidez Verbal |
| Q30 | - |  |  | SI | Reconocimiento Auditivo |
| Q31 | - |  |  | SI | Token Test |
| Q32 | - |  |  | SI | Discurso Comprensivo |
| Q33 | - |  |  | SI | Automática |
| Q34 | - |  |  | SI | Dictado |
| Q35 | - |  |  | SI | Copia |
| Q36 | - |  |  | SI | Descriptiva |
| Q37 | - |  |  | SI | Copia |
| Q38 | - |  |  | SI | Páreo Visual - Verbal |
| Q39 | - |  |  | SI | Lectura Oral |
| Q40 | - |  |  | SI | Cálculo |
| Q41 | - |  |  | SI | Visual (p. v/v) |
| Q42 | - |  |  | SI | Copia Figura |
| Q43 | - |  |  | SI | Pantomima |
| Q44 | - |  |  | SI | Tipo I |
| Q45 | - |  |  | SI | Tipo II |
| Q46 | - |  |  | SI | Tipo III |
| Q47 | - |  |  | SI | Tipo IV |
| Q48 | - |  |  | SI | Observaciones |
| Q49 | - |  |  | SI | OFA |
| Q50 | - |  |  | SI | Respiración |
| Q51 | - |  |  | SI | Fonación |
| Q52 | - |  |  | SI | Articulación y CMO |
| Q53 | - |  |  | SI | Resonancia |
| Q54 | - |  |  | SI | Prosodia |
| Q55 | - |  |  | SI | Lectura |
| Q56 | - |  |  | SI | Observaciones |
| Q57 | - |  |  | SI | Orientación/Estado de Conciencia |
| Q58 | - |  |  | SI | Atención/Concentración |
| Q59 | - |  |  | SI | Función Ejecutiva |
| Q60 | - |  |  | SI | Memoria Inmediata |
| Q61 | - |  |  | SI | Memoria Reciente (Lapso) |
| Q62 | - |  |  | SI | Memoria a largo Plazo |
| Q63 | - |  |  | SI | Secuncias Automáticas (Control Mental) |
| Q64 | - |  |  | SI | Denominación |
| Q65 | - |  |  | SI | Comprensión Verbal |
| Q66 | - |  |  | SI | Lectura Oral |
| Q67 | - |  |  | SI | Comprensión de Lectura |
| Q68 | - |  |  | SI | Escritura |
| Q69 | - |  |  | SI | Discurso |
| Q70 | - |  |  | SI | Visuo-Constructivo |
| Q71 | - |  |  | SI | Abstracción Verbal |
| Q72 | - |  |  | SI | Absurdos Verbales/Resolución de Problemas/Raciocin... |
| Q73 | - |  |  | SI | Observaciones |
| Q74 | - |  |  | SI | Estática |
| Q75 | - |  |  | SI | Dinámica |
| Q76 | - |  |  | SI | Dinámica |
| Q77 | - |  |  | SI | Palpación |
| Q78 | - |  |  | SI | Emisión |
| Q79 | - |  |  | SI | Intensidad |
| Q80 | - |  |  | SI | Altura Tonal |
| Q81 | - |  |  | SI | Extensión Tonal |
| Q82 | - |  |  | SI | Ataque Vocal |
| Q83 | - |  |  | SI | Quiebres Tonales |
| Q84 | - |  |  | SI | Prosodia |
| Q85 | - |  |  | SI | Colocación |
| Q86 | - |  |  | SI | Resonancia |
| Q87 | - |  |  | SI | Mordiente |
| Q88 | - |  |  | SI | Articulación |
| Q89 | - |  |  | SI | Apertura Bucal |
| Q90 | - |  |  | SI | Temblor de Voz |
| Q91 | - |  |  | SI | TMF /O/ |
| Q92 | - |  |  | SI | TMF /S/ |
| Q93 | - |  |  | SI | Indice s/o |
| Q94 | - |  |  | SI | Compromiso Cognitivo |
| Q95 | - |  |  | SI | OFA |
| Q96 | - |  |  | SI | CMO |
| Q97 | - |  |  | SI | Reflejos Orales |
| Q98 | - |  |  | SI | Tos Voluntaria |
| Q99 | - |  |  | SI | Elavoración Laríngea |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*