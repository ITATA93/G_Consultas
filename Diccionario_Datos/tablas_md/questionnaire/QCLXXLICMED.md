# questionnaire.QCLXXLICMED

> Licencia Médica

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Licencia Médica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Origen de la Licencia |
| Q02 | date |  |  | SI | Fecha de Inicio del reposo |
| Q03 | numeric |  |  | SI | Número de días |
| Q04 | date |  |  | SI | Fecha de final del Reposo |
| Q05 | varchar |  |  | SI | Tipo de Reposo |
| Q06 | varchar |  |  | SI | Jornada |
| Q07 | varchar |  |  | SI | Lugar de Reposo |
| Q08 | varchar |  |  | SI | Comuna de Reposo |
| Q09 | varchar |  |  | SI | Dirección de Reposo |
| Q10 | varchar |  |  | SI | Teléfono |
| Q11 | varchar |  |  | SI | Justificación otro Domicilio |
| Q12 | varchar |  |  | SI | Lugar de Reposo Alternativo |
| Q13 | varchar |  |  | SI | Comuna de Reposo Alternativo |
| Q14 | varchar |  |  | SI | Dirección de Reposo Alternativo:  |
| Q15 | numeric |  |  | SI | Teléfono Alternativo |
| Q16 | varchar |  |  | SI | Otro Domicilio Alternativo |
| Q17 | varchar |  |  | SI | Tipo de Licencia |
| Q18 | varchar |  |  | SI | Datos del Hijo |
| Q19 | varchar |  |  | SI | RUN del Hijo |
| Q20 | varchar |  |  | SI | DV del Hijo |
| Q21 | varchar |  |  | SI | Nombre del Hijo |
| Q22 | varchar |  |  | SI | Apellido Paterno del Hijo |
| Q23 | varchar |  |  | SI | Apellido Materno del Hijo |
| Q24 | date |  |  | SI | Fecha de Nacimiento del Hijo |
| Q25 | date |  |  | SI | Fecha de Accidente |
| Q26 | time |  |  | SI | Hora de Accidente |
| Q27 | varchar |  |  | SI | Trayecto |
| Q28 | varchar |  |  | SI | Subtipo de Licencia |
| Q29 | date |  |  | SI | Fecha Concepción |
| Q30 | varchar |  |  | SI | Diagnostico principal  |
| Q31 | varchar |  |  | SI | Observaciones Diagnóstico |
| Q32 | varchar |  |  | SI | Otros Antecedentes médicos |
| Q33 | varchar |  |  | SI | Diagnóstico Secundario CIE-10 |
| Q34 | varchar |  |  | SI | Diagnostico Secundario |
| Q35 | varchar |  |  | SI | Otros Diagnósticos CIE-10 |
| Q36 | varchar |  |  | SI | Otros Diagnósticos |
| Q37 | varchar |  |  | SI | Antecedentes Clínicos |
| Q38 | varchar |  |  | SI | Exámenes de Apoyo |
| Q39 | varchar |  |  | SI | Código de Proceso  |
| Q40 | varchar |  |  | SI | UrlConexion |
| Q41 | varchar |  |  | SI | Número Licencia  |
| Q42 | varchar |  |  | SI | Estado Licencia |
| Q43 | varchar |  |  | SI | Motivo de Licencia |
| Q44 | varchar |  |  | SI | Inicio Trámite Invalidez |
| Q45 | varchar |  |  | SI | Correo Electrónico |
| Q46 | numeric |  |  | SI | Número de empleadores |
| Q47 | varchar |  |  | SI | Hijo Mortinato |
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