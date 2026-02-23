# SQLUser.AR_HICClaimStatus

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CS_ParRef | bigint | PK |  | NO | - |
| CS_AssociateName | varchar |  |  | SI | Name of the associated fund |
| CS_LodgementDateTime | varchar |  |  | SI | Date and time of lodgement in medicare's format DD... |
| CS_ProcessStatusCode | varchar |  |  | SI | Code to indicate the processing status of the clai... |
| CS_ReferenceId | varchar |  |  | SI | Claim ID |
| CS_ReportStatusCode | varchar |  |  | SI | Code to indicate the report status
PROCESSING 
I... |
| CS_RequestContentType | varchar |  |  | SI | Request type of the claim |
| CS_RowID | varchar |  |  | NO | - |
| CS_StatusRequestDate | date |  |  | SI | Date of the status request |
| CS_StatusRequestTime | time |  |  | SI | Time of the status request |
| CS_StatusRequestTransactionID | varchar |  |  | SI | Transaction ID of the status request |
| CS_StatusRequestUser_DR | bigint |  | FK | SI | Status request user |
| CS_TransactionId | varchar |  |  | SI | Transaction ID
Already resolved to a claim transa... |
| Q01 | - |  |  | SI | Nivel Instrucción |
| Q01a | - |  |  | SI | Motivo de Consulta |
| Q02 | - |  |  | SI | Fecha de Ingreso UHD |
| Q03 | - |  |  | SI | Hora Ingreso UHD |
| Q04 | - |  |  | SI | Anamnesis |
| Q05 | - |  |  | SI | Examen Psicológico |
| Q06 | - |  |  | SI | Hipótesis Diagnostica |
| Q07 | - |  |  | SI | Plan de Tratamiento |
| Q08 | - |  |  | SI | Fecha de Evaluación |
| Q09 | - |  |  | SI | Nobre del Usuario |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*