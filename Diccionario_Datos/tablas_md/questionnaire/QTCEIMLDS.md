# questionnaire.QTCEIMLDS

> Informe Medico Legal Delitos Sexuales

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe Medico Legal Delitos Sexuales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | No Informe |
| Q02 | varchar |  |  | SI | Denuncia Presentada En |
| Q03 | varchar |  |  | SI | Juzgado |
| Q04 | varchar |  |  | SI | Ciudad |
| Q05 | numeric |  |  | SI | ROL |
| Q06 | varchar |  |  | SI | Denuncia |
| Q07 | varchar |  |  | SI | Violacion |
| Q08 | varchar |  |  | SI | Abuso Sexual |
| Q09 | varchar |  |  | SI | Outros |
| Q10 | varchar |  |  | SI | Nombres |
| Q11 | varchar |  |  | SI | Apellido Materno |
| Q12 | varchar |  |  | SI | Apellido Paterno |
| Q13 | varchar |  |  | SI | Sexo |
| Q14 | varchar |  |  | SI | Edad (Años) |
| Q15 | varchar |  |  | SI | Edad (Meses) |
| Q16 | varchar |  |  | SI | Cedula de Identidad |
| Q17 | varchar |  |  | SI | Estado Civil |
| Q18 | varchar |  |  | SI | Nivel Educacional |
| Q19 | varchar |  |  | SI | Actvidad Laboral |
| Q20 | varchar |  |  | SI | Domicilio |
| Q21 | date |  |  | SI | Fecha Del Examen |
| Q22 | time |  |  | SI | Hora Del Examen |
| Q23 | date |  |  | SI | Fecha Despacho Informe ao Tribunal |
| Q24 | varchar |  |  | SI | Describir Brevemente la Agresión |
| Q25 | date |  |  | SI | Fecha del Delito |
| Q26 | time |  |  | SI | Hora del Delito |
| Q27 | varchar |  |  | SI | Dia Ocurrenia del Delito |
| Q28 | varchar |  |  | SI | El Autor de La Agresion Fue |
| Q29 | varchar |  |  | SI | Día de Ocurrencia del Delito |
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