# epr_OEOrder.PrefItem

**Schema:** epr_OEOrder
**Columnas:** 430
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| OffsetExecDR | varchar |  | FK | SI | Offset Exec DR
Offset from this execution node |
| OffsetItemDR | bigint |  | FK | SI | Offset Item DR
Offset from this order item |
| OffsetType | varchar |  |  | SI | Offset Type
Standard Type OrderOffsetType  |
| OffsetUnit | varchar |  |  | SI | Offset Unit |
| OffsetValue | double |  |  | SI | Offset Value  |
| PREFARCIMDR | varchar |  | FK | NO | Order Item CT reference
Preference applies to thi... |
| PREFARCOSDR | varchar |  | FK | SI | Order Set CT reference
Restrict applies to this o... |
| PREFDesc | varchar |  |  | SI | Overriding description to be displayed in Order Fa... |
| PREFDescAsOrderLine | bit |  |  | SI | Display Order Favourite as Order Line Text
Overri... |
| PREFDoseModelDoseChange | bit |  |  | SI | PREFDoseModelDoseChange |
| PREFDoseModelFrequencyChange | bit |  |  | SI | PREFDoseModelFrequencyChange |
| PREFDosingModelChangeType | varchar |  |  | SI | PREFDosingModelChangeType |
| PREFFormName | varchar |  |  | SI | The Name of the Order Detail component |
| PREFParams_AccessionNumber | varchar |  |  | SI | - |
| PREFParams_ActivityModifierList | varchar |  |  | SI | - |
| PREFParams_AdmAfterSkinTest | varchar |  |  | SI | - |
| PREFParams_AdministrativeOrder | bit |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMAddedAdditiveFlg | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMAdmixType | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMAllowToModify | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMFinalFormDR | bigint |  | FK | SI | - |
| PREFParams_AdmixParamsDR_AMMainItem | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMMaxFlowRate | double |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMMinFlowRate | double |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMOrderedBagVolume | double |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMPCALoadingVolume | double |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMPCALoadingVolumeUOMDR | bigint |  | FK | SI | - |
| PREFParams_AdmixParamsDR_AMQuantity | double |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMResolvedSolvDR | varchar |  | FK | SI | - |
| PREFParams_AdmixParamsDR_AMSolventDR | varchar |  | FK | SI | - |
| PREFParams_AdmixParamsDR_AMSubtractAdditive | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMTotalFlowRate | double |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMTotalFlowRatePerUOM | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_AMTotalFlowRateUOMDR | bigint |  | FK | SI | - |
| PREFParams_AdmixParamsDR_AMUOMDR | bigint |  | FK | SI | - |
| PREFParams_AdmixParamsDR_AMWithoutSolvent | varchar |  |  | SI | - |
| PREFParams_AdmixParamsDR_Additives | varchar |  |  | SI | - |
| PREFParams_AlertReason | varchar |  |  | SI | - |
| PREFParams_Altpatloc | varchar |  |  | SI | - |
| PREFParams_ApptID | varchar |  |  | SI | - |
| PREFParams_AuthDoctor | varchar |  |  | SI | - |
| PREFParams_BillPrice | varchar |  |  | SI | - |
| PREFParams_BodySite | varchar |  |  | SI | - |
| PREFParams_BookingOrder | bit |  |  | SI | - |
| PREFParams_CONSDesc | varchar |  |  | SI | - |
| PREFParams_COPYID | varchar |  |  | SI | - |
| PREFParams_CTLOCDesc | varchar |  |  | SI | - |
| PREFParams_CTPCPDesc | varchar |  |  | SI | - |
| PREFParams_CTPCPID | varchar |  |  | SI | - |
| PREFParams_CTUOMDesc | varchar |  |  | SI | - |
| PREFParams_CalcQtyFlag2 | varchar |  |  | SI | - |
| PREFParams_Carbohydrate | varchar |  |  | SI | - |
| PREFParams_CarePlanIssueID | varchar |  |  | SI | - |
| PREFParams_CareProvCodeList | varchar |  |  | SI | - |
| PREFParams_CareProvList | varchar |  |  | SI | - |
| PREFParams_ClinCondDR | varchar |  | FK | SI | - |
| PREFParams_ColDate | varchar |  |  | SI | - |
| PREFParams_ColTime | varchar |  |  | SI | - |
| PREFParams_ContactCareProv | varchar |  |  | SI | - |
| PREFParams_CoveredByMainInsur | varchar |  |  | SI | - |
| PREFParams_CreateDate | date |  |  | SI | - |
| PREFParams_CreateTime | time |  |  | SI | - |
| PREFParams_DBLaboratoryCode | varchar |  |  | SI | - |
| PREFParams_DayCycle | varchar |  |  | SI | - |
| PREFParams_DefRptDur | varchar |  |  | SI | - |
| PREFParams_DefRptLoc | varchar |  |  | SI | - |
| PREFParams_DelayMeal | varchar |  |  | SI | - |
| PREFParams_DeptDesc | varchar |  |  | SI | - |
| PREFParams_DoNotDisp | varchar |  |  | SI | - |
| PREFParams_Doctor | varchar |  |  | SI | - |
| PREFParams_DrugDelRate | varchar |  |  | SI | - |
| PREFParams_DrugDelUnit | varchar |  |  | SI | - |
| PREFParams_EligibilityStatus | varchar |  |  | SI | - |
| PREFParams_EndDate | varchar |  |  | SI | - |
| PREFParams_Energy | varchar |  |  | SI | - |
| PREFParams_EnteredUOM | varchar |  |  | SI | - |
| PREFParams_EpisodeID | bigint |  |  | SI | - |
| PREFParams_Fat | varchar |  |  | SI | - |
| PREFParams_FeedString | varchar |  |  | SI | - |
| PREFParams_FlowQty | varchar |  |  | SI | - |
| PREFParams_FlowRateUnit | varchar |  |  | SI | - |
| PREFParams_FlowTime | varchar |  |  | SI | - |
| PREFParams_ForceGenEXE | varchar |  |  | SI | - |
| PREFParams_FreeText | varchar |  |  | SI | - |
| PREFParams_HL7Flag | varchar |  |  | SI | - |
| PREFParams_HidAuthPrescDetail | varchar |  |  | SI | - |
| PREFParams_HotReport | varchar |  |  | SI | - |
| PREFParams_ITM2AcceptDisabilityInd | varchar |  |  | SI | - |
| PREFParams_ITM2AcceptDisabilityText | varchar |  |  | SI | - |
| PREFParams_ITM2AltBodyWeightObsDR | varchar |  | FK | SI | - |
| PREFParams_ITM2AntimicrobialApprovalNo | varchar |  |  | SI | - |
| PREFParams_ITM2ApprovalAdminReq | varchar |  |  | SI | - |
| PREFParams_ITM2BPGDoseBased | varchar |  |  | SI | - |
| PREFParams_ITM2BPGUOMDR | varchar |  | FK | SI | - |
| PREFParams_ITM2BPQuantity | varchar |  |  | SI | - |
| PREFParams_ITM2BPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| PREFParams_ITM2BPRequiredByDate | varchar |  |  | SI | - |
| PREFParams_ITM2BPRequiredByTime | varchar |  |  | SI | - |
| PREFParams_ITM2BPReservationPeriod | varchar |  |  | SI | - |
| PREFParams_ITM2BPReservationPeriodUnit | varchar |  |  | SI | - |
| PREFParams_ITM2CNMItemNotes | varchar |  |  | SI | - |
| PREFParams_ITM2CNMNo | varchar |  |  | SI | - |
| PREFParams_ITM2CNMOverrideReason | varchar |  |  | SI | - |
| PREFParams_ITM2CNMStatusDR | varchar |  | FK | SI | - |
| PREFParams_ITM2CalDoseHTMLPlainText | varchar |  |  | SI | - |
| PREFParams_ITM2CalDoseHTMLRichText | varchar |  |  | SI | - |
| PREFParams_ITM2CalTemplateDR | varchar |  | FK | SI | - |
| PREFParams_ITM2CalTemplateParamsDR_DCTCTUOMDR | bigint |  | FK | SI | - |
| PREFParams_ITM2CalTemplateParamsDR_DCTDurationUnit | varchar |  |  | SI | - |
| PREFParams_ITM2CalTemplateParamsDR_Details | varchar |  |  | SI | - |
| PREFParams_ITM2CalcDoseDetail | varchar |  |  | SI | - |
| PREFParams_ITM2CalcIVDose | varchar |  |  | SI | - |
| PREFParams_ITM2Confidential | varchar |  |  | SI | - |
| PREFParams_ITM2CopyCycleOrder | varchar |  |  | SI | - |
| PREFParams_ITM2Derived | varchar |  |  | SI | - |
| PREFParams_ITM2DispenseType | varchar |  |  | SI | - |
| PREFParams_ITM2DistanceKms | varchar |  |  | SI | - |
| PREFParams_ITM2DoNotSubstitute | varchar |  |  | SI | - |
| PREFParams_ITM2DoseCalLinkedNONTCLELabs | varchar |  |  | SI | - |
| PREFParams_ITM2DoseCalLinkedObs | varchar |  |  | SI | - |
| PREFParams_ITM2DoseCalLinkedTCLELabs | varchar |  |  | SI | - |
| PREFParams_ITM2DoseCalProtocolBase | double |  |  | SI | - |
| PREFParams_ITM2DoseCalRangeDesc | varchar |  |  | SI | - |
| PREFParams_ITM2DoseCalRangeFrom | double |  |  | SI | - |
| PREFParams_ITM2DoseCalRangeTo | double |  |  | SI | - |
| PREFParams_ITM2DoseCalRangeUnit | varchar |  |  | SI | - |
| PREFParams_ITM2DoseInML | varchar |  |  | SI | - |
| PREFParams_ITM2DoseRecalPermitted | bit |  |  | SI | - |
| PREFParams_ITM2DropsMin | varchar |  |  | SI | - |
| PREFParams_ITM2DuplServOverrideReason | varchar |  |  | SI | - |
| PREFParams_ITM2DurationType | varchar |  |  | SI | - |
| PREFParams_ITM2DurationUnit | varchar |  |  | SI | - |
| PREFParams_ITM2DurationValue | varchar |  |  | SI | - |
| PREFParams_ITM2EPrescItemNotes | varchar |  |  | SI | - |
| PREFParams_ITM2EPrescNo | varchar |  |  | SI | - |
| PREFParams_ITM2EPrescOverrideReason | varchar |  |  | SI | - |
| PREFParams_ITM2EPrescStatus | varchar |  |  | SI | - |
| PREFParams_ITM2EquipmentId | varchar |  |  | SI | - |
| PREFParams_ITM2Event | varchar |  |  | SI | - |
| PREFParams_ITM2ExpiryDate | date |  |  | SI | - |
| PREFParams_ITM2ExternalDocFiscalCode | varchar |  |  | SI | - |
| PREFParams_ITM2ExternalPaperPrescNo | varchar |  |  | SI | - |
| PREFParams_ITM2ExternalPrescriptionID | varchar |  |  | SI | - |
| PREFParams_ITM2FieldQuantity | varchar |  |  | SI | - |
| PREFParams_ITM2FluidConsistModDR | varchar |  | FK | SI | - |
| PREFParams_ITM2FluidVolumeRestrDR | varchar |  | FK | SI | - |
| PREFParams_ITM2FoodTextureModDR | varchar |  | FK | SI | - |
| PREFParams_ITM2FreeTextFreqUnit | varchar |  |  | SI | - |
| PREFParams_ITM2FreeTextFreqValue | varchar |  |  | SI | - |
| PREFParams_ITM2IVContTotalDose | varchar |  |  | SI | - |
| PREFParams_ITM2IVContTotalDoseUnitDR | varchar |  | FK | SI | - |
| PREFParams_ITM2IVDose | varchar |  |  | SI | - |
| PREFParams_ITM2IVUnitDR | varchar |  | FK | SI | - |
| PREFParams_ITM2InHospService | varchar |  |  | SI | - |
| PREFParams_ITM2Indication | varchar |  |  | SI | - |
| PREFParams_ITM2InfusTypeEndDate | varchar |  |  | SI | - |
| PREFParams_ITM2InfusTypeEndTime | varchar |  |  | SI | - |
| PREFParams_ITM2LSPNum | varchar |  |  | SI | - |
| PREFParams_ITM2LateralityDR | varchar |  | FK | SI | - |
| PREFParams_ITM2Link | varchar |  |  | SI | - |
| PREFParams_ITM2LoanRetDate | date |  |  | SI | - |
| PREFParams_ITM2LostLoanItem | varchar |  |  | SI | - |
| PREFParams_ITM2MRMedLinkedOrder | varchar |  |  | SI | - |
| PREFParams_ITM2MaxDeliveryRate | double |  |  | SI | - |
| PREFParams_ITM2MedicationDR | varchar |  | FK | SI | - |
| PREFParams_ITM2MinDeliveryRate | double |  |  | SI | - |
| PREFParams_ITM2MinDoseQty | varchar |  |  | SI | - |
| PREFParams_ITM2MinPhQtyOrd | varchar |  |  | SI | - |
| PREFParams_ITM2MultPrSamePatSameDocSameDay | varchar |  |  | SI | - |
| PREFParams_ITM2MultProcNotes | varchar |  |  | SI | - |
| PREFParams_ITM2NFMICategDepart | varchar |  |  | SI | - |
| PREFParams_ITM2NewPRNMaxDose24hrs | varchar |  |  | SI | - |
| PREFParams_ITM2NewPRNMaxDose24hrsUnitDR | varchar |  | FK | SI | - |
| PREFParams_ITM2NonPBSQuanUOMDR | varchar |  | FK | SI | - |
| PREFParams_ITM2NonPBSQuantity | double |  |  | SI | - |
| PREFParams_ITM2O2AdminOver | double |  |  | SI | - |
| PREFParams_ITM2O2AdminOverUnit | varchar |  |  | SI | - |
| PREFParams_ITM2O2ContDelivery | varchar |  |  | SI | - |
| PREFParams_ITM2O2DeliveryMethodDR | varchar |  | FK | SI | - |
| PREFParams_ITM2O2MaxRate | double |  |  | SI | - |
| PREFParams_ITM2O2Rate | double |  |  | SI | - |
| PREFParams_ITM2O2RateCalMethod | varchar |  |  | SI | - |
| PREFParams_ITM2O2RateUOMDR | varchar |  | FK | SI | - |
| PREFParams_ITM2OrderVersion | varchar |  |  | SI | - |
| PREFParams_ITM2OverUnit | varchar |  |  | SI | - |
| PREFParams_ITM2OverValue | varchar |  |  | SI | - |
| PREFParams_ITM2OverrideIVUnitDR | varchar |  | FK | SI | - |
| PREFParams_ITM2OverrideQtyBaseUOM | varchar |  |  | SI | - |
| PREFParams_ITM2PBSAuthorityApprovalCode | varchar |  |  | SI | - |
| PREFParams_ITM2PBSAuthorityApprovalPending | varchar |  |  | SI | - |
| PREFParams_ITM2PBSAuthorityNumber | varchar |  |  | SI | - |
| PREFParams_ITM2PBSNonPBSFlag | varchar |  |  | SI | - |
| PREFParams_ITM2PBSPrescribingRuleBenefitDR | varchar |  | FK | SI | - |
| PREFParams_ITM2PBSQuantity | double |  |  | SI | - |
| PREFParams_ITM2PBSRepeats | double |  |  | SI | - |
| PREFParams_ITM2PBSRestrictionDR | varchar |  | FK | SI | - |
| PREFParams_ITM2PBSStreamlineNumber | varchar |  |  | SI | - |
| PREFParams_ITM2PCABolusDose | varchar |  |  | SI | - |
| PREFParams_ITM2PCADoseInterval | varchar |  |  | SI | - |
| PREFParams_ITM2PCADoseUOMDR | varchar |  | FK | SI | - |
| PREFParams_ITM2PCALoadingDose | varchar |  |  | SI | - |
| PREFParams_ITM2PCAMaxDoseHours | varchar |  |  | SI | - |
| PREFParams_ITM2PCAMaximumDose | varchar |  |  | SI | - |
| PREFParams_ITM2PHCIVAdminSetDR | varchar |  | FK | SI | - |
| PREFParams_ITM2PRNFlag | varchar |  |  | SI | - |
| PREFParams_ITM2PRNMaxDoseHrs | double |  |  | SI | - |
| PREFParams_ITM2PRNMaxDoseNumHrs | varchar |  |  | SI | - |
| PREFParams_ITM2PatchApplyAt | varchar |  |  | SI | - |
| PREFParams_ITM2PatchDurUnit | varchar |  |  | SI | - |
| PREFParams_ITM2PatchDuration | varchar |  |  | SI | - |
| PREFParams_ITM2PatchRemoveAfter | integer |  |  | SI | - |
| PREFParams_ITM2PatchRemoveAt | varchar |  |  | SI | - |
| PREFParams_ITM2PathwayItemDR | varchar |  | FK | SI | - |
| PREFParams_ITM2PatientHeight | double |  |  | SI | - |
| PREFParams_ITM2PatientWeight | varchar |  |  | SI | - |
| PREFParams_ITM2PerIVGuideline | varchar |  |  | SI | - |
| PREFParams_ITM2ProcActivityDR | varchar |  | FK | SI | - |
| PREFParams_ITM2ProcPhaseDR | varchar |  | FK | SI | - |
| PREFParams_ITM2ProgBolusDose | double |  |  | SI | - |
| PREFParams_ITM2ProgBolusDoseUOMDR | varchar |  | FK | SI | - |
| PREFParams_ITM2ProgBolusFrequency | integer |  |  | SI | - |
| PREFParams_ITM2ProgBolusFrequencyUnit | varchar |  |  | SI | - |
| PREFParams_ITM2ReasonForModificDR | varchar |  | FK | SI | - |
| PREFParams_ITM2ReasonForVariance | varchar |  |  | SI | - |
| PREFParams_ITM2RecalcDoseBeforeAdmin | varchar |  |  | SI | - |
| PREFParams_ITM2RegAnestheticsProg | varchar |  |  | SI | - |
| PREFParams_ITM2RestrictOverrideCde | varchar |  |  | SI | - |
| PREFParams_ITM2Rule3ExemptInd | varchar |  |  | SI | - |
| PREFParams_ITM2S4B3ExemptInd | varchar |  |  | SI | - |
| PREFParams_ITM2SameServMultTimesSameDay | varchar |  |  | SI | - |
| PREFParams_ITM2SelfDeemedCode | varchar |  |  | SI | - |
| PREFParams_ITM2ServPartNormAftercare | varchar |  |  | SI | - |
| PREFParams_ITM2ServiceText | varchar |  |  | SI | - |
| PREFParams_ITM2TargetSPO2DR | varchar |  | FK | SI | - |
| PREFParams_ITM2TeleConsult | varchar |  |  | SI | - |
| PREFParams_ITM2TempMedicareNumber | varchar |  |  | SI | - |
| PREFParams_ITM2TimeCriticalWindow | double |  |  | SI | - |
| PREFParams_ITM2TreatmentLocCde | varchar |  |  | SI | - |
| PREFParams_ITM2VarReasonDoseDR | varchar |  | FK | SI | - |
| PREFParams_ITM2VarReasonDoseDuratDR | varchar |  | FK | SI | - |
| PREFParams_ITM2VarReasonDuratDR | varchar |  | FK | SI | - |
| PREFParams_ITM2VarReasonFreqDR | varchar |  | FK | SI | - |
| PREFParams_ITM2VarReasonRateDoseDR | varchar |  | FK | SI | - |
| PREFParams_ITM2VarReasonRateDuratDR | varchar |  | FK | SI | - |
| PREFParams_IVCalcMeth | varchar |  |  | SI | - |
| PREFParams_IVType | varchar |  |  | SI | - |
| PREFParams_IVUnit | varchar |  |  | SI | - |
| PREFParams_IncompReas | varchar |  |  | SI | - |
| PREFParams_IndicateTransfusion | varchar |  |  | SI | - |
| PREFParams_Interval | varchar |  |  | SI | - |
| PREFParams_LBTSBPNumberOfUnits | varchar |  |  | SI | - |
| PREFParams_LBTSBPQuantity | varchar |  |  | SI | - |
| PREFParams_LBTSBPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| PREFParams_LBTSBPReservationPeriod | varchar |  |  | SI | - |
| PREFParams_LBTSBPReservationPeriodUnit | varchar |  |  | SI | - |
| PREFParams_LBTSConfidential | varchar |  |  | SI | - |
| PREFParams_LabSpecSites | varchar |  |  | SI | - |
| PREFParams_LabVolume | varchar |  |  | SI | - |
| PREFParams_LabelText | varchar |  |  | SI | - |
| PREFParams_Linked | varchar |  |  | SI | - |
| PREFParams_LinkedItmID | varchar |  |  | SI | - |
| PREFParams_MSOEOrdItemID | varchar |  |  | SI | - |
| PREFParams_MealType | varchar |  |  | SI | - |
| PREFParams_MeteredDose | varchar |  |  | SI | - |
| PREFParams_Modifiers | varchar |  |  | SI | - |
| PREFParams_NeedleGauge | varchar |  |  | SI | - |
| PREFParams_NeedleType | varchar |  |  | SI | - |
| PREFParams_NewOrdItemID | varchar |  |  | SI | - |
| PREFParams_NextDoseDate | varchar |  |  | SI | - |
| PREFParams_NextDoseTime | varchar |  |  | SI | - |
| PREFParams_NotifyClinician | varchar |  |  | SI | - |
| PREFParams_NotifyMod | varchar |  |  | SI | - |
| PREFParams_OECPRDesc | varchar |  |  | SI | - |
| PREFParams_OEORIActivity | varchar |  |  | SI | - |
| PREFParams_OEORIAnnotateDR | bigint |  | FK | SI | - |
| PREFParams_OEORIApprovalDate | varchar |  |  | SI | - |
| PREFParams_OEORIApprovalInd | varchar |  |  | SI | - |
| PREFParams_OEORIApprovalNo | varchar |  |  | SI | - |
| PREFParams_OEORIApprovalTime | varchar |  |  | SI | - |
| PREFParams_OEORIApprovedBy | varchar |  |  | SI | - |
| PREFParams_OEORIAutologousBloodReq | varchar |  |  | SI | - |
| PREFParams_OEORIBBTAG1 | varchar |  |  | SI | - |
| PREFParams_OEORIBBTAG2 | varchar |  |  | SI | - |
| PREFParams_OEORIBBTAG3 | varchar |  |  | SI | - |
| PREFParams_OEORIBBTAG4 | varchar |  |  | SI | - |
| PREFParams_OEORIBBTAG5 | varchar |  |  | SI | - |
| PREFParams_OEORIBillDesc | varchar |  |  | SI | - |
| PREFParams_OEORICompXMatchReq | varchar |  |  | SI | - |
| PREFParams_OEORIConsult | varchar |  |  | SI | - |
| PREFParams_OEORIContOrderAfterDischarge | varchar |  |  | SI | - |
| PREFParams_OEORICurrRepeatNumber | varchar |  |  | SI | - |
| PREFParams_OEORIDSReportFlag | varchar |  |  | SI | - |
| PREFParams_OEORIDepProcNotes | varchar |  |  | SI | - |
| PREFParams_OEORIDoseQty | varchar |  |  | SI | - |
| PREFParams_OEORIEndDate | varchar |  |  | SI | - |
| PREFParams_OEORIEndTime | varchar |  |  | SI | - |
| PREFParams_OEORIFreqDelay | varchar |  |  | SI | - |
| PREFParams_OEORIInsBillConditDR | varchar |  | FK | SI | - |
| PREFParams_OEORIItemGroup | varchar |  |  | SI | - |
| PREFParams_OEORIItmMastDR | varchar |  | FK | SI | - |
| PREFParams_OEORILab1 | varchar |  |  | SI | - |
| PREFParams_OEORILab2 | varchar |  |  | SI | - |
| PREFParams_OEORILabEpisodeNo | varchar |  |  | SI | - |
| PREFParams_OEORIMaxNumberOfRepeats | varchar |  |  | SI | - |
| PREFParams_OEORIMaxRepeats | varchar |  |  | SI | - |
| PREFParams_OEORIPatConsentObtained | varchar |  |  | SI | - |
| PREFParams_OEORIPrescRepExpiryDate | varchar |  |  | SI | - |
| PREFParams_OEORIPrescRepNumberDays | varchar |  |  | SI | - |
| PREFParams_OEORIPrice | varchar |  |  | SI | - |
| PREFParams_OEORIQty | varchar |  |  | SI | - |
| PREFParams_OEORIQtyPackUOM | varchar |  |  | SI | - |
| PREFParams_OEORIRBResourceDR | varchar |  | FK | SI | - |
| PREFParams_OEORIReasOrdCMVNegBlood | varchar |  |  | SI | - |
| PREFParams_OEORIRefDocDR | varchar |  | FK | SI | - |
| PREFParams_OEORIRemarks | varchar |  |  | SI | - |
| PREFParams_OEORIResultDSReportFlag | varchar |  |  | SI | - |
| PREFParams_OEORIRoute | varchar |  |  | SI | - |
| PREFParams_OEORISpecialty | varchar |  |  | SI | - |
| PREFParams_OEORISttDat | varchar |  |  | SI | - |
| PREFParams_OEORISttTim | varchar |  |  | SI | - |
| PREFParams_OEORIText1 | varchar |  |  | SI | - |
| PREFParams_OEORIText2 | varchar |  |  | SI | - |
| PREFParams_OEORIText3 | varchar |  |  | SI | - |
| PREFParams_OEORIText4 | varchar |  |  | SI | - |
| PREFParams_OEORIUserGroupAdd | bigint |  |  | SI | - |
| PREFParams_OEORIVarianceReasonDR | varchar |  | FK | SI | - |
| PREFParams_OEORIView | varchar |  |  | SI | - |
| PREFParams_OEORIWhoGoWhere | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo1 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo2 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo3 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo4 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo5 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo6 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo7 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo8 | varchar |  |  | SI | - |
| PREFParams_OEORIYesNo9 | varchar |  |  | SI | - |
| PREFParams_OERemoteDutyID | bigint |  |  | SI | - |
| PREFParams_ORDERSETID | varchar |  |  | SI | - |
| PREFParams_ORNCDesc | varchar |  |  | SI | - |
| PREFParams_OSTATDesc | varchar |  |  | SI | - |
| PREFParams_OperationID | varchar |  |  | SI | - |
| PREFParams_OrdSetDateID | varchar |  |  | SI | - |
| PREFParams_OrderID | varchar |  |  | SI | - |
| PREFParams_OverseerUser | bigint |  |  | SI | - |
| PREFParams_PHCDUDesc1 | varchar |  |  | SI | - |
| PREFParams_PHCFRDesc1 | varchar |  |  | SI | - |
| PREFParams_PHCINDesc1 | varchar |  |  | SI | - |
| PREFParams_PRNIndication | varchar |  |  | SI | - |
| PREFParams_PRNMaxDose24hr | varchar |  |  | SI | - |
| PREFParams_PRNTotNumDoseAllow | varchar |  |  | SI | - |
| PREFParams_PasteurisedFood | varchar |  |  | SI | - |
| PREFParams_PathwayId | varchar |  |  | SI | - |
| PREFParams_PatientLoc | varchar |  |  | SI | - |
| PREFParams_Payor | varchar |  |  | SI | - |
| PREFParams_PhoneOrder | varchar |  |  | SI | - |
| PREFParams_Plan | varchar |  |  | SI | - |
| PREFParams_PortableEquiptRequired | varchar |  |  | SI | - |
| PREFParams_PrefConMethod | varchar |  |  | SI | - |
| PREFParams_PreparationTime | varchar |  |  | SI | - |
| PREFParams_Protein | varchar |  |  | SI | - |
| PREFParams_REMODCareProvText | varchar |  |  | SI | - |
| PREFParams_REMODContactNoText | varchar |  |  | SI | - |
| PREFParams_REMODDMOSeenByDate | varchar |  |  | SI | - |
| PREFParams_REMODDMOSeenByTime | varchar |  |  | SI | - |
| PREFParams_REMODHospNotifDate | varchar |  |  | SI | - |
| PREFParams_REMODHospNotifTime | varchar |  |  | SI | - |
| PREFParams_REMODPlaceOfOrder | varchar |  |  | SI | - |
| PREFParams_REMODPlanCallBackBy | varchar |  |  | SI | - |
| PREFParams_REMODPlanCallBackDate | varchar |  |  | SI | - |
| PREFParams_REMODPlanCallBackTime | varchar |  |  | SI | - |
| PREFParams_REMODRecCareProv | varchar |  |  | SI | - |
| PREFParams_REMODRecCareProvText | varchar |  |  | SI | - |
| PREFParams_REMODReferPrio | varchar |  |  | SI | - |
| PREFParams_REMODRemarks | varchar |  |  | SI | - |
| PREFParams_REMODRetAcceptDate | varchar |  |  | SI | - |
| PREFParams_REMODRetAcceptTime | varchar |  |  | SI | - |
| PREFParams_REMODRetArriveDestDate | varchar |  |  | SI | - |
| PREFParams_REMODRetArriveDestTime | varchar |  |  | SI | - |
| PREFParams_REMODRetDepartBaseDate | varchar |  |  | SI | - |
| PREFParams_REMODRetDepartBaseTime | varchar |  |  | SI | - |
| PREFParams_REMODRetDepartDestDate | varchar |  |  | SI | - |
| PREFParams_REMODRetDepartDestTime | varchar |  |  | SI | - |
| PREFParams_REMODRetETABaseDate | varchar |  |  | SI | - |
| PREFParams_REMODRetETABaseTime | varchar |  |  | SI | - |
| PREFParams_REMODRetPlanDate | varchar |  |  | SI | - |
| PREFParams_REMODRetPlanTime | varchar |  |  | SI | - |
| PREFParams_REMODRetPrio | varchar |  |  | SI | - |
| PREFParams_REMODRetTransp | varchar |  |  | SI | - |
| PREFParams_REMODTransferLoc | varchar |  |  | SI | - |
| PREFParams_REMODTriaged | varchar |  |  | SI | - |
| PREFParams_REMODType | varchar |  |  | SI | - |
| PREFParams_RMDuration | varchar |  |  | SI | - |
| PREFParams_RMFrequency | varchar |  |  | SI | - |
| PREFParams_RadNo | varchar |  |  | SI | - |
| PREFParams_ReceivedDate | varchar |  |  | SI | - |
| PREFParams_ReceivedTime | varchar |  |  | SI | - |
| PREFParams_RefDoctorList | varchar |  |  | SI | - |
| PREFParams_ReqForTheat | varchar |  |  | SI | - |
| PREFParams_RequestedDate | varchar |  |  | SI | - |
| PREFParams_RequestedTime | varchar |  |  | SI | - |
| PREFParams_RiceType | varchar |  |  | SI | - |
| PREFParams_RouteAdmin | varchar |  |  | SI | - |
| PREFParams_Session | varchar |  |  | SI | - |
| PREFParams_StartEndMealType | varchar |  |  | SI | - |
| PREFParams_SteriliseUtensils | varchar |  |  | SI | - |
| PREFParams_TempStat | varchar |  |  | SI | - |
| PREFParams_TheatBookDate | varchar |  |  | SI | - |
| PREFParams_USERID | bigint |  |  | SI | - |
| PREFParams_UnitHrs | varchar |  |  | SI | - |
| PREFParams_UnitsColl | varchar |  |  | SI | - |
| PREFParams_Volume | varchar |  |  | SI | - |
| PREFParams_formAltReasonDR | varchar |  | FK | SI | - |
| PREFParams_hiddenLBEPClinicalConditions | varchar |  |  | SI | - |
| PREFParams_lstEmbedOSExcluded | varchar |  |  | SI | - |
| PREFParams_lstOSExclusions | varchar |  |  | SI | - |
| PREFParams_mDate | varchar |  |  | SI | - |
| PREFParams_mTime | varchar |  |  | SI | - |
| PREFParams_prosthetic2 | varchar |  |  | SI | - |
| PREFParams_refclincode | varchar |  |  | SI | - |
| PREFParams_teeth | varchar |  |  | SI | - |
| PREFParams_urgent | varchar |  |  | SI | - |
| PREFParams_zProsthetics | varchar |  |  | SI | - |
| PREFParams_zSpecSites | varchar |  |  | SI | - |
| PREFPrefParamsDosingDR | varchar |  | FK | SI | Default Dosing Cycle |
| PREFSequenceFlag | varchar |  |  | SI | Sequence Flag |
| PREFUpdateDate | date |  |  | SI | Last Updated Date |
| PREFUpdateTime | time |  |  | SI | Last Updated Time |
| PREFUpdateUserDR | bigint |  | FK | SI | Last Updated By User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*