# SQLUser.CF_PatConf

**Schema:** SQLUser
**Columnas:** 389
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATCF_RowID | bigint | PK |  | NO | - |
| ChildQ82DR | - |  |  | SI | Child Reference: Gestión de Casos |
| PATCF_ADEVQuesGroup_DR | bigint |  | FK | SI | Recorded Adverse Drug/Event Reactions Questionnair... |
| PATCF_ActivateAdvancdEPRSecu | varchar |  |  | SI | ActivateAdvancdEPRSecurty |
| PATCF_ActivateAdvancdSOAPCon | varchar |  |  | SI | ActivateAdvancdSOAPConsSecurty |
| PATCF_ActualTimesInDiary | varchar |  |  | SI | ActualTimesInDiary |
| PATCF_AddLinkedPlansOnAdm | varchar |  |  | SI | Add Linked Plans OnAdm |
| PATCF_AddressType_DR | bigint |  | FK | SI | Des Ref AddressType |
| PATCF_AdmCancelGracePeriod | double |  |  | SI | Admission Cancellation Grace Period |
| PATCF_AdmQuest_DR | bigint |  | FK | SI | Des Ref Admission Questionnaire |
| PATCF_AgeCutOffMinors | double |  |  | SI | Age Cut Off for Minors |
| PATCF_AllAdmsForNewDischarge | varchar |  |  | SI | AllAdmsForNewDischarge |
| PATCF_AllOverlapSuspens | varchar |  |  | SI | Allow Overlapping Suspensions |
| PATCF_Allergy_DR | bigint |  | FK | SI | Des Ref Allergy |
| PATCF_AllowCarePlanIntApptDCONOutcClose | varchar |  |  | SI | AllowCarePlanIntApptDCONOutcClose |
| PATCF_AllowChangePreadmDateWL | varchar |  |  | SI | Allow to Change Preadm Date in WL |
| PATCF_AllowDirectCashPayment | varchar |  |  | SI | Allow Direct Cash Payment |
| PATCF_AllowEditCPforLinkedWLAdm | varchar |  |  | SI | Allow Edit CP for Linked WL Admissions |
| PATCF_AllowEnterDiagnosisDischarge | varchar |  |  | SI | Allow to Enter Diagnosis on Discharge |
| PATCF_AllowInpatDischWOFin | varchar |  |  | SI | Allow In Pat Discharge W/O Fin Discharge |
| PATCF_AllowMultipleActiveGP | varchar |  |  | SI | Allow MultipleActiveGP |
| PATCF_AllowOverlapGP | varchar |  |  | SI | Allow Overlap GP |
| PATCF_AllowOverlapIPEpisodes | varchar |  |  | SI | Allow Overlap IP Episodes |
| PATCF_AllowPartialPaymentPayorBill | varchar |  |  | SI | Allow Partial Payment of Payor Bill |
| PATCF_AllowPartialPaymentSystemBill | varchar |  |  | SI | Allow Partial Payment System Bill |
| PATCF_AllowSelfAdmission | varchar |  |  | SI | Allow Self Admission |
| PATCF_AllowWLChangesAfterAdm | varchar |  |  | SI | Allow WL Changes After Admission |
| PATCF_AlloweChangeOvertimeBtwOps | double |  |  | SI | Base Allowed Overtime between Procedures (minutes) |
| PATCF_AnaestLength | double |  |  | SI | Anaest. Length |
| PATCF_AnaestPrefix | varchar |  |  | SI | Anaest. Prefix |
| PATCF_AnaestSuffix | varchar |  |  | SI | Anaest. Suffix |
| PATCF_AnonymousName | varchar |  |  | SI | Anonymous Name |
| PATCF_AppCreatePayPlanAdm | varchar |  |  | SI | Keep AppCreatePayPlanForAdm |
| PATCF_ApplyMaxPatDiscount | varchar |  |  | SI | Apply Max Patient Discount |
| PATCF_ApplyNewRoomRates | varchar |  |  | SI | Apply New Room Rates for existing patients |
| PATCF_ArrivePatientOnReg | varchar |  |  | SI | Arrive Patient On Registration |
| PATCF_AssignDepartmentToBed | varchar |  |  | SI | Assign Department To Bed |
| PATCF_AutoCreateOTBookEpConditions | varchar |  |  | SI | AutoCreateOTBookEpConditions |
| PATCF_AutoCreatePregnanForBookMAT | varchar |  |  | SI | AutoCreatePregnanForBookMAT |
| PATCF_AutomaticReadLinkedProviders | varchar |  |  | SI | AutomaticReadLinkedProviders |
| PATCF_BedReqCurrentLoc | varchar |  |  | SI | Bed Request From Current Non-temporary Location |
| PATCF_BedRequestHours | double |  |  | SI | Bed Request Hours |
| PATCF_BedType_DR | bigint |  | FK | SI | Des REf BedType |
| PATCF_BirthWeightMax | double |  |  | SI | BirthWeightMax |
| PATCF_BirthWeightMin | double |  |  | SI | BirthWeightMin |
| PATCF_BookingTypeForMaternityEquals_DR | bigint |  | FK | SI | Des Ref BookingTypeForMaternityEquals |
| PATCF_BreastfeedAlertCategory_DR | bigint |  | FK | SI | Des Ref BreastfeedAlertCategory |
| PATCF_CancelPaymUponCancelBill | varchar |  |  | SI | CancelPaymUponCancelBill |
| PATCF_CancelWListStatus_DR | bigint |  | FK | SI | Des Ref CancelWListStatus |
| PATCF_CanclAdmOnCanclOTAppt | varchar |  |  | SI | CanclAdmOnCanclOTAppt |
| PATCF_CareProvType | varchar |  |  | SI | CareProvType |
| PATCF_CashRecptDiscntReadOnly | varchar |  |  | SI | CashRecptDiscntReadOnly |
| PATCF_ChangeOPWLStDoneArrAppt | varchar |  |  | SI | ChangeOPWLStDoneArrAppt |
| PATCF_ChangeWLStDoneArrAppt | varchar |  |  | SI | Change WL Stat to Done upon Arrival Appt |
| PATCF_ChooseReferalDoctorFromList | varchar |  |  | SI | Choose Referal Doctor From List |
| PATCF_ClearRefHospOnRemove | varchar |  |  | SI | Clear Ref Hosp On Remove |
| PATCF_ClearWLApptDateOutPCancel | varchar |  |  | SI | Clear WLApptDate on Cancel From OutPat |
| PATCF_CollectRegistrFee | varchar |  |  | SI | Collect Registration Fee |
| PATCF_CompleteOnZeroBills | varchar |  |  | SI | Complete On Zero Bills |
| PATCF_ComputersInWard | varchar |  |  | SI | Computers in Ward |
| PATCF_ConfirmCreateAliasName | varchar |  |  | SI | ConfirmCreateAliasName |
| PATCF_ConfirmCreateAliasSexDOB | varchar |  |  | SI | Confirm to Create Alias Sex/DOB |
| PATCF_ConfirmToSaveAsPreviousAddress | varchar |  |  | SI | ConfirmToSaveAsPreviousAddress |
| PATCF_ContactType_DR | bigint |  | FK | SI | Des Ref ContactType |
| PATCF_ConvertCurrencyInBilling | varchar |  |  | SI | Convert Currency In Billing |
| PATCF_CopyAlrgAlrtToBothPatU | varchar |  |  | SI | Copy Alrg/Alrt To Both Pat on Unmerge |
| PATCF_CopyDiagToInPatAdm | varchar |  |  | SI | CopyDiagToInPatAdm |
| PATCF_CopyPayorPlanDetFromPrevAdm | varchar |  |  | SI | CopyPayorPlanDetFromPrevAdm |
| PATCF_CopyPayorPlanFromPrevAdm | varchar |  |  | SI | CopyPayorPlanFromPrevAdm |
| PATCF_CreateAliasForNameFields5To8 | varchar |  |  | SI | Create Alias For Name Fields 5,6,7,8 |
| PATCF_CurrentEpOutpatAPPT_DWB | varchar |  |  | SI | Current Ep/OutpatAPPT in DWB |
| PATCF_CutOffTimeDischarge | time |  |  | SI | Cut Off Time for Automatice Discharge |
| PATCF_DEMAWorkFlow_DR | bigint |  | FK | SI | Clinical Pathway DEMA Workflow |
| PATCF_DPLSearchByHospitalUseWard | varchar |  |  | SI | Use Wards instead of Locations when searching for ... |
| PATCF_DVANumberVerMeth | varchar |  |  | SI | DVA Number Verification Method |
| PATCF_DailyCounterLength | double |  |  | SI | Daily Counter Length |
| PATCF_DaySurgeryType_DR | bigint |  | FK | SI | Des Ref Epis SubType |
| PATCF_DaysAgreedEDD | double |  |  | SI | Days AgreedEDD |
| PATCF_DaysAllowChangeTCI | double |  |  | SI | DaysAllowChangeTCI |
| PATCF_DaysStatDischPreAdmCheck | integer |  |  | SI | Days Statistical Discharge Pre-Admission Check |
| PATCF_DaysToClosePregnEvent | double |  |  | SI | DaysToClosePregnEvent |
| PATCF_DaysToIncludeDischPat | double |  |  | SI | Number of Days To Include Discharged Patients |
| PATCF_DeceasedWaitList_DR | bigint |  | FK | SI | des ref Deceased WaitList |
| PATCF_Def2ndTabEpisDetails | varchar |  |  | SI | Default 2nd Tab in Episode Details |
| PATCF_DefAdmDepartBDMAN | varchar |  |  | SI | Default Adm Depart in BDMAN |
| PATCF_DefNewBornDep_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PATCF_DefOperResource_DR | bigint |  | FK | SI | Des Ref RB_Resource |
| PATCF_DefProcDateSameDay | varchar |  |  | SI | Default Procedure Date if SameDay |
| PATCF_DefaultDepartUser | varchar |  |  | SI | use Default Department as User login location |
| PATCF_DefaultDiscretOutType | bigint |  |  | SI | Des Ref OUTS type |
| PATCF_DefaultEMQuePriorityDR | bigint |  | FK | SI | Default Emergency Que Priority |
| PATCF_DefaultIPVisitTypeDR | bigint |  | FK | SI | Default Admitting Service |
| PATCF_DefaultInsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PATCF_DefaultNoLabels | double |  |  | SI | Default Number Of Labels |
| PATCF_DefaultNurseryWard | bigint |  |  | SI | Default Nursery Ward (On Assignment) |
| PATCF_DefaultOPQuePriorityDR | bigint |  | FK | SI | Default Out Patient Que Priority |
| PATCF_DefaultOPVisTypDR | bigint |  | FK | SI | Default Out Patient Visit Type |
| PATCF_DefaultPatTypeToWL | varchar |  |  | SI | Default Patient type into WL Entry |
| PATCF_DefaultPrintLanguageDR | varchar |  | FK | SI | Not Used Default Print Language |
| PATCF_DefaultReqStatus_DR | bigint |  | FK | SI | Des PAC TransReqStatus |
| PATCF_DefaultTabInRegistration | numeric |  |  | SI | Default Tab In Registration |
| PATCF_DefaultTariff_DR | bigint |  | FK | SI | Des REf Tariff |
| PATCF_DefaultUseDeptAsDefault | varchar |  |  | SI | Default Use Logon Dept As Default |
| PATCF_DefaultZipDescIntoAddress | varchar |  |  | SI | Default Zip Desc Into Address field |
| PATCF_DepositAllocAlert | varchar |  |  | SI | DepositAllocAlert |
| PATCF_Description | varchar |  |  | SI | Configuration Desc  |
| PATCF_DisQuest_DR | bigint |  | FK | SI | Des Ref Discharge Questionnaire |
| PATCF_DisableInsuranceOfficeCombo | varchar |  |  | SI | Disable Insurance Office Combo |
| PATCF_DisableMultiselectBills | varchar |  |  | SI | DisableMultiselectBills |
| PATCF_DisableRefLetDateLogic | varchar |  |  | SI | Disable Referral Letter Date Logic |
| PATCF_DischGracePeriod | double |  |  | SI | Disch Grace Priod |
| PATCF_DischargePolicy | varchar |  |  | SI | Discharge Policy |
| PATCF_DisconOrdersOnDischarge | varchar |  |  | SI | Discontinue Orders On Discharge |
| PATCF_DisplayEnhancedFP | varchar |  |  | SI | DisplayEnhancedFP |
| PATCF_DisplayRegDetAfterBedAssign | varchar |  |  | SI | Display Reg Details After Bed Assignment |
| PATCF_DisplayTheatreTimeExcWarn | varchar |  |  | SI | Display Theatre Time Exc Warning |
| PATCF_DisplayZipDescription | varchar |  |  | SI | DisplayZipDescription |
| PATCF_DoNotCreateTransAdmFromED | varchar |  |  | SI | Do Not Create Trans on Adm From DE |
| PATCF_DontCalculateICUhrs | varchar |  |  | SI | DontCalculateICUhrs |
| PATCF_DontDischOutPatOnDecease | varchar |  |  | SI | Do not discharge outpatient epis on decease |
| PATCF_DontDisplayInactiveAlias | varchar |  |  | SI | Dont Display Inactive Alias |
| PATCF_EMAdmNoDelim | varchar |  |  | SI | Emergency Admission Number Delimiter |
| PATCF_EMAdmNoLength | double |  |  | SI | Emergency Admission Number Length |
| PATCF_EMAdmNoPrefix | varchar |  |  | SI | Emergency Admission Number Prefix |
| PATCF_EMAdmNoSuffix | varchar |  |  | SI | Emergency Admission Number Suffix |
| PATCF_EligMechVentCopayment | varchar |  |  | SI | Eligible For Mechanical Vent Copayment |
| PATCF_EligMechVentCopaymentNICU | varchar |  |  | SI | EligMechVentCopaymentNICU |
| PATCF_EmergDischDetails | varchar |  |  | SI | Emergency Discharge Details |
| PATCF_EmergStandAlone | varchar |  |  | SI | Use Emergency As StandAlone  |
| PATCF_EmergencyOrder_DR | varchar |  | FK | SI | Des Ref ARCIM |
| PATCF_EmergencyPatBedOption | varchar |  |  | SI | Put Emergency Patient in Non-Emergency Bed |
| PATCF_EmergencySurChargeCode | varchar |  |  | SI | Emergency Surcharge Charge Code |
| PATCF_EnableMultipleDiscountsOuts | varchar |  |  | SI | Enable Multiple Discounts Outs |
| PATCF_EncTimelineEmergency_DR | bigint |  | FK | SI | Des Ref Timeline to open when emergency encounter ... |
| PATCF_EncTimelineInpatient_DR | bigint |  | FK | SI | Des Ref Timeline to open when inpatient encounter ... |
| PATCF_EncTimelineOpTheatre_DR | bigint |  | FK | SI | Des Ref Timeline to open when operating theatre en... |
| PATCF_EncTimelineOutpatient_DR | bigint |  | FK | SI | Des Ref Timeline to open when outpatient encounter... |
| PATCF_ErrorOnExtractCodingIncomplete | varchar |  |  | SI | Error on Extract if Coding Incomplete |
| PATCF_ExcludeLinkedEpisOrdersFromDischargeBehaviour | varchar |  |  | SI | Allows orders to remained unchanged upon discharge... |
| PATCF_ExemptionCounterType_DR | bigint |  | FK | SI | Des Ref CounterType |
| PATCF_ExtendDiagnosis | varchar |  |  | SI | Extend Diagnosis ListBox to Full Screen |
| PATCF_ExternalPatValid | varchar |  |  | SI | ExternalPatValid |
| PATCF_ExtrInterFixDevice | varchar |  |  | SI | ExtrInterFixDevice |
| PATCF_FemalePensionAge | double |  |  | SI | Female Pension Age |
| PATCF_FemaleSex_DR | bigint |  | FK | SI | Des Ref Sex |
| PATCF_FieldLength | numeric |  |  | SI | maximum Text Field Length |
| PATCF_FreqAttendAge | double |  |  | SI | FreqAttendAge |
| PATCF_FromThisAreaReadOnly | varchar |  |  | SI | FromThisArea flag ReadOnly |
| PATCF_GenerateAdmNo | varchar |  |  | SI | Generate Admission Number on |
| PATCF_GenerateRego | varchar |  |  | SI | Generate Registation Number on |
| PATCF_GestationMaxDays | double |  |  | SI | GestationMaxDays |
| PATCF_GestationMaxWeeks | double |  |  | SI | GestationMaxWeeks |
| PATCF_GestationMinDays | double |  |  | SI | Gestation MinDays |
| PATCF_GestationMinWeeks | double |  |  | SI | GestationMinWeeks |
| PATCF_GovExtract | varchar |  |  | SI | GovExtract |
| PATCF_GroupAliasNames | varchar |  |  | SI | Group Alias Names |
| PATCF_HICClaimCounter_DR | bigint |  | FK | SI | Des Ref HICClaimCounter |
| PATCF_HPLength | double |  |  | SI | HPLength |
| PATCF_HPPrefix | varchar |  |  | SI | HPPrefix |
| PATCF_HPSuffix | varchar |  |  | SI | HPSuffix |
| PATCF_HideEncRecCarePlan | varchar |  |  | SI | Option to hide "Clinical Summaries" menu action in... |
| PATCF_HideEncRecClinicalSummaries | varchar |  |  | SI | Option to hide "Clinical Summaries" menu action in... |
| PATCF_HideEncRecProblemTimeline | varchar |  |  | SI | Option to hide "Problem Timeline" menu action in t... |
| PATCF_HideSSPRestrictListMessages | varchar |  |  | SI | Show messages when results are hidden due to acces... |
| PATCF_HospLinkedThrBedDepAlloc | varchar |  |  | SI | Hospital linked thr Bed Dept Allocation |
| PATCF_IPAdmNo | varchar |  |  | SI | In Patient Admission Number |
| PATCF_IPAdmNoDelim | varchar |  |  | SI | In Patient Admission Number Delimiter |
| PATCF_IPAdmNoLength | double |  |  | SI | In Patient Admission Number Length |
| PATCF_IPAdmNoPrefix | varchar |  |  | SI | In Patient Admission Number Prefix |
| PATCF_IPAdmNoSuffix | varchar |  |  | SI | In Patient Admission Number Suffix |
| PATCF_IPInclDischPat | varchar |  |  | SI | Include Disch Pats for IP search |
| PATCF_IPNo | varchar |  |  | SI | In Patient Number |
| PATCF_IPNoLength | double |  |  | SI | In Patient Number Length |
| PATCF_IPNoOnly | varchar |  |  | SI | In Patient Number Only |
| PATCF_IPNoPrefix | varchar |  |  | SI | In Patient Number Prefix |
| PATCF_IPNoSuffix | varchar |  |  | SI | In Patient Number Suffix |
| PATCF_IPOPAdmNoSame | varchar |  |  | SI | In Pat / Out Pat Admission Number Same |
| PATCF_IPOPSame | varchar |  |  | SI | Same Numbers For In/Out Patient |
| PATCF_InclRecsAfterExtrctEndDate | varchar |  |  | SI | Include Records after Extract EndDate |
| PATCF_InpatFloorplanMovement | varchar |  |  | SI | Inpatient Episode FloorPlan Movement |
| PATCF_InpatientPriceDelay | integer |  |  | SI | Inpatient Price Delay (Lab Billing)
If left blank... |
| PATCF_InsuranceCardHolder | bigint |  |  | SI | Insurance Card Holder Code |
| PATCF_IntQuest_DR | bigint |  | FK | SI | Des Ref Intermediate Questionnaire |
| PATCF_InvoiceRounding | double |  |  | SI | InvoiceRounding |
| PATCF_IsDoctorMandatory | varchar |  |  | SI | Is Doctor Mandatory ? |
| PATCF_IsRefDoctorMandatory | varchar |  |  | SI | Is Referal Doctor Mandatory Field ? |
| PATCF_KeywordLength | double |  |  | SI | Ignore words shorter or equal to |
| PATCF_LabCounterType_DR | bigint |  | FK | SI | Des Ref LabCounterType |
| PATCF_LabEpisodeNumberMethod | varchar |  |  | SI | Lab Episode Number Method |
| PATCF_LabSubLength | double |  |  | SI | Lab Subject Length |
| PATCF_LabSubPrefix | varchar |  |  | SI | Lab Subject Prefix |
| PATCF_LabSubSuffix | varchar |  |  | SI | Lab Subject Suffix |
| PATCF_Language_DR | bigint |  | FK | SI | Des Ref Language |
| PATCF_LastCPPaidForED | varchar |  |  | SI | LastCPPaidForED |
| PATCF_LimitNoDaysForSearch | double |  |  | SI | Limit Number of Days for Search |
| PATCF_LinkEDOUTEpisToIP | varchar |  |  | SI | Link ED OUT Epis To IP |
| PATCF_LinkOTBookToExistPreAdm | varchar |  |  | SI | LinkOTBookToExistPreAdm |
| PATCF_MRCType1_DR | bigint |  | FK | SI | Des Ref MRCType1 |
| PATCF_MRCType2_DR | bigint |  | FK | SI | Des Ref Diag Type2 |
| PATCF_MREncEntryAutolockPeriod | integer |  |  | SI | Period before automatically locking encounter entr... |
| PATCF_MREncEntryAutolockUnits | varchar |  |  | SI | Units for automatically locking encounter entries |
| PATCF_MREncEntryLatencyInDays | integer |  |  | SI | Latency period for locking encounter entries |
| PATCF_MRROSAndPhyETerminology | varchar |  |  | SI | - |
| PATCF_MakeCurrOPAdmForOPDAttend | varchar |  |  | SI | MakeCurrOPAdmForOPDAttend |
| PATCF_MalePensionAge | double |  |  | SI | Male Pension Age |
| PATCF_MaleSex_DR | bigint |  | FK | SI | Des Ref CTSEX |
| PATCF_MaxDaysOnLeave | double |  |  | SI | Max Days On Leave w/o discharge |
| PATCF_MaxOperatingTimeMins | double |  |  | SI | Base Maximum Operating Time (minutes) |
| PATCF_MedicareNumberVerMeth | varchar |  |  | SI | Medicare Number Verification Method |
| PATCF_MotherBabyEpisAutoLink | varchar |  |  | SI | MotherBabyEpisAutoLink |
| PATCF_MoveDelUpdFromPrevTrans | varchar |  |  | SI | Movement Deletion Update From Previous Transaction |
| PATCF_NAllORBookNA | varchar |  |  | SI | Do Not Allow ORBookings in Not Avail area |
| PATCF_NAllORBookNoSess | varchar |  |  | SI | Do Not Allow ORBooking in Non Session area |
| PATCF_NAllORBookPast | varchar |  |  | SI | Do Not Allow ORBookings in the past |
| PATCF_NCPActivitiesLimit | integer |  |  | SI | NCP Max Number of Activities Supported |
| PATCF_NCPQuesGroup_DR | bigint |  | FK | SI | NCP Questionnaire Group DR |
| PATCF_NewBornEpisSubType_DR | bigint |  | FK | SI | Des Ref NewBornEpisSubType |
| PATCF_NextOfKin | varchar |  |  | SI | Next Of Kin |
| PATCF_NoCPAdm4PAPersonSearch | varchar |  |  | SI | NoCPAdm4PAPersonSearch |
| PATCF_NoDaysForAdmSearchToCopyFrom | double |  |  | SI | No of Days For Adms Search to Copy from |
| PATCF_NoEdTransaction | varchar |  |  | SI | No Ed Transaction |
| PATCF_NoExecuteOrdUponDisc | varchar |  |  | SI | Do Not Execute Orders UponDischarge |
| PATCF_NoFieldsPatName | double |  |  | SI | No of Fields for Patient Name |
| PATCF_NoGenPRNforEMergPats | varchar |  |  | SI | Do Not Generate PRN for Emergency Patients |
| PATCF_NoOfYearsAgeSearch | double |  |  | SI | No Of Years Age Search |
| PATCF_NoOrdersCopyFromOrigAdm | varchar |  |  | SI | NoOrdersCopyFromOrigAdm |
| PATCF_NoRowsDiagProc | double |  |  | SI | No of Rows to display for Diag and Proc |
| PATCF_NoSimultanCurrentIPEDAdms | varchar |  |  | SI | NoSimultanCurrentIPEDAdms |
| PATCF_NoTempLocUpdateOnPatArrival | varchar |  |  | SI | NoTempLocUpdateOnPatArrival |
| PATCF_NonProperIncisionPerc | varchar |  |  | SI | NonProperIncisionPerc |
| PATCF_NotPopDischDateTimeOnLeave | varchar |  |  | SI | NotPopDischDateTimeOnLeave |
| PATCF_NumberOfVisits | double |  |  | SI | NumberOfVisits |
| PATCF_NurseryBedCleanupHours | double |  |  | SI | Nursery Bed Cleanup Hours |
| PATCF_OPAdmNo | varchar |  |  | SI | Out Patient Admission Number |
| PATCF_OPAdmNoDelim | varchar |  |  | SI | Out Patient Admission Number Delimiter |
| PATCF_OPAdmNoLength | double |  |  | SI | Out Patient Number Length |
| PATCF_OPAdmNoPrefix | varchar |  |  | SI | Out Patient Admission Number Prefix |
| PATCF_OPAdmNoSuffix | varchar |  |  | SI | Out Patient Admission Number Suffix |
| PATCF_OPNo | varchar |  |  | SI | Out Patient Number |
| PATCF_OPNoLength | double |  |  | SI | Out Patient Number Length |
| PATCF_OPNoOnly | varchar |  |  | SI | Out Patient Number Only |
| PATCF_OPNoPrefix | varchar |  |  | SI | Out Patient Number Prefix |
| PATCF_OPNoSuffix | varchar |  |  | SI | Out Patient Number Suffix |
| PATCF_OTBookCancelReason_DR | bigint |  | FK | SI | Des Ref OTBookCancelReason |
| PATCF_OTCPayor | varchar |  |  | SI | Display OTC Payor |
| PATCF_OTDelayMargin | double |  |  | SI | Base OT Delay Margin (minutes) |
| PATCF_OTStartMargin | double |  |  | SI | Base OT Start Margin (minutes) |
| PATCF_OperLength | double |  |  | SI | Oper. Length |
| PATCF_OperPrefix | varchar |  |  | SI | Oper. Prefix |
| PATCF_OperRoom_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PATCF_OperSuffix | varchar |  |  | SI | Oper. Suffix |
| PATCF_OrderingWorkFlow_DR | bigint |  | FK | SI | Clinical Pathway Ordering Workflow |
| PATCF_OutpatientPriceDelay | integer |  |  | SI | Outpatient Price Delay (Lab Billing)
If left blan... |
| PATCF_PAAdmNoDelim | varchar |  |  | SI | Pre Admission Number Delimiter |
| PATCF_PAAdmNoLength | double |  |  | SI | Pre Admission Number Length |
| PATCF_PAAdmNoPrefix | varchar |  |  | SI | Pre Admission No Prefix |
| PATCF_PAAdmNoSuffix | varchar |  |  | SI | Pre Admission No Suffix |
| PATCF_PAPersonFindMinSearch | varchar |  |  | SI | PAPersonFindMinSearch |
| PATCF_PATMANReadOnly | varchar |  |  | SI | PATMAN ReadOnly |
| PATCF_ParentGuardianTitle | varchar |  |  | SI | Parent Guardian Title |
| PATCF_PatNamesOrder | varchar |  |  | SI | PatNamesOrder |
| PATCF_PatTypeEmerg | bigint |  |  | SI | Des Ref PatTypeEmerg |
| PATCF_PatTypeHealthProm | bigint |  |  | SI | Des Ref PatTypeHealthProm |
| PATCF_PatTypeInPat | bigint |  |  | SI | Des Ref PatTypeInPat |
| PATCF_PatTypeOutPat | bigint |  |  | SI | Des Ref PatTypeOutPat |
| PATCF_PathologyServiceDateType | varchar |  |  | SI | Pathology Service Date Type
A service date is use... |
| PATCF_PlacePatInHoldArea | varchar |  |  | SI | Place Patients In Holding Area |
| PATCF_PlacentaDetailsRequired | varchar |  |  | SI | PlacentaDetailsRequired  Note: When this property ... |
| PATCF_PlacentaDocumentationLimit | integer |  |  | SI | Placenta documentation required for babies born ov... |
| PATCF_PopulateAdmDocForNewWL | varchar |  |  | SI | PopulateAdmDocForNewWL |
| PATCF_PrLabNewPat | varchar |  |  | SI | Print Label for New Patient |
| PATCF_PregLength | integer |  |  | SI | Define the length of pregnancy (days) |
| PATCF_PregnancyAlertCategory_DR | bigint |  | FK | SI | Des Ref PregnancyAlertCategory |
| PATCF_PregnancyAlert_DR | bigint |  | FK | SI | Des Ref Patient Alert |
| PATCF_PregnancyCheckAgeFrom | double |  |  | SI | Pregnancy Check Age From |
| PATCF_PregnancyCheckAgeTo | double |  |  | SI | Pregnancy Check Age To |
| PATCF_PrematureGestation | integer |  |  | SI | Define the gestation at birth for premature baby (... |
| PATCF_PriceToDisplayOnRB | varchar |  |  | SI | Price To Display On RB |
| PATCF_PrintAdmSheetOnPaym | varchar |  |  | SI | Print Admission Sheet On Payment |
| PATCF_PrintAdmissionNotif | varchar |  |  | SI | Print the admission notification slip |
| PATCF_PrintAppointmentSlip | varchar |  |  | SI | Print Appointment Slip |
| PATCF_PrintAutom1 | varchar |  |  | SI | Automatic Print 1 On Registration |
| PATCF_PrintAutom2 | varchar |  |  | SI | Automatic Print 2 |
| PATCF_PrintBillOnPayment | varchar |  |  | SI | Print Bill On Payment |
| PATCF_PrintDischargeConf | varchar |  |  | SI | Print the discharge confirmation sheet |
| PATCF_PrintRBINQ01 | varchar |  |  | SI | Print RBINQ01 |
| PATCF_PrintRBINQ02 | varchar |  |  | SI | Print RBINQ02 |
| PATCF_PrintRBINQ03 | varchar |  |  | SI | Print RBINQ03 |
| PATCF_PrintReceipt | varchar |  |  | SI | Print Receipt |
| PATCF_PrintRegisCard | varchar |  |  | SI | Automatically Print Registration Card |
| PATCF_PrintWaitList | varchar |  |  | SI | PrintWaitList |
| PATCF_Process | varchar |  |  | SI | Combine Episodes and Processes |
| PATCF_ProcessLength | double |  |  | SI | Process Length |
| PATCF_ProcessPrefix | varchar |  |  | SI | Process Prefix |
| PATCF_ProcessSuffix | varchar |  |  | SI | Process Suffix |
| PATCF_ProofPrefix1 | varchar |  |  | SI | Proof Prefix 1 |
| PATCF_ProofPrefix2 | varchar |  |  | SI | Proof Prefix 2 |
| PATCF_ProperIncisionPerc | varchar |  |  | SI | ProperIncisionPerc |
| PATCF_Que1CounterMethod | varchar |  |  | SI | Queue Counter Method |
| PATCF_RBResource_DR | bigint |  | FK | SI | Des Ref Resource |
| PATCF_ReasonCancelBill | varchar |  |  | SI | Reason for Cancel Bill |
| PATCF_RefreshCashiierAfterOE | varchar |  |  | SI | RefreshCashiierAfterOE |
| PATCF_RefreshPATMANOE | varchar |  |  | SI | Refresh PATMAN after OE |
| PATCF_ResetWLDaysPriorIncrease | varchar |  |  | SI | Reset WL Days on Priority Increase |
| PATCF_RestCancerRegLogonHosp | varchar |  |  | SI | RestrictCancerRegLogonHosp |
| PATCF_RestWardDeptBook | varchar |  |  | SI | RestWardDeptBook |
| PATCF_RestrictAdmListForLogonHosp | varchar |  |  | SI | RestrictAdmListForLogonHosp |
| PATCF_RestrictLocList | varchar |  |  | SI | Restrict Loc List |
| PATCF_RestrictNegOutsAmt | varchar |  |  | SI | Restrict Neg Outs Amt |
| PATCF_RestrictPatManSearchByDefPatType | varchar |  |  | SI | RestrictPatManSearchByDefPatType |
| PATCF_RestrictSingleDiagType | varchar |  |  | SI | Restrict to Single Diagnosis Type |
| PATCF_ReversalInpatAdmCutOffTime | double |  |  | SI | ReversalInpatAdmCutOffTime |
| PATCF_RoundingAmount | double |  |  | SI | RoundingAmount |
| PATCF_RoundingPaymentAdjustment_DR | bigint |  | FK | SI | Des Ref RoundingPaymentAdjustment |
| PATCF_SMRReporting | varchar |  |  | SI | SMR Reporting |
| PATCF_SameBillPatientPayor | varchar |  |  | SI | Same Bill for Patient and Payor |
| PATCF_SameDayPreAdm | varchar |  |  | SI | SameDayPreAdm |
| PATCF_SaveOutPatEpUponInConv | varchar |  |  | SI | Save Outpatient Episode Upon InPat Conversion |
| PATCF_SaveRegNumExtDB | varchar |  |  | SI | Save Reg Num from Ext DB |
| PATCF_SearchByKeywords | varchar |  |  | SI | Search By Keywords |
| PATCF_SearchOnDays | double |  |  | SI | SearchOnDays |
| PATCF_SearchOnExactMRN | varchar |  |  | SI | SearchOnExactMRN |
| PATCF_SearchOnMonth | varchar |  |  | SI | Search On Month |
| PATCF_SearchStartswithRego | varchar |  |  | SI | Search on  Startswith Rego |
| PATCF_SetAppToBook | varchar |  |  | SI | SetAppToBook |
| PATCF_SetBOpStatDoneWhenAnaD | varchar |  |  | SI | SetBOpStatDoneWhenAnaDone |
| PATCF_ShowMRNumberFloorPlan | varchar |  |  | SI | Show MR Number on FloorPlan |
| PATCF_ShowMonthsWhenInactive | double |  |  | SI | Show Months When Inactive |
| PATCF_ShowNegativeInvUnpaid | varchar |  |  | SI | Show Negative Invoices when Unpaid is ticked |
| PATCF_ShowOEMessageOnAdmUpdate | varchar |  |  | SI | Show Order Entry  Message On Admission Update |
| PATCF_ShowPreAdmInfoOnEDBedRequest | varchar |  |  | SI | ShowPreAdmInfoOnEDBedRequest |
| PATCF_ShowPreadmAfterAppoint | varchar |  |  | SI | Show Preadm After Appoint |
| PATCF_ShowPreviousEMR | varchar |  |  | SI | Show Previous EMR |
| PATCF_ShowRefDoctorSpec | varchar |  |  | SI | Show Referral Doctor Specialty |
| PATCF_ShowRegWaitTimeFloorPlan | varchar |  |  | SI | Show Reg Waiting Timeon FloorPlan |
| PATCF_ShowWarnProcDateOutEpis | varchar |  |  | SI | Show Warning when Proc Date Out of Epis |
| PATCF_ShowZeroBillsUnpaid | varchar |  |  | SI | Show Zero Bills when Unpaid |
| PATCF_ShowreasonChangePatData | varchar |  |  | SI | Show Reason for Change Pat Data |
| PATCF_SkipPatientType | varchar |  |  | SI | Skip Patient Type |
| PATCF_SortByQueue | varchar |  |  | SI | Sort By Queue |
| PATCF_SortBySurnameFirstOther | varchar |  |  | SI | Sort by Surname First Other name |
| PATCF_StampDutyCharge_DR | varchar |  | FK | SI | Des Ref ARCIM |
| PATCF_StoreAppPayPlanOverAdm | varchar |  |  | SI | StoreAppPayPlanOverAdm |
| PATCF_StoreAppPayorPlanDoNotDefaultFromEpis | varchar |  |  | SI | Store Appointment’s Payor and Plan as Override and... |
| PATCF_SuppressMRRego | varchar |  |  | SI | Suppress MR same as Rego |
| PATCF_TBCAlrgAlertEpisMove | varchar |  |  | SI | TBCAlrgAlertEpisMove |
| PATCF_TenderPayment | varchar |  |  | SI | TenderPayment |
| PATCF_TimeBetweenExtDocRequests | integer |  |  | SI | Minimum Time between External Document Requests (H... |
| PATCF_TimeFrame | double |  |  | SI | TimeFrame |
| PATCF_TimeFrameType | varchar |  |  | SI | TimeFrameType |
| PATCF_TimeRoomChargeApply | time |  |  | SI | TimeRoomChargeApply |
| PATCF_TitleOfDeceasedPat | varchar |  |  | SI | Title Of Deceased Patient |
| PATCF_TransferReasonMandatory | varchar |  |  | SI | Transfer Reason Mandatory |
| PATCF_TrfCancelGracePeriod | double |  |  | SI | Bed Transfer Reversal Grace Period |
| PATCF_TriageWaitTime1st | double |  |  | SI | TriageWaitTime1st |
| PATCF_TriageWaitTime2nd | double |  |  | SI | TriageWaitTime2nd |
| PATCF_UnavailBedStatus | bigint |  |  | SI | Des Ref UnavailBedStatus |
| PATCF_UnknownSex_DR | bigint |  | FK | SI | Des Ref UnknownSex |
| PATCF_UpperLimitDisplayDays | double |  |  | SI | Upper Limit Display Days |
| PATCF_UpperLimitDisplayMonths | double |  |  | SI | Upper Limit Display Months |
| PATCF_UpperLimitDisplayWeeks | double |  |  | SI | Upper Limit Display Weeks |
| PATCF_UseAntibioticSeqInLab | varchar |  |  | SI | UseAntibioticSeqInLab |
| PATCF_UseBedManagementScreen | varchar |  |  | SI | Use Bed Management Screen |
| PATCF_UseBedReqDateTimeEm | varchar |  |  | SI | Use Bed Req Date Time f PreAdm from Emergency |
| PATCF_UseCRAFTFunctionality | varchar |  |  | SI | Use CRAFT Functionality |
| PATCF_UseClientBasedDRGGrouper | varchar |  |  | SI | Use Client Based DRG Grouper |
| PATCF_UseDRGGrouper | varchar |  |  | SI | Use DRG Grouper |
| PATCF_UseDischargeDateTimeAdm | varchar |  |  | SI | Use Discharge Date/Time on Admission |
| PATCF_UseMaxDaysOnLeaveDisch | varchar |  |  | SI | UseMaxDaysOnLeaveDisch |
| PATCF_UsePayorFromPrevEpisode | varchar |  |  | SI | UsePayorFromPrevEpisode |
| PATCF_UseSoundexSearchAllNames | varchar |  |  | SI | UseSoundexSearchAllNames |
| PATCF_UseUserDefPayor | varchar |  |  | SI | Use User Default Payor |
| PATCF_UseWIESVICDRGFunction | varchar |  |  | SI | Use WIES and VIC-DRG functionality |
| PATCF_VerifyNewAdmissions | varchar |  |  | SI | Verify New Admissions |
| PATCF_WLChangeToRemovedOnDepartReason_DR | bigint |  | FK | SI | Des Ref PACWLReasonNotAvail |
| PATCF_WLReverseRemovedOnDepartReason_DR | bigint |  | FK | SI | Des Ref PACWLReasonNotAvail |
| PATCF_WLSortByDays | varchar |  |  | SI | WLSortByDays |
| PATCF_WLStatInitOnCancel | varchar |  |  | SI | Set WL Status to Initial OnCancel |
| PATCF_WLStatOnAdm_DR | bigint |  | FK | SI | Des Ref WLStatOnAdm |
| PATCF_WSGridLength | double |  |  | SI | Lab worksheet Grid Length |
| PATCF_WSGridPrefix | varchar |  |  | SI | Lab WorkSheet Grid Prefix |
| PATCF_WSGridSuffix | varchar |  |  | SI | Lab WorkSheet Grid Suffix |
| PATCF_WarnORBookingMoveRes | varchar |  |  | SI | Warn if user moves ORBooking to another Res |
| PATCF_YearsSinceLastEpisode | double |  |  | SI | YearsSinceLastEpisode |
| PATCF_ZipCodesSetup | varchar |  |  | SI | Zip Codes Setup |
| Q81Q1 | - |  |  | SI | Programa de Salud |
| Q81Q2 | - |  |  | SI | Tipo de Atención |
| Q81Q3 | - |  |  | SI | ID MRC_EncEntryType |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*