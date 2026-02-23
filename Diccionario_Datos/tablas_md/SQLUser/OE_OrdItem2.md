# SQLUser.OE_OrdItem2

**Schema:** SQLUser
**Columnas:** 302
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM2_ParRef | numeric | PK |  | NO | OE_Order Parent Reference |
| ChildQ59DR | - |  |  | SI | Child Reference: Deep Tendon Reflexes |
| ITM2_APCVM_DR | bigint |  | FK | SI | Des Ref to APCVendor, stock item vendor |
| ITM2_AcceptDisabilityInd | varchar |  |  | SI | AcceptedDisabilityInd |
| ITM2_AcceptDisabilityText | varchar |  |  | SI | AcceptedDisabilityText |
| ITM2_AccountPeriod_DR | bigint |  | FK | SI | Des Ref BLCAccountingPeriod |
| ITM2_ActivityType_DR | bigint |  | FK | SI | Des Ref OECActivityType |
| ITM2_AdjustDiscGLAccount_DR | bigint |  | FK | SI | Adjustment Discount GL Account, Des Ref GLCAcct |
| ITM2_AdminFirstNode | varchar |  |  | SI | First Node Marked to be Administered |
| ITM2_AltBodyWeightObs_DR | varchar |  | FK | SI | Alternative Body Weight Observation |
| ITM2_AntimicrobialApprovalNo | varchar |  |  | SI | Antimicrobial Approval Number  |
| ITM2_ApprovalAdminReq | varchar |  |  | SI | Approval for Administration Required |
| ITM2_ApprovalAdminReqDate | date |  |  | SI | Date ITM2ApprovalAdminReq flag was changed |
| ITM2_ApprovalAdminReqTime | time |  |  | SI | Time ITM2ApprovalAdminReq flag was changed |
| ITM2_AuthorityCode | varchar |  |  | SI | Authority Code |
| ITM2_AuthorityNumber | varchar |  |  | SI | Authority Number |
| ITM2_AutoResolved | bit |  |  | SI | Auto Resolved to Item by System |
| ITM2_BPGDoseBased | varchar |  |  | SI | Dose based |
| ITM2_BPGUOM_DR | bigint |  | FK | SI | Units of measurement |
| ITM2_BPQuantity | numeric |  |  | SI | Quantity requested
For dose based products |
| ITM2_BPRecentTransfusionPregnancy | varchar |  |  | SI | Patient has had recent transfusion or pregnancy
F... |
| ITM2_BPRequiredByDate | date |  |  | SI | Required Date |
| ITM2_BPRequiredByTime | time |  |  | SI | Required Date |
| ITM2_BPReservationPeriod | integer |  |  | SI | Reservation period |
| ITM2_BPReservationPeriodUnit | varchar |  |  | SI | Reservation period unit |
| ITM2_CNMItemNotes | varchar |  |  | SI | Controlled e-Prescription Item Notes |
| ITM2_CNMNo | varchar |  |  | SI | Controlled e-Prescription Number |
| ITM2_CNMOverrideReason | varchar |  |  | SI | Controlled e-Prescription Override Reason |
| ITM2_CNMStatus_DR | bigint |  | FK | SI | Controlled e-Prescription Status |
| ITM2_CalDoseHTMLPlainText | bigint |  |  | SI |  Calculate Dose ckeditor Plain Text |
| ITM2_CalDoseHTMLRichText | bigint |  |  | SI | Calculate Dose ckeditor Rich Text |
| ITM2_CalTemplateParamsDR_DCTCTUOMDR | bigint |  | FK | SI | - |
| ITM2_CalTemplateParamsDR_DCTDurationUnit | varchar |  |  | SI | - |
| ITM2_CalTemplateParamsDR_Details | varchar |  |  | SI | - |
| ITM2_CalTemplate_DR | bigint |  | FK | SI | Calendar Template |
| ITM2_CalcDoseDetail | varchar |  |  | SI | CalcDoseDetail |
| ITM2_CalcIVDose | varchar |  |  | SI | CalcIVDose |
| ITM2_CancelRemainDate | date |  |  | SI | CancelRemainDate |
| ITM2_CancelRemainReason | varchar |  |  | SI | CancelRemainingReason  |
| ITM2_CancelRemainRepeats | varchar |  |  | SI | CancelRemainRepeats  |
| ITM2_CancelRemainTime | time |  |  | SI | CancelRemainTime |
| ITM2_CancelRemainUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| ITM2_CarePlanIssues_DR | varchar |  | FK | SI | Des Ref NRCarePlanIssues  |
| ITM2_Childsub | double |  |  | NO | Childsub |
| ITM2_ComplementaryService | varchar |  |  | SI | Item is a complementary Service |
| ITM2_CompletionDate | date |  |  | SI | CompletionDate |
| ITM2_Confidential | varchar |  |  | SI | Confidential |
| ITM2_ContrDiscGLAccount_DR | bigint |  | FK | SI | Contract Discount GL Account, Des Ref GLCAcct |
| ITM2_CopyCycleOrder | varchar |  |  | SI | Copy From Previous Cycle |
| ITM2_CopyFromOEORI_DR | varchar |  | FK | SI | Des Ref OEOrdItem - order from which current order... |
| ITM2_CostCentre_DR | bigint |  | FK | SI | Des Ref GLCCC |
| ITM2_DMCopied | varchar |  |  | SI | Dosing Model Copied State: 1) Y (Yes) 2) N(No) 3) ... |
| ITM2_DateMoreStockReq | date |  |  | SI | Date More Stock Requested |
| ITM2_DatePORAuthorised | date |  |  | SI | DatePORAuthorised |
| ITM2_DeliveryRate | double |  |  | SI | DeliveryRate |
| ITM2_DeliveryUOM_DR | bigint |  | FK | SI | DeliveryUOM |
| ITM2_Derived | double |  |  | SI | Derived |
| ITM2_DiscretDiscGLAccount_DR | bigint |  | FK | SI | Discretionary Discount GL Account, Des Ref GLCAcct |
| ITM2_DispenseType | varchar |  |  | SI | Dispense Type |
| ITM2_DistanceKms | double |  |  | SI | DistanceKms |
| ITM2_DoNotSubstitute | varchar |  |  | SI | DoNotSubstitute |
| ITM2_DoseCalDesc | varchar |  |  | SI | Dose Range Short Description |
| ITM2_DoseCalLinkedNONTCLELabs | varchar |  |  | SI | Dose Range Linked NON TCLE Lab List |
| ITM2_DoseCalLinkedObs | varchar |  |  | SI | Dose Range Linked Observation List |
| ITM2_DoseCalLinkedTCLELabs | varchar |  |  | SI | Dose Range Linked Lab Item List |
| ITM2_DoseCalProtocolBase | double |  |  | SI | Dose Range Protocol Base |
| ITM2_DoseCalRangeFrom | double |  |  | SI | Dose Range From  |
| ITM2_DoseCalRangeTo | double |  |  | SI | Dose Range To |
| ITM2_DoseCalRangeUnit | bigint |  |  | SI | Dose Range Unit |
| ITM2_DoseInML | double |  |  | SI | Dose in ML |
| ITM2_DoseModelDoseChange | bit |  |  | SI | ITM2DoseModelDoseChange |
| ITM2_DoseModelFrequencyChange | bit |  |  | SI | ITM2DoseModelFrequencyChange |
| ITM2_DoseRecalPermitted | bit |  |  | SI |  Dose Recalculation at Administration Permitted |
| ITM2_DosingModelChangeType | varchar |  |  | SI | Dosing Model Change Type |
| ITM2_DrgHistDesc_DR | varchar |  | FK | SI | Des Ref PHCDrgHistDesc |
| ITM2_DropsMin | double |  |  | SI | DropsMin |
| ITM2_DuplServOverrideReason | varchar |  |  | SI | Duplicate service override Reason |
| ITM2_DurationType | varchar |  |  | SI | DurationType |
| ITM2_DurationUnit | varchar |  |  | SI |  DurationUnit |
| ITM2_DurationValue | double |  |  | SI | DurationValue |
| ITM2_EPrescItemNotes | varchar |  |  | SI | e-Prescription Item Notes |
| ITM2_EPrescNo | varchar |  |  | SI | e-Prescription Number |
| ITM2_EPrescOverrideReason | bigint |  |  | SI | e-Prescription Override Reason |
| ITM2_EPrescStatus | bigint |  |  | SI | e-Prescription Status |
| ITM2_EnteredInError | varchar |  |  | SI | Entered in Error |
| ITM2_EquipmentId | double |  |  | SI | Equipment Id |
| ITM2_Equipment_DR | bigint |  | FK | SI | Des Ref RBCEquipment  |
| ITM2_Event | varchar |  |  | SI | Event |
| ITM2_ExcludeFromSequence | varchar |  |  | SI | Exclude From Sequence Plan |
| ITM2_ExcludeReason | varchar |  |  | SI | Reason For Exclusion Of Order Items |
| ITM2_ExcludedFromPayorRank1 | varchar |  |  | SI | ExcludedFromPayorRank1 |
| ITM2_ExpiryDate | date |  |  | SI | ExpiryDate |
| ITM2_ExpiryDateProcessed | varchar |  |  | SI | ExpiryDateProcessed |
| ITM2_ExtCode | varchar |  |  | SI | ExtCode |
| ITM2_ExternalDocFiscalCode | varchar |  |  | SI | External Doctor Fiscal Code |
| ITM2_ExternalPaperPrescNo | varchar |  |  | SI | External PAPER Prescription Number |
| ITM2_ExternalPrescriptionID | varchar |  |  | SI | External Prescription Item Identifier |
| ITM2_FieldQuantity | double |  |  | SI | Field Quantity |
| ITM2_FinApprLastUpdateDate | date |  |  | SI | Finance Approved Date |
| ITM2_FinApprLastUpdateTime | time |  |  | SI | Finance Approved Time |
| ITM2_FinApprLastUpdateUser_DR | bigint |  | FK | SI | Des Ref SSUSR |
| ITM2_FinDate | date |  |  | SI | Finish Date of the order |
| ITM2_FinanceApproved | varchar |  |  | SI | ExcludedFromPayorRank1 |
| ITM2_FinanceApprovedOverride | varchar |  |  | SI | Finance approved override |
| ITM2_FinanceApprvComments | varchar |  |  | SI | Finance Approved Comments |
| ITM2_FirstBillDate | date |  |  | SI | First Bill Date |
| ITM2_FlowRateLabel | varchar |  |  | SI | FlowRateLabel |
| ITM2_FluidConsistMod_DR | bigint |  | FK | SI | Fluid Consistency Modification |
| ITM2_FluidVolumeRestr_DR | bigint |  | FK | SI | Fluid Volume Restriction |
| ITM2_FoodTextureMod_DR | bigint |  | FK | SI | Food Texture Modification |
| ITM2_FormAltReason_DR | bigint |  | FK | SI | Des Ref OECFormAlternativeReason  |
| ITM2_FreeTextFreqUnit | varchar |  |  | SI | Free Text Frequency Unit |
| ITM2_FreeTextFreqValue | double |  |  | SI | Free Text Frequency Value  |
| ITM2_GFR | varchar |  |  | SI | GFR At Time Of Order As A list: Value, UOM Descipt... |
| ITM2_GenericHistDesc_DR | varchar |  | FK | SI | Des Ref PHCGenericHistDesc |
| ITM2_GenericRtForms_DR | varchar |  | FK | SI | Des Ref to PHCGenericRtForms |
| ITM2_Group_DR | bigint |  | FK | SI | Des Ref SSGroup |
| ITM2_HasSequenceData | varchar |  |  | SI | Item Has Sequence Plan Data |
| ITM2_IVCalcMethod | varchar |  |  | SI | IV calculation method 85138 standard type IVCalcMe... |
| ITM2_IVContTotalDose | double |  |  | SI | IVContTotalDose |
| ITM2_IVContTotalDoseUnit_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| ITM2_IVDose | double |  |  | SI | IVDose  |
| ITM2_IVUnit_DR | bigint |  | FK | SI | Des Ref CTUOM |
| ITM2_InHospService | varchar |  |  | SI | In Hospital Service |
| ITM2_Indication | varchar |  |  | SI | Order Indication |
| ITM2_InfusTypeEndDate | date |  |  | SI | Deprecated
Infusion Type End Date |
| ITM2_InfusTypeEndTime | time |  |  | SI | Deprecated
Infusion Type End Time |
| ITM2_Instructions | varchar |  |  | SI | Instructions |
| ITM2_LMPKnown | varchar |  |  | SI | LMP Date Known |
| ITM2_LSPNum | varchar |  |  | SI | LSPNum |
| ITM2_LabelNotes | varchar |  |  | SI | Label Direction Notes |
| ITM2_Laterality_DR | bigint |  | FK | SI | Laterality - Radiology |
| ITM2_Link | varchar |  |  | SI | Link  |
| ITM2_LoanEquipRetDate | date |  |  | SI | LoanEquipRetDate |
| ITM2_LostLoanItem | varchar |  |  | SI | LostLoanItem |
| ITM2_MRMedLinkedOrder | varchar |  |  | SI | ID of linked hospital/discharge order in MRMed Rec... |
| ITM2_MaintenanceDose | double |  |  | SI | Maintenance Dose |
| ITM2_MaintenanceInstruction | varchar |  |  | SI | Maintenance Instruction |
| ITM2_MaintenanceType | varchar |  |  | SI | Maintenance Type  |
| ITM2_MaxDeliveryRate | double |  |  | SI | Max Delivery Rate |
| ITM2_MedReconComments | varchar |  |  | SI | Medication Reconcilation Comments |
| ITM2_MedReconDischComments | varchar |  |  | SI | Medication Reconcilation Discharge Comments |
| ITM2_MedSubsOEORI_DR | varchar |  | FK | SI | medication substitution item, Des Ref OEOrdItem |
| ITM2_MedicationSource_DR | bigint |  | FK | SI | Des Ref PHCMedicationSource  |
| ITM2_Medication_DR | varchar |  | FK | SI | Des Ref MRMedication |
| ITM2_Message_DR | bigint |  | FK | SI | Des Ref SSMessage |
| ITM2_MinDeliveryRate | double |  |  | SI | Min Delivery Rate |
| ITM2_MinDoseQty | varchar |  |  | SI | Minimum Dose Quantity, if set than OEORIDoseQty of... |
| ITM2_MinPhQtyOrd | varchar |  |  | SI | Minimum Quantity |
| ITM2_ModifyExistPastNodes | varchar |  |  | SI | Modify Exisiting Past Nodes  |
| ITM2_MultPrSamePatSameDocSameDay | varchar |  |  | SI | Multiple Procedure Same Patient, Same Provider, Sa... |
| ITM2_MultProcNotes | varchar |  |  | SI | Multiple Procedure Notes |
| ITM2_MultiResolveIncludeNonFormulary | varchar |  |  | SI | - |
| ITM2_MultiResolveStockLoc_DR | bigint |  | FK | SI | - |
| ITM2_NFMICategDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart  |
| ITM2_NewPRNMaxDose24hrs | double |  |  | SI | NewPRNMaxDose24hrs |
| ITM2_NewPRNMaxDose24hrsUnit_DR | bigint |  | FK | SI | NewPRNMaxDose24hrsUnit |
| ITM2_NewPRNMaxDoseHrs | double |  |  | SI | PRNMaxDoseHrs |
| ITM2_NewPRNMaxDoseNumHrs | integer |  |  | SI | PRNMaxDoseNumHrs |
| ITM2_NonMeteredDose | bit |  |  | SI | Non-Metered Dose |
| ITM2_NonPBSQuanUOMDR | bigint |  | FK | SI | Non-PBS Quantity Unit |
| ITM2_NonPBSQuantity | double |  |  | SI | Non-PBS Quantity |
| ITM2_NotifUsersChangeOrder | varchar |  |  | SI | Notify users of change to order  |
| ITM2_O2AdminOver | double |  |  | SI | O2 Administer Over (Value) |
| ITM2_O2AdminOverUnit | varchar |  |  | SI | O2 Administer Over (Unit) |
| ITM2_O2ContDelivery | varchar |  |  | SI | O2 Continuous Delivery |
| ITM2_O2DeliveryMethod_DR | bigint |  | FK | SI | O2 Delivery Method |
| ITM2_O2MaxRate | double |  |  | SI | Max O2 Rate |
| ITM2_O2Rate | double |  |  | SI | O2 Rate |
| ITM2_O2RateCalMethod | varchar |  |  | SI | O2 Rate Calculation Method |
| ITM2_O2RateUOM_DR | bigint |  | FK | SI | O2 Rate UOM |
| ITM2_OEAdmix_DR | bigint |  | FK | SI | Des Ref to OEOrdAdmix |
| ITM2_OTAuthorised | varchar |  |  | SI | OT Order Authorised for Invoicing |
| ITM2_OffsetExec_DR | varchar |  | FK | SI | Offset Exec DR
Offset from this execution node
F... |
| ITM2_OffsetItem_DR | varchar |  | FK | SI | Offset Item DR
Offset from this order item
For r... |
| ITM2_OffsetType | varchar |  |  | SI | Offset Type
Standard Type OrderOffsetType 
For r... |
| ITM2_OffsetUnit | varchar |  |  | SI | Offset Unit
Standard Type DurationPlus 
For rela... |
| ITM2_OffsetValue | double |  |  | SI | Offset Value 
For relative time offsets |
| ITM2_OpBundleMainOEORI_DR | varchar |  | FK | SI | Operation Bundle main item, Des Ref OEOrdItem |
| ITM2_OrdSetDateItem_DR | varchar |  | FK | SI | Order Set Date Item DR |
| ITM2_OrderVersion | varchar |  |  | SI | Order Version |
| ITM2_OrderedWithSingleNodeOn | varchar |  |  | SI | Ordered with Single Node On |
| ITM2_OrigHospitalOEORI_DR | varchar |  | FK | SI | Des Ref OEOrdItem - Original Hospital Order |
| ITM2_OrigQtyOrderedInBaseUOM | double |  |  | SI | Original Qty Ordered in Base UOM  |
| ITM2_OverUnit | varchar |  |  | SI | OverUnit |
| ITM2_OverValue | double |  |  | SI | OverValue |
| ITM2_OverrideIVUnit_DR | bigint |  | FK | SI | Des Ref CTUOM |
| ITM2_OverrideOrderLineName | varchar |  |  | SI |  Override Orderline Name free text |
| ITM2_OverrideQtyBaseUOM | double |  |  | SI | OverrideQtyBaseUOM |
| ITM2_PAAdverseEvent_DR | varchar |  | FK | SI | Des Ref PAAdverseEvent |
| ITM2_PBSAuthorityApprovalCode | varchar |  |  | SI | PBS Authority Approval Code |
| ITM2_PBSAuthorityApprovalPending | varchar |  |  | SI | PBS Authority Approval Pending |
| ITM2_PBSAuthorityNumber | varchar |  |  | SI | PBS Authority Number |
| ITM2_PBSNonPBSFlag | varchar |  |  | SI | Non PBS/RPBS |
| ITM2_PBSPrescribingRuleBenefit_DR | varchar |  | FK | SI | Des Ref to PHCPBSPrescribingRuleRule |
| ITM2_PBSQuantity | double |  |  | SI | PBS Quantity |
| ITM2_PBSRepeats | double |  |  | SI | PBS Repeats |
| ITM2_PBSRestriction_DR | bigint |  | FK | SI | Des Ref to PHCPBSRestriction |
| ITM2_PBSStreamlineNumber | varchar |  |  | SI | PBS Streamline Number |
| ITM2_PCABolusDose | double |  |  | SI | PCABolusDose  |
| ITM2_PCADoseInterval | double |  |  | SI | PCADoseInterval  |
| ITM2_PCADoseUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| ITM2_PCALoadingDose | double |  |  | SI | PCALoadingDose  |
| ITM2_PCAMaxDoseHours | double |  |  | SI | PCAMaxDoseHours  |
| ITM2_PCAMaximumDose | double |  |  | SI | PCAMaximumDose  |
| ITM2_PHCIVAdminSet_DR | bigint |  | FK | SI | Des Ref PHCIVAdminSet |
| ITM2_PRNFlag | varchar |  |  | SI | PRN Flag |
| ITM2_PROSCatalogNo | varchar |  |  | SI |  Prosthetic Item Catalogue Number free text |
| ITM2_PROSDesc | varchar |  |  | SI |  Prosthetic Item Description free text |
| ITM2_PROSPartNo | varchar |  |  | SI |  Prosthetic Item Part Number free text |
| ITM2_PROSRebateCode | varchar |  |  | SI | Prosthetic Item Rebate Code free text |
| ITM2_PROSUsed | varchar |  |  | SI | Operation Procedure Preferences Preordered |
| ITM2_PatchApplyAt | time |  |  | SI | Time field to specify the start time for patch app... |
| ITM2_PatchDurUnit | varchar |  |  | SI | Transdermal patch application duration unit |
| ITM2_PatchDuration | varchar |  |  | SI | Transdermal Patch Duration Option |
| ITM2_PatchRemoveAfter | integer |  |  | SI | Transdermal patch application duration |
| ITM2_PatchRemoveAt | time |  |  | SI | Time field to specify when the patch to be removed |
| ITM2_PathwayItem_DR | varchar |  | FK | SI | Des Ref to PAPathwayItem, pathway item |
| ITM2_PatientHeight | double |  |  | SI | Patient Height at time of order |
| ITM2_PatientWeight | double |  |  | SI | PatientWeight |
| ITM2_PayorApprStatus | varchar |  |  | SI | Payor Approval Status |
| ITM2_PerIVGuideline | varchar |  |  | SI | Per IV Guideline |
| ITM2_PharmRevwNotes | varchar |  |  | SI | Pharmacy Review Comments |
| ITM2_PharmRevwStatus_DR | bigint |  | FK | SI | Des Ref PharmReviewStatus |
| ITM2_PrescribedAs_DR | varchar |  | FK | SI | Des Ref ARCItmMast  |
| ITM2_ProcActivity_DR | bigint |  | FK | SI | Des Ref ProcActivity |
| ITM2_ProcPhase_DR | bigint |  | FK | SI | Des Ref ProcPhase |
| ITM2_ProgBolusDose | double |  |  | SI | Automated Bolus Dose |
| ITM2_ProgBolusDoseUOM_DR | bigint |  | FK | SI | Automated Bolus Dose UOM |
| ITM2_ProgBolusFrequency | integer |  |  | SI | Automated Bolus Frequency Value  |
| ITM2_ProgBolusFrequencyUnit | varchar |  |  | SI | Automated Bolus Frequency |
| ITM2_ProsthetImplant | varchar |  |  | SI |  Prosthetic Item Implant free text |
| ITM2_ProsthetImplant_DR | bigint |  | FK | SI |  Prosthetic Item Implant des ref |
| ITM2_ProsthetSource | varchar |  |  | SI |  Prosthetic Item Source free text |
| ITM2_ProsthetSource_DR | bigint |  | FK | SI |  Prosthetic Item Source des ref |
| ITM2_ReasPharmRevwNotApproved_DR | bigint |  | FK | SI | Des Ref PHCReasonPharmRevwNotApproved  |
| ITM2_ReasonBrandSubs_DR | bigint |  | FK | SI | Des Ref PHCReasonBrandSubs |
| ITM2_ReasonFail | varchar |  |  | SI | Check Fail Reason |
| ITM2_ReasonForExclOrdItem_DR | bigint |  | FK | SI | Des Ref OECReasonForExclOrdItem |
| ITM2_ReasonForModific_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_ReasonForVariance | varchar |  |  | SI | Reason for variance  |
| ITM2_ReasonLMPUnknown_DR | bigint |  | FK | SI | Reason for Unknown LMP |
| ITM2_RecalcDoseBeforeAdmin | varchar |  |  | SI | Recalculate Dose Before Administration |
| ITM2_RecollectionDetails2_DR | bigint |  | FK | SI | Des Ref OERecollectionDetails |
| ITM2_RecollectionDetails_DR | bigint |  | FK | SI | Des Ref OERecollectionDetails |
| ITM2_Recommendations | varchar |  |  | SI | Recommendations |
| ITM2_RegAnestheticsProg | varchar |  |  | SI | Regional Anesthetics Program |
| ITM2_RenderingDate | date |  |  | SI | Rendering Date |
| ITM2_RenderingDateOverride | date |  |  | SI | Rendering Date Override |
| ITM2_RenderingTime | time |  |  | SI | Rendering Time |
| ITM2_RenderingTimeOverride | time |  |  | SI | Rendering Time Override |
| ITM2_RequestedDate | date |  |  | SI | RequestedDate |
| ITM2_RequestedTime | time |  |  | SI | RequestedTime |
| ITM2_Resource_DR | bigint |  | FK | SI | Des Ref RBResource |
| ITM2_RestrictOverrideCde | varchar |  |  | SI | RestrictiveOverrideCde |
| ITM2_ResultCatGroupCat_DR | varchar |  | FK | SI | Des Ref OECResultCatGroupCat                 |
| ITM2_RevenueGLAccount_DR | bigint |  | FK | SI | Revenue GL Account, Des Ref GLCAcct |
| ITM2_ReviewStatus_DR | bigint |  | FK | SI | Des Ref ReviewStatus |
| ITM2_RowId | varchar |  |  | NO | - |
| ITM2_Rule3ExemptInd | varchar |  |  | SI | Rule3ExemptInd |
| ITM2_S4B3ExemptInd | varchar |  |  | SI | S4B3ExemptInd |
| ITM2_SameServMultTimesSameDay | varchar |  |  | SI | Same Service provided multiple times on same day |
| ITM2_SelfDeemedCode | varchar |  |  | SI | Self Deemed Code |
| ITM2_SeqPlanStartDate | date |  |  | SI | Sequence Planned Start Date |
| ITM2_SeqPlanStartTime | time |  |  | SI | Sequence Planned Start Time |
| ITM2_SerumCreatinine | varchar |  |  | SI | Serum Creatinine At Time Of Order As A list: Value... |
| ITM2_ServPartNormAftercare | varchar |  |  | SI | Service Part of Normal Aftercare |
| ITM2_ServiceText | varchar |  |  | SI | Service Text |
| ITM2_SetOverDueToBeAdmin | varchar |  |  | SI | SetOverDueToBeAdmin |
| ITM2_SplitLabelQty | varchar |  |  | SI | Split Label Quantity |
| ITM2_StreamlineIndication_DR | bigint |  | FK | SI | Des Ref PHCStreamlineIndication |
| ITM2_SubsComments | varchar |  |  | SI | Substition Comments |
| ITM2_SubsDate | date |  |  | SI | SubsDate |
| ITM2_SubsTime | time |  |  | SI | SubsTime |
| ITM2_SubsType | varchar |  |  | SI | substitution type |
| ITM2_SubsUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| ITM2_TargetSPO2_DR | bigint |  | FK | SI | Target SP O2 |
| ITM2_TeleConsult | varchar |  |  | SI | Tele-consultation  |
| ITM2_TempMedicareNumber | varchar |  |  | SI | Temporary Medicare Number |
| ITM2_TimeCriticalWindow | double |  |  | SI | Time Critical Window |
| ITM2_TimeMoreStockReq | time |  |  | SI | Time More Stock Requested |
| ITM2_TimePORAuthorised | time |  |  | SI | TimePORAuthorised |
| ITM2_ToBillDate | date |  |  | SI | ToBillDate |
| ITM2_TotalVolInfused | double |  |  | SI | Total Volume Infused since since single node order... |
| ITM2_TreatmentLocCde | varchar |  |  | SI | Treatment Location Code |
| ITM2_Use | varchar |  |  | SI | Use |
| ITM2_VarReasonDoseDurat_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_VarReasonDose_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_VarReasonDurat_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_VarReasonFreq_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_VarReasonRateDose_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_VarReasonRateDurat_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| ITM2_WithoutAdminStat | varchar |  |  | SI | WithoutAdminStat |
| ITM2_YesNo5 | varchar |  |  | SI | YesNo5 |
| ITM2_YesNo6 | varchar |  |  | SI | YesNo6 |
| ITM2_YesNo7 | varchar |  |  | SI | YesNo7 |
| ITM2_YesNo8 | varchar |  |  | SI | YesNo8 |
| ITM2_YesNo9 | varchar |  |  | SI | YesNo9 |
| Q58Q1 | - |  |  | SI | Muscle |
| Q58Q2 | - |  |  | SI | Right |
| Q58Q3 | - |  |  | SI | Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*