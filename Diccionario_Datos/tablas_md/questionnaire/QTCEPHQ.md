# questionnaire.QTCEPHQ

> Cuestionario PHQ-9 para Adultos

**Schema:** questionnaire
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cuestionario PHQ-9 para Adultos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | varchar |  |  | SI | 1. Tener poco interés o placer en hacer las cosas |
| Q03 | varchar |  |  | SI | 2. Sentirse desanimado/a, deprimido/a, o sin esper... |
| Q04 | varchar |  |  | SI | 3. Con problemas en dormirse o en mantenerse dormi... |
| Q05 | varchar |  |  | SI | 4. Sentirse cansado/a o tener poca energía |
| Q06 | varchar |  |  | SI | 5. Tener poco apetito o comer en exceso |
| Q07 | varchar |  |  | SI | 6. Sentir falta de amor propio - o que sea un frac... |
| Q08 | varchar |  |  | SI | 7. Tener dificultad para concentrarse en cosas tal... |
| Q09 | varchar |  |  | SI | 8. Se mueve o habla tan lentamente que otra gente ... |
| Q1 | varchar |  |  | SI | Resultado PHQ9 |
| Q10 | varchar |  |  | SI | 9. Se le han ocurrido pensamientos de que sería me... |
| Q11 | varchar |  |  | SI | Si usted se identificó con cualquier problema en e... |
| Q12 | varchar |  |  | SI | Resultado de Planificación |
| Q13 | varchar |  |  | SI | La puntuación indica que, probablemente, el pacien... |
| Q14 | varchar |  |  | SI | El médico debe utilizar su juicio clínico sobre el... |
| Q15 | varchar |  |  | SI | Se justifica el tratamiento de la depresión con an... |
| Q16 | varchar |  |  | SI | La pregunta 9 tiene un valor mayor a 0, independie... |
| Q17 | varchar |  |  | SI | Resultado |
| Q1ObsDR | varchar |  | FK | SI | Resultado PHQ9 DR |
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