# questionnaire.QCLXXPENS

> Pauta Evaluación Neurosensorial (PENS) Modificado

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta Evaluación Neurosensorial (PENS) Modificado

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo Evaluación |
| Q02 | date |  |  | SI | Fecha Evaluación |
| Q03 | varchar |  |  | SI | REFLEJOS DEL DESARROLLO |
| Q04 | varchar |  |  | SI | 1.&nbsp;Reflejo Moro |
| Q05 | varchar |  |  | SI | Metodología. Levantar y dejar caer suavemente la c... |
| Q06 | varchar |  |  | SI | 2.&nbsp;Postura esgrimista (PE) |
| Q07 | varchar |  |  | SI | Metodología: Mostrar un objeto y observar si apare... |
| Q08 | varchar |  |  | SI | 3. Reflejo Prensión Plantar |
| Q09 | varchar |  |  | SI | Metodología: Tocar, sin presionar la planta del pi... |
| Q10 | varchar |  |  | SI | 4.&nbsp;Reflejos de Succión y Deglución |
| Q11 | varchar |  |  | SI | Metodología: Observar reflejo de succión y aliment... |
| Q12 | varchar |  |  | SI | ANTROPOMETRÍA |
| Q13 | varchar |  |  | SI | 5. Perímetro Cefálico (PCe/E) |
| Q14 | varchar |  |  | SI | Metodología: Valorar Incremento de PCe. Evaluar y ... |
| Q15 | varchar |  |  | SI | 6.&nbsp;Talla (T/E) |
| Q16 | varchar |  |  | SI | Metodología: Evaluar y registrar en curva de creci... |
| Q17 | varchar |  |  | SI | 7. Peso (P/E) |
| Q18 | varchar |  |  | SI | Metodología: Evaluar y registrar en curva de creci... |
| Q19 | varchar |  |  | SI | PIEL |
| Q20 | varchar |  |  | SI | 8.&nbsp;Inspección de Piel |
| Q21 | varchar |  |  | SI | Metodología: Realizar inspección de la piel. |
| Q22 | varchar |  |  | SI | CONDUCTA Y COMUNICACIÓN |
| Q23 | varchar |  |  | SI | 9.&nbsp;Conducta (evaluación cualitativa) |
| Q24 | varchar |  |  | SI | Metodología: Preguntarle a la madre, padre o cuida... |
| Q25 | varchar |  |  | SI | 10.&nbsp;Llanto |
| Q26 | varchar |  |  | SI | Metodología: Observar durante la evaluación. Pregu... |
| Q27 | varchar |  |  | SI | 11. Consolabilidad |
| Q28 | varchar |  |  | SI | Metodología: Observar al acunarlo/a después de rea... |
| Q29 | varchar |  |  | SI | 12. Sonrisa Social* (2 meses) |
| Q30 | varchar |  |  | SI | Metodología: *Sólo en niños y niñas desde los 2 me... |
| Q31 | varchar |  |  | SI | MOVILIDAD |
| Q32 | varchar |  |  | SI | 13. Control Cefálico |
| Q33 | varchar |  |  | SI | imagen1 |
| Q34 | varchar |  |  | SI | imagem2 |
| Q35 | varchar |  |  | SI | Metodología: Traccionar suavemente desde los brazo... |
| Q36 | varchar |  |  | SI | 14. Movimientos espontáneos de extremidades |
| Q37 | varchar |  |  | SI | Metodología: Observar durante examen físico. |
| Q38 | varchar |  |  | SI | 15.&nbsp;Apertura de Manos |
| Q39 | varchar |  |  | SI | Metodología: Observar en movimientos espontáneos, ... |
| Q40 | varchar |  |  | SI | 16. Movilidad Facial |
| Q41 | varchar |  |  | SI | Metodología: Observar durante evaluación. |
| Q42 | varchar |  |  | SI | TONO |
| Q43 | varchar |  |  | SI | 17.&nbsp;Tono Axial |
| Q44 | varchar |  |  | SI | imagen3 |
| Q45 | varchar |  |  | SI | imagen4 |
| Q46 | varchar |  |  | SI | imagen 5 |
| Q47 | varchar |  |  | SI | Metodología: Observar al niño o niña en sus movimi... |
| Q48 | varchar |  |  | SI | VISIÓN |
| Q49 | varchar |  |  | SI | 18.&nbsp;Rojo Pupilar |
| Q50 | varchar |  |  | SI | Metodología: Evaluar simultáneamente a 50 cm los o... |
| Q51 | varchar |  |  | SI | 19.&nbsp;Mira fijamente al examinador/a y sigue un... |
| Q52 | varchar |  |  | SI | Metodología: Observar si fija la mirada y sigue un... |
| Q53 | varchar |  |  | SI | AUDICIÓN |
| Q54 | varchar |  |  | SI | 20.&nbsp;Reacciona frente a ruido fuerte |
| Q55 | varchar |  |  | SI | Metodología: Aplaudir fuerte o dejar caer algo, pr... |
| Q56 | varchar |  |  | SI | RESULTADO |
| Q57 | varchar |  |  | SI | PUNTAJE |
| Q58 | varchar |  |  | SI | ACCIÓN |
| Q59 | varchar |  |  | SI | Normal |
| Q60 | varchar |  |  | SI | 0 puntos |
| Q61 | varchar |  |  | SI | Continuar con calendario de controles habituales y... |
| Q62 | varchar |  |  | SI | Anormal |
| Q63 | varchar |  |  | SI | 1 - 3 puntos |
| Q64 | varchar |  |  | SI | Repetir PENS en control de los 2 meses, si persist... |
| Q65 | varchar |  |  | SI | Muy Anormal |
| Q66 | varchar |  |  | SI | ≥4 puntos y/o microcefalia y/o macrocefalia y/o ro... |
| Q67 | varchar |  |  | SI | Derivar a especialista en nivel secundario |
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