# questionnaire.QTCNSUPDRS

> Escala unificada de calificación de la enfermedad de Parkinson

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala unificada de calificación de la enfermedad de Parkinson

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | I. ESTADO MENTAL. COMPORTAMIENTO Y ESTADO DE ÁNIMO |
| Q02 | varchar |  |  | SI | ALTERACIÓN DEL INTELECTO |
| Q03 | varchar |  |  | SI | TRASTORNOS DEL PENSAMIENTO (Por demencia o por int... |
| Q04 | varchar |  |  | SI | DEPRESIÓN |
| Q05 | varchar |  |  | SI | MOTIVACIÓN – INICIATIVA |
| Q06 | varchar |  |  | SI | II. ACTIVIDADES DE LA VIDA DIARIA |
| Q07 | varchar |  |  | SI | LENGUAJE |
| Q08 | varchar |  |  | SI | SALIVACIÓN |
| Q09 | varchar |  |  | SI | DEGLUCIÓN |
| Q10 | varchar |  |  | SI | ESCRITURA |
| Q11 | varchar |  |  | SI | CORTAR ALIMENTOS Y MANEJAR CUBIERTOS |
| Q12 | varchar |  |  | SI | VESTIDO |
| Q13 | varchar |  |  | SI | HIGIENE |
| Q14 | varchar |  |  | SI | DAR VUELTAS EN LA CAMA Y AJUSTAR LA ROPA DE CAMA |
| Q15 | varchar |  |  | SI | CAÍDAS (Sin relación con el fenómeno de “congelaci... |
| Q16 | varchar |  |  | SI | “CONGELACIÓN” AL CAMINAR |
| Q17 | varchar |  |  | SI | CAMINAR |
| Q18 | varchar |  |  | SI | TEMBLOR |
| Q19 | varchar |  |  | SI | SÍNTOMAS SENSORIALES RELACIONADOS CON EL PARKINSON... |
| Q20 | varchar |  |  | SI | III. EXPLORACIÓN DE ASPECTOS MOTORES |
| Q21 | varchar |  |  | SI | LENGUAJE |
| Q22 | varchar |  |  | SI | EXPRESIÓN FACIAL |
| Q23 | varchar |  |  | SI | TEMBLOR DE REPOSO EN MMSS |
| Q24 | varchar |  |  | SI | TEMBLOR DE ACCIÓN O POSTURAL DE LAS MANOS |
| Q25 | varchar |  |  | SI | RIGIDEZ (Rueda dentada para ser ignorada) |
| Q26 | varchar |  |  | SI | GOLPETEO DE LOS DEDOS (El paciente golpea el pulga... |
| Q27 | varchar |  |  | SI | MOVIMIENTOS ALTERNANTES CON LAS MANOS (El paciente... |
| Q28 | varchar |  |  | SI | MOVIMIENTOS RÁPIDOS ALTERNANTES DE MMSS (movimient... |
| Q29 | varchar |  |  | SI | AGILIDAD DE PIERNAS |
| Q30 | varchar |  |  | SI | LEVANTARSE DE LA SILLA (El paciente intenta levant... |
| Q31 | varchar |  |  | SI | POSTURA |
| Q32 | varchar |  |  | SI | MARCHA |
| Q33 | varchar |  |  | SI | ESTABILIDAD POSTURA (Respuesta al desplazamiento s... |
| Q34 | varchar |  |  | SI | BRADIQUINESIA E HIPOQUINESIA (Combina lentitud, ti... |
| Q35 | varchar |  |  | SI | IV. COMPLICACIONES DEL TRATAMIENTO (En la semana p... |
| Q36 | varchar |  |  | SI | A. DISCINESIAS |
| Q37 | varchar |  |  | SI | DURACIÓN ¿Qué proporción del día vigil están prese... |
| Q38 | varchar |  |  | SI | INCAPACIDAD ¿Hasta qué punto son incapacitantes la... |
| Q39 | varchar |  |  | SI | DISCINESIAS DOLOROSAS ¿Son dolorosas las discinesi... |
| Q40 | varchar |  |  | SI | PRESENCIA DE DISTONÍA MATUTINA |
| Q41 | varchar |  |  | SI | B. FLUCTUACIONES CLÍNICAS |
| Q42 | varchar |  |  | SI | ¿Hay PERÍODOS OFF PREDECIBLES en relación temporal... |
| Q43 | varchar |  |  | SI | ¿Hay PERÍODOS OFF DE INSTAURACIÓN SÚBITA? |
| Q44 | varchar |  |  | SI | ¿Qué PROPORCIÓN DEL DÍA vigil está el paciente en ... |
| Q45 | varchar |  |  | SI | C. OTRAS COMPLICACIONES |
| Q46 | varchar |  |  | SI | ¿TIENE EL PACIENTE ANOREXIA, NAUSEAS O VÓMITOS? |
| Q47 | varchar |  |  | SI | ¿TIENE EL PACIENTE TRASTORNOS DEL SUEÑO? (P.E. ins... |
| Q48 | varchar |  |  | SI | ¿TIENE EL PACIENTE ORTOSTATISMO SINTOMÁTICO? |
| Q49 | varchar |  |  | SI | 179 representa la peor discapacidad (total) |
| Q50 | varchar |  |  | SI | 0 representa la ausencia de discapacidad |
| Q51 | varchar |  |  | SI | La UPDRS es una herramienta de calificación para s... |
| Q52 | varchar |  |  | SI | Se compone de las secciones 1) Mención, Comportami... |
| Q53 | varchar |  |  | SI | Un total de 179 puntos son posibles. 179 represent... |
| Q54 | varchar |  |  | SI | 0 = Sin discapacidad y 179 = Alta discapacidad |
| Q55 | varchar |  |  | SI | A. Discinesias |
| Q56 | varchar |  |  | SI | B. Fluctuaciones clínicas |
| Q57 | varchar |  |  | SI | C. Otra complicación |
| Q58 | varchar |  |  | SI | ¿Hay PERÍODOS OFF IMPREDECIBLES en relación tempor... |
| Q59 | date |  |  | SI | Fecha |
| Q60 | time |  |  | SI | Hora |
| Q61 | varchar |  |  | SI | 0 - 179 |
| Q62 | varchar |  |  | SI | 0 representa ninguna discapacidad y 179 representa... |
| Q63 | varchar |  |  | SI | 0 - 179: 0 representa ninguna discapacidad y 179 r... |
| Q64 | varchar |  |  | SI | Puntaje |
| Q65 | varchar |  |  | SI | Clasificación |
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