# questionnaire.QTCEVCC

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ017AI | varchar | PK |  | SI | - |
| CQ018AI | varchar | PK |  | SI | - |
| CQ023ASP | varchar | PK |  | SI | - |
| CQ024ASP | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q001 | varchar | PK |  | SI | TIPO DE VACUNA |
| Q002 | varchar | PK |  | SI | GRUPO DE EDAD |
| Q003 | varchar | PK |  | SI | FECHA DE ADMINISTRACIÓN |
| Q004 | varchar | PK |  | SI | SERIE |
| Q005 | varchar | PK |  | SI | LOCAL DE ADMINISTRACIÓN |
| Q006 | varchar | PK |  | SI | SITIO DE ADMINISTRACIÓN |
| Q007 | varchar | PK |  | SI | LATERALIDAD |
| Q008 | varchar | PK |  | SI | PROFESIONAL DE SALUD |
| Q009 | varchar | PK |  | SI | REACCION ADVERSA |
| Q010 | varchar | PK |  | SI | ANTI INFLUENZA |
| Q011 | varchar | PK |  | SI | ANTISARAMPIONOSA  |
| Q012AI | bit | PK |  | SI | Enfermo Crónico |
| Q013AI | bit | PK |  | SI | Embarazada |
| Q014AI | bit | PK |  | SI | Personal de Salud |
| Q015AI | date | PK |  | SI | Fecha de Administración |
| Q016AI | varchar | PK |  | SI | Serie |
| Q017AI | varchar | PK |  | SI | Lateralidad  |
| Q018AI | varchar | PK |  | SI | Sitio de Administración |
| Q019AI | varchar | PK |  | SI | Profesional de Salud |
| Q020AI | varchar | PK |  | SI | Reacción Adversa  |
| Q021ASP | date | PK |  | SI | Fecha de Administración |
| Q022ASP | varchar | PK |  | SI | Serie |
| Q023ASP | varchar | PK |  | SI | Sitio de Administración |
| Q024ASP | varchar | PK |  | SI | Lateralidad  |
| Q025ASP | varchar | PK |  | SI | Profesional de Salud |
| Q026ASP | varchar | PK |  | SI | Reacción Adversa  |
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