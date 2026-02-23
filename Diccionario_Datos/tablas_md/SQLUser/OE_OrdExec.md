# SQLUser.OE_OrdExec

**Schema:** SQLUser
**Columnas:** 223
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEORE_OEORI_ParRef | varchar | PK |  | NO | Des Ref to OEORI |
| ChildQ62DR | - |  |  | SI | Child Reference: Range of Motion (ROM) |
| OEORE_ActiveIngrUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| OEORE_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| OEORE_AdminVarReason | varchar |  |  | SI | Reason for administration variance |
| OEORE_AlertReason_DR | bigint |  | FK | SI | Des Ref AlertReason |
| OEORE_AltRecLoc_DR | bigint |  | FK | SI | Des Ref AltRecLoc |
| OEORE_AmountActiveIngr | double |  |  | SI | Amount of active ingredient   |
| OEORE_ApplyRate | varchar |  |  | SI | ApplyRate |
| OEORE_Appt_DR | varchar |  | FK | SI | Des Ref Appt |
| OEORE_BatchFTExpiryDate | date |  |  | SI | Free Text Batch Expiry Date |
| OEORE_BatchFreeText | varchar |  |  | SI | Batch Free Text |
| OEORE_Billed | varchar |  |  | SI | OEORE_Billed Flag |
| OEORE_BodySite_DR | bigint |  | FK | SI | Des Ref to BodySite |
| OEORE_CTPCPStarted_DR | varchar |  | FK | SI | Des Ref CTPCPStarted |
| OEORE_CTPCP_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| OEORE_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| OEORE_CarePlanGoalStatus | varchar |  |  | SI | Care Plan Goal Status |
| OEORE_Childsub | numeric |  |  | NO | OEORE Child Sub (New Key) |
| OEORE_ChosenAdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute Chosen from PHCAdminRouteMultiR... |
| OEORE_ChosenForm_DR | bigint |  | FK | SI | Des Ref PHCForm Chosen from Form |
| OEORE_ChosenIVType | varchar |  |  | SI | Chosen IV Type |
| OEORE_DateExecuted | date |  |  | SI | Date Executed |
| OEORE_DeferAdmin | varchar |  |  | SI | Defer Admin |
| OEORE_DeferAdminReason | varchar |  |  | SI | Defer Admin Reason |
| OEORE_DeliveryRate | double |  |  | SI | DeliveryRate |
| OEORE_DeliveryUOM_DR | bigint |  | FK | SI | DeliveryUOM |
| OEORE_Desc | varchar |  |  | SI | Short Description |
| OEORE_DilutionRequired | varchar |  |  | SI | Dilution Required Flag |
| OEORE_Dispensing_DR | varchar |  | FK | SI | Des Ref Dispensing |
| OEORE_Entry_DR | varchar |  | FK | SI | Des Ref Observ Entry |
| OEORE_ExEnDate | date |  |  | SI | ExEnDate |
| OEORE_ExEnTime | time |  |  | SI | ExEnTime |
| OEORE_ExStDate | date |  |  | SI | Execute Start Date |
| OEORE_ExStTime | time |  |  | SI | Execute Start Time |
| OEORE_ExVol | double |  |  | SI | ExVol |
| OEORE_ExpectedFinishDate | date |  |  | SI | ExpectedFinishDate |
| OEORE_ExpectedFinishTime | time |  |  | SI | ExpectedFinishTime |
| OEORE_ExtVaccBatchExpDate | date |  |  | SI | ExtVaccBatchExpDate |
| OEORE_ExtVaccBatchNumber | varchar |  |  | SI | ExtBatchNumber |
| OEORE_GlobalDispensed | varchar |  |  | SI | GlobalDispensed |
| OEORE_ICDDx_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| OEORE_IVCalcMethod | varchar |  |  | SI | IV calculation method 85138 standard type IVCalcMe... |
| OEORE_IVStartDropMin | double |  |  | SI | IVStartDropMin |
| OEORE_IVType | varchar |  |  | SI | IVType |
| OEORE_Instruction | varchar |  |  | SI | Instruction  |
| OEORE_IsConditional | varchar |  |  | SI | Execution node is a Conditional Dose |
| OEORE_IsInactive | varchar |  |  | SI | Is Inactive |
| OEORE_IsLastAdmin | varchar |  |  | SI | Is Last admin |
| OEORE_MedOutcome_DR | bigint |  | FK | SI | Des Ref MedOutcome |
| OEORE_MinPhQtyOrd | double |  |  | SI | Minimum Quantity Ordered, if is set than OEOREPhQt... |
| OEORE_O2DeliveryMethod_DR | bigint |  | FK | SI | O2 Delivery Method |
| OEORE_O2Rate | double |  |  | SI | O2 Rate |
| OEORE_O2RateCalMethod | varchar |  |  | SI | O2 Rate Calculation Method |
| OEORE_O2RateUOM_DR | bigint |  | FK | SI | O2 Rate UOM |
| OEORE_OffsetExec_DR | varchar |  | FK | SI | Offset Exec DR
Offset from this execution node
F... |
| OEORE_OffsetItem_DR | varchar |  | FK | SI | Offset Item DR
Offset from this order item
For r... |
| OEORE_OffsetType | varchar |  |  | SI | Offset Type
Standard Type OrderOffsetType 
For r... |
| OEORE_OffsetUnit | varchar |  |  | SI | Offset Unit
Standard Type DurationPlus 
For rela... |
| OEORE_OffsetValue | double |  |  | SI | Offset Value 
For relative time offsets |
| OEORE_OrderItemChange_DR | bigint |  | FK | SI | Order Item Change DR
Latest order modification ap... |
| OEORE_Order_Status_DR | bigint |  | FK | SI | Order Status Des Ref to OECOrdStat |
| OEORE_Outcome_DR | bigint |  | FK | SI | Des Ref Outcome |
| OEORE_OverseeUser_DR | bigint |  | FK | SI | Des Ref OverseeUser |
| OEORE_PCALoadingDose | double |  |  | SI | PCALoadingDose  |
| OEORE_PHCDuration_DR | bigint |  | FK | SI | Des Ref to PHCDU (HealthShare Specific) |
| OEORE_PHCFreq_DR | bigint |  | FK | SI | Des Ref to Freq (HealthShare Specific) |
| OEORE_PRNReason | varchar |  |  | SI | PRNReason |
| OEORE_PRNStockRequested | varchar |  |  | SI | PRN Stock Requested |
| OEORE_PartialOriginID | integer |  |  | SI | Partial administrations:
Child id {OEORE_Childsub... |
| OEORE_PatchRemoveDate | date |  |  | SI | Patch Remove Date  |
| OEORE_PatchRemoveTime | time |  |  | SI | Patch Remove Time  |
| OEORE_PhQtyIss | double |  |  | SI | Ph Qty Issued |
| OEORE_PhQtyOrd | double |  |  | SI | Quantity Ordered, if OEOREMinPhQtyOrd is set than ... |
| OEORE_PrevAdminEndDate | date |  |  | SI | PrevAdminEndDate |
| OEORE_PrevAdminEndTime | time |  |  | SI | PrevAdminEndTime |
| OEORE_PrevBagVolume | double |  |  | SI | PrevBagVolume |
| OEORE_PrimaryIntervention | varchar |  |  | SI | PrimaryIntervention |
| OEORE_PumpLine | varchar |  |  | SI | ID of pump and line pair that are associated with ... |
| OEORE_QtyAdmin | double |  |  | SI | Quantity Administered |
| OEORE_RVIBC_DR | varchar |  | FK | SI | Des Ref RVIBC |
| OEORE_Route_DR | bigint |  | FK | SI | Des Ref Route |
| OEORE_RowId | varchar |  |  | NO | - |
| OEORE_SeqPlanStartDate | date |  |  | SI | Sequence Planned Start Date |
| OEORE_SeqPlanStartTime | time |  |  | SI | Sequence Planned Start Time |
| OEORE_SignFile | varchar |  |  | SI | Signature File |
| OEORE_Signature | varchar |  |  | SI | Signature |
| OEORE_SkinTestOutcome_DR | bigint |  | FK | SI | Des Ref SkinTestOutcome |
| OEORE_StDateTime | varchar |  |  | SI | Start Date Time |
| OEORE_StartTime | double |  |  | SI | StartTime |
| OEORE_StartVolume | double |  |  | SI | StartVolume |
| OEORE_StockBatches | varchar |  |  | SI | StockBatches |
| OEORE_SubsHideFlag | varchar |  |  | SI | Substitution Hide Flag |
| OEORE_Text1 | varchar |  |  | SI | Free Text Field 1 |
| OEORE_TimeExecuted | time |  |  | SI | Time Executed |
| OEORE_TimeTaken | double |  |  | SI | Time Taken |
| OEORE_TimeUnit | varchar |  |  | SI | TimeUnit |
| OEORE_VarianceReason_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason |
| OEORE_VolOfDiluent | double |  |  | SI | VolOfDiluent  |
| OEORE_VolRateChange | double |  |  | SI | VolRateChange |
| OEORE_VolumeUnit | varchar |  |  | SI | VolumeUnit |
| OEORE_XDate | date |  |  | SI | Cross Out Date |
| OEORE_XTime | time |  |  | SI | Cross Out Time |
| Q01 | - |  |  | SI | Occupation |
| Q02 | - |  |  | SI | Affected knee |
| Q03 | - |  |  | SI | Contralateral |
| Q04 | - |  |  | SI | VAS score |
| Q05 | - |  |  | SI | Pain location |
| Q06 | - |  |  | SI | Pain description |
| Q07 | - |  |  | SI | Pain pattern worse with the following |
| Q08 | - |  |  | SI | Other |
| Q09 | - |  |  | SI | Pain pattern better with the following |
| Q10 | - |  |  | SI | Other |
| Q11 | - |  |  | SI | Pain pattern normal with the following |
| Q12 | - |  |  | SI | Other |
| Q13 | - |  |  | SI | Stiffness |
| Q14 | - |  |  | SI | Swelling |
| Q15 | - |  |  | SI | When the swelling happend |
| Q16 | - |  |  | SI | Pain present since |
| Q17 | - |  |  | SI | Pain progress |
| Q18 | - |  |  | SI | Reason |
| Q19 | - |  |  | SI | Mechanism of Injury |
| Q20 | - |  |  | SI | Medical history |
| Q21 | - |  |  | SI | Other |
| Q22 | - |  |  | SI | Previous surgery |
| Q23 | - |  |  | SI | Comment |
| Q24 | - |  |  | SI | Previous physical therapy treatment |
| Q25 | - |  |  | SI | X-ray |
| Q26 | - |  |  | SI | Report |
| Q27 | - |  |  | SI | Patient goals |
| Q28 | - |  |  | SI | Gait |
| Q29 | - |  |  | SI | Comment |
| Q30 | - |  |  | SI | Normal genu valgum |
| Q31 | - |  |  | SI | Genu varum |
| Q32 | - |  |  | SI | Genu recurvatum |
| Q33 | - |  |  | SI | Patella position |
| Q34 | - |  |  | SI | Effusion |
| Q35 | - |  |  | SI | Effusion right |
| Q36 | - |  |  | SI | Effusion left |
| Q37 | - |  |  | SI | Atrophy |
| Q38 | - |  |  | SI | Other |
| Q39 | - |  |  | SI | Temperature |
| Q40 | - |  |  | SI | Patella mobility |
| Q41 | - |  |  | SI | Tibial tubercle |
| Q42 | - |  |  | SI | Patella tendon |
| Q43 | - |  |  | SI | Quadriceps tendon |
| Q44 | - |  |  | SI | Ligaments LCL |
| Q45 | - |  |  | SI | Ligaments MCL |
| Q46 | - |  |  | SI | Other |
| Q47 | - |  |  | SI | Girth above 15 cm left |
| Q48 | - |  |  | SI | Girth above 15 cm right |
| Q49 | - |  |  | SI | Girth 5 cm left |
| Q50 | - |  |  | SI | Girth 5 cm right |
| Q51 | - |  |  | SI | Girth med patella left |
| Q52 | - |  |  | SI | Girth med patella right |
| Q53 | - |  |  | SI | Girth 15 cm left |
| Q54 | - |  |  | SI | Girth 15 cm right |
| Q55 | - |  |  | SI | Girth Measurements |
| Q58 | - |  |  | SI | Leg length |
| Q59 | - |  |  | SI | Leg length (cm) |
| Q60 | - |  |  | SI | Q Angle right |
| Q61 | - |  |  | SI | Q Angle left |
| Q65 | - |  |  | SI | Other special test |
| Q66 | - |  |  | SI | Diagnosis |
| Q67 | - |  |  | SI | Problems list |
| Q68 | - |  |  | SI | Rehabilitation potential |
| Q69 | - |  |  | SI | Patient / Family participation |
| Q70 | - |  |  | SI | Comment |
| Q71 | - |  |  | SI | Education |
| Q72 | - |  |  | SI | Short term goals |
| Q73 | - |  |  | SI | Long term goals |
| Q74 | - |  |  | SI | Treatment |
| Q75 | - |  |  | SI | Other |
| Q76 | - |  |  | SI | Number of treatments per week |
| Q77 | - |  |  | SI | Number of weeks |
| Q78 | - |  |  | SI | Re Evaluation |
| Q79 | - |  |  | SI | Chief Complaint |
| Q80 | - |  |  | SI | Observation |
| Q81 | - |  |  | SI | Alignment |
| Q82 | - |  |  | SI | Palpation |
| Q83 | - |  |  | SI | Examination |
| Q84 | - |  |  | SI | Date |
| Q85 | - |  |  | SI | Time |
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