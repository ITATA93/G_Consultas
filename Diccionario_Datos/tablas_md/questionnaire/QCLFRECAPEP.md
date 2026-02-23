# questionnaire.QCLFRECAPEP

> Formulario Registro Entrega de Condones en Actividades de Prevención Entre Pares

**Schema:** questionnaire
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario Registro Entrega de Condones en Actividades de Prevención Entre Pares

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Actividades Masivas: 1 condón por persona |
| Q02 | varchar |  |  | SI | Nombre Institución Responsable Actividad |
| Q03 | varchar |  |  | SI | Nombre Persona Realiza Reporte |
| Q04 | date |  |  | SI | Período Comprende Reporte |
| Q05 | date |  |  | SI | Período Comprende Reporte |
| Q06 | varchar |  |  | SI | Distribución |
| Q07 | varchar |  |  | SI | Nombre Actividad |
| Q08 | varchar |  |  | SI | Nombre Actividad |
| Q09 | varchar |  |  | SI | Nombre Actividad |
| Q10 | date |  |  | SI | Fecha |
| Q11 | date |  |  | SI | Fecha |
| Q12 | date |  |  | SI | Fecha |
| Q13 | numeric |  |  | SI | N° Personas Alcanzadas |
| Q14 | numeric |  |  | SI | N° Personas Alcanzadas |
| Q15 | numeric |  |  | SI | N° Personas Alcanzadas |
| Q16 | varchar |  |  | SI | Sexo y Rango Etareo |
| Q17 | varchar |  |  | SI | 15 - 19 |
| Q18 | numeric |  |  | SI | H |
| Q19 | numeric |  |  | SI | H |
| Q20 | numeric |  |  | SI | H |
| Q21 | numeric |  |  | SI | H |
| Q22 | numeric |  |  | SI | M |
| Q23 | numeric |  |  | SI | M |
| Q24 | numeric |  |  | SI | M |
| Q25 | numeric |  |  | SI | M |
| Q26 | numeric |  |  | SI | Trans |
| Q27 | numeric |  |  | SI | Trans |
| Q28 | numeric |  |  | SI | Trans |
| Q29 | numeric |  |  | SI | Trans |
| Q30 | varchar |  |  | SI | 20 - 24 |
| Q31 | numeric |  |  | SI | H |
| Q32 | numeric |  |  | SI | H |
| Q33 | numeric |  |  | SI | H |
| Q34 | numeric |  |  | SI | H |
| Q35 | numeric |  |  | SI | M |
| Q36 | numeric |  |  | SI | M |
| Q37 | numeric |  |  | SI | M |
| Q38 | numeric |  |  | SI | M |
| Q39 | numeric |  |  | SI | Trans |
| Q40 | numeric |  |  | SI | Trans |
| Q41 | numeric |  |  | SI | Trans |
| Q42 | numeric |  |  | SI | Trans |
| Q43 | varchar |  |  | SI | 25 - 29 |
| Q44 | numeric |  |  | SI | H |
| Q45 | numeric |  |  | SI | H |
| Q46 | numeric |  |  | SI | H |
| Q47 | numeric |  |  | SI | H |
| Q48 | numeric |  |  | SI | M |
| Q49 | numeric |  |  | SI | M |
| Q50 | numeric |  |  | SI | M |
| Q51 | numeric |  |  | SI | M |
| Q52 | numeric |  |  | SI | Trans |
| Q53 | numeric |  |  | SI | Trans |
| Q54 | numeric |  |  | SI | Trans |
| Q55 | numeric |  |  | SI | Trans |
| Q56 | varchar |  |  | SI | 30 y Más |
| Q57 | numeric |  |  | SI | H |
| Q58 | numeric |  |  | SI | H |
| Q59 | numeric |  |  | SI | H |
| Q60 | numeric |  |  | SI | H |
| Q61 | numeric |  |  | SI | M |
| Q62 | numeric |  |  | SI | M |
| Q63 | numeric |  |  | SI | M |
| Q64 | numeric |  |  | SI | M |
| Q65 | numeric |  |  | SI | Trans |
| Q66 | numeric |  |  | SI | Trans |
| Q67 | numeric |  |  | SI | Trans |
| Q68 | numeric |  |  | SI | Trans |
| Q69 | numeric |  |  | SI | Total Cantidad de Condones Entregados |
| Q70 | numeric |  |  | SI | Total Cantidad de Condones Entregados |
| Q71 | numeric |  |  | SI | Total Cantidad de Condones Entregados |
| Q72 | numeric |  |  | SI | Total Cantidad de Condones Entregados |
| Q73 | numeric |  |  | SI | Total Lubricantes |
| Q74 | numeric |  |  | SI | Total Lubricantes |
| Q75 | numeric |  |  | SI | Total Lubricantes |
| Q76 | numeric |  |  | SI | Total Lubricantes |
| Q77 | varchar |  |  | SI | Observaciones |
| Q78 | numeric |  |  | SI | N° Personas Alcanzadas |
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