# SQLUser.PA_PersonPatMas

**Schema:** SQLUser
**Columnas:** 227
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPER_RowId | bigint | PK |  | NO | - |
| PAPER_AccomSetting_DR | bigint |  | FK | SI | Des Ref Accom Setting |
| PAPER_Address2 | varchar |  |  | SI | Address2 |
| PAPER_Age | varchar |  |  | SI | Age External |
| PAPER_AgeDay | varchar |  |  | SI | Age In Day |
| PAPER_AgeMth | varchar |  |  | SI | Age In Month |
| PAPER_AgeYr | varchar |  |  | SI | Age In Year |
| PAPER_AusSouthSeaIslander_DR | bigint |  | FK | SI | Des Ref AusSouthSeaIslander |
| PAPER_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAPER_BillCode | varchar |  |  | SI | Bill Code |
| PAPER_BloodType_DR | bigint |  | FK | SI | Des Ref Blood type |
| PAPER_CTRLT_DR | bigint |  | FK | SI | Des Ref CTRLT |
| PAPER_CT_HCA_DR | bigint |  | FK | SI | Des Ref CT_HCA |
| PAPER_CT_Province_DR | bigint |  | FK | SI | Des Ref CT_Province |
| PAPER_CT_Region_DR | bigint |  | FK | SI | Des Ref CT_Region |
| PAPER_CancerReg | varchar |  |  | SI | CancerReg |
| PAPER_CityArea_DR | bigint |  | FK | SI | Des Ref CityArea |
| PAPER_CityBirth_DR | bigint |  | FK | SI | Des Ref CityBirth |
| PAPER_CityCode_DR | bigint |  | FK | SI | Des Ref to CTCIT |
| PAPER_Complement | varchar |  |  | SI | Complement |
| PAPER_ContactNotes | varchar |  |  | SI | ContactNotes |
| PAPER_CountryCameFrom_DR | bigint |  | FK | SI | Des Ref Country |
| PAPER_Country_Birth_DR | bigint |  | FK | SI | Des Ref to Country |
| PAPER_Country_DR | bigint |  | FK | SI | Des Ref to CTCOU |
| PAPER_DVAExpiryDate | date |  |  | SI | DVAExpiryDate |
| PAPER_DateAdded | date |  |  | SI | DateAdded |
| PAPER_DateOfEntry | date |  |  | SI | Date Of Entry |
| PAPER_DateOfInterview | date |  |  | SI | Date Of Interview |
| PAPER_Debtor_DR | bigint |  | FK | SI | Des Ref to ARC_Debtor |
| PAPER_Deceased | varchar |  |  | SI | Deceased |
| PAPER_DeceasedTime | time |  |  | SI | Deceased Time |
| PAPER_Deceased_Date | date |  |  | SI | Deceased Date |
| PAPER_DentalDisplay | varchar |  |  | SI | DentalDisplay |
| PAPER_DependChildren_DR | bigint |  | FK | SI | Des Ref DependChildren |
| PAPER_DiscDateFrom | date |  |  | SI | Discount Date From |
| PAPER_DiscDateTo | date |  |  | SI | Discount Date To |
| PAPER_DiscType_DR | bigint |  | FK | SI | Des Ref DiscType |
| PAPER_DiscretOutsType_DR | bigint |  | FK | SI | Discret OutsType |
| PAPER_Dob | date |  |  | SI | Person Date Of Birth |
| PAPER_DocNumber | varchar |  |  | SI | DocNumber |
| PAPER_DoctorDeclared_DR | varchar |  | FK | SI | Des Ref DoctorDeclared as deceased |
| PAPER_DonatedOrgansOnDeath | varchar |  |  | SI | Donated Organs On Death |
| PAPER_Education_DR | bigint |  | FK | SI | Des Ref Education |
| PAPER_EffDateCurrAddress | date |  |  | SI | EffDateCurrAddress |
| PAPER_Email | varchar |  |  | SI | Email |
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
| PAPER_ExemptionNumber | varchar |  |  | SI | Exemption Number |
| PAPER_ExpectedPayDate | date |  |  | SI | Expected Pay Date |
| PAPER_FamilyDoctorClinic_DR | varchar |  | FK | SI | Des Ref FamilyDoctorClinic |
| PAPER_FamilyDoctor_DR | bigint |  | FK | SI | Des Ref Ref Doctor |
| PAPER_FamilyGroup_DR | bigint |  | FK | SI | Des Ref FamilyGroup |
| PAPER_FamilyLinkText | varchar |  |  | SI | FamilyLinkText |
| PAPER_Father_DR | bigint |  | FK | SI | Des REf Father |
| PAPER_FeedBackConsent | varchar |  |  | SI | FeedBackConsent |
| PAPER_FeedbackConsentDate | date |  |  | SI | FeedbackConsentDate |
| PAPER_ForeignAddress | varchar |  |  | SI | Foreign Address |
| PAPER_ForeignCity | varchar |  |  | SI | Foreign City |
| PAPER_ForeignCountry | varchar |  |  | SI | Foreign Country |
| PAPER_ForeignId | varchar |  |  | SI | ForeignID |
| PAPER_ForeignNotes | varchar |  |  | SI | ForeignNotes |
| PAPER_ForeignPhone | varchar |  |  | SI | Foreign Phone |
| PAPER_ForeignPostCode | varchar |  |  | SI | Foreign Post Code |
| PAPER_FromThisArea | varchar |  |  | SI | From This Area |
| PAPER_GLFlag | varchar |  |  | SI | GLFlag |
| PAPER_GovernCardNo | varchar |  |  | SI | Government Card No |
| PAPER_Guardian1_DR | bigint |  | FK | SI | Des Ref PAPER |
| PAPER_Guardian2_DR | bigint |  | FK | SI | Des Ref PAPER |
| PAPER_HCP_DR | bigint |  | FK | SI | Des Ref HCP |
| PAPER_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAPER_ID | varchar |  |  | SI | Person ID (ICPPBC) |
| PAPER_IDDocType_DR | bigint |  | FK | SI | Des Ref IDDocType |
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
| PAPER_LangPrim_DR | bigint |  | FK | SI | Des Ref to CTLAN |
| PAPER_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| PAPER_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAPER_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| PAPER_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| PAPER_LivingArrangement_DR | bigint |  | FK | SI | Des Ref LivingArrangement |
| PAPER_LocationOfDeath | varchar |  |  | SI | Location Of Death |
| PAPER_Marital_DR | bigint |  | FK | SI | Des Ref to CTMAR |
| PAPER_MobPhone | varchar |  |  | SI | MobPhone |
| PAPER_Mother_DR | bigint |  | FK | SI | Des Ref Mother |
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
| PAPER_Nation_DR | bigint |  | FK | SI | Des Ref to CTNAT |
| PAPER_NationalResident | varchar |  |  | SI | National Resident |
| PAPER_NokAddress1 | varchar |  |  | SI | Nok Address |
| PAPER_NokAddress2 | varchar |  |  | SI | NokAddress2 |
| PAPER_NokCTRLT_DR | bigint |  | FK | SI | Des Ref CTRLT |
| PAPER_NokCity_DR | bigint |  | FK | SI | Des Ref City |
| PAPER_NokName | varchar |  |  | SI | Next of Kin Name |
| PAPER_NokPhone | varchar |  |  | SI | Next of Kin Phone |
| PAPER_NokText | varchar |  |  | SI | Next of Kin Text |
| PAPER_NokZip_DR | bigint |  | FK | SI | Des Ref NZip |
| PAPER_OSVStatus_DR | bigint |  | FK | SI | Des Ref OSVStatus |
| PAPER_Occupation | varchar |  |  | SI | Occupation |
| PAPER_Occupation_DR | bigint |  | FK | SI | Des Ref Occupation |
| PAPER_OutstandAmt | double |  |  | SI | Outstanding Amt |
| PAPER_OutstandingDate | date |  |  | SI | Outstanding Date |
| PAPER_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPER_PAPMI_DR |
| PAPER_PAPatMas2_DR | bigint |  | FK | SI | Des Ref PAPatMas2 |
| PAPER_PDSSerialNumber | varchar |  |  | SI | PDSSerialNumber |
| PAPER_PassportNumber | varchar |  |  | SI | PassportNumber |
| PAPER_PatType_DR | bigint |  | FK | SI | Des Ref PatType |
| PAPER_PensionCardExpiryDate | date |  |  | SI | PensionCardExpiryDate |
| PAPER_Photo | varchar |  |  | SI | Photo |
| PAPER_PrefLanguage_DR | bigint |  | FK | SI | Des Ref PrefLanguage |
| PAPER_PreferredContactMethod | varchar |  |  | SI | PreferredContactMethod |
| PAPER_PrevHACCEligible | varchar |  |  | SI | Prev HACC Eligible |
| PAPER_ProcuratorFiscalInformed | varchar |  |  | SI | Procurator Fiscal Informed |
| PAPER_Province_Birth_DR | bigint |  | FK | SI | Des Ref Province of Birth |
| PAPER_ReasonForChangeData | varchar |  |  | SI | Reason For Change Data |
| PAPER_RegionBirth_DR | bigint |  | FK | SI | Des Ref Region |
| PAPER_Religion_DR | bigint |  | FK | SI | Des Ref to CTRLG |
| PAPER_Remark | varchar |  |  | SI | Remark |
| PAPER_ResidenceStatus_DR | bigint |  | FK | SI | Des Ref ResidenceStatus |
| PAPER_ResponsibleForPayment | bigint |  |  | SI | Responsible For Payment |
| PAPER_ReversedBy | varchar |  |  | SI | ReversedBy |
| PAPER_SecondPhone | varchar |  |  | SI | Second Phone |
| PAPER_Sex_DR | bigint |  | FK | NO | Des Ref to CTSEX |
| PAPER_SocialStatus_DR | bigint |  | FK | SI | Des Ref Social Status |
| PAPER_Soundex1 | varchar |  |  | SI | Soundex1 |
| PAPER_Soundex2 | varchar |  |  | SI | Soundex2 |
| PAPER_Soundex3 | varchar |  |  | SI | Soundex3 |
| PAPER_SourceOfIncome_DR | bigint |  | FK | SI | Des Ref SourceOfIncome |
| PAPER_StName | varchar |  |  | SI | Person Street |
| PAPER_StNameLine1 | varchar |  |  | SI | Line 1 of St Name |
| PAPER_StateCode_DR | bigint |  | FK | SI | Des Ref to CTSTT |
| PAPER_StayingPermanently | varchar |  |  | SI | Staying Permanently |
| PAPER_SurName | varchar |  |  | SI | Sur Name (Computered) |
| PAPER_TelH | varchar |  |  | SI | Telephone No(Home) |
| PAPER_TelO | varchar |  |  | SI | Telephone No(Office) |
| PAPER_Title_DR | bigint |  | FK | SI | Des Ref Title |
| PAPER_TransportUsed_DR | bigint |  | FK | SI | Des Ref TransportUsed |
| PAPER_UpdateDate | date |  |  | SI | Update Date |
| PAPER_UpdateTime | time |  |  | SI | Update Time |
| PAPER_UserAdded_DR | bigint |  | FK | SI | Des Ref UserAdded_DR |
| PAPER_UserCheck1 | varchar |  |  | SI | UserCheck1 |
| PAPER_UserCheck2 | varchar |  |  | SI | UserCheck2 |
| PAPER_UserCheck3 | varchar |  |  | SI | UserCheck3 |
| PAPER_UserHospital_DR | bigint |  | FK | SI | Des Ref UserHospital |
| PAPER_UserText1 | varchar |  |  | SI | UserText1 |
| PAPER_UserText2 | varchar |  |  | SI | UserText2 |
| PAPER_UserText3 | varchar |  |  | SI | UserText3 |
| PAPER_UserUpdate | bigint |  |  | SI | UserUpdate |
| PAPER_UsualRound_DR | bigint |  | FK | SI | Des Ref Resource |
| PAPER_WhoNotified | varchar |  |  | SI | Who Notified about death |
| PAPER_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP |
| PAPMI_Active | varchar |  |  | SI | Is This Patient Usable? |
| PAPMI_Alias | varchar |  |  | SI | Patient Alias |
| PAPMI_Allergy | varchar |  |  | SI | Allergy |
| PAPMI_Batallion | varchar |  |  | SI | Batallion |
| PAPMI_BlackList | varchar |  |  | SI | Black List Flag |
| PAPMI_CHCPatient | varchar |  |  | SI | CHC Patient |
| PAPMI_CardType_DR | bigint |  | FK | SI | Des Ref CardType |
| PAPMI_ConcessionCardExpDate | date |  |  | SI | Concession Card ExpDate |
| PAPMI_ConcessionCardNo | varchar |  |  | SI | ConcessionCardNo |
| PAPMI_DVAnumber | varchar |  |  | SI | DVA number |
| PAPMI_DentistClinic_DR | varchar |  | FK | SI | Des Ref DentistClinic |
| PAPMI_Dentist_DR | bigint |  | FK | SI | Des Ref Dentist |
| PAPMI_EPRDescription | varchar |  |  | SI | EPR Description |
| PAPMI_EstimatedDeathDate | varchar |  |  | SI | Estimated Death Date |
| PAPMI_ForeignPhoneNo | varchar |  |  | SI | Foreign Phone Number |
| PAPMI_GPOrgAddress | varchar |  |  | SI | GPOrgAddress |
| PAPMI_GPText | varchar |  |  | SI | GP Text |
| PAPMI_HealthCardExpiryDate | date |  |  | SI | HealthCardExpiryDate |
| PAPMI_HealthFundNo | varchar |  |  | SI | Health FundNo |
| PAPMI_HomeClinicNo | varchar |  |  | SI | Home Clinic number |
| PAPMI_IPNo | varchar |  |  | SI | Inpatient No |
| PAPMI_IndexMark | varchar |  |  | SI | Mark "*" in Index |
| PAPMI_LangPrintDR | varchar |  | FK | SI | Not Used Des Ref to CTPTI |
| PAPMI_LangSecondDR | bigint |  | FK | SI | Des Ref to CTLAN (Secondary Language) |
| PAPMI_LookupDisplay | varchar |  |  | SI | Lookup Display |
| PAPMI_Medicare | varchar |  |  | SI | Medicare No |
| PAPMI_MedicareCode | varchar |  |  | SI | Medicare Code |
| PAPMI_MedicareExpDate | date |  |  | SI | Medicare Expiry Date |
| PAPMI_MedicareString | varchar |  |  | SI | Medicare String |
| PAPMI_MedicareSuffix_DR | bigint |  | FK | SI | Des Ref MedicareSuffix_DR |
| PAPMI_Mother_DR | bigint |  | FK | SI | Des Ref to PA_Mother |
| PAPMI_No | varchar |  |  | SI | Patient No |
| PAPMI_NxtOPAdmNo | double |  |  | SI | Next OP Encounter No |
| PAPMI_OPNo | varchar |  |  | SI | Outpatient No |
| PAPMI_PAPER_DR | bigint |  | FK | SI | Des Ref to PAPER |
| PAPMI_PatCategory_DR | bigint |  | FK | SI | Des Ref to Pat. Categ |
| PAPMI_PensionType_DR | bigint |  | FK | SI | Des Ref PensionType |
| PAPMI_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| PAPMI_Refund | varchar |  |  | SI | Refund |
| PAPMI_Remark | varchar |  |  | SI | Patient Remark |
| PAPMI_RequireAssistanceMeal | varchar |  |  | SI | RequireAssistanceMeal |
| PAPMI_RequireAssistanceMenu | varchar |  |  | SI | RequireAssistanceMenu |
| PAPMI_SafetyNetCardExpDate | date |  |  | SI | Safety Net Card ExpDate |
| PAPMI_SafetyNetCardNo | varchar |  |  | SI | Safety Net Card No |
| PAPMI_Soundex | varchar |  |  | SI | Patient Soundex |
| PAPMI_SurName | varchar |  |  | SI | Computered Surname |
| PAPMI_TraceStatus_DR | bigint |  | FK | SI | Des Ref TraceOutcome |
| PAPMI_VIPFlag | varchar |  |  | SI | VIP Flag |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*