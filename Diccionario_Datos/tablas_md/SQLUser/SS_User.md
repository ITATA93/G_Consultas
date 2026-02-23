# SQLUser.SS_User

**Schema:** SQLUser
**Columnas:** 164
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSUSR_RowId | bigint | PK |  | NO | - |
| SSUSR_Active | varchar |  |  | SI | Active |
| SSUSR_Admitted | varchar |  |  | SI | Admitted |
| SSUSR_AllowArchiveProblems | varchar |  |  | SI | Enable API access |
| SSUSR_AllowBookPastTTGDateOP | varchar |  |  | SI | Allow to Book Past TTG Guaranteed Date OP  |
| SSUSR_AllowBookPastTTGDateWL | varchar |  |  | SI | Allow to Book Past TTG Guaranteed Date WL  |
| SSUSR_AllowDeleteCodeTables | varchar |  |  | SI | Allowed to Delete Code Table Entries |
| SSUSR_AllowSkipLDAPLogonLocal | varchar |  |  | SI | Allow user skip LDAP and logon locally |
| SSUSR_AllowWebColumnManager | varchar |  |  | SI | AllowWebColumnManager |
| SSUSR_AllowWebLayoutManager | varchar |  |  | SI | AllowWebLayoutManager |
| SSUSR_AlwaysUseSoundex | varchar |  |  | SI | Always Use Soundex |
| SSUSR_AutoAuthorise | varchar |  |  | SI | Auto Authorise |
| SSUSR_BillSequence_DR | bigint |  | FK | SI | Des Ref BillSequence |
| SSUSR_BillingTaskSupervisor | varchar |  |  | SI | Billing Task Supervisor |
| SSUSR_BioKey | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| SSUSR_BioMode | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| SSUSR_Booked | varchar |  |  | SI | Booked |
| SSUSR_CPGroup | varchar |  |  | SI | Free text for Associated Care Provider Group |
| SSUSR_CPList | varchar |  |  | SI | List of associated care providers  |
| SSUSR_CTLAN_DR | bigint |  | FK | SI | Des Ref to CTLAN |
| SSUSR_CTPCP_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| SSUSR_CareProv_DR | varchar |  | FK | SI | Des Ref to Care Provider |
| SSUSR_CashierShift | varchar |  |  | SI | CashierShift |
| SSUSR_CashierSupervisor | varchar |  |  | SI | Cashier Supervisor |
| SSUSR_ChangeLocWithinLogHosp | varchar |  |  | SI | Only Change Loc Within Logon Hospital |
| SSUSR_ChangeLocation | varchar |  |  | SI | User allowed to change location flag |
| SSUSR_Coder | varchar |  |  | SI | Identify User as a Coder |
| SSUSR_Comments | varchar |  |  | SI | Comments |
| SSUSR_CreatedBy_DR | bigint |  | FK | SI | Des Ref User |
| SSUSR_CreatedDate | date |  |  | SI | CreatedDate |
| SSUSR_CreatedTime | time |  |  | SI | CreatedTime |
| SSUSR_DRGTariffVisible | varchar |  |  | SI | DRG Tariff Visible |
| SSUSR_DateFrom | date |  |  | SI | Date From |
| SSUSR_DateFromToday | varchar |  |  | SI | Default Date From to Today |
| SSUSR_DateLastLogin | date |  |  | SI | Date Last Login |
| SSUSR_DateTo | date |  |  | SI | Date To |
| SSUSR_DateToToday | varchar |  |  | SI | Default Date To to Today |
| SSUSR_DateToWhenInactive | date |  |  | SI | Previous DateTo value at the time user was marked ... |
| SSUSR_DefAllResources | varchar |  |  | SI | Default All Resources |
| SSUSR_DefAppointMeth_DR | bigint |  | FK | SI | Des Ref AppointMeth |
| SSUSR_DefApptSlots | varchar |  |  | SI | Def Appt Slots |
| SSUSR_DefDateInDisch | varchar |  |  | SI | Def Date In Discharge form |
| SSUSR_DefDateinOE | varchar |  |  | SI | Default Date in OE |
| SSUSR_DefEpisode | varchar |  |  | SI | Use default EpisodeDep for RB |
| SSUSR_DefRBDepartment_DR | bigint |  | FK | SI | Des REf Department |
| SSUSR_DefRBResource_DR | bigint |  | FK | SI | Des RBResource |
| SSUSR_DefRBService_DR | bigint |  | FK | SI | DEs REf DefRBService |
| SSUSR_DefRefHosp_DR | bigint |  | FK | SI | Des Ref RefHosp |
| SSUSR_DefUseStartTimeEachday | varchar |  |  | SI | SDefUseStartTimeEachday |
| SSUSR_DefaultARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM_DR |
| SSUSR_DefaultCareProv | varchar |  |  | SI | Default Care Prov |
| SSUSR_DefaultDept_DR | bigint |  | FK | SI | DEs Ref to CTLOC |
| SSUSR_DefaultEntryType_DR | bigint |  | FK | SI | Default Entry Type |
| SSUSR_DefaultLocation | varchar |  |  | SI | Default Location |
| SSUSR_DefaultResEntryButtons | varchar |  |  | SI | Default Res Entry Buttons |
| SSUSR_DepartmentHead | varchar |  |  | SI | DepartmentHead |
| SSUSR_DeptforEMRLists | bigint |  |  | SI | Department / Location for EMR lists |
| SSUSR_DisableEMRPreadm | varchar |  |  | SI | Disable EMR for Preadmission |
| SSUSR_Discharged | varchar |  |  | SI | Discharged |
| SSUSR_DisclaimerSigned | date |  |  | SI | DisclaimerSigned |
| SSUSR_DoctorFlag | varchar |  |  | SI | DoctorFlag |
| SSUSR_EMailName | varchar |  |  | SI | Name on E Mail system |
| SSUSR_Email | varchar |  |  | SI | Email |
| SSUSR_Emergency | varchar |  |  | SI | Emergency |
| SSUSR_EnableAPI | varchar |  |  | SI | Enable API access |
| SSUSR_EntryNumberSavedSearches | integer |  |  | SI | Entry Number of Custom Saved Search Tabs (0-5) |
| SSUSR_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| SSUSR_ExternalID2 | varchar |  |  | SI | ExternalID2 |
| SSUSR_ExternalUserIdentifier | varchar |  |  | SI | ExternalUserIdentifier |
| SSUSR_ExtraAccessibilitySupport | varchar |  |  | SI | Enable Extra Accessibility Support |
| SSUSR_FreeText1 | varchar |  |  | SI | FreeText1 |
| SSUSR_FreeText2 | varchar |  |  | SI | FreeText2 |
| SSUSR_FreeText3 | varchar |  |  | SI | FreeText3 |
| SSUSR_GivenName | varchar |  |  | SI | GivenName |
| SSUSR_Group | bigint |  |  | NO | Security Group for the User |
| SSUSR_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| SSUSR_IEPath | varchar |  |  | SI | IEPath |
| SSUSR_Initials | varchar |  |  | NO | Initials (Shortname) |
| SSUSR_Inpatient | varchar |  |  | SI | Inpatient |
| SSUSR_IsThisDoctor | varchar |  |  | SI | Is this a Doctor? |
| SSUSR_LastPAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| SSUSR_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| SSUSR_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| SSUSR_LastUpdateUserHosp_DR | bigint |  | FK | SI | Des Ref LastUpdateUserHosp |
| SSUSR_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| SSUSR_LayoutRestrictions | varchar |  |  | SI | Layout Restrictions. Comma delimited string of val... |
| SSUSR_LinkToBedManagement | varchar |  |  | SI | Link To Bed Management |
| SSUSR_LocList_DR | bigint |  | FK | SI | Des Ref LocList |
| SSUSR_LocationNotMandatoryOnResEntry | varchar |  |  | SI | LocationNotMandatoryOnResEntry |
| SSUSR_LoginID | varchar |  |  | SI | LoginID |
| SSUSR_LoginRound | varchar |  |  | SI | LoginRound |
| SSUSR_MainUserCareProvider | varchar |  |  | SI | Main User for Care Provider |
| SSUSR_MarkInactiveDate | date |  |  | SI | Mark Inactive Date |
| SSUSR_MarkInactiveTime | time |  |  | SI | Mark Inactive Time |
| SSUSR_MarkInactiveUser_DR | bigint |  | FK | SI | Des Ref MarkInactiveUser |
| SSUSR_Mobile | varchar |  |  | SI | Mobile |
| SSUSR_MultiSelectRows | double |  |  | SI | Multi Select Rows |
| SSUSR_NAllORBookNA | varchar |  |  | SI | Do Not Allow ORBookings in Not Avail area |
| SSUSR_NAllORBookNoSess | varchar |  |  | SI | Do Not Allow ORBooking in Non Session area |
| SSUSR_NAllORBookPast | varchar |  |  | SI | Do Not Allow OR Bookings in Past |
| SSUSR_Name | varchar |  |  | NO | Name |
| SSUSR_Name1 | varchar |  |  | SI | Name1 |
| SSUSR_Name2 | varchar |  |  | SI | Name2 |
| SSUSR_Name3 | varchar |  |  | SI | Name3 |
| SSUSR_NoDiagnosis | varchar |  |  | SI | NoDiagnosis |
| SSUSR_NoEMR | varchar |  |  | SI | No EMR flag |
| SSUSR_NoOrders | varchar |  |  | SI | NoOrders |
| SSUSR_NotAllowToOverbook | varchar |  |  | SI | Not Allow To Overbook |
| SSUSR_NotReadResults | varchar |  |  | SI | Not Read Results |
| SSUSR_NurseFlag | varchar |  |  | SI | NurseFlag |
| SSUSR_OtherName | varchar |  |  | SI | OtherName |
| SSUSR_Outpatient | varchar |  |  | SI | Outpatient |
| SSUSR_OwnPatientsOnly | varchar |  |  | SI | Own Patients Only |
| SSUSR_Pager | varchar |  |  | SI | Pager |
| SSUSR_Password | varchar |  |  | NO | SSUSR_Password |
| SSUSR_PasswordAlgorithm | varchar |  |  | SI | Password Algorithm |
| SSUSR_PasswordChanged | varchar |  |  | SI | Password Changed |
| SSUSR_PasswordDate | date |  |  | SI | Password Date |
| SSUSR_PasswordSalt | varchar |  |  | SI | Password Salt |
| SSUSR_PatchingUser | varchar |  |  | SI | PatchingUser  |
| SSUSR_PayrollNumber | double |  |  | SI | PayrollNumber |
| SSUSR_PerformanceStatisticsDisplay | varchar |  |  | SI | Display performance statistics even if system-wide... |
| SSUSR_PersonalCommunity | varchar |  |  | SI | Synchronize User with Personal Community |
| SSUSR_Pin | varchar |  |  | SI | Pin Number |
| SSUSR_PrefOverrideLevel | varchar |  |  | SI | Preference Override Level |
| SSUSR_PrintSecurityLevel | varchar |  |  | SI | Print Security Level |
| SSUSR_PrivilegeStock | varchar |  |  | SI | Privilege for Stock |
| SSUSR_Profile | bigint |  |  | NO | Access Profile for the User |
| SSUSR_Purpose | varchar |  |  | SI | Purpose |
| SSUSR_RBNumberOfRows | double |  |  | SI | RB Number Of Rows |
| SSUSR_RegistrationNumber | varchar |  |  | SI | Registration Number |
| SSUSR_ResEntryButtons | varchar |  |  | SI | Res Entry Buttons |
| SSUSR_RestrictModifDischarge | varchar |  |  | SI | Restrict Modification after Discharge |
| SSUSR_RetainOrderCategory | varchar |  |  | SI | Retain Order Category |
| SSUSR_SSORequired | varchar |  |  | SI | Require user to logon with OpenSSO |
| SSUSR_SSOTest | varchar |  |  | SI | To Test SSO authentication without connection to S... |
| SSUSR_SearchAllAdm | varchar |  |  | SI | Search All Admisions for Orders |
| SSUSR_SearchPrevAdm | varchar |  |  | SI | Search Prev Adm for Order Entry |
| SSUSR_SecurityMessage | varchar |  |  | SI | SecurityMessage |
| SSUSR_SecurityMsgRead | varchar |  |  | SI | SecurityMsgRead |
| SSUSR_Segment_DR | bigint |  | FK | SI | Des Ref to FHCSegment |
| SSUSR_SigCertif | longvarbinary |  |  | SI | Certificate Signature as BinaryStream data |
| SSUSR_SigCertifType | varchar |  |  | SI | Stored Signature Certificate Type |
| SSUSR_Signature | longvarbinary |  |  | SI | Signature as BinaryStream |
| SSUSR_StaffType_DR | bigint |  | FK | SI | Des Ref StaffType |
| SSUSR_Surname | varchar |  |  | SI | Surname |
| SSUSR_TempPassword | varchar |  |  | SI | Temporary Password |
| SSUSR_TemporarilyDisabled | varchar |  |  | SI |  TemporarilyDisabled - Initiated by Patching/CCR (... |
| SSUSR_TimeLastLogin | time |  |  | SI | Time Last Login |
| SSUSR_TimeSinceLastAppt | double |  |  | SI | Time Since Last Appt |
| SSUSR_TimeSincePeriod | varchar |  |  | SI | Time Since Period |
| SSUSR_Title | varchar |  |  | SI | Title |
| SSUSR_Title_DR | bigint |  | FK | SI | Des REf Title |
| SSUSR_TreatmentPathwayOwner | varchar |  |  | SI | TreatmentPathwayOwner |
| SSUSR_TreatmentStageOwner | varchar |  |  | SI | TreatmentStage |
| SSUSR_UseDefaultEpisDep | varchar |  |  | SI | Use Default Epis Dep (for pat registration) |
| SSUSR_UseDeptAsDefault | varchar |  |  | SI | Use Department As Default |
| SSUSR_WarnORBookingMoveRes | varchar |  |  | SI | Warn if user moves ORBooking to another Res |
| SSUSR_WebSecurityAccess | varchar |  |  | SI | Web Security Access |
| SSUSR_YesNo1 | varchar |  |  | SI | YesNo1 |
| SSUSR_YesNo2 | varchar |  |  | SI | YesNo2 |
| SSUSR_YesNo3 | varchar |  |  | SI | YesNo3 |
| SSUSR_YesNo4 | varchar |  |  | SI | YesNo4 |
| SSUSR_YesNo5 | varchar |  |  | SI | YesNo5 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*