# questionnaire.QTCEARC

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric | PK |  | SI | No Informe |
| Q02 | varchar | PK |  | SI | Denuncia Presentada En |
| Q03 | varchar | PK |  | SI | Juzgado |
| Q04 | varchar | PK |  | SI | Ciudad |
| Q05 | numeric | PK |  | SI | ROL |
| Q06 | varchar | PK |  | SI | Denuncia |
| Q07 | varchar | PK |  | SI | Violacion |
| Q08 | varchar | PK |  | SI | Abuso Sexual |
| Q09 | varchar | PK |  | SI | Outros |
| Q10 | varchar | PK |  | SI | Nombres |
| Q11 | varchar | PK |  | SI | Edad (Años) |
| Q12 | varchar | PK |  | SI | Edad (Meses) |
| Q13 | varchar | PK |  | SI | Sexo |
| Q14 | varchar | PK |  | SI | Domicilio |
| Q15 | varchar | PK |  | SI | Comuna |
| Q16 | date | PK |  | SI | Fecha Del Examen |
| Q17 | time | PK |  | SI | Hora Del Examen |
| Q18 | varchar | PK |  | SI | Nombre Del  Profesional Que Realiza El Examen |
| Q19 | varchar | PK |  | SI | Reconocimiento Realizado |
| Q20 | varchar | PK |  | SI | Solicitud De Examenes De Laboratorio, Pruebas Biol... |
| Q21 | varchar | PK |  | SI | Especificar |
| Q22 | varchar | PK |  | SI | Apellido Materno |
| Q23 | varchar | PK |  | SI | Apellido Paterno |
| Q24 | varchar | PK |  | SI | Cedula de Identidad |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*