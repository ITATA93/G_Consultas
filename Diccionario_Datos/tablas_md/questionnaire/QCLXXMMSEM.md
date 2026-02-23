# questionnaire.QCLXXMMSEM

> MMSE MODIFICADO

**Schema:** questionnaire
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* MMSE MODIFICADO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Que día de la semana es hoy |
| Q02 | varchar |  |  | SI | Ahora me gustaría hacerle una preguntas para ver c... |
| Q03 | varchar |  |  | SI | 2. Cual es la fecha de hoy |
| Q04 | varchar |  |  | SI | Respuesta 1 |
| Q05 | varchar |  |  | SI | respuesta 2 |
| Q06 | varchar |  |  | SI | 3. En qué mes estamos |
| Q07 | varchar |  |  | SI | 4. En qué estación del año estamos  |
| Q08 | varchar |  |  | SI | respuesta 3 |
| Q09 | varchar |  |  | SI | respuesta 4 |
| Q10 | varchar |  |  | SI | 5. En qué año estamos  |
| Q11 | varchar |  |  | SI | respuesta 5 |
| Q12 | varchar |  |  | SI | 6. Qué dirección es esta (calle, número) |
| Q13 | varchar |  |  | SI | respuesta 6 |
| Q14 | varchar |  |  | SI | 7. En qué país estamos |
| Q15 | varchar |  |  | SI | respuesta 7 |
| Q16 | varchar |  |  | SI | 8. En qué ciudad estamos |
| Q17 | varchar |  |  | SI | respuesta 8 |
| Q18 | varchar |  |  | SI | 9. Cuáles son las dos calles principales cerca de ... |
| Q19 | varchar |  |  | SI | respuesta 9 |
| Q20 | varchar |  |  | SI | 10. En qué piso estamos |
| Q21 | varchar |  |  | SI | 11. Árbol |
| Q22 | varchar |  |  | SI | respuesta 11 |
| Q23 | varchar |  |  | SI | 12. Mesa |
| Q24 | varchar |  |  | SI | respuesta 12 |
| Q25 | varchar |  |  | SI | 13. Avión |
| Q26 | varchar |  |  | SI | respuesta 13 |
| Q27 | numeric |  |  | SI | NÚMERO DE RESPUESTAS CORRECTAS |
| Q28 | numeric |  |  | SI | NÚMERO DE REPETICIONES |
| Q29 | varchar |  |  | SI | 14.a 93 |
| Q30 | varchar |  |  | SI | respuesta 14 |
| Q31 | varchar |  |  | SI | 15.a 86 |
| Q32 | varchar |  |  | SI | respuesta 15 |
| Q33 | varchar |  |  | SI | 16.a 79 |
| Q34 | varchar |  |  | SI | respuesta 16 |
| Q35 | varchar |  |  | SI | 17.a 72 |
| Q36 | varchar |  |  | SI | respuesta 17 |
| Q37 | varchar |  |  | SI | 18.a 65 |
| Q38 | varchar |  |  | SI | respuesta 18 |
| Q39 | varchar |  |  | SI | 14.b 9 |
| Q40 | varchar |  |  | SI | respuesta 14 b |
| Q41 | varchar |  |  | SI | 15.b 7 |
| Q42 | varchar |  |  | SI | respuesta 15 b |
| Q43 | varchar |  |  | SI | 16.b 5 |
| Q44 | varchar |  |  | SI | respuesta 16 b |
| Q45 | varchar |  |  | SI | 17.b 3 |
| Q46 | varchar |  |  | SI | respuesta 17 b  |
| Q47 | varchar |  |  | SI | 18.b 1 |
| Q48 | varchar |  |  | SI | respuesta 18 b  |
| Q49 | varchar |  |  | SI | 19. Árbol |
| Q50 | varchar |  |  | SI | respuesta 19 |
| Q51 | varchar |  |  | SI | 20. Mesa |
| Q52 | varchar |  |  | SI | respuesta 20 |
| Q53 | varchar |  |  | SI | 21. Avión |
| Q54 | varchar |  |  | SI | respuesta 21 |
| Q55 | varchar |  |  | SI | 22. ¿Qué es esto? |
| Q56 | varchar |  |  | SI | respuesta 22 |
| Q57 | varchar |  |  | SI | 23. ¿Cómo se llama esto? |
| Q58 | varchar |  |  | SI | respuesta 23 |
| Q59 | varchar |  |  | SI | 24. |
| Q60 | varchar |  |  | SI | respuesta 24  |
| Q61 | varchar |  |  | SI | 25.a |
| Q62 | varchar |  |  | SI | respuesta 25a |
| Q63 | varchar |  |  | SI | 25.b |
| Q64 | varchar |  |  | SI | respuesta 25b |
| Q65 | varchar |  |  | SI | 26 |
| Q66 | varchar |  |  | SI | respuesta 26 |
| Q67 | varchar |  |  | SI | 27 |
| Q68 | varchar |  |  | SI | respuesta 27 |
| Q69 | varchar |  |  | SI | 28.a Pentágonos (incorrecto:0 ; correcto: 1) |
| Q70 | varchar |  |  | SI | respuesta 28a |
| Q71 | varchar |  |  | SI | 29.b Círculos  (incorrecto:0 ; correcto: 1) |
| Q72 | varchar |  |  | SI | respuest 28 b |
| Q73 | varchar |  |  | SI | respuesta 10  |
| Q74 | varchar |  |  | SI | Resultado: |
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