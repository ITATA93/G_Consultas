# SQLUser.CF_PatConf1

**Schema:** SQLUser
**Columnas:** 261
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATCF1_RowId | bigint | PK |  | NO | - |
| PACTF1_AllowAllocRefInvToInv | varchar |  |  | SI | Allow Allocation Refund Invoice to an Invoice |
| PACTF1_AllowLinkNewPatToExistingWL | varchar |  |  | SI | Allow to link the new Inpatient admission with an ... |
| PATCF1_AccrualsControl | varchar |  |  | SI | Accruals Control  |
| PATCF1_AddGestAtBirthBasedOnAEDD | varchar |  |  | SI | Add Baby's Gestation at Time of Birth based on Mot... |
| PATCF1_AddIrrigationToFB | varchar |  |  | SI | Enable Adding Irrigation Input/Output to Overall F... |
| PATCF1_AddOrderItemsProc | varchar |  |  | SI | Add Order Items for Procedure |
| PATCF1_AddWLToDeceased | varchar |  |  | SI | Allow adding WL to deceased patient |
| PATCF1_AdolAgeFrom | double |  |  | SI | Paediatric Age Field Adolescent Years FROM  |
| PATCF1_AdolAgeTo | double |  |  | SI | Paediatric Age Field Adolescent Years To  |
| PATCF1_AdultLiquidFastOffsetHrs | double |  |  | SI | Adult Fasting Time Offset for liquids |
| PATCF1_AdultSolidFastOffsetHrs | double |  |  | SI | Adult Fasting Time Offset for solids |
| PATCF1_AgrEDDDCancPregNoDel | double |  |  | SI | AgrEDDDCancPregNoDel |
| PATCF1_AllocSameBillNumAllInv | varchar |  |  | SI | Allocate Same Bill Number To All Invoices |
| PATCF1_AllowAddOrderSecondProc | varchar |  |  | SI | Allow to add order item from the Secondary Operati... |
| PATCF1_AllowCSverOutOfLogonHosp | varchar |  |  | SI | Allow creation of new CS version outside of logon ... |
| PATCF1_AllowCreateWLNoAdmRight | varchar |  |  | SI | Allow Users without Admission Rights create Waitin... |
| PATCF1_AllowEMAdmInWard | varchar |  |  | SI | Allow Emergency Episodes to be allocated to a Ward |
| PATCF1_AllowInpatAdmInEDLocBeds | varchar |  |  | SI | Allow Inpatient Admissions to be allocated to ED l... |
| PATCF1_AllowMultUpdSurgPrefs | varchar |  |  | SI | Allow Multiple updates to Surgical Preferences Ord... |
| PATCF1_AllowMultipleLanguages | varchar |  |  | SI | Allow multiple preferred languages for a patient |
| PATCF1_AllowNegOutStandAmt | varchar |  |  | SI | Allow negative outstanding amount |
| PATCF1_AllowOTBookingWOBedCode | varchar |  |  | SI | Allow OT Booking without Bed Code |
| PATCF1_AllowPartialMatchForOpProc | varchar |  |  | SI | Allow partial string match for Operation/Procedure... |
| PATCF1_AllowSuspAfterWLComp | varchar |  |  | SI | PATCF1AllowSuspAfterWLComp |
| PATCF1_AllowTransferOTLocat | varchar |  |  | SI | Allow Transfer between Operating Theatre Locations |
| PATCF1_ApplyDischCutOffSameDay | varchar |  |  | SI | Apply Discharge Cut off time to Same Day Accommoda... |
| PATCF1_ApplyLabBilling | varchar |  |  | SI | Apply Lab Billing |
| PATCF1_ApplyPayorPaysFromEachBill | varchar |  |  | SI | Apply Payor Pays From to each Episode Bill |
| PATCF1_ApplyStockBatchPriceForBilling | varchar |  |  | SI | ApplyBatchPriceForPharmacyAndSupplies |
| PATCF1_ApplyTariffOnAdminDate | varchar |  |  | SI | Apply Tariff On Administration Date |
| PATCF1_AuthoriseOTAdmInvoice | varchar |  |  | SI | Authorise Theatre Episodes for Invoicing |
| PATCF1_AutoPatAlertPregn | varchar |  |  | SI | Autocreate Patient Alert for Pregnancy |
| PATCF1_AutoPopBabySurname | varchar |  |  | SI | Auto-populate Baby's Surname during Delivery with |
| PATCF1_BankAccount | varchar |  |  | SI | Bank Account  |
| PATCF1_BaseAnaesStartTm | double |  |  | SI | Base Anaesthetic Start Time (minutes) |
| PATCF1_BaseAreaOutTm | double |  |  | SI | Base Area Out Time (minutes) |
| PATCF1_BaseIntoAnaesRoomTm | double |  |  | SI | Base Into Anaesthetic Room Time (minutes) |
| PATCF1_BaseIntoTheatreRoomTm | double |  |  | SI | Base Into Theatre Room Time (minutes) |
| PATCF1_BaseOTArrivalTm | double |  |  | SI | Base OT Arrival Time (minutes) |
| PATCF1_BaseOTSessDelayTm | double |  |  | SI | Base Allowed Session Delay Time (minutes) |
| PATCF1_BaseOTSessOverrunTm | double |  |  | SI | Base Allowed Session Overrun Time (minutes) |
| PATCF1_BaseOutOfTheatreTm | double |  |  | SI | Base Out of Theatre Time (minutes) |
| PATCF1_BaseRecoveryTheatreOutTm | double |  |  | SI | Base Recovery in Theatre Out Time (minutes) |
| PATCF1_BaseRecoveryTm | double |  |  | SI | Base Recovery Time (minutes) |
| PATCF1_BatchStatusAllBillsPaid | varchar |  |  | SI | BatchStatusAllBillsPaid |
| PATCF1_BedReasonNotAvail_DR | bigint |  | FK | SI | Des Ref BedReasonNotAvail |
| PATCF1_BedTypeOSAccumQty | varchar |  |  | SI | Bed Type - Order Set Accumulate Quantity |
| PATCF1_BillAdmixIndivIngred | varchar |  |  | SI | Bill Admixture Individual Ingredients |
| PATCF1_BillBabyEpisNonPackOI | varchar |  |  | SI | Bill Baby Episode Non Package Order Item |
| PATCF1_BillOrdItemsLinkEpis | varchar |  |  | SI | Bill Order Items to Link Episode |
| PATCF1_BillQuantityPacked | varchar |  |  | SI | Bill Quantity Packed |
| PATCF1_BookNextAvailOverlap | varchar |  |  | SI | Book next available time for overlapping booking |
| PATCF1_BookedOTReadOnly | varchar |  |  | SI | OT Booking of status Booked display read-only |
| PATCF1_CalEpisDurationOnAdm | varchar |  |  | SI | Calculate episode duration based on admission date... |
| PATCF1_CalcAverAccom | varchar |  |  | SI | CalcAverAccom |
| PATCF1_CalcLabourStagesBasedExpulsion | varchar |  |  | SI | Use Expulsion Start Date and Time to Calculate Lab... |
| PATCF1_CalcOTBillMinFromOTInOut | varchar |  |  | SI | Calculate Theatre Billing Minutes from Theatre In/... |
| PATCF1_CalcPretermBirthBasedNoPreg | varchar |  |  | SI | Calculate Preterm Birth Based on Number of Pregnan... |
| PATCF1_CancLinkedInvOnBillCanc | varchar |  |  | SI | Cancel All Linked Invoices Upon Bill Cancellation |
| PATCF1_CancelAdmAndOTAppt | varchar |  |  | SI | Cancel Admission and Outpatient Appointment when c... |
| PATCF1_CancerTreatAgree | double |  |  | SI | Cancer Treatment Agreement |
| PATCF1_CheckOrdersCovered | varchar |  |  | SI | Check if Orders are Covered |
| PATCF1_CheckSimilarName | varchar |  |  | SI | CheckSimilarName |
| PATCF1_ChildAgeFrom | double |  |  | SI | Paediatric Age Field Child Years FROM  |
| PATCF1_ChildAgeTo | double |  |  | SI | Paediatric Age Field Child Years TO  |
| PATCF1_ChkItemReadyForBilling | varchar |  |  | SI | Check if Item is Ready for Billing |
| PATCF1_ChkMultiTestSetPerDay | varchar |  |  | SI | ChkMultiTestSetPerDay |
| PATCF1_ConflictCheckAlgAltMerge | varchar |  |  | SI | Conflict Checking for Allergies and Alerts on Pati... |
| PATCF1_ContactReminderDateRemovalReason_DR | bigint |  | FK | SI | Contact/Reminder Date Removal Reason |
| PATCF1_CopyDiagFromLinkedEpisode | varchar |  |  | SI | Copy Diagnosis/Procedures from Linked Episode |
| PATCF1_CopyEpDiagnosisThroughBOW | varchar |  |  | SI | Copy diagnosis from ordering episode to OP episode... |
| PATCF1_CopyMotherPayorDetBaby | varchar |  |  | SI | Copy Mother Payor Details to Baby |
| PATCF1_CopyPatientRegLimits | varchar |  |  | SI | Copy Patient Registraton Limits |
| PATCF1_CopyPayPlanFrmPersonToEpisode | varchar |  |  | SI | Copy Payor Plan Details from Person to Episode |
| PATCF1_CopySessASForExistingBooking | varchar |  |  | SI | Copy Session Additional Staff for Existing Booking... |
| PATCF1_CreateAnaOnArrival | varchar |  |  | SI | Create Anaesthetic and Operation Records on Patien... |
| PATCF1_CreateOpRecSecondary | varchar |  |  | SI | Create Anaesthetic Operation Record for Secondary ... |
| PATCF1_CreditAdjPayMethod_DR | bigint |  | FK | SI | Credit Adjustment Payment Method |
| PATCF1_CreditNoteOutsBalance | varchar |  |  | SI | Credit Notes Outstanding Balance |
| PATCF1_DailyChargeBlock | double |  |  | SI | DailyChargeBlock |
| PATCF1_DaysAfterAEDDEndPregAlert | double |  |  | SI | Days after AEDD to end pregnancy Alert |
| PATCF1_DaysClinSummaryED | double |  |  | SI | days prior to estimated date of discharge that the... |
| PATCF1_DaysClinSummaryIP | double |  |  | SI | days prior to estimated date of discharge that the... |
| PATCF1_DaysClinSummaryOP | double |  |  | SI | days prior to estimated date of discharge that the... |
| PATCF1_DaysParityAfterDeliver | double |  |  | SI | DaysParityAfterDeliver |
| PATCF1_DebtorControl | varchar |  |  | SI | Debtor Control  |
| PATCF1_DefAdmDateAsExpctAdmDate | varchar |  |  | SI | Default Admission Date as Expected Admission Date |
| PATCF1_DefEDDischSummaryType | varchar |  |  | SI | DefEDDischSummaryType |
| PATCF1_DefFullEpisTimeRangeForDisEpis | varchar |  |  | SI | Default full episode time range for Discharged Epi... |
| PATCF1_DefIPDischSummaryType | varchar |  |  | SI | DefIPDischSummaryType |
| PATCF1_DefOPDischSummaryType | varchar |  |  | SI | DefOPDischSummaryType |
| PATCF1_DefOrdVarReasEpisCanc_DR | bigint |  | FK | SI | Default Order Variance Reason for Episode Cancel |
| PATCF1_DefaultGPLetterReport_DR | bigint |  | FK | SI | Default GP Letter Report |
| PATCF1_DefaultIfEligable | varchar |  |  | SI | DefaultIfEligable |
| PATCF1_DefaultRejectReason_DR | bigint |  | FK | SI | Des Ref PACTransRejectReason |
| PATCF1_DelayOverWarn | varchar |  |  | SI | Enable Delay and Overrun Warnings |
| PATCF1_DentalNumberingPolicy | varchar |  |  | SI | Dental Numbering Policy |
| PATCF1_DisTimeCutoff | double |  |  | SI | DisTimeCutoff |
| PATCF1_DisWarnMessEpisOTBookLoc | varchar |  |  | SI | DisableWarningMessageEpisodeDoesNotMatchOTBookingL... |
| PATCF1_DiscrDiscountOrdItmLevel | varchar |  |  | SI | Discretionary Discount Order Item Level  |
| PATCF1_DispAllTransFromClinician | varchar |  |  | SI | Display all Transactions from Clinician Menu |
| PATCF1_DispBillQtyMultPayors | varchar |  |  | SI | Display Bill Quantity Over Muliple Payors |
| PATCF1_DispEPRDataLinkEpis | varchar |  |  | SI | Display EPR Data Across Linked Episodes |
| PATCF1_DispPriceBeforeTaxInvDet | varchar |  |  | SI | Display Price Before Tax in Invoice Details |
| PATCF1_DisplayIncompleteEWSTotals | varchar |  |  | SI | Display Incomplete EWS Totals |
| PATCF1_DisplayMsgTCIOTChgDate | varchar |  |  | SI | Display message when TCI Date/OT Date changes from... |
| PATCF1_DoNotAllowChangeDiagOnCodingScreen | varchar |  |  | SI | Do Not Allow Changing Diagnosis On Coding Screen |
| PATCF1_DoNotDelDiscBefDate | date |  |  | SI | Do not Delete Discounts Before Date |
| PATCF1_DoNotLinkNewEpToDischEp | varchar |  |  | SI | Do Not Link New Episode to Recently Discharged Epi... |
| PATCF1_DuplicatePatientWarning | varchar |  |  | SI | DuplicatePatientWarning |
| PATCF1_EarliestYear | double |  |  | SI | Earliest Year |
| PATCF1_EffDateCopySchedCP | varchar |  |  | SI | New Effective Date Copies Schedule Care Providers |
| PATCF1_EligibilityModule | varchar |  |  | SI | Eligibility Module |
| PATCF1_EnableBrief | varchar |  |  | SI | Enable Briefing/Debriefing Management for Operatin... |
| PATCF1_EnableDeceaseEdit | varchar |  |  | SI | PATCF1EnableDeceaseEdit |
| PATCF1_EnableEWSScoreCompletenessCheckAlerts | varchar |  |  | SI | Enable EWS Score Completeness Check and Alerts |
| PATCF1_EnableEnglishRTT | varchar |  |  | SI | Enable English RTT Rules |
| PATCF1_EnablePreadmissionsMove | varchar |  |  | SI | EnablePreadmissionsMove |
| PATCF1_EpTypeMedDisBeforeFinDis | varchar |  |  | SI | Episode Types for Medical Discharge before Financi... |
| PATCF1_EpisTypeDeductibles | varchar |  |  | SI | Episode Type for Deductibles |
| PATCF1_ExcludeAdditDiagFromCoding | varchar |  |  | SI | ExcludeAdditDiagFromCoding |
| PATCF1_ExcludeFromLC | double |  |  | SI | Exclude from living children calculations if baby ... |
| PATCF1_ForCurrPaymAdj_DR | bigint |  | FK | SI | Des Ref ReasonWriteOff |
| PATCF1_GenResidentNo | varchar |  |  | SI | Generate Resident Number |
| PATCF1_HoursMembRuptured | numeric |  |  | SI | Number of Hours when Membrane Ruptured to Return a... |
| PATCF1_IPTreatPathReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason, not in use ... |
| PATCF1_InclOSItemsInPackBill | varchar |  |  | SI |  Include Order Set Items in the Package Billing |
| PATCF1_IncludeSecondaryOpProcOrders | varchar |  |  | SI | Include Orders for Secondary Operation/Procedure P... |
| PATCF1_InfantAgeFrom | double |  |  | SI | Paediatric Age Field Infant Months FROM (note TO i... |
| PATCF1_InfantAgeTo | double |  |  | SI | Paediatric Age Field Infant Years TO (note FROM is... |
| PATCF1_InpatientOrder_DR | varchar |  | FK | SI | Des Ref ARCIM |
| PATCF1_InvAllBillsSameTime | varchar |  |  | SI | Invoice All Bills At The Same Time |
| PATCF1_InvokeAgeSexICDRestrict | varchar |  |  | SI | InvokeAgeSexICDRestrict |
| PATCF1_LetterCatInPathway_DR | bigint |  | FK | SI | Letter Category for Patient Consent in Clinical Pa... |
| PATCF1_LifeTimeCumDoseWarnThresh | double |  |  | SI | Lifetime cumulative dose warning threshold |
| PATCF1_LinkEDOPtoIPNextDayHrLimit | double |  |  | SI | Link ED/OP to IP Episode Next Day Hour Limit |
| PATCF1_LinkOTBookToExistingAdm | varchar |  |  | SI | Link OT Booking to Existing Admission when coming ... |
| PATCF1_LinkOTBookToPreAdm | varchar |  |  | SI | Link OT Booking to Pre Admission |
| PATCF1_LnkMumBabyRoomTyp | varchar |  |  | SI | Link Mothers Room Type To Babies |
| PATCF1_MainEpisPayorForLinkEpis | varchar |  |  | SI | Use Main Episode Payor For Linked Episodes |
| PATCF1_MortuaryAdmNoLength | double |  |  | SI | Mortuary Admission Number Length |
| PATCF1_MortuaryAdmNoPrefix | varchar |  |  | SI | Mortuary Admission Number Prefix |
| PATCF1_MortuaryAdmNoSuffix | varchar |  |  | SI | Mortuary Admission Number Suffix |
| PATCF1_MultFactorLowerRange | double |  |  | SI | Multiplier Factor Lower Range |
| PATCF1_MultFactorUpperRange | double |  |  | SI | Multiplier Factor Upper Range |
| PATCF1_MultipleTCI | varchar |  |  | SI | Allow multiple TCI on same day |
| PATCF1_NewbornAgeFrom | double |  |  | SI | Paediatric Age Field Newborn Months From |
| PATCF1_NewbornAgeTo | double |  |  | SI | Paediatric Age Field Newborn Months To |
| PATCF1_NextMUrgentPatDocCP | varchar |  |  | SI | NextMUrgentPatDocCP |
| PATCF1_NoAdmAfterFinancialDisch | varchar |  |  | SI | No Administration after Financial Discharge |
| PATCF1_NoAutoAllocCredNoteNum | varchar |  |  | SI | Do Not Automatically Allocate Credit Note Number |
| PATCF1_NoAutoPopRecLocOrder | varchar |  |  | SI | NoAutoPopRecLocOrder |
| PATCF1_NoCancelOTAnaOpDone | varchar |  |  | SI | Do not allow OT booking cancellation when Anaesthe... |
| PATCF1_NoChangeDateTime1stBedMove | varchar |  |  | SI | Do not allow changes to date and time of first bed... |
| PATCF1_NoConcurrentIPEDAdms | varchar |  |  | SI | Do Not Allow Concurrent IP and ED Episode At The S... |
| PATCF1_NoDiscrDiscountInvoicedBill | varchar |  |  | SI | Do Not Allow Discretionary Discount on Invoiced Bi... |
| PATCF1_NoDispPatEditPatContact | varchar |  |  | SI | Do Not Display Patient Edit on Patient Contact |
| PATCF1_NoExclOrdItemsFinDisch | varchar |  |  | SI | Do Not Allow to Exclude Order Items after Financia... |
| PATCF1_NoLinkArrivalToAreaIn | varchar |  |  | SI | Separate Area In Date/Time from Arrival Date/Time |
| PATCF1_NoReplEpisPresCompProcFreeText | varchar |  |  | SI | Do Not Replace Episode Presenting Complaint with P... |
| PATCF1_NoResetStepDownMedProc | varchar |  |  | SI | Do No Reset Step Down Days for Medical Procedure |
| PATCF1_NoSplitBillExcessCopay | varchar |  |  | SI | Do not split bill for Excess and Co-Payment |
| PATCF1_NoStorePerDiemForEpisBill | varchar |  |  | SI | Do Not Store Per Diem Rates for Episodic Billing  |
| PATCF1_NoUpdBillStatOnDCPackOI | varchar |  |  | SI | Do Not Update Billing Status Upon Discontinue of P... |
| PATCF1_NoUpdClinPNWithRefDocPN | varchar |  |  | SI | Do not update Clinic Provider Number with Referrin... |
| PATCF1_NumDaysPatTCITreatDefCanc | double |  |  | SI | Number of Days that patient needs to be brought ba... |
| PATCF1_OTCPConflictCheck | varchar |  |  | SI | OT CP ConflictCheck |
| PATCF1_OTQuestProfile_DR | bigint |  | FK | SI | Des Ref OT Questionnaire Profile |
| PATCF1_OTSessDelayType | varchar |  |  | SI | Time to Use for Delay (Standard type OTDelayTime) |
| PATCF1_OTSessOverrunType | varchar |  |  | SI | Time to Use for Overrun (Standard type OTOverrunTi... |
| PATCF1_OldestAge | double |  |  | SI | Oldest Age |
| PATCF1_OutpatientOrder_DR | varchar |  | FK | SI | Des Ref ARCIM |
| PATCF1_PackDisconAdjReason_DR | bigint |  | FK | SI | Package Discontinue Adjustment Reason Des Ref Reas... |
| PATCF1_PaedLiquidFastOffsetHrs | double |  |  | SI | Paediatric Fasting Time Offset for liquids |
| PATCF1_PaedSolidFastOffsetHrs | double |  |  | SI | Paediatric Fasting Time Offset for solids |
| PATCF1_ParityCalculationOnPregnancyNo | varchar |  |  | SI | ParityCalculationOnPregnancyNo |
| PATCF1_PartialAdmTimeCutoff | time |  |  | SI | PartialAdmTimeCutoff |
| PATCF1_PartialAdmTimeCutoffPerc | double |  |  | SI | PartialAdmTimeCutoffPerc |
| PATCF1_PartialDisTimeCutoff | time |  |  | SI | PartialDisTimeCutoff |
| PATCF1_PartialDisTimeCutoffPerc | double |  |  | SI | PartialDisTimeCutoffPerc |
| PATCF1_PartialICD10Search | varchar |  |  | SI | Allow partial string match for ICD10 search |
| PATCF1_PathwayOutcome_DR | bigint |  | FK | SI | Clinical Pathway outcome on Patient death  |
| PATCF1_PayorApproval | varchar |  |  | SI | Payor Approval Functiomality activated |
| PATCF1_PreanaestheticConsultNoLength | double |  |  | SI | Preanaesthetic Consultation Number Length |
| PATCF1_PreanaestheticConsultNoPrefix | varchar |  |  | SI | Preanaesthetic Consultation Number Prefix |
| PATCF1_PreanaestheticConsultNoSuffix | varchar |  |  | SI | Preanaesthetic Consultation Number Suffix |
| PATCF1_PreanaestheticDoneOnOT | varchar |  |  | SI | Set Aanesthetic Consultation to Done on OT Booking |
| PATCF1_PregICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| PATCF1_PregICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PATCF1_PregSnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PATCF1_PregSnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PATCF1_ReinstateEDBedRequest | varchar |  |  | SI | Reinstate ED Bed Request when Rejecting IP Request |
| PATCF1_RestrLocByDepGroup | varchar |  |  | SI | Restrict Location by User/Care Provider department... |
| PATCF1_ReturnPFBListSeenByDate | varchar |  |  | SI | Return PFB list by SeenByDate  |
| PATCF1_RevertWLStatOnApptCancel | varchar |  |  | SI | Revert Waiting List Status to Previous Status on a... |
| PATCF1_RoundAmtFrom | double |  |  | SI | RoundAmtFrom |
| PATCF1_RoundAmtTo | double |  |  | SI | RoundAmtTo |
| PATCF1_RoundTotOrdItemBillAmt | varchar |  |  | SI | Round on Total Order Item Bill Amount |
| PATCF1_RoundUp | varchar |  |  | SI | Always Round to Highest Value |
| PATCF1_SendSMSMsgIfConsentNull | varchar |  |  | SI | Send SMS Message if Consent is Null or Not Stated |
| PATCF1_SetAdmDateEarliestOTDate | varchar |  |  | SI | Set Admission Date/Time to the Earliest OT Date/Ti... |
| PATCF1_ShortTermCumDoseWarnThresh | double |  |  | SI | Short-term Cumulative Dose Warning Threshold |
| PATCF1_ShowProfileType | varchar |  |  | SI | ShowProfileType |
| PATCF1_SimplifyDupWLWarningMsg | varchar |  |  | SI | Simplify Duplicate WL Warning Message |
| PATCF1_SpecPatAccWarningInpat | double |  |  | SI | Special Patient Account Warning Inpatient |
| PATCF1_SpecPatAccWarningOutpat | double |  |  | SI | Special Patient Account Warning Outpatient |
| PATCF1_StartWaitDaysFromZero | varchar |  |  | SI | Start Wait Days from Zero |
| PATCF1_StkBatchPricePreServTax | varchar |  |  | SI | Stock Batch Price Pre Service Tax |
| PATCF1_StopAccomMedDisch | varchar |  |  | SI | Stop charging Accom from date of Medical Discharge |
| PATCF1_SupEpisBillInlAddOnOverlap | varchar |  |  | SI | Supress Episodic Billing Inlier Charges when Add O... |
| PATCF1_SuspenCalcWTimeGuarDate | double |  |  | SI | SuspenCalcWTimeGuarDate |
| PATCF1_SyncEDandIPBedRequests | varchar |  |  | SI | Sync ED and IP Bed Requests |
| PATCF1_TariffAdjustPayorPatientShare | varchar |  |  | SI | ApplyTariffAdjustmentToPayor/Patient Share |
| PATCF1_TemporaryAddressType_DR | bigint |  | FK | SI | Temporary Address Type |
| PATCF1_TmBasedDayAccmRate | varchar |  |  | SI | Time Based Daily Accommodation Rate |
| PATCF1_TolAnaesStartTm | double |  |  | SI | Tolerance Anaesthetic Start Time (minutes) |
| PATCF1_TolAreaOutTm | double |  |  | SI | Tolerance Area Out Time (minutes) |
| PATCF1_TolIntoAnaesRoomTm | double |  |  | SI | Tolerance Into Anaesthetic Room Time (minutes) |
| PATCF1_TolIntoTheatreRoomTm | double |  |  | SI | Tolerance Into Theatre Room Time (minutes) |
| PATCF1_TolMaxOperTmMins | double |  |  | SI | Tolerance Maximum Operating Time (minutes) |
| PATCF1_TolOTArrivalTm | double |  |  | SI | Tolerance OT Arrival Time (minutes) |
| PATCF1_TolOTDelayMargin | double |  |  | SI | Tolerance OT Delay Margin (minutes) |
| PATCF1_TolOTSessDelayTm | double |  |  | SI | Tolerance Allowed Session Delay Time (minutes) |
| PATCF1_TolOTSessOverrunTm | double |  |  | SI | Tolerance Allowed Session Overrun Time (minutes) |
| PATCF1_TolOTStartMargin | double |  |  | SI | Tolerance OT Start Margin (minutes) |
| PATCF1_TolOutOfTheatreTm | double |  |  | SI | Tolerance Out of Theatre Time (minutes) |
| PATCF1_TolRecoveryTheatreOutTm | double |  |  | SI | Tolerance Recovery in Theatre Out Time (minutes) |
| PATCF1_TolRecoveryTm | double |  |  | SI | Tolerance Recovery Time (minutes) |
| PATCF1_TolrcAllwChngeOvertmBtwOps | double |  |  | SI | Tolerance Allowed Overtime between Procedures (min... |
| PATCF1_TransferBookedNewPreAdm | varchar |  |  | SI | Transfer Booked appointment to new pre-admission |
| PATCF1_UnallocPayment | varchar |  |  | SI | Unallocated Payment  |
| PATCF1_UnknownName | varchar |  |  | SI | UnknownName |
| PATCF1_UpdAnaFromAnaOpOnArrival | varchar |  |  | SI | Allow on Arrive OT Booking update Anaesthetic Reco... |
| PATCF1_UpdateWLStatBasedOnAllAppts | varchar |  |  | SI | Update Waiting List Status based on all appointmen... |
| PATCF1_UseCabFileAddressSearch | varchar |  |  | SI | UseCabFileForAddressSearch |
| PATCF1_UseConditionOnsetFlag | varchar |  |  | SI | Use Condition Onset Flag in DRG Coding |
| PATCF1_UseExtStockDispQtyBill | varchar |  |  | SI | UseExtStockDispQtyBill |
| PATCF1_UseFirstWLApptDate | varchar |  |  | SI | Use the earliest appointment date for the WLApptDa... |
| PATCF1_UseOTOrdersList | varchar |  |  | SI | Use OT Orders List on Anaesthetic Summary |
| PATCF1_UsePerioperativeMovement | varchar |  |  | SI | Use Perioperative Movement Details for Floorplan M... |
| PATCF1_UsePlannedTotalTheatreTime | varchar |  |  | SI | Use Planned Total Theatre Time For Estimated Time |
| PATCF1_UsePostOffForPayPlanRest | varchar |  |  | SI | Use Post Office for Payor/Plan Restrictions |
| PATCF1_UserDefWindow_DR | bigint |  | FK | SI | Des Ref SSUserDefWindowDR |
| PATCF1_VarianceAlertOnUpdate | varchar |  |  | SI | Variance Alert on Update |
| PATCF1_WLAdmOperationStartTimeAsOTEstStartTime | varchar |  |  | SI | Set Operation Start Time on Waiting List Admission... |
| PATCF1_WLAdmTimeAsBedInTime | varchar |  |  | SI | Set Admission Time on Waiting List Admission as Be... |
| PATCF1_WLResourceOneSpecialty | varchar |  |  | SI | Resources chosen from a WL can only have one speci... |
| PATCF1_WarnPatOutstandingInv | varchar |  |  | SI | Warning Patient Outstanding Invoice |
| PATCF1_WarnPatOutstandingInvUserHosp | varchar |  |  | SI | Warning Patient Outstanding Invoice User Hospital |
| Q08Q1 | - |  |  | SI | Día |
| Q08Q10 | - |  |  | SI | Frecuencia Cardíaca |
| Q08Q2 | - |  |  | SI | Fecha |
| Q08Q3 | - |  |  | SI | ¿Trae inhalador y aerocámara? |
| Q08Q4 | - |  |  | SI | ¿Ha ingerido alimentos o líquidos durante la últim... |
| Q08Q5 | - |  |  | SI | Uso de musculatura accesoria |
| Q08Q6 | - |  |  | SI | ¿Cuál? |
| Q08Q7 | - |  |  | SI | Saturación O2 |
| Q08Q8 | - |  |  | SI | Temperatura Axilar |
| Q08Q9 | - |  |  | SI | Frecuencia Respiratoria |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*