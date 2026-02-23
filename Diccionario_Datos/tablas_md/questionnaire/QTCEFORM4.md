# questionnaire.QTCEFORM4

> Control Oxigenoterapia ambulatoria paciente EPOC

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Control Oxigenoterapia ambulatoria paciente EPOC

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QAtencionCons | varchar |  |  | SI | Atención en Consultorio |
| QBDD | varchar |  |  | SI | Budesonida (dosis) |
| QComuna | varchar |  |  | SI | Comuna |
| QConsultorio | varchar |  |  | SI | Consultorio |
| QDomic | varchar |  |  | SI | Domicilio |
| QEvalOxig | varchar |  |  | SI | 6. Evaluación de Oxigenoterapia |
| QExistenciaAct | varchar |  |  | SI | 5. Existencia Actual de |
| QFactores | varchar |  |  | SI | 1. Factores ambientales de Riesgo actuales |
| QFechaReg | date |  |  | SI | Fecha Registro |
| QFuente | varchar |  |  | SI | Fuente del Suministro O2 |
| QHoraReg | time |  |  | SI | Hora Registro |
| QIPD | varchar |  |  | SI | Ipatropio (dosis) |
| QMantFlujo | numeric |  |  | SI | Mantener Flujo O2  |
| QNombre | varchar |  |  | SI | Nombre |
| QNombreInf | varchar |  |  | SI | Nombre del Informantr |
| QNumVisita | numeric |  |  | SI | 3. Número de Visitas a consultorio en últimos 3 me... |
| QNumVisitaUrg | numeric |  |  | SI | 4. Número Visitas a Urgencia en últimos 3 meses |
| QNumeroReg | varchar |  |  | SI | N° Registro O2 |
| QOTD | varchar |  |  | SI | Otro (dosis) |
| QPrev | varchar |  |  | SI | Previsión |
| QPuntajeCuest | numeric |  |  | SI | 10. Puntaje Cuestionario de calida de Vida (CRQ) |
| QPuntajeEs | numeric |  |  | SI | 9. Puntaje Escala de Disnea |
| QRegion | varchar |  |  | SI | Región |
| QRut | varchar |  |  | SI | Rut |
| QSTD | varchar |  |  | SI | Salbutamol (dosis) |
| QSalaEra | varchar |  |  | SI | Sala ERA Consultorio |
| QServicio | varchar |  |  | SI | Servicio de Salud |
| QTelef | varchar |  |  | SI | Teléfono |
| QTiempo | time |  |  | SI | Tiempo Diario de uso |
| QTutorRes | varchar |  |  | SI | 7. Tutor Responsable y Capacitado |
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
| QUsoBron | varchar |  |  | SI | 2. Uso Broncodilatadores (Dosis) |
| QVisitaDom | varchar |  |  | SI | Visita Domiciliaria |
| Qservoxig | varchar |  |  | SI | 8. Servicio de oxigenoterapia continuo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*