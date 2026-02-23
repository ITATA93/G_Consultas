# SQLUser.ARC_PayAgreemBedCharges

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BED_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| BED_Amt | double |  |  | SI | Amount |
| BED_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| BED_BillSub_DR | varchar |  | FK | SI | Des Ref Bill Sub |
| BED_Childsub | double |  |  | NO | Childsub |
| BED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BED_CreatedDate | date |  |  | SI | Created Date |
| BED_CreatedTime | time |  |  | SI | Created Time |
| BED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BED_DateFrom | date |  |  | SI | Date From |
| BED_DateTo | date |  |  | SI | Date To |
| BED_DaysFrom | double |  |  | SI | Days From |
| BED_DaysTo | double |  |  | SI | Days To |
| BED_Description | varchar |  |  | SI | Description  |
| BED_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref EpisodeSubType |
| BED_FixedPrice | double |  |  | SI | FixedPrice |
| BED_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| BED_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| BED_PatientShare | double |  |  | SI | Patient Share |
| BED_PayorCode | varchar |  |  | SI | PayorCode |
| BED_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| BED_RowId | varchar |  |  | NO | - |
| BED_TimeFrom | varchar |  |  | SI | TimeFrom |
| BED_TimeTo | varchar |  |  | SI | TimeTo |
| BED_UpdatedDate | date |  |  | SI | Updated Date |
| BED_UpdatedTime | time |  |  | SI | Updated Time |
| BED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Número y tipo de visitas |
| Q02 | - |  |  | SI | Procedimientos |
| Q03 | - |  |  | SI | Oxigenoterapia |
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