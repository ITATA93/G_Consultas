# questionnaire.QTCENEURO

> Ingreso Neurocirugía / Neurología

**Schema:** questionnaire
**Columnas:** 235
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Neurocirugía / Neurología

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Ingreso |
| Q02 | time |  |  | SI | Hora de Ingreso |
| Q03 | varchar |  |  | SI | Unidad |
| Q04 | varchar |  |  | SI | Información Entregada por |
| Q05 | varchar |  |  | SI | Contacto |
| Q06 | varchar |  |  | SI | Teléfono de contacto |
| Q07 | varchar |  |  | SI | Procedencia del paciente |
| Q08 | varchar |  |  | SI | Referido desde establecimiento |
| Q09 | varchar |  |  | SI | Profesión del paciente |
| Q10 | varchar |  |  | SI | Motivo de Consulta |
| Q101 | varchar |  |  | SI | Movimientos involuntarios anormales |
| Q102 | varchar |  |  | SI | Movimientos involuntarios anorm comentarios |
| Q103 | varchar |  |  | SI | R. Bicipital derecho |
| Q104 | varchar |  |  | SI | R. Bicipital Izquierdo |
| Q105 | varchar |  |  | SI | R. Tricipital Derecho |
| Q106 | varchar |  |  | SI | R. Tricipital Izquierdo |
| Q107 | varchar |  |  | SI | R. Rotuliano Derecho |
| Q108 | varchar |  |  | SI | R. Rotuliano Izquierdo |
| Q109 | varchar |  |  | SI | R. Tibial Posterior Derecho |
| Q11 | varchar |  |  | SI | Anamnesis Próxima |
| Q110 | varchar |  |  | SI | R. Tibial Posterior Izquierdo |
| Q111 | varchar |  |  | SI | R. Plantar Derecho |
| Q112 | varchar |  |  | SI | R. Plantar Izquierdo |
| Q114 | varchar |  |  | SI | Estereognosia |
| Q115 | varchar |  |  | SI | Grafoestesia |
| Q116 | varchar |  |  | SI | Discriminación de dos puntos |
| Q117 | varchar |  |  | SI | Sensibilidad comentarios |
| Q118 | varchar |  |  | SI | Test Índice - Nariz |
| Q119 | varchar |  |  | SI | Test Talón - Rodilla |
| Q12 | varchar |  |  | SI | Presión arterial sistólica (mmHg) |
| Q120 | varchar |  |  | SI | Diádococinesia |
| Q121 | varchar |  |  | SI | Coordinación comentarios |
| Q122 | varchar |  |  | SI | Signos meníngeos |
| Q123 | varchar |  |  | SI | Signos meníngeos comentarios |
| Q124 | bit |  |  | SI | Paciente vigil y atento. Orientado en tiempo y esp... |
| Q125 | bit |  |  | SI | Memoria sin alteraciones. Lenguaje apropiado, norm... |
| Q126 | bit |  |  | SI | Pares craneanos sin alteraciones. |
| Q127 | bit |  |  | SI | Marcha normal. Musculatura de fuerza, tono y trofi... |
| Q128 | bit |  |  | SI | Reflejos osteotendíneos simétricos, normales. Sin ... |
| Q129 | bit |  |  | SI | Sensibilidad primaria y secundaria conservada, nor... |
| Q12ObsDR | varchar |  | FK | SI | Presión arterial sistólica (mmHg) DR |
| Q13 | varchar |  |  | SI | Presión arterial diastólica (mmHg) |
| Q130 | bit |  |  | SI | Coordinación motora normal. Sin signos cerebelosos... |
| Q131 | bit |  |  | SI | Sin signos meníngeos al examen. |
| Q132 | varchar |  |  | SI | Exámenes de laboratorio |
| Q133 | varchar |  |  | SI | Exámenes de Rayos X |
| Q134 | varchar |  |  | SI | Tomografía Axial Computada (TAC) |
| Q135 | varchar |  |  | SI | Resonancia Nuclear Magnética (RNM) |
| Q136 | varchar |  |  | SI | Electroencefalograma |
| Q137 | varchar |  |  | SI | Conclusión |
| Q138 | varchar |  |  | SI | Plan al Ingreso |
| Q139 | varchar |  |  | SI | Profesional de Salud |
| Q13ObsDR | varchar |  | FK | SI | Presión arterial diastólica (mmHg) DR |
| Q14 | varchar |  |  | SI | Saturación de O2 (%) |
| Q140 | varchar |  |  | SI | Escala Glasgow |
| Q141 | varchar |  |  | SI | Esquema Dermatomas |
| Q142 | varchar |  |  | SI | Apertura ocular (Neo) |
| Q142ObsDR | varchar |  | FK | SI | Apertura ocular (Neo) DR |
| Q143 | varchar |  |  | SI | Respuesta motora (Neo) |
| Q143ObsDR | varchar |  | FK | SI | Respuesta motora (Neo) DR |
| Q144 | varchar |  |  | SI | Respuesta verbal (Neo) |
| Q144ObsDR | varchar |  | FK | SI | Respuesta verbal (Neo) DR |
| Q145 | varchar |  |  | SI | Resultado E. Glasgow Neonatal |
| Q146 | varchar |  |  | SI | Limitación eval. por edema palpebral (Neo) |
| Q146ObsDR | varchar |  | FK | SI | Limitación eval. por edema palpebral (Neo) DR |
| Q147 | varchar |  |  | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q147ObsDR | varchar |  | FK | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q148 | varchar |  |  | SI | Limitación eval. por lesión medular alta (Neo) |
| Q148ObsDR | varchar |  | FK | SI | Limitación eval. por lesión medular alta (Neo) DR |
| Q149 | varchar |  |  | SI | Limitación eval. por sedación / relajación (Neo) |
| Q149ObsDR | varchar |  | FK | SI | Limitación eval. por sedación / relajación (Neo) D... |
| Q14ObsDR | varchar |  | FK | SI | Saturación de O2 (%) DR |
| Q15 | varchar |  |  | SI | Temperatura axilar (°C) |
| Q150 | varchar |  |  | SI | Apertura ocular (Ped) |
| Q150ObsDR | varchar |  | FK | SI | Apertura ocular (Ped) DR |
| Q151 | varchar |  |  | SI | Respuesta motora (Ped) |
| Q151ObsDR | varchar |  | FK | SI | Respuesta motora (Ped) DR |
| Q152 | varchar |  |  | SI | Respuesta verbal (Ped) |
| Q152ObsDR | varchar |  | FK | SI | Respuesta verbal (Ped) DR |
| Q153 | varchar |  |  | SI | Resultado E. Glasgow pediátrica |
| Q154 | varchar |  |  | SI | Limitación ev. por edema palpebral (Ped) |
| Q154ObsDR | varchar |  | FK | SI | Limitación ev. por edema palpebral (Ped) DR |
| Q155 | varchar |  |  | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q155ObsDR | varchar |  | FK | SI | Limitación ev. por afasia, intubación orotraqueal ... |
| Q156 | varchar |  |  | SI | Limitación de ev. por lesión medular alta (Ped) |
| Q156ObsDR | varchar |  | FK | SI | Limitación de ev. por lesión medular alta (Ped) DR |
| Q157 | varchar |  |  | SI | Limitación de ev. por sedación / relajación (Ped) |
| Q157ObsDR | varchar |  | FK | SI | Limitación de ev. por sedación / relajación (Ped) ... |
| Q158 | varchar |  |  | SI | Circunferencia craneana |
| Q158ObsDR | varchar |  | FK | SI | Circunferencia craneana DR |
| Q15ObsDR | varchar |  | FK | SI | Temperatura axilar (°C) DR |
| Q16 | varchar |  |  | SI | Escala de dolor (EVA) |
| Q161 | varchar |  |  | SI | Fondo de ojo (espec) |
| Q163 | varchar |  |  | SI | Diploscopía |
| Q164 | varchar |  |  | SI | Test de Colirios |
| Q167 | varchar |  |  | SI | Escala de Eastern |
| Q167ObsDR | varchar |  | FK | SI | Escala de Eastern DR |
| Q168 | varchar |  |  | SI | Escala de Karnofsky |
| Q168ObsDR | varchar |  | FK | SI | Escala de Karnofsky DR |
| Q16ObsDR | varchar |  | FK | SI | Escala de dolor (EVA) DR |
| Q17 | varchar |  |  | SI | Peso (kg) |
| Q17ObsDR | varchar |  | FK | SI | Peso (kg) DR |
| Q18 | varchar |  |  | SI | Talla (cms.) |
| Q18ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q19 | varchar |  |  | SI | Frecuencia cardíaca (lpm) |
| Q19ObsDR | varchar |  | FK | SI | Frecuencia cardíaca (lpm) DR |
| Q20 | varchar |  |  | SI | Frecuencia respiratoria (rpm) |
| Q20ObsDR | varchar |  | FK | SI | Frecuencia respiratoria (rpm) DR |
| Q21 | varchar |  |  | SI | FIO2 (%) |
| Q21ObsDR | varchar |  | FK | SI | FIO2 (%) DR |
| Q22 | varchar |  |  | SI | Examen físico general |
| Q23 | bit |  |  | SI | Conciencia normal |
| Q24 | bit |  |  | SI | Conciencia alterado |
| Q25 | bit |  |  | SI | Conciencia no evaluado |
| Q26 | varchar |  |  | SI | Conciencia comentarios |
| Q27 | varchar |  |  | SI | Estado cuantitativo de conciencia |
| Q28 | varchar |  |  | SI | Estado cualitativo de conciencia |
| Q29 | varchar |  |  | SI | Apertura ocular |
| Q29ObsDR | varchar |  | FK | SI | Apertura ocular DR |
| Q30 | varchar |  |  | SI | Respuesta verbal |
| Q30ObsDR | varchar |  | FK | SI | Respuesta verbal DR |
| Q31 | varchar |  |  | SI | Respuesta motora |
| Q31ObsDR | varchar |  | FK | SI | Respuesta motora DR |
| Q32 | varchar |  |  | SI | Ev. limitada por edema palpebral |
| Q32ObsDR | varchar |  | FK | SI | Ev. limitada por edema palpebral DR |
| Q33 | varchar |  |  | SI | Ev. limitada por lesión medular alta |
| Q33ObsDR | varchar |  | FK | SI | Ev. limitada por lesión medular alta DR |
| Q34 | varchar |  |  | SI | Ev. limitada por afasia / intubación |
| Q34ObsDR | varchar |  | FK | SI | Ev. limitada por afasia / intubación DR |
| Q35 | varchar |  |  | SI | Ev. limitada por sedación / relajación |
| Q35ObsDR | varchar |  | FK | SI | Ev. limitada por sedación / relajación DR |
| Q36 | bit |  |  | SI | Atención normal |
| Q37 | bit |  |  | SI | Atención alterado |
| Q38 | bit |  |  | SI | Atención no evaluado |
| Q39 | varchar |  |  | SI | Atención comentarios |
| Q40 | bit |  |  | SI | Orientación normal |
| Q41 | bit |  |  | SI | Orientación alterado |
| Q42 | bit |  |  | SI | Orientación no evaluado |
| Q43 | varchar |  |  | SI | Orientación comentarios |
| Q44 | bit |  |  | SI | Memoria normal |
| Q45 | bit |  |  | SI | Memoria alterado |
| Q46 | bit |  |  | SI | Memoria no evaluado |
| Q47 | varchar |  |  | SI | Memoria comentarios |
| Q48 | bit |  |  | SI | Lenguaje normal |
| Q49 | bit |  |  | SI | Lenguaje alterado |
| Q50 | bit |  |  | SI | Lenguaje no evaluado |
| Q51 | varchar |  |  | SI | Lenguaje comentarios |
| Q52 | varchar |  |  | SI | Lenguaje espontáneo |
| Q53 | varchar |  |  | SI | Prosodia |
| Q54 | varchar |  |  | SI | Comprensión |
| Q55 | varchar |  |  | SI | Repetición |
| Q56 | varchar |  |  | SI | Nominación |
| Q57 | varchar |  |  | SI | Lecto-escritura |
| Q58 | bit |  |  | SI | Olfatorio normal |
| Q59 | bit |  |  | SI | Olfatorio alterado |
| Q60 | bit |  |  | SI | Olfatorio no evaluado |
| Q61 | varchar |  |  | SI | Olfatorio comentarios |
| Q62 | bit |  |  | SI | Óptico normal |
| Q63 | bit |  |  | SI | Óptico alterado |
| Q64 | bit |  |  | SI | Óptico no evaluado |
| Q65 | varchar |  |  | SI | Óptico comentarios |
| Q66 | varchar |  |  | SI | Agudeza visual |
| Q67 | varchar |  |  | SI | Campo visual |
| Q68 | varchar |  |  | SI | Fondo de ojo |
| Q69 | bit |  |  | SI | Oculomotor normal |
| Q70 | bit |  |  | SI | Oculomotor alterado |
| Q71 | bit |  |  | SI | Oculomotor no evaluado |
| Q72 | varchar |  |  | SI | Oculomotor comentarios |
| Q74 | varchar |  |  | SI | Mirada conjugada |
| Q75 | bit |  |  | SI | Trigémino normal |
| Q76 | bit |  |  | SI | Trigémino alterado |
| Q77 | bit |  |  | SI | Trigémino no evaluado |
| Q78 | varchar |  |  | SI | Trigémino comentarios |
| Q79 | bit |  |  | SI | Facial normal |
| Q80 | bit |  |  | SI | Facial alterado |
| Q81 | bit |  |  | SI | Facial no evaluado |
| Q82 | varchar |  |  | SI | Facial comentarios |
| Q83 | bit |  |  | SI | Acústico normal |
| Q84 | bit |  |  | SI | Acústico alterado |
| Q85 | bit |  |  | SI | Acústico no evaluado |
| Q86 | varchar |  |  | SI | Acústico comentarios |
| Q87 | bit |  |  | SI | Glosovago normal |
| Q88 | bit |  |  | SI | Glosovago alterado |
| Q89 | bit |  |  | SI | Glosovago no evaluado |
| Q90 | varchar |  |  | SI | Glosovago comentarios |
| Q91 | bit |  |  | SI | Espinal normal |
| Q92 | bit |  |  | SI | Espinal alterado |
| Q93 | bit |  |  | SI | Espinal no evaluado |
| Q94 | varchar |  |  | SI | Espinal comentarios |
| Q95 | bit |  |  | SI | Hipogloso normal |
| Q96 | bit |  |  | SI | Hipogloso alterado |
| Q97 | bit |  |  | SI | Hipogloso no evaluado |
| Q98 | varchar |  |  | SI | Hipogloso comentarios |
| Q99 | varchar |  |  | SI | Marcha |
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