# questionnaire.QCLXXDGPCM

> Registro Procedimiento Endoscópico

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Procedimiento Endoscópico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedimiento Endoscópico |
| Q02 | varchar |  |  | SI | Detalles Procedimiento / Cirugía Menor a Realizar |
| Q03 | varchar |  |  | SI | Especialidad |
| Q04 | time |  |  | SI | Hora Inicio Programada |
| Q05 | time |  |  | SI | Hora Inicio Real |
| Q06 | time |  |  | SI | Hora Término |
| Q07 | varchar |  |  | SI | Paciente Acompañado |
| Q08 | varchar |  |  | SI | Nº Frascos |
| Q09 | varchar |  |  | SI | Test de Ureasa |
| Q10 | varchar |  |  | SI | Test de Lactasa |
| Q11 | varchar |  |  | SI | Comentarios |
| Q12 | varchar |  |  | SI | Comentarios |
| Q13 | varchar |  |  | SI | Otros Exámenes |
| Q14 | varchar |  |  | SI | Comentarios |
| Q15 | varchar |  |  | SI | Observaciones / Comentarios |
| Q16 | varchar |  |  | SI | Especialidad Cirugía / Procedimento |
| Q17 | varchar |  |  | SI | Biopsia |
| Q18 | varchar |  |  | SI | N° de Serie Equipo |
| Q19 | varchar |  |  | SI | Test de Fuga |
| Q20 | varchar |  |  | SI | Comentarios |
| Q22 | varchar |  |  | SI | Consulte la vista completa del Registro Procedimie... |
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