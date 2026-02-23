# questionnaire.QCLXXEMULTP

> Evaluación Multiprofesional

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Multiprofesional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora de Evaluación |
| Q03 | varchar |  |  | SI | Fisiatra que deriva |
| Q04 | varchar |  |  | SI | Impresión General |
| Q05 | varchar |  |  | SI | Habilidades Motoras |
| Q06 | varchar |  |  | SI | Actividades de la vida diaria |
| Q07 | varchar |  |  | SI | Cognición, Comunicación y Lenguaje |
| Q08 | varchar |  |  | SI | Área Servicio Social |
| Q09 | varchar |  |  | SI | Área Psicología |
| Q10 | varchar |  |  | SI | Enfermería |
| Q11 | varchar |  |  | SI | Dental |
| Q12 | varchar |  |  | SI | Ayuda Técnica |
| Q13 | varchar |  |  | SI | Situación Educativa |
| Q14 | varchar |  |  | SI | ¿Cuáles son los problemas principales que le dific... |
| Q15 | varchar |  |  | SI | Recibe o ha recibido rehabilitación en otro centro |
| Q16 | varchar |  |  | SI | Modalidad de Atención Sugerida |
| Q17 | varchar |  |  | SI | Objetivos Funcionales |
| Q18 | varchar |  |  | SI | Indicaciones |
| Q19 | varchar |  |  | SI | Registros Médicos |
| Q20 | date |  |  | SI | Citaciones Especialista |
| Q21 | date |  |  | SI | Citación Médico |
| Q22 | varchar |  |  | SI | Comentarios Citación |
| Q23 | varchar |  |  | SI | Diagnóstico |
| Q24 | varchar |  |  | SI | I Datos Personales |
| Q25 | varchar |  |  | SI | II Evaluación Integral |
| Q26 | varchar |  |  | SI | III Asistencia Profesionales Firmada |
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