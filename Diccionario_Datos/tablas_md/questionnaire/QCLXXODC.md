# questionnaire.QCLXXODC

> Orden de Cirugía

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Orden de Cirugía

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Atención |
| Q02 | time |  |  | SI | Hora Atención |
| Q05 | varchar |  |  | SI | Requiere Donante de Sangre |
| Q06 | varchar |  |  | SI | Prioridad |
| Q07 | varchar |  |  | SI | Convenio |
| Q08 | varchar |  |  | SI | Datos de Hospitalización |
| Q09 | varchar |  |  | SI | Tipo de Estadía |
| Q10 | varchar |  |  | SI | Centro |
| Q11 | varchar |  |  | SI | Fecha Estimada |
| Q12 | varchar |  |  | SI | Precauciones adicionales |
| Q13 | varchar |  |  | SI | Complejidad |
| Q14 | numeric |  |  | SI | UCI |
| Q15 | numeric |  |  | SI | Intermedio |
| Q16 | numeric |  |  | SI | Básica |
| Q17 | varchar |  |  | SI | Otros |
| Q18 | varchar |  |  | SI | Cirugía Robótica |
| Q19 | varchar |  |  | SI | Alergias |
| Q20 | varchar |  |  | SI | Proveedor |
| Q21 | varchar |  |  | SI | Implantes |
| Q22 | varchar |  |  | SI | Observaciones |
| Q23 | varchar |  |  | SI | Anestesia |
| Q24 | varchar |  |  | SI | Para el Paciente |
| Q25 | varchar |  |  | SI | Sobre Materiales Especiales - Rayos, etc. |
| Q26 | varchar |  |  | SI | Para Presupuestos |
| Q27 | varchar |  |  | SI | Profesional Clínico |
| Q28 | date |  |  | SI | Fecha Acordada |
| Q29 | date |  |  | SI | Fecha Desde |
| Q30 | date |  |  | SI | Fecha Hasta |
| Q31 | varchar |  |  | SI | Observacion General |
| Q32 | varchar |  |  | SI | Identificación del Paciente |
| Q33 | varchar |  |  | SI | Número |
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