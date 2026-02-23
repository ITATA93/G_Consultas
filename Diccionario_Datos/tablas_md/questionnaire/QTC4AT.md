# questionnaire.QTC4AT

> Evaluación de delirio y deterioro cognitivo (4AT)

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de delirio y deterioro cognitivo (4AT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | [1] Alerta |
| Q04 | varchar |  |  | SI | [2] Prueba mental abreviada (AMT4) |
| Q05 | varchar |  |  | SI | Preguntar: Edad, fecha de nacimiento, lugar, año a... |
| Q06 | varchar |  |  | SI | [3] Atención  |
| Q07 | varchar |  |  | SI | Pregunte: meses del año al revés |
| Q08 | varchar |  |  | SI | [4] Cambio agudo o curso fluctuante |
| Q09 | varchar |  |  | SI | Estado de alerta, cognición, otras funciones menta... |
| Q10 | varchar |  |  | SI | [1] ALERTA |
| Q11 | varchar |  |  | SI | Esto incluye pacientes que pueden estar marcadamen... |
| Q12 | varchar |  |  | SI | Pida al paciente que indique su nombre y dirección... |
| Q13 | varchar |  |  | SI | Agitado / Hiperactivo. observar al paciente. Si es... |
| Q14 | varchar |  |  | SI | [2] AMT4 |
| Q15 | varchar |  |  | SI | Edad, fecha de nacimiento, lugar (nombre del hospi... |
| Q16 | varchar |  |  | SI | [3] ATENCIÓN |
| Q17 | varchar |  |  | SI | Pregúntele al paciente: Por favor, dígame los mese... |
| Q18 | varchar |  |  | SI | Para ayudar a la comprensión inicial, un mensaje d... |
| Q19 | varchar |  |  | SI | [4] CAMBIO AGUDO O CURSO FLUCTUANTE |
| Q20 | varchar |  |  | SI | Evidencia de cambios significativos o fluctuacione... |
| Q21 | varchar |  |  | SI | El 4AT es un instrumento de detección diseñado par... |
| Q22 | varchar |  |  | SI | Una puntuación de 4 o más sugiere delirio pero no ... |
| Q23 | varchar |  |  | SI | Una puntuación de 1 a 3 sugiere deterioro cognitiv... |
| Q24 | varchar |  |  | SI | Una puntuación de 0 no excluye definitivamente el ... |
| Q25 | varchar |  |  | SI | Deterioro: es posible que se requieran pruebas más... |
| Q26 | varchar |  |  | SI | Los ítems 1-3 se califican únicamente en base a la... |
| Q27 | varchar |  |  | SI | su propio conocimiento del paciente, otro personal... |
| Q28 | varchar |  |  | SI | El examinador debe tener en cuenta las dificultade... |
| Q29 | varchar |  |  | SI | El nivel alterado de alerta es muy probable que se... |
| Q30 | varchar |  |  | SI | Si el paciente muestra un estado de alerta alterad... |
| Q31 | varchar |  |  | SI | AMT4 (Prueba Mental Abreviada - 4): Esta puntuació... |
| Q32 | varchar |  |  | SI | La fluctuación puede ocurrir sin delirio en alguno... |
| Q33 | varchar |  |  | SI | Para ayudar a provocar alucinaciones y/o pensamien... |
| Q34 | varchar |  |  | SI | ¿Estás preocupado por algo que esté pasando aquí?;... |
| Q35 | varchar |  |  | SI | Tenga en cuenta que el 4AT no está diseñado para l... |
| Q36 | varchar |  |  | SI | El nivel alterado de excitación (ítem 1) y el camb... |
| Q37 | varchar |  |  | SI | junto con el juicio clínico general y/o el uso de ... |
| Q38 | varchar |  |  | SI | Puntaje |
| Q39 | varchar |  |  | SI | Alertas: |
| Q40 | varchar |  |  | SI | Clasificación |
| Q41 | varchar |  |  | SI | ≥ 4 |
| Q42 | varchar |  |  | SI | Posible delirio +/- deterioro cognitivo |
| Q43 | varchar |  |  | SI | 1-3 |
| Q44 | varchar |  |  | SI | Posible deterioro cognitivo |
| Q45 | varchar |  |  | SI | 0 |
| Q46 | varchar |  |  | SI | Delirio o deterioro cognitivo grave poco probable ... |
| Q47 | varchar |  |  | SI | El 4AT es una herramienta clínica para la detecció... |
| Q48 | varchar |  |  | SI | >= 4: Posible delirio +/- deterioro cognitivo |
| Q49 | varchar |  |  | SI | 1-3: Posible deterioro cognitivo |
| Q50 | varchar |  |  | SI | 0: delirio o deterioro cognitivo grave improbable ... |
| Q51 | varchar |  |  | SI | Comentarios adicionales |
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