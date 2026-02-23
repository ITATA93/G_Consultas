# questionnaire.QREMA19AB4

> Talleres Grupales Según Temática y Número de Participantes en Programa Espacios Amigables

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Talleres Grupales Según Temática y Número de Participantes en Programa Espacios Amigables

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | ESPACIOS COMUNITARIOS |
| Q02 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 1 |
| Q03 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 2 |
| Q04 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 3 |
| Q05 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 4  |
| Q06 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 5 |
| Q07 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 6 |
| Q08 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 7 |
| Q09 | numeric |  |  | SI | ESPACIOS COMUNITARIOS 8 |
| Q10 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES |
| Q11 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 1 |
| Q12 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 2 |
| Q13 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 3 |
| Q14 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 4 |
| Q15 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 5 |
| Q16 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 6 |
| Q17 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 7 |
| Q18 | numeric |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 8 |
| Q19 | numeric |  |  | SI | CENTROS DE SALUD |
| Q20 | numeric |  |  | SI | CENTROS DE SALUD 1 |
| Q21 | numeric |  |  | SI | CENTROS DE SALUD 2 |
| Q22 | numeric |  |  | SI | CENTROS DE SALUD 3 |
| Q23 | numeric |  |  | SI | CENTROS DE SALUD 4 |
| Q24 | numeric |  |  | SI | CENTROS DE SALUD 5 |
| Q25 | numeric |  |  | SI | CENTROS DE SALUD 6 |
| Q26 | numeric |  |  | SI | CENTROS DE SALUD 7 |
| Q27 | numeric |  |  | SI | CENTROS DE SALUD 8 |
| Q29 | varchar |  |  | SI | Mes |
| Q30 | numeric |  |  | SI | Año |
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