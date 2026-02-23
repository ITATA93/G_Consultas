# questionnaire.QREMA23SM2

> Educación Grupal en sala (agendada y programada)

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Educación Grupal en sala (agendada y programada)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | varchar |  |  | SI | codigo establecimiento de salud |
| Q03 | date |  |  | SI | Fecha Ejecución |
| Q04 | time |  |  | SI | Hora Inicio |
| Q05 | time |  |  | SI | Hora Término |
| Q06 | varchar |  |  | SI | Ejecutada por |
| Q07 | numeric |  |  | SI | N° Sesiones Pacientes, Padre y/o Cuidadores (E) |
| Q08 | varchar |  |  | SI | Tema |
| Q09 | varchar |  |  | SI | Tipo de asistentes (02-Tema) |
| Q10 | varchar |  |  | SI | Tipo de Asistentes (01 y 03-Tema) |
| Q11 | varchar |  |  | SI | Observaciones de la atención grupal |
| Q13 | varchar |  |  | SI | Mes |
| Q14 | numeric |  |  | SI | Año |
| Q15 | numeric |  |  | SI | N° Participantes Pacientes, Padres y/o Cuidadores ... |
| Q16 | numeric |  |  | SI | Un Profesional (E) |
| Q17 | numeric |  |  | SI | N° Sesiones Salas Cunas y Jardines Infantiles (E) |
| Q18 | numeric |  |  | SI | N° Participantes Salas Cunas y Jardines Infantiles... |
| Q19 | numeric |  |  | SI | Un Profesional (E) |
| Q20 | numeric |  |  | SI | N° Sesiones Establecimientos Educacionales (E) |
| Q21 | numeric |  |  | SI | N° Participantes Establecimientos Educacionales (E... |
| Q22 | numeric |  |  | SI | N° Sesiones Intersector (E) |
| Q23 | numeric |  |  | SI | N° Participantes Intersector (E) |
| Q24 | numeric |  |  | SI | Un Profesional (E) |
| Q25 | numeric |  |  | SI | N° Sesiones Pacientes y/o Cuidadores (R) |
| Q26 | numeric |  |  | SI | N° Participantes Pacientes y/o Cuidadores (R) |
| Q27 | numeric |  |  | SI | Un Profesional (R) |
| Q28 | numeric |  |  | SI | N° Sesiones Pacientes, Padres y/o Cuidadores (A) |
| Q29 | numeric |  |  | SI | N° Participantes Pacientes, Pades y/o Cuidadores (... |
| Q30 | numeric |  |  | SI | Un Profesional (A) |
| Q31 | numeric |  |  | SI | N° Sesiones Salas Cunas y Jardines Infantiles (A) |
| Q32 | numeric |  |  | SI | N° Participantes Salas Cunas y Jardines Infantiles... |
| Q33 | numeric |  |  | SI | Un Profesional (A) |
| Q34 | numeric |  |  | SI | N° Sesiones Establecimientos Educacionales (A) |
| Q35 | numeric |  |  | SI | N° Participantes Establecimientos Educacionales (A... |
| Q36 | numeric |  |  | SI | Un Profesional (A) |
| Q37 | numeric |  |  | SI | N° Sesiones Intersector (A) |
| Q38 | numeric |  |  | SI | N° Participantes Intersector (A) |
| Q39 | numeric |  |  | SI | Un Profesional (A) |
| Q40 | numeric |  |  | SI | Un Profesional (E) |
| Q41 | numeric |  |  | SI | Dos o Más Profesionales (E) |
| Q42 | numeric |  |  | SI | Dos o Más Profesionales (E) |
| Q43 | numeric |  |  | SI | Dos o Más Profesionales (E) |
| Q44 | numeric |  |  | SI | Dos o Más Profesionales (R) |
| Q45 | numeric |  |  | SI | Dos o Más Profesionales (A) |
| Q46 | numeric |  |  | SI | Dos o Más Profesionales (A) |
| Q47 | numeric |  |  | SI | Dos o Más Profesionales (A) |
| Q48 | numeric |  |  | SI | Dos o Más Profesionales (A) |
| Q49 | numeric |  |  | SI | Dos o Más Profesionales (E) |
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