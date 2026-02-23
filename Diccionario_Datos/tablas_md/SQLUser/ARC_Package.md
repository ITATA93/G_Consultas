# SQLUser.ARC_Package

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACK_RowId | bigint | PK |  | NO | - |
| PACK_Code | varchar |  |  | NO | Code |
| PACK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACK_Comment | varchar |  |  | SI | Comments |
| PACK_CreatedDate | date |  |  | SI | Created Date |
| PACK_CreatedTime | time |  |  | SI | Created Time |
| PACK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACK_DateFrom | date |  |  | SI | Date From |
| PACK_DateTo | date |  |  | SI | Date To |
| PACK_Desc | varchar |  |  | NO | Description |
| PACK_ExternalCode | varchar |  |  | SI | External Code |
| PACK_FixedPrice | double |  |  | SI | FixedPrice |
| PACK_FreeText | varchar |  |  | SI | Free Text |
| PACK_MainOrderTariffPrice | varchar |  |  | SI | Main Order Tariff Price |
| PACK_Method | varchar |  |  | SI | Package Method |
| PACK_MultipleEpisode | varchar |  |  | SI | MultipleEpisode |
| PACK_NumberOfDays | double |  |  | SI | NumberOfDays |
| PACK_NumberOfVisits | double |  |  | SI | NumberOfVisits |
| PACK_Owner | varchar |  |  | SI | Owner |
| PACK_PrefMethPayment_DR | bigint |  | FK | SI | PrefMethPayment  |
| PACK_Reason_DR | bigint |  | FK | SI | Package Reason  |
| PACK_Repeat | varchar |  |  | SI | Repeat |
| PACK_SelectionMethod | varchar |  |  | SI | Selection Method |
| PACK_UpdatedDate | date |  |  | SI | Updated Date |
| PACK_UpdatedTime | time |  |  | SI | Updated Time |
| PACK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Motivo de Egreso Cuidados Paliativos Universal |
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