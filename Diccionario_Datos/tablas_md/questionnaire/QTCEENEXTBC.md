# questionnaire.QTCEENEXTBC

> Encuesta Pacientes Extranjeros en Tratamiento de Tuberculosis

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta Pacientes Extranjeros en Tratamiento de Tuberculosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nacionalidad |
| Q02 | varchar |  |  | SI | Pasaporte |
| Q02a | varchar |  |  | SI | VIH |
| Q02aObsDR | varchar |  | FK | SI | VIH DR |
| Q03 | varchar |  |  | SI | Ocupación |
| Q03a | varchar |  |  | SI | Otra Ocupación |
| Q04 | varchar |  |  | SI | Domicilio Particular en Chile |
| Q05 | varchar |  |  | SI | Comuna Chile |
| Q07 | numeric |  |  | SI | Fono |
| Q08 | varchar |  |  | SI | Domicilio Laboral en Chile |
| Q09 | varchar |  |  | SI | Comuna de Trabajo |
| Q10 | numeric |  |  | SI | Fono Trabajo |
| Q11 | varchar |  |  | SI | Domicilio en país de origen:  Detalle |
| Q12 | varchar |  |  | SI | Diagnóstico de TBC (Órgano) |
| Q13 | varchar |  |  | SI | Confirmación |
| Q14 | varchar |  |  | SI | Caso Nuevo |
| Q15 | varchar |  |  | SI | AT por recaída |
| Q16 | varchar |  |  | SI | AT por Abandono |
| Q17 | varchar |  |  | SI | Esquema de Tratamiento |
| Q18 | date |  |  | SI | Fecha inicio de tratamiento |
| Q19 | varchar |  |  | SI | Lugar de Notificación |
| Q20 | date |  |  | SI | Fecha de Notificación |
| Q21 | varchar |  |  | SI | Servicio de Salud Residencia |
| Q23 | numeric |  |  | SI | Total Contactos Laborales |
| Q24 | numeric |  |  | SI | Niños |
| Q25 | numeric |  |  | SI | Adulto |
| Q26 | numeric |  |  | SI | Total Contactos Personales |
| Q27 | numeric |  |  | SI | Niños |
| Q28 | numeric |  |  | SI | Adultos |
| Q29 | numeric |  |  | SI | Total contactos con quimioprofilaxis |
| Q30 | numeric |  |  | SI | Total casos secundarios (Enfermos) |
| Q31 | varchar |  |  | SI | Traslado a (otro País) |
| Q32 | date |  |  | SI | Fecha Traslado  |
| Q33 | varchar |  |  | SI | Condición de Egreso |
| Q34 | date |  |  | SI | Fecha  Condición de egreso |
| Q35 | varchar |  |  | SI | Observaciones |
| Q37 | varchar |  |  | SI | Nombre |
| Q38 | varchar |  |  | SI | Apellido Paterno |
| Q39 | varchar |  |  | SI | Apellido Materno |
| Q40 | varchar |  |  | SI | Edad |
| Q41 | varchar |  |  | SI | Sexo |
| Q42 | varchar |  |  | SI | RUT |
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