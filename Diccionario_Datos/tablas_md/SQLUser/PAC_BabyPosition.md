# SQLUser.PAC_BabyPosition

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BABYPOS_RowId | bigint | PK |  | NO | - |
| BABYPOS_Code | varchar |  |  | NO | Code |
| BABYPOS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BABYPOS_CreatedDate | date |  |  | SI | Created Date |
| BABYPOS_CreatedTime | time |  |  | SI | Created Time |
| BABYPOS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BABYPOS_DateFrom | date |  |  | SI | Date From |
| BABYPOS_DateTo | date |  |  | SI | Date To |
| BABYPOS_Desc | varchar |  |  | NO | Description |
| BABYPOS_NationalCode | varchar |  |  | SI | National Code |
| BABYPOS_Owner | varchar |  |  | SI | Owner |
| BABYPOS_UpdatedDate | date |  |  | SI | Updated Date |
| BABYPOS_UpdatedTime | time |  |  | SI | Updated Time |
| BABYPOS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Receive clinical handover from Anaesthetist / Medi... |
| Q02 | - |  |  | SI | Assess patient with full clinical history and exam... |
| Q03 | - |  |  | SI | Review operative record and post operative plan |
| Q04 | - |  |  | SI | Review anaesthetic record |
| Q05 | - |  |  | SI | Review any clinical information from medical recor... |
| Q06 | - |  |  | SI | Review and document pre-op medications |
| Q07 | - |  |  | SI | Order immediate post- op investigations as require... |
| Q08 | - |  |  | SI | Order any delayed doctors investigations including... |
| Q09 | - |  |  | SI | Chart  all ICU interventions including IV fluids a... |
| Q10 | - |  |  | SI | Chart medical admission including the definitive p... |
| Q11 | - |  |  | SI | Communicate the detailed post-op operative plan wi... |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
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