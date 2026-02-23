# questionnaire.QTCESAS

> Evaluación de Síntomas de Edmonton (ESAS)

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de Síntomas de Edmonton (ESAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Dolor  |
| Q02 | varchar |  |  | SI | Cansancio |
| Q03 | varchar |  |  | SI | Náuseas |
| Q04 | varchar |  |  | SI | Somnolencia |
| Q05 | varchar |  |  | SI | Depresión |
| Q06 | varchar |  |  | SI | Ansiedad |
| Q07 | varchar |  |  | SI | Apetito |
| Q08 | varchar |  |  | SI | Dificultad para respirar |
| Q09 | varchar |  |  | SI | Bienestar |
| Q10 | varchar |  |  | SI | Otro problema (por ejemplo, estreñimiento) |
| Q11 | varchar |  |  | SI | Descripción del problema |
| Q12 | varchar |  |  | SI | Gravedad del problema |
| Q13 | varchar |  |  | SI | Sin Dolor  |
| Q14 | varchar |  |  | SI | El peor dolor posible |
| Q15 | varchar |  |  | SI | Sin cansancio |
| Q16 | varchar |  |  | SI | El peor cansancio posible |
| Q17 | varchar |  |  | SI | Sin náuseas |
| Q18 | varchar |  |  | SI | Las peores náuseas posibles |
| Q19 | varchar |  |  | SI | Sin somnolencia |
| Q20 | varchar |  |  | SI | La peor somnolencia posible |
| Q21 | varchar |  |  | SI | Sin depresión |
| Q22 | varchar |  |  | SI | La peor depresión posible |
| Q23 | varchar |  |  | SI | Sin ansiedad |
| Q24 | varchar |  |  | SI | La peor ansiedad posible |
| Q25 | varchar |  |  | SI | Sin apetito |
| Q26 | varchar |  |  | SI | El peor apetito posible |
| Q27 | varchar |  |  | SI | Sin dificultad para respirar |
| Q28 | varchar |  |  | SI | La peor dificultad para respirar posible |
| Q29 | varchar |  |  | SI | Mejor bienestar |
| Q30 | varchar |  |  | SI | El peor bienestar posible |
| Q31 | varchar |  |  | SI | Ningún problema |
| Q32 | varchar |  |  | SI | Lo peor posible |
| Q33 | varchar |  |  | SI | Un número más alto se asocia con una mayor graveda... |
| Q34 | varchar |  |  | SI | Cada puntuación representa la gravedad del síntoma... |
| Q35 | varchar |  |  | SI | El Sistema de Evaluación de Síntomas de Edmonton (... |
| Q36 | varchar |  |  | SI | 0 - 100: un número más alto se asocia con una mayo... |
| Q37 | varchar |  |  | SI | Dolor |
| Q38 | varchar |  |  | SI | Cansancio |
| Q39 | varchar |  |  | SI | Náuseas |
| Q40 | varchar |  |  | SI | Somnolencia |
| Q41 | varchar |  |  | SI | Depresión |
| Q42 | varchar |  |  | SI | Ansiedad |
| Q43 | varchar |  |  | SI | Apetito |
| Q44 | varchar |  |  | SI | Dificultad para respirar |
| Q45 | varchar |  |  | SI | Bienestar |
| Q46 | varchar |  |  | SI | Puntaje |
| Q47 | varchar |  |  | SI | Clasificación |
| Q48 | varchar |  |  | SI | 0 - 100 |
| Q49 | varchar |  |  | SI | Gravedad del problema |
| Q50 | varchar |  |  | SI | Dolor |
| Q51 | varchar |  |  | SI | Cansancio |
| Q52 | varchar |  |  | SI | Náuseas |
| Q53 | varchar |  |  | SI | Somnolencia |
| Q54 | varchar |  |  | SI | Depresión |
| Q55 | varchar |  |  | SI | Ansiedad |
| Q56 | varchar |  |  | SI | Apetito |
| Q57 | varchar |  |  | SI | Dificultad para respirar |
| Q58 | varchar |  |  | SI | Bienestar |
| Q59 | date |  |  | SI | Fecha |
| Q60 | time |  |  | SI | Hora |
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