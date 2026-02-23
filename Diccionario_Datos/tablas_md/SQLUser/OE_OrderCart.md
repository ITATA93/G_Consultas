# SQLUser.OE_OrderCart

**Schema:** SQLUser
**Columnas:** 450
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OECART_RowId | bigint | PK |  | NO | - |
| ChildQ30DR | - |  |  | SI | Child Reference: Elbow |
| OECART_CSPSessionId | varchar |  |  | SI | Updated by CSP Session |
| OECART_ComputerId | varchar |  |  | SI | Updated by Device Identifier
ComputerName else IP |
| OECART_Date | date |  |  | NO | Updated Date |
| OECART_EncounterEntryParams | varchar |  |  | SI | Encounter Entry Parameters, if the original order ... |
| OECART_ExcludeFromSequence | varchar |  |  | SI | ITM2ExcludeFromSequence Flag of the original order... |
| OECART_Group_DR | bigint |  | FK | SI | Logon Security Group at time of Creation |
| OECART_HasDosingModel | varchar |  |  | SI | ITM2HasDosingModel Flag of the original order item |
| OECART_HasRecurrenceOrder | varchar |  |  | SI | Recurrence Order Flag of the original order item |
| OECART_HasSequenceData | varchar |  |  | SI | ITM2HasSequenceData Flag of the original order ite... |
| OECART_OEEntId | varchar |  |  | SI | OEOrdEnt ID when the item was placed, to distingui... |
| OECART_OEORD_DR | numeric |  | FK | NO | Des Ref to OEORD
OEOrder header for Item |
| OECART_OEORIChildsub | numeric |  |  | SI | Childsub of the Inactive OEOrdItem that this recor... |
| OECART_OIVALAdmix | varchar |  |  | SI | OEAdmix data from global |
| OECART_OIVAL_AccessionNumber | varchar |  |  | SI | - |
| OECART_OIVAL_ActivityModifierList | varchar |  |  | SI | - |
| OECART_OIVAL_AdmAfterSkinTest | varchar |  |  | SI | - |
| OECART_OIVAL_AdministrativeOrder | bit |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMAddedAdditiveFlg | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMAdmixType | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMAllowToModify | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMFinalFormDR | bigint |  | FK | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMMainItem | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMMaxFlowRate | double |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMMinFlowRate | double |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMOrderedBagVolume | double |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMPCALoadingVolume | double |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMPCALoadingVolumeUOMDR | bigint |  | FK | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMQuantity | double |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMResolvedSolvDR | varchar |  | FK | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMSolventDR | varchar |  | FK | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMSubtractAdditive | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMTotalFlowRate | double |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMTotalFlowRatePerUOM | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMTotalFlowRateUOMDR | bigint |  | FK | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMUOMDR | bigint |  | FK | SI | - |
| OECART_OIVAL_AdmixParamsDR_AMWithoutSolvent | varchar |  |  | SI | - |
| OECART_OIVAL_AdmixParamsDR_Additives | varchar |  |  | SI | - |
| OECART_OIVAL_AlertReason | varchar |  |  | SI | - |
| OECART_OIVAL_Altpatloc | varchar |  |  | SI | - |
| OECART_OIVAL_ApptID | varchar |  |  | SI | - |
| OECART_OIVAL_AuthDoctor | varchar |  |  | SI | - |
| OECART_OIVAL_BillPrice | varchar |  |  | SI | - |
| OECART_OIVAL_BodySite | varchar |  |  | SI | - |
| OECART_OIVAL_BookingOrder | bit |  |  | SI | - |
| OECART_OIVAL_CONSDesc | varchar |  |  | SI | - |
| OECART_OIVAL_COPYID | varchar |  |  | SI | - |
| OECART_OIVAL_CTLOCDesc | varchar |  |  | SI | - |
| OECART_OIVAL_CTPCPDesc | varchar |  |  | SI | - |
| OECART_OIVAL_CTPCPID | varchar |  |  | SI | - |
| OECART_OIVAL_CTUOMDesc | varchar |  |  | SI | - |
| OECART_OIVAL_CalcQtyFlag2 | varchar |  |  | SI | - |
| OECART_OIVAL_Carbohydrate | varchar |  |  | SI | - |
| OECART_OIVAL_CarePlanIssueID | varchar |  |  | SI | - |
| OECART_OIVAL_CareProvCodeList | varchar |  |  | SI | - |
| OECART_OIVAL_CareProvList | varchar |  |  | SI | - |
| OECART_OIVAL_ClinCondDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ColDate | varchar |  |  | SI | - |
| OECART_OIVAL_ColTime | varchar |  |  | SI | - |
| OECART_OIVAL_ContactCareProv | varchar |  |  | SI | - |
| OECART_OIVAL_CoveredByMainInsur | varchar |  |  | SI | - |
| OECART_OIVAL_CreateDate | date |  |  | SI | - |
| OECART_OIVAL_CreateTime | time |  |  | SI | - |
| OECART_OIVAL_DBLaboratoryCode | varchar |  |  | SI | - |
| OECART_OIVAL_DayCycle | varchar |  |  | SI | - |
| OECART_OIVAL_DefRptDur | varchar |  |  | SI | - |
| OECART_OIVAL_DefRptLoc | varchar |  |  | SI | - |
| OECART_OIVAL_DelayMeal | varchar |  |  | SI | - |
| OECART_OIVAL_DeptDesc | varchar |  |  | SI | - |
| OECART_OIVAL_DoNotDisp | varchar |  |  | SI | - |
| OECART_OIVAL_Doctor | varchar |  |  | SI | - |
| OECART_OIVAL_DrugDelRate | varchar |  |  | SI | - |
| OECART_OIVAL_DrugDelUnit | varchar |  |  | SI | - |
| OECART_OIVAL_EligibilityStatus | varchar |  |  | SI | - |
| OECART_OIVAL_EndDate | varchar |  |  | SI | - |
| OECART_OIVAL_Energy | varchar |  |  | SI | - |
| OECART_OIVAL_EnteredUOM | varchar |  |  | SI | - |
| OECART_OIVAL_EpisodeID | bigint |  |  | SI | - |
| OECART_OIVAL_Fat | varchar |  |  | SI | - |
| OECART_OIVAL_FeedString | varchar |  |  | SI | - |
| OECART_OIVAL_FlowQty | varchar |  |  | SI | - |
| OECART_OIVAL_FlowRateUnit | varchar |  |  | SI | - |
| OECART_OIVAL_FlowTime | varchar |  |  | SI | - |
| OECART_OIVAL_ForceGenEXE | varchar |  |  | SI | - |
| OECART_OIVAL_FreeText | varchar |  |  | SI | - |
| OECART_OIVAL_HL7Flag | varchar |  |  | SI | - |
| OECART_OIVAL_HidAuthPrescDetail | varchar |  |  | SI | - |
| OECART_OIVAL_HotReport | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2AcceptDisabilityInd | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2AcceptDisabilityText | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2AltBodyWeightObsDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2AntimicrobialApprovalNo | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ApprovalAdminReq | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPGDoseBased | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPGUOMDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2BPQuantity | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPRequiredByDate | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPRequiredByTime | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPReservationPeriod | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2BPReservationPeriodUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CNMItemNotes | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CNMNo | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CNMOverrideReason | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CNMStatusDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2CalDoseHTMLPlainText | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CalDoseHTMLRichText | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CalTemplateDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2CalTemplateParamsDR_DCTCTUOMDR | bigint |  | FK | SI | - |
| OECART_OIVAL_ITM2CalTemplateParamsDR_DCTDurationUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CalTemplateParamsDR_Details | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CalcDoseDetail | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CalcIVDose | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2Confidential | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2CopyCycleOrder | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2Derived | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DispenseType | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DistanceKms | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoNotSubstitute | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalLinkedNONTCLELabs | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalLinkedObs | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalLinkedTCLELabs | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalProtocolBase | double |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalRangeDesc | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalRangeFrom | double |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalRangeTo | double |  |  | SI | - |
| OECART_OIVAL_ITM2DoseCalRangeUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseInML | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DoseRecalPermitted | bit |  |  | SI | - |
| OECART_OIVAL_ITM2DropsMin | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DuplServOverrideReason | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DurationType | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DurationUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2DurationValue | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2EPrescItemNotes | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2EPrescNo | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2EPrescOverrideReason | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2EPrescStatus | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2EquipmentId | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2Event | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ExpiryDate | date |  |  | SI | - |
| OECART_OIVAL_ITM2ExternalDocFiscalCode | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ExternalPaperPrescNo | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ExternalPrescriptionID | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2FieldQuantity | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2FluidConsistModDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2FluidVolumeRestrDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2FoodTextureModDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2FreeTextFreqUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2FreeTextFreqValue | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2IVContTotalDose | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2IVContTotalDoseUnitDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2IVDose | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2IVUnitDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2InHospService | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2Indication | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2InfusTypeEndDate | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2InfusTypeEndTime | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2LSPNum | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2LateralityDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2Link | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2LoanRetDate | date |  |  | SI | - |
| OECART_OIVAL_ITM2LostLoanItem | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2MRMedLinkedOrder | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2MaxDeliveryRate | double |  |  | SI | - |
| OECART_OIVAL_ITM2MedicationDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2MinDeliveryRate | double |  |  | SI | - |
| OECART_OIVAL_ITM2MinDoseQty | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2MinPhQtyOrd | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2MultPrSamePatSameDocSameDay | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2MultProcNotes | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2NFMICategDepart | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2NewPRNMaxDose24hrs | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2NewPRNMaxDose24hrsUnitDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2NonPBSQuanUOMDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2NonPBSQuantity | double |  |  | SI | - |
| OECART_OIVAL_ITM2O2AdminOver | double |  |  | SI | - |
| OECART_OIVAL_ITM2O2AdminOverUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2O2ContDelivery | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2O2DeliveryMethodDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2O2MaxRate | double |  |  | SI | - |
| OECART_OIVAL_ITM2O2Rate | double |  |  | SI | - |
| OECART_OIVAL_ITM2O2RateCalMethod | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2O2RateUOMDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2OrderVersion | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2OverUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2OverValue | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2OverrideIVUnitDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2OverrideQtyBaseUOM | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PBSAuthorityApprovalCode | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PBSAuthorityApprovalPending | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PBSAuthorityNumber | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PBSNonPBSFlag | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PBSPrescribingRuleBenefitDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2PBSQuantity | double |  |  | SI | - |
| OECART_OIVAL_ITM2PBSRepeats | double |  |  | SI | - |
| OECART_OIVAL_ITM2PBSRestrictionDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2PBSStreamlineNumber | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PCABolusDose | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PCADoseInterval | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PCADoseUOMDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2PCALoadingDose | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PCAMaxDoseHours | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PCAMaximumDose | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PHCIVAdminSetDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2PRNFlag | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PRNMaxDoseHrs | double |  |  | SI | - |
| OECART_OIVAL_ITM2PRNMaxDoseNumHrs | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PatchApplyAt | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PatchDurUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PatchDuration | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PatchRemoveAfter | integer |  |  | SI | - |
| OECART_OIVAL_ITM2PatchRemoveAt | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PathwayItemDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2PatientHeight | double |  |  | SI | - |
| OECART_OIVAL_ITM2PatientWeight | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2PerIVGuideline | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ProcActivityDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2ProcPhaseDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2ProgBolusDose | double |  |  | SI | - |
| OECART_OIVAL_ITM2ProgBolusDoseUOMDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2ProgBolusFrequency | integer |  |  | SI | - |
| OECART_OIVAL_ITM2ProgBolusFrequencyUnit | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ReasonForModificDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2ReasonForVariance | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2RecalcDoseBeforeAdmin | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2RegAnestheticsProg | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2RestrictOverrideCde | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2Rule3ExemptInd | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2S4B3ExemptInd | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2SameServMultTimesSameDay | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2SelfDeemedCode | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ServPartNormAftercare | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2ServiceText | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2TargetSPO2DR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2TeleConsult | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2TempMedicareNumber | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2TimeCriticalWindow | double |  |  | SI | - |
| OECART_OIVAL_ITM2TreatmentLocCde | varchar |  |  | SI | - |
| OECART_OIVAL_ITM2VarReasonDoseDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2VarReasonDoseDuratDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2VarReasonDuratDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2VarReasonFreqDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2VarReasonRateDoseDR | varchar |  | FK | SI | - |
| OECART_OIVAL_ITM2VarReasonRateDuratDR | varchar |  | FK | SI | - |
| OECART_OIVAL_IVCalcMeth | varchar |  |  | SI | - |
| OECART_OIVAL_IVType | varchar |  |  | SI | - |
| OECART_OIVAL_IVUnit | varchar |  |  | SI | - |
| OECART_OIVAL_IncompReas | varchar |  |  | SI | - |
| OECART_OIVAL_IndicateTransfusion | varchar |  |  | SI | - |
| OECART_OIVAL_Interval | varchar |  |  | SI | - |
| OECART_OIVAL_LBTSBPNumberOfUnits | varchar |  |  | SI | - |
| OECART_OIVAL_LBTSBPQuantity | varchar |  |  | SI | - |
| OECART_OIVAL_LBTSBPRecentTransfusionPregnancy | varchar |  |  | SI | - |
| OECART_OIVAL_LBTSBPReservationPeriod | varchar |  |  | SI | - |
| OECART_OIVAL_LBTSBPReservationPeriodUnit | varchar |  |  | SI | - |
| OECART_OIVAL_LBTSConfidential | varchar |  |  | SI | - |
| OECART_OIVAL_LabSpecSites | varchar |  |  | SI | - |
| OECART_OIVAL_LabVolume | varchar |  |  | SI | - |
| OECART_OIVAL_LabelText | varchar |  |  | SI | - |
| OECART_OIVAL_Linked | varchar |  |  | SI | - |
| OECART_OIVAL_LinkedItmID | varchar |  |  | SI | - |
| OECART_OIVAL_MSOEOrdItemID | varchar |  |  | SI | - |
| OECART_OIVAL_MealType | varchar |  |  | SI | - |
| OECART_OIVAL_MeteredDose | varchar |  |  | SI | - |
| OECART_OIVAL_Modifiers | varchar |  |  | SI | - |
| OECART_OIVAL_NeedleGauge | varchar |  |  | SI | - |
| OECART_OIVAL_NeedleType | varchar |  |  | SI | - |
| OECART_OIVAL_NewOrdItemID | varchar |  |  | SI | - |
| OECART_OIVAL_NextDoseDate | varchar |  |  | SI | - |
| OECART_OIVAL_NextDoseTime | varchar |  |  | SI | - |
| OECART_OIVAL_NotifyClinician | varchar |  |  | SI | - |
| OECART_OIVAL_NotifyMod | varchar |  |  | SI | - |
| OECART_OIVAL_OECPRDesc | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIActivity | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIAnnotateDR | bigint |  | FK | SI | - |
| OECART_OIVAL_OEORIApprovalDate | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIApprovalInd | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIApprovalNo | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIApprovalTime | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIApprovedBy | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIAutologousBloodReq | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIBBTAG1 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIBBTAG2 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIBBTAG3 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIBBTAG4 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIBBTAG5 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIBillDesc | varchar |  |  | SI | - |
| OECART_OIVAL_OEORICompXMatchReq | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIConsult | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIContOrderAfterDischarge | varchar |  |  | SI | - |
| OECART_OIVAL_OEORICurrRepeatNumber | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIDSReportFlag | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIDepProcNotes | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIDoseQty | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIEndDate | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIEndTime | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIFreqDelay | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIInsBillConditDR | varchar |  | FK | SI | - |
| OECART_OIVAL_OEORIItemGroup | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIItmMastDR | varchar |  | FK | SI | - |
| OECART_OIVAL_OEORILab1 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORILab2 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORILabEpisodeNo | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIMaxNumberOfRepeats | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIMaxRepeats | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIPatConsentObtained | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIPrescRepExpiryDate | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIPrescRepNumberDays | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIPrice | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIQty | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIQtyPackUOM | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIRBResourceDR | varchar |  | FK | SI | - |
| OECART_OIVAL_OEORIReasOrdCMVNegBlood | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIRefDocDR | varchar |  | FK | SI | - |
| OECART_OIVAL_OEORIRemarks | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIResultDSReportFlag | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIRoute | varchar |  |  | SI | - |
| OECART_OIVAL_OEORISpecialty | varchar |  |  | SI | - |
| OECART_OIVAL_OEORISttDat | varchar |  |  | SI | - |
| OECART_OIVAL_OEORISttTim | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIText1 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIText2 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIText3 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIText4 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIUserGroupAdd | bigint |  |  | SI | - |
| OECART_OIVAL_OEORIVarianceReasonDR | varchar |  | FK | SI | - |
| OECART_OIVAL_OEORIView | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIWhoGoWhere | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo1 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo2 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo3 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo4 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo5 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo6 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo7 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo8 | varchar |  |  | SI | - |
| OECART_OIVAL_OEORIYesNo9 | varchar |  |  | SI | - |
| OECART_OIVAL_OERemoteDutyID | bigint |  |  | SI | - |
| OECART_OIVAL_ORDERSETID | varchar |  |  | SI | - |
| OECART_OIVAL_ORNCDesc | varchar |  |  | SI | - |
| OECART_OIVAL_OSTATDesc | varchar |  |  | SI | - |
| OECART_OIVAL_OperationID | varchar |  |  | SI | - |
| OECART_OIVAL_OrdSetDateID | varchar |  |  | SI | - |
| OECART_OIVAL_OrderID | varchar |  |  | SI | - |
| OECART_OIVAL_OverseerUser | bigint |  |  | SI | - |
| OECART_OIVAL_PHCDUDesc1 | varchar |  |  | SI | - |
| OECART_OIVAL_PHCFRDesc1 | varchar |  |  | SI | - |
| OECART_OIVAL_PHCINDesc1 | varchar |  |  | SI | - |
| OECART_OIVAL_PRNIndication | varchar |  |  | SI | - |
| OECART_OIVAL_PRNMaxDose24hr | varchar |  |  | SI | - |
| OECART_OIVAL_PRNTotNumDoseAllow | varchar |  |  | SI | - |
| OECART_OIVAL_PasteurisedFood | varchar |  |  | SI | - |
| OECART_OIVAL_PathwayId | varchar |  |  | SI | - |
| OECART_OIVAL_PatientLoc | varchar |  |  | SI | - |
| OECART_OIVAL_Payor | varchar |  |  | SI | - |
| OECART_OIVAL_PhoneOrder | varchar |  |  | SI | - |
| OECART_OIVAL_Plan | varchar |  |  | SI | - |
| OECART_OIVAL_PortableEquiptRequired | varchar |  |  | SI | - |
| OECART_OIVAL_PrefConMethod | varchar |  |  | SI | - |
| OECART_OIVAL_PreparationTime | varchar |  |  | SI | - |
| OECART_OIVAL_Protein | varchar |  |  | SI | - |
| OECART_OIVAL_REMODCareProvText | varchar |  |  | SI | - |
| OECART_OIVAL_REMODContactNoText | varchar |  |  | SI | - |
| OECART_OIVAL_REMODDMOSeenByDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODDMOSeenByTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODHospNotifDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODHospNotifTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODPlaceOfOrder | varchar |  |  | SI | - |
| OECART_OIVAL_REMODPlanCallBackBy | varchar |  |  | SI | - |
| OECART_OIVAL_REMODPlanCallBackDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODPlanCallBackTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRecCareProv | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRecCareProvText | varchar |  |  | SI | - |
| OECART_OIVAL_REMODReferPrio | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRemarks | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetAcceptDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetAcceptTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetArriveDestDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetArriveDestTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetDepartBaseDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetDepartBaseTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetDepartDestDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetDepartDestTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetETABaseDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetETABaseTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetPlanDate | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetPlanTime | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetPrio | varchar |  |  | SI | - |
| OECART_OIVAL_REMODRetTransp | varchar |  |  | SI | - |
| OECART_OIVAL_REMODTransferLoc | varchar |  |  | SI | - |
| OECART_OIVAL_REMODTriaged | varchar |  |  | SI | - |
| OECART_OIVAL_REMODType | varchar |  |  | SI | - |
| OECART_OIVAL_RMDuration | varchar |  |  | SI | - |
| OECART_OIVAL_RMFrequency | varchar |  |  | SI | - |
| OECART_OIVAL_RadNo | varchar |  |  | SI | - |
| OECART_OIVAL_ReceivedDate | varchar |  |  | SI | - |
| OECART_OIVAL_ReceivedTime | varchar |  |  | SI | - |
| OECART_OIVAL_RefDoctorList | varchar |  |  | SI | - |
| OECART_OIVAL_ReqForTheat | varchar |  |  | SI | - |
| OECART_OIVAL_RequestedDate | varchar |  |  | SI | - |
| OECART_OIVAL_RequestedTime | varchar |  |  | SI | - |
| OECART_OIVAL_RiceType | varchar |  |  | SI | - |
| OECART_OIVAL_RouteAdmin | varchar |  |  | SI | - |
| OECART_OIVAL_Session | varchar |  |  | SI | - |
| OECART_OIVAL_StartEndMealType | varchar |  |  | SI | - |
| OECART_OIVAL_SteriliseUtensils | varchar |  |  | SI | - |
| OECART_OIVAL_TempStat | varchar |  |  | SI | - |
| OECART_OIVAL_TheatBookDate | varchar |  |  | SI | - |
| OECART_OIVAL_USERID | bigint |  |  | SI | - |
| OECART_OIVAL_UnitHrs | varchar |  |  | SI | - |
| OECART_OIVAL_UnitsColl | varchar |  |  | SI | - |
| OECART_OIVAL_Volume | varchar |  |  | SI | - |
| OECART_OIVAL_formAltReasonDR | varchar |  | FK | SI | - |
| OECART_OIVAL_hiddenLBEPClinicalConditions | varchar |  |  | SI | - |
| OECART_OIVAL_lstEmbedOSExcluded | varchar |  |  | SI | - |
| OECART_OIVAL_lstOSExclusions | varchar |  |  | SI | - |
| OECART_OIVAL_mDate | varchar |  |  | SI | - |
| OECART_OIVAL_mTime | varchar |  |  | SI | - |
| OECART_OIVAL_prosthetic2 | varchar |  |  | SI | - |
| OECART_OIVAL_refclincode | varchar |  |  | SI | - |
| OECART_OIVAL_teeth | varchar |  |  | SI | - |
| OECART_OIVAL_urgent | varchar |  |  | SI | - |
| OECART_OIVAL_zProsthetics | varchar |  |  | SI | - |
| OECART_OIVAL_zSpecSites | varchar |  |  | SI | - |
| OECART_OffsetExecID | varchar |  |  | SI | OEOrdExec row ID to the offset order item in the s... |
| OECART_OffsetItemID | varchar |  |  | SI | OEOrdItem row ID to the offset order item in the s... |
| OECART_OffsetType | varchar |  |  | SI | OffsetType in the Sequence Plan |
| OECART_OffsetUnit | varchar |  |  | SI | OffsetUnit in the Sequence Plan |
| OECART_OffsetValue | double |  |  | SI | OffsetValue in the Sequence Plan |
| OECART_OrdSetDateItemID | varchar |  |  | SI | ITM2OrdSetDateItemDR of original order item |
| OECART_OrderItemRestored | bit |  |  | SI | Whether this cart item is associated with an order... |
| OECART_Profile_DR | bigint |  | FK | SI | Logon Access Profile at time of Creation |
| OECART_STATDoseOrderItemID | varchar |  |  | SI | ID of STAT dose order item attached to original or... |
| OECART_STATDoseOrderItemParentID | varchar |  |  | SI | ID of parent order item, if original order item is... |
| OECART_Time | time |  |  | NO | Updated Time |
| OECART_Type | varchar |  |  | SI | Order Cart record created by system autogenerated,... |
| OECART_User_DR | bigint |  | FK | NO | Des Ref to SSUSR
User Created Order |
| OECART_Version | varchar |  |  | NO | Version |
| OECART_WorkFlow_DR | bigint |  | FK | SI | The order entry workflow |
| OECART_WorkFlow_InMainWin | bit |  |  | SI | Was Order Entry displayed in the main window (=1) ... |
| Q29Q1 | - |  |  | SI | Movement |
| Q29Q2 | - |  |  | SI | Strength - Right |
| Q29Q3 | - |  |  | SI | Strength - Left |
| Q29Q4 | - |  |  | SI | AROM - Right |
| Q29Q5 | - |  |  | SI | AROM - Left |
| Q29Q6 | - |  |  | SI | PROM - Right |
| Q29Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*