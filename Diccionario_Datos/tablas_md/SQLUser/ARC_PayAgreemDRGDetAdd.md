# SQLUser.ARC_PayAgreemDRGDetAdd

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADD_ParRef | varchar | PK |  | NO | ARC_PayAgreemDRGDetails Parent Reference |
| ADD_AddOnDesc | varchar |  |  | SI | Add On Description |
| ADD_Childsub | double |  |  | NO | Childsub |
| ADD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADD_CreatedDate | date |  |  | SI | Created Date |
| ADD_CreatedTime | time |  |  | SI | Created Time |
| ADD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADD_DayFrom | double |  |  | SI | Day From |
| ADD_DayTo | double |  |  | SI | Day To |
| ADD_InlierAddon | double |  |  | SI | Inlier Addon |
| ADD_InlierPayorCode | varchar |  |  | SI | Inlier Add On Payor Code |
| ADD_OutlierAddon | double |  |  | SI | Outlier Addon |
| ADD_OutlierPayorCode | varchar |  |  | SI | Outlier Add On Payor Code |
| ADD_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| ADD_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| ADD_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ADD_RowId | varchar |  |  | NO | - |
| ADD_ShortInlierAddon | double |  |  | SI | Short Inlier Addon |
| ADD_ShortInlierPayorCode | varchar |  |  | SI | Short Inlier Add On Payor Code |
| ADD_UpdatedDate | date |  |  | SI | Updated Date |
| ADD_UpdatedTime | time |  |  | SI | Updated Time |
| ADD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Escala de Espasmos de Penn |
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