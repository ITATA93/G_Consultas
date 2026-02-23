# questionnaire.QCLXXMAST

> Test de Cribado de Afasia (MAST)

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de Cribado de Afasia (MAST)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | I. Denominación |
| Q02 | varchar |  |  | SI | 1. Lápiz |
| Q03 | varchar |  |  | SI | 2. Mano |
| Q04 | varchar |  |  | SI | 3. Pulgar |
| Q05 | varchar |  |  | SI | 4. Reloj |
| Q06 | varchar |  |  | SI | 5. Techo |
| Q07 | varchar |  |  | SI | II. Habla Automática |
| Q08 | varchar |  |  | SI | 1. Contar del 1 al 10 |
| Q09 | varchar |  |  | SI | 2. Los días de la semana |
| Q10 | varchar |  |  | SI | 3. Más vale pájaro en mano… |
| Q11 | varchar |  |  | SI | 4. Perro que ladra… |
| Q12 | varchar |  |  | SI | 5. No por mucho madrugar… |
| Q13 | varchar |  |  | SI | III. Repetición |
| Q14 | varchar |  |  | SI | 1. Tarro |
| Q15 | varchar |  |  | SI | 2. Zanahoria |
| Q16 | varchar |  |  | SI | 3. Abecedario |
| Q17 | varchar |  |  | SI | 4. Debajo del viejo puente de madera |
| Q18 | varchar |  |  | SI | 5. La plateada luna brilla en la oscura noche |
| Q19 | varchar |  |  | SI | IV. Respuestas de Si/No |
| Q20 | varchar |  |  | SI | 1. ¿Te llamas ________? (Cambiamos su nombre) |
| Q21 | varchar |  |  | SI | 2. ¿Te llamas ________? (Su nombre) |
| Q22 | varchar |  |  | SI | 3. ¿Estamos en ______? (Cambiamos el lugar) |
| Q23 | varchar |  |  | SI | 4. ¿Estamos en ________? (Lugar correcto) |
| Q24 | varchar |  |  | SI | 5. ¿Te pones los guantes en los pies? |
| Q25 | varchar |  |  | SI | 7. ¿El lunes viene antes que el martes? |
| Q26 | varchar |  |  | SI | 8. ¿El verano viene después que la primavera? |
| Q27 | varchar |  |  | SI | 9. ¿Un pollo es tan grande como una araña? |
| Q28 | varchar |  |  | SI | 10. ¿Te pones el zapato antes que el calcetín? |
| Q29 | varchar |  |  | SI | V. Reconocimiento de Objetos |
| Q30 | varchar |  |  | SI | 1. Reloj |
| Q31 | varchar |  |  | SI | 2. Llaves |
| Q32 | varchar |  |  | SI | 3. Libro |
| Q33 | varchar |  |  | SI | 4. Papel |
| Q34 | varchar |  |  | SI | 5. Lápiz |
| Q35 | varchar |  |  | SI | VI. Órdenes Verbales |
| Q36 | varchar |  |  | SI | 1. Tócate la nariz |
| Q37 | varchar |  |  | SI | 2. Abre la boca |
| Q38 | varchar |  |  | SI | 3. Con la mano izquierda, tócate el ojo derecho |
| Q39 | varchar |  |  | SI | 4. Señala el suelo, después tócate la nariz |
| Q40 | varchar |  |  | SI | 5. Tócate la oreja antes de abrir la boca |
| Q41 | varchar |  |  | SI | VII. Órdenes Escritas |
| Q42 | varchar |  |  | SI | 1. Abre la boca |
| Q43 | varchar |  |  | SI | 2. Cierra la mano |
| Q44 | varchar |  |  | SI | 3. Señala el suelo, después señala el techo |
| Q45 | varchar |  |  | SI | 4. Con la mano derecha, tócate la rodilla izquierd... |
| Q46 | varchar |  |  | SI | 5. Tócate la oreja izquierda y después cierra la m... |
| Q47 | varchar |  |  | SI | VIII. Escritura |
| Q48 | varchar |  |  | SI | 1. Silla |
| Q49 | varchar |  |  | SI | 2. Girar |
| Q50 | varchar |  |  | SI | 3. Aeroplano |
| Q51 | varchar |  |  | SI | 4. Computador |
| Q52 | varchar |  |  | SI | 5. Bajo el puente negro |
| Q53 | varchar |  |  | SI | IX. Expresión Oral |
| Q54 | varchar |  |  | SI | Expresión Oral |
| Q55 | varchar |  |  | SI | 6. ¿Estoy tocándome el ojo? (nos tocamos la nariz) |
| Q56 | varchar |  |  | SI | Resultado Índice Comprensivo |
| Q57 | varchar |  |  | SI | Resultado Índice Expresivo |
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