# SQLUser.MR_ObservationsAudit

**Schema:** SQLUser
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Observaciones**. Datos de observación clínica. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VAL_ParRef | varchar | PK |  | NO | MR_Observations Parent Reference |
| Q01 | - |  |  | SI | Receive clinical handover from Anaesthetist / Medi... |
| Q02 | - |  |  | SI | Assess patient with full clinical history and exam... |
| Q03 | - |  |  | SI | Review operative record and post operative plan |
| Q04 | - |  |  | SI | Review Anaesthetic record |
| Q05 | - |  |  | SI | Review any clinical information from medical recor... |
| Q06 | - |  |  | SI | Review and document pre-op medications |
| Q07 | - |  |  | SI | Order immediate post- op investigations as require... |
| Q08 | - |  |  | SI | Order any delayed doctors investigations including... |
| Q09 | - |  |  | SI | Chart  all ICU interventions including IV fluids a... |
| Q10 | - |  |  | SI | Chart medical admission including the definitive p... |
| Q11 | - |  |  | SI | Communicate the detailed post-op operative plan wi... |
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
| VAL_Childsub | double |  |  | NO | Childsub |
| VAL_Date | date |  |  | SI | Date |
| VAL_RowId | varchar |  |  | NO | - |
| VAL_Time | time |  |  | SI | Time |
| VAL_User_DR | bigint |  | FK | SI | Des Ref User |
| VAL_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*