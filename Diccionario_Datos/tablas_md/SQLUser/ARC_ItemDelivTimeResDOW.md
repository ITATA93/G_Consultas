# SQLUser.ARC_ItemDelivTimeResDOW

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOW_ParRef | varchar | PK |  | NO | ARC_ItemDelivTimeRes Parent Reference |
| DOW_Childsub | double |  |  | NO | Childsub |
| DOW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOW_CreatedDate | date |  |  | SI | Created Date |
| DOW_CreatedTime | time |  |  | SI | Created Time |
| DOW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOW_DateFrom | date |  |  | SI | Date From |
| DOW_DateTo | date |  |  | SI | Date To |
| DOW_DayOfWeek_DR | double |  | FK | SI | Des Ref DayOfWeek |
| DOW_RowId | varchar |  |  | NO | - |
| DOW_UpdatedDate | date |  |  | SI | Updated Date |
| DOW_UpdatedTime | time |  |  | SI | Updated Time |
| DOW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age |
| Q04 | - |  |  | SI | Date of birth |
| Q05 | - |  |  | SI | Place |
| Q06 | - |  |  | SI | Year |
| Q07 | - |  |  | SI | The four-item Abbreviated Mental Test Score (AMT4)... |
| Q08 | - |  |  | SI | Swain DG, Nightingale PG. Evaluation of a shortene... |
| Q09 | - |  |  | SI | Hodkinson HM. Evaluation of a mental test score fo... |
| Q10 | - |  |  | SI | Blessed G, Tomlinson BE, Roth M. The association b... |
| Q11 | - |  |  | SI | The Abbreviated Mental Test 4 (AMT-4) is a brief i... |
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