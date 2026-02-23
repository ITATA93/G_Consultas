# questionnaire.QTCABBEYPS

> Escala de Dolor Abbey

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Dolor Abbey

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Para medir el dolor en personas que no pueden verb... |
| Q02 | varchar |  |  | SI | Vocalización: lamentos, gruñidos, llanto |
| Q03 | varchar |  |  | SI | Expresión facial: expresión tensa, fruncida, lamen... |
| Q04 | varchar |  |  | SI | Cambios de lenguaje corporal: movimientos de nervi... |
| Q05 | varchar |  |  | SI | Cambios de comportamiento: aumento de confusión, r... |
| Q06 | varchar |  |  | SI | Cambios fisiológicos: temperatura, pulso o de&nbsp... |
| Q07 | varchar |  |  | SI | Cambios físicos: cortes en la piel, áreas de presi... |
| Q08 | varchar |  |  | SI | Marque la opción que corresponda al tipo de dolor |
| Q09 | varchar |  |  | SI | 0-2 Sin Dolor |
| Q10 | varchar |  |  | SI | 3-7 Leve |
| Q11 | varchar |  |  | SI | 8-13 Moderado |
| Q12 | varchar |  |  | SI | 14+ Severo |
| Q13 | varchar |  |  | SI | Puntaje |
| Q14 | varchar |  |  | SI | Clasificación |
| Q15 | varchar |  |  | SI | 0 - 2 |
| Q16 | varchar |  |  | SI | Sin Dolor |
| Q17 | varchar |  |  | SI | 3 - 7 |
| Q18 | varchar |  |  | SI | Leve |
| Q19 | varchar |  |  | SI | 8 - 13 |
| Q20 | varchar |  |  | SI | Moderado |
| Q21 | varchar |  |  | SI | ≥ 14 |
| Q22 | varchar |  |  | SI | Severo |
| Q23 | varchar |  |  | SI | 0 - 2: Sin Dolor |
| Q24 | varchar |  |  | SI | 3 - 7: Leve |
| Q25 | varchar |  |  | SI | 8 - 13: Moderado |
| Q26 | varchar |  |  | SI | ≥ 14: Severo |
| Q27 | date |  |  | SI | Fecha |
| Q28 | time |  |  | SI | Hora |
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