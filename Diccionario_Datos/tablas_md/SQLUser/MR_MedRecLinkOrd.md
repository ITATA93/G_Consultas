# SQLUser.MR_MedRecLinkOrd

**Schema:** SQLUser
**Columnas:** 512
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRLO_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| MRLO_Childsub | double |  |  | NO | Childsub |
| MRLO_Decision | varchar |  |  | SI | Decision |
| MRLO_DoseModelDoseChange | bit |  |  | SI | DoseModel Dose Change |
| MRLO_DoseModelFrequencyChange | bit |  |  | SI | DoseModel Frequency Change |
| MRLO_DosingModelChangeType | varchar |  |  | SI | DosingModel ChangeType |
| MRLO_OEOrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| MRLO_OrderStatus_DR | bigint |  | FK | SI | Med Rec Order Status |
| MRLO_PendingOrderStatus_DR | bigint |  | FK | SI | Pending Order Status |
| MRLO_PrefParamsDosing_DR | varchar |  | FK | SI | Default Dosing Cycle |
| MRLO_PrefParams_DR_AccessionNumber | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ActivityModifierList | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmAfterSkinTest | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdministrativeOrder | bit |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMAddedAdditiveFlg | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMAdmixType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMAllowToModify | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMFinalFormDR | bigint |  | FK | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMMainItem | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMMaxFlowRate | double |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMMinFlowRate | double |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMOrderedBagVolume | double |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMPCALoadingVolume | double |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMPCALoadingVolumeUOMDR | bigint |  | FK | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMQuantity | double |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMResolvedSolvDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMSolventDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMSubtractAdditive | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMTotalFlowRate | double |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMTotalFlowRatePerUOM | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMTotalFlowRateUOMDR | bigint |  | FK | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMUOMDR | bigint |  | FK | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_AMWithoutSolvent | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AdmixParamsDR_Additives | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AlertReason | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Altpatloc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ApptID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_AuthDoctor | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_BillPrice | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_BodySite | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_BookingOrder | bit |  |  | SI | - |
| MRLO_PrefParams_DR_CONSDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_COPYID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CTLOCDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CTPCPDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CTPCPID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CTUOMDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CalcQtyFlag2 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Carbohydrate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CarePlanIssueID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CareProvCodeList | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CareProvList | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ClinCondDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ColDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ColTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ContactCareProv | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CoveredByMainInsur | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_CreateDate | date |  |  | SI | - |
| MRLO_PrefParams_DR_CreateTime | time |  |  | SI | - |
| MRLO_PrefParams_DR_DBLaboratoryCode | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DayCycle | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DefRptDur | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DefRptLoc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DelayMeal | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DeptDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DoNotDisp | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Doctor | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DrugDelRate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_DrugDelUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_EligibilityStatus | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_EndDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Energy | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_EnteredUOM | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_EpisodeID | bigint |  |  | SI | - |
| MRLO_PrefParams_DR_Fat | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_FeedString | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_FlowQty | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_FlowRateUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_FlowTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ForceGenEXE | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_FreeText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_HL7Flag | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_HidAuthPrescDetail | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_HotReport | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2AcceptDisabilityInd | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2AcceptDisabilityText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2AltBodyWeightObsDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2AntimicrobialApprovalNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ApprovalAdminReq | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPGDoseBased | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPGUOMDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2BPQuantity | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPRequiredByDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPRequiredByTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPReservationPeriod | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2BPReservationPeriodUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CNMItemNotes | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CNMNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CNMOverrideReason | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CNMStatusDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2CalDoseHTMLPlainText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CalDoseHTMLRichText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CalTemplateDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2CalTemplateParamsDR_DCTCTUOMDR | bigint |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2CalTemplateParamsDR_DCTDurationUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CalTemplateParamsDR_Details | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CalcDoseDetail | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CalcIVDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2Confidential | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2CopyCycleOrder | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2Derived | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DispenseType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DistanceKms | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoNotSubstitute | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalLinkedNONTCLELabs | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalLinkedObs | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalLinkedTCLELabs | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalProtocolBase | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalRangeDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalRangeFrom | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalRangeTo | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseCalRangeUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseInML | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DoseRecalPermitted | bit |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DropsMin | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DuplServOverrideReason | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DurationType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DurationUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2DurationValue | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2EPrescItemNotes | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2EPrescNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2EPrescOverrideReason | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2EPrescStatus | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2EquipmentId | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2Event | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ExpiryDate | date |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ExternalDocFiscalCode | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ExternalPaperPrescNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ExternalPrescriptionID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2FieldQuantity | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2FluidConsistModDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2FluidVolumeRestrDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2FoodTextureModDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2FreeTextFreqUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2FreeTextFreqValue | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2IVContTotalDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2IVContTotalDoseUnitDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2IVDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2IVUnitDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2InHospService | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2Indication | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2InfusTypeEndDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2InfusTypeEndTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2LSPNum | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2LateralityDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2Link | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2LoanRetDate | date |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2LostLoanItem | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MRMedLinkedOrder | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MaxDeliveryRate | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MedicationDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2MinDeliveryRate | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MinDoseQty | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MinPhQtyOrd | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MultPrSamePatSameDocSameDay | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2MultProcNotes | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2NFMICategDepart | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2NewPRNMaxDose24hrs | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2NewPRNMaxDose24hrsUnitDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2NonPBSQuanUOMDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2NonPBSQuantity | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2AdminOver | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2AdminOverUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2ContDelivery | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2DeliveryMethodDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2O2MaxRate | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2Rate | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2RateCalMethod | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2O2RateUOMDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2OrderVersion | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2OverUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2OverValue | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2OverrideIVUnitDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2OverrideQtyBaseUOM | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSAuthorityApprovalCode | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSAuthorityApprovalPending | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSAuthorityNumber | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSNonPBSFlag | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSPrescribingRuleBenefitDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2PBSQuantity | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSRepeats | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PBSRestrictionDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2PBSStreamlineNumber | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PCABolusDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PCADoseInterval | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PCADoseUOMDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2PCALoadingDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PCAMaxDoseHours | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PCAMaximumDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PHCIVAdminSetDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2PRNFlag | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PRNMaxDoseHrs | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PRNMaxDoseNumHrs | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PatchApplyAt | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PatchDurUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PatchDuration | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PatchRemoveAfter | integer |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PatchRemoveAt | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PathwayItemDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2PatientHeight | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PatientWeight | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2PerIVGuideline | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ProcActivityDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2ProcPhaseDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2ProgBolusDose | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ProgBolusDoseUOMDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2ProgBolusFrequency | integer |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ProgBolusFrequencyUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ReasonForModificDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2ReasonForVariance | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2RecalcDoseBeforeAdmin | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2RegAnestheticsProg | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2RestrictOverrideCde | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2Rule3ExemptInd | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2S4B3ExemptInd | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2SameServMultTimesSameDay | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2SelfDeemedCode | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ServPartNormAftercare | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2ServiceText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2TargetSPO2DR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2TeleConsult | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2TempMedicareNumber | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2TimeCriticalWindow | double |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2TreatmentLocCde | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ITM2VarReasonDoseDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2VarReasonDoseDuratDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2VarReasonDuratDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2VarReasonFreqDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2VarReasonRateDoseDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_ITM2VarReasonRateDuratDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_IVCalcMeth | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_IVType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_IVUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_IncompReas | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_IndicateTransfusion | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Interval | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LBTSBPNumberOfUnits | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LBTSBPQuantity | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LBTSBPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LBTSBPReservationPeriod | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LBTSBPReservationPeriodUnit | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LBTSConfidential | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LabSpecSites | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LabVolume | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LabelText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Linked | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_LinkedItmID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_MSOEOrdItemID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_MealType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_MeteredDose | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Modifiers | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NeedleGauge | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NeedleType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NewOrdItemID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NextDoseDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NextDoseTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NotifyClinician | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_NotifyMod | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OECPRDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIActivity | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIAnnotateDR | bigint |  | FK | SI | - |
| MRLO_PrefParams_DR_OEORIApprovalDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIApprovalInd | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIApprovalNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIApprovalTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIApprovedBy | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIAutologousBloodReq | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIBBTAG1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIBBTAG2 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIBBTAG3 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIBBTAG4 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIBBTAG5 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIBillDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORICompXMatchReq | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIConsult | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIContOrderAfterDischarge | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORICurrRepeatNumber | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIDSReportFlag | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIDepProcNotes | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIDoseQty | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIEndDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIEndTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIFreqDelay | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIInsBillConditDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_OEORIItemGroup | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIItmMastDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_OEORILab1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORILab2 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORILabEpisodeNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIMaxNumberOfRepeats | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIMaxRepeats | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIPatConsentObtained | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIPrescRepExpiryDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIPrescRepNumberDays | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIPrice | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIQty | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIQtyPackUOM | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIRBResourceDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_OEORIReasOrdCMVNegBlood | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIRefDocDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_OEORIRemarks | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIResultDSReportFlag | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIRoute | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORISpecialty | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORISttDat | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORISttTim | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIText1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIText2 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIText3 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIText4 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIUserGroupAdd | bigint |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIVarianceReasonDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_OEORIView | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIWhoGoWhere | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo2 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo3 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo4 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo5 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo6 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo7 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo8 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OEORIYesNo9 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OERemoteDutyID | bigint |  |  | SI | - |
| MRLO_PrefParams_DR_ORDERSETID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ORNCDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OSTATDesc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OperationID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OrdSetDateID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OrderID | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_OverseerUser | bigint |  |  | SI | - |
| MRLO_PrefParams_DR_PHCDUDesc1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PHCFRDesc1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PHCINDesc1 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PRNIndication | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PRNMaxDose24hr | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PRNTotNumDoseAllow | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PasteurisedFood | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PathwayId | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PatientLoc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Payor | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PhoneOrder | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Plan | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PortableEquiptRequired | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PrefConMethod | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_PreparationTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Protein | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODCareProvText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODContactNoText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODDMOSeenByDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODDMOSeenByTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODHospNotifDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODHospNotifTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODPlaceOfOrder | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODPlanCallBackBy | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODPlanCallBackDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODPlanCallBackTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRecCareProv | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRecCareProvText | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODReferPrio | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRemarks | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetAcceptDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetAcceptTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetArriveDestDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetArriveDestTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetDepartBaseDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetDepartBaseTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetDepartDestDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetDepartDestTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetETABaseDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetETABaseTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetPlanDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetPlanTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetPrio | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODRetTransp | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODTransferLoc | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODTriaged | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_REMODType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RMDuration | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RMFrequency | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RadNo | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ReceivedDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ReceivedTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RefDoctorList | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_ReqForTheat | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RequestedDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RequestedTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RiceType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_RouteAdmin | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Session | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_StartEndMealType | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_SteriliseUtensils | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_TempStat | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_TheatBookDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_USERID | bigint |  |  | SI | - |
| MRLO_PrefParams_DR_UnitHrs | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_UnitsColl | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_Volume | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_formAltReasonDR | varchar |  | FK | SI | - |
| MRLO_PrefParams_DR_hiddenLBEPClinicalConditions | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_lstEmbedOSExcluded | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_lstOSExclusions | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_mDate | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_mTime | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_prosthetic2 | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_refclincode | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_teeth | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_urgent | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_zProsthetics | varchar |  |  | SI | - |
| MRLO_PrefParams_DR_zSpecSites | varchar |  |  | SI | - |
| MRLO_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Face |
| Q02 | - |  |  | SI | Legs |
| Q03 | - |  |  | SI | Activity |
| Q04 | - |  |  | SI | Cry |
| Q05 | - |  |  | SI | Consolability |
| Q06 | - |  |  | SI | How to use the FLACC |
| Q07 | - |  |  | SI | Inpatient who are awake: |
| Q08 | - |  |  | SI | observe for 1 to 5 minutes or longer. Observe legs... |
| Q09 | - |  |  | SI | Inpatients wo are asleep: |
| Q10 | - |  |  | SI | observe for 5 minutes or longer. Observe body and ... |
| Q11 | - |  |  | SI | Face |
| Q12 | - |  |  | SI | Score 0 if the patient has a relaxed face, makes e... |
| Q13 | - |  |  | SI | Score 1 if the patient has a worried facial expres... |
| Q14 | - |  |  | SI | Score 2 if the patient has deep furrows in the for... |
| Q15 | - |  |  | SI | Legs |
| Q16 | - |  |  | SI | Score 0 if the muscle tone and motion in the limbs... |
| Q17 | - |  |  | SI | Score 1 if patient has increased tone, rigidity, o... |
| Q18 | - |  |  | SI | Score 2 if patient has hypertonicity, the legs are... |
| Q19 | - |  |  | SI | Activity |
| Q20 | - |  |  | SI | Score 0 if the patient moves easily and freely, no... |
| Q21 | - |  |  | SI | Score 1 if the patient shifts positions, appears h... |
| Q22 | - |  |  | SI | Score 2 if the patient is in a fixed position, roc... |
| Q23 | - |  |  | SI | Cry |
| Q24 | - |  |  | SI | Score 0 if the patient has no cry or moan, awake o... |
| Q25 | - |  |  | SI | Score 1 if the patient has occasional moans, cries... |
| Q26 | - |  |  | SI | Score 2 if the patient has frequent or continuous ... |
| Q27 | - |  |  | SI | Consolability |
| Q28 | - |  |  | SI | Score 0 if the patient is calm and does not requir... |
| Q29 | - |  |  | SI | Score 1 if the patient responds to comfort by touc... |
| Q30 | - |  |  | SI | Score 2 if the patient requires constant comfortin... |
| Q31 | - |  |  | SI | Whenever feasible, behavioral measurement of pain ... |
| Q32 | - |  |  | SI | 0: Relaxed and comfortable |
| Q33 | - |  |  | SI | 1–3: Mild discomfort |
| Q34 | - |  |  | SI | 4–6: Moderate pain |
| Q35 | - |  |  | SI | 7–10: Severe discomfort or pain or both |
| Q36 | - |  |  | SI | From Merkel, S. I., Voepel-Lewis, T., Shayevitz, J... |
| Q37 | - |  |  | SI | require careful consideration of the context in wh... |
| Q38 | - |  |  | SI | Instructions |
| Q39 | - |  |  | SI | Date |
| Q40 | - |  |  | SI | Time |
| Q41 | - |  |  | SI | Score |
| Q42 | - |  |  | SI | Classification |
| Q43 | - |  |  | SI | 0 |
| Q44 | - |  |  | SI | Relaxed and comfortable |
| Q45 | - |  |  | SI | 1 – 3 |
| Q46 | - |  |  | SI | Mild discomfort |
| Q47 | - |  |  | SI | 4 - 6 |
| Q48 | - |  |  | SI | Moderate pain |
| Q49 | - |  |  | SI | 7 - 10 |
| Q50 | - |  |  | SI | Severe discomfort or pain or both |
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