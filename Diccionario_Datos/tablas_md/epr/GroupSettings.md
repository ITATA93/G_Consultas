# epr.GroupSettings

**Schema:** epr
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AllergiesInactiveByDoctorOnly | bit |  |  | SI | THIS IS NO LONGER A "DOCTOR ONLY" FLAG.
Log 39282... |
| AllergySeverity | varchar |  |  | SI | ab 21.02.05 48554 |
| AllowBedHistory | bit |  |  | SI | - |
| AllowChangeAdminStatus | bit |  |  | SI | ab 15.08.06 60192
Allow to Change Admin Status |
| AllowEditPatientFlag | bit |  |  | SI | Allow to Edit Patient Flag |
| AllowMixedOrders | bit |  |  | SI | Allow mixed orders from Phone Order workflow |
| AllowOverbookNA | bit |  |  | SI | MD 11/12/06  - Allow overbooking when session unav... |
| AllowPrescOverride | bit |  |  | SI | Log 59215 - JD |
| AllowReverseAdminStatus | bit |  |  | SI | EH 31.08.06 69296
Allow to Reverse Admin Status |
| AllowXML | bit |  |  | SI | - |
| AppTimeout | varchar |  |  | SI | - |
| ApptStatusID | varchar |  |  | SI | - |
| AuditTables | varchar |  |  | SI | [DEPRECATED]Replaced by User.SSProfile.AuditTables... |
| CanAddDSMedications | bit |  |  | SI | - |
| CanChangeBrand | bit |  |  | SI | SB 06/04/05 (50319) |
| CanEditClosedAss | bit |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPCanEditC... |
| CanEditResQues | bit |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPCanEditR... |
| CanOverpackPrescriptions | bit |  |  | SI | JW (54994) |
| CannotUpdatePDS | bit |  |  | SI | - |
| CarPrvTp | varchar |  |  | SI | Mapped on XMLDataHandler |
| CarPrvTpHideEps | bit |  |  | SI | - |
| ClinSummDocTypeDR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile->SSPDisSumD... |
| ConsultActionsInInfoPane | varchar |  |  | SI | - |
| CumAbnormal | varchar |  |  | SI | - |
| CumAcrossAllEpisodes | varchar |  |  | SI | Cumulative View Across All Episodes |
| CumAllowedSeeGraphLink | varchar |  |  | SI | Cumulative View Allowed to See Graph Link |
| CumColumnWidth | integer |  |  | SI | Log 39287 - AI - 02-10-2003 : New field Cumulative... |
| CumCommentSuffix | varchar |  |  | SI | - |
| CumDoNotDisplayLabEpisNo | bit |  |  | SI | - |
| CumDoNotDisplayRead | bit |  |  | SI | - |
| CumDoNotDisplayUnit | bit |  |  | SI | - |
| CumIncludeRPrefix | varchar |  |  | SI | Cumulative View Include R Prefix |
| CumNoColumns | integer |  |  | SI | Cumulative View Number of Columns |
| CumRefRangePosition | varchar |  |  | SI | Cumulative View Reference Range Position |
| CumShowSpecimenCol | bit |  |  | SI | - |
| CumVariedRange | varchar |  |  | SI | - |
| DSSChartBookDR | bigint |  | FK | SI | - |
| DefaultCSDocumentOnNewAndEdit | bit |  |  | SI | Default Clinical Summary Document on New and Edit |
| DisSumDocTp | varchar |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPDisSumDo... |
| DisSumEPRChartBookDR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile.SSPDisSumEP... |
| DisableWardSumLink | bit |  |  | SI | - |
| DisplayDayEditIcon | bit |  |  | SI | SB 06/05/06 (58637) - Display Day Edit Icon on OT ... |
| DisplayOPOTBookingIcon | bit |  |  | SI | Display OT Booking Icon on OT Planner for Outpatie... |
| DisplayObservationsInCPSum | bit |  |  | SI | Display Observations in Care Plan Summary |
| DisplayOrdersInCPSum | bit |  |  | SI | Display Orders in Care Plan Summary |
| DisplayQuestInCPSum | bit |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPDisplayQ... |
| DisplayResultTypes | varchar |  |  | SI | Log 51381 - BKJ - 09-05-2005 : New field for "Resu... |
| DisplaySessEditIcon | bit |  |  | SI | SB 06/05/06 (58637) - Display Session Edit Icon on... |
| DisplayStaticHome | bit |  |  | SI | ab 7.02.08 66221 |
| DisplayStaticTools | bit |  |  | SI | - |
| DisplayTreatPlanInCPSum | bit |  |  | SI | Display Treatment Plan in Care Plan Summary |
| DisplayWordFormat | bit |  |  | SI | - |
| DontShowClosedNCPs | bit |  |  | SI | Do Not Show Closed Nursing Care Plans in NCP Summa... |
| DrugIntSeverity | varchar |  |  | SI | - |
| EDWardListRefreshTime | integer |  |  | SI | - |
| EPRCTGraphGroupDR | bigint |  | FK | SI | Log 44734 - AI - 29-09-2004 : New field for "Graph... |
| EPRClinEncounter | varchar |  |  | SI | display an episode selection frame on EPR? |
| ExecCatDetails | varchar |  |  | SI | Set Order Status to Executed for Orders of Categor... |
| ExecItemDetails | varchar |  |  | SI | Set Order Status to Executed for Order Items |
| ExecSubCatDetails | varchar |  |  | SI | Set Order Status to Executed for Orders of Subcate... |
| ExpandMenuByDefault | bit |  |  | SI | - |
| ExternalGroupID | varchar |  |  | SI | - |
| FPStyleSheet | varchar |  |  | SI | - |
| FlexiBookDiaryHeight | integer |  |  | SI | Flexi Book Diary Height |
| FlexiBookDiaryWidth | integer |  |  | SI | Flexi Book Diary Width |
| FlexiBookDiaryX | integer |  |  | SI | Flexi Book Diary X |
| FlexiBookDiaryY | integer |  |  | SI | Flexi Book Diary Y |
| GroupDR | bigint |  | FK | NO | - |
| HL7OutboundQueueDel | bit |  |  | SI | Log 58574 - ML - 21/06/2006 - HL7 Outbound Queue D... |
| IPWardListRefreshTime | integer |  |  | SI | Refresh time for IP Ward List |
| IWNewErrorsMessage | bit |  |  | SI | Log 46439 - AI - 22-10-2004 : New field for "Displ... |
| IWNewRejectionsMessage | bit |  |  | SI | Log 46439 - AI - 22-10-2004 : New field for "Displ... |
| IWRefreshTime | integer |  |  | SI | Log 45046 - AI - 17-09-2004 : New field for "Inter... |
| LabNoDisplayType | varchar |  |  | SI | - |
| LabQueues | varchar |  |  | SI | Laboratory Properties |
| LastUpdateDate | date |  |  | SI | KK 8/Jan/04 L:39835 - New fields Udate Date,Time,U... |
| LastUpdateTime | time |  |  | SI | - |
| LastUpdateUserDR | bigint |  | FK | SI | - |
| LastUpdateUserHospDR | bigint |  | FK | SI | - |
| LongPressGestureMenuDR | bigint |  | FK | SI | - |
| MainChartBookDR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPMainChar... |
| MainChartDR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPMainChar... |
| MainMenuDR | bigint |  | FK | SI | - |
| MenuSecurity | varchar |  |  | SI | Web Menu Security Access |
| MidApptFramePerc | integer |  |  | SI | Percentage size of the top Frame in the Multiple A... |
| MobileStartWorkflow | bigint |  |  | SI | Mobile Enabled UI Start Workflow |
| NoPubHolBook | bit |  |  | SI | Log 48106 - RC - 05-04-2006 : New field for "Do no... |
| NoSelectMultiRow | bit |  |  | SI | - |
| NumOPDiaryFrames | integer |  |  | SI | - |
| OEExecItemDetails | varchar |  |  | SI | Mapped on XMLDataHandler |
| OEExecPriorityDetails | varchar |  |  | SI | Mapped on XMLDataHandler |
| OEExecSubCatDetails | varchar |  |  | SI | Mapped on XMLDataHandler |
| OEItemDetails | varchar |  |  | SI | Mapped on XMLDataHandler |
| OEItemItemDetails | varchar |  |  | SI | Mapped on XMLDataHandler |
| OEItemSubCatDetails | varchar |  |  | SI | Mapped on XMLDataHandler |
| OEQuesCatDetails | varchar |  |  | SI | Log 58162 BoC 04/09/2006
New field for "Show ques... |
| OEQuesSubCatDetails | varchar |  |  | SI | Log 58162 BoC 04/09/2006
New field for "Show ques... |
| OESetItems | varchar |  |  | SI | Mapped on XMLDataHandler |
| OESetSets | varchar |  |  | SI | - |
| OESetSubCats | varchar |  |  | SI | Mapped on XMLDataHandler |
| OPDiaryViewFrames | integer |  |  | SI | Number of frames displayed in in OPD search result... |
| OTDiaryDisplay | varchar |  |  | SI | Log 53079 - RC - 07-07-2005 : Change for OT Diary ... |
| OTPlannerRefreshTime | integer |  |  | SI | Operating Theatre Planner Refresh Time |
| OTQuestProfileDR | bigint |  | FK | SI | log 87201 |
| OnlyShowUncollectedOnCollection | bit |  |  | SI | Log 39459 - AI - 09-10-2003 : New field for "Only ... |
| OrderProfileDR | bigint |  | FK | SI | - |
| PatTypeRestrictOPD | bit |  |  | SI | 65700-82299 Extend Patient Type Restrictions to OP... |
| PatientTypeRestrict | varchar |  |  | SI | 65700 |
| PharmCanDispNonForm | bit |  |  | SI | Pharmacy - can dispense non-formulary items |
| PharmQ | varchar |  |  | SI | Log 46501 - MD - 19-10-2004 : New field for "Pharm... |
| PharmRefreshTime | integer |  |  | SI | - |
| PrevEpisChartDR | bigint |  | FK | SI | [DEPRECATED]Replaced by User.SSProfile,SSPPrevEpis... |
| RBDisplaySessionType | varchar |  |  | SI | SB 29/09/04 (45587): This param allows user to swi... |
| RadSTOrdStatus | varchar |  |  | SI | RC 14/06/07 51746 Define Radiology Standard type a... |
| RefreshTime | integer |  |  | SI | - |
| RequireCheckOnPack | bit |  |  | SI | 48863 |
| RequireSecondSignature | bit |  |  | SI | Require Second Signature on Admin |
| ResultRangeSep | varchar |  |  | SI | Result Range Separator - 59655 |
| Reuse2 | bit |  |  | SI | Please reuse this property |
| Reuse3 | bit |  |  | SI | Please reuse this property |
| ShowAllRows | bit |  |  | SI | for use with RBAppointment |
| ShowOrderListFrame | bit |  |  | SI | Log 54852 - JD |
| SideMenuGroupDR | bigint |  | FK | SI | reference to websys.MenuGroup to display security ... |
| SkipAdminWorkflow | varchar |  |  | SI | Skip Admin Workflow |
| StartPageDR | bigint |  | FK | SI | - |
| StartWorklist | bigint |  |  | SI | - |
| StyleSheet | varchar |  |  | SI | - |
| TaskCategory | varchar |  |  | SI | Task Category - Mapped on XMLDataHandler |
| TimeLockSession | varchar |  |  | SI | LockSession TimeOut in minutes |
| TopApptFramePerc | integer |  |  | SI | Percentage size of the top Frame in the Multiple A... |
| TransCspMidFrame | integer |  |  | SI | The height (in pixels) of the middle frame in paad... |
| TransCspTopFrame | integer |  |  | SI | The height (in pixels) of the top frame in paadmtr... |
| UDWAdminAccess | bit |  |  | SI | [DEPRECATED]Replaced by User.SSProfile,SSPUDWAdmin... |
| UseAuthClinGrpPhoneOrders | bit |  |  | SI | 60317 |
| ViewEpisodeAlertFlag | bit |  |  | SI | EZ 07/12/06 (49183) - View Episode Alert Active (y... |
| ViewPAAdmTreeOnOTWorkflow | bit |  |  | SI | EZ 26/03/07 (62758) - View PAAdm.Tree when using q... |
| XXNotUsed | bit |  |  | SI | MD 12/12/2006 -Display message when adding/replaci... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*