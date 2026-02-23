# web_Msg.MR_Medication

**Schema:** web_Msg
**Columnas:** 491
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ExternalData | bit |  |  | SI | External data from National Database. If set to 1 ... |
| FavPrefParams | varchar |  |  | SI | todo |
| ID | varchar |  |  | NO | - |
| MED_AdminRoute_DR | bigint |  | FK | SI | Des Ref PHCAdministrationRoute |
| MED_Ceased | varchar |  |  | SI | Ceased |
| MED_Childsub | double |  |  | SI | Childsub |
| MED_Condition_DR | bigint |  | FK | SI | Des Ref ICDDx |
| MED_DMDForm_DR | bigint |  | FK | SI | Des Ref PHCForm |
| MED_DMDStrength_DR | bigint |  | FK | SI | Des Ref PHCStrength |
| MED_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| MED_DischStatus | varchar |  |  | SI | Medication Discharge Status |
| MED_DispenseDate | date |  |  | SI | Dispense Date |
| MED_DispenseType | varchar |  |  | SI | Dispense Type for Discharge |
| MED_Dose | varchar |  |  | SI | Dose |
| MED_DoseModelDoseChange | bit |  |  | SI | MEDDoseModelDoseChange |
| MED_DoseModelFrequencyChange | bit |  |  | SI | MEDDoseModelFrequencyChange |
| MED_DoseUOM_DR | bigint |  | FK | SI | Des Ref UOM |
| MED_DosingCycles | varchar |  |  | SI | A List of Dosing Cycles |
| MED_DosingModelChangeType | varchar |  |  | SI | MEDDosingModelChangeType |
| MED_DrgForm_DR | varchar |  | FK | SI | Des Ref DrgForm |
| MED_DrgMast_DR | bigint |  | FK | SI | Des Ref DrgMast |
| MED_DurationFree | varchar |  |  | SI | DurationFree |
| MED_DurationType | varchar |  |  | SI | Duration Type |
| MED_DurationUnit | varchar |  |  | SI | Duration Unit |
| MED_DurationValue | double |  |  | SI | Duration Value |
| MED_Duration_DR | bigint |  | FK | SI | Des Ref Duration |
| MED_EndDate | date |  |  | SI | EndDate |
| MED_EndTime | time |  |  | SI | End Time |
| MED_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| MED_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| MED_ExcludeFromDS | varchar |  |  | SI | ExcludeFromDS |
| MED_ExtIdenfierCode | varchar |  |  | SI | External Identifier Code |
| MED_FreeTextFreqUnit | varchar |  |  | SI | Free Text Frequency Unit |
| MED_FreeTextFreqValue | double |  |  | SI | Free Text Frequency Value  |
| MED_FreqDelay | double |  |  | SI | FreqDelay |
| MED_Freq_DR | bigint |  | FK | SI | Des Ref Freq |
| MED_GenRtFrm_DR | varchar |  | FK | SI | Des Ref GenRtFrm |
| MED_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| MED_HL7Number | varchar |  |  | SI | HL7Number |
| MED_HisCompliance_DR | bigint |  | FK | SI | Des Ref PHCMedHisCompliance |
| MED_HisDurType_DR | bigint |  | FK | SI | Des Ref PHCMedHisDurationType |
| MED_HisInfoSrc_DR | bigint |  | FK | SI | Des Ref PHCMedHistInformSource |
| MED_IVType | varchar |  |  | SI | IVType |
| MED_Ingredient_DR | bigint |  | FK | SI | Lifetime Cumulative Dose Tracked Ingedient  |
| MED_ItmMast_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| MED_LastDoseDate | date |  |  | SI | Last Dose Date |
| MED_LastDoseTime | time |  |  | SI | Last Dose Time |
| MED_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| MED_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MED_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| MED_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| MED_LifeTimeCumDose | varchar |  |  | SI | Lifetime Cumulative Dose Addition  |
| MED_NewPRNMaxDose24hrs | double |  |  | SI | NewPRNMaxDose24hrs |
| MED_NewPRNMaxDose24hrsUnit_DR | bigint |  | FK | SI | NewPRNMaxDose24hrsUnit |
| MED_OEORI_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| MED_PRN | varchar |  |  | SI | PRN |
| MED_Pack_DR | bigint |  | FK | SI | Des Ref to PHCPA (Packing) |
| MED_ParRef | bigint |  |  | SI | MR_Adm Parent Reference
Required by User.MRMedica... |
| MED_PrefParamsDosing_DR | varchar |  | FK | SI | Default Dosing Cycle |
| MED_PrefParams_DR_AccessionNumber | varchar |  |  | SI | - |
| MED_PrefParams_DR_ActivityModifierList | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmAfterSkinTest | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdministrativeOrder | bit |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMAddedAdditiveFlg | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMAdmixType | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMAllowToModify | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMFinalFormDR | bigint |  | FK | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMMainItem | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMMaxFlowRate | double |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMMinFlowRate | double |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMOrderedBagVolume | double |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMPCALoadingVolume | double |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMPCALoadingVolumeUOMDR | bigint |  | FK | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMQuantity | double |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMResolvedSolvDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMSolventDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMSubtractAdditive | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMTotalFlowRate | double |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMTotalFlowRatePerUOM | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMTotalFlowRateUOMDR | bigint |  | FK | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMUOMDR | bigint |  | FK | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_AMWithoutSolvent | varchar |  |  | SI | - |
| MED_PrefParams_DR_AdmixParamsDR_Additives | varchar |  |  | SI | - |
| MED_PrefParams_DR_AlertReason | varchar |  |  | SI | - |
| MED_PrefParams_DR_Altpatloc | varchar |  |  | SI | - |
| MED_PrefParams_DR_ApptID | varchar |  |  | SI | - |
| MED_PrefParams_DR_AuthDoctor | varchar |  |  | SI | - |
| MED_PrefParams_DR_BillPrice | varchar |  |  | SI | - |
| MED_PrefParams_DR_BodySite | varchar |  |  | SI | - |
| MED_PrefParams_DR_BookingOrder | bit |  |  | SI | - |
| MED_PrefParams_DR_CONSDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_COPYID | varchar |  |  | SI | - |
| MED_PrefParams_DR_CTLOCDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_CTPCPDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_CTPCPID | varchar |  |  | SI | - |
| MED_PrefParams_DR_CTUOMDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_CalcQtyFlag2 | varchar |  |  | SI | - |
| MED_PrefParams_DR_Carbohydrate | varchar |  |  | SI | - |
| MED_PrefParams_DR_CarePlanIssueID | varchar |  |  | SI | - |
| MED_PrefParams_DR_CareProvCodeList | varchar |  |  | SI | - |
| MED_PrefParams_DR_CareProvList | varchar |  |  | SI | - |
| MED_PrefParams_DR_ClinCondDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ColDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_ColTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_ContactCareProv | varchar |  |  | SI | - |
| MED_PrefParams_DR_CoveredByMainInsur | varchar |  |  | SI | - |
| MED_PrefParams_DR_CreateDate | date |  |  | SI | - |
| MED_PrefParams_DR_CreateTime | time |  |  | SI | - |
| MED_PrefParams_DR_DBLaboratoryCode | varchar |  |  | SI | - |
| MED_PrefParams_DR_DayCycle | varchar |  |  | SI | - |
| MED_PrefParams_DR_DefRptDur | varchar |  |  | SI | - |
| MED_PrefParams_DR_DefRptLoc | varchar |  |  | SI | - |
| MED_PrefParams_DR_DelayMeal | varchar |  |  | SI | - |
| MED_PrefParams_DR_DeptDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_DoNotDisp | varchar |  |  | SI | - |
| MED_PrefParams_DR_Doctor | varchar |  |  | SI | - |
| MED_PrefParams_DR_DrugDelRate | varchar |  |  | SI | - |
| MED_PrefParams_DR_DrugDelUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_EligibilityStatus | varchar |  |  | SI | - |
| MED_PrefParams_DR_EndDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_Energy | varchar |  |  | SI | - |
| MED_PrefParams_DR_EnteredUOM | varchar |  |  | SI | - |
| MED_PrefParams_DR_EpisodeID | bigint |  |  | SI | - |
| MED_PrefParams_DR_Fat | varchar |  |  | SI | - |
| MED_PrefParams_DR_FeedString | varchar |  |  | SI | - |
| MED_PrefParams_DR_FlowQty | varchar |  |  | SI | - |
| MED_PrefParams_DR_FlowRateUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_FlowTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_ForceGenEXE | varchar |  |  | SI | - |
| MED_PrefParams_DR_FreeText | varchar |  |  | SI | - |
| MED_PrefParams_DR_HL7Flag | varchar |  |  | SI | - |
| MED_PrefParams_DR_HidAuthPrescDetail | varchar |  |  | SI | - |
| MED_PrefParams_DR_HotReport | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2AcceptDisabilityInd | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2AcceptDisabilityText | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2AltBodyWeightObsDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2AntimicrobialApprovalNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ApprovalAdminReq | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPGDoseBased | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPGUOMDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2BPQuantity | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPRequiredByDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPRequiredByTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPReservationPeriod | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2BPReservationPeriodUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CNMItemNotes | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CNMNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CNMOverrideReason | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CNMStatusDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2CalDoseHTMLPlainText | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CalDoseHTMLRichText | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CalTemplateDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2CalTemplateParamsDR_DCTCTUOMDR | bigint |  | FK | SI | - |
| MED_PrefParams_DR_ITM2CalTemplateParamsDR_DCTDurationUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CalTemplateParamsDR_Details | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CalcDoseDetail | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CalcIVDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2Confidential | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2CopyCycleOrder | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2Derived | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DispenseType | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DistanceKms | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoNotSubstitute | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalLinkedNONTCLELabs | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalLinkedObs | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalLinkedTCLELabs | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalProtocolBase | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalRangeDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalRangeFrom | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalRangeTo | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseCalRangeUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseInML | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DoseRecalPermitted | bit |  |  | SI | - |
| MED_PrefParams_DR_ITM2DropsMin | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DuplServOverrideReason | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DurationType | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DurationUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2DurationValue | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2EPrescItemNotes | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2EPrescNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2EPrescOverrideReason | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2EPrescStatus | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2EquipmentId | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2Event | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ExpiryDate | date |  |  | SI | - |
| MED_PrefParams_DR_ITM2ExternalDocFiscalCode | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ExternalPaperPrescNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ExternalPrescriptionID | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2FieldQuantity | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2FluidConsistModDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2FluidVolumeRestrDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2FoodTextureModDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2FreeTextFreqUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2FreeTextFreqValue | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2IVContTotalDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2IVContTotalDoseUnitDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2IVDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2IVUnitDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2InHospService | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2Indication | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2InfusTypeEndDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2InfusTypeEndTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2LSPNum | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2LateralityDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2Link | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2LoanRetDate | date |  |  | SI | - |
| MED_PrefParams_DR_ITM2LostLoanItem | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2MRMedLinkedOrder | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2MaxDeliveryRate | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2MedicationDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2MinDeliveryRate | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2MinDoseQty | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2MinPhQtyOrd | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2MultPrSamePatSameDocSameDay | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2MultProcNotes | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2NFMICategDepart | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2NewPRNMaxDose24hrs | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2NewPRNMaxDose24hrsUnitDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2NonPBSQuanUOMDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2NonPBSQuantity | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2AdminOver | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2AdminOverUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2ContDelivery | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2DeliveryMethodDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2O2MaxRate | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2Rate | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2RateCalMethod | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2O2RateUOMDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2OrderVersion | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2OverUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2OverValue | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2OverrideIVUnitDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2OverrideQtyBaseUOM | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSAuthorityApprovalCode | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSAuthorityApprovalPending | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSAuthorityNumber | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSNonPBSFlag | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSPrescribingRuleBenefitDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2PBSQuantity | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSRepeats | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2PBSRestrictionDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2PBSStreamlineNumber | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PCABolusDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PCADoseInterval | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PCADoseUOMDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2PCALoadingDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PCAMaxDoseHours | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PCAMaximumDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PHCIVAdminSetDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2PRNFlag | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PRNMaxDoseHrs | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2PRNMaxDoseNumHrs | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PatchApplyAt | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PatchDurUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PatchDuration | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PatchRemoveAfter | integer |  |  | SI | - |
| MED_PrefParams_DR_ITM2PatchRemoveAt | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PathwayItemDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2PatientHeight | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2PatientWeight | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2PerIVGuideline | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ProcActivityDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2ProcPhaseDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2ProgBolusDose | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2ProgBolusDoseUOMDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2ProgBolusFrequency | integer |  |  | SI | - |
| MED_PrefParams_DR_ITM2ProgBolusFrequencyUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ReasonForModificDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2ReasonForVariance | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2RecalcDoseBeforeAdmin | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2RegAnestheticsProg | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2RestrictOverrideCde | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2Rule3ExemptInd | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2S4B3ExemptInd | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2SameServMultTimesSameDay | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2SelfDeemedCode | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ServPartNormAftercare | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2ServiceText | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2TargetSPO2DR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2TeleConsult | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2TempMedicareNumber | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2TimeCriticalWindow | double |  |  | SI | - |
| MED_PrefParams_DR_ITM2TreatmentLocCde | varchar |  |  | SI | - |
| MED_PrefParams_DR_ITM2VarReasonDoseDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2VarReasonDoseDuratDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2VarReasonDuratDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2VarReasonFreqDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2VarReasonRateDoseDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_ITM2VarReasonRateDuratDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_IVCalcMeth | varchar |  |  | SI | - |
| MED_PrefParams_DR_IVType | varchar |  |  | SI | - |
| MED_PrefParams_DR_IVUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_IncompReas | varchar |  |  | SI | - |
| MED_PrefParams_DR_IndicateTransfusion | varchar |  |  | SI | - |
| MED_PrefParams_DR_Interval | varchar |  |  | SI | - |
| MED_PrefParams_DR_LBTSBPNumberOfUnits | varchar |  |  | SI | - |
| MED_PrefParams_DR_LBTSBPQuantity | varchar |  |  | SI | - |
| MED_PrefParams_DR_LBTSBPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| MED_PrefParams_DR_LBTSBPReservationPeriod | varchar |  |  | SI | - |
| MED_PrefParams_DR_LBTSBPReservationPeriodUnit | varchar |  |  | SI | - |
| MED_PrefParams_DR_LBTSConfidential | varchar |  |  | SI | - |
| MED_PrefParams_DR_LabSpecSites | varchar |  |  | SI | - |
| MED_PrefParams_DR_LabVolume | varchar |  |  | SI | - |
| MED_PrefParams_DR_LabelText | varchar |  |  | SI | - |
| MED_PrefParams_DR_Linked | varchar |  |  | SI | - |
| MED_PrefParams_DR_LinkedItmID | varchar |  |  | SI | - |
| MED_PrefParams_DR_MSOEOrdItemID | varchar |  |  | SI | - |
| MED_PrefParams_DR_MealType | varchar |  |  | SI | - |
| MED_PrefParams_DR_MeteredDose | varchar |  |  | SI | - |
| MED_PrefParams_DR_Modifiers | varchar |  |  | SI | - |
| MED_PrefParams_DR_NeedleGauge | varchar |  |  | SI | - |
| MED_PrefParams_DR_NeedleType | varchar |  |  | SI | - |
| MED_PrefParams_DR_NewOrdItemID | varchar |  |  | SI | - |
| MED_PrefParams_DR_NextDoseDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_NextDoseTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_NotifyClinician | varchar |  |  | SI | - |
| MED_PrefParams_DR_NotifyMod | varchar |  |  | SI | - |
| MED_PrefParams_DR_OECPRDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIActivity | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIAnnotateDR | bigint |  | FK | SI | - |
| MED_PrefParams_DR_OEORIApprovalDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIApprovalInd | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIApprovalNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIApprovalTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIApprovedBy | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIAutologousBloodReq | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIBBTAG1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIBBTAG2 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIBBTAG3 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIBBTAG4 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIBBTAG5 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIBillDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORICompXMatchReq | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIConsult | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIContOrderAfterDischarge | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORICurrRepeatNumber | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIDSReportFlag | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIDepProcNotes | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIDoseQty | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIEndDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIEndTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIFreqDelay | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIInsBillConditDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_OEORIItemGroup | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIItmMastDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_OEORILab1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORILab2 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORILabEpisodeNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIMaxNumberOfRepeats | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIMaxRepeats | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIPatConsentObtained | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIPrescRepExpiryDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIPrescRepNumberDays | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIPrice | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIQty | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIQtyPackUOM | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIRBResourceDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_OEORIReasOrdCMVNegBlood | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIRefDocDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_OEORIRemarks | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIResultDSReportFlag | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIRoute | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORISpecialty | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORISttDat | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORISttTim | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIText1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIText2 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIText3 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIText4 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIUserGroupAdd | bigint |  |  | SI | - |
| MED_PrefParams_DR_OEORIVarianceReasonDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_OEORIView | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIWhoGoWhere | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo2 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo3 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo4 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo5 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo6 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo7 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo8 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OEORIYesNo9 | varchar |  |  | SI | - |
| MED_PrefParams_DR_OERemoteDutyID | bigint |  |  | SI | - |
| MED_PrefParams_DR_ORDERSETID | varchar |  |  | SI | - |
| MED_PrefParams_DR_ORNCDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_OSTATDesc | varchar |  |  | SI | - |
| MED_PrefParams_DR_OperationID | varchar |  |  | SI | - |
| MED_PrefParams_DR_OrdSetDateID | varchar |  |  | SI | - |
| MED_PrefParams_DR_OrderID | varchar |  |  | SI | - |
| MED_PrefParams_DR_OverseerUser | bigint |  |  | SI | - |
| MED_PrefParams_DR_PHCDUDesc1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_PHCFRDesc1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_PHCINDesc1 | varchar |  |  | SI | - |
| MED_PrefParams_DR_PRNIndication | varchar |  |  | SI | - |
| MED_PrefParams_DR_PRNMaxDose24hr | varchar |  |  | SI | - |
| MED_PrefParams_DR_PRNTotNumDoseAllow | varchar |  |  | SI | - |
| MED_PrefParams_DR_PasteurisedFood | varchar |  |  | SI | - |
| MED_PrefParams_DR_PathwayId | varchar |  |  | SI | - |
| MED_PrefParams_DR_PatientLoc | varchar |  |  | SI | - |
| MED_PrefParams_DR_Payor | varchar |  |  | SI | - |
| MED_PrefParams_DR_PhoneOrder | varchar |  |  | SI | - |
| MED_PrefParams_DR_Plan | varchar |  |  | SI | - |
| MED_PrefParams_DR_PortableEquiptRequired | varchar |  |  | SI | - |
| MED_PrefParams_DR_PrefConMethod | varchar |  |  | SI | - |
| MED_PrefParams_DR_PreparationTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_Protein | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODCareProvText | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODContactNoText | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODDMOSeenByDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODDMOSeenByTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODHospNotifDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODHospNotifTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODPlaceOfOrder | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODPlanCallBackBy | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODPlanCallBackDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODPlanCallBackTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRecCareProv | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRecCareProvText | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODReferPrio | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRemarks | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetAcceptDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetAcceptTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetArriveDestDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetArriveDestTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetDepartBaseDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetDepartBaseTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetDepartDestDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetDepartDestTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetETABaseDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetETABaseTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetPlanDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetPlanTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetPrio | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODRetTransp | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODTransferLoc | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODTriaged | varchar |  |  | SI | - |
| MED_PrefParams_DR_REMODType | varchar |  |  | SI | - |
| MED_PrefParams_DR_RMDuration | varchar |  |  | SI | - |
| MED_PrefParams_DR_RMFrequency | varchar |  |  | SI | - |
| MED_PrefParams_DR_RadNo | varchar |  |  | SI | - |
| MED_PrefParams_DR_ReceivedDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_ReceivedTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_RefDoctorList | varchar |  |  | SI | - |
| MED_PrefParams_DR_ReqForTheat | varchar |  |  | SI | - |
| MED_PrefParams_DR_RequestedDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_RequestedTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_RiceType | varchar |  |  | SI | - |
| MED_PrefParams_DR_RouteAdmin | varchar |  |  | SI | - |
| MED_PrefParams_DR_Session | varchar |  |  | SI | - |
| MED_PrefParams_DR_StartEndMealType | varchar |  |  | SI | - |
| MED_PrefParams_DR_SteriliseUtensils | varchar |  |  | SI | - |
| MED_PrefParams_DR_TempStat | varchar |  |  | SI | - |
| MED_PrefParams_DR_TheatBookDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_USERID | bigint |  |  | SI | - |
| MED_PrefParams_DR_UnitHrs | varchar |  |  | SI | - |
| MED_PrefParams_DR_UnitsColl | varchar |  |  | SI | - |
| MED_PrefParams_DR_Volume | varchar |  |  | SI | - |
| MED_PrefParams_DR_formAltReasonDR | varchar |  | FK | SI | - |
| MED_PrefParams_DR_hiddenLBEPClinicalConditions | varchar |  |  | SI | - |
| MED_PrefParams_DR_lstEmbedOSExcluded | varchar |  |  | SI | - |
| MED_PrefParams_DR_lstOSExclusions | varchar |  |  | SI | - |
| MED_PrefParams_DR_mDate | varchar |  |  | SI | - |
| MED_PrefParams_DR_mTime | varchar |  |  | SI | - |
| MED_PrefParams_DR_prosthetic2 | varchar |  |  | SI | - |
| MED_PrefParams_DR_refclincode | varchar |  |  | SI | - |
| MED_PrefParams_DR_teeth | varchar |  |  | SI | - |
| MED_PrefParams_DR_urgent | varchar |  |  | SI | - |
| MED_PrefParams_DR_zProsthetics | varchar |  |  | SI | - |
| MED_PrefParams_DR_zSpecSites | varchar |  |  | SI | - |
| MED_ReasonForCorrection_DR | bigint |  | FK | SI | Reason for Correction |
| MED_ReasonForStop_DR | bigint |  | FK | SI | Medication Stop Reason |
| MED_RowId | varchar |  |  | SI | - |
| MED_ShowInDS | varchar |  |  | SI | ShowInDS |
| MED_Sources | varchar |  |  | SI | Sources |
| MED_StartDate | date |  |  | SI | StartDate |
| MED_Status | varchar |  |  | SI | Medication Status |
| MED_SupplyOnHand | varchar |  |  | SI | Supply on Hand |
| MED_SupplyOnHandUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| MED_TimeCriticalWindow | double |  |  | SI | Time Critical Window (minutes) |
| MED_Type | varchar |  |  | SI | Type |
| MED_UpdateDate | date |  |  | SI | UpdateDate |
| MED_UpdateTime | time |  |  | SI | UpdateTime |
| MED_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| MED_UseSelectedType | varchar |  |  | SI | Use Selected Dispense Type |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ToBeDeleted | bit |  |  | SI | Mark this row to be deleted when the whole page is... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*