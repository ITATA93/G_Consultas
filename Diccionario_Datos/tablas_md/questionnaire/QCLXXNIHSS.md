# questionnaire.QCLXXNIHSS

> Escala de Evaluación Neurológica en ACV Agudo - NIHSS

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Evaluación Neurológica en ACV Agudo - NIHSS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nivel de Conciencia |
| Q02 | varchar |  |  | SI | Preguntar mes y edad |
| Q03 | varchar |  |  | SI | Ordenes (Abrir y cerrar los ojos - Apretar y abrir... |
| Q04 | varchar |  |  | SI | Mirada horizontal |
| Q05 | varchar |  |  | SI | Campos visuales |
| Q06 | varchar |  |  | SI | Parálisis facial |
| Q07 | varchar |  |  | SI | Examen Motor (ESI - examinar por 10 segs.) |
| Q08 | varchar |  |  | SI | Examen Motor (ESD - examinar por 10 segs.)  |
| Q09 | varchar |  |  | SI | Examen Motor (EII - examinar por 5 segs.)  |
| Q10 | varchar |  |  | SI | Examen Motor (EID - examinar por 5 segs.)  |
| Q11 | varchar |  |  | SI | Ataxia de extremidades de un hemicuerpo (ES: Índic... |
| Q12 | varchar |  |  | SI | Sensibilidad al dolor |
| Q13 | varchar |  |  | SI | Lenguaje |
| Q14 | varchar |  |  | SI | Disartria |
| Q15 | varchar |  |  | SI | Extinción o inatención |
| Q16 | varchar |  |  | SI | Resultado |
| Q16ObsDR | varchar |  | FK | SI | Resultado DR |
| Q17 | varchar |  |  | SI | Recomendaciones 1 al 4 |
| Q18 | varchar |  |  | SI | Recomendaciones 5 a 14 |
| Q19 | varchar |  |  | SI | Recomendaciones 15 a 20 |
| Q20 | varchar |  |  | SI | Recomendaciones 21 a 42 |
| Q21 | varchar |  |  | SI | Recomendaciones 1 al 4 MEUI |
| Q22 | varchar |  |  | SI | Recomendaciones 5 a 14 MEUI |
| Q23 | varchar |  |  | SI | Recomendaciones 15 a 20 MEUI |
| Q24 | varchar |  |  | SI | Recomendaciones 21 a 42 MEUI |
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