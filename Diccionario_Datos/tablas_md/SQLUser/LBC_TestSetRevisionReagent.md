# SQLUser.LBC_TestSetRevisionReagent

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRRE_ParRef | bigint | PK |  | NO | - |
| LBCTSRRE_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCTSRRE_CreatedDate | date |  |  | SI | Created Date |
| LBCTSRRE_CreatedTime | time |  |  | SI | Created Time |
| LBCTSRRE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTSRRE_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRRE_DateTo | date |  |  | SI | Last day the record is active |
| LBCTSRRE_Mandatory | varchar |  |  | SI | Mandatory |
| LBCTSRRE_Reagent_DR | bigint |  | FK | NO | Reagent |
| LBCTSRRE_RowID | varchar |  |  | NO | - |
| LBCTSRRE_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTSRRE_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTSRRE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | MES |
| Q03 | - |  |  | SI | AÑO |
| Q04 | - |  |  | SI | TOTAL DE EGRESOS MENORES DE 15 AÑOS (en el periodo... |
| Q05 | - |  |  | SI | TOTAL DE EGRESOS MAYORES DE 15 AÑOS (en el periodo... |
| Q06 | - |  |  | SI | EGRESADOS CON INFORMACIÓN U ORIENTACIÓN A FAMILIAR... |
| Q07 | - |  |  | SI | EGRESADOS CON INFORMACIÓN U ORIENTACIÓN A FAMILIAR... |
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