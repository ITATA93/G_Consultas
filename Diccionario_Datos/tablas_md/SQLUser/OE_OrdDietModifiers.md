# SQLUser.OE_OrdDietModifiers

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DM_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| DM_Childsub | double |  |  | NO | Childsub |
| DM_DietModifier_DR | bigint |  | FK | SI | Des Ref DietModifier |
| DM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | 1. En las últimas 4 semanas, ¿Cuán a menudo usted ... |
| Q02 | - |  |  | SI | 2.&nbsp |
| Q03 | - |  |  | SI | 3. En las últimas 4 semanas, ¿Con cuánta frecuenci... |
| Q04 | - |  |  | SI | 4. En las últimas 4 semanas, ¿Cómo clasifica su ni... |
| Q05 | - |  |  | SI | 5. En las últimas 4 semanas, ¿Cuánta confianza tie... |
| Q06 | - |  |  | SI | 6. En las últimas 4 semanas, ¿Con qué frecuencia s... |
| Q07 | - |  |  | SI | 7. En las últimas 4 semanas, ¿Con cuánta frecuenci... |
| Q08 | - |  |  | SI | 8. En las últimas 4 semanas, ¿le es difícil lubric... |
| Q09 | - |  |  | SI | 9. En las últimas 4 semanas, ¿Con qué frecuencia m... |
| Q10 | - |  |  | SI | 10. En las últimas 4 semanas, ¿Le es difícil mante... |
| Q11 | - |  |  | SI | 11. En las últimas 4 semanas, cuando usted tiene e... |
| Q12 | - |  |  | SI | 12. En las últimas 4 semanas, cuando usted tiene e... |
| Q13 | - |  |  | SI | 13. En las últimas 4 semanas, ¿Cuán satisfecha est... |
| Q14 | - |  |  | SI | 14. En las últimas 4 semanas, ¿Cuán satisfecha est... |
| Q15 | - |  |  | SI | 15. En las últimas 4 semanas, ¿Cuán satisfecha est... |
| Q16 | - |  |  | SI | 16. En las últimas 4 semanas, ¿Cuán satisfecha est... |
| Q17 | - |  |  | SI | 17. En las últimas 4 semanas, ¿Cuán a menudo sient... |
| Q18 | - |  |  | SI | 18. En las últimas 4 semanas, ¿Cuán a menudo sient... |
| Q19 | - |  |  | SI | 19. En las últimas 4 semanas, ¿Cómo clasifica su n... |
| Q20 | - |  |  | SI | Puntaje Deseo |
| Q21 | - |  |  | SI | Puntaje Excitación |
| Q22 | - |  |  | SI | Puntaje Lubricación |
| Q23 | - |  |  | SI | Puntaje Orgasmo |
| Q24 | - |  |  | SI | Puntaje Satisfacción |
| Q25 | - |  |  | SI | Puntaje Dolor |
| Q26 | - |  |  | SI | Puntaje Final |
| Q27 | - |  |  | SI | Dominio |
| Q28 | - |  |  | SI | Preguntas |
| Q29 | - |  |  | SI | Rango Puntaje |
| Q30 | - |  |  | SI | Factor |
| Q31 | - |  |  | SI | Mínimo |
| Q32 | - |  |  | SI | Máximo |
| Q33 | - |  |  | SI | Deseo |
| Q34 | - |  |  | SI | 1, 2 |
| Q35 | - |  |  | SI | 1 - 5 |
| Q36 | - |  |  | SI | 0.6 |
| Q37 | - |  |  | SI | 1.2 |
| Q38 | - |  |  | SI | 6.0 |
| Q39 | - |  |  | SI | Excitación |
| Q40 | - |  |  | SI | 3, 4, 5, 6 |
| Q41 | - |  |  | SI | 0 - 5 |
| Q42 | - |  |  | SI | 0.3 |
| Q43 | - |  |  | SI | 0 |
| Q44 | - |  |  | SI | 6.0 |
| Q45 | - |  |  | SI | Lubricación |
| Q46 | - |  |  | SI | 7, 8, 9, 10 |
| Q47 | - |  |  | SI | 0 - 5 |
| Q48 | - |  |  | SI | 0.3 |
| Q49 | - |  |  | SI | 0 |
| Q50 | - |  |  | SI | 6.0 |
| Q51 | - |  |  | SI | Orgasmo |
| Q52 | - |  |  | SI | 11, 12, 13 |
| Q53 | - |  |  | SI | 0 - 5 |
| Q54 | - |  |  | SI | 0.4 |
| Q55 | - |  |  | SI | 0 |
| Q56 | - |  |  | SI | 6.0 |
| Q57 | - |  |  | SI | Satisfacción |
| Q58 | - |  |  | SI | 14, 15, 16 |
| Q59 | - |  |  | SI | 0 (o 1) - 5 |
| Q60 | - |  |  | SI | 0.4 |
| Q61 | - |  |  | SI | 0.8 |
| Q62 | - |  |  | SI | 6.0 |
| Q63 | - |  |  | SI | Dolor |
| Q64 | - |  |  | SI | 17, 18, 19 |
| Q65 | - |  |  | SI | 0 - 5 |
| Q66 | - |  |  | SI | 0.4 |
| Q67 | - |  |  | SI | 0 |
| Q68 | - |  |  | SI | 6.0 |
| Q69 | - |  |  | SI | Rango Total Escala |
| Q70 | - |  |  | SI | 2.0 |
| Q71 | - |  |  | SI | 36.0 |
| Q72 | - |  |  | SI | Fecha |
| Q73 | - |  |  | SI | Las puntuaciones de cada dominio y la puntuación d... |
| Q74 | - |  |  | SI | que se indica en la tabla siguiente. Para las punt... |
| Q75 | - |  |  | SI | y multiplique la suma por el factor de dominio. Su... |
| Q76 | - |  |  | SI | Debe tenerse en cuenta que, dentro de los dominios... |
| Q77 | - |  |  | SI | actividad sexual durante el último mes. |
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