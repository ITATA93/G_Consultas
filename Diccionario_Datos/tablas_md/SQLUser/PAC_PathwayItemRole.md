# SQLUser.PAC_PathwayItemRole

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPIR_ParRef | varchar | PK |  | NO | Parent Reference |
| PACPIR_Childsub | double |  |  | NO | Childsub |
| PACPIR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPIR_CreatedDate | date |  |  | SI | Created Date |
| PACPIR_CreatedTime | time |  |  | SI | Created Time |
| PACPIR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPIR_PathwayRole_DR | varchar |  | FK | SI | Pathway Care Team Role |
| PACPIR_RowId | varchar |  |  | NO | - |
| PACPIR_UpdatedDate | date |  |  | SI | Updated Date |
| PACPIR_UpdatedTime | time |  |  | SI | Updated Time |
| PACPIR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | I. ESTADO MENTAL. COMPORTAMIENTO Y ESTADO DE ÁNIMO |
| Q02 | - |  |  | SI | ALTERACIÓN DEL INTELECTO |
| Q03 | - |  |  | SI | TRASTORNOS DEL PENSAMIENTO (Por demencia o por int... |
| Q04 | - |  |  | SI | DEPRESIÓN |
| Q05 | - |  |  | SI | MOTIVACIÓN – INICIATIVA |
| Q06 | - |  |  | SI | II. ACTIVIDADES DE LA VIDA DIARIA |
| Q07 | - |  |  | SI | LENGUAJE |
| Q08 | - |  |  | SI | SALIVACIÓN |
| Q09 | - |  |  | SI | DEGLUCIÓN |
| Q10 | - |  |  | SI | ESCRITURA |
| Q11 | - |  |  | SI | CORTAR ALIMENTOS Y MANEJAR CUBIERTOS |
| Q12 | - |  |  | SI | VESTIDO |
| Q13 | - |  |  | SI | HIGIENE |
| Q14 | - |  |  | SI | DAR VUELTAS EN LA CAMA Y AJUSTAR LA ROPA DE CAMA |
| Q15 | - |  |  | SI | CAÍDAS (Sin relación con el fenómeno de “congelaci... |
| Q16 | - |  |  | SI | “CONGELACIÓN” AL CAMINAR |
| Q17 | - |  |  | SI | CAMINAR |
| Q18 | - |  |  | SI | TEMBLOR |
| Q19 | - |  |  | SI | SÍNTOMAS SENSORIALES RELACIONADOS CON EL PARKINSON... |
| Q20 | - |  |  | SI | III. EXPLORACIÓN DE ASPECTOS MOTORES |
| Q21 | - |  |  | SI | LENGUAJE |
| Q22 | - |  |  | SI | EXPRESIÓN FACIAL |
| Q23 | - |  |  | SI | TEMBLOR DE REPOSO EN MMSS |
| Q24 | - |  |  | SI | TEMBLOR DE ACCIÓN O POSTURAL DE LAS MANOS |
| Q25 | - |  |  | SI | RIGIDEZ (Rueda dentada para ser ignorada) |
| Q26 | - |  |  | SI | GOLPETEO DE LOS DEDOS (El paciente golpea el pulga... |
| Q27 | - |  |  | SI | MOVIMIENTOS ALTERNANTES CON LAS MANOS (El paciente... |
| Q28 | - |  |  | SI | MOVIMIENTOS RÁPIDOS ALTERNANTES DE MMSS (movimient... |
| Q29 | - |  |  | SI | AGILIDAD DE PIERNAS |
| Q30 | - |  |  | SI | LEVANTARSE DE LA SILLA (El paciente intenta levant... |
| Q31 | - |  |  | SI | POSTURA |
| Q32 | - |  |  | SI | MARCHA |
| Q33 | - |  |  | SI | ESTABILIDAD POSTURA (Respuesta al desplazamiento s... |
| Q34 | - |  |  | SI | BRADIQUINESIA E HIPOQUINESIA (Combina lentitud, ti... |
| Q35 | - |  |  | SI | IV. COMPLICACIONES DEL TRATAMIENTO (En la semana p... |
| Q36 | - |  |  | SI | A. DISCINESIAS |
| Q37 | - |  |  | SI | DURACIÓN ¿Qué proporción del día vigil están prese... |
| Q38 | - |  |  | SI | INCAPACIDAD ¿Hasta qué punto son incapacitantes la... |
| Q39 | - |  |  | SI | DISCINESIAS DOLOROSAS ¿Son dolorosas las discinesi... |
| Q40 | - |  |  | SI | PRESENCIA DE DISTONÍA MATUTINA |
| Q41 | - |  |  | SI | B. FLUCTUACIONES CLÍNICAS |
| Q42 | - |  |  | SI | ¿Hay PERÍODOS OFF PREDECIBLES en relación temporal... |
| Q43 | - |  |  | SI | ¿Hay PERÍODOS OFF DE INSTAURACIÓN SÚBITA? |
| Q44 | - |  |  | SI | ¿Qué PROPORCIÓN DEL DÍA vigil está el paciente en ... |
| Q45 | - |  |  | SI | C. OTRAS COMPLICACIONES |
| Q46 | - |  |  | SI | ¿TIENE EL PACIENTE ANOREXIA, NAUSEAS O VÓMITOS? |
| Q47 | - |  |  | SI | ¿TIENE EL PACIENTE TRASTORNOS DEL SUEÑO? (P.E. ins... |
| Q48 | - |  |  | SI | ¿TIENE EL PACIENTE ORTOSTATISMO SINTOMÁTICO? |
| Q49 | - |  |  | SI | 179 representa la peor discapacidad (total) |
| Q50 | - |  |  | SI | 0 representa la ausencia de discapacidad |
| Q51 | - |  |  | SI | La UPDRS es una herramienta de calificación para s... |
| Q52 | - |  |  | SI | Se compone de las secciones 1) Mención, Comportami... |
| Q53 | - |  |  | SI | Un total de 179 puntos son posibles. 179 represent... |
| Q54 | - |  |  | SI | 0 = Sin discapacidad y 179 = Alta discapacidad |
| Q55 | - |  |  | SI | A. Discinesias |
| Q56 | - |  |  | SI | B. Fluctuaciones clínicas |
| Q57 | - |  |  | SI | C. Otra complicación |
| Q58 | - |  |  | SI | ¿Hay PERÍODOS OFF IMPREDECIBLES en relación tempor... |
| Q59 | - |  |  | SI | Fecha |
| Q60 | - |  |  | SI | Hora |
| Q61 | - |  |  | SI | 0 - 179 |
| Q62 | - |  |  | SI | 0 representa ninguna discapacidad y 179 representa... |
| Q63 | - |  |  | SI | 0 - 179: 0 representa ninguna discapacidad y 179 r... |
| Q64 | - |  |  | SI | Puntaje |
| Q65 | - |  |  | SI | Clasificación |
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