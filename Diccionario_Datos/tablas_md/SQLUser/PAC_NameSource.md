# SQLUser.PAC_NameSource

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NAMSRC_RowId | bigint | PK |  | NO | - |
| NAMSRC_Code | varchar |  |  | NO | Code |
| NAMSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NAMSRC_CreatedDate | date |  |  | SI | Created Date |
| NAMSRC_CreatedTime | time |  |  | SI | Created Time |
| NAMSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NAMSRC_DateFrom | date |  |  | SI | Date From |
| NAMSRC_DateTo | date |  |  | SI | Date To |
| NAMSRC_Desc | varchar |  |  | NO | Description |
| NAMSRC_Owner | varchar |  |  | SI | Owner |
| NAMSRC_UpdatedDate | date |  |  | SI | Updated Date |
| NAMSRC_UpdatedTime | time |  |  | SI | Updated Time |
| NAMSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Please select one of the following |
| Q02 | - |  |  | SI | Patients with MS who are fully ambulatory |
| Q03 | - |  |  | SI | Patients with MS who are imparied to ambulation |
| Q04 | - |  |  | SI | The Kurtzke Expanded Disability Status Scale (EDSS... |
| Q05 | - |  |  | SI | The EDSS scale ranges from 0 to 10 in 0.5 unit inc... |
| Q06 | - |  |  | SI | Score 1.0 - 4.5: refer to people with MS who are f... |
| Q07 | - |  |  | SI | Score 5.0 - 9.5: refer to people with MS impared t... |
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