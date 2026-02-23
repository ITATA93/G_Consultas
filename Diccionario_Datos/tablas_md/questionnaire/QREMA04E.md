# questionnaire.QREMA04E

> REM A04 E - Consultas de morbilidad solicitadas y rechazadas dentro de las 48 horas de solicitada la atención

**Schema:** questionnaire
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REM A04 E - Consultas de morbilidad solicitadas y rechazadas dentro de las 48 horas de solicitada la atención

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Horario Normal - Total Atención Solicitada - Menor... |
| Q02 | numeric |  |  | SI | Horario Normal - Rechazos - Menor 5 Años |
| Q03 | numeric |  |  | SI | Horario Normal - Total Atención Solicitada - 65 y ... |
| Q04 | numeric |  |  | SI | Horario Normal - Rechazos - 65 y más años |
| Q05 | numeric |  |  | SI | Horario Normal - Total Atención Solicitada - Embar... |
| Q06 | numeric |  |  | SI | Horario Normal - Rechazos - Embarazadas |
| Q07 | numeric |  |  | SI | Horario Continuado - Total Atención Utilizada - Me... |
| Q08 | numeric |  |  | SI | Horario Continuado - Rechazos - Menor 5 años |
| Q09 | numeric |  |  | SI | Horario Continuado - Total Atención Utilizada - 65... |
| Q10 | numeric |  |  | SI | Horario Continuado - Rechazo - 65 y Más Años |
| Q11 | numeric |  |  | SI | Horario Continuado - Total Atención Utilizada - Em... |
| Q12 | numeric |  |  | SI | Horario Continuado - Rechazo - Embarazadas |
| Q16 | varchar |  |  | SI | Mes |
| Q17 | numeric |  |  | SI | Año |
| QFF | date |  |  | SI | Fecha FIn |
| QFI | date |  |  | SI | Fecha Inicio |
| QHR | varchar |  |  | SI | Establecimiento |
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