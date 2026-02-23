# SQLUser.LBCF

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCF_RowID | bigint | PK |  | NO | - |
| LBCF_AdditionalTextIndicator | varchar |  |  | SI | Additional Text Indicator
Default ... |
| LBCF_AntibioticPanelKey | varchar |  |  | SI | Antibiotics Key
Function key that toggles the ant... |
| LBCF_AssociatedDepartment | bigint |  |  | SI | Associated Department for Laboratory Transfusion M... |
| LBCF_AttentionExceptionQueue_DR | bigint |  | FK | SI | Default Attention / Exception Queue for test sets ... |
| LBCF_AuthorisedText | varchar |  |  | SI | Authorised Report Text [DEPRECATED - TC-252142 - T... |
| LBCF_AutoCollectedUser_DR | bigint |  | FK | SI | Automated Collected By User |
| LBCF_AutoSpecColFinanceCondition | varchar |  |  | SI | If finance required for Specimen Collection test s... |
| LBCF_AutoSpecColFinanceReasonInvalid_DR | bigint |  | FK | SI | Default reason for test set removal for the auto f... |
| LBCF_BloodProductBulkUpdateReport_DR | bigint |  | FK | SI | Blood Product Bulk Update Report
This is used to ... |
| LBCF_BloodProductFindListReport_DR | bigint |  | FK | SI | Blood Product Find List Report
This is used to pr... |
| LBCF_BracketedResultFlags | varchar |  |  | SI | Doctor Report Bracketed Result Flags
N = test set... |
| LBCF_ClinicalDetailTextLength | integer |  |  | SI | Allows user to define the length of clinical detai... |
| LBCF_ConfidentialPrintingSite | varchar |  |  | SI | Confidential Printing Location
 T=TestSet
 R=Reg... |
| LBCF_CorrectedIndicator | varchar |  |  | SI | Corrected Result Indicator
Used to denote results... |
| LBCF_CorrectedText | varchar |  |  | SI | Corrected Report Text [DEPRECATED - TC-252142 - Tr... |
| LBCF_CourierBatch_DR | bigint |  | FK | SI | Default Courier Batch type
The Batch definition (... |
| LBCF_CourierOrderBy | varchar |  |  | SI | Sort Courier Batches By
The name of a property in... |
| LBCF_CumulativeColWidthLabels | integer |  |  | SI | Horizontal Cumulative Label Column Width
The colu... |
| LBCF_CumulativeColWidthRanges | integer |  |  | SI | Horizontal Cumulative Ranges Column Width
The col... |
| LBCF_CumulativeColWidthResults | integer |  |  | SI | Horizontal Cumulative Results Column Width
The co... |
| LBCF_CumulativeColWidthUnits | integer |  |  | SI | Horizontal Cumulative Units Column Width
The colu... |
| LBCF_CumulativeDateFormat | varchar |  |  | SI | Cumulative Date Format
The Episode CollectionDate... |
| LBCF_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| LBCF_CumulativeEpisodesMaxAge | integer |  |  | SI | Cumulatives Maximum Age
The maximum age (in days)... |
| LBCF_CumulativeOrder | varchar |  |  | SI | Doctors Reports Cumulative Order
The Episode Sequ... |
| LBCF_CumulativeTimeFormat | varchar |  |  | SI | Cumulative Time Format
The format to use for the ... |
| LBCF_DefaultBloodGroupForBatch_DR | bigint |  | FK | SI | Default Blood Group For Batch Products |
| LBCF_DefaultCourier_DR | bigint |  | FK | SI | Default Courier
This courier will be used for doc... |
| LBCF_DefaultDoctorsreportsPage_DR | bigint |  | FK | SI | Default ReportPage
If a TestSet has no ReportPage... |
| LBCF_DefaultReferralLaboratory_DR | bigint |  | FK | SI | Default Referral Laboratory |
| LBCF_DoctorReportCatalogFile | varchar |  |  | SI | Logi Doctor Report Catalog File |
| LBCF_DoctorReportCumPreference | varchar |  |  | SI | Doctors Reports Cumulative Preference
Y = print a... |
| LBCF_DoctorReportGenerateOnAutorisation | varchar |  |  | SI | Generate Doctor Report on Authorisation. |
| LBCF_DoctorReportLanguage_DR | bigint |  | FK | SI | Doctors Reports Language |
| LBCF_DoctorReportReportFile | varchar |  |  | SI | Logi Doctor Report Main Report (Landing Page) |
| LBCF_DoctorReportUsesWebServer | varchar |  |  | SI | Doctor Reports access images via web server.<br/>... |
| LBCF_DoctorsReportHeaderPatientFlagCount | integer |  |  | SI | Number of patient flags to display in Doctors Repo... |
| LBCF_DoctorsReportInstantPrint_DR | bigint |  | FK | SI | Doctors Report Instant Print Report
This is used ... |
| LBCF_DoctorsReport_DR | bigint |  | FK | SI | Doctors Report
This is used to produce automated ... |
| LBCF_DoctorsReportsBatchRetainDays | integer |  |  | SI | Doctors Reports Batch Retain Days
How many days t... |
| LBCF_DoctorsReportsDestination | varchar |  |  | SI | Switch to decide type of ReportDestination to use ... |
| LBCF_DoctorsReportsDirectory | varchar |  |  | SI | Doctors Reports Directory
The directory where all... |
| LBCF_DoctorsReportsIncludePreliminary | varchar |  |  | SI | Doctors Reports Include Preliminary Results |
| LBCF_DoctorsReportsSingleEpisode | varchar |  |  | SI | Doctors Reports per Patient
Whether to produce Do... |
| LBCF_DoctorsReportsType | varchar |  |  | SI | Report Type
I = Interims Only
F = Finals Only
A... |
| LBCF_EnsemblePortalURL | varchar |  |  | SI | Ensemble Management Portal URL
The base URL to th... |
| LBCF_FlagAlignment | varchar |  |  | SI | Flag Alignment  |
| LBCF_IgnoreConfidInFinals | varchar |  |  | SI | Ignore Confidential TS In Finals
This flag is use... |
| LBCF_InstrumentInterfaceNamespace | varchar |  |  | SI | Ensemble Instrument Interface Namespace
Namespace... |
| LBCF_InstrumentTraceExportDir | varchar |  |  | SI | Instrument Message Trace Export Directory
Directo... |
| LBCF_LabBatchBloodProductLabelReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_LabBloodIssueLabelReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_LabEpisodeSpecimenExtLabelReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_LabEpisodeSpecimenLabelReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_LabEpisodeSpecimenPrecollectLabelPrint | varchar |  |  | SI | Specimen Collection may print labels prior to coll... |
| LBCF_LabInstalled | varchar |  |  | SI | Enable Lab Enterprise
This property specifies if ... |
| LBCF_LabResultFlagHigh | varchar |  |  | SI | High Range
The character(s) to use on a Lab Resul... |
| LBCF_LabResultFlagLow | varchar |  |  | SI | Low Range
The character(s) to use on a Lab Result... |
| LBCF_LabResultFlagSpace | varchar |  |  | SI | Range Space
Whether to include a space between <r... |
| LBCF_LabResultRangeEndCum | varchar |  |  | SI | Range End Cumulative
The character(s) to use at t... |
| LBCF_LabResultRangeEndTSI | varchar |  |  | SI | Range End TestSetItem
The character(s) to use at ... |
| LBCF_LabResultRangeEndWG | varchar |  |  | SI | Range End WorkGroup
The character(s) to use at th... |
| LBCF_LabResultRangeStartCum | varchar |  |  | SI | Range Start Cumulative
The character(s) to use at... |
| LBCF_LabResultRangeStartTSI | varchar |  |  | SI | Range Start TestSetItem
The character(s) to use a... |
| LBCF_LabResultRangeStartWG | varchar |  |  | SI | Range Start WorkGroup
The character(s) to use at ... |
| LBCF_LabTransferLabelReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_LabTransferListReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_LimitAntibioticPanelSelection | varchar |  |  | SI | Limit Antibiotic Panel Selection  |
| LBCF_MICReportingFormat | varchar |  |  | SI | MIC Reporting Format
When the field is blank, usi... |
| LBCF_MaxEpisodesPerDRBatch | integer |  |  | SI | Max Number of Lab Episodes in a Doctor Report Batc... |
| LBCF_NoTimeNominator | varchar |  |  | SI | Missing Time Indicator [DEPRECATED - TC-252142 - T... |
| LBCF_NumberOfEpisodeLabels | integer |  |  | SI | Number of Lab Episode Labels |
| LBCF_POCTUser_DR | bigint |  | FK | SI | Default Point of Care Testing User
TrakCare User ... |
| LBCF_PathToDoctorReport | varchar |  |  | SI | Network Path to Doctor Report Directory from Logi ... |
| LBCF_PathogenColHeaderAntibiotics | varchar |  |  | SI | Pathogen Table Antibiotic Column Header [DEPRECATE... |
| LBCF_PathogenColWidth | integer |  |  | SI | Pathogen Table Pathogen Column Width (Pathogen Cod... |
| LBCF_PathogenColWidthAntibiotics | integer |  |  | SI | Pathogen Table Antibiotic Column Width
The width ... |
| LBCF_PositivePatientID | varchar |  |  | SI | Positive Patient ID (URN) required for Specimen Co... |
| LBCF_PreliminaryIndicator | varchar |  |  | SI | Preliminary Result Indicator
Used to denote resul... |
| LBCF_PreliminaryText | varchar |  |  | SI | Preliminary Report Text
The text to appear on a T... |
| LBCF_QualityControlSummaryReport_DR | bigint |  | FK | SI | Quality Control Summary Report |
| LBCF_QuickDoctorsReport_DR | bigint |  | FK | SI | Quick Doctors Report
This is used to produce quic... |
| LBCF_QuickPrintBatch_DR | bigint |  | FK | SI | Default QuickPrint Batch type
The Batch definitio... |
| LBCF_ReasonNotPerformedForDiscontinuedOrder_DR | bigint |  | FK | SI | Reason Not Performed For Discontinued Order
When ... |
| LBCF_ReasonNotPerformedForInvalidSpecimen_DR | bigint |  | FK | SI | Reason Not Performed For Invalid Specimens
When a... |
| LBCF_ReportAttachmentMaxCol | numeric |  |  | SI | Number of Column for Test Set Attachments on Docto... |
| LBCF_ReportFont | varchar |  |  | SI | Doctors Reports Font
Specifies the font family to... |
| LBCF_ReportFormatBloodProductUnitNumbers | varchar |  |  | SI | Report Format for Blood Product Unit Numbers
Spec... |
| LBCF_ReportFormatNationalIDNumbers | varchar |  |  | SI | Report Format for National ID (e.g. NHS number)
S... |
| LBCF_ReportOrganismBoldFont | varchar |  |  | SI | Use Bold Font on Growth Code and Organism Line |
| LBCF_ReportOrganismLabelFormat | varchar |  |  | SI | Alternate format of Organism Name in Sensitivity T... |
| LBCF_ReportOrganismNoItalics | varchar |  |  | SI | Supress italics on Growth Code and Organism Line |
| LBCF_ReportShowMedicalStaffAsgn | varchar |  |  | SI | Display Medical Staff Assignment in Doctor Report ... |
| LBCF_RequiredAcknowledgeBarcodeData | varchar |  |  | SI | Fields required to be barcoded to acknowledge a un... |
| LBCF_RequiredBarcodeData | varchar |  |  | SI | Fields required to be barcoded to mark the blood p... |
| LBCF_ResultEntryDisplayComments | varchar |  |  | SI | Display Comments by default in the Result entry co... |
| LBCF_ResultEntryDisplayRange | varchar |  |  | SI | Display Ranges by default in the Result entry comp... |
| LBCF_ResultEntryDisplayUnits | varchar |  |  | SI | Display Units by default in the Result entry compo... |
| LBCF_ResultTitreReciprocalCompare | varchar |  |  | SI | Compare Titre Results using reciprocal values
Def... |
| LBCF_ShipmentContainerReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCF_SinglePatientBatch_DR | bigint |  | FK | SI | Default Single-Patient Batch type
The Batch defin... |
| LBCF_SpecColFinanceCondition | varchar |  |  | SI | Finance required for Specimen Collection.  Require... |
| LBCF_SpecRecOrderQuestionEnable | varchar |  |  | SI | Order Question editable in Specimen Receive if con... |
| LBCF_SuppressClinicalDetails | varchar |  |  | SI | Suppress Clinical Details in doctor reports |
| LBCF_SupressMICLegend | varchar |  |  | SI | Supress MIC Legend |
| LBCF_TestItemDetailsKey | varchar |  |  | SI | Test Item Details Key
Function key that toggles t... |
| LBCF_TestNotPerformedText | varchar |  |  | SI | TestNotPerformed Report Text [DEPRECATED - TC-2521... |
| LBCF_ToFollow | varchar |  |  | SI | To-follow Text [DEPRECATED - TC-252142 - Translati... |
| LBCF_VerifyUnitNumber | varchar |  |  | SI | Verify the blood product unit number
This setting... |
| LBCF_VeterinarySubjectCounter_DR | bigint |  | FK | SI | Veterinary Subject Counter
If set the subject IDs... |
| LBCF_WorkStatusSummaryReport_DR | bigint |  | FK | SI | The report available to the Work Status Summary sc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*