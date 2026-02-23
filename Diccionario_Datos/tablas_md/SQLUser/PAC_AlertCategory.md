# SQLUser.PAC_AlertCategory

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALERTCAT_RowId | bigint | PK |  | NO | - |
| ALERTCAT_Code | varchar |  |  | NO | Code |
| ALERTCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALERTCAT_CreatedDate | date |  |  | SI | Created Date |
| ALERTCAT_CreatedTime | time |  |  | SI | Created Time |
| ALERTCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALERTCAT_DateFrom | date |  |  | SI | Date From |
| ALERTCAT_DateTo | date |  |  | SI | Date To |
| ALERTCAT_Desc | varchar |  |  | NO | Description |
| ALERTCAT_IconName | varchar |  |  | SI | IconName |
| ALERTCAT_IconPriority | varchar |  |  | SI | IconPriority |
| ALERTCAT_Owner | varchar |  |  | SI | Owner |
| ALERTCAT_UpdatedDate | date |  |  | SI | Updated Date |
| ALERTCAT_UpdatedTime | time |  |  | SI | Updated Time |
| ALERTCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | I |
| Q02 | - |  |  | SI | II |
| Q03 | - |  |  | SI | II A |
| Q04 | - |  |  | SI | III |
| Q05 | - |  |  | SI | III Vertex |
| Q06 | - |  |  | SI | III A |
| Q07 | - |  |  | SI | IV |
| Q08 | - |  |  | SI | V |
| Q09 | - |  |  | SI | IV A |
| Q10 | - |  |  | SI | VI |
| Q11 | - |  |  | SI | VII |
| Q12 | - |  |  | SI | V A |
| Q13 | - |  |  | SI | Grade |
| Q14 | - |  |  | SI | Date |
| Q15 | - |  |  | SI | Time |
| Q16 | - |  |  | SI | Hair |
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