# SQLUser.LBC_AntibioticClass

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCANTC_RowID | bigint | PK |  | NO | - |
| LBCANTC_Code | varchar |  |  | SI | Code |
| LBCANTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCANTC_CreatedDate | date |  |  | SI | Created Date |
| LBCANTC_CreatedTime | time |  |  | SI | Created Time |
| LBCANTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCANTC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCANTC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCANTC_Desc | varchar |  |  | SI | Description |
| LBCANTC_Owner | varchar |  |  | SI | Owner |
| LBCANTC_Sequence | double |  |  | SI | Display Sequence |
| LBCANTC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCANTC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCANTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Don (ña) |
| Q02 | - |  |  | SI | Procedimientos Diagnósticos |
| Q03 | - |  |  | SI | Procedimientos Terapéuticos |
| Q04 | - |  |  | SI | Procedimientos Quirúrgicos |
| Q05 | - |  |  | SI | Paciente |
| Q06 | - |  |  | SI | RUT |
| Q07 | - |  |  | SI | Nombre |
| Q08 | - |  |  | SI | RUT |
| Q09 | - |  |  | SI | Representante del Paciente |
| Q10 | - |  |  | SI | RUT |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*