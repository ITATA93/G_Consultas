# questionnaire.QCLXXVAPTGA

> Valoración de Amnesia Post Traumática Galveston (GOAT)

**Schema:** questionnaire
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Valoración de Amnesia Post Traumática Galveston (GOAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha del Traumatismo Craneoencefálico |
| Q02 | varchar |  |  | SI | 1. ¿Cuál es su nombre? |
| Q03 | varchar |  |  | SI | ¿Cuándo nació? |
| Q04 | varchar |  |  | SI | ¿Dónde vive? |
| Q05 | varchar |  |  | SI | 2. ¿Dónde se encuentra usted ahora? Ciudad |
| Q06 | varchar |  |  | SI | Hospital |
| Q07 | varchar |  |  | SI | 3. ¿En qué fecha ingresó en este hospital? |
| Q08 | varchar |  |  | SI | ¿Cómo llego hasta aquí? |
| Q09 | varchar |  |  | SI | 4. ¿Qué es lo primero que recuerda después del acc... |
| Q10 | varchar |  |  | SI | ¿Puede describir con detalle lo primero que recuer... |
| Q11 | varchar |  |  | SI | 5. ¿Qué es lo primero que recuerda antes del accid... |
| Q12 | varchar |  |  | SI | ¿Puede describir con detalle lo primero que recuer... |
| Q13 | varchar |  |  | SI | 6. ¿Puede decirme la hora? |
| Q14 | varchar |  |  | SI | 7. ¿En qué día de la semana estamos? |
| Q15 | varchar |  |  | SI | 8. ¿En qué día del mes estamos? |
| Q16 | varchar |  |  | SI | 9. ¿En qué mes estamos? |
| Q17 | varchar |  |  | SI | 10. ¿En qué año estamos? |
| Q18 | varchar |  |  | SI | Puntuación total |
| Q19 | varchar |  |  | SI | Resultado |
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