# SQLUser.PAC_EpisodeSubType

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBT_RowId | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: Multidrug resistant organism bund... |
| Q01 | - |  |  | SI | Month |
| Q02 | - |  |  | SI | Location |
| Q03 | - |  |  | SI | MDRO test result date |
| Q05 | - |  |  | SI | Observer |
| Q06 | - |  |  | SI | Date |
| Q07 | - |  |  | SI | Time |
| Q08 | - |  |  | SI | Organism name |
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
| SUBT_AdmType | varchar |  |  | NO | Admission Type |
| SUBT_Code | varchar |  |  | NO | Code |
| SUBT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUBT_CreatedDate | date |  |  | SI | Created Date |
| SUBT_CreatedTime | time |  |  | SI | Created Time |
| SUBT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBT_DateFrom | date |  |  | SI | Date From |
| SUBT_DateTo | date |  |  | SI | Date To |
| SUBT_DaySurgery | varchar |  |  | SI | Day Surgery |
| SUBT_Desc | varchar |  |  | NO | Description |
| SUBT_EpsSubtypeNumber | varchar |  |  | SI | Episode Subtype Number |
| SUBT_ExclFromFreqAttender | varchar |  |  | SI | Exclude From Frequent Attender |
| SUBT_FirstRegDayNight | varchar |  |  | SI | First Reg Day Night |
| SUBT_InpatientCount | varchar |  |  | SI | Inpatient Count |
| SUBT_NationCode | varchar |  |  | SI | National Code |
| SUBT_NoAppointmentRequired | varchar |  |  | SI | No Appointment required |
| SUBT_Owner | varchar |  |  | SI | Owner |
| SUBT_ReceivingLocHospital | varchar |  |  | SI | Receiving Location Hospital |
| SUBT_RefPathwayStageType_DR | bigint |  | FK | SI | Default Stage Type DR |
| SUBT_Subregion_DR | bigint |  | FK | SI | Subregion  |
| SUBT_UpdatedDate | date |  |  | SI | Updated Date |
| SUBT_UpdatedTime | time |  |  | SI | Updated Time |
| SUBT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SUBT_WaitTime | double |  |  | SI | Wait Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*