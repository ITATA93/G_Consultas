# SQLUser.BLC_ContractDetailsDateItems

**Schema:** SQLUser
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | BLC_ContractDetailsDate Parent Reference |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_Department_DR | bigint |  | FK | SI | Des Ref Department |
| ITM_EpisodeType | varchar |  |  | SI | Episode Type |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tipo Evaluación |
| Q02 | - |  |  | SI | Fecha Evaluación |
| Q03 | - |  |  | SI | REFLEJOS DEL DESARROLLO |
| Q04 | - |  |  | SI | 1.&nbsp |
| Q05 | - |  |  | SI | Metodología. Levantar y dejar caer suavemente la c... |
| Q06 | - |  |  | SI | 2.&nbsp |
| Q07 | - |  |  | SI | Metodología: Mostrar un objeto y observar si apare... |
| Q08 | - |  |  | SI | 3. Reflejo Prensión Plantar |
| Q09 | - |  |  | SI | Metodología: Tocar, sin presionar la planta del pi... |
| Q10 | - |  |  | SI | 4.&nbsp |
| Q11 | - |  |  | SI | Metodología: Observar reflejo de succión y aliment... |
| Q12 | - |  |  | SI | ANTROPOMETRÍA |
| Q13 | - |  |  | SI | 5. Perímetro Cefálico (PCe/E) |
| Q14 | - |  |  | SI | Metodología: Valorar Incremento de PCe. Evaluar y ... |
| Q15 | - |  |  | SI | 6.&nbsp |
| Q16 | - |  |  | SI | Metodología: Evaluar y registrar en curva de creci... |
| Q17 | - |  |  | SI | 7. Peso (P/E) |
| Q18 | - |  |  | SI | Metodología: Evaluar y registrar en curva de creci... |
| Q19 | - |  |  | SI | PIEL |
| Q20 | - |  |  | SI | 8.&nbsp |
| Q21 | - |  |  | SI | Metodología: Realizar inspección de la piel. |
| Q22 | - |  |  | SI | CONDUCTA Y COMUNICACIÓN |
| Q23 | - |  |  | SI | 9.&nbsp |
| Q24 | - |  |  | SI | Metodología: Preguntarle a la madre, padre o cuida... |
| Q25 | - |  |  | SI | 10.&nbsp |
| Q26 | - |  |  | SI | Metodología: Observar durante la evaluación. Pregu... |
| Q27 | - |  |  | SI | 11. Consolabilidad |
| Q28 | - |  |  | SI | Metodología: Observar al acunarlo/a después de rea... |
| Q29 | - |  |  | SI | 12. Sonrisa Social* (2 meses) |
| Q30 | - |  |  | SI | Metodología: *Sólo en niños y niñas desde los 2 me... |
| Q31 | - |  |  | SI | MOVILIDAD |
| Q32 | - |  |  | SI | 13. Control Cefálico |
| Q33 | - |  |  | SI | imagen1 |
| Q34 | - |  |  | SI | imagem2 |
| Q35 | - |  |  | SI | Metodología: Traccionar suavemente desde los brazo... |
| Q36 | - |  |  | SI | 14. Movimientos espontáneos de extremidades |
| Q37 | - |  |  | SI | Metodología: Observar durante examen físico. |
| Q38 | - |  |  | SI | 15.&nbsp |
| Q39 | - |  |  | SI | Metodología: Observar en movimientos espontáneos, ... |
| Q40 | - |  |  | SI | 16. Movilidad Facial |
| Q41 | - |  |  | SI | Metodología: Observar durante evaluación. |
| Q42 | - |  |  | SI | TONO |
| Q43 | - |  |  | SI | 17.&nbsp |
| Q44 | - |  |  | SI | imagen3 |
| Q45 | - |  |  | SI | imagen4 |
| Q46 | - |  |  | SI | imagen 5 |
| Q47 | - |  |  | SI | Metodología: Observar al niño o niña en sus movimi... |
| Q48 | - |  |  | SI | VISIÓN |
| Q49 | - |  |  | SI | 18.&nbsp |
| Q50 | - |  |  | SI | Metodología: Evaluar simultáneamente a 50 cm los o... |
| Q51 | - |  |  | SI | 19.&nbsp |
| Q52 | - |  |  | SI | Metodología: Observar si fija la mirada y sigue un... |
| Q53 | - |  |  | SI | AUDICIÓN |
| Q54 | - |  |  | SI | 20.&nbsp |
| Q55 | - |  |  | SI | Metodología: Aplaudir fuerte o dejar caer algo, pr... |
| Q56 | - |  |  | SI | RESULTADO |
| Q57 | - |  |  | SI | PUNTAJE |
| Q58 | - |  |  | SI | ACCIÓN |
| Q59 | - |  |  | SI | Normal |
| Q60 | - |  |  | SI | 0 puntos |
| Q61 | - |  |  | SI | Continuar con calendario de controles habituales y... |
| Q62 | - |  |  | SI | Anormal |
| Q63 | - |  |  | SI | 1 - 3 puntos |
| Q64 | - |  |  | SI | Repetir PENS en control de los 2 meses, si persist... |
| Q65 | - |  |  | SI | Muy Anormal |
| Q66 | - |  |  | SI | ≥4 puntos y/o microcefalia y/o macrocefalia y/o ro... |
| Q67 | - |  |  | SI | Derivar a especialista en nivel secundario |
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