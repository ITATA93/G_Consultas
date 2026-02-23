# questionnaire.QTCMCBS

> Escala de Comfort - B

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Comfort - B

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Paciente esta intubado (a) |
| Q02 | varchar |  |  | SI | Objetivo de la evaluación |
| Q03 | varchar |  |  | SI | Puntuación Objetiva |
| Q04 | varchar |  |  | SI | Alerta |
| Q05 | varchar |  |  | SI | Calma / Agitación |
| Q06 | varchar |  |  | SI | Respuesta respiratoria (solo en niños&nbsp;ventila... |
| Q07 | varchar |  |  | SI | Llanto (sólo en niños&nbsp;con ventilación no inva... |
| Q08 | varchar |  |  | SI | Movimiento fisico |
| Q09 | varchar |  |  | SI | Tono muscular |
| Q10 | varchar |  |  | SI | Tensión facial |
| Q11 | varchar |  |  | SI | La Escala COMFORT mide varios parámetros para dete... |
| Q12 | varchar |  |  | SI | 6 - 10  |
| Q13 | varchar |  |  | SI | 11 - 15  |
| Q14 | varchar |  |  | SI | 16 - 22  |
| Q15 | varchar |  |  | SI | 23 - 40  |
| Q16 | varchar |  |  | SI | Amarillo |
| Q17 | varchar |  |  | SI | Azul |
| Q18 | varchar |  |  | SI | Verde |
| Q19 | varchar |  |  | SI | Red |
| Q20 | varchar |  |  | SI | Puntaje |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | date |  |  | SI | Fecha |
| Q23 | time |  |  | SI | Hora |
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