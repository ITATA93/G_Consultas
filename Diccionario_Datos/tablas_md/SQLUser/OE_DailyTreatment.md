# SQLUser.OE_DailyTreatment

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DTR_RowId | bigint | PK |  | NO | - |
| DTR_Adm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| DTR_DateCreated | date |  |  | SI | DateCreated |
| DTR_DateExpiry | date |  |  | SI | DateExpiry |
| DTR_Number | varchar |  |  | SI | Number |
| DTR_OEOrder_DR | numeric |  | FK | SI | Des Ref OEOrder |
| DTR_Status | varchar |  |  | SI | Status |
| DTR_TimeCreated | time |  |  | SI | TimeCreated |
| DTR_TimeExpiry | time |  |  | SI | TimeExpiry |
| DTR_UserCreated_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | [1] Alerta |
| Q04 | - |  |  | SI | [2] Prueba mental abreviada (AMT4) |
| Q05 | - |  |  | SI | Preguntar: Edad, fecha de nacimiento, lugar, año a... |
| Q06 | - |  |  | SI | [3] Atención |
| Q07 | - |  |  | SI | Pregunte: meses del año al revés |
| Q08 | - |  |  | SI | [4] Cambio agudo o curso fluctuante |
| Q09 | - |  |  | SI | Estado de alerta, cognición, otras funciones menta... |
| Q10 | - |  |  | SI | [1] ALERTA |
| Q11 | - |  |  | SI | Esto incluye pacientes que pueden estar marcadamen... |
| Q12 | - |  |  | SI | Pida al paciente que indique su nombre y dirección... |
| Q13 | - |  |  | SI | Agitado / Hiperactivo. observar al paciente. Si es... |
| Q14 | - |  |  | SI | [2] AMT4 |
| Q15 | - |  |  | SI | Edad, fecha de nacimiento, lugar (nombre del hospi... |
| Q16 | - |  |  | SI | [3] ATENCIÓN |
| Q17 | - |  |  | SI | Pregúntele al paciente: Por favor, dígame los mese... |
| Q18 | - |  |  | SI | Para ayudar a la comprensión inicial, un mensaje d... |
| Q19 | - |  |  | SI | [4] CAMBIO AGUDO O CURSO FLUCTUANTE |
| Q20 | - |  |  | SI | Evidencia de cambios significativos o fluctuacione... |
| Q21 | - |  |  | SI | El 4AT es un instrumento de detección diseñado par... |
| Q22 | - |  |  | SI | Una puntuación de 4 o más sugiere delirio pero no ... |
| Q23 | - |  |  | SI | Una puntuación de 1 a 3 sugiere deterioro cognitiv... |
| Q24 | - |  |  | SI | Una puntuación de 0 no excluye definitivamente el ... |
| Q25 | - |  |  | SI | Deterioro: es posible que se requieran pruebas más... |
| Q26 | - |  |  | SI | Los ítems 1-3 se califican únicamente en base a la... |
| Q27 | - |  |  | SI | su propio conocimiento del paciente, otro personal... |
| Q28 | - |  |  | SI | El examinador debe tener en cuenta las dificultade... |
| Q29 | - |  |  | SI | El nivel alterado de alerta es muy probable que se... |
| Q30 | - |  |  | SI | Si el paciente muestra un estado de alerta alterad... |
| Q31 | - |  |  | SI | AMT4 (Prueba Mental Abreviada - 4): Esta puntuació... |
| Q32 | - |  |  | SI | La fluctuación puede ocurrir sin delirio en alguno... |
| Q33 | - |  |  | SI | Para ayudar a provocar alucinaciones y/o pensamien... |
| Q34 | - |  |  | SI | ¿Estás preocupado por algo que esté pasando aquí? |
| Q35 | - |  |  | SI | Tenga en cuenta que el 4AT no está diseñado para l... |
| Q36 | - |  |  | SI | El nivel alterado de excitación (ítem 1) y el camb... |
| Q37 | - |  |  | SI | junto con el juicio clínico general y/o el uso de ... |
| Q38 | - |  |  | SI | Puntaje |
| Q39 | - |  |  | SI | Alertas: |
| Q40 | - |  |  | SI | Clasificación |
| Q41 | - |  |  | SI | ≥ 4 |
| Q42 | - |  |  | SI | Posible delirio +/- deterioro cognitivo |
| Q43 | - |  |  | SI | 1-3 |
| Q44 | - |  |  | SI | Posible deterioro cognitivo |
| Q45 | - |  |  | SI | 0 |
| Q46 | - |  |  | SI | Delirio o deterioro cognitivo grave poco probable ... |
| Q47 | - |  |  | SI | El 4AT es una herramienta clínica para la detecció... |
| Q48 | - |  |  | SI | >= 4: Posible delirio +/- deterioro cognitivo |
| Q49 | - |  |  | SI | 1-3: Posible deterioro cognitivo |
| Q50 | - |  |  | SI | 0: delirio o deterioro cognitivo grave improbable ... |
| Q51 | - |  |  | SI | Comentarios adicionales |
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