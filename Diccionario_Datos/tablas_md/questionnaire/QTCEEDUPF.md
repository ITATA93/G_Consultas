# questionnaire.QTCEEDUPF

> Educación al Paciente y su Familia

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Educación al Paciente y su Familia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Evaluación de Necesidades Educativas |
| Q02 | varchar |  |  | SI | Otro (Evaluación) |
| Q03 | varchar |  |  | SI | Barreras de Aprendizaje |
| Q04 | varchar |  |  | SI | Otro (Barreras) |
| Q05 | varchar |  |  | SI | Recibe Educación  |
| Q06 | varchar |  |  | SI | Razón para No Educar |
| Q07 | varchar |  |  | SI | Otro (Razón) |
| Q08 | varchar |  |  | SI | 1.- Patología(s) Presente(s) |
| Q09 | varchar |  |  | SI | Contenidos |
| Q10 | varchar |  |  | SI | Actividad Educativa |
| Q11 | varchar |  |  | SI | Especificaciones Entregadas |
| Q12 | varchar |  |  | SI | 2.- Seguridad Medicación |
| Q13 | varchar |  |  | SI | Contenidos |
| Q14 | varchar |  |  | SI | Actividad Educativa |
| Q15 | varchar |  |  | SI | Especificaciones Entregadas |
| Q16 | varchar |  |  | SI | 3.- Uso de Equipos Biomédicos |
| Q17 | varchar |  |  | SI | Contenidos |
| Q18 | varchar |  |  | SI | Actividad Educativa |
| Q19 | varchar |  |  | SI | Especificaciones Entregadas |
| Q20 | varchar |  |  | SI | 4.- Condiciones Clínicas |
| Q21 | varchar |  |  | SI | Contenidos |
| Q22 | varchar |  |  | SI | Actividad Educativa |
| Q23 | varchar |  |  | SI | Especificaciones Entregadas |
| Q24 | varchar |  |  | SI | Receptor de Educación |
| Q25 | varchar |  |  | SI | Comprensión de la Educación |
| Q26 | varchar |  |  | SI | Demostración Correcta |
| Q27 | varchar |  |  | SI | Comentarios |
| Q28 | varchar |  |  | SI | Contenidos Entregados |
| Q29 | varchar |  |  | SI | Otro (Receptor) |
| Q30 | varchar |  |  | SI | Profesional Responsable |
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