# SQLUser.PA_Person

**Schema:** SQLUser
**Columnas:** 317
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPER_RowId | bigint | PK |  | NO | - |
| PAPER_AIFANumber | varchar |  |  | SI | AIFA number |
| PAPER_AccessToServText | varchar |  |  | SI | PAPERAccessToServText |
| PAPER_AccessToServ_DR | bigint |  | FK | SI | Des Ref PACAccessToService |
| PAPER_AccomSetting_DR | bigint |  | FK | SI | Des Ref Accom Setting |
| PAPER_AddrManualEntry | varchar |  |  | SI | Unvalidated address is manually entered |
| PAPER_AddreSamID | varchar |  |  | SI | Address eSam ID |
| PAPER_Address2 | varchar |  |  | SI | Address2 |
| PAPER_AddressGeoLocationCode | varchar |  |  | SI | Address Geo-location Code |
| PAPER_AddressLatitude | varchar |  |  | SI | Address Latitude |
| PAPER_AddressLongitude | varchar |  |  | SI | Address Longitude |
| PAPER_Age | varchar |  |  | SI | Age External |
| PAPER_AgeDay | varchar |  |  | SI | Age In Day |
| PAPER_AgeMth | varchar |  |  | SI | Age In Month |
| PAPER_AgeYr | varchar |  |  | SI | Age In Year |
| PAPER_AppartmentNo | varchar |  |  | SI | AppartmentNo |
| PAPER_AppointTransport_DR | bigint |  | FK | SI | Des Ref RBCAppointTransport |
| PAPER_AppointmentSMS | varchar |  |  | SI | AppointmentSMS |
| PAPER_AusSouthSeaIslander_DR | bigint |  | FK | SI | Des Ref AusSouthSeaIslander |
| PAPER_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAPER_BGOverwriteReason_DR | bigint |  | FK | SI | Reason for overwritting the lab blood group |
| PAPER_BGTestSetItem_DR | varchar |  | FK | SI | Lab Enterprise Test Set Item from which the bloog ... |
| PAPER_BGUpdateDate | date |  |  | SI | Lab Blood Group Update Date |
| PAPER_BGUpdateTime | time |  |  | SI | Lab Blood Group Update Time |
| PAPER_BGUpdateUser_DR | bigint |  | FK | SI | Lab Blood Group Update User |
| PAPER_BillCode | varchar |  |  | SI | Bill Code |
| PAPER_BirthGender_DR | bigint |  | FK | SI | Birth Gender DR |
| PAPER_BirthOrderNumber | integer |  |  | SI | Birth Order Number |
| PAPER_BloodGroupStatus | varchar |  |  | SI | Lab Blood Group Status |
| PAPER_BloodGroup_DR | bigint |  | FK | SI | Lab Blood Group |
| PAPER_BloodType_DR | bigint |  | FK | SI | Des Ref Blood type |
| PAPER_CCC1 | varchar |  |  | SI | CCC1 |
| PAPER_CCC2 | varchar |  |  | SI | CCC2 |
| PAPER_CCC3 | varchar |  |  | SI | CCC3 |
| PAPER_CCC4 | varchar |  |  | SI | CCC4 |
| PAPER_CCC5 | varchar |  |  | SI | CCC5 |
| PAPER_CCC6 | varchar |  |  | SI | CCC6 |
| PAPER_CTRLT_DR | bigint |  | FK | SI | Des Ref CTRLT |
| PAPER_CT_HCA_DR | bigint |  | FK | SI | Des Ref CT_HCA |
| PAPER_CT_Province_DR | bigint |  | FK | SI | Des Ref CT_Province |
| PAPER_CT_Region_DR | bigint |  | FK | SI | Des Ref CT_Region |
| PAPER_CanLeaveMessagesOn | varchar |  |  | SI | CanLeaveMessagesOn |
| PAPER_CancerReg | varchar |  |  | SI | CancerReg |
| PAPER_Caregiver | varchar |  |  | SI | Caregiver  |
| PAPER_CaregiverContactDetails | varchar |  |  | SI | Caregiver Contact Details |
| PAPER_CarerAvailability_DR | bigint |  | FK | SI | Des Ref CarerAvailability |
| PAPER_ChildrenAlive | double |  |  | SI | Children Alive |
| PAPER_ChineseAddress | varchar |  |  | SI | ChineseAddress |
| PAPER_ChineseArea | varchar |  |  | SI | ChineseArea |
| PAPER_ChineseDistrict | varchar |  |  | SI | ChineseDistrict |
| PAPER_ChineseName | varchar |  |  | SI | ChineseName |
| PAPER_CitizenshipStatusSource_DR | bigint |  | FK | SI | Des Ref to PACCitizenshipStatusSource |
| PAPER_CitizenshipStatus_DR | bigint |  | FK | SI | Des Ref to PACCitizenshipStatus |
| PAPER_CityArea_DR | bigint |  | FK | SI | Des Ref CityArea |
| PAPER_CityBirth_DR | bigint |  | FK | SI | Des Ref CityBirth |
| PAPER_CityCode_DR | bigint |  | FK | SI | Des Ref to CTCIT |
| PAPER_CommunicationNeeds_DR | bigint |  | FK | SI | Des Ref PACCommunicationNeeds |
| PAPER_CommunicationPrefs_DR | bigint |  | FK | SI | Des Ref PACCommunicationPrefs |
| PAPER_Complement | varchar |  |  | SI | Complement |
| PAPER_ConcessCardType_DR | bigint |  | FK | SI | Des Ref to PACConcessionCardType |
| PAPER_ConcessionCardStatus | varchar |  |  | SI | ConcessionCardStatus |
| PAPER_ConfidentialityCode_DR | bigint |  | FK | SI | Des Ref PACConfidentialityCode |
| PAPER_ContactNotes | varchar |  |  | SI | ContactNotes |
| PAPER_CountryCameFrom_DR | bigint |  | FK | SI | Des Ref Country |
| PAPER_CountryOfBirthSource_DR | bigint |  | FK | SI | Des Ref to PACCountryOfBirthSource |
| PAPER_Country_Birth_DR | bigint |  | FK | SI | Des Ref to Country |
| PAPER_Country_DR | bigint |  | FK | SI | Des Ref to CTCOU |
| PAPER_DVAExpiryDate | date |  |  | SI | DVAExpiryDate |
| PAPER_DateAdded | date |  |  | SI | DateAdded |
| PAPER_DateCreatePhoto | date |  |  | SI | DateCreatePhoto |
| PAPER_DateOfBirthSource_DR | bigint |  | FK | SI | Des Ref to PACDateOfBirthSource |
| PAPER_DateOfDeathSource_DR | bigint |  | FK | SI | Des Ref to PACDateOfDeathSource |
| PAPER_DateOfEntry | date |  |  | SI | Date Of Entry |
| PAPER_DateOfInterview | date |  |  | SI | Date Of Interview |
| PAPER_DateRegToNHS | date |  |  | SI | Date of Patient Registration to NHS  |
| PAPER_DateTermFromNHS | date |  |  | SI | Date of Patient Termination from NHS  |
| PAPER_DateUpdatePhoto | date |  |  | SI | DateUpdatePhoto |
| PAPER_DeathNotificationStatus | varchar |  |  | SI | DeathNotificationStatus |
| PAPER_Debtor_DR | bigint |  | FK | SI | Des Ref to ARC_Debtor |
| PAPER_Deceased | varchar |  |  | SI | Deceased |
| PAPER_DeceasedOutsideHosp | varchar |  |  | SI | Deceased Outside The Hospital |
| PAPER_DeceasedTime | time |  |  | SI | Deceased Time |
| PAPER_Deceased_Date | date |  |  | SI | Deceased Date |
| PAPER_DentalDisplay | varchar |  |  | SI | DentalDisplay |
| PAPER_DependChildren_DR | bigint |  | FK | SI | Des Ref DependChildren |
| PAPER_DependUponPatText | varchar |  |  | SI | DependUponPatText |
| PAPER_DependUponPat_DR | bigint |  | FK | SI | Des Ref DependencyUponPatient |
| PAPER_DependentLocality | varchar |  |  | SI | DependentLocality |
| PAPER_DesUsualHCConsent | varchar |  |  | SI | Designated Usual Health Centre Consent |
| PAPER_DiscDateFrom | date |  |  | SI | Discount Date From |
| PAPER_DiscDateTo | date |  |  | SI | Discount Date To |
| PAPER_DiscType_DR | bigint |  | FK | SI | Des Ref DiscType |
| PAPER_DiscretOutsType_DR | bigint |  | FK | SI | Discret OutsType |
| PAPER_Dob | date |  |  | SI | Person Date Of Birth |
| PAPER_DocNumber | varchar |  |  | SI | DocNumber |
| PAPER_DocTypePlaceIssue1 | varchar |  |  | SI | DocTypePlaceIssue1 |
| PAPER_DocTypePlaceIssue2 | varchar |  |  | SI | DocTypePlaceIssue2 |
| PAPER_DoctorDeclared_DR | varchar |  | FK | SI | Des Ref DoctorDeclared as deceased |
| PAPER_DomicileCode | varchar |  |  | SI | Domicile Code |
| PAPER_DonatedOrgansOnDeath | varchar |  |  | SI | Donated Organs On Death |
| PAPER_EXT_EHRConsent | varchar |  |  | SI | MHR Consent |
| PAPER_Education_DR | bigint |  | FK | SI | Des Ref Education |
| PAPER_EffDateCurrAddress | date |  |  | SI | EffDateCurrAddress |
| PAPER_Email | varchar |  |  | SI | Email |
| PAPER_Email2 | varchar |  |  | SI | Email2 |
| PAPER_EmplDep_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| PAPER_EmplRelatedTo | varchar |  |  | SI | Employee Related To |
| PAPER_EmplType_DR | bigint |  | FK | SI | Des Ref EmplType |
| PAPER_EmployeeCoContract | varchar |  |  | SI | Contract with the employees company |
| PAPER_EmployeeCompany | bigint |  |  | SI | Company the person works for |
| PAPER_EmployeeDateFrom | date |  |  | SI | EmployeeDateFrom |
| PAPER_EmployeeDateTo | date |  |  | SI | Employee DateTo |
| PAPER_EmployeeFunction | bigint |  |  | SI | Employee Function |
| PAPER_EmployeeGrade | varchar |  |  | SI | EmployeeGrade |
| PAPER_EmployeeNo | varchar |  |  | SI | Employee No |
| PAPER_EmploymentStat_DR | bigint |  | FK | SI | Des Ref EmploymentStat |
| PAPER_EstAgeMonth | double |  |  | SI | Estimated Age in Month |
| PAPER_EstAgeTmStmp | date |  |  | SI | Estimate Age Time Stamp |
| PAPER_EstAgeYear | double |  |  | SI | Estimated Age in Year |
| PAPER_EstDOB | varchar |  |  | SI | PAPEstDOB |
| PAPER_EstimateDOBInFuture | varchar |  |  | SI | EstimateDOBInFuture |
| PAPER_ExemptionNumber | varchar |  |  | SI | Exemption Number |
| PAPER_ExpectedPayDate | date |  |  | SI | Expected Pay Date |
| PAPER_ExtAccessCode | varchar |  |  | SI | External Access Code |
| PAPER_ExtDocumAccessStat_DR | bigint |  | FK | SI | External Document Access Status |
| PAPER_ExtVerNumber | varchar |  |  | SI | External Version Number |
| PAPER_ExternalOIDs | varchar |  |  | SI | ExternalOIDs |
| PAPER_FHCArea_DR | bigint |  | FK | SI | Des Ref FHCArea |
| PAPER_FHCMicroArea_DR | bigint |  | FK | SI | Des Ref FHCMicroArea |
| PAPER_FHCSegment_DR | bigint |  | FK | SI | Des Ref FHCSegment |
| PAPER_FamDocPractice | varchar |  |  | SI | FamDocPractice |
| PAPER_FamilyDoctorClinic_DR | varchar |  | FK | SI | Des Ref FamilyDoctorClinic |
| PAPER_FamilyDoctor_DR | bigint |  | FK | SI | Des Ref Ref Doctor |
| PAPER_FamilyGroup_DR | bigint |  | FK | SI | Des Ref FamilyGroup |
| PAPER_FamilyLinkText | varchar |  |  | SI | FamilyLinkText |
| PAPER_FatherName | varchar |  |  | SI | FatherName |
| PAPER_FatherSurname | varchar |  |  | SI | FatherSurname |
| PAPER_Father_DR | bigint |  | FK | SI | Des REf Father |
| PAPER_Fax | varchar |  |  | SI | Fax |
| PAPER_FeedBackConsent | varchar |  |  | SI | FeedBackConsent |
| PAPER_FeedbackConsentDate | date |  |  | SI | FeedbackConsentDate |
| PAPER_FetusID | varchar |  |  | SI | Fetus Identifier |
| PAPER_ForeignAddress | varchar |  |  | SI | Foreign Address |
| PAPER_ForeignCity | varchar |  |  | SI | Foreign City |
| PAPER_ForeignCountry | varchar |  |  | SI | Foreign Country |
| PAPER_ForeignId | varchar |  |  | SI | ForeignID |
| PAPER_ForeignNotes | varchar |  |  | SI | ForeignNotes |
| PAPER_ForeignPhone | varchar |  |  | SI | Foreign Phone |
| PAPER_ForeignPostCode | varchar |  |  | SI | Foreign Post Code |
| PAPER_ForeignSuburb | varchar |  |  | SI | Foreign Suburb |
| PAPER_FreeText1 | varchar |  |  | SI | FreeText1 |
| PAPER_FreeText2 | varchar |  |  | SI | FreeText2 |
| PAPER_FreeText3 | varchar |  |  | SI | FreeText3 |
| PAPER_FreeText4 | varchar |  |  | SI | FreeText4 |
| PAPER_FreeText5 | varchar |  |  | SI | FreeText5 |
| PAPER_FromThisArea | varchar |  |  | SI | From This Area |
| PAPER_GLFlag | varchar |  |  | SI | GLFlag |
| PAPER_GPConsent | varchar |  |  | SI | GP Consent |
| PAPER_GenderIdentity_DR | bigint |  | FK | SI | Des Ref to CTGenderIdentity |
| PAPER_GenderPronounsList | varchar |  |  | SI | List of Gender Pronouns CTGenderPronouns  |
| PAPER_GenderPronouns_DR | bigint |  | FK | SI | Des Ref to CTGenderPronouns |
| PAPER_GestationDays | double |  |  | SI | Gestation Days |
| PAPER_GestationWeeks | double |  |  | SI | Gestation weeks |
| PAPER_GovernCardNo | varchar |  |  | SI | Government Card No |
| PAPER_Gravida | double |  |  | SI | Gravida |
| PAPER_Guarantor_DR | varchar |  | FK | SI | Des Ref to PANok |
| PAPER_Guardian1_DR | bigint |  | FK | SI | Des Ref PAPER |
| PAPER_Guardian2_DR | bigint |  | FK | SI | Des Ref PAPER |
| PAPER_HCP_DR | bigint |  | FK | SI | Des Ref HCP |
| PAPER_HSCommunityEnrollmentComment | varchar |  |  | SI | Personal Community Enrollment comments |
| PAPER_HSCommunityEnrollmentStatus | varchar |  |  | SI | Personal Community Enrollment Status |
| PAPER_HealthCentre_DR | bigint |  | FK | SI | Health Centre |
| PAPER_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAPER_House_Building_No | varchar |  |  | SI | House building_No |
| PAPER_ID | varchar |  |  | SI | Person ID (ICPPBC) |
| PAPER_IDDocType_DR | bigint |  | FK | SI | Des Ref IDDocType |
| PAPER_IDStatus_DR | bigint |  | FK | SI | Des Ref to PACIDStatus |
| PAPER_IDValidDate | date |  |  | SI | Last ID Validation Date  |
| PAPER_IDValidDateFrom | date |  |  | SI | Patient ID Valid From   |
| PAPER_IDValidDateTo | date |  |  | SI | Patient ID Valid To   |
| PAPER_IncompleteRegistration | varchar |  |  | SI | Incomplete Registration |
| PAPER_IndigStat_DR | bigint |  | FK | SI | Des Ref IndigStat |
| PAPER_InsCardOwner | varchar |  |  | SI | Insurance Card Owner |
| PAPER_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PAPER_InsuranceCardHolder | varchar |  |  | SI | Insurance Card Holder |
| PAPER_InterpreterRequired | varchar |  |  | SI | Interpreter Required |
| PAPER_InterviewedBy | varchar |  |  | SI | Interviewed By |
| PAPER_JobTitle | varchar |  |  | SI | Job Title |
| PAPER_LBCSpecies_DR | bigint |  | FK | SI | Species DR |
| PAPER_LangPrim_DR | bigint |  | FK | SI | Des Ref to CTLAN |
| PAPER_LanguageSpokenAtHome_DR | bigint |  | FK | SI | Des Ref to PACPreferredLanguage |
| PAPER_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAPER_LateTOP | double |  |  | SI | LateTOP |
| PAPER_LivesWith | varchar |  |  | SI | LivesWith |
| PAPER_LivingArrangement_DR | bigint |  | FK | SI | Des Ref LivingArrangement |
| PAPER_LivingChild | double |  |  | SI | LivingChild |
| PAPER_LocationOfDeath | varchar |  |  | SI | Location Of Death |
| PAPER_Marital_DR | bigint |  | FK | SI | Des Ref to CTMAR |
| PAPER_MentalHealthArea_DR | bigint |  | FK | SI | Mental Health Area |
| PAPER_Miscarriage | double |  |  | SI | Miscarriage |
| PAPER_MobPhone | varchar |  |  | SI | MobPhone |
| PAPER_MotherName | varchar |  |  | SI | MotherName |
| PAPER_MotherSurname | varchar |  |  | SI | MotherSurname |
| PAPER_Mother_DR | bigint |  | FK | SI | Des Ref Mother |
| PAPER_MultBirth | double |  |  | SI | MultBirth |
| PAPER_NOKBusPhone | varchar |  |  | SI | NOK Business Phone |
| PAPER_NOKInformed | varchar |  |  | SI | NOKInformed |
| PAPER_Name | varchar |  |  | NO | Person Name |
| PAPER_Name2 | varchar |  |  | SI | Person Name 2 |
| PAPER_Name3 | varchar |  |  | SI | Patient Name3 |
| PAPER_Name4 | varchar |  |  | SI | Name4 |
| PAPER_Name5 | varchar |  |  | SI | Name5 |
| PAPER_Name6 | varchar |  |  | SI | Name6 |
| PAPER_Name7 | varchar |  |  | SI | Name7 |
| PAPER_Name8 | varchar |  |  | SI | Name8 |
| PAPER_NameID | varchar |  |  | SI | Name ID |
| PAPER_NameSource_DR | bigint |  | FK | SI | Name Source - Des Ref to PACNameSource |
| PAPER_Nation_DR | bigint |  | FK | SI | Des Ref to CTNAT |
| PAPER_NationalIDCreationDate | date |  |  | SI | National ID Creation Date |
| PAPER_NationalResident | varchar |  |  | SI | National Resident |
| PAPER_NoChinName | varchar |  |  | SI | NoChinName |
| PAPER_NokAddress1 | varchar |  |  | SI | Nok Address |
| PAPER_NokAddress2 | varchar |  |  | SI | NokAddress2 |
| PAPER_NokCTRLT_DR | bigint |  | FK | SI | Des Ref CTRLT |
| PAPER_NokCity_DR | bigint |  | FK | SI | Des Ref City |
| PAPER_NokName | varchar |  |  | SI | Next of Kin Name |
| PAPER_NokPhone | varchar |  |  | SI | Next of Kin Phone |
| PAPER_NokText | varchar |  |  | SI | Next of Kin Text |
| PAPER_NokZip_DR | bigint |  | FK | SI | Des Ref NZip |
| PAPER_NotValidAddrReason_DR | bigint |  | FK | SI | Not Validated Address Reason - Des Ref to PACNotVa... |
| PAPER_OSVStatus_DR | bigint |  | FK | SI | Des Ref OSVStatus |
| PAPER_Occupation | varchar |  |  | SI | Occupation |
| PAPER_Occupation_DR | bigint |  | FK | SI | Des Ref Occupation |
| PAPER_OtherPronouns | varchar |  |  | SI | Pronoun Description |
| PAPER_OutstandAmt | double |  |  | SI | Outstanding Amt |
| PAPER_OutstandingDate | date |  |  | SI | Outstanding Date |
| PAPER_Outstation_DR | bigint |  | FK | SI | Outstation |
| PAPER_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPER_PAPMI_DR |
| PAPER_PDSSerialNumber | varchar |  |  | SI | PDSSerialNumber |
| PAPER_Pager | varchar |  |  | SI | Pager |
| PAPER_Para | double |  |  | SI | Para |
| PAPER_ParaDisplayUK | double |  |  | SI | ParaDisplayUK |
| PAPER_PassportExpiryDate | date |  |  | SI | Passport Expiry Date |
| PAPER_PassportNumber | varchar |  |  | SI | PassportNumber |
| PAPER_PassportPlaceIssue | varchar |  |  | SI | PassportPlaceIssue |
| PAPER_PatType_DR | bigint |  | FK | SI | Des Ref PatType |
| PAPER_PatientDetConfirmed | varchar |  |  | SI | PatientDetConfirmed |
| PAPER_PensionCardExpiryDate | date |  |  | SI | PensionCardExpiryDate |
| PAPER_Photo | varchar |  |  | SI | Photo |
| PAPER_PhotoDocument | bigint |  |  | SI | PhotoDocument |
| PAPER_PostCode | varchar |  |  | SI | PostCode |
| PAPER_PreTerm | double |  |  | SI | PreTerm |
| PAPER_PrefCareProvGender_DR | bigint |  | FK | SI | Des Ref CTSex |
| PAPER_PrefContDelivMode_DR | bigint |  | FK | SI | Des Ref PACContDelivMode |
| PAPER_PrefGenderInterpreter_DR | bigint |  | FK | SI | Des Ref CTSex |
| PAPER_PrefLanguage_DR | bigint |  | FK | SI | Des Ref PrefLanguage |
| PAPER_PreferredContactMethod | varchar |  |  | SI | PreferredContactMethod |
| PAPER_PrevHACCEligible | varchar |  |  | SI | Prev HACC Eligible |
| PAPER_PrimaryHouseholdMember | varchar |  |  | SI | PrimaryHouseholdMember |
| PAPER_ProcuratorFiscalInformed | varchar |  |  | SI | Procurator Fiscal Informed |
| PAPER_Province_Birth_DR | bigint |  | FK | SI | Des Ref Province of Birth |
| PAPER_ReasonForAttention | varchar |  |  | SI | ReasonForAttention |
| PAPER_ReasonForChangeData | varchar |  |  | SI | Reason For Change Data |
| PAPER_RefCareProvConsent | varchar |  |  | SI | Referring Care Provider Consent |
| PAPER_RefugeeStatus_DR | bigint |  | FK | SI | Des Ref to PACRefugeeStatus |
| PAPER_RegionBirth_DR | bigint |  | FK | SI | Des Ref Region |
| PAPER_Religion_DR | bigint |  | FK | SI | Des Ref to CTRLG |
| PAPER_Remark | varchar |  |  | SI | Remark |
| PAPER_ResidenceStatus_DR | bigint |  | FK | SI | Des Ref ResidenceStatus |
| PAPER_ResidencySource_DR | bigint |  | FK | SI | Residency Source - Des Ref to PACResidencySource |
| PAPER_ResidentNumber | varchar |  |  | SI | ResidentNumber |
| PAPER_ResponsibleForPayment | bigint |  |  | SI | Responsible For Payment |
| PAPER_ReversedBy | varchar |  |  | SI | ReversedBy |
| PAPER_SMSConsent | varchar |  |  | SI | SMS Consent |
| PAPER_SNSLastLiveUpdDate | date |  |  | SI | SNSLastLiveUpdDate |
| PAPER_SNSLastReviewDate | date |  |  | SI | SpecNeedStatLastReviewDate |
| PAPER_SNSNextReviewDate | date |  |  | SI | SNSNextReviewDate |
| PAPER_SecondPhone | varchar |  |  | SI | Second Phone |
| PAPER_SelfGuarantor | varchar |  |  | SI | Self Guarantor |
| PAPER_SendWrittenComm1stCont | varchar |  |  | SI | Send Written Communication to First Contact |
| PAPER_Sex_DR | bigint |  | FK | NO | Des Ref to CTSEX |
| PAPER_SexualOrientation_DR | bigint |  | FK | SI | Des Ref to CTSexualOrientation |
| PAPER_SocialStatusList | varchar |  |  | SI | List of Social Status - Des Ref to CTSocialStatus |
| PAPER_SocialStatus_DR | bigint |  | FK | SI | Des Ref Social Status |
| PAPER_Soundex1 | varchar |  |  | SI | Soundex1 |
| PAPER_Soundex2 | varchar |  |  | SI | Soundex2 |
| PAPER_Soundex3 | varchar |  |  | SI | Soundex3 |
| PAPER_SourceOfIncome_DR | bigint |  | FK | SI | Des Ref SourceOfIncome |
| PAPER_SpecNeedStat_DR | bigint |  | FK | SI | Des Ref SpecNeedStat |
| PAPER_StName | varchar |  |  | SI | Person Street |
| PAPER_StNameLine1 | varchar |  |  | SI | Line 1 of St Name |
| PAPER_StateCode_DR | bigint |  | FK | SI | Des Ref to CTSTT |
| PAPER_StayingPermanently | varchar |  |  | SI | Staying Permanently |
| PAPER_StillBirth | double |  |  | SI | StillBirth |
| PAPER_SurName | varchar |  |  | SI | Sur Name (Computered) |
| PAPER_TOP | double |  |  | SI | TOP |
| PAPER_TelH | varchar |  |  | SI | Telephone No(Home) |
| PAPER_TelO | varchar |  |  | SI | Telephone No(Office) |
| PAPER_TimeCreatePhoto | time |  |  | SI | TimeCreatePhoto |
| PAPER_TimeUpdatePhoto | time |  |  | SI | TimeUpdatePhoto |
| PAPER_Title_DR | bigint |  | FK | SI | Des Ref Title |
| PAPER_TransportUsed_DR | bigint |  | FK | SI | Des Ref TransportUsed |
| PAPER_TravelVisaEndDate | date |  |  | SI | Travel Visa End Date |
| PAPER_TravelVisaNumber | varchar |  |  | SI | Travel Visa Number |
| PAPER_TravelVisaStartDate | date |  |  | SI | Travel Visa Start Date |
| PAPER_TravelVisaType_DR | bigint |  | FK | SI | Des Ref to CTVisaType - Travel Visa Type |
| PAPER_UpdateDate | date |  |  | SI | Update Date |
| PAPER_UpdateTime | time |  |  | SI | Update Time |
| PAPER_UserAdded_DR | bigint |  | FK | SI | Des Ref UserAdded_DR |
| PAPER_UserCreatePhoto | bigint |  |  | SI | UserCreatePhoto |
| PAPER_UserUpdate | bigint |  |  | SI | UserUpdate |
| PAPER_UserUpdatePhoto | bigint |  |  | SI | UserUpdatePhoto |
| PAPER_UsualRound_DR | bigint |  | FK | SI | Des Ref Resource |
| PAPER_WebConferencingID | varchar |  |  | SI | Web Conferencing ID |
| PAPER_WhoNotified | varchar |  |  | SI | Who Notified about death |
| PAPER_WrittenCommFormat_DR | bigint |  | FK | SI | Des Ref PACWrittenCommFormat |
| PAPER_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*