# SQLUser.ARC_PayAgreemBillByBillGrp

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLBYGRP_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| BILLBYGRP_BillDesc_DR | bigint |  | FK | SI | Des Ref ARCBillDescription |
| BILLBYGRP_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| BILLBYGRP_Childsub | double |  |  | NO | Childsub |
| BILLBYGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BILLBYGRP_CreatedDate | date |  |  | SI | Created Date |
| BILLBYGRP_CreatedTime | time |  |  | SI | Created Time |
| BILLBYGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BILLBYGRP_Entry | double |  |  | SI | Entry |
| BILLBYGRP_EpisodeType | varchar |  |  | SI | EpisodeType |
| BILLBYGRP_Priority_DR | bigint |  | FK | SI | Des Ref OECPriority |
| BILLBYGRP_Rank | double |  |  | SI | Rank |
| BILLBYGRP_RecLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| BILLBYGRP_RowId | varchar |  |  | NO | - |
| BILLBYGRP_Text1 | varchar |  |  | SI | Text1 |
| BILLBYGRP_Text2 | varchar |  |  | SI | Text2 |
| BILLBYGRP_Text3 | varchar |  |  | SI | Text3 |
| BILLBYGRP_UpdatedDate | date |  |  | SI | Updated Date |
| BILLBYGRP_UpdatedTime | time |  |  | SI | Updated Time |
| BILLBYGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Escala de Fuerza Muscular |
| Q02 | - |  |  | SI | Músculo o Grupo Muscular Evaluado |
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