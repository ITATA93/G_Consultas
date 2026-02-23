# SQLUser.OE_LoanTrans

**Schema:** SQLUser
**Columnas:** 177
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOAN_RowId | bigint | PK |  | NO | - |
| LOAN_BatchNo | varchar |  |  | SI | Batch Number (Serial Number) |
| LOAN_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| LOAN_CollectionDate | date |  |  | SI | CollectionDate |
| LOAN_DateCreated | date |  |  | SI | DateCreated |
| LOAN_DateUpdated | date |  |  | SI | DateUpdated |
| LOAN_Deposit | double |  |  | SI | Loan Deposit Amount |
| LOAN_ExpReturnDate | date |  |  | SI | ExpReturnDate |
| LOAN_LostItem | varchar |  |  | SI | LostItem |
| LOAN_Notes | varchar |  |  | SI | Notes for Care Provider |
| LOAN_OrdItem_DR | varchar |  | FK | SI | Des Ref OrdItem |
| LOAN_OrdLoanStat | varchar |  |  | SI | OrdLoanStat |
| LOAN_OrdLoc_DR | bigint |  | FK | SI | Des Ref CTLOC Receiving Location |
| LOAN_OrdStatus_DR | bigint |  | FK | SI | Des Ref OECOrderStatus |
| LOAN_OrderDate | date |  |  | SI | OrderDate |
| LOAN_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| LOAN_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPatMas |
| LOAN_ReturnDate | date |  |  | SI | ReturnDate |
| LOAN_StockLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LOAN_TimeCreated | time |  |  | SI | TimeCreated |
| LOAN_TimeUpdated | time |  |  | SI | TimeUpdated |
| LOAN_UseUpdated_DR | bigint |  | FK | SI | Des Ref SSUser |
| LOAN_UserCreated_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q01 | - |  |  | SI | Developmental Evaluation |
| Q02 | - |  |  | SI | Gross motor |
| Q03 | - |  |  | SI | Fine Motor |
| Q04 | - |  |  | SI | Dominant hand |
| Q05 | - |  |  | SI | Grasping / Releasing |
| Q06 | - |  |  | SI | Handwriting |
| Q07 | - |  |  | SI | Manipulation |
| Q08 | - |  |  | SI | Hand eye coordination |
| Q09 | - |  |  | SI | Note |
| Q10 | - |  |  | SI | Social |
| Q100 | - |  |  | SI | Goal |
| Q101 | - |  |  | SI | Type |
| Q102 | - |  |  | SI | Type |
| Q103 | - |  |  | SI | Performance |
| Q104 | - |  |  | SI | Performance |
| Q105 | - |  |  | SI | Satisfaction |
| Q106 | - |  |  | SI | Goal |
| Q107 | - |  |  | SI | Goal |
| Q108 | - |  |  | SI | Type |
| Q109 | - |  |  | SI | Type |
| Q11 | - |  |  | SI | Language |
| Q110 | - |  |  | SI | Performance |
| Q111 | - |  |  | SI | Performance |
| Q112 | - |  |  | SI | Satisfaction |
| Q113 | - |  |  | SI | Satisfaction |
| Q114 | - |  |  | SI | Satisfaction |
| Q12 | - |  |  | SI | Reflex testing |
| Q13 | - |  |  | SI | Note |
| Q14 | - |  |  | SI | Sensory Integration |
| Q15 | - |  |  | SI | Tactile |
| Q16 | - |  |  | SI | Proprioception |
| Q17 | - |  |  | SI | Vestibular |
| Q18 | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Perception |
| Q20 | - |  |  | SI | Follow command |
| Q21 | - |  |  | SI | Orientation |
| Q22 | - |  |  | SI | Orientation test |
| Q23 | - |  |  | SI | Attention span |
| Q24 | - |  |  | SI | Activity |
| Q25 | - |  |  | SI | Activity |
| Q26 | - |  |  | SI | Spending time |
| Q27 | - |  |  | SI | minutes |
| Q28 | - |  |  | SI | Distraction |
| Q29 | - |  |  | SI | times |
| Q30 | - |  |  | SI | Dysphagia evaluation |
| Q31 | - |  |  | SI | Fall Risk Assessment |
| Q32 | - |  |  | SI | Fall risk |
| Q33 | - |  |  | SI | High risk by |
| Q34 | - |  |  | SI | Fracture risk |
| Q35 | - |  |  | SI | Pain Assessment |
| Q36 | - |  |  | SI | Does patient have pain? |
| Q37 | - |  |  | SI | Location |
| Q38 | - |  |  | SI | Assessment tool |
| Q39 | - |  |  | SI | Pain assessment core |
| Q40 | - |  |  | SI | Characteristic of pain |
| Q41 | - |  |  | SI | Other characteristic |
| Q42 | - |  |  | SI | Frequency |
| Q43 | - |  |  | SI | Duration |
| Q44 | - |  |  | SI | Pain re-assessment score |
| Q45 | - |  |  | SI | Goals and Planning |
| Q46 | - |  |  | SI | Goal No 1 |
| Q47 | - |  |  | SI | Type |
| Q48 | - |  |  | SI | Performance |
| Q49 | - |  |  | SI | Satisfaction |
| Q50 | - |  |  | SI | Goal No 2 |
| Q51 | - |  |  | SI | Type |
| Q52 | - |  |  | SI | Performance |
| Q53 | - |  |  | SI | Satisfaction |
| Q54 | - |  |  | SI | Goal No 3 |
| Q55 | - |  |  | SI | Type |
| Q56 | - |  |  | SI | Performance |
| Q57 | - |  |  | SI | Satisfaction |
| Q58 | - |  |  | SI | Goal No 4 |
| Q59 | - |  |  | SI | Type |
| Q60 | - |  |  | SI | Performance |
| Q61 | - |  |  | SI | Satisfaction |
| Q62 | - |  |  | SI | Intervention plan |
| Q63 | - |  |  | SI | Re-assessment date |
| Q64 | - |  |  | SI | Goal |
| Q65 | - |  |  | SI | Instruction |
| Q66 | - |  |  | SI | Patient and/or family was given and understood abo... |
| Q67 | - |  |  | SI | Need reviewed |
| Q68 | - |  |  | SI | Reach |
| Q69 | - |  |  | SI | Pinches |
| Q70 | - |  |  | SI | Grasping |
| Q71 | - |  |  | SI | Releasing |
| Q72 | - |  |  | SI | Bilateral coordination of hands |
| Q73 | - |  |  | SI | Writing and Drawing |
| Q74 | - |  |  | SI | Grip |
| Q75 | - |  |  | SI | Mark making |
| Q76 | - |  |  | SI | Scribbles |
| Q77 | - |  |  | SI | Shapes ( I, -, +, H, O, triangle, cross) |
| Q78 | - |  |  | SI | Was E.T.C.H. performed? |
| Q79 | - |  |  | SI | Writing and Drawing notes |
| Q80 | - |  |  | SI | Vision |
| Q81 | - |  |  | SI | Fixation |
| Q82 | - |  |  | SI | Tracking |
| Q83 | - |  |  | SI | Convergence |
| Q84 | - |  |  | SI | Vision notes |
| Q85 | - |  |  | SI | Completed puzzle |
| Q86 | - |  |  | SI | Was MVPT-R completed? |
| Q87 | - |  |  | SI | Was BERRY VMI completed? |
| Q88 | - |  |  | SI | Notes |
| Q89 | - |  |  | SI | Date |
| Q90 | - |  |  | SI | Time |
| Q91 | - |  |  | SI | EXAMPLE |
| Q92 | - |  |  | SI | Type |
| Q93 | - |  |  | SI | Performance |
| Q94 | - |  |  | SI | Satisfaction |
| Q95 | - |  |  | SI | Goal No 1 |
| Q96 | - |  |  | SI | Goal No 2 |
| Q97 | - |  |  | SI | Goal No 3 |
| Q98 | - |  |  | SI | Goal No 4 |
| Q99 | - |  |  | SI | Goal |
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