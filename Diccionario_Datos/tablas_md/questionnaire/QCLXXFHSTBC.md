# questionnaire.QCLXXFHSTBC

> Solicitud Investigación Bacteriológica de Tuberculosis

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud Investigación Bacteriológica de Tuberculosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01a | varchar |  |  | SI | Nombre |
| Q01b | varchar |  |  | SI | Apellido Paterno |
| Q01c | varchar |  |  | SI | Apellido Materno |
| Q02 | varchar |  |  | SI | RUN |
| Q03 | varchar |  |  | SI | Domicilio |
| Q04 | varchar |  |  | SI | Teléfono |
| Q05 | varchar |  |  | SI | Procedencia |
| Q06 | varchar |  |  | SI | Edad |
| Q07 | varchar |  |  | SI | Muestra |
| Q08 | varchar |  |  | SI | 1a |
| Q09 | varchar |  |  | SI | 2a |
| Q10 | varchar |  |  | SI | Especificar |
| Q11 | varchar |  |  | SI | Examen solicitado para |
| Q12 | varchar |  |  | SI | Mes |
| Q13 | varchar |  |  | SI | Identifique Grupos Vulnerables |
| Q14 | varchar |  |  | SI | Otro grupo (especificar) |
| Q15 | date |  |  | SI | Fecha de Solicitud |
| Q16 | varchar |  |  | SI | Identificación del Solicitante |
| Q19 | varchar |  |  | SI | Fecha de Nacimiento |
| Q20 | varchar |  |  | SI | Sexo |
| Q21 | varchar |  |  | SI | Establecimiento |
| Q22 | varchar |  |  | SI | Unidad |
| Q23 | varchar |  |  | SI | Local (ambulatorio) |
| Q24 | varchar |  |  | SI | Nacionalidad |
| Q25 | numeric |  |  | SI | N° Mes |
| Q26 | varchar |  |  | SI | Antecedentes de Tratamiento |
| Q27 | varchar |  |  | SI | Señale el Tipo de Muestra |
| Q28 | varchar |  |  | SI | Otros líquidos o tejidos (especificar): |
| Q29 | varchar |  |  | SI | Otras poblaciones cerradas (especificar): |
| Q30 | date |  |  | SI | Fecha de Toma de Muestra |
| Q31 | varchar |  |  | SI | Responsable de Toma de Muestra |
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