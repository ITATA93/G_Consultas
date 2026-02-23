# SQLUser.ARC_PayAgreemBGLimits

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIM_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| LIM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| LIM_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| LIM_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| LIM_Childsub | double |  |  | NO | Childsub |
| LIM_CoPaymentPercentage | double |  |  | SI | Co-Payment Percentage |
| LIM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LIM_CreatedDate | date |  |  | SI | Created Date |
| LIM_CreatedTime | time |  |  | SI | Created Time |
| LIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LIM_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| LIM_EpisodeType | varchar |  |  | SI | EpisodeType |
| LIM_MaxAmountAllowed | double |  |  | SI | Maximum Amount Allowed |
| LIM_MaxCoPayAmountBeforeTax | double |  |  | SI | Maximum Co-Payment Amount Before Tax |
| LIM_MaxCoPaymentAmount | double |  |  | SI | Maximum Co-Payment Amount |
| LIM_MaxCoverage | double |  |  | SI | Max Coverage |
| LIM_MinCoPaymentAmount | double |  |  | SI | Minimum Co-Payment Amount |
| LIM_OrderStatus_DR | bigint |  | FK | SI | Des Ref OrderStatus |
| LIM_PatShareDiscountAmount | double |  |  | SI | Patient Share Discount Amount |
| LIM_PatShareDiscountPerc | double |  |  | SI | Patient Share Discount Percentage |
| LIM_PatientAmount | double |  |  | SI | Patient Amount |
| LIM_PayorPercent | double |  |  | SI | Payor Percent |
| LIM_Priority_DR | bigint |  | FK | SI | Des Ref OECPriority |
| LIM_Qty | double |  |  | SI | Qty |
| LIM_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| LIM_RowId | varchar |  |  | NO | - |
| LIM_UpdatedDate | date |  |  | SI | Updated Date |
| LIM_UpdatedTime | time |  |  | SI | Updated Time |
| LIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Paresia Facial |
| Q02 | - |  |  | SI | Paresia Braquial |
| Q03 | - |  |  | SI | Lenguaje |
| Q04 | - |  |  | SI | Resultado |
| Q04ObsDR | - |  |  | SI | Resultado DR |
| Q05 | - |  |  | SI | Recomendaciones |
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