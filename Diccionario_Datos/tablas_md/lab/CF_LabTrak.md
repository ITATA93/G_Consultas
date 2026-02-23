# lab.CF_LabTrak

**Schema:** lab
**Columnas:** 218
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLAB_RowId | bigint | PK |  | NO | - |
| CFLAB_AccountsFieldsUnlocked | varchar |  |  | SI | AccountsFieldsUnlocked |
| CFLAB_AllowControlKeys | varchar |  |  | SI | Allow Control Keys |
| CFLAB_AlternateSystemResult | varchar |  |  | SI | Alternate System Result |
| CFLAB_AsianF6CommentMode | varchar |  |  | SI | Asian F6 Comment Mode |
| CFLAB_AuditClearDays | numeric |  |  | SI | Audit Clear Days |
| CFLAB_AuditOfAddedPInfo | varchar |  |  | SI | Audit of added patient info |
| CFLAB_AutoDoctorComments | varchar |  |  | SI | Auto Doctor Comments |
| CFLAB_AutoPopulateDSGrid | varchar |  |  | SI | Auto Populate DS Grid |
| CFLAB_AutoPrintLabels | varchar |  |  | SI | Auto Print Labels |
| CFLAB_BB_AllowEXMforAutologous | varchar |  |  | SI | BB Allow EXM for Autologous pack |
| CFLAB_BB_BBOnUpdate | varchar |  |  | SI | BB BB Registry change on Update |
| CFLAB_BB_BGColours | varchar |  |  | SI | BG colours |
| CFLAB_BB_BloodGroupHidden | varchar |  |  | SI | BB BloodGroup Hidden |
| CFLAB_BB_ClearStatusAutol_DR | varchar |  | FK | SI | BB Clear Status Autologous DR |
| CFLAB_BB_ClearStatusReserve_DR | varchar |  | FK | SI | BB Clear Status Reserve DR |
| CFLAB_BB_ClearTransaction_DR | varchar |  | FK | SI | BB Clear Transaction DR |
| CFLAB_BB_DeAuthorizeStatAuto_DR | varchar |  | FK | SI | BB DeAuthorize Status Autologous DR |
| CFLAB_BB_DeAuthorizeStatRes_DR | varchar |  | FK | SI | BB DeAuthorize Status Reserve DR |
| CFLAB_BB_DeAuthorizeTrans_DR | varchar |  | FK | SI | BB DeAuthorize Transaction DR |
| CFLAB_BB_DisableSecIDforBatchProd | varchar |  |  | SI | BB Disable SecondaryID for Batch Products |
| CFLAB_BB_EDNManualSelection | varchar |  |  | SI | BB Allow manual selection in EDN |
| CFLAB_BB_ErrorNoPin | varchar |  |  | SI | BB Error for no Pin |
| CFLAB_BB_OrderOfBBPinOCX | varchar |  |  | SI | BB Order Of BBP in OCX |
| CFLAB_BB_PackExpiryStatus_DR | varchar |  | FK | SI | BB Pack Expiry Status DR |
| CFLAB_BB_PackExpiryTrans_DR | varchar |  | FK | SI | BB Pack Expiry Transaction DR |
| CFLAB_BB_PackReceiveFields | varchar |  |  | SI | BB Pack Receive fields retention |
| CFLAB_BB_PackReceiveLoadAntigen | varchar |  |  | SI | Pack Receive Load Antigen |
| CFLAB_BB_ReadOnlyPIinPT | varchar |  |  | SI | BB Read Only Pack Inquiry in Pack Transactions |
| CFLAB_BB_RevToStockStatAutol_D | varchar |  |  | SI | BB Pack Expiry Status Autologous DR |
| CFLAB_BB_RevToStockStatRes_DR | varchar |  | FK | SI | BB Revert To Stock Status Reserve DR |
| CFLAB_BB_RevToStockTrans_DR | varchar |  | FK | SI | BB Revert To Stock Transaction DR |
| CFLAB_BB_SVABRegister | double |  |  | SI | BB Specimen Valid ABRegister |
| CFLAB_BB_SVCommon | double |  |  | SI | BB Specimen Valid Common |
| CFLAB_BB_SVFrozen | double |  |  | SI | BB Specimen Valid Forzen |
| CFLAB_BB_SVPregnant | double |  |  | SI | BB Specimen Valid Pregnant |
| CFLAB_BB_SVTran1 | double |  |  | SI | BB Specimen Valid Transfusion 1 |
| CFLAB_BB_SVTran1Time | double |  |  | SI | BB Specimen Valid Transfusion 1 Time |
| CFLAB_BB_SVTran2 | double |  |  | SI | BB Specimen Valid Transfusion 2 |
| CFLAB_BB_SVTran2Time | double |  |  | SI | BB Specimen Valid Transfusion 2 Time |
| CFLAB_BB_SVTran3 | double |  |  | SI | BB Specimen Valid Transfusion 3 |
| CFLAB_BB_SVTran3Time | double |  |  | SI | BB Specimen Valid Transfusion 3 Time |
| CFLAB_BB_SVTran4 | double |  |  | SI | BB Specimen Valid Transfusion 4 |
| CFLAB_BB_SVTran4Time | double |  |  | SI | BB Specimen Valid Transfusion 4 Time |
| CFLAB_BB_SVTran5 | double |  |  | SI | BB Specimen Valid Transfusion 5 |
| CFLAB_BB_SVTran5Time | double |  |  | SI | BB Specimen Valid Transfusion 5 Time |
| CFLAB_BB_StopPacksMovingToCu | varchar |  |  | SI | Stop Packs Moving To Current Test |
| CFLAB_BB_TransactionPatientinPT | varchar |  |  | SI | BB Transaction Patient in Pack Transactions |
| CFLAB_BB_UnitIDCheck | varchar |  |  | SI | Unit ID Check |
| CFLAB_BB_UpdStatAutologous_DR | varchar |  | FK | SI | BB Update Status Autologous DR |
| CFLAB_BB_UpdateStatusReserve_DR | varchar |  | FK | SI | BB Update Status Reserve DR |
| CFLAB_BB_UpdateTransaction_DR | varchar |  | FK | SI | BB Update Transaction DR |
| CFLAB_BB_Warning | varchar |  |  | SI | BB Warning for not preference 1 |
| CFLAB_BB_row1 | varchar |  |  | SI | BB row1 |
| CFLAB_BB_row2 | varchar |  |  | SI | BB row2 |
| CFLAB_BB_row3 | varchar |  |  | SI | BB row3 |
| CFLAB_BPAY | double |  |  | SI | BPAY prefix |
| CFLAB_CCR_FileCounter_1 | numeric |  |  | SI | CCR File Counter - 1 |
| CFLAB_CCR_FileCounter_2 | numeric |  |  | SI | CCR File Counter - 2 |
| CFLAB_CCR_LaboratoryID | varchar |  |  | SI | CCR Laboratory ID |
| CFLAB_CCR_PathToCCR | varchar |  |  | SI | CCR Path To CCR |
| CFLAB_CCR_RecordID_1 | numeric |  |  | SI | CCR Record ID - 1 |
| CFLAB_CCR_RecordID_2 | double |  |  | SI | CCR Record ID - 2 |
| CFLAB_CheckDRCTChanges | varchar |  |  | SI | Check DR for CT Changes |
| CFLAB_ClientSpecificPanel_BBP | varchar |  |  | SI | Client Specific Panel for BBP |
| CFLAB_ClientSpecificPanel_Pat | varchar |  |  | SI | Client Specific Panel for Patients |
| CFLAB_ConfidentialPrintingSite | varchar |  |  | SI | Confidential printing location |
| CFLAB_CreateDeepSeeIndexes | varchar |  |  | SI | BB BloodGroup Hidden |
| CFLAB_CreateMovementTS | varchar |  |  | SI | Create movement by Test Set |
| CFLAB_CrystalDataSource | varchar |  |  | SI | Crystal Data Source |
| CFLAB_CrystalPassword | varchar |  |  | SI | Crystal Password |
| CFLAB_CrystalType | varchar |  |  | SI | Crystal type |
| CFLAB_CrystalUserId | varchar |  |  | SI | Crystal User Id |
| CFLAB_CumulativeBy | varchar |  |  | SI | Cumulative By |
| CFLAB_CumulativeColumns | double |  |  | SI | Number of Columns in Cumulative Report |
| CFLAB_CumulativeFullYear | varchar |  |  | SI | Cumulative Full Year |
| CFLAB_CumulativeInvoice | varchar |  |  | SI | Cumulative Invoice |
| CFLAB_DP_ClinicalHistory | varchar |  |  | SI | DP ClinicalHistory |
| CFLAB_DP_DepartmentHistory | varchar |  |  | SI | DP DepartmentHistory |
| CFLAB_DP_PatientHistory | varchar |  |  | SI | DP PatientHistory |
| CFLAB_DayBookLabNumber | double |  |  | SI | DayBook Lab Number |
| CFLAB_DayBookModule_New | varchar |  |  | SI | New DayBook Module |
| CFLAB_DayBookPathologist | varchar |  |  | SI | DayBook Pathologist |
| CFLAB_DayBookPathologistLink | varchar |  |  | SI | DayBook Pathologist Link |
| CFLAB_DayBookSiteNumber | double |  |  | SI | DayBook Site Number |
| CFLAB_DefCollectedDate | varchar |  |  | SI | Default Collected Date as System Date |
| CFLAB_DefCollectedTime | varchar |  |  | SI | Default Collected Time as System Time |
| CFLAB_DefDocReportTemplate_DR | varchar |  | FK | SI | Default Doctor Report Template |
| CFLAB_DefEDI | varchar |  |  | SI | Default EDI type |
| CFLAB_DefFasting_DR | varchar |  | FK | SI | Default Fasting DR |
| CFLAB_DefFaxTemplate | varchar |  |  | SI | Default Fax Template |
| CFLAB_DefInitiation_DR | varchar |  | FK | SI | Default Initiation Code DR |
| CFLAB_DefPaymentCode | varchar |  |  | SI | DesRef Common Pay code |
| CFLAB_DefPersonel_DR | varchar |  | FK | SI | Default Personel (Collected by) DR |
| CFLAB_DefPriority_DR | varchar |  | FK | SI | Default Priority DR |
| CFLAB_DefReceiptDate | varchar |  |  | SI | Default Receipt Date as System Date |
| CFLAB_DefRequestDate | varchar |  |  | SI | Default Request Date as System Date |
| CFLAB_DefTS_LeftMargin | numeric |  |  | SI | Default T/S Left Margin |
| CFLAB_DefWidthDoctorReport | numeric |  |  | SI | Default Width for Doctor Report |
| CFLAB_DefWordPrintingTemplate | varchar |  |  | SI | Default Word Printing template |
| CFLAB_DefaultFlagsForIP | varchar |  |  | SI | Default flags for Instant reprint |
| CFLAB_DeleteFromHospitalDB | varchar |  |  | SI | Delete From Hospital DB |
| CFLAB_DestroyWordObject | varchar |  |  | SI | Destroy Word Object |
| CFLAB_Dictionary | varchar |  |  | SI | Dictionary |
| CFLAB_DisablePEActions | varchar |  |  | SI | Disable PE Actions for Hospital Patients |
| CFLAB_DisablePackSelection | varchar |  |  | SI | Disable selection of packs from enquiry |
| CFLAB_DisableViewImages | varchar |  |  | SI | Disable View Images |
| CFLAB_DisplayAge | varchar |  |  | SI | Display Age |
| CFLAB_DisplayEpisodeMRNinPE | varchar |  |  | SI | Display Episode and MRN in PE |
| CFLAB_DisplayPatientWindows | varchar |  |  | SI | Display Patient Windows |
| CFLAB_DisplayRebilledPatients | varchar |  |  | SI | Display Rebilled Patients |
| CFLAB_DisplayStaffNotes | varchar |  |  | SI | Display Staff Notes |
| CFLAB_DoctorCourierRun | varchar |  |  | SI | CopyTo Doctor Courier Run selection |
| CFLAB_DoctorReportPrintOrder | varchar |  |  | SI | Doctor's Report Print Order |
| CFLAB_DoctorTimeOut | numeric |  |  | SI | Doctor Time Out days |
| CFLAB_DoctorsReportListing | varchar |  |  | SI | Doctors Report Listing |
| CFLAB_DoctorsReportsDestination | varchar |  |  | SI | Doctors Reports Destination |
| CFLAB_DownsCorrAffected | double |  |  | SI | Downs Corr Affected |
| CFLAB_DownsCorrUnAffected | double |  |  | SI | Downs Corr UnAffected |
| CFLAB_DownsWeeksFrom | double |  |  | SI | Downs Weeks From |
| CFLAB_DownsWeeksTo | double |  |  | SI | Downs Weeks To |
| CFLAB_EDIConfidential | varchar |  |  | SI | EDI Confidential |
| CFLAB_EIssueDisabledonManual | varchar |  |  | SI | Electronic Issue disabled on manual entry of pack |
| CFLAB_EnableMIC | varchar |  |  | SI | Enable MIC/mm |
| CFLAB_ExtraLineInF6Comments | varchar |  |  | SI | Extra Line In F6 Comments |
| CFLAB_F6_Box_Height | numeric |  |  | SI | F6 box height |
| CFLAB_FaxConfidentials | varchar |  |  | SI | Fax Confidentials |
| CFLAB_IgnoreConfidInFinals | varchar |  |  | SI | Ignore Confidential TS In Finals |
| CFLAB_ImageIndicator | varchar |  |  | SI | Use Image Indicator |
| CFLAB_InquiryResolution | varchar |  |  | SI | Result Inquiry Screen Resolution |
| CFLAB_InternalInfection | double |  |  | SI | Internal infection time slot (hours) |
| CFLAB_LREFindWarning | varchar |  |  | SI | LRE Find Warning |
| CFLAB_LRE_ExtraLog | varchar |  |  | SI | LRE Extra Log |
| CFLAB_LabelsMessage | varchar |  |  | SI | Labels Message |
| CFLAB_LiveDate | date |  |  | SI | Live Date |
| CFLAB_MVAllTestSelection | varchar |  |  | SI | MV All Test Selection |
| CFLAB_MedicalValidationOption | varchar |  |  | SI | Medical Validation Option |
| CFLAB_MedicalValidationView | varchar |  |  | SI | Medical Validation View |
| CFLAB_MinimumAge | double |  |  | SI | Minimum Age |
| CFLAB_MinsOutsideArea | numeric |  |  | SI | Default Mins outside area |
| CFLAB_MortuaryButtons | varchar |  |  | SI | Mortuary buttons sequence |
| CFLAB_NLStableID | varchar |  |  | SI | NLS table ID |
| CFLAB_NNIdentifier_TC | varchar |  |  | SI | NN Identifier TC |
| CFLAB_NNIdentifier_TS | varchar |  |  | SI | NN Identifier TS |
| CFLAB_NonConfidentialPrintingSite | varchar |  |  | SI | Non-Confidential printing location |
| CFLAB_NumericDayBookSpecimen | varchar |  |  | SI | Numeric DayBook Specimen |
| CFLAB_OrderOfEpisodes | varchar |  |  | SI | Order Of Episodes |
| CFLAB_PE_2stages | varchar |  |  | SI | CFLAB_PE_2stages |
| CFLAB_PE_QuickMode | varchar |  |  | SI | PE Quick Mode |
| CFLAB_PFforBatchEntry | varchar |  |  | SI | Patient Fields for Batch Entry |
| CFLAB_PackBarcodeFields | varchar |  |  | SI | Pack Barcode Fields |
| CFLAB_PatLinkDefaultSelectAll | varchar |  |  | SI | Patient Linking default Select All |
| CFLAB_PathAllocationColours | varchar |  |  | SI | PathAllocationColours |
| CFLAB_PatientFieldsRetrived | varchar |  |  | SI | Patient Fields Retrived |
| CFLAB_PatientWarningMode | varchar |  |  | SI | Patient Warning Mode |
| CFLAB_PercentOfScheduleFee | varchar |  |  | SI | Percent Of Schedule Fee |
| CFLAB_PostCodeWidth | double |  |  | SI | Post Code Width |
| CFLAB_PracticeSecurityType | varchar |  |  | SI | Practice Security Type |
| CFLAB_PreEntry | varchar |  |  | SI | Barcode PreEntry |
| CFLAB_PreEntryFields | varchar |  |  | SI | PreEntry Fields |
| CFLAB_PreEntry_prefix_Fasting | varchar |  |  | SI | prefix for Fasting |
| CFLAB_PreEntry_prefix_Priority | varchar |  |  | SI | prefix for Priority |
| CFLAB_PreEntry_prefix_SP | varchar |  |  | SI | prefix for Specimen |
| CFLAB_PreEntry_prefix_Sex | varchar |  |  | SI | prefix for Sex |
| CFLAB_PreEntry_prefix_TS | varchar |  |  | SI | prefix for Test Set |
| CFLAB_PreEntry_prefix_UserSite | varchar |  |  | SI | prefix for User Site |
| CFLAB_PricingDelay | numeric |  |  | SI | Pricing Delay |
| CFLAB_PricingDelayInpatient | double |  |  | SI | Pricing Delay Inpatient |
| CFLAB_PricingInpatientsOnce | varchar |  |  | SI | Pricing Inpatients once |
| CFLAB_PrintDischForDischarged | varchar |  |  | SI | Print Discharge Summary For Discharged Patien |
| CFLAB_PrinterInactiveTries | numeric |  |  | SI | Printer Inactive Tries |
| CFLAB_RangeEnd | varchar |  |  | SI | Range Display End |
| CFLAB_RangeStart | varchar |  |  | SI | Range Display Start |
| CFLAB_RefreshInResultEntry | varchar |  |  | SI | Refresh In Result Entry |
| CFLAB_ReminderDays | varchar |  |  | SI | Reminder Days |
| CFLAB_ReportableResults | varchar |  |  | SI | Reportable Results |
| CFLAB_ResultFlagHigh | varchar |  |  | SI | Result Flag High |
| CFLAB_ResultFlagLow | varchar |  |  | SI | Result Flag Low |
| CFLAB_SLAmount | double |  |  | SI | SL Amount |
| CFLAB_SLComment | varchar |  |  | SI | SL Comment |
| CFLAB_SLJournalCode_DR | varchar |  | FK | SI | SL Journal Code DR |
| CFLAB_SL_Commission_Journal_DR | varchar |  | FK | SI | SL_Commission_Journal_DR |
| CFLAB_SL_Commission_Percent | double |  |  | SI | SL_Commission_Percent |
| CFLAB_SMSEmailPassword | varchar |  |  | SI | SMS Email Password |
| CFLAB_SMSEmailRefNumber | varchar |  |  | SI | SMS Email RefNumber |
| CFLAB_SMSEmailTo | varchar |  |  | SI | SMS Email To |
| CFLAB_SMSEmailUsername | varchar |  |  | SI | SMS Email Username |
| CFLAB_SaveResultAuditPH | varchar |  |  | SI | Save Result Audit in Patient History |
| CFLAB_ScratchpadEnabled | varchar |  |  | SI | Scratchpad enabled |
| CFLAB_SecondaryIDEnabled | varchar |  |  | SI | Secondary ID Enabled |
| CFLAB_SecondaryIDInOCX | varchar |  |  | SI | Display Secondary ID in OCX |
| CFLAB_SendTestFindAdd | varchar |  |  | SI | Send Test Find Add |
| CFLAB_SingleBatchCrediting_DR | varchar |  | FK | SI | Single Batch Crediting DR |
| CFLAB_SinglePatientBilling | varchar |  |  | SI | Single Patient Billing |
| CFLAB_SinglePatientRun | varchar |  |  | SI | Single Patient Run |
| CFLAB_SiteOptions | varchar |  |  | SI | Site Options |
| CFLAB_StartPosition | varchar |  |  | SI | Start Position for Storage Container |
| CFLAB_StatusEnterd | varchar |  |  | SI | Status Enterd |
| CFLAB_SuppressDeauth | varchar |  |  | SI | Suppress Deauthorisation |
| CFLAB_SystemStatus | varchar |  |  | SI | System Status |
| CFLAB_TSBatchEntryMode | varchar |  |  | SI | TS Batch Entry Mode |
| CFLAB_TSCompletionTime | varchar |  |  | SI | TS Completion Time Logic |
| CFLAB_TSPricing | varchar |  |  | SI | TestSet Based Pricing |
| CFLAB_TSUserSiteAssignment | varchar |  |  | SI | TS Usersite Assignment |
| CFLAB_TelepathyIP | varchar |  |  | SI | Telepathy IP address |
| CFLAB_TestEntryType | varchar |  |  | SI | Test Entry Type |
| CFLAB_TimeEDI | double |  |  | SI | Time EDI |
| CFLAB_TimeFAX | double |  |  | SI | Time FAX |
| CFLAB_TimePMI | double |  |  | SI | Time PMI |
| CFLAB_ValidationActionsMandatory | varchar |  |  | SI | Validation Actions Mandatory |
| CFLAB_VisitNumberFormat | varchar |  |  | SI | Visit Number Format |
| CFLAB_WebCharSet | varchar |  |  | SI | Web CharSet |
| CFLAB_WindowsDespooler | varchar |  |  | SI | Windows Despooler |
| CFLAB_Word_FontName | varchar |  |  | SI | Word FontName |
| CFLAB_Word_FontSize | varchar |  |  | SI | Word FontSize |
| CFLAB_WorksheetDataOrder | varchar |  |  | SI | Worksheet Data Order |
| CFLAB_email_IP | varchar |  |  | SI | email IP |
| CFLAB_email_address | varchar |  |  | SI | Email address |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*