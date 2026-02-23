# SQLUser.ARC_OrdSetPrice

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRICE_ParRef | varchar | PK |  | NO | ARC_OrdSets Parent Reference |
| PRICE_AdjustmentOnly | varchar |  |  | SI | Adjustment Only |
| PRICE_Childsub | double |  |  | NO | Childsub |
| PRICE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRICE_CreatedDate | date |  |  | SI | Created Date |
| PRICE_CreatedTime | time |  |  | SI | Created Time |
| PRICE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRICE_Currency_DR | bigint |  | FK | SI | Des Ref Currency |
| PRICE_DateFrom | date |  |  | NO | PRICE_DateFrom |
| PRICE_DateTo | date |  |  | SI | Date To |
| PRICE_EpisodeType | varchar |  |  | SI | Episode Type |
| PRICE_HospitalDR | bigint |  | FK | SI | Hospital DR |
| PRICE_PayorShare | double |  |  | SI | Payor Share |
| PRICE_Price | double |  |  | SI | Price |
| PRICE_RowId | varchar |  |  | NO | - |
| PRICE_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| PRICE_UpdatedDate | date |  |  | SI | Updated Date |
| PRICE_UpdatedTime | time |  |  | SI | Updated Time |
| PRICE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Certifico que no he solicitado exámenes en esta at... |
| Q02 | - |  |  | SI | “Actualizar” para realizar la certificación” |
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