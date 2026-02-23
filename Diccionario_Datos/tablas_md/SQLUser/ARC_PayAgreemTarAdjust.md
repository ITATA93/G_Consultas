# SQLUser.ARC_PayAgreemTarAdjust

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADJ_ParRef | varchar | PK |  | NO | ARC_PayAgreemTariff Parent Reference |
| ADJ_Adjustment | double |  |  | SI | Adjustment (%) |
| ADJ_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| ADJ_Childsub | double |  |  | NO | Childsub |
| ADJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADJ_CreatedDate | date |  |  | SI | Created Date |
| ADJ_CreatedTime | time |  |  | SI | Created Time |
| ADJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADJ_DateFrom | date |  |  | NO | Date From |
| ADJ_DateTo | date |  |  | SI | Date To |
| ADJ_MaxAmtCovered | double |  |  | SI | Max Amt Covered |
| ADJ_MultFactor | double |  |  | SI | Multiplier Factor |
| ADJ_PayorShare | double |  |  | SI | Payor Share |
| ADJ_RowId | varchar |  |  | NO | - |
| ADJ_Type | varchar |  |  | SI | Type |
| ADJ_UpdatedDate | date |  |  | SI | Updated Date |
| ADJ_UpdatedTime | time |  |  | SI | Updated Time |
| ADJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ01DR | - |  |  | SI | Child Reference: Pauta Aplicada |
| Q02 | - |  |  | SI | Notas |
| Q02TxtOnly | - |  |  | SI | Notas Plain Text Only |
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