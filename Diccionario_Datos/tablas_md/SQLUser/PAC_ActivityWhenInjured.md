# SQLUser.PAC_ActivityWhenInjured

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACTINJ_RowId | bigint | PK |  | NO | - |
| ACTINJ_Code | varchar |  |  | NO | Code |
| ACTINJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACTINJ_CreatedDate | date |  |  | SI | Created Date |
| ACTINJ_CreatedTime | time |  |  | SI | Created Time |
| ACTINJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACTINJ_DateFrom | date |  |  | SI | Date From |
| ACTINJ_DateTo | date |  |  | SI | Date To |
| ACTINJ_Desc | varchar |  |  | NO | Description |
| ACTINJ_Owner | varchar |  |  | SI | Owner |
| ACTINJ_UpdatedDate | date |  |  | SI | Updated Date |
| ACTINJ_UpdatedTime | time |  |  | SI | Updated Time |
| ACTINJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ17DR | - |  |  | SI | Child Reference: Gastric tube assessments |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pre-procedure checklist |
| Q04 | - |  |  | SI | Pre-procedure notes |
| Q05 | - |  |  | SI | Insertion date |
| Q06 | - |  |  | SI | Insertion time |
| Q07 | - |  |  | SI | Insertion reason |
| Q08 | - |  |  | SI | Other insertion reason |
| Q09 | - |  |  | SI | Insertion route |
| Q10 | - |  |  | SI | Tube type |
| Q11 | - |  |  | SI | Other gastric tube type |
| Q12 | - |  |  | SI | Tube size (french) |
| Q13 | - |  |  | SI | Length of tube from nostril / teeth / gums (cm) |
| Q14 | - |  |  | SI | Position checked by |
| Q15 | - |  |  | SI | Inserted by |
| Q16 | - |  |  | SI | Due date for tube change |
| Q18 | - |  |  | SI | Removal date |
| Q19 | - |  |  | SI | Removal time |
| Q20 | - |  |  | SI | Removal reason |
| Q21 | - |  |  | SI | Other removal reason |
| Q22 | - |  |  | SI | Removal notes |
| Q23 | - |  |  | SI | Removed by |
| Q24 | - |  |  | SI | Complications |
| Q25 | - |  |  | SI | Other complications |
| Q26 | - |  |  | SI | Complication notes |
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