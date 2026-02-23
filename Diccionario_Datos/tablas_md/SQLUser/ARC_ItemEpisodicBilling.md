# SQLUser.ARC_ItemEpisodicBilling

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| EP_AnaestType_DR | bigint |  | FK | SI | Des Ref ORCAnaestType |
| EP_ApplyOrderDate | varchar |  |  | SI | Apply Order Date |
| EP_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| EP_BillAdditProcedures | varchar |  |  | SI | Bill Additional Procedures |
| EP_BillField1 | varchar |  |  | SI | BillField1 |
| EP_BillField2 | varchar |  |  | SI | BillField2 |
| EP_BillField3 | varchar |  |  | SI | BillField3 |
| EP_BillField4 | varchar |  |  | SI | BillField4 |
| EP_BillField5 | varchar |  |  | SI | BillField5 |
| EP_BillField6 | varchar |  |  | SI | BillField6 |
| EP_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| EP_CasePaymPrimaryProcOnly | varchar |  |  | SI | Case Payment Primary Procedure Only |
| EP_Childsub | double |  |  | NO | Childsub |
| EP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EP_Contract_DR | bigint |  | FK | SI | Des Ref Contract |
| EP_CreatedDate | date |  |  | SI | Created Date |
| EP_CreatedTime | time |  |  | SI | Created Time |
| EP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EP_DateFrom | date |  |  | SI | Date From |
| EP_DateTo | date |  |  | SI | Date To |
| EP_EpisBill_DR | bigint |  | FK | SI | Des Ref EpisBill |
| EP_EpisodeType | varchar |  |  | SI | Episode Type |
| EP_HOOverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| EP_HOOverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| EP_HOOverrideDesc | varchar |  |  | SI | Description |
| EP_HOPayorCode | varchar |  |  | SI | Payor Code  |
| EP_IncludePrivateSuppl | varchar |  |  | SI | Include Private Supplements |
| EP_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| EP_LOOverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| EP_LOOverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| EP_LOOverrideDesc | varchar |  |  | SI | Description |
| EP_LOPayorCode | varchar |  |  | SI | Payor Code  |
| EP_LinkItem_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| EP_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| EP_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| EP_OverrideDesc | varchar |  |  | SI | Description |
| EP_PayorCode | varchar |  |  | SI | Payor Code  |
| EP_Rank | double |  |  | SI | Rank |
| EP_RevertPerDiemHODays | varchar |  |  | SI | Revert to Per Diem for H/O Days |
| EP_RevertPerDiemLODays | varchar |  |  | SI | Revert to Per Diem for L/O Days |
| EP_RowId | varchar |  |  | NO | - |
| EP_UpdatedDate | date |  |  | SI | Updated Date |
| EP_UpdatedTime | time |  |  | SI | Updated Time |
| EP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Difficulty  swallowing |
| Q01N | - |  |  | SI | Note |
| Q02 | - |  |  | SI | Painful swallowing |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Abdominal or flank pain |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Character |
| Q04N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Location |
| Q09N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Duration |
| Q12 | - |  |  | SI | Worsened by |
| Q12N | - |  |  | SI | Note |
| Q14 | - |  |  | SI | Improved by |
| Q14N | - |  |  | SI | Note |
| Q16 | - |  |  | SI | Radiation |
| Q16N | - |  |  | SI | Note |
| Q18 | - |  |  | SI | Nausea |
| Q18N | - |  |  | SI | Note |
| Q20 | - |  |  | SI | Vomiting |
| Q20N | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Multiple episodes |
| Q22 | - |  |  | SI | Ongoing |
| Q23 | - |  |  | SI | Hematemesis / bloody vomitus |
| Q25 | - |  |  | SI | Blood in stools |
| Q25N | - |  |  | SI | Note |
| Q26 | - |  |  | SI | Dark red / melena |
| Q27 | - |  |  | SI | Bright red |
| Q28 | - |  |  | SI | Number of episodes |
| Q29 | - |  |  | SI | Last episode |
| Q30 | - |  |  | SI | Last episode time |
| Q31 | - |  |  | SI | Diarrhea |
| Q31N | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Frequency of episodes |
| Q34 | - |  |  | SI | Duration |
| Q35 | - |  |  | SI | Most recent episode |
| Q36 | - |  |  | SI | Stool description |
| Q38 | - |  |  | SI | Date |
| Q39 | - |  |  | SI | Time |
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