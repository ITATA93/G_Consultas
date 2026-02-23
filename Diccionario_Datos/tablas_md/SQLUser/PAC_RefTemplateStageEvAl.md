# SQLUser.PAC_RefTemplateStageEvAl

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVAL_ParRef | bigint | PK |  | NO | PACRefStageTemplate Parent Reference |
| EVAL_Childsub | double |  |  | NO | Childsub |
| EVAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EVAL_CreatedDate | date |  |  | SI | Created Date |
| EVAL_CreatedTime | time |  |  | SI | Created Time |
| EVAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EVAL_RowId | varchar |  |  | NO | - |
| EVAL_StageStatus_DR | bigint |  | FK | SI | Des Ref StateStatus |
| EVAL_UpdatedDate | date |  |  | SI | Updated Date |
| EVAL_UpdatedTime | time |  |  | SI | Updated Time |
| EVAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Delivery location |
| Q04 | - |  |  | SI | Renal ready room location |
| Q05 | - |  |  | SI | Patient delivery address |
| Q06 | - |  |  | SI | Other location and delivery address |
| Q07 | - |  |  | SI | Requested delivery from |
| Q08 | - |  |  | SI | to |
| Q09 | - |  |  | SI | Requested delivery to |
| Q10 | - |  |  | SI | Delivery notes |
| Q11 | - |  |  | SI | Equipment requested |
| Q12 | - |  |  | SI | APD machine serial number |
| Q13 | - |  |  | SI | Modem serial number |
| Q14 | - |  |  | SI | Bag warmer serial number |
| Q15 | - |  |  | SI | Other equipment and serial number(s) |
| Q16 | - |  |  | SI | Equipment notes |
| Q17 | - |  |  | SI | Equipment received date |
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