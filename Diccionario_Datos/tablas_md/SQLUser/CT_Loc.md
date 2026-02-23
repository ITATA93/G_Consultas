# SQLUser.CT_Loc

**Schema:** SQLUser
**Columnas:** 321
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Catalogo de **Ubicaciones/Servicios** del hospital.

Define la estructura organizacional:
- Servicios clinicos (UCI, Urgencia, Pediatria)
- Areas administrativas
- Pabellones quirurgicos
- Unidades de apoyo (Laboratorio, Imagenes)

**Campos clave:**
- CTLOC_Code: Codigo unico del servicio
- CTLOC_Desc: Descripcion
- CTLOC_Hospital_DR: Hospital al que pertenece
- CTLOC_Type: Tipo de ubicacion

**Uso:**
- Asignacion de camas
- Destino de ordenes
- Estadisticas por servicio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLOC_RowID | bigint | PK |  | NO | - |
| CTLOC_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTLOC_Address | varchar |  |  | SI | Address |
| CTLOC_AdmQuest_DR | bigint |  | FK | SI | Des Ref Admission Questionnaire |
| CTLOC_AgeFrom | double |  |  | SI | Age From |
| CTLOC_AgeTo | double |  |  | SI | Age To |
| CTLOC_AllowLabBulkReceive | varchar |  |  | SI | Allow bulk receive of lab shipment container |
| CTLOC_AutoSendawaytoLabEpLabSite | varchar |  |  | SI | Schedule Automatic Sendaway to Lab Episode Lab Sit... |
| CTLOC_BedReasonNotAvail_DR | bigint |  | FK | SI | Des Ref PACBedReasonNotAvail |
| CTLOC_BroadPatientGroup_DR | bigint |  | FK | SI | Des Ref Broad Patient Group |
| CTLOC_Cashier_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| CTLOC_ChargeAccomPatientOnLeave | varchar |  |  | SI | Charge for Accom when Patient is on Leave |
| CTLOC_ChildHealthOrganisation_DR | bigint |  | FK | SI | Des Ref Child Health Organisation |
| CTLOC_City_DR | bigint |  | FK | SI | Des Ref to CTCITY |
| CTLOC_Code | varchar |  |  | NO | Location Code |
| CTLOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTLOC_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTLOC_CollectionCentreLicenseNumber | varchar |  |  | SI | Collection Centre License Number |
| CTLOC_CommunityUnit | varchar |  |  | SI | CommunityUnit |
| CTLOC_ConfidentialFax | varchar |  |  | SI | Confidential Fax Number |
| CTLOC_ContactName | varchar |  |  | SI | Contact Name |
| CTLOC_CounterType_DR | bigint |  | FK | SI | User Defined Counter Type |
| CTLOC_CreatedDate | date |  |  | SI | Created Date |
| CTLOC_CreatedTime | time |  |  | SI | Created Time |
| CTLOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTLOC_CumulativeEpisodes | integer |  |  | SI | Deprecated
Cumulatives Maximum Number of Episodes... |
| CTLOC_CumulativeOrder | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Order
The ... |
| CTLOC_CumulativePreference | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Preference... |
| CTLOC_DateActiveFrom | date |  |  | NO | Date Active From |
| CTLOC_DateActiveTo | date |  |  | SI | Date Active To |
| CTLOC_DaysAutoGenerate | double |  |  | SI | Days to AutoGenerate schedule overnight |
| CTLOC_DaysClinSummaryED | double |  |  | SI | days prior to estimated date of discharge that the... |
| CTLOC_DaysClinSummaryIP | double |  |  | SI | days prior to estimated date of discharge that the... |
| CTLOC_DaysClinSummaryOP | double |  |  | SI | days prior to estimated date of discharge that the... |
| CTLOC_DaysForOPDOffer | double |  |  | SI | DaysForOPDOffer |
| CTLOC_DaysForOPLetterResponse | double |  |  | SI | DaysForOPLetterResponse |
| CTLOC_DaysOfferOutcomeChange | double |  |  | SI | DaysOfferOutcomeChange |
| CTLOC_DaysToKeepRecord | double |  |  | SI | DaysToKeepRecord |
| CTLOC_DefAdmTimLoc | time |  |  | SI | Default adm time for loc |
| CTLOC_DefDischTimeLoc | time |  |  | SI | Default Discharge Time for Location |
| CTLOC_DefReqByType | varchar |  |  | SI | Default Requested By Type |
| CTLOC_DefaultCollectionCentre_DR | bigint |  | FK | SI | Default Collection Centre |
| CTLOC_DefaultMRType_DR | bigint |  | FK | SI | Des Ref DefaultMRType |
| CTLOC_DefaultRapidRequestForm_DR | bigint |  | FK | SI | Default Rapid Request Form |
| CTLOC_Dep_DR | bigint |  | FK | SI | Des Ref to Dep_DR |
| CTLOC_DepartmentHeadUserDR | bigint |  | FK | SI | Department Head UserDR |
| CTLOC_Desc | varchar |  |  | NO | Location Description |
| CTLOC_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTLOC_DifferentSexPatients | varchar |  |  | SI | Different Sex Patients in Room |
| CTLOC_DisQuest_DR | bigint |  | FK | SI | Des Ref Discharge Questionnaire |
| CTLOC_DischSumEDRequired | varchar |  |  | SI | Disch Sum EDRequired |
| CTLOC_DischSumIPRequired | varchar |  |  | SI | Disch Sum IPRequired |
| CTLOC_DischSumNotRequired | varchar |  |  | SI | Disch Sum NotRequired |
| CTLOC_DischSumOPRequired | varchar |  |  | SI | Disch Sum OPRequired |
| CTLOC_DischargeLounge | varchar |  |  | SI | Discharge Lounge |
| CTLOC_DispLoc_DR | bigint |  | FK | SI | Primary Dispensing Location DR |
| CTLOC_DoNotDisplayRoomDescForBed | varchar |  |  | SI | DoNotDisplayRoomDescForBed |
| CTLOC_DoNotSetBedUnavail | varchar |  |  | SI | Do not set bed unavailable  |
| CTLOC_DocCourierCopies | numeric |  |  | SI | Deprecated
For PatientLocation: Not used
For Lab... |
| CTLOC_DocCourier_DR | bigint |  | FK | SI | Deprecated
For PatientLocation: Not used
For Lab... |
| CTLOC_DoctorsReportsDeliverySort | varchar |  |  | SI | Deprecated
Doctors Reports Delivery Sort
The sor... |
| CTLOC_DoctorsReportsType | varchar |  |  | SI | Deprecated
For PatientLocation: The report type t... |
| CTLOC_DrgType | varchar |  |  | SI | Location DRG Type |
| CTLOC_EBookerEnabled | varchar |  |  | SI | EBooker Enabled |
| CTLOC_EBookerID | varchar |  |  | SI | EBooker ID |
| CTLOC_EBookerIURPEnabled | varchar |  |  | SI | EBooker IURP Generation Enabled |
| CTLOC_EBookerSuspDate | date |  |  | SI | EBooker Suspended Date From |
| CTLOC_EBookerSuspReas | varchar |  |  | SI | EBooker Suspended Reason |
| CTLOC_EBookingEnabled | varchar |  |  | SI | EBooking Enabled |
| CTLOC_EBookingID | varchar |  |  | SI | EBooking ID |
| CTLOC_EDDischSummaryType | varchar |  |  | SI | EDDischSummaryType |
| CTLOC_EDStreamingMethod | varchar |  |  | SI | Custom Class Method for ED Streaming - Overrides c... |
| CTLOC_Email | varchar |  |  | SI | Email |
| CTLOC_EnableDischargeAllHyperlink | varchar |  |  | SI | Enable Discharge All Hyperlink |
| CTLOC_EnableEDStreaming | varchar |  |  | SI | Enable ED Streaming - Emergency Department locatio... |
| CTLOC_EnabledPharmRev | varchar |  |  | SI | Enabled Pharmacy Review |
| CTLOC_EndTime | time |  |  | SI | Operation End Time (close) |
| CTLOC_EnvSubjectApplicable | varchar |  |  | SI | Flag for Environmental Subject Type applicable |
| CTLOC_ExclHospAverPriceQty | varchar |  |  | SI | Exclude from Hospital Average Price and Stock Qty ... |
| CTLOC_ExecuteConfirmation | varchar |  |  | SI | Order Execute Confirmation |
| CTLOC_ExtAvailable_DR | bigint |  | FK | SI | Location Externally Available |
| CTLOC_ExtGroup_DR | bigint |  | FK | SI | Des Ref ExtGroup |
| CTLOC_ExternalInfoSystem | varchar |  |  | SI | External Information System |
| CTLOC_ExternalInterfaceQueue_DR | bigint |  | FK | SI | Deprecated
External Interface Queue |
| CTLOC_ExternalViewerLink | varchar |  |  | SI | External Viewer Link |
| CTLOC_Fax | varchar |  |  | SI | Fax |
| CTLOC_Floor | varchar |  |  | SI | Floor |
| CTLOC_FloorplanQuery | varchar |  |  | SI | Floorplans Query |
| CTLOC_FlowsheetName | varchar |  |  | SI | FlowsheetName  |
| CTLOC_GLCCC_DR | bigint |  | FK | SI | Des Ref to GLCCC (Cost Center) |
| CTLOC_HL7OrdersLink | varchar |  |  | SI | HL7 Orders Link |
| CTLOC_HealthCentre | varchar |  |  | SI | Usual Health Centre |
| CTLOC_HighDependencyUnit | varchar |  |  | SI | High Dependency Unit Flag |
| CTLOC_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CTLOC_IPDischSummaryType | varchar |  |  | SI | IPDischSummaryType |
| CTLOC_InPatientUnit | varchar |  |  | SI | InPatient Unit |
| CTLOC_InclDisOrders | varchar |  |  | SI | Include Discontinued Orders |
| CTLOC_Index | varchar |  |  | SI | Build Index by Order Date |
| CTLOC_IntQuest_DR | bigint |  | FK | SI | Des Ref Intermediate Questionnaire |
| CTLOC_IntendClinCareIntensity_DR | bigint |  | FK | SI | Des Ref Intend Clinical Care Intensity |
| CTLOC_JBGroup_DR | bigint |  | FK | SI | Des Ref to PACJourneyBoardGroup |
| CTLOC_LabAutoReceive | varchar |  |  | SI | Lab Auto-receive external orders |
| CTLOC_LabDefaultReceiveDateTime | varchar |  |  | SI | Lab Default Receive Date Time |
| CTLOC_LabReportPage_DR | bigint |  | FK | SI | Des Ref to LBCReportPage
Note: [ DEPRECATED - NO ... |
| CTLOC_Language_DR | bigint |  | FK | SI | Deprecated
Doctors Reports Language
The language... |
| CTLOC_Laundry | varchar |  |  | SI | CSR Flag |
| CTLOC_LocCourierCopies | numeric |  |  | SI | Deprecated
The default #copies to use with CTLOCL... |
| CTLOC_LocCourier_DR | bigint |  | FK | SI | Deprecated
For PatientLocation: The default Couri... |
| CTLOC_MRRequestMoveValid | varchar |  |  | SI | MR Request Move Valid |
| CTLOC_MandatoryBeforeAdmin | varchar |  |  | SI | Mandatory before Administration  |
| CTLOC_MandatoryBeforePack | varchar |  |  | SI | Mandatory before Pack |
| CTLOC_ManualPrint | varchar |  |  | SI | Deprecated
Manual Print
Flag to show if Doctors ... |
| CTLOC_MaxDaysOnLeave | double |  |  | SI | Max Days On Leave Without Discharge |
| CTLOC_MedicalRecordActive | varchar |  |  | SI | Medical Record Active at this Location |
| CTLOC_MentalHealthUnit | varchar |  |  | SI | Mental Health Unit |
| CTLOC_MultDateRangesVisitHrs | varchar |  |  | SI | Multiple Date Ranges of Visit Hrs |
| CTLOC_NATAHeadings | varchar |  |  | SI | NATA Headings |
| CTLOC_NFMI_DR | varchar |  | FK | SI | Des Ref to CT_NFMI |
| CTLOC_NatCodeDateFrom | date |  |  | SI | NatCode DateFrom |
| CTLOC_NatCodeDateTo | date |  |  | SI | NatCodeDateTo |
| CTLOC_NationCode | varchar |  |  | SI | National Code |
| CTLOC_NotUsed | varchar |  |  | SI | Not Used |
| CTLOC_OPDischSummaryType | varchar |  |  | SI | OPDischSummaryType |
| CTLOC_OTC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| CTLOC_OffersBeforeIP_OPWaitReset | double |  |  | SI | OffersBeforeIP OPWaitReset |
| CTLOC_OpenOvernightIndicator | varchar |  |  | SI | Open Overnight Indicator |
| CTLOC_OrdersToRecLoc | varchar |  |  | SI | Send OrdersToRecLoc |
| CTLOC_OutPatientUnit | varchar |  |  | SI | OutPatient Unit |
| CTLOC_OwnQueFlag | varchar |  |  | SI | Create Queue Flag (By Own Dept) |
| CTLOC_Owner | varchar |  |  | SI | Owner |
| CTLOC_PBSPharmacyApprovalNumber | varchar |  |  | SI | The PBS-assigned unique identifier for this dispen... |
| CTLOC_POEnabled | varchar |  |  | SI | PO Enabled |
| CTLOC_PagerNo | varchar |  |  | SI | Pager Number |
| CTLOC_Password | varchar |  |  | SI | Location Password |
| CTLOC_PatDiarySpecColour | varchar |  |  | SI | Specialty Colour |
| CTLOC_PatientAgeSexMix_DR | bigint |  | FK | SI | Des Ref Patient Age Sex Mix |
| CTLOC_PatientType_DR | bigint |  | FK | SI | PatientType |
| CTLOC_Period | varchar |  |  | SI | Period |
| CTLOC_PharmRevSTATNotReq | varchar |  |  | SI | Pharmacy Review Not Required for STAT Orders |
| CTLOC_PrefConMethod | varchar |  |  | SI | Preferred Contact Method |
| CTLOC_PreferedOutlierWard | bigint |  |  | SI | Prefered Outlier Ward |
| CTLOC_PrintLabelsUrgMRRequest | varchar |  |  | SI | Print Labels for Urgent MR Request |
| CTLOC_Province_DR | bigint |  | FK | SI | Province |
| CTLOC_QuickPrint | varchar |  |  | SI | Deprecated
For Recipient Location: the default Qu... |
| CTLOC_RadOrdAccessNoPrefix | varchar |  |  | SI | RadOrdAccessNoPrefix |
| CTLOC_RecQueFlag | varchar |  |  | SI | Create Queue Flag (By Other Dept) |
| CTLOC_ReferringDoctorCourierCopies | numeric |  |  | SI | Deprecated
For PatientLocation: Not used
For Lab... |
| CTLOC_ReferringDoctorCourier_DR | bigint |  | FK | SI | Deprecated
For PatientLocation: Not used
For Lab... |
| CTLOC_Region_DR | bigint |  | FK | SI | Region |
| CTLOC_RehabilitativeFlag | varchar |  |  | SI | Rehabilitative Flag |
| CTLOC_ReportMode | varchar |  |  | SI | Deprecated
Report Mode |
| CTLOC_ResetPharmStatus | varchar |  |  | SI | Return to Review On Hold or Resume |
| CTLOC_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| CTLOC_RestPeriodFrom | time |  |  | SI | Rest Period From |
| CTLOC_RestPeriodTo | time |  |  | SI | Rest Period To |
| CTLOC_ResultDelivery | varchar |  |  | SI | Result Delivery |
| CTLOC_SNAPFlag | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare 2011+ (Log:8010... |
| CTLOC_SendHL7MessageOn | varchar |  |  | SI | Send HL7 Message On |
| CTLOC_ShortLabSiteCode | varchar |  |  | SI | Short Lab Site Code  |
| CTLOC_SignFacilDateFrom | date |  |  | SI | Signif Facil Date From |
| CTLOC_SignifFacilDateTo | date |  |  | SI | Signif Facil DateTo |
| CTLOC_SignifFacility_DR | bigint |  | FK | SI | Des Ref Signif Facility |
| CTLOC_StartTime | time |  |  | SI | Opening Time (Open) |
| CTLOC_StartTimeFB24 | time |  |  | SI | Start Time of 24 Hr Fluid Balance |
| CTLOC_StockEnabled | varchar |  |  | SI | Stock Enabled |
| CTLOC_StorageBinStatus | varchar |  |  | SI | Storage Bin Status  |
| CTLOC_TelehealthAppointment | varchar |  |  | SI | Flag for Telehealth Appointments. Flag will not dr... |
| CTLOC_Telephone | varchar |  |  | SI | Telephone |
| CTLOC_TelephoneExt | varchar |  |  | SI | Telephone Extension |
| CTLOC_ThirdPartyCourierCopies | numeric |  |  | SI | Deprecated
For PatientLocation: Not used
For Lab... |
| CTLOC_ThirdPartyCourier_DR | bigint |  | FK | SI | Deprecated
For PatientLocation: Not used
For Lab... |
| CTLOC_TimeSinceLastAppt | double |  |  | SI | TimeSinceLastAppt |
| CTLOC_TimeZone | varchar |  |  | SI | Time Zone 
If left blank the location will use th... |
| CTLOC_Type | varchar |  |  | SI | Location Type |
| CTLOC_UpdPharmStatus | varchar |  |  | SI | Update Pharmacy Status |
| CTLOC_UpdatedDate | date |  |  | SI | Updated Date |
| CTLOC_UpdatedTime | time |  |  | SI | Updated Time |
| CTLOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTLOC_VetSubjectApplicable | varchar |  |  | SI | Flag for Veterinary Subject Type applicable |
| CTLOC_VisitHrFrom | time |  |  | SI | Visiting Hours From |
| CTLOC_VisitHrTo | time |  |  | SI | Visiting Hours To |
| CTLOC_WardFlag | varchar |  |  | SI | Ward Flag |
| CTLOC_WardSingleSex | bigint |  |  | SI | Ward Single Sex |
| CTLOC_WeeklyAvailIndicator | varchar |  |  | SI | Weekly Availability Indicator |
| CTLOC_WeeksSuspensionReview | double |  |  | SI | WeeksSuspensionReview |
| CTLOC_Zip_DR | bigint |  | FK | SI | Des Ref CTZip |
| CTLoc_BPDisposalAllow | varchar |  |  | SI | Blood Product Disposal Allowed |
| Q01 | - |  |  | SI | Have you received any early pregnancy advice |
| Q02 | - |  |  | SI | Have you had a previous booking for this pregnancy |
| Q02A | - |  |  | SI | Location of previous booking |
| Q02B | - |  |  | SI | Reason for new booking |
| Q02T | - |  |  | SI | Details |
| Q03 | - |  |  | SI | Are you intending to move out of the area in the n... |
| Q04 | - |  |  | SI | Seen within 2 weeks of first contact (Gestation at... |
| Q04A | - |  |  | SI | Details |
| Q05 | - |  |  | SI | Have you been admitted to hospital recently |
| Q05A | - |  |  | SI | Details |
| Q06 | - |  |  | SI | Place of birth |
| Q07 | - |  |  | SI | Are your family origins Mediterranean, Africa, Car... |
| Q08 | - |  |  | SI | Mothers family origins are South Asia, Caribbean o... |
| Q09 | - |  |  | SI | Preferred method of contact |
| Q12 | - |  |  | SI | Is English your first language |
| Q13 | - |  |  | SI | Do you have any language or literacy issues |
| Q13A | - |  |  | SI | Literacy issues |
| Q13B | - |  |  | SI | Language spoken |
| Q14 | - |  |  | SI | Interpreter required |
| Q15 | - |  |  | SI | Preferred methods of communication |
| Q16 | - |  |  | SI | Learning disabilities details |
| Q17 | - |  |  | SI | What is your sexuality |
| Q18 | - |  |  | SI | Height |
| Q18ObsDR | - |  |  | SI | Height DR |
| Q19 | - |  |  | SI | Weight (kg) |
| Q19ObsDR | - |  |  | SI | Weight (kg) DR |
| Q20 | - |  |  | SI | BMI |
| Q21 | - |  |  | SI | Systolic BP |
| Q21ObsDR | - |  |  | SI | Systolic BP DR |
| Q22 | - |  |  | SI | Diastolic BP |
| Q22ObsDR | - |  |  | SI | Diastolic BP DR |
| Q23 | - |  |  | SI | Was your pregnancy planned |
| Q24 | - |  |  | SI | Is VBAC intended for this pregnancy |
| Q25 | - |  |  | SI | Is the uterus palpable |
| Q26 | - |  |  | SI | Have you had any vaginal bleeding |
| Q26A | - |  |  | SI | Type of vaginal bleeding |
| Q27 | - |  |  | SI | Do you have pain on passing urine |
| Q27T | - |  |  | SI | Details |
| Q28 | - |  |  | SI | Have you had recent contact with anyone with Chick... |
| Q28T | - |  |  | SI | Details |
| Q29 | - |  |  | SI | Do you take regular journeys by car, plane or trai... |
| Q30 | - |  |  | SI | Have you received advice about your weight |
| Q31 | - |  |  | SI | Do you have any tattoos or piercings |
| Q31T | - |  |  | SI | Details |
| Q32 | - |  |  | SI | Medications taken during this pregnancy |
| Q32A | - |  |  | SI | Medications |
| Q32T | - |  |  | SI | Details |
| Q33 | - |  |  | SI | Do you have support in pregnancy and childcare |
| Q33A | - |  |  | SI | Type of support |
| Q33T | - |  |  | SI | Details |
| Q34 | - |  |  | SI | Are there any accommodation issues |
| Q34A | - |  |  | SI | Accommodation issues |
| Q34T | - |  |  | SI | Details |
| Q35 | - |  |  | SI | Occupation |
| Q36 | - |  |  | SI | Employment status |
| Q36T | - |  |  | SI | Details |
| Q37 | - |  |  | SI | Does anyone you live with have personal issues |
| Q37A | - |  |  | SI | Personal issues |
| Q37T | - |  |  | SI | Details |
| Q38 | - |  |  | SI | Are there any broader family issues |
| Q38A | - |  |  | SI | Broader issues |
| Q38T | - |  |  | SI | Details |
| Q39 | - |  |  | SI | Any agencies involved |
| Q39A | - |  |  | SI | Agencies |
| Q39T | - |  |  | SI | Details |
| Q40 | - |  |  | SI | How are things at home |
| Q41 | - |  |  | SI | Is there anybody at home who is not happy about th... |
| Q41T | - |  |  | SI | Details |
| Q42 | - |  |  | SI | Will this baby be in the CONI programme |
| Q43 | - |  |  | SI | In the past month have you been bothered by |
| Q43A | - |  |  | SI | Feeling down, depressed or hopeless |
| Q43AObsDR | - |  |  | SI | Feeling down, depressed or hopeless DR |
| Q43B | - |  |  | SI | Having little interest or pleasure in doing things |
| Q43BObsDR | - |  |  | SI | Having little interest or pleasure in doing things... |
| Q43C | - |  |  | SI | Do you want help with any mental health issues |
| Q43CObsDR | - |  |  | SI | Do you want help with any mental health issues DR |
| Q43T | - |  |  | SI | Details |
| Q44 | - |  |  | SI | Have you made/will you be making any referrals |
| Q44A | - |  |  | SI | Referrals |
| Q44T | - |  |  | SI | Details |
| Q74 | - |  |  | SI | Do you have any learning disabilities |
| Q75 | - |  |  | SI | Number of years in education |
| Q76 | - |  |  | SI | Referral Required |
| Q76ObsDR | - |  |  | SI | Referral Required DR |
| Q77 | - |  |  | SI | Worrying or feeling anxious |
| Q77ObsDR | - |  |  | SI | Worrying or feeling anxious DR |
| Q78 | - |  |  | SI | Does your partner have any history |
| Q78ObsDR | - |  |  | SI | Does your partner have any history DR |
| Q79 | - |  |  | SI | Family History |
| Q79ObsDR | - |  |  | SI | Family History DR |
| Q80 | - |  |  | SI | Previous treatment/in-patient care |
| Q80ObsDR | - |  |  | SI | Previous treatment/in-patient care DR |
| Q81 | - |  |  | SI | Past or present mental illness |
| Q81ObsDR | - |  |  | SI | Past or present mental illness DR |
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