# questionnaire.QTCEHMSURG8

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1DecOpModAt | varchar | PK |  | SI | 1.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q1DecOpModAtObs | varchar | PK |  | SI | 1.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q1FormIngServUrg | varchar | PK |  | SI | 1.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q1FormIngServUrgObs | varchar | PK |  | SI | 1.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q1FormSolTras | varchar | PK |  | SI | 1.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q1FormSolTrasObs | varchar | PK |  | SI | 1.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q2FormIngServUrg | varchar | PK |  | SI | 2.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q2FormIngServUrgObs | varchar | PK |  | SI | 2.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q2FormSolTras | varchar | PK |  | SI | 2.Llenar y faxear formulario SOLICITUD DE TRASLADO... |
| Q2FormSolTrasObs | varchar | PK |  | SI | 2.Llenar y faxear formulario SOLICITUD DE TRASLADO... |
| Q3DecOpModAt | varchar | PK |  | SI | 3.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q3DecOpModAtObs | varchar | PK |  | SI | 3.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q3FormIngServUrg | varchar | PK |  | SI | 3.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q3FormIngServUrgObs | varchar | PK |  | SI | 3.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q3FormSolTras | varchar | PK |  | SI | 3.Llenar y faxear formulario SOLICITUD DE TRASLADO... |
| Q3FormSolTrasObs | varchar | PK |  | SI | 3.Llenar y faxear formulario SOLICITUD DE TRASLADO... |
| Q4DecOpModAt | varchar | PK |  | SI | 4.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q4DecOpModAtObs | varchar | PK |  | SI | 4.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q4FaxCopDAU | varchar | PK |  | SI | 4.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q4FaxCopDAUObs | varchar | PK |  | SI | 4.Llenar DECLARACION DE OPCION POR MODALIDAD DE AT... |
| Q4FormIngServUrg | varchar | PK |  | SI | 4.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q4FormIngServUrgObs | varchar | PK |  | SI | 4.Llenar y faxear formulario INGRESO AL SERVICIO D... |
| Q4FormSolTras | varchar | PK |  | SI | 4.Llenar y faxear formulario SOLICITUD DE TRASLADO... |
| Q4FormSolTrasObs | varchar | PK |  | SI | 4.Llenar y faxear formulario SOLICITUD DE TRASLADO... |
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