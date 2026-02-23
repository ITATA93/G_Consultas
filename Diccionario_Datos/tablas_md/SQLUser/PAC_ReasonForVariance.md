# SQLUser.PAC_ReasonForVariance

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFV_RowId | bigint | PK |  | NO | - |
| ChildQ01DR | - |  |  | SI | Child Reference: Patient Behaviour Observational C... |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Specialled |
| Q05 | - |  |  | SI | Specialled commenced |
| Q06 | - |  |  | SI | Specialled commenced time |
| Q07 | - |  |  | SI | Specialled ceased |
| Q08 | - |  |  | SI | Specialled ceased time |
| Q13 | - |  |  | SI | To be used in addition to documenting observations... |
| Q14 | - |  |  | SI | Please fill in at end of every nursing shift, or h... |
| Q15 | - |  |  | SI | • Document time of behaviour's if present. |
| Q16 | - |  |  | SI | • Provide brief description of behaviour's on char... |
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
| RFV_Code | varchar |  |  | NO | Code |
| RFV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFV_CreatedDate | date |  |  | SI | Created Date |
| RFV_CreatedTime | time |  |  | SI | Created Time |
| RFV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFV_DateFrom | date |  |  | SI | Date From |
| RFV_DateTo | date |  |  | SI | Date To |
| RFV_Default | varchar |  |  | SI | Default |
| RFV_Desc | varchar |  |  | NO | Description |
| RFV_Owner | varchar |  |  | SI | Owner |
| RFV_UpdatedDate | date |  |  | SI | Updated Date |
| RFV_UpdatedTime | time |  |  | SI | Updated Time |
| RFV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*