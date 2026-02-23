# questionnaire.QCLXXMCHATR

> M-CHAT- R/F

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* M-CHAT- R/F

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | Llenado por |
| Q04 | varchar |  |  | SI | 1. Si usted indica algo al otro lado de la pieza, ... |
| Q05 | varchar |  |  | SI | 1. Si usted indica algo al otro lado de la pieza, ... |
| Q06 | varchar |  |  | SI | 2. ¿Alguna vez se ha preguntado si su hijo/a es so... |
| Q07 | varchar |  |  | SI | 2. ¿Alguna vez se ha preguntado si su hijo/a es so... |
| Q08 | varchar |  |  | SI | 3. ¿Su hijo/a realiza juegos de fantasía o imagina... |
| Q09 | varchar |  |  | SI | 3. ¿Su hijo/a realiza juegos de fantasía o imagina... |
| Q10 | varchar |  |  | SI | 4. ¿A su hijo/a le gusta subirse a cesas? (Por eje... |
| Q11 | varchar |  |  | SI | 4. ¿A su hijo/a le gusta subirse a cesas? (Profesi... |
| Q12 | varchar |  |  | SI | 5. ¿Su hijo/a hace movimientos raros con sus dedos... |
| Q13 | varchar |  |  | SI | 5. ¿Su hijo/a hace movimientos raros con sus dedos... |
| Q14 | varchar |  |  | SI | 6. ¿Su hijo/a indica o apunta con e dedo cuando qu... |
| Q15 | varchar |  |  | SI | 6. ¿Su hijo/a indica o apunta con e dedo cuando qu... |
| Q16 | varchar |  |  | SI | 7. ¿Su hijo/a señala con un dedo cuando quiere mos... |
| Q17 | varchar |  |  | SI | 7. ¿Su hijo/a señala con un dedo cuando quiere mos... |
| Q18 | varchar |  |  | SI | 8. ¿Su hijo/a muestra interés en otros niños? (Por... |
| Q19 | varchar |  |  | SI | 8. ¿Su hijo/a muestra interés en otros niños? (Pro... |
| Q20 | varchar |  |  | SI | 9. ¿Su hijo/a le muestra cosas acercándoselas o se... |
| Q21 | varchar |  |  | SI | 9. ¿Su hijo/a le muestra cosas acercándoselas o se... |
| Q22 | varchar |  |  | SI | 10.¿Su hijo/a responde cuando usted lo llama por s... |
| Q23 | varchar |  |  | SI | 10.¿Su hijo/a responde cuando usted lo llama por s... |
| Q24 | varchar |  |  | SI | 11.¿Cuándo usted le sonríe a su hijo./a, él/ella t... |
| Q25 | varchar |  |  | SI | 11.¿Cuándo usted le sonríe a su hijo./a, él/ella t... |
| Q26 | varchar |  |  | SI | 12.¿Le molestan a su hijo/a los ruidos comunes? (P... |
| Q27 | varchar |  |  | SI | 12.¿Le molestan a su hijo/a los ruidos comunes?&nb... |
| Q28 | varchar |  |  | SI | 13.¿Su hijo/a camina solo? |
| Q29 | varchar |  |  | SI | 13.¿Su hijo/a camina solo? (Profesional) |
| Q30 | varchar |  |  | SI | 14.¿Su hijo/a lo mira a los ojos cuando usted le h... |
| Q31 | varchar |  |  | SI | 14.¿Su hijo/a lo mira a los ojos cuando usted le h... |
| Q32 | varchar |  |  | SI | 15.¿Su hijo/a imita sus movimientos? (Por ejemplo:... |
| Q33 | varchar |  |  | SI | 15.¿Su hijo/a imita sus movimientos? (Profesional) |
| Q34 | varchar |  |  | SI | 16. Si usted se da vuelta a ver algo, ¿su hijo/a t... |
| Q35 | varchar |  |  | SI | 16 Si usted se da vuelta a ver algo, ¿su hijo/a tr... |
| Q36 | varchar |  |  | SI | 17.¿Su hijo/a intenta que usted le mire o le prest... |
| Q37 | varchar |  |  | SI | 17.¿Su hijo/a intenta que usted le mire o le prest... |
| Q38 | varchar |  |  | SI | 18. ¿Su hijo/a le entiende cuando usted le pide qu... |
| Q39 | varchar |  |  | SI | 18. ¿Su hijo/a le entiende cuando usted le pide qu... |
| Q40 | varchar |  |  | SI | 19. Si ocurre algo que llame la atención de su hij... |
| Q41 | varchar |  |  | SI | 19. Si ocurre algo que llame la atención de su hij... |
| Q42 | varchar |  |  | SI | 20. ¿Le gustan a su hijo/a los juegos con movimien... |
| Q43 | varchar |  |  | SI | 20. ¿Le gustan a su hijo/a los juegos con movimien... |
| Q44 | numeric |  |  | SI | Total M-CHAT (Profesional) |
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