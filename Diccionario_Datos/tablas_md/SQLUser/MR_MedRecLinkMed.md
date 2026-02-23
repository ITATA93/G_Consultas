# SQLUser.MR_MedRecLinkMed

**Schema:** SQLUser
**Columnas:** 493
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRLM_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| MRLM_Ceased | varchar |  |  | SI | Ceased |
| MRLM_Childsub | double |  |  | NO | Childsub |
| MRLM_Decision | varchar |  |  | SI | Decision |
| MRLM_DoseModelDoseChange | bit |  |  | SI | DoseModel Dose Change |
| MRLM_DoseModelFrequencyChange | bit |  |  | SI | DoseModel Frequency Change |
| MRLM_DosingModelChangeType | varchar |  |  | SI | DosingModel ChangeType |
| MRLM_MRMedication_DR | varchar |  | FK | SI | Des Ref MRMedication |
| MRLM_PrefParamsDosing_DR | varchar |  | FK | SI | Default Dosing Cycle |
| MRLM_PrefParams_DR_AccessionNumber | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ActivityModifierList | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmAfterSkinTest | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdministrativeOrder | bit |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMAddedAdditiveFlg | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMAdmixType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMAllowToModify | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMFinalFormDR | bigint |  | FK | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMMainItem | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMMaxFlowRate | double |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMMinFlowRate | double |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMOrderedBagVolume | double |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMPCALoadingVolume | double |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMPCALoadingVolumeUOMDR | bigint |  | FK | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMQuantity | double |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMResolvedSolvDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMSolventDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMSubtractAdditive | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMTotalFlowRate | double |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMTotalFlowRatePerUOM | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMTotalFlowRateUOMDR | bigint |  | FK | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMUOMDR | bigint |  | FK | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_AMWithoutSolvent | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AdmixParamsDR_Additives | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AlertReason | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Altpatloc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ApptID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_AuthDoctor | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_BillPrice | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_BodySite | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_BookingOrder | bit |  |  | SI | - |
| MRLM_PrefParams_DR_CONSDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_COPYID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CTLOCDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CTPCPDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CTPCPID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CTUOMDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CalcQtyFlag2 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Carbohydrate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CarePlanIssueID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CareProvCodeList | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CareProvList | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ClinCondDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ColDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ColTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ContactCareProv | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CoveredByMainInsur | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_CreateDate | date |  |  | SI | - |
| MRLM_PrefParams_DR_CreateTime | time |  |  | SI | - |
| MRLM_PrefParams_DR_DBLaboratoryCode | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DayCycle | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DefRptDur | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DefRptLoc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DelayMeal | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DeptDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DoNotDisp | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Doctor | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DrugDelRate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_DrugDelUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_EligibilityStatus | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_EndDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Energy | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_EnteredUOM | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_EpisodeID | bigint |  |  | SI | - |
| MRLM_PrefParams_DR_Fat | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_FeedString | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_FlowQty | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_FlowRateUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_FlowTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ForceGenEXE | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_FreeText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_HL7Flag | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_HidAuthPrescDetail | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_HotReport | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2AcceptDisabilityInd | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2AcceptDisabilityText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2AltBodyWeightObsDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2AntimicrobialApprovalNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ApprovalAdminReq | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPGDoseBased | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPGUOMDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2BPQuantity | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPRequiredByDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPRequiredByTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPReservationPeriod | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2BPReservationPeriodUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CNMItemNotes | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CNMNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CNMOverrideReason | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CNMStatusDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2CalDoseHTMLPlainText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CalDoseHTMLRichText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CalTemplateDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2CalTemplateParamsDR_DCTCTUOMDR | bigint |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2CalTemplateParamsDR_DCTDurationUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CalTemplateParamsDR_Details | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CalcDoseDetail | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CalcIVDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2Confidential | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2CopyCycleOrder | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2Derived | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DispenseType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DistanceKms | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoNotSubstitute | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalLinkedNONTCLELabs | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalLinkedObs | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalLinkedTCLELabs | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalProtocolBase | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalRangeDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalRangeFrom | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalRangeTo | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseCalRangeUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseInML | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DoseRecalPermitted | bit |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DropsMin | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DuplServOverrideReason | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DurationType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DurationUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2DurationValue | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2EPrescItemNotes | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2EPrescNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2EPrescOverrideReason | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2EPrescStatus | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2EquipmentId | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2Event | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ExpiryDate | date |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ExternalDocFiscalCode | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ExternalPaperPrescNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ExternalPrescriptionID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2FieldQuantity | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2FluidConsistModDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2FluidVolumeRestrDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2FoodTextureModDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2FreeTextFreqUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2FreeTextFreqValue | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2IVContTotalDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2IVContTotalDoseUnitDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2IVDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2IVUnitDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2InHospService | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2Indication | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2InfusTypeEndDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2InfusTypeEndTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2LSPNum | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2LateralityDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2Link | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2LoanRetDate | date |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2LostLoanItem | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MRMedLinkedOrder | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MaxDeliveryRate | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MedicationDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2MinDeliveryRate | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MinDoseQty | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MinPhQtyOrd | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MultPrSamePatSameDocSameDay | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2MultProcNotes | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2NFMICategDepart | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2NewPRNMaxDose24hrs | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2NewPRNMaxDose24hrsUnitDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2NonPBSQuanUOMDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2NonPBSQuantity | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2AdminOver | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2AdminOverUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2ContDelivery | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2DeliveryMethodDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2O2MaxRate | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2Rate | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2RateCalMethod | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2O2RateUOMDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2OrderVersion | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2OverUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2OverValue | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2OverrideIVUnitDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2OverrideQtyBaseUOM | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSAuthorityApprovalCode | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSAuthorityApprovalPending | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSAuthorityNumber | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSNonPBSFlag | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSPrescribingRuleBenefitDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2PBSQuantity | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSRepeats | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PBSRestrictionDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2PBSStreamlineNumber | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PCABolusDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PCADoseInterval | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PCADoseUOMDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2PCALoadingDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PCAMaxDoseHours | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PCAMaximumDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PHCIVAdminSetDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2PRNFlag | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PRNMaxDoseHrs | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PRNMaxDoseNumHrs | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PatchApplyAt | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PatchDurUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PatchDuration | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PatchRemoveAfter | integer |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PatchRemoveAt | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PathwayItemDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2PatientHeight | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PatientWeight | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2PerIVGuideline | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ProcActivityDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2ProcPhaseDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2ProgBolusDose | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ProgBolusDoseUOMDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2ProgBolusFrequency | integer |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ProgBolusFrequencyUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ReasonForModificDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2ReasonForVariance | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2RecalcDoseBeforeAdmin | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2RegAnestheticsProg | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2RestrictOverrideCde | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2Rule3ExemptInd | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2S4B3ExemptInd | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2SameServMultTimesSameDay | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2SelfDeemedCode | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ServPartNormAftercare | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2ServiceText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2TargetSPO2DR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2TeleConsult | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2TempMedicareNumber | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2TimeCriticalWindow | double |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2TreatmentLocCde | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ITM2VarReasonDoseDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2VarReasonDoseDuratDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2VarReasonDuratDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2VarReasonFreqDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2VarReasonRateDoseDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_ITM2VarReasonRateDuratDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_IVCalcMeth | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_IVType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_IVUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_IncompReas | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_IndicateTransfusion | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Interval | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LBTSBPNumberOfUnits | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LBTSBPQuantity | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LBTSBPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LBTSBPReservationPeriod | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LBTSBPReservationPeriodUnit | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LBTSConfidential | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LabSpecSites | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LabVolume | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LabelText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Linked | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_LinkedItmID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_MSOEOrdItemID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_MealType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_MeteredDose | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Modifiers | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NeedleGauge | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NeedleType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NewOrdItemID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NextDoseDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NextDoseTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NotifyClinician | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_NotifyMod | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OECPRDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIActivity | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIAnnotateDR | bigint |  | FK | SI | - |
| MRLM_PrefParams_DR_OEORIApprovalDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIApprovalInd | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIApprovalNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIApprovalTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIApprovedBy | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIAutologousBloodReq | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIBBTAG1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIBBTAG2 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIBBTAG3 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIBBTAG4 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIBBTAG5 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIBillDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORICompXMatchReq | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIConsult | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIContOrderAfterDischarge | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORICurrRepeatNumber | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIDSReportFlag | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIDepProcNotes | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIDoseQty | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIEndDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIEndTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIFreqDelay | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIInsBillConditDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_OEORIItemGroup | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIItmMastDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_OEORILab1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORILab2 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORILabEpisodeNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIMaxNumberOfRepeats | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIMaxRepeats | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIPatConsentObtained | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIPrescRepExpiryDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIPrescRepNumberDays | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIPrice | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIQty | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIQtyPackUOM | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIRBResourceDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_OEORIReasOrdCMVNegBlood | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIRefDocDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_OEORIRemarks | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIResultDSReportFlag | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIRoute | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORISpecialty | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORISttDat | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORISttTim | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIText1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIText2 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIText3 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIText4 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIUserGroupAdd | bigint |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIVarianceReasonDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_OEORIView | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIWhoGoWhere | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo2 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo3 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo4 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo5 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo6 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo7 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo8 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OEORIYesNo9 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OERemoteDutyID | bigint |  |  | SI | - |
| MRLM_PrefParams_DR_ORDERSETID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ORNCDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OSTATDesc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OperationID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OrdSetDateID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OrderID | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_OverseerUser | bigint |  |  | SI | - |
| MRLM_PrefParams_DR_PHCDUDesc1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PHCFRDesc1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PHCINDesc1 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PRNIndication | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PRNMaxDose24hr | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PRNTotNumDoseAllow | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PasteurisedFood | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PathwayId | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PatientLoc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Payor | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PhoneOrder | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Plan | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PortableEquiptRequired | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PrefConMethod | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_PreparationTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Protein | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODCareProvText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODContactNoText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODDMOSeenByDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODDMOSeenByTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODHospNotifDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODHospNotifTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODPlaceOfOrder | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODPlanCallBackBy | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODPlanCallBackDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODPlanCallBackTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRecCareProv | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRecCareProvText | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODReferPrio | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRemarks | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetAcceptDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetAcceptTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetArriveDestDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetArriveDestTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetDepartBaseDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetDepartBaseTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetDepartDestDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetDepartDestTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetETABaseDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetETABaseTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetPlanDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetPlanTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetPrio | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODRetTransp | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODTransferLoc | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODTriaged | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_REMODType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RMDuration | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RMFrequency | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RadNo | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ReceivedDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ReceivedTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RefDoctorList | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_ReqForTheat | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RequestedDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RequestedTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RiceType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_RouteAdmin | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Session | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_StartEndMealType | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_SteriliseUtensils | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_TempStat | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_TheatBookDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_USERID | bigint |  |  | SI | - |
| MRLM_PrefParams_DR_UnitHrs | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_UnitsColl | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_Volume | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_formAltReasonDR | varchar |  | FK | SI | - |
| MRLM_PrefParams_DR_hiddenLBEPClinicalConditions | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_lstEmbedOSExcluded | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_lstOSExclusions | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_mDate | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_mTime | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_prosthetic2 | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_refclincode | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_teeth | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_urgent | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_zProsthetics | varchar |  |  | SI | - |
| MRLM_PrefParams_DR_zSpecSites | varchar |  |  | SI | - |
| MRLM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Proptosis right |
| Q02 | - |  |  | SI | Proptosis left |
| Q03 | - |  |  | SI | Periorbital haemorrhage right |
| Q04 | - |  |  | SI | Periorbital haemorrhage left |
| Q05 | - |  |  | SI | Subconjunctival haemorrhage right |
| Q06 | - |  |  | SI | Subconjunctival haemorrhage left |
| Q07 | - |  |  | SI | Subcutaneous emphysema right |
| Q08 | - |  |  | SI | Subcutaneous emphysema left |
| Q09 | - |  |  | SI | Occular movement right |
| Q10 | - |  |  | SI | Occular movement left |
| Q11 | - |  |  | SI | Pupil reflexes right |
| Q12 | - |  |  | SI | Pupil reflexes left |
| Q13 | - |  |  | SI | Pupil size right |
| Q14 | - |  |  | SI | Pupil size left |
| Q15 | - |  |  | SI | Visual acuity right |
| Q16 | - |  |  | SI | Visual acuity left |
| Q17 | - |  |  | SI | Epistaxis right |
| Q18 | - |  |  | SI | Epistaxis left |
| Q19 | - |  |  | SI | FESS comments |
| Q20 | - |  |  | SI | The eye appears protruding forward |
| Q21 | - |  |  | SI | Bruising around the eye |
| Q22 | - |  |  | SI | Bleeding into the white portion of the eye |
| Q23 | - |  |  | SI | Bubbles of air under the skin |
| Q24 | - |  |  | SI | Assess lateral, medial, up and down movement |
| Q25 | - |  |  | SI | Light shone into eye should product constriction o... |
| Q26 | - |  |  | SI | Use pupil scale 1-8 |
| Q27 | - |  |  | SI | Check for deterioration compared with pre-op |
| Q28 | - |  |  | SI | Bleeding from the nose |
| Q29 | - |  |  | SI | Right side |
| Q30 | - |  |  | SI | Left side |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
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