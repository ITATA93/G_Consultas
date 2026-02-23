# questionnaire.QLEONEO

> Ficha Neonatal

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Neonatal

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Nombres del Recién Nacido (RN) |
| Q04 | varchar |  |  | SI | Apellido Paterno RN |
| Q05 | varchar |  |  | SI | Apellido Materno RN |
| Q06 | date |  |  | SI | Fecha de Nacimiento |
| Q07 | time |  |  | SI | Hora de Nacimiento |
| Q08 | varchar |  |  | SI | RUT |
| Q09 | varchar |  |  | SI | Dirección |
| Q10 | varchar |  |  | SI | Comuna |
| Q11 | varchar |  |  | SI | Teléfono |
| Q12 | varchar |  |  | SI | Consultorio |
| Q13 | varchar |  |  | SI | Previsión |
| Q14 | varchar |  |  | SI | Nombres de la Madre |
| Q15 | varchar |  |  | SI | Apellido Paterno de la Madre |
| Q16 | varchar |  |  | SI | Apellido Materno de la Madre |
| Q17 | numeric |  |  | SI | Edad de la Madre |
| Q18 | varchar |  |  | SI | RUT |
| Q19 | varchar |  |  | SI | Grupo Sanguíneo AB0 materno |
| Q20 | varchar |  |  | SI | Grupo Sanguíneo Rh Materno |
| Q21 | numeric |  |  | SI | Gestaciones |
| Q22 | numeric |  |  | SI | Partos |
| Q23 | numeric |  |  | SI | Abortos |
| Q24 | varchar |  |  | SI | VDRL |
| Q25 | varchar |  |  | SI | VIH |
| Q26 | varchar |  |  | SI | Antecedentes Mórbidos |
| Q27 | varchar |  |  | SI | Uso de Corticoides |
| Q28 | varchar |  |  | SI | Uso de Corticoides |
| Q29 | varchar |  |  | SI | Uso de Antibióticos |
| Q30 | varchar |  |  | SI | Uso de Antibióticos  |
| Q31 | varchar |  |  | SI | Uso de Otros Fármacos |
| Q32 | varchar |  |  | SI | Uso de Otros fármacos |
| Q33 | varchar |  |  | SI | Controles médicos de embarazo |
| Q34 | numeric |  |  | SI | Número de controles de embarazo realizados |
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