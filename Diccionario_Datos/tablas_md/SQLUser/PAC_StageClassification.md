# SQLUser.PAC_StageClassification

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STCL_RowId | bigint | PK |  | NO | - |
| ChildQ16DR | - |  |  | SI | Child Reference: Treatment history |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Detail of issue (in patient's / carer's own words) |
| Q04 | - |  |  | SI | Occurrence |
| Q05 | - |  |  | SI | How would you describe the onset? |
| Q06 | - |  |  | SI | Is it changing over time? |
| Q07 | - |  |  | SI | Associated symptoms |
| Q08 | - |  |  | SI | Other symptoms |
| Q09 | - |  |  | SI | Does this condition impact aspects of your life? i... |
| Q10 | - |  |  | SI | Impact details |
| Q11 | - |  |  | SI | Any concerns in the following areas? |
| Q12 | - |  |  | SI | Details of concern(s) |
| Q13 | - |  |  | SI | Recent travel |
| Q14 | - |  |  | SI | Travel details |
| Q15 | - |  |  | SI | Additional case history notes |
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
| STCL_Code | varchar |  |  | NO | Code |
| STCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STCL_CreatedDate | date |  |  | SI | Created Date |
| STCL_CreatedTime | time |  |  | SI | Created Time |
| STCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STCL_Desc | varchar |  |  | NO | Description |
| STCL_Owner | varchar |  |  | SI | Owner |
| STCL_UpdatedDate | date |  |  | SI | Updated Date |
| STCL_UpdatedTime | time |  |  | SI | Updated Time |
| STCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*