# questionnaire.QTCDHI

> Test de Discapacidad Vestibular (DHI)

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de Discapacidad Vestibular (DHI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Se le pide al paciente que responda cada pregunta ... |
| Q04 | varchar |  |  | SI | Las preguntas están diseñadas para incorporar impa... |
| Q05 | varchar |  |  | SI | FI1. ¿Cúando usted mira hacia arriba se siente más... |
| Q06 | varchar |  |  | SI | E2. ¿Debido a su problema o, mareo ¿se siente como... |
| Q07 | varchar |  |  | SI | F3. ¿Debido a su mareo o problema ¿evita hacer via... |
| Q08 | varchar |  |  | SI | FI4. Cuando camina por los pasillos de un supermer... |
| Q09 | varchar |  |  | SI | F5. ¿A causa de su problema, o del mareo le cuesta... |
| Q10 | varchar |  |  | SI | F6. ¿Debido a su problema o el mareo, trata de par... |
| Q11 | varchar |  |  | SI | F7. ¿A causa de su problema o mareo le cuesta leer... |
| Q12 | varchar |  |  | SI | FI8. ¿Al tener que realizar actividades más exigen... |
| Q13 | varchar |  |  | SI | E9. ¿Debido a su problema o por el mareo tiene mie... |
| Q14 | varchar |  |  | SI | E10. ¿A causa de su problema o mareo se siente inc... |
| Q15 | varchar |  |  | SI | FI11. ¿Al hacer movimientos rápidos de su cabeza n... |
| Q16 | varchar |  |  | SI | F12. ¿Debido a su problema o mareo evita las altur... |
| Q17 | varchar |  |  | SI | FI13. ¿Al darse vuelta en la cama siente que aumen... |
| Q18 | varchar |  |  | SI | F14. ¿Debido a su problema o mareo le cuesta hacer... |
| Q19 | varchar |  |  | SI | E15. ¿Debido a su problema o mareo se avergüenza a... |
| Q20 | varchar |  |  | SI | F16. ¿A consecuencias de su problema o mareo le cu... |
| Q21 | varchar |  |  | SI | FI17. ¿Al bajar de la vereda a la calle o calzada ... |
| Q22 | varchar |  |  | SI | E18. ¿Debido a su problema o mareo le cuesta conce... |
| Q23 | varchar |  |  | SI | F19. ¿Debido a su problema o mareo le cuesta camin... |
| Q24 | varchar |  |  | SI | E20. ¿A consecuencias de su problema o mareo tiene... |
| Q25 | varchar |  |  | SI | E21. ¿Debido a su problema o mareo se siente incap... |
| Q26 | varchar |  |  | SI | E22. ¿A consecuencias de su problema o mareo ha te... |
| Q27 | varchar |  |  | SI | E23. ¿Debido a su problema o mareo se encuentra qu... |
| Q28 | varchar |  |  | SI | F24. ¿El problema que usted tiene o el mareo que s... |
| Q29 | varchar |  |  | SI | FI25. ¿Al agacharse o inclinarse hacia delante com... |
| Q30 | varchar |  |  | SI | Comentarios |
| Q31 | varchar |  |  | SI | Total Puntaje Funcional (F) |
| Q32 | varchar |  |  | SI | /36 |
| Q33 | varchar |  |  | SI | Total Puntaje Emocional (E) |
| Q34 | varchar |  |  | SI | /36 |
| Q35 | varchar |  |  | SI | Total Puntaje Fisico (FI) |
| Q36 | varchar |  |  | SI | /28 |
| Q37 | varchar |  |  | SI | Total |
| Q38 | varchar |  |  | SI | /100 |
| Q39 | varchar |  |  | SI | Cuanto mayor sea la puntuación, mayor será la disc... |
| Q40 | varchar |  |  | SI | Total |
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