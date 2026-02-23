# SQLUser.SS_Group

**Schema:** SQLUser
**Columnas:** 244
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSGRP_RowId | bigint | PK |  | NO | - |
| SSGRP_AddAmend | varchar |  |  | SI | AddAmend |
| SSGRP_AddClinicsShowCPGroupOnly | varchar |  |  | SI | Allow Additional Clinics to Show Care Provider Dep... |
| SSGRP_AdjCompletedStockItemsOnly | varchar |  |  | SI | Adjust completed stock items only |
| SSGRP_AdjReverseComplete | varchar |  |  | SI | Allow AdjReverseComplete |
| SSGRP_AllocEpisDeposOtherEpis | varchar |  |  | SI | Allow to Allocate Episode Deposit To Another Episo... |
| SSGRP_AllocateAnyPatientType | varchar |  |  | SI | [DEPRECATED]Replaced by SSPAllocateAnyPatientType ... |
| SSGRP_AllocateOrderToBatch | varchar |  |  | SI | Allocate Order ToBatch |
| SSGRP_AllowActivateVolume | varchar |  |  | SI | Allow Activate Volume |
| SSGRP_AllowAddStockItem | varchar |  |  | SI | Allow to Add Stock Item to Location |
| SSGRP_AllowAdmitAllInPatPreAdm | varchar |  |  | SI | AllowAdmitAllInPatPreAdm |
| SSGRP_AllowApptChangeOrdDate | varchar |  |  | SI |  THIS PROPERTY IS NEVER USED:
 Permission to Igno... |
| SSGRP_AllowArchiveProblems | varchar |  |  | SI | Allow this user group to archive problems in probl... |
| SSGRP_AllowBookForDeceasedPatient | varchar |  |  | SI | Allow Booking For Deceased Patient |
| SSGRP_AllowBookOutsideRange | varchar |  |  | SI | Allow to Book Outside Range |
| SSGRP_AllowBookPastGuarDateOP | varchar |  |  | SI | AllowBookPastGuarDateOP |
| SSGRP_AllowBookPastGuarDateWL | varchar |  |  | SI | AllowBookPastGuarDateWL |
| SSGRP_AllowChangeDepOT | varchar |  |  | SI | Allow to Change Dep in OT |
| SSGRP_AllowCreateOtherNumbers | varchar |  |  | SI | Allowed to Create Other Numbers |
| SSGRP_AllowDeleteBedTransactions | varchar |  |  | SI | Allow Delete Bed Transactions |
| SSGRP_AllowDeleteDiagOtherUs | varchar |  |  | SI | Allow to Delete Diagnosis entered byOtherUser |
| SSGRP_AllowDeleteEpisode | varchar |  |  | SI | Allowed to Delete Episode/Process |
| SSGRP_AllowDiscOrdPackedPres | varchar |  |  | SI | Allow discontinue order of packed prescrips |
| SSGRP_AllowDiscPaidOrder | varchar |  |  | SI | AllowDiscPaidOrder |
| SSGRP_AllowEditEpLogLoc | varchar |  |  | SI | Allow only edit adms in login Location |
| SSGRP_AllowEditOTOrders | varchar |  |  | SI | Allow Edit OT Orders from AnaesSummaryOrders.List,... |
| SSGRP_AllowEditPriceGR | varchar |  |  | SI | Allow to Edit Price in  GR |
| SSGRP_AllowEditWLStatusTreated | varchar |  |  | SI | AllowEditWLStatusTreated |
| SSGRP_AllowIssueArchiveMR | varchar |  |  | SI | Allow to Issue Archived MR |
| SSGRP_AllowMultipleServAdhoc | varchar |  |  | SI | AllowMultipleServAdhoc |
| SSGRP_AllowNewMRTypesPat | varchar |  |  | SI | Allow to create new MR Types for Patient |
| SSGRP_AllowNurseManufacturing | varchar |  |  | SI | Allow to Perform Nurse Manufacturing |
| SSGRP_AllowOSFEdit24hrs | varchar |  |  | SI | Allow Obj Subj Findings Edit Within 24hrs |
| SSGRP_AllowOverBookOnSlotZero | varchar |  |  | SI | Allow Overbook when Slots Override r Zero |
| SSGRP_AllowOverBookRB | varchar |  |  | SI | Allow Over BookRB |
| SSGRP_AllowOverPayorRestrict | varchar |  |  | SI | Allow to Override Payor Restrictions |
| SSGRP_AllowRescAdmAfterLateAdm | varchar |  |  | SI | Allowed to Reschedule Administration after Late Ad... |
| SSGRP_AllowSendMsgAll | varchar |  |  | SI | Allow Send Msg to All users |
| SSGRP_AllowToAddItemToLocPortfolio | varchar |  |  | SI | Allow To Add Item To Location Portfolio |
| SSGRP_AllowToAddItemToVendPortfolio | varchar |  |  | SI | Allow To Add Item To Vend Portfolio |
| SSGRP_AllowToChangeAgrPrice | varchar |  |  | SI | AllowToChangeAgrPrice |
| SSGRP_AllowToChangeFamilyDoctor | varchar |  |  | SI | Allow To Change Family Doctor |
| SSGRP_AllowToChangeOEStatus | varchar |  |  | SI | AllowToChangeStatus |
| SSGRP_AllowToCreateAdhocAdmixture | varchar |  |  | SI | Allow to Create Adhoc Admixture  |
| SSGRP_AllowToExecuteOrderOutsideShift | varchar |  |  | SI | Allow To Execute Order Outside Shift |
| SSGRP_AllowToModifyAdmixSolvent | varchar |  |  | SI | Allow to Add/Modify Admixture Solvent after Orderi... |
| SSGRP_AllowToModifyAdmixSolventRoutes | varchar |  |  | SI | Allow to Add/Modify Admixture Solvent after Orderi... |
| SSGRP_AllowToModifyAdmixture | varchar |  |  | SI | Allow to Modify Admixture (When Manufacturing)   |
| SSGRP_AllowToModifyFixedRecipeAdmixture | varchar |  |  | SI | Allow to Modify Fixed Recipe Admixture (When Presc... |
| SSGRP_AllowToReverseReadyInvoice | varchar |  |  | SI | Allow to Reverse Ready for Invoicing |
| SSGRP_AllowUndoAppt | varchar |  |  | SI | Allow Undo Appointment |
| SSGRP_AllowViewVIPPatients | varchar |  |  | SI | Allow to View VIP Patients |
| SSGRP_AllowWebColumnManager | varchar |  |  | SI | Allow Web Column Manager |
| SSGRP_AllowWebLayoutManager | varchar |  |  | SI | Allow Web Layout Manager |
| SSGRP_AllowedAddOrdersReview | varchar |  |  | SI | Allowed To Add Orders after Review flag |
| SSGRP_AllowedSeeSEnsitRes | varchar |  |  | SI | Allow See Sensitive Results |
| SSGRP_AllowedSeeSensitAntib | varchar |  |  | SI | AllowedSeeSensitAntib |
| SSGRP_AllowedSeeSensitOrd | varchar |  |  | SI | Allowed See Sensitive Orders |
| SSGRP_AllowedSeeSensitTask | varchar |  |  | SI | Allowed See Sensitive Tasks |
| SSGRP_AllowedtoBookOR | varchar |  |  | SI | Allowed to Book Operation Times |
| SSGRP_AnMethodIsntMandOT | varchar |  |  | SI | Anaest Method Isnt Mandatory in OT booking |
| SSGRP_ApptAutofind | varchar |  |  | SI | Appt Autofind |
| SSGRP_ApptPast | varchar |  |  | SI | Appt Past |
| SSGRP_AutoMedDischarge | varchar |  |  | SI | Auto Med Discharge |
| SSGRP_AutoPatientDeposAlloc | varchar |  |  | SI | Automatic Patient Deposit Allocation |
| SSGRP_BlockEncounterRecordEntryItemEditsAfterLock | varchar |  |  | SI | Block Encounter Record Entry Item Edits After Lock |
| SSGRP_Breached | varchar |  |  | SI | Breached |
| SSGRP_ByPassHardStop | bit |  |  | SI | Allow to bypass Allergy Nature of Reaction Hard St... |
| SSGRP_CanDeleteLockedACNEntries | varchar |  |  | SI | Can delete locked ACN entries of other Users |
| SSGRP_CanEditDeletePreAuth | varchar |  |  | SI | Can Edit/Delete Preauthorization |
| SSGRP_CartAutoSave | varchar |  |  | SI | AutoSave Inactive Items to Interim Cart |
| SSGRP_CartExpiryDays | integer |  |  | SI | Days to Purge Cart Items |
| SSGRP_CartExpiryHours | integer |  |  | SI | Hours to Purge Cart Items |
| SSGRP_CashierCustomPrintRcpt | varchar |  |  | SI | CashierCustomPrintRcpt |
| SSGRP_ChangeDataAfterDischarge | varchar |  |  | SI | Allow To Change Data AfterPatient Discharge |
| SSGRP_CheckApproved | varchar |  |  | SI | CheckApproved |
| SSGRP_CheckOrdersCovered | varchar |  |  | SI | Check if Orders are Covered |
| SSGRP_ChkFutureAppts | varchar |  |  | SI | Check for Future Appointments |
| SSGRP_ClinicalLocListDr | bigint |  |  | SI | Clinical Loc List DR |
| SSGRP_ClosePatList1PatReturned | varchar |  |  | SI | ClosePatList1PatReturned |
| SSGRP_ConsReasonMandatory | varchar |  |  | SI | Consumption Reason Mandatory |
| SSGRP_ConsReverseComplete | varchar |  |  | SI | Allow ConsReverseComplete |
| SSGRP_CreateMRNLookUpForDoNotCreateVol | varchar |  |  | SI | Create MRN - Look Up For Do Not Create Volume Only |
| SSGRP_CumAcrossAllEpisodes | varchar |  |  | SI | not used |
| SSGRP_CumAllowedSeeGraphLink | varchar |  |  | SI | not used |
| SSGRP_CumIncludeRPrefix | varchar |  |  | SI | not used |
| SSGRP_CumNoColumns | double |  |  | SI | not used |
| SSGRP_CumRefRangePosition | varchar |  |  | SI | not used |
| SSGRP_DFLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPDFLocLis... |
| SSGRP_DateFrom | date |  |  | SI | Date From |
| SSGRP_DateTo | date |  |  | SI | Date To |
| SSGRP_DefAdminStat_DR | bigint |  | FK | SI | BPOC Des Ref to Administration Status |
| SSGRP_DefaultDoseEquiv | varchar |  |  | SI | Use Default Dose Equivalent |
| SSGRP_DefaultPOReference_DR | bigint |  | FK | SI | Des Ref DefaultPOReference |
| SSGRP_Desc | varchar |  |  | NO | Group DescriptionSESSParRef |
| SSGRP_DiaryEndTime | time |  |  | SI | Diary End Time |
| SSGRP_DiarySlotLength | double |  |  | SI | Diary Slot Length |
| SSGRP_DiaryStartTime | time |  |  | SI | Diary Start Time |
| SSGRP_DisReverseComplete | varchar |  |  | SI | Allow DisReverseComplete |
| SSGRP_DisableAddAll | varchar |  |  | SI | Disable Add All on OE |
| SSGRP_DisableFindStAdj | varchar |  |  | SI | DisableFindStAdj |
| SSGRP_DisableFindStCons | varchar |  |  | SI | DisableFindStCons |
| SSGRP_DisableFindStDisp | varchar |  |  | SI | DisableFindStDisp |
| SSGRP_DisableModifyOrdFinDisch | varchar |  |  | SI | Disable ability to modify orders after financial d... |
| SSGRP_DischargeLocList | bigint |  |  | SI | Discharge Location List |
| SSGRP_DiscontinueExecOrders | varchar |  |  | SI | DiscontinueExecOrders |
| SSGRP_DisplayApptBooking | varchar |  |  | SI | Display Appointment Bookings in Calendar |
| SSGRP_DisplayDiagnProcDRG | varchar |  |  | SI | Display Diagn Proc DRG |
| SSGRP_DisplayDiagnosis | varchar |  |  | SI | Display Diagnosis |
| SSGRP_DisplayOEfromRBAfterAp | varchar |  |  | SI | DisplayOEfromRBAfterApptCreated |
| SSGRP_DisplayParityBannerPatNotPreg | varchar |  |  | SI | Display Parity in Banner when Patient not Pregnant |
| SSGRP_DisplayPatmanActiveCWB | varchar |  |  | SI | DisplayPatmanActiveCWB |
| SSGRP_DisplayQnsOnAlertScreen | varchar |  |  | SI | DisplayQnsOnAlertScreen |
| SSGRP_DisplayQnsOnSumScreen | varchar |  |  | SI | DisplayQnsOnSumScreen |
| SSGRP_DisplayServiceDetails | varchar |  |  | SI | Display Service Details in Calendar |
| SSGRP_DisplaySessionofLogonCP | varchar |  |  | SI | Display Resource Session Defaults Based on Logon C... |
| SSGRP_DisplayTransIconOPDiaryGrid | varchar |  |  | SI | DisplayTransIconOPDiaryGrid |
| SSGRP_DoNotClearPatManUponUpdate | varchar |  |  | SI | DoNotClearPatManUponUpdate |
| SSGRP_DoNotUpdateDOCTORWithLinkedCP | varchar |  |  | SI | DoNotUpdateDOCTORWithLinkedCP |
| SSGRP_DontAllowContactInDiffHosp | varchar |  |  | SI | Do not Allow Contact to be created when Log On Hos... |
| SSGRP_DontBookOutsideOTSchedule | varchar |  |  | SI | DontBookOutsideOTSchedule |
| SSGRP_DontShowInactiveDiagInInvSum | varchar |  |  | SI | Do Not Display Inactive Diagnosis in Invoice Summa... |
| SSGRP_EMRIgnoreRestrForAdm | varchar |  |  | SI | EMRIgnoreRestrForAdm |
| SSGRP_EmergencyLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPEmergenc... |
| SSGRP_EnableSystemCT | varchar |  |  | SI | Enable System CT |
| SSGRP_FirstMenu | double |  |  | SI | First Menu |
| SSGRP_FirstMenuType | varchar |  |  | SI | First Menu Type |
| SSGRP_FloorPlanDisplayOnly | varchar |  |  | SI | ED Floor Plan Display Only |
| SSGRP_FreezeReverseComplete | varchar |  |  | SI | Allow FreezeReverseComplete |
| SSGRP_GP | varchar |  |  | SI | GP group |
| SSGRP_HealthPromLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPHealthPr... |
| SSGRP_IPFloorPlanDisplayOnly | varchar |  |  | SI | IPFloorPlanDisplayOnly |
| SSGRP_IgnoreOrderRestrictions | varchar |  |  | SI | Ignore Order Restrictions |
| SSGRP_InPatLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPInPatLoc... |
| SSGRP_InPatTransferList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPInPatTra... |
| SSGRP_InactivityTimeOut | varchar |  |  | SI | [DEPRECATED]Redundant VB field removed in TrakCare... |
| SSGRP_IssRetReverseComplete | varchar |  |  | SI | Allow IssRetReverseComplete |
| SSGRP_JobOE | varchar |  |  | SI | Job aOET11 in OE |
| SSGRP_LabQueues | varchar |  |  | SI | Lab Queues Definition |
| SSGRP_LayoutRestrictions | varchar |  |  | SI | Layout Restrictions. Comma delimited string of val... |
| SSGRP_LocMandatoryPOInquiry | varchar |  |  | SI | LocMandatoryPOInquiry |
| SSGRP_LocMandatoryPOSearch | varchar |  |  | SI | LocMandatoryPOSearch |
| SSGRP_MainAnaestIsntMandOT | varchar |  |  | SI | Main Anaestethist Isnt Mandator in OT booking |
| SSGRP_MainSurgeonIsNotMandOT | varchar |  |  | SI | Main Surgeon Is Not Mandatory in OT booking |
| SSGRP_MaxPOAmount | double |  |  | SI | MaxPOAmount |
| SSGRP_MinimizeOEUpdate | varchar |  |  | SI | Minimize Order Entry on Update |
| SSGRP_MoveToDefaultBed | varchar |  |  | SI | MoveToDefaultBed |
| SSGRP_NAllAddPastAppt | varchar |  |  | SI | Not Allow to Add Past Appt |
| SSGRP_NAllORBookNA | varchar |  |  | SI | Do Not Allow ORBookings in Not Avail area |
| SSGRP_NAllORBookNoSess | varchar |  |  | SI | Do Not Allow ORBooking in Non Session area |
| SSGRP_NAllORBookPast | varchar |  |  | SI | Do Not Allow OR Bookings in Past |
| SSGRP_NAllowEntServToPkgWithApprovedStat | varchar |  |  | SI | Allowed to Enter Services to Packages with Approve... |
| SSGRP_NoDisplayReasonStAdj | varchar |  |  | SI | NoDisplayReasonStAdj |
| SSGRP_NoDisplayReasonStCons | varchar |  |  | SI | NoDisplayReasonStCons |
| SSGRP_NoDisplayReasonStDisp | varchar |  |  | SI | NoDisplayReasonStDisp |
| SSGRP_NoRestrictUserSameGroupOE | varchar |  |  | SI | NoRestrictUserSameGroupOE |
| SSGRP_NotActNonFinanceAppOI | varchar |  |  | SI | Do Not Action Non Finance Approve Order Item |
| SSGRP_NotAllowOverbookPast | varchar |  |  | SI | Do Not Allow to Overbook Appointments in the Past |
| SSGRP_NotBookOutSess | varchar |  |  | SI | Do Not Allow Booking Outside of Session Time |
| SSGRP_NotExcLoadLevelOverrides | varchar |  |  | SI | do Not Exceed LoadLevel for slot Overrides |
| SSGRP_NotLoadOrderDetails | varchar |  |  | SI | Do Not Load Order Details Automatically |
| SSGRP_NotOTOPBookOutSess | varchar |  |  | SI | Do Not Allow OT Bookings for OP Outside OT Schedul... |
| SSGRP_OEDontSkipUponUDFReject | varchar |  |  | SI | OEDontSkipUponUDFReject |
| SSGRP_OEMEUIStartTab | varchar |  |  | SI | Order Entry MEUI Start Tab |
| SSGRP_OPLocList_DR | bigint |  | FK | SI | Des Ref OPLocList |
| SSGRP_OTFloorPlanDisplayOnly | varchar |  |  | SI | OTFloorPlanDisplayOnly |
| SSGRP_OffsetFuture | numeric |  |  | SI | BPOC Offset Future Minutes |
| SSGRP_OffsetPast | numeric |  |  | SI | BPOC Offset Past Minutes |
| SSGRP_OnePOforEveryVendor | varchar |  |  | SI | OnePOforEveryVendor |
| SSGRP_OnlyInpatUnitsForMyHospital | varchar |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPOnlyInpa... |
| SSGRP_OnlyOutpatUnitsForMyHospital | varchar |  |  | SI | Only OutPat Units For My Hospital |
| SSGRP_OpenSlotsbyOPDSessRoomHosp | varchar |  |  | SI | Search Open Slots by OPD Session Room's Hospital   |
| SSGRP_OrdersPrevEpisode | varchar |  |  | SI | Display Orders from Previous Episode |
| SSGRP_OutPatLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPOutPatLo... |
| SSGRP_OverrideAccessProfile_DR | bigint |  | FK | SI | Break The Glass Access Profile |
| SSGRP_OverrideDepositExpDate | varchar |  |  | SI | Override Deposit Expirary Date |
| SSGRP_OverrideSecurityGroup_DR | bigint |  | FK | SI | Des Ref SSGroup |
| SSGRP_Owner | varchar |  |  | SI | Owner |
| SSGRP_POReverseComplete | varchar |  |  | SI | Allow POReverseComplete |
| SSGRP_PasswordDaysToExpire | double |  |  | SI | PasswordDaysToExpire |
| SSGRP_PatTypeRestrictOPD | varchar |  |  | SI | [DEPRECATED]Replaced by User.SSProfilePatTypeRestr... |
| SSGRP_PatTypeRestrictPF | varchar |  |  | SI | [DEPRECATED]Replaced by SSPPatTypeRestrictPF in SS... |
| SSGRP_PatTypeRestrictWL | varchar |  |  | SI | [DEPRECATED]Replaced by User.SSProfilePatTypeRestr... |
| SSGRP_PerformanceStatisticsDisplay | varchar |  |  | SI | Display performance statistics even if system-wide... |
| SSGRP_PhoneOrdSecondSignOptional | varchar |  |  | SI | Second Signature Optional for Phone Orders  |
| SSGRP_PleaseReuse1 | varchar |  |  | SI | Please reuse this property |
| SSGRP_PleaseReuse2 | varchar |  |  | SI | Please reuse this property |
| SSGRP_PleaseReuse3 | varchar |  |  | SI | Please reuse this property |
| SSGRP_PleaseReuse4 | varchar |  |  | SI | Please reuse this property |
| SSGRP_Price | varchar |  |  | SI | Show Order Price NO LONGER USED TC-8801 |
| SSGRP_Purpose | varchar |  |  | SI | Purpose |
| SSGRP_RadLocList | bigint |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPRadLocLi... |
| SSGRP_RecReverseComplete | varchar |  |  | SI | Allow RecReverseComplete |
| SSGRP_RecordSchedBrief | varchar |  |  | SI | Record Theatre Session De/Brief Form |
| SSGRP_RequireSecondSignCN | varchar |  |  | SI | Require Second Sign CN |
| SSGRP_RestrictApptRadOrders | varchar |  |  | SI | Restrict Appt for Radiology Orders |
| SSGRP_RestrictLocForGrHospitals | varchar |  |  | SI | Restrict Locations for Group Hospitals |
| SSGRP_RestrictMRTypeCurrHosp | varchar |  |  | SI | RestrictMRType to Current Hospital |
| SSGRP_RestrictModifDischarge | varchar |  |  | SI | Restrict Modification after Discharge |
| SSGRP_RestrictSearchEMR | varchar |  |  | SI | Restrict Search EMR |
| SSGRP_RestrictWardsToDepartment | varchar |  |  | SI | RestrictWardsToDepartment |
| SSGRP_RetReverseComplete | varchar |  |  | SI | Allow RetReverseComplete |
| SSGRP_RetainOrderCategory | varchar |  |  | SI | Retain Order Category |
| SSGRP_ReturnSearchListLogonHosp | varchar |  |  | SI | ReturnSearchListLogonHosp |
| SSGRP_RingWardFlag | varchar |  |  | SI | RingWardFlag |
| SSGRP_RoundingAutomatic | varchar |  |  | SI | RoundingAutomatic |
| SSGRP_RoundingOnPayment | varchar |  |  | SI | RoundingOnPayment |
| SSGRP_SecurityLevel | numeric |  |  | SI | Security Level |
| SSGRP_SelectAllEpisodesEMR | varchar |  |  | SI | Select All Episodes in EMR |
| SSGRP_ShowAllLocations | varchar |  |  | SI | Show All Locations in Patient Registration |
| SSGRP_ShowAllPatientsInNWB | varchar |  |  | SI | Show All patients in assigned ward in NWB |
| SSGRP_ShowAllergy_DSS_QA | varchar |  |  | SI | ShowAllergy_DSS_QA |
| SSGRP_ShowAntibioSensVertically | varchar |  |  | SI | Show the antibiotic sensitivity table with the ant... |
| SSGRP_ShowMIC | varchar |  |  | SI | ShowMIC |
| SSGRP_ShowOnlyIPUnitsForWL | varchar |  |  | SI | ShowOnlyIPUnitsForWL |
| SSGRP_ShowPatientSearch | varchar |  |  | SI | Auto Show Patient Search in Registration |
| SSGRP_ShowPreadmafterAppoint | varchar |  |  | SI | Show Preadm After Appoint |
| SSGRP_ShowRejectTransactions | varchar |  |  | SI | ShowRejectTransactions |
| SSGRP_StWardReverseComplete | varchar |  |  | SI | Allow StWardReverseComplete |
| SSGRP_StaffWorkloadAlertThresholds | varchar |  |  | SI | StaffWorkloadAlertThresholds |
| SSGRP_StockDecimalPlaces | double |  |  | SI | Number of decimal places used by currency conversi... |
| SSGRP_SuppressPin | varchar |  |  | SI | SuppressPin |
| SSGRP_TakeAdjReverseComplete | varchar |  |  | SI | Allow TakeAdjReverseComplete |
| SSGRP_TakeCntReverseComplete | varchar |  |  | SI | Allow TakeCntReverseComplete |
| SSGRP_TakeEnterReverseComplete | varchar |  |  | SI | Allow TakeEnterReverseComplete |
| SSGRP_TempPatLocList | bigint |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPTempPatL... |
| SSGRP_TrAckReverseComplete | varchar |  |  | SI | Allow TrAckReverseComplete |
| SSGRP_TrReqReverseComplete | varchar |  |  | SI | Allow TrReqReverseComplete |
| SSGRP_TransReverseComplete | varchar |  |  | SI | Allow TransReverseComplete |
| SSGRP_TreatmentPathwayOwner | varchar |  |  | SI | TreatmentPathwayOwner |
| SSGRP_TreatmentStageOwner | varchar |  |  | SI | TreatmentStage |
| SSGRP_UpdateOrderDetails | varchar |  |  | SI | Update Order Details |
| SSGRP_UserPOReferenceNotMandatory | varchar |  |  | SI | UserPOReferenceNotMandatory |
| SSGRP_WLAuditLetterDays | double |  |  | SI | WL Audit Letter Days |
| SSGRP_WLStatusList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPWLStatus... |
| SSGRP_WaitListLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPWaitList... |
| SSGRP_WaitListStatus_DR | bigint |  | FK | SI | Des Ref WaitListStatus |
| SSGRP_WardAttendLocList_DR | bigint |  | FK | SI | Des Ref WardAttendLocList |
| SSGRP_WardPlaceLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPWardPlac... |
| SSGRP_WardViewLocList_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPWardView... |
| SSGRP_WarnFutureAppt | varchar |  |  | SI | Warning if Future Appt exist |
| SSGRP_WarnORBookingMoveRes | varchar |  |  | SI | Warn if user moves ORBooking to another Res |
| SSUSR_MaxAmountRoundedFrom | varchar |  |  | SI | MaxAmountRoundedFrom |
| SSUSR_MaxAmountRoundedTo | varchar |  |  | SI | MaxAmountRoundedTo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*