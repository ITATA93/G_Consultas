# SQLUser.LBC_ProtocolProcedure

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPTP_ParRef | bigint | PK |  | NO | Parent Protocol |
| LBCPTP_Autocomplete | varchar |  |  | SI | Autocomplete
Indicates that this procedure is aut... |
| LBCPTP_CreatedDate | date |  |  | SI | Created Date |
| LBCPTP_CreatedTime | time |  |  | SI | Created Time |
| LBCPTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPTP_Notes | longvarchar |  |  | SI | Notes
HTMLRichText |
| LBCPTP_Procedure_DR | bigint |  | FK | SI | Lab Procedure  |
| LBCPTP_RowID | varchar |  |  | NO | - |
| LBCPTP_Source_DR | varchar |  | FK | SI | Source Material  |
| LBCPTP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPTP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | AMBULANCIA TOTAL |
| Q02 | - |  |  | SI | MARÍTIMO TOTAL |
| Q03 | - |  |  | SI | AÉREO TOTAL |
| Q04 | - |  |  | SI | AMBULANCIA A BENEFICIARIOS |
| Q05 | - |  |  | SI | MARITIMO A BENEFICIARIOS |
| Q06 | - |  |  | SI | AEREO A BENEFICIARIOS |
| Q07 | - |  |  | SI | AMBULANCIA POR COMPRA DE SERVICIO |
| Q08 | - |  |  | SI | MARITIMO POR COMPRA DE SERVICIO |
| Q09 | - |  |  | SI | AEREO POR COMPRA DE SERVICIO |
| Q10 | - |  |  | SI | Fecha de Registro Desde |
| Q11 | - |  |  | SI | Fecha de Registro Hasta |
| Q13 | - |  |  | SI | MES |
| Q14 | - |  |  | SI | AÑO |
| QHR | - |  |  | SI | ESTABLECIMIENTO |
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