# questionnaire.QTCEINGENPA

> Instrucciones Generales al Paciente y Familia

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Instrucciones Generales al Paciente y Familia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre de la Enfermera/Matrona |
| Q02 | varchar |  |  | SI | Manejo de la Cama |
| Q03 | varchar |  |  | SI | Localización del Baño |
| Q04 | varchar |  |  | SI | Horarios de  Comidas |
| Q05 | varchar |  |  | SI | Horario de Visitas |
| Q06 | varchar |  |  | SI | Nombre de quién recibe la Información |
| Q07 | varchar |  |  | SI | Comentario Nombre de la Enfermera/Matrona |
| Q08 | varchar |  |  | SI | Comentario Manejo de la Cama |
| Q09 | varchar |  |  | SI | Comentario Localización del Baño |
| Q10 | varchar |  |  | SI | Comentario Horarios de Comidas |
| Q11 | varchar |  |  | SI | Comentario Horario de Visitas |
| Q12 | varchar |  |  | SI | Uso del Timbre de llamado |
| Q13 | varchar |  |  | SI | Comentarios Uso del Timbre de Llmado |
| Q14 | varchar |  |  | SI | Sistemas de Monitorización y Equipos |
| Q15 | varchar |  |  | SI | Comentario Sistemas de Monitorización y Equipos |
| Q16 | varchar |  |  | SI | Profesional de Salud |
| Q17 | varchar |  |  | SI | Rutina del Servicio |
| Q18 | varchar |  |  | SI | Comentario Rutina del Servicio |
| Q19 | varchar |  |  | SI | Normas de Ingreso |
| Q20 | varchar |  |  | SI | Lactancia |
| Q21 | varchar |  |  | SI | Comentario Lactancia |
| Q22 | varchar |  |  | SI | Comentario Normas de Ingreso |
| Q23 | varchar |  |  | SI | Extracción de Leche |
| Q24 | varchar |  |  | SI | Comentario Extracción de Leche |
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