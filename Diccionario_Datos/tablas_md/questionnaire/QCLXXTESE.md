# questionnaire.QCLXXTESE

> Mini-BESTest: Test de evaluación de los sistemas de equilibrio

**Schema:** questionnaire
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mini-BESTest: Test de evaluación de los sistemas de equilibrio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | varchar |  |  | SI | Evaluador/a |
| Q03 | varchar |  |  | SI | ANTICIPATORIO |
| Q04 | varchar |  |  | SI | 1. SENTADO DE PIE |
| Q05 | varchar |  |  | SI | Instrucción: Cruce los brazos sobre el tórax. Inte... |
| Q06 | varchar |  |  | SI | 2. PONERSE DE PUNTILLAS |
| Q07 | varchar |  |  | SI | Instrucción: Coloque sus pies separados a la anchu... |
| Q08 | varchar |  |  | SI | Intente mantenerse en esa posición al menos 3 segu... |
| Q09 | varchar |  |  | SI | 3. APOYO MONOPODAL |
| Q10 | varchar |  |  | SI | Instrucción: Mire al frente. Mantenga las manos en... |
| Q11 | varchar |  |  | SI | Mire al frente. Levante ahora. |
| Q12 | varchar |  |  | SI | Izquierdo |
| Q13 | varchar |  |  | SI | Derecho |
| Q14 | numeric |  |  | SI | Tiempo Prueba 1 |
| Q15 | varchar |  |  | SI | segundos |
| Q16 | numeric |  |  | SI | Tiempo Prueba 2 |
| Q17 | varchar |  |  | SI | segundos |
| Q18 | numeric |  |  | SI | Tiempo Prueba 1 |
| Q19 | varchar |  |  | SI | segundos |
| Q20 | numeric |  |  | SI | Tiempo Prueba 2 |
| Q21 | varchar |  |  | SI | segundos |
| Q22 | varchar |  |  | SI | Para registrar cada lado por separado use la prueb... |
| Q23 | varchar |  |  | SI | SUBPUNTUACIÓN ANTICIPATORIO |
| Q24 | varchar |  |  | SI | /6 |
| Q25 | varchar |  |  | SI | CONTROL POSTURAL REACTIVO |
| Q26 | varchar |  |  | SI | 4. CORRECCIÓN COMPENSATORIA CON UN PASO-HACIA DELA... |
| Q27 | varchar |  |  | SI | Instrucción: Coloque sus pies separados a la anchu... |
| Q28 | varchar |  |  | SI | Cuando lo suelte haga lo que sea necesario, inclui... |
| Q29 | varchar |  |  | SI | 5. CORRECCIÓN COMPENSATORIA CON UN PASO-HACIA ATRÁ... |
| Q30 | varchar |  |  | SI | Instrucción: Coloque sus pies separados a la anchu... |
| Q31 | varchar |  |  | SI | Cuando lo suelte haga lo que sea necesario, inclui... |
| Q32 | varchar |  |  | SI | 6. CORRECCIÓN COMPENSATORIA CON UN PASO-LATERAL |
| Q33 | varchar |  |  | SI | Instrucción: De pie con los pies juntos, brazos a ... |
| Q34 | varchar |  |  | SI | Use el lado con la puntuación más baja para calcul... |
| Q35 | varchar |  |  | SI | Izquierda |
| Q36 | varchar |  |  | SI | Derecha |
| Q37 | varchar |  |  | SI | SUBPUNTUACIÓN CONTROL POSTURAL REACTIVO |
| Q38 | varchar |  |  | SI | /6 |
| Q39 | varchar |  |  | SI | ORIENTACIÓN SENSORIAL |
| Q40 | varchar |  |  | SI | 7. DE PIE (PIES JUNTOS); OJOS ABIERTOS, SUPERFICIE... |
| Q41 | varchar |  |  | SI | Instrucción: Coloque sus manos en sus caderas. Col... |
| Q42 | varchar |  |  | SI | 8. DE PIE (PIES JUNTOS): OJOS CERRADOS. SUPERFICIE... |
| Q43 | varchar |  |  | SI | Instrucción Póngase en la gomaespuma. Coloque sus ... |
| Q44 | varchar |  |  | SI | Comenzaré a cronometrar cuando cierre sus ojos. |
| Q45 | varchar |  |  | SI | 9. INCLINADO OJOS CERRADOS |
| Q46 | varchar |  |  | SI | Intrucción: Sitúese en la rampa inclinada. Coloque... |
| Q47 | varchar |  |  | SI | Comenzaré a cronometrar cuando cierre sus ojos. |
| Q48 | varchar |  |  | SI | SUBPUNTUACIÓN ORIENTACIÓN SENSORIAL |
| Q49 | varchar |  |  | SI | /6 |
| Q50 | varchar |  |  | SI | MARCHA DINÁMICA |
| Q51 | varchar |  |  | SI | 10. CAMBIO EN LA VELOCIDAD DE MARCHA |
| Q52 | varchar |  |  | SI | Instrucción: Comience a caminar a su velocidad nor... |
| Q53 | varchar |  |  | SI | 11. CAMINAR CON GIROS DE CABEZA – HORIZONTAL |
| Q54 | varchar |  |  | SI | Instrucción: Comience caminando a su velocidad hab... |
| Q55 | varchar |  |  | SI | Intente mantenerse caminando en línea recta. |
| Q56 | varchar |  |  | SI | 12. CAMINAR CON GIROS DE PIVOTE |
| Q57 | varchar |  |  | SI | 13. PASO POR ENCIMA DE OBSTÁCULOS |
| Q58 | varchar |  |  | SI | Instrucción: Comience caminando a su velocidad hab... |
| Q59 | varchar |  |  | SI | 14. TEST UP &amp; GO (TUG) (en español: “LEVANTARS... |
| Q60 | varchar |  |  | SI | Instrucción TUG: Cuando le diga “vaya”, levántese ... |
| Q61 | varchar |  |  | SI | Instrucción TUG con doble tarea: “Cuente hacia atr... |
| Q62 | varchar |  |  | SI | dé la vuelta y siéntese en la silla. Continúe cont... |
| Q63 | numeric |  |  | SI | TUG |
| Q64 | varchar |  |  | SI | segundos |
| Q65 | numeric |  |  | SI | TUG doble tarea |
| Q66 | varchar |  |  | SI | segundos |
| Q67 | varchar |  |  | SI | SUBPUNTUACIÓN MARCHA DINÁMICA |
| Q68 | varchar |  |  | SI | /10 |
| Q69 | varchar |  |  | SI | PUNTUACIÓN TOTAL&nbsp; |
| Q70 | varchar |  |  | SI | /28 |
| Q71 | varchar |  |  | SI | Instrucción: Comience caminando a su velocidad hab... |
| Q72 | varchar |  |  | SI | Cuando puntúe el ítem 14, si la velocidad del suje... |
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