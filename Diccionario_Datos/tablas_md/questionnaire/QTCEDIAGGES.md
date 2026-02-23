# questionnaire.QTCEDIAGGES

> Diagnóstico GES

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Diagnóstico GES

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QDiagProblem | bit |  |  | SI | MRDiagnos with PAProblem |
| QFechaConf | date |  |  | SI | Fecha de Confirmación |
| QFechaConfImp | date |  |  | SI | Fecha Confirmación Impresión IPD |
| QFechaDes | date |  |  | SI | Fecha Descarte |
| QFechaDesImp | date |  |  | SI | Fecha Descarte Impresión |
| QFechaNot | date |  |  | SI | Fecha Notificación |
| QFechaNotImp | date |  |  | SI | Fecha Notificación Impresión |
| QHoraConf | time |  |  | SI | Hora de Confirmación |
| QHoraConfImp | time |  |  | SI | Hora Confirmación Impresión IPD |
| QHoraDes | time |  |  | SI | Hora Descarte |
| QHoraDesImp | time |  |  | SI | Hora Desacarte Impresión |
| QHoraNot | time |  |  | SI | Hora Notificación |
| QHoraNotImp | time |  |  | SI | Hora Notificación Impresión |
| QMRDIAGNOS | varchar |  |  | SI | MRDiagnos  |
| QPACREFTEMPLATE | varchar |  |  | SI | Problema de Salud  |
| QPAPROBLEM | varchar |  |  | SI | PAProblem |
| QPAWAITINGLIST | varchar |  |  | SI | PAWaitingList |
| QRBOperatingRoom | varchar |  |  | SI | Operating Room |
| QTeleconsulta | bit |  |  | SI | Teleconsulta |
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
| QUserConf | varchar |  |  | SI | Usuario Confirmación |
| QUserDes | varchar |  |  | SI | Usuario de Descarte |
| QUserImpConf | varchar |  |  | SI | Usuario Imprime la Confirmación |
| QUserImpDes | varchar |  |  | SI | Usuario Imprime el Descarte |
| QUserImpNot | varchar |  |  | SI | Usuario Imprime la Notificación |
| QUserNot | varchar |  |  | SI | Código Usuario Notificación  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*