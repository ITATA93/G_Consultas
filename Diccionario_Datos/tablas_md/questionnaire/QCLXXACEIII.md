# questionnaire.QCLXXACEIII

> ACE III

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile. *(ACE III)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | Responsable Evaluación |
| Q04 | varchar |  |  | SI | ADDENBROOKE’S COGNITIVE EXAMINATION – ACE-III   Ve... |
| Q05 | varchar |  |  | SI | ATENCION |
| Q06 | varchar |  |  | SI | Pregunte: ¿En que…estamos? |
| Q07 | varchar |  |  | SI | Pregunte: ¿En que…estamos? |
| Q08 | varchar |  |  | SI | Diga: “Le voy a decir 3 palabras y me gustaría que... |
| Q09 | numeric |  |  | SI | Registro número de ensayo |
| Q10 | varchar |  |  | SI | ¿Ahora por favor dígame cuánto es 100 menos 7?  … ... |
| Q11 | varchar |  |  | SI | MEMORIA |
| Q12 | varchar |  |  | SI | Diga: “¿Cuáles eran las 3 palabras que yo le pedí ... |
| Q13 | varchar |  |  | SI | FLUENCIA (CONTESTAR RECUEADRO PRINCIPIO PÁGINA) |
| Q14 | varchar |  |  | SI | Letras: Le voy a pedir que durante un minuto me di... |
| Q15 | varchar |  |  | SI | Cuantas palabra pudo decir ? |
| Q16 | varchar |  |  | SI | Animales: Diga: “¿Ahora dígame todos los animales ... |
| Q17 | varchar |  |  | SI | Cuantos Animales pudo decir ? |
| Q18 | varchar |  |  | SI | Diga: “Voy a decirle un nombre y una dirección y m... |
| Q19 | varchar |  |  | SI | Primer Ensayo |
| Q20 | varchar |  |  | SI | Segundo Ensayo |
| Q21 | varchar |  |  | SI | Tercer Ensayo (Valido) |
| Q22 | varchar |  |  | SI | Cual es el Nombre? |
| Q23 | varchar |  |  | SI | LENGUAJE |
| Q24 | varchar |  |  | SI | Ahora le voy a dar algunas instrucciones simples. |
| Q25 | varchar |  |  | SI | Diga al sujeto |
| Q26 | varchar |  |  | SI | Diga: “Me gustaría que escriba dos oraciones. Pued... |
| Q27 | varchar |  |  | SI | Por favor repita: ‘hipopótamo’,  ‘excentricidad’, ... |
| Q28 | varchar |  |  | SI | Por favor repita: ‘El flan tiene frutillas y framb... |
| Q29 | varchar |  |  | SI | Ahora repita: “La orquesta tocó y la audiencia apl... |
| Q30 | varchar |  |  | SI | Por favor lea en voz alta las siguientes palabras ... |
| Q31 | varchar |  |  | SI | Diagrama de Infinidad: Por favor copie este dibujo... |
| Q32 | varchar |  |  | SI | Cubo: Por favor copie este dibujo  |
| Q33 | varchar |  |  | SI | Pida al examinado que nombre las siguientes imagen... |
| Q34 | varchar |  |  | SI | Usando las imágenes que aparecen anteriormente, pi... |
| Q35 | varchar |  |  | SI | HABILIDADES VISOESPACIALES |
| Q36 | varchar |  |  | SI | Reloj: Por favor dibuje un reloj, con todos los nú... |
| Q37 | varchar |  |  | SI | Por favor cuente los puntos en cada cuadrado sin s... |
| Q38 | varchar |  |  | SI | Por favor dígame que letras son estas (Puntaje) |
| Q39 | varchar |  |  | SI | Diga: “Ahora dígame, por favor, lo que usted recue... |
| Q40 | varchar |  |  | SI | Sub-prueba de Memoria |
| Q41 | varchar |  |  | SI | PUNTAJE TOTAL ACE-III |
| Q42 | varchar |  |  | SI | Atención |
| Q43 | varchar |  |  | SI | Memoria |
| Q44 | varchar |  |  | SI | Fluencia |
| Q45 | varchar |  |  | SI | Lenguaje |
| Q46 | varchar |  |  | SI | Visoespacial |
| Q47 | numeric |  |  | SI | PUNTAJE TOTAL M-ACE |
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