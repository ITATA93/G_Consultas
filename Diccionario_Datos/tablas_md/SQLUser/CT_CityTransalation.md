# SQLUser.CT_CityTransalation

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CITYTRANS_RowId | bigint | PK |  | NO | - |
| CITYTRANS_Code | varchar |  |  | NO | Abbreviation |
| CITYTRANS_CodeTableTags | varchar |  |  | SI | - |
| CITYTRANS_CreatedDate | date |  |  | SI | Created Date |
| CITYTRANS_CreatedTime | time |  |  | SI | Created Time |
| CITYTRANS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CITYTRANS_Desc | varchar |  |  | NO | Description |
| CITYTRANS_Owner | varchar |  |  | SI | - |
| CITYTRANS_UpdatedDate | date |  |  | SI | Updated Date |
| CITYTRANS_UpdatedTime | time |  |  | SI | Updated Time |
| CITYTRANS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | I. Denominación |
| Q02 | - |  |  | SI | 1. Lápiz |
| Q03 | - |  |  | SI | 2. Mano |
| Q04 | - |  |  | SI | 3. Pulgar |
| Q05 | - |  |  | SI | 4. Reloj |
| Q06 | - |  |  | SI | 5. Techo |
| Q07 | - |  |  | SI | II. Habla Automática |
| Q08 | - |  |  | SI | 1. Contar del 1 al 10 |
| Q09 | - |  |  | SI | 2. Los días de la semana |
| Q10 | - |  |  | SI | 3. Más vale pájaro en mano… |
| Q11 | - |  |  | SI | 4. Perro que ladra… |
| Q12 | - |  |  | SI | 5. No por mucho madrugar… |
| Q13 | - |  |  | SI | III. Repetición |
| Q14 | - |  |  | SI | 1. Tarro |
| Q15 | - |  |  | SI | 2. Zanahoria |
| Q16 | - |  |  | SI | 3. Abecedario |
| Q17 | - |  |  | SI | 4. Debajo del viejo puente de madera |
| Q18 | - |  |  | SI | 5. La plateada luna brilla en la oscura noche |
| Q19 | - |  |  | SI | IV. Respuestas de Si/No |
| Q20 | - |  |  | SI | 1. ¿Te llamas ________? (Cambiamos su nombre) |
| Q21 | - |  |  | SI | 2. ¿Te llamas ________? (Su nombre) |
| Q22 | - |  |  | SI | 3. ¿Estamos en ______? (Cambiamos el lugar) |
| Q23 | - |  |  | SI | 4. ¿Estamos en ________? (Lugar correcto) |
| Q24 | - |  |  | SI | 5. ¿Te pones los guantes en los pies? |
| Q25 | - |  |  | SI | 7. ¿El lunes viene antes que el martes? |
| Q26 | - |  |  | SI | 8. ¿El verano viene después que la primavera? |
| Q27 | - |  |  | SI | 9. ¿Un pollo es tan grande como una araña? |
| Q28 | - |  |  | SI | 10. ¿Te pones el zapato antes que el calcetín? |
| Q29 | - |  |  | SI | V. Reconocimiento de Objetos |
| Q30 | - |  |  | SI | 1. Reloj |
| Q31 | - |  |  | SI | 2. Llaves |
| Q32 | - |  |  | SI | 3. Libro |
| Q33 | - |  |  | SI | 4. Papel |
| Q34 | - |  |  | SI | 5. Lápiz |
| Q35 | - |  |  | SI | VI. Órdenes Verbales |
| Q36 | - |  |  | SI | 1. Tócate la nariz |
| Q37 | - |  |  | SI | 2. Abre la boca |
| Q38 | - |  |  | SI | 3. Con la mano izquierda, tócate el ojo derecho |
| Q39 | - |  |  | SI | 4. Señala el suelo, después tócate la nariz |
| Q40 | - |  |  | SI | 5. Tócate la oreja antes de abrir la boca |
| Q41 | - |  |  | SI | VII. Órdenes Escritas |
| Q42 | - |  |  | SI | 1. Abre la boca |
| Q43 | - |  |  | SI | 2. Cierra la mano |
| Q44 | - |  |  | SI | 3. Señala el suelo, después señala el techo |
| Q45 | - |  |  | SI | 4. Con la mano derecha, tócate la rodilla izquierd... |
| Q46 | - |  |  | SI | 5. Tócate la oreja izquierda y después cierra la m... |
| Q47 | - |  |  | SI | VIII. Escritura |
| Q48 | - |  |  | SI | 1. Silla |
| Q49 | - |  |  | SI | 2. Girar |
| Q50 | - |  |  | SI | 3. Aeroplano |
| Q51 | - |  |  | SI | 4. Computador |
| Q52 | - |  |  | SI | 5. Bajo el puente negro |
| Q53 | - |  |  | SI | IX. Expresión Oral |
| Q54 | - |  |  | SI | Expresión Oral |
| Q55 | - |  |  | SI | 6. ¿Estoy tocándome el ojo? (nos tocamos la nariz) |
| Q56 | - |  |  | SI | Resultado Índice Comprensivo |
| Q57 | - |  |  | SI | Resultado Índice Expresivo |
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