# SQLUser.BLC_DRGClass1

**Schema:** SQLUser
**Columnas:** 170
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CL1_RowId | bigint | PK |  | NO | - |
| CL1_Code | varchar |  |  | NO | Code |
| CL1_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CL1_CreatedDate | date |  |  | SI | Created Date |
| CL1_CreatedTime | time |  |  | SI | Created Time |
| CL1_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CL1_Desc | varchar |  |  | NO | Description |
| CL1_Owner | varchar |  |  | SI | Owner |
| CL1_UpdatedDate | date |  |  | SI | Updated Date |
| CL1_UpdatedTime | time |  |  | SI | Updated Time |
| CL1_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Nombre del Evaluador |
| Q04 | - |  |  | SI | ¿Existe asimetría de la boca durante la sonrisa? |
| Q05 | - |  |  | SI | ¿Existe asimetría de la boca durante la sonrisa? U... |
| Q06 | - |  |  | SI | ¿Existe asimetría de la boca durante la sonrisa? S... |
| Q07 | - |  |  | SI | Sección I. EVALUACIÓN OROFACIAL |
| Q08 | - |  |  | SI | 1.1 CARA |
| Q09 | - |  |  | SI | ¿Existe asimetría en la contracción de la frente c... |
| Q10 | - |  |  | SI | ¿Existe asimetría en la contracción de la frente c... |
| Q100 | - |  |  | SI | de la producción y la cantidad de repeticiones (R)... |
| Q101 | - |  |  | SI | ¿El paciente se encuentra fuera de la norma para C... |
| Q102 | - |  |  | SI | ¿El paciente se encuentra fuera de la norma para C... |
| Q103 | - |  |  | SI | (Toledo, et al. 2011) HOMBRES - Media: 2.3 ciclos ... |
| Q104 | - |  |  | SI | 4.5. INDIQUE CUALES SON LAS CARACTERÍSTICAS DE LA ... |
| Q105 | - |  |  | SI | CARACTERÍSTICAS DE LA ARTICULACIÓN DEL PACIENTE |
| Q106 | - |  |  | SI | 4.6. NATURALIDAD DEL HABLA |
| Q107 | - |  |  | SI | ¿El habla del paciente resulta poco natural según ... |
| Q108 | - |  |  | SI | ¿El habla del paciente resulta poco natural según ... |
| Q109 | - |  |  | SI | A opinión del paciente o acompañante, ¿su habla re... |
| Q11 | - |  |  | SI | ¿Existe asimetría en la contracción de la frente c... |
| Q110 | - |  |  | SI | A opinión del paciente o acompañante, ¿su habla re... |
| Q111 | - |  |  | SI | 4.7 COMPRENSIBILIDAD DEL HABLA |
| Q112 | - |  |  | SI | ¿El uso del lenguaje no verbal resulta poco eficie... |
| Q113 | - |  |  | SI | ¿El uso del lenguaje no verbal resulta poco eficie... |
| Q114 | - |  |  | SI | Sección: V SÍNTESIS. |
| Q115 | - |  |  | SI | 5.1. Tomando como base la información obtenida en ... |
| Q116 | - |  |  | SI | Identifique el(los) tipos(s) de disartria |
| Q117 | - |  |  | SI | 5.2. Tomando como base la inteligibilidad del habl... |
| Q118 | - |  |  | SI | Severidad del Trastorno |
| Q12 | - |  |  | SI | Al inflar sus mejillas. ¿Falla al intentar mantene... |
| Q13 | - |  |  | SI | Al inflar sus mejillas. ¿Falla al intentar mantene... |
| Q14 | - |  |  | SI | 1.2 MANDÍBULA |
| Q15 | - |  |  | SI | ¿Se desvía la mandíbula cuando realiza apertura bu... |
| Q16 | - |  |  | SI | ¿Se desvía la mandíbula cuando realiza apertura bu... |
| Q17 | - |  |  | SI | ¿Se desvía la mandíbula cuando realiza apertura bu... |
| Q18 | - |  |  | SI | 1.3 LENGUA |
| Q19 | - |  |  | SI | ¿Se desvía la lengua cuando realiza protrusión lin... |
| Q20 | - |  |  | SI | ¿Se desvía la lengua cuando realiza protrusión lin... |
| Q21 | - |  |  | SI | ¿Se desvía la lengua cuando realiza protrusión lin... |
| Q22 | - |  |  | SI | ¿Presenta dificultades para lograr mover en la len... |
| Q23 | - |  |  | SI | ¿Presenta dificultades para lograr mover en la len... |
| Q24 | - |  |  | SI | ¿Presenta dificultades para lograr mover en la len... |
| Q25 | - |  |  | SI | ¿Presenta dificultades para lograr mover en la len... |
| Q26 | - |  |  | SI | ¿Se observan fasciculaciones? |
| Q27 | - |  |  | SI | ¿Se observan fasciculaciones? Severidad |
| Q28 | - |  |  | SI | 1.4 FUNCIÓN VELAR |
| Q29 | - |  |  | SI | ¿Cuándo prolonga una /a/ el velo se mueve de forma... |
| Q30 | - |  |  | SI | ¿Cuándo prolonga una /a/ el velo se mueve de forma... |
| Q31 | - |  |  | SI | ¿Cuándo prolonga una /a/ el velo se mueve de forma... |
| Q32 | - |  |  | SI | Sección II. EVALUACIÓN INTEGRADA DE LA RESPIRACIÓN... |
| Q33 | - |  |  | SI | 2.1 TIEMPO MÁXIMO DE ESPIRACIÓN |
| Q34 | - |  |  | SI | Tras inspirar tan profundamente como sea posible ¿... |
| Q35 | - |  |  | SI | HOMBRES - Media: 21.4 seg. / D.S.: +- 1.36 seg. //... |
| Q36 | - |  |  | SI | Duración del primer intento:, ¿Se encuentra fuera ... |
| Q37 | - |  |  | SI | Duración del primer intento:, ¿Se encuentra fuera ... |
| Q38 | - |  |  | SI | Duración del segundo intento: ¿Se encuentra fuera ... |
| Q39 | - |  |  | SI | Duración del segundo intento: ¿Se encuentra fuera ... |
| Q40 | - |  |  | SI | 2.2 TIEMPO MÁXIMO DE FONACIÓN |
| Q41 | - |  |  | SI | Tras inspirar tan profundamente como sea posible. ... |
| Q42 | - |  |  | SI | HOMBRES - Media: 16.3 seg. / D.S.: +- 0.39 seg. //... |
| Q43 | - |  |  | SI | Duración del primer intento: ¿Se encuentra fuera d... |
| Q44 | - |  |  | SI | Duración del primer intento: ¿Se encuentra fuera d... |
| Q45 | - |  |  | SI | Duración del segundo intento: ¿Se encuentra fuera ... |
| Q46 | - |  |  | SI | Duración del segundo intento: ¿Se encuentra fuera ... |
| Q47 | - |  |  | SI | 2.3. RESONANCIA DE LA EMISIÓN |
| Q48 | - |  |  | SI | ¿Cuándo prolonga una /a/ se observa emisión nasal ... |
| Q49 | - |  |  | SI | ¿Cuándo prolonga una /a/ se observa emisión nasal ... |
| Q50 | - |  |  | SI | ¿Cuándo prolonga una /a/ se observa emisión nasal ... |
| Q51 | - |  |  | SI | ¿Cuándo prolonga una /a/ se aprecia hipernasalidad... |
| Q52 | - |  |  | SI | ¿Cuándo prolonga una /a/ se aprecia hipernasalidad... |
| Q53 | - |  |  | SI | 2.4 INDIQUE COMO ES LA INTENSIDAD DE LA VOZ |
| Q54 | - |  |  | SI | ¿Intensidad de la Voz? |
| Q55 | - |  |  | SI | 2.5. INDIQUE COMO ES LA CALIDAD DE LA VOZ |
| Q56 | - |  |  | SI | ¿Calidad de la Voz? |
| Q57 | - |  |  | SI | 2.6. INDIQUE COMO ES EL TONO DE LA VOZ |
| Q58 | - |  |  | SI | ¿Tono de la Voz? |
| Q59 | - |  |  | SI | Sección III. EVALUACIÓN DE LA PROSODIA |
| Q60 | - |  |  | SI | 3.1. Entregue al paciente la lámina 1, el paciente... |
| Q61 | - |  |  | SI | (Afirmación) - Vamos de viaje |
| Q62 | - |  |  | SI | (Afirmación) Vamos de viaje Severidad |
| Q63 | - |  |  | SI | (Pregunta) ¿Vamos de viaje? |
| Q64 | - |  |  | SI | (Pregunta) ¿Vamos de viaje? Severidad |
| Q65 | - |  |  | SI | (Afirmación) El auto es usado - ¿Falla? |
| Q66 | - |  |  | SI | (Afirmación) El auto es usado - ¿Falla? Severidad |
| Q67 | - |  |  | SI | (Pregunta) ¿El auto es usado? - ¿Falla? |
| Q68 | - |  |  | SI | (Pregunta) ¿El auto es usado? - ¿Falla? Severidad |
| Q69 | - |  |  | SI | (Afirmación) El pollo está en el horno - ¿Falla? |
| Q70 | - |  |  | SI | (Afirmación) El pollo está en el horno - ¿Falla? S... |
| Q71 | - |  |  | SI | (Feliz) Me gané un premio - ¿Falla? |
| Q72 | - |  |  | SI | (Feliz) Me gané un premio - ¿Falla?&nbsp |
| Q73 | - |  |  | SI | (Feliz) Me fue bien en la prueba - ¿Falla? |
| Q74 | - |  |  | SI | (Feliz) Me fue bien en la prueba - ¿Falla? Severid... |
| Q75 | - |  |  | SI | (Triste) Perdí todo mi dinero - ¿Falla? |
| Q76 | - |  |  | SI | (Triste) Perdí todo mi dinero - ¿Falla? Severidad |
| Q77 | - |  |  | SI | (Enojado) Te dije que no lo hicieras - ¿Falla? Sev... |
| Q77a | - |  |  | SI | (Enojado) Te dije que no lo hicieras - ¿Falla? |
| Q78 | - |  |  | SI | 3.2. INDIQUE CUALES SON LAS CARACTERÍSTICAS DE LA ... |
| Q79 | - |  |  | SI | CARACTERÍSTICAS DE LA PROSODIA DEL PACIENTE |
| Q80 | - |  |  | SI | Sección: IV. EVALUACIÓN INTEGRADA DE LA ARTICULACI... |
| Q81 | - |  |  | SI | 4.1. INTELIGIBILIDAD |
| Q82 | - |  |  | SI | Entregue al paciente la lámina 2, la cual contiene... |
| Q83 | - |  |  | SI | Posteriormente registre las palabras correctas (C)... |
| Q84 | - |  |  | SI | Respuestas |
| Q85 | - |  |  | SI | Total Correctas |
| Q86 | - |  |  | SI | Total % |
| Q87 | - |  |  | SI | 4.2. VELOCIDAD DEL HABLA |
| Q88 | - |  |  | SI | Solicite al paciente leer en voz alta la lámina 4,... |
| Q89 | - |  |  | SI | Tiempo de lectura (T) |
| Q90 | - |  |  | SI | Velocidad del habla (X = 13.560 /T) |
| Q91 | - |  |  | SI | La velocidad del habla se encuentra |
| Q92 | - |  |  | SI | 4.3. HABLA AUTOMÁTICA |
| Q93 | - |  |  | SI | Solicite al paciente que diga los días de la seman... |
| Q94 | - |  |  | SI | ¿Falla al decir los días de la semana y los número... |
| Q95 | - |  |  | SI | ¿Falla al decir los días de la semana y los número... |
| Q96 | - |  |  | SI | ¿Se observan variaciones en la intensidad de la vo... |
| Q97 | - |  |  | SI | ¿Se observan variaciones en la intensidad de la vo... |
| Q98 | - |  |  | SI | 4.4. DIADOCOCINESIAS ORALES |
| Q99 | - |  |  | SI | Solicite al paciente realizar una profunda inspira... |
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