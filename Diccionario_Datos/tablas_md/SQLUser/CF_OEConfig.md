# SQLUser.CF_OEConfig

**Schema:** SQLUser
**Columnas:** 351
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OECF_RowID | bigint | PK |  | NO | - |
| ChildQ73DR | - |  |  | SI | Child Reference: Programa de Salud |
| OECF_ATCInterface | varchar |  |  | SI | Send details to Auto. Tablet Counter |
| OECF_AcceptIP | varchar |  |  | SI | OECF_AcceptIP |
| OECF_AcceptOP | varchar |  |  | SI | Accept OP |
| OECF_AdmMedRecDMDLevelForCont | varchar |  |  | SI | Admission Medication Reconciliation Default Prescr... |
| OECF_AdmMedRecForceFormAlt | varchar |  |  | SI | Admission Medication Reconciliation Force Formular... |
| OECF_AdminIsLateTime | double |  |  | SI | Admin late Time (will mark the administration as '... |
| OECF_AdminLock | double |  |  | SI | AdminLock  |
| OECF_AdminOffsetTime | double |  |  | SI | PRN Offset Time (allows the PRN adminsitration x m... |
| OECF_AdministrationOffsetTime | double |  |  | SI | Administration Offset time |
| OECF_AdmixAutoResolve | varchar |  |  | SI | Admix Auto Resolve |
| OECF_AgeFrom | double |  |  | SI | Age From |
| OECF_AgeTo | double |  |  | SI | Age To |
| OECF_AlertSTATDoseLinkedOrders | varchar |  |  | SI | Display alert message when applying STAT dose to l... |
| OECF_AllocateOrderToBatch | varchar |  |  | SI | Allocate Order To Batch |
| OECF_AllowActiveOrdersAdmDates | varchar |  |  | SI | Allow definition ActiveOrders as of AdmDates |
| OECF_AllowConcurrentOrders | varchar |  |  | SI | AllowConcurrentOrders |
| OECF_AllowDrugModifPharmAccept | varchar |  |  | SI | Allow modification of Drug Orders after Pharmacy A... |
| OECF_AllowNegStockAutoPacking | varchar |  |  | SI | Allow Neg Stock for AutoPacking |
| OECF_AllowPRNWithoutFreq | varchar |  |  | SI | Allow PRN orders with no frequency |
| OECF_AllowPackUOM | varchar |  |  | SI | Allow to change Pack UOM |
| OECF_AllowPlaceOrderOutsideEpisDates | varchar |  |  | SI | AllowPlaceOrderOutsideEpisDates |
| OECF_ApplyAddOnLabOrder | varchar |  |  | SI | Apply Add On lab order function |
| OECF_ApplyPreciseAdmixCalculationForNurses | varchar |  |  | SI | Apply Precise Admixture Calculation for Nurses |
| OECF_AutoBackspace | double |  |  | SI | Auto Backspace |
| OECF_AutoPacking | varchar |  |  | SI | Auto Packing |
| OECF_AutoResolve | varchar |  |  | SI | AutoResolve |
| OECF_BillAdminDrugs | varchar |  |  | SI | BillAdminDrugs |
| OECF_BulkAdministeredStatus_DR | bigint |  | FK | SI | Bulk Administration: Administered Status |
| OECF_BulkNotAdministeredStatus_DR | bigint |  | FK | SI | Bulk Administration: Not Administered Status |
| OECF_BypassPBSMedicareDVAChecking | varchar |  |  | SI | Bypass Medicare/DVA checking for prescribing under... |
| OECF_CMVTest_DR | varchar |  | FK | SI | Des Ref ARCIM |
| OECF_CTProfileParams_DR | bigint |  | FK | SI | Des Ref to epr.CTProfileParams |
| OECF_CartAutoSave | varchar |  |  | SI | AutoSave Inactive Items to Interim Cart |
| OECF_CartExpiryDays | integer |  |  | SI | Days to Purge Cart Items |
| OECF_CartExpiryHours | integer |  |  | SI | Hours to Purge Cart Items |
| OECF_ChangeLinkedOnUpdate | varchar |  |  | SI | Change Linked On Update |
| OECF_CheckOrdersCovered | varchar |  |  | SI | Check if Orders are Covered |
| OECF_CheckPrice | varchar |  |  | SI | Logic for when no Price defined |
| OECF_ChkLocQty | varchar |  |  | SI | Check Location Quantity with Receiving Dept. |
| OECF_ClearOrdersOnUpdate | varchar |  |  | SI | Clear Orders On Update |
| OECF_Copyright | varchar |  |  | SI | Copyright |
| OECF_Create1OrderPerSpecimen | varchar |  |  | SI | Create 1 Order Per Specimen |
| OECF_Create1OrderPerToothFace | varchar |  |  | SI | Create 1 Order Per Tooth Face |
| OECF_CreateReturnQueueDisch | varchar |  |  | SI | Create Return Queue upon Discharge |
| OECF_CustAutoResMethod | varchar |  |  | SI | Custom Auto Resolve Method |
| OECF_DatesRangeAddOnValid | integer |  |  | SI | Dates Range for Add On Validation |
| OECF_DaysToRemainAtPacked | double |  |  | SI | DaysToRemainAtPacked |
| OECF_DaysToRemainAtUncollected | double |  |  | SI | DaysToRemainAtUncollected |
| OECF_DefRefundReason_DR | bigint |  | FK | SI | Des Ref DefRefundReason |
| OECF_DefaultCheckBsUnselect | varchar |  |  | SI | Default Checkboxes on OS list unselect |
| OECF_DefaultDispLoc_DR | bigint |  | FK | SI | Default Disp Location |
| OECF_DefaultDosingGap | integer |  |  | SI | Default Dosing Gap Days |
| OECF_DefaultOSItemBillingPriceBlank | varchar |  |  | SI | DefaultOSItemBillingPriceBlank |
| OECF_DefaultOrderGroup | varchar |  |  | SI | Default Order Group FIELD NO LONGER USED TC-8813 |
| OECF_Description | varchar |  |  | SI | Configuration Description |
| OECF_DiagWarning | varchar |  |  | SI | Diagnosis Warning Message Logic |
| OECF_DisMedRecDMDLevelForCont | varchar |  |  | SI | Discharge Medication Reconciliation Default Prescr... |
| OECF_DisMedRecForceFormAlt | varchar |  |  | SI | Discharge Medication Reconciliation Force Formular... |
| OECF_DisableAddForQtyBlank | varchar |  |  | SI | DisableAddForQtyBlank |
| OECF_DisableExecuteNotArrAppt | varchar |  |  | SI | Disable Execution Not Arrived Appt |
| OECF_DischargeOrderStatusChangeReason_DR | bigint |  | FK | SI | Reason for order status change upon discharge |
| OECF_Disclaim | varchar |  |  | SI | Disclaim |
| OECF_DiscontExecutedOrder | varchar |  |  | SI | Allow Discontinue Executed Order |
| OECF_DiscontinueOverlapExTime | varchar |  |  | SI | Discontinue Overlapping Execution Time |
| OECF_DisplayDuplDosageTextBox | varchar |  |  | SI | Display Duplicate Dosage TextBox |
| OECF_DisplayOIDescOnPharmWB | varchar |  |  | SI | Display OI description on Pharmacy WB |
| OECF_DisplayRefundReason | varchar |  |  | SI | Display Refund Reason in stock return |
| OECF_DontAggregateSpecimens | varchar |  |  | SI | DontAggregateSpecimens |
| OECF_DoseToleranceBounds | varchar |  |  | SI | Medication Dose Adjustment Tolerance Bounds |
| OECF_DoseTolerancePercent | integer |  |  | SI | Medication Dose Adjustment Tolerance Percentage |
| OECF_DownTimeadminStat_DR | bigint |  | FK | SI | Down time administration status |
| OECF_DrugRegAutoSetManItems | varchar |  |  | SI | Auto set drug register for manufactured items |
| OECF_DrugRegDrugMan | varchar |  |  | SI | Drug Register for Drug Manufacturing |
| OECF_DrugRegPharmPack | varchar |  |  | SI | Drug Register for Pharmacy Packing |
| OECF_DrugRegPharmReturn | varchar |  |  | SI | Drug Register for Pharmacy Return |
| OECF_DrugRegPharmUnpack | varchar |  |  | SI | Drug Register for Pharmacy Unpacking |
| OECF_DrugRegStockAdjustment | varchar |  |  | SI | Drug Register for Stock Adjustment |
| OECF_DrugRegStockConsumption | varchar |  |  | SI | Drug Register for Stock Consumption |
| OECF_DrugRegStockDisposal | varchar |  |  | SI | Drug Register for Stock Disposal |
| OECF_DrugRegStockIssue | varchar |  |  | SI | Drug Register for Stock Issue |
| OECF_DrugRegStockIssueReturn | varchar |  |  | SI | Drug Register for Stock Issue Return |
| OECF_DrugRegStockReceive | varchar |  |  | SI | Drug Register for Stock Receive |
| OECF_DrugRegStockReplenish | varchar |  |  | SI | Drug Register for Stock Replenish |
| OECF_DrugRegStockReturn | varchar |  |  | SI | Drug Register for Stock Return |
| OECF_DrugRegStockTakeAdjustment | varchar |  |  | SI | Drug Register for Stock take Adjustment |
| OECF_DrugRegStockTransfer | varchar |  |  | SI | Drug Register for Stock Transfer |
| OECF_Drugfile | varchar |  |  | SI | StandardType Drugfile - used for integrated Drug U... |
| OECF_Duration_DR | bigint |  | FK | SI | Des Ref Duration |
| OECF_EditBilledScripts | varchar |  |  | SI | Allow Edit OF billed Outpatient Scripts |
| OECF_EditNotes | varchar |  |  | SI | Edit Notes |
| OECF_EnableSingleNodesIVContOrd | varchar |  |  | SI | Enable Single Nodes for IV Continuous Orders |
| OECF_EnabledPharmRev | varchar |  |  | SI | Enabled Pharmacy Review |
| OECF_ExcludeOngoingExecOrdIntAlert | varchar |  |  | SI | Exclude Executed orders with Ongoing Duration from... |
| OECF_ExePhDischOrdersOnDisch | varchar |  |  | SI | ExePhDischOrdersOnDisch |
| OECF_ExecuteConfirmation | varchar |  |  | SI | Execute Confirmation |
| OECF_ExecuteFutureOrders | varchar |  |  | SI | Execute Future Orders |
| OECF_ExecuteLabOrder | varchar |  |  | SI | Execute Lab Order before sending to Labtrak |
| OECF_ExecuteUponCollection | varchar |  |  | SI | ExecuteUponCollection |
| OECF_ExternalMonographPath | varchar |  |  | SI | ExternalMonographPath |
| OECF_ExternalMonographPathUnix | varchar |  |  | SI | OECFExternalMonographPathUnix |
| OECF_ExternalMonographURL | varchar |  |  | SI | ExternalMonographURL |
| OECF_ExtraPercentPerBag | integer |  |  | SI | Allowed extra percentage of fluid per solvent bag |
| OECF_FormAltHideGeneric | varchar |  |  | SI | FormAltHideGeneric |
| OECF_FormAltMatchLevel | varchar |  |  | SI | FormAltMatchLevel |
| OECF_Frequency_DR | bigint |  | FK | SI | Des Ref to Frequency |
| OECF_GenDiffLabEpisNoAutoRecv | varchar |  |  | SI | GenDiffLabEpisNoAutoRecv |
| OECF_GenerateAMP | varchar |  |  | SI | Generate AMP |
| OECF_GenerateAMPP | varchar |  |  | SI | Generate AMPP |
| OECF_GenerateExecSchedOutpat | varchar |  |  | SI | Generate Execution Schedule for Outpatients |
| OECF_GenerateStockItem | varchar |  |  | SI | Generate Stock Item |
| OECF_GenerateTF | varchar |  |  | SI | Generate TF |
| OECF_GenerateVMP | varchar |  |  | SI | Generate VMP |
| OECF_GenerateVMPP | varchar |  |  | SI | Generate VMPP |
| OECF_GenerateVTM | varchar |  |  | SI | Generate VTM |
| OECF_GenericPrescribing | varchar |  |  | SI | GenericPrescribing |
| OECF_GenericsOnly | varchar |  |  | SI | GenericsOnly |
| OECF_GrpCumTestSet | varchar |  |  | SI | Group cumulative display by test set |
| OECF_HoursRangeAddOnValid | integer |  |  | SI | Hours Range for Add On Validation |
| OECF_IPPLateAdminHonorOrdDateTime | varchar |  |  | SI | IV Continuous, PCA and PRN late administration to ... |
| OECF_IVExpiryDays | integer |  |  | SI | Days to expiry of manufactured IVs |
| OECF_IVExpiryHours | integer |  |  | SI | Hours to expiry of manufactured IVs |
| OECF_IgnorePayorPlanRest | varchar |  |  | SI | Ignore Payor/Plan Restrictions arrive appt |
| OECF_IgnorePriorityDEf | varchar |  |  | SI | IgnorePriorityDEf |
| OECF_InpatientBilling | varchar |  |  | SI | InPatient Billing Configuration |
| OECF_Issue | varchar |  |  | SI | Issue |
| OECF_KeepPriorDateSession | varchar |  |  | SI | Keep Priorty,StartDate/Time dur Order Session |
| OECF_Kinetics | varchar |  |  | SI | Kinetics |
| OECF_Limit | varchar |  |  | SI | Limit |
| OECF_ManualIVFluidBalanceEntry | varchar |  |  | SI | Manual IV Fluid Balance entry |
| OECF_ManualVerifLabOrders | varchar |  |  | SI | Manual Verif LabOrders |
| OECF_ManufCheckDisposalConsumptionReason_DR | bigint |  | FK | SI | Manufacture Check Disposal: Reason for consumption... |
| OECF_ManufCheckDisposalReasonAdjustment_DR | bigint |  | FK | SI | Manufacture Check Disposal: Reason for adjustment... |
| OECF_MarkOrderUnverifOnRecoll | varchar |  |  | SI | MarkOrderAsUnverifiedOnRecollection  |
| OECF_MinCharsPartialSearch | integer |  |  | SI | Minimum number of characters for partial string ma... |
| OECF_NIVExpiryDays | integer |  |  | SI | Days to expiry of manufactured Non-IVs |
| OECF_NIVExpiryHours | integer |  |  | SI | Hours to expiry of manufactured Non-IVs |
| OECF_NewEpisodeForDifferentHospital | varchar |  |  | SI | Create New Episode for Different Hospital Receivin... |
| OECF_NoAdjustSubNodePRNFreqMin | double |  |  | SI | Do Not Adjust Subsequent Nodes If the PRN Order Fr... |
| OECF_NoDCOrdersOnNurseWB | varchar |  |  | SI | NoDCOrdersOnNurseWB |
| OECF_NoDefaultPatLocOnOE | varchar |  |  | SI | Do Not Default Patient Location on OE |
| OECF_NoDisplayEpisNoForNormal | varchar |  |  | SI | NoDisplayEpisNoForNormal |
| OECF_NoIntCheckBetweenIPandDIS | varchar |  |  | SI | Omit interaction checking between inpatient and di... |
| OECF_NoShowLabEpForAllOrdersIP_EStat | varchar |  |  | SI | Do Not ShowLabEpForAllOrdersIP_EStat |
| OECF_NoShowReorderNurseWB | varchar |  |  | SI | do Not Show Reorder warning on Nurse WB |
| OECF_NoTHPDCheckBetweenIPandDIS | varchar |  |  | SI | Omit therapeutic duplication checking between inpa... |
| OECF_NoWordResultCode | varchar |  |  | SI | Do Not Use Word Result Code |
| OECF_NotUseOrderLineCaseFormatting | varchar |  |  | SI | Do Not Use Order Line Case Formatting |
| OECF_NumOfDaysGenExecForInHospitalPatients | integer |  |  | SI | Number of Days for Administrations generation for ... |
| OECF_NumOfDaysGenExecForOutOfHospitalPatients | integer |  |  | SI | Number of Days for Administrations generation for ... |
| OECF_NumOfIngredientsToSkipGenericKeywGen | integer |  |  | SI | Number of Ingredients to Skip Keyword Generation f... |
| OECF_NumberOfOrdersAllowedSameGroup | double |  |  | SI | Number Of Orders Allowed for the Same Group |
| OECF_OEComponent | varchar |  |  | SI | Order Entry Component |
| OECF_OrdCatAutoItemCreation_DR | bigint |  | FK | SI | Des Ref OECOrderCategory |
| OECF_OrderAdminStatus_DR | bigint |  | FK | SI | Des Ref to OECOrderAdminStatus |
| OECF_OrderCovContractBillAllPayAgreem | varchar |  |  | SI | Check if Order Is Covered - Contract Billing All P... |
| OECF_OrderEntryObservationGroup_DR | bigint |  | FK | SI | Des Ref to MRCObservationGroup |
| OECF_OrderLineWrap | varchar |  |  | SI | Order Line Wrapping  |
| OECF_OrderReviewModel | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| OECF_OrdersToRecLoc | varchar |  |  | SI | Send orders to Receiving Location |
| OECF_OverDueAdminTimeIntv | integer |  |  | SI | OverDueAdminTimeIntv |
| OECF_OverDueNodesAdmStat_DR | bigint |  | FK | SI | Des Ref OECOrderAdminStatus, for OverDue Nodes |
| OECF_PBSInformation | varchar |  |  | SI | PBSInformation |
| OECF_PBSPrescriptionReport | bigint |  |  | SI | PBS Printing Report |
| OECF_PRNIndicationMandatory | varchar |  |  | SI | PRNIndicationMandatory |
| OECF_PRNIndicationMandatoryForMedAdmin | varchar |  |  | SI | PRNIndicationMandatoryForMedAdmin |
| OECF_PackAllDispToFirstExec | varchar |  |  | SI | PackAllDispToFirstExec |
| OECF_PartialStringMatchOE | varchar |  |  | SI | Allow partial string match for searches at order e... |
| OECF_PatLeaveOrderAdmStatus_DR | bigint |  | FK | SI | Des Ref PatLeaveOrderAdmStatus |
| OECF_PerProtOrderAdmStatus_DR | bigint |  | FK | SI | As per Protocol Des Ref OrderAdmStatus |
| OECF_PharmacyItemNoStock | varchar |  |  | SI | Allow Pharmacy Item Not Linked to Stock Item |
| OECF_PickBlankExpBatchLast | varchar |  |  | SI | PickBlankExpBatchLast |
| OECF_PrescriptionGenerated | varchar |  |  | SI | Prescription Generated |
| OECF_PreventMultiResultTypes | varchar |  |  | SI | Prevent Creation of Multiple Result Types |
| OECF_Price | varchar |  |  | SI | Show Order Price |
| OECF_PrintDelLabelOnUpdate | varchar |  |  | SI | Print Result Delivery Label On Update |
| OECF_PrintPresc | varchar |  |  | SI | Automatic Print Prescription on Acceptance |
| OECF_PriorUpdateRecLoc | varchar |  |  | SI | Update to Order Priority Updates Receiving Locatio... |
| OECF_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| OECF_RMQueue | varchar |  |  | SI | Remove Queue |
| OECF_RapidOrderAdmStatus_DR | bigint |  | FK | SI | Des Ref RapidOrderAdmStatus |
| OECF_RapidOrderDiscReas_DR | bigint |  | FK | SI | One Touch Order Discontinue Reason |
| OECF_RapidOrderReverseAdmReas_DR | bigint |  | FK | SI | One Touch Order Reverse Administration Reason |
| OECF_Reject | varchar |  |  | SI | Reject |
| OECF_RespectVolumeForIntermittentInfusion | varchar |  |  | SI | Respect Volume for Intermittent Infusion in Nurse ... |
| OECF_ReviewDischargeReason_DR | bigint |  | FK | SI | Des Ref to MRCVarianceReason |
| OECF_RoundDoseQty | varchar |  |  | SI | Round Dose Qty |
| OECF_RouteChangeVariance_DR | bigint |  | FK | SI | Change Route/Form Variance Reason |
| OECF_SameStartDateWarning | varchar |  |  | SI | Same Start Date Warning |
| OECF_SaveOrderCategory | varchar |  |  | SI | Save Order Category |
| OECF_SendHospitalCodeToLab | varchar |  |  | SI | Send Hospital Code To LabTrak |
| OECF_SendOrderingDoctorToLab | varchar |  |  | SI | Send Ordering Doctor To Labtrak |
| OECF_SendRecLocToLab | varchar |  |  | SI | SendRecLocToLab |
| OECF_SendWebNRtoLabTrak | varchar |  |  | SI | Send Web NR to LabTrak |
| OECF_ShowAllPharmStatCollectQ | varchar |  |  | SI | Show all pharmacy statuses in Collect queue |
| OECF_ShowAllergy_DSS_QA | varchar |  |  | SI | Show Allergy_DSS_QA |
| OECF_ShowDeliveryInfoOnPin | varchar |  |  | SI | Show Delivery Info On Pin |
| OECF_ShowDisOrdersResults | varchar |  |  | SI | Show Discontinued Orders with Results |
| OECF_ShowInstructionAs | varchar |  |  | SI | Show Instruction As |
| OECF_ShowSnomedCodes | varchar |  |  | SI | Show Snomed Codes |
| OECF_ShowWarnOIDepOverCT | varchar |  |  | SI | Show Warning as on OI Deptmt Override ct |
| OECF_SignOffDisclaimerDays | double |  |  | SI | SignOffDisclaimerDays |
| OECF_SystemFluidBalanceCorrectionReason_DR | bigint |  | FK | SI | Reason for System Fluid Balance Correction |
| OECF_TCOrISM | varchar |  |  | SI | TrakCare or Integrated Stock Management |
| OECF_TPN | varchar |  |  | SI | TPN |
| OECF_TextForDeletedTestItem | varchar |  |  | SI | TextForDeletedTestItem |
| OECF_TotalContainerVolMandatoryForIVContAdmix | varchar |  |  | SI | Total Container Volume Mandatory for IV Continuous... |
| OECF_UpdateDate | date |  |  | SI | Last Update Date |
| OECF_UpdateTime | time |  |  | SI | Last Update Time |
| OECF_UpdateUser_DR | bigint |  | FK | SI | Last Update User |
| OECF_UseCombinedPharmScreen | varchar |  |  | SI | Use Combined Pharmacy Screen |
| OECF_UsePatLocForFavourites | varchar |  |  | SI | OECFUsePatLocForFavourites |
| OECF_UsePreprintedLabelsLab | varchar |  |  | SI | Use Preprinted Labels for Lab |
| OECF_UseRepeatsOrEndDate | varchar |  |  | SI | Use Repeats Or EndDate |
| OECF_VarianceReasMandatoryUponLateAdmin | varchar |  |  | SI | Variance Reason Mandatory Upon Late Medication Adm... |
| OECF_WarnOutstanAmtExist | varchar |  |  | SI | WarnOutstanAmtExist |
| OECF_WarnQtyRangeDuration | varchar |  |  | SI | Warn Qty Range to include Duration |
| OECF_WithoutAdminStatus_DR | bigint |  | FK | SI | Des Ref OECOrderAdminStatus, Without Administratio... |
| Q01 | - |  |  | SI | Fecha Atención |
| Q01ObsDR | - |  |  | SI | Fecha Atención DR |
| Q02 | - |  |  | SI | Fecha Última Atención |
| Q03 | - |  |  | SI | Tipo de Actividad Agendada |
| Q04 | - |  |  | SI | Tipo de Actividad Realizada |
| Q05 | - |  |  | SI | ACTIVIDAD |
| Q06 | - |  |  | SI | CUIDADO INTEGRAL |
| Q07 | - |  |  | SI | Anamnesis |
| Q08 | - |  |  | SI | Control / Compensación |
| Q09 | - |  |  | SI | Reacciones Adversas a Medicamentos |
| Q10 | - |  |  | SI | Observaciones de la Reación |
| Q11 | - |  |  | SI | Examen Físico |
| Q12 | - |  |  | SI | EXAMEN FÍSICO |
| Q13 | - |  |  | SI | Presión Arterial Sistólica |
| Q13ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q14 | - |  |  | SI | Presión Arterial Diastólica |
| Q14ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q15 | - |  |  | SI | Frecuencia Cardíaca |
| Q15ObsDR | - |  |  | SI | Frecuencia Cardíaca DR |
| Q16 | - |  |  | SI | Frecuencia Respiratoria |
| Q16ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q17 | - |  |  | SI | Saturación de Oxígeno |
| Q17ObsDR | - |  |  | SI | Saturación de Oxígeno DR |
| Q18 | - |  |  | SI | Peso |
| Q18ObsDR | - |  |  | SI | Peso DR |
| Q19 | - |  |  | SI | Talla |
| Q19ObsDR | - |  |  | SI | Talla DR |
| Q20 | - |  |  | SI | IMC |
| Q21 | - |  |  | SI | Hemoglucotest |
| Q21ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q22 | - |  |  | SI | Circunferencia Craneana |
| Q22ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q23 | - |  |  | SI | Circunferencia Cintura |
| Q23ObsDR | - |  |  | SI | Circunferencia Cintura DR |
| Q24 | - |  |  | SI | Estado Nutricional |
| Q25 | - |  |  | SI | Síntomas de disnea |
| Q26 | - |  |  | SI | Resultado Riesgo Ulceración |
| Q27 | - |  |  | SI | Úlcera activa del pie |
| Q28 | - |  |  | SI | Grado de Úlcera |
| Q29 | - |  |  | SI | Fecha Estado Nutricional |
| Q30 | - |  |  | SI | Fecha Síntomas de disnea |
| Q31 | - |  |  | SI | Fecha Evaluación del pie DM |
| Q32 | - |  |  | SI | Fecha Úlcera activa del pie |
| Q33 | - |  |  | SI | Fecha Grado Wagner úlcera |
| Q34 | - |  |  | SI | Fecha Parámetros Clínicos |
| Q35 | - |  |  | SI | Espirometría Basal VEF1/CVF |
| Q36 | - |  |  | SI | Fecha Espirometría Basal VEF1/CVF |
| Q37 | - |  |  | SI | Espirometría post BD VEF1/CVF |
| Q38 | - |  |  | SI | Fecha Espirometría post BD VEF1/CVF |
| Q39 | - |  |  | SI | Flujometría Basal |
| Q40 | - |  |  | SI | Fecha Flujometría Basal |
| Q41 | - |  |  | SI | Flujometría pot BD |
| Q42 | - |  |  | SI | Fecha Flujometría pot BD |
| Q43 | - |  |  | SI | Pirometría |
| Q44 | - |  |  | SI | Fecha Pimometría |
| Q45 | - |  |  | SI | Test de Provocación con Ejercicio |
| Q46 | - |  |  | SI | Fecha Test de Provocación con Ejercicio |
| Q47 | - |  |  | SI | Resultado Test Marcha 6 Min |
| Q48 | - |  |  | SI | Fecha Test de Marcha |
| Q49 | - |  |  | SI | Resultado COPD Assessment Test CAT |
| Q50 | - |  |  | SI | Fecha Resultado COPD Assessment Test CAT |
| Q51 | - |  |  | SI | EQ5D |
| Q52 | - |  |  | SI | Fecha EQ5D |
| Q53 | - |  |  | SI | Electrocardiograma Descripción |
| Q53ObsDR | - |  |  | SI | Electrocardiograma Descripción DR |
| Q54 | - |  |  | SI | Fecha Electrocardiograma |
| Q55 | - |  |  | SI | Cuestionario Pediátrico de Síntomas (PSC) 5-9 años |
| Q56 | - |  |  | SI | Fecha Cuestionario Pediátrico de Síntomas (PSC) 5-... |
| Q57 | - |  |  | SI | Cuestionario Pediátrico de Síntomas (PSC-Y) 10-14 ... |
| Q58 | - |  |  | SI | Fecha Cuestionario Pediátrico de Síntomas (PSC-Y) ... |
| Q59 | - |  |  | SI | Cuestionario de Salud General GHQ-12 |
| Q60 | - |  |  | SI | Fecha Cuestionario de Salud General GHQ-12 |
| Q61 | - |  |  | SI | PEDS-QL |
| Q62 | - |  |  | SI | Fecha PEDS-QL |
| Q63 | - |  |  | SI | Plan de Cuidado Integral |
| Q64 | - |  |  | SI | Compromiso Acordado |
| Q65 | - |  |  | SI | Cumplimiento de cada uno de los acuerdos de plan d... |
| Q66 | - |  |  | SI | Consejería Familiar |
| Q67 | - |  |  | SI | Consejeria Breve Tabaquismo |
| Q68 | - |  |  | SI | Monitoreo a Distancia |
| Q69 | - |  |  | SI | Próximo Control con |
| Q70 | - |  |  | SI | Próximo Control |
| Q71 | - |  |  | SI | Fecha Próximo Control |
| Q72 | - |  |  | SI | Electrocardiograma |
| Q72ObsDR | - |  |  | SI | Electrocardiograma DR |
| Q74 | - |  |  | SI | Hora Ultimo Registro Atención RUI |
| Q75 | - |  |  | SI | La Etiqueta de Caida |
| Q76 | - |  |  | SI | EVALUACIÓN DEL PIE DIABÉTICO |
| Q77 | - |  |  | SI | EVALUACIÓN ENFERMEDAD RESPIRATORIA CRÓNICA |
| Q78 | - |  |  | SI | OTROS PROCEDIMIENTOS DIAGNÓSTICOS |
| Q79 | - |  |  | SI | PLAN DE CUIDADO INTEGRAL |
| Q80 | - |  |  | SI | OTROS PROCEDIMIENTOS DIAGNÓSTICOS |
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