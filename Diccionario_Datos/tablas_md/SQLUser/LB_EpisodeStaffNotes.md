# SQLUser.LB_EpisodeStaffNotes

**Schema:** SQLUser
**Columnas:** 243
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPSN_ParRef | bigint | PK |  | NO | - |
| ChildQ100DR | - |  |  | SI | Child Reference: Fuerza y resistencia |
| LBEPSN_Date | date |  |  | SI | Date of  note |
| LBEPSN_Notes_DR | bigint |  | FK | SI | Note as websys.Document  (HTML = OTHER)
HTMLRichT... |
| LBEPSN_RowID | varchar |  |  | NO | - |
| LBEPSN_Time | time |  |  | SI | Time of note |
| LBEPSN_Type_DR | bigint |  | FK | SI | Link to the code table staff notes type |
| LBEPSN_User_DR | bigint |  | FK | SI | Link to the user that created the note |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora de Ingreso |
| Q03 | - |  |  | SI | Unidad |
| Q04 | - |  |  | SI | Información Entregada por |
| Q05 | - |  |  | SI | Contacto |
| Q06 | - |  |  | SI | Teléfono de contacto |
| Q07 | - |  |  | SI | Procedencia del paciente |
| Q08 | - |  |  | SI | Referido desde establecimiento |
| Q09 | - |  |  | SI | Profesión del paciente |
| Q10 | - |  |  | SI | Motivo de Consulta |
| Q101 | - |  |  | SI | Movimientos involuntarios anormales |
| Q102 | - |  |  | SI | Movimientos involuntarios anorm comentarios |
| Q103 | - |  |  | SI | R. Bicipital derecho |
| Q104 | - |  |  | SI | R. Bicipital Izquierdo |
| Q105 | - |  |  | SI | R. Tricipital Derecho |
| Q106 | - |  |  | SI | R. Tricipital Izquierdo |
| Q107 | - |  |  | SI | R. Rotuliano Derecho |
| Q108 | - |  |  | SI | R. Rotuliano Izquierdo |
| Q109 | - |  |  | SI | R. Tibial Posterior Derecho |
| Q11 | - |  |  | SI | Anamnesis Próxima |
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
| Q137 | - |  |  | SI | Conclusión |
| Q138 | - |  |  | SI | Plan al Ingreso |
| Q139 | - |  |  | SI | Profesional de Salud |
| Q13ObsDR | - |  |  | SI | Presión arterial diastólica (mmHg) DR |
| Q14 | - |  |  | SI | Saturación de O2 (%) |
| Q140 | - |  |  | SI | Escala Glasgow |
| Q141 | - |  |  | SI | Esquema Dermatomas |
| Q142 | - |  |  | SI | Apertura ocular (Neo) |
| Q142ObsDR | - |  |  | SI | Apertura ocular (Neo) DR |
| Q143 | - |  |  | SI | Respuesta motora (Neo) |
| Q143ObsDR | - |  |  | SI | Respuesta motora (Neo) DR |
| Q144 | - |  |  | SI | Respuesta verbal (Neo) |
| Q144ObsDR | - |  |  | SI | Respuesta verbal (Neo) DR |
| Q145 | - |  |  | SI | Resultado E. Glasgow Neonatal |
| Q146 | - |  |  | SI | Limitación eval. por edema palpebral (Neo) |
| Q146ObsDR | - |  |  | SI | Limitación eval. por edema palpebral (Neo) DR |
| Q147 | - |  |  | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q147ObsDR | - |  |  | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q148 | - |  |  | SI | Limitación eval. por lesión medular alta (Neo) |
| Q148ObsDR | - |  |  | SI | Limitación eval. por lesión medular alta (Neo) DR |
| Q149 | - |  |  | SI | Limitación eval. por sedación / relajación (Neo) |
| Q149ObsDR | - |  |  | SI | Limitación eval. por sedación / relajación (Neo) D... |
| Q14ObsDR | - |  |  | SI | Saturación de O2 (%) DR |
| Q15 | - |  |  | SI | Temperatura axilar (°C) |
| Q150 | - |  |  | SI | Apertura ocular (Ped) |
| Q150ObsDR | - |  |  | SI | Apertura ocular (Ped) DR |
| Q151 | - |  |  | SI | Respuesta motora (Ped) |
| Q151ObsDR | - |  |  | SI | Respuesta motora (Ped) DR |
| Q152 | - |  |  | SI | Respuesta verbal (Ped) |
| Q152ObsDR | - |  |  | SI | Respuesta verbal (Ped) DR |
| Q153 | - |  |  | SI | Resultado E. Glasgow pediátrica |
| Q154 | - |  |  | SI | Limitación ev. por edema palpebral (Ped) |
| Q154ObsDR | - |  |  | SI | Limitación ev. por edema palpebral (Ped) DR |
| Q155 | - |  |  | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q155ObsDR | - |  |  | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q156 | - |  |  | SI | Limitación de ev. por lesión medular alta (Ped) |
| Q156ObsDR | - |  |  | SI | Limitación de ev. por lesión medular alta (Ped) DR |
| Q157 | - |  |  | SI | Limitación de ev. por sedación / relajación (Ped) |
| Q157ObsDR | - |  |  | SI | Limitación de ev. por sedación / relajación (Ped) ... |
| Q158 | - |  |  | SI | Circunferencia craneana |
| Q158ObsDR | - |  |  | SI | Circunferencia craneana DR |
| Q15ObsDR | - |  |  | SI | Temperatura axilar (°C) DR |
| Q16 | - |  |  | SI | Escala de dolor (EVA) |
| Q161 | - |  |  | SI | Fondo de ojo (espec) |
| Q163 | - |  |  | SI | Diploscopía |
| Q164 | - |  |  | SI | Test de Colirios |
| Q167 | - |  |  | SI | Escala de Eastern |
| Q167ObsDR | - |  |  | SI | Escala de Eastern DR |
| Q168 | - |  |  | SI | Escala de Karnofsky |
| Q168ObsDR | - |  |  | SI | Escala de Karnofsky DR |
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
| Q29 | - |  |  | SI | Apertura ocular |
| Q29ObsDR | - |  |  | SI | Apertura ocular DR |
| Q30 | - |  |  | SI | Respuesta verbal |
| Q30ObsDR | - |  |  | SI | Respuesta verbal DR |
| Q31 | - |  |  | SI | Respuesta motora |
| Q31ObsDR | - |  |  | SI | Respuesta motora DR |
| Q32 | - |  |  | SI | Ev. limitada por edema palpebral |
| Q32ObsDR | - |  |  | SI | Ev. limitada por edema palpebral DR |
| Q33 | - |  |  | SI | Ev. limitada por lesión medular alta |
| Q33ObsDR | - |  |  | SI | Ev. limitada por lesión medular alta DR |
| Q34 | - |  |  | SI | Ev. limitada por afasia / intubación |
| Q34ObsDR | - |  |  | SI | Ev. limitada por afasia / intubación DR |
| Q35 | - |  |  | SI | Ev. limitada por sedación / relajación |
| Q35ObsDR | - |  |  | SI | Ev. limitada por sedación / relajación DR |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*