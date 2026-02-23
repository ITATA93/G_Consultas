# lab.EP_VisitNumber

**Schema:** lab
**Columnas:** 199
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPVIS_RowId | varchar | PK |  | NO | - |
| EPVIS_ALPHAUPBillName | varchar |  |  | SI | ALPHAUP BillName |
| EPVIS_ALPHAUPDoctorReference | varchar |  |  | SI | ALPHAUP DoctorReference |
| EPVIS_ALPHAUPExtra13 | varchar |  |  | SI | ALPHAUP Extra13 |
| EPVIS_ALPHAUPExtra14 | varchar |  |  | SI | ALPHAUP Extra14 |
| EPVIS_ALPHAUPExtra15 | varchar |  |  | SI | ALPHAUP Extra15 |
| EPVIS_ALPHAUPGivenName | varchar |  |  | SI | ALPHAUP GivenName |
| EPVIS_ALPHAUPName1 | varchar |  |  | SI | ALPHAUP Name_1 |
| EPVIS_ALPHAUPName2 | varchar |  |  | SI | ALPHAUP Name_2 |
| EPVIS_ALPHAUPName3 | varchar |  |  | SI | ALPHAUP Name_3 |
| EPVIS_ALPHAUPPatientAddress1 | varchar |  |  | SI | ALPHAUP PatientAddress1 |
| EPVIS_ALPHAUPPatientAddress5PostCode | varchar |  |  | SI | ALPHAUP PatientAddress5_PostCode |
| EPVIS_ALPHAUPSurname | varchar |  |  | SI | ALPHAUP Surname |
| EPVIS_ALPHAUPmicroAerobic | varchar |  |  | SI | ALPHAUP microAerobic |
| EPVIS_ALPHAUPmicroAnaerobic | varchar |  |  | SI | ALPHAUP microAnaerobic |
| EPVIS_ALPHAUPpcDVA | varchar |  |  | SI | ALPHAUP pc_DVA |
| EPVIS_ALPHAUPpcMedicare | varchar |  |  | SI | ALPHAUP pc_Medicare |
| EPVIS_ALPHAUPpcPensionerCard | varchar |  |  | SI | ALPHAUP pc_PensionerCard |
| EPVIS_AccountNumber_DR | varchar |  | FK | SI | Account Number DR |
| EPVIS_Age | double |  |  | SI | Age |
| EPVIS_Altitude_DR | varchar |  | FK | SI | Altitude DR |
| EPVIS_AnimalBreed_DR | varchar |  | FK | SI | Animal Breed DR |
| EPVIS_BBP_Acceptance | varchar |  |  | SI | Donor BBP Acceptance |
| EPVIS_BillAddress1 | varchar |  |  | SI | Bill Address1 |
| EPVIS_BillAddress2 | varchar |  |  | SI | Bill Address2 |
| EPVIS_BillAddress3_Suburb | varchar |  |  | SI | Bill Suburb |
| EPVIS_BillAddress4_State | varchar |  |  | SI | Bill State |
| EPVIS_BillAddress5_PostCode | varchar |  |  | SI | Bill Post Code |
| EPVIS_BillLocation_DR | varchar |  | FK | SI | Billing Location DR |
| EPVIS_BillName | varchar |  |  | SI | Bill Name |
| EPVIS_BloodGroup_DR | varchar |  | FK | SI | Blood Group DR |
| EPVIS_Case_QC | varchar |  |  | SI | QC Case |
| EPVIS_Case_Study | varchar |  |  | SI | Study Case |
| EPVIS_Category_DR | varchar |  | FK | SI | Category DR |
| EPVIS_CentreCode_DR | varchar |  | FK | SI | Des Ref CentreCode |
| EPVIS_ClinicalConditions_DR | varchar |  | FK | SI | Clinical Conditions DR |
| EPVIS_ClinicalHistory | varchar |  |  | SI | Clinical History |
| EPVIS_CollectedBy_DR | varchar |  | FK | SI | Collected By |
| EPVIS_Confidential | varchar |  |  | SI | Confidential |
| EPVIS_Contract_DR | varchar |  | FK | SI | Contract DR |
| EPVIS_DateOfAdmission | date |  |  | SI | Date Of Admission |
| EPVIS_DateOfBirth | date |  |  | SI | Date Of Birth |
| EPVIS_DateOfCollection | date |  |  | SI | Date Of Collection |
| EPVIS_DateOfCompletion_1 | date |  |  | SI | Date Of Completion 1 |
| EPVIS_DateOfCompletion_2 | date |  |  | SI | Date Of Completion 2 |
| EPVIS_DateOfDeath | date |  |  | SI | Date of Death |
| EPVIS_DateOfDelivery | date |  |  | SI | Expected Date of Delivery |
| EPVIS_DateOfDischarge | date |  |  | SI | Date Of Discharge |
| EPVIS_DateOfEntry | date |  |  | SI | Date Of Entry |
| EPVIS_DateOfInvoice | date |  |  | SI | Date Of Invoice |
| EPVIS_DateOfLMP | date |  |  | SI | Date of Last Menstrual Period |
| EPVIS_DateOfOperation | date |  |  | SI | Date Of Operation |
| EPVIS_DateOfPricing | date |  |  | SI | Date Of Pricing |
| EPVIS_DateOfReceiving | date |  |  | SI | Date Of Receiving |
| EPVIS_DateOfRequest | date |  |  | SI | Date Of Request |
| EPVIS_DayOfCycle | double |  |  | SI | Day of cycle |
| EPVIS_Dead | varchar |  |  | SI | Dead |
| EPVIS_DebtorNumber_DR | varchar |  | FK | SI | Des Ref DebtorNumber |
| EPVIS_Discount | double |  |  | SI | Discount |
| EPVIS_DoctorCode_DR | varchar |  | FK | SI | Des Ref DoctorCode |
| EPVIS_DoctorReference | varchar |  |  | SI | Doctor Reference |
| EPVIS_DonorID | varchar |  |  | SI | Donor ID |
| EPVIS_Donor_BBP_DR | varchar |  | FK | SI | Donor Blood Bank Pack DR |
| EPVIS_Donor_Questionare_DR | varchar |  | FK | SI | Donor Questionare DR |
| EPVIS_EDIOrderNumber | varchar |  |  | SI | EDI Order Number |
| EPVIS_EPVStatus | varchar |  |  | SI | EPV status |
| EPVIS_EPVTransactionID | varchar |  |  | SI | EPV TransactionID |
| EPVIS_EXMEnabled | varchar |  |  | SI | EXM Enabled |
| EPVIS_Ethnicity_DR | varchar |  | FK | SI | Des Ref Ethnicity |
| EPVIS_ExcludeFromPatientMean | varchar |  |  | SI | Exclude From Patient Mean |
| EPVIS_Extra1 | varchar |  |  | SI | Extra field 1 |
| EPVIS_Extra10 | varchar |  |  | SI | Extra field 10 |
| EPVIS_Extra11 | varchar |  |  | SI | Extra field 11 |
| EPVIS_Extra12 | varchar |  |  | SI | Extra field 12 |
| EPVIS_Extra13 | varchar |  |  | SI | Extra field 13 |
| EPVIS_Extra14 | varchar |  |  | SI | Extra field 14 |
| EPVIS_Extra15 | varchar |  |  | SI | Extra field 15 |
| EPVIS_Extra2 | varchar |  |  | SI | Extra field 2 |
| EPVIS_Extra3 | varchar |  |  | SI | Extra field 3 |
| EPVIS_Extra4 | varchar |  |  | SI | Extra field 4 |
| EPVIS_Extra5 | varchar |  |  | SI | Extra field 5 |
| EPVIS_Extra6 | varchar |  |  | SI | Extra field 6 |
| EPVIS_Extra7 | varchar |  |  | SI | Extra field 7 |
| EPVIS_Extra8 | varchar |  |  | SI | Extra field 8 |
| EPVIS_Extra9 | varchar |  |  | SI | Extra field 9 |
| EPVIS_Fasting | varchar |  |  | SI | Fasting |
| EPVIS_FinancialClass_DR | varchar |  | FK | SI | Financial Class DR |
| EPVIS_FutureEpisode | varchar |  |  | SI | Future Episode |
| EPVIS_FutureMRN | varchar |  |  | SI | Future MRN |
| EPVIS_GivenName | varchar |  |  | SI | Given Name |
| EPVIS_HoldDate | date |  |  | SI | BB Hold Date |
| EPVIS_HoldTime | time |  |  | SI | BB Hold Time |
| EPVIS_HoldUnits | numeric |  |  | SI | BB Hold Units |
| EPVIS_HospitalBed | varchar |  |  | SI | Hospital Bed |
| EPVIS_HospitalCodeOriginal_DR | varchar |  | FK | SI | Patient Location Original |
| EPVIS_HospitalCode_DR | varchar |  | FK | SI | Patient Location Current |
| EPVIS_HospitalEpisode | varchar |  |  | SI | Hospital Episode |
| EPVIS_HospitalRoom | varchar |  |  | SI | Hospital Room |
| EPVIS_HospitalUR | varchar |  |  | SI | Hospital UR |
| EPVIS_Hospital_EpisodeUR_Number | varchar |  |  | SI | Hospital Episode/UR Number |
| EPVIS_ICD10List | varchar |  |  | SI | ICD10 list |
| EPVIS_InitiationCode_DR | varchar |  | FK | SI | Des Ref Initiation Code |
| EPVIS_InitiationItem_DR | varchar |  | FK | SI | Des Ref Initiation Item |
| EPVIS_InvoiceBatch_DR | varchar |  | FK | SI | Invoice Batch |
| EPVIS_Language_DR | bigint |  | FK | SI | Language DR |
| EPVIS_MTOEOrdItemDR | varchar |  | FK | SI | - |
| EPVIS_ManualEntry | varchar |  |  | SI | Manual Entry |
| EPVIS_MortuaryCase | varchar |  |  | SI | Mortuary Case |
| EPVIS_Name_1 | varchar |  |  | SI | Extra Name 1 |
| EPVIS_Name_2 | varchar |  |  | SI | Extra Name 2 |
| EPVIS_Name_3 | varchar |  |  | SI | Extra Name 3 |
| EPVIS_NationalID | varchar |  |  | SI | NationalID |
| EPVIS_NationalIDType_DR | varchar |  | FK | SI | National ID Type DR |
| EPVIS_OutbreakCode_DR | varchar |  | FK | SI | Outbreak Code DR |
| EPVIS_PatientAddress1 | varchar |  |  | SI | Patient Address1 |
| EPVIS_PatientAddress2 | varchar |  |  | SI | Patient Address2 |
| EPVIS_PatientAddress3_Suburb | varchar |  |  | SI | Patient Suburb |
| EPVIS_PatientAddress4_State | varchar |  |  | SI | Patient State |
| EPVIS_PatientAddress5_PostCode | varchar |  |  | SI | Patient Post Code |
| EPVIS_PatientType | varchar |  |  | SI | Patient Type |
| EPVIS_PayCodeReference | varchar |  |  | SI | Pay Code Reference |
| EPVIS_PaymentCode_DR | varchar |  | FK | SI | Des Ref Payment Code |
| EPVIS_PhoneHome | varchar |  |  | SI | Home Phone |
| EPVIS_PhoneWork | varchar |  |  | SI | Work Phone |
| EPVIS_PregnancyEvent_DR | varchar |  | FK | SI | Pregnancy Event |
| EPVIS_PregnancyEvent_Unlinked | varchar |  |  | SI | Pregnancy Event unlinked  |
| EPVIS_Pregnant | varchar |  |  | SI | Pregnant |
| EPVIS_PregnantNumberOfWeeks | double |  |  | SI | Number Of Weeks Pregnant |
| EPVIS_PrevisouMRN | varchar |  |  | SI | Previous MRN |
| EPVIS_PricingEpisodeMaster | varchar |  |  | SI | Master Episode for Pricing |
| EPVIS_PricingEpisodes | varchar |  |  | SI | List of Episodes included with the Master |
| EPVIS_PriorityCode_DR | varchar |  | FK | SI | Des Ref Priority Code |
| EPVIS_PromptBilling | varchar |  |  | SI | Prompt Billing |
| EPVIS_ReceiptNumber | varchar |  |  | SI | Receipt Number |
| EPVIS_Reminder | varchar |  |  | SI | Reminder type |
| EPVIS_RequestType_DR | varchar |  | FK | SI | Request Type DR |
| EPVIS_SoundexExtraName1 | varchar |  |  | SI | Soundex Extra Name 1 |
| EPVIS_SoundexExtraName2 | varchar |  |  | SI | Soundex Extra Name 2 |
| EPVIS_SoundexExtraName3 | varchar |  |  | SI | Soundex Extra Name 3 |
| EPVIS_SoundexName | varchar |  |  | SI | Soundex Name |
| EPVIS_SoundexSurname | varchar |  |  | SI | Soundex Surname |
| EPVIS_SourceOfDeath | varchar |  |  | SI | Source of Death |
| EPVIS_SpecialInterest_DR | varchar |  | FK | SI | Special Interest |
| EPVIS_Specialty_DR | varchar |  | FK | SI | Specialty DR |
| EPVIS_Species_DR | varchar |  | FK | SI | Des Ref Species |
| EPVIS_StaffNotes | varchar |  |  | SI | Staff Notes |
| EPVIS_StatusPatient | varchar |  |  | NO | Patient Status |
| EPVIS_StatusPrinting | varchar |  |  | SI | Printing Status |
| EPVIS_Surname | varchar |  |  | SI | Surname |
| EPVIS_TestSets | varchar |  |  | SI | List of Test Sets |
| EPVIS_TimeOfAdmission | varchar |  |  | SI | Time Of Admission |
| EPVIS_TimeOfCollection | varchar |  |  | SI | Time Of Collection |
| EPVIS_TimeOfEntry | varchar |  |  | SI | Time Of Entry |
| EPVIS_TimeOfReceiving | varchar |  |  | SI | Time Of Receiving |
| EPVIS_TimeOfRequest | varchar |  |  | SI | Time Of Request |
| EPVIS_Title_DR | varchar |  | FK | SI | Des Ref Title |
| EPVIS_UrgentComment | varchar |  |  | SI | Urgent Comment |
| EPVIS_UserID_DR | varchar |  | FK | SI | User ID |
| EPVIS_UserSite_DR | varchar |  | FK | SI | User Site |
| EPVIS_VisitAction_DR | varchar |  | FK | SI | Des Ref VisitAction |
| EPVIS_VisitComments | varchar |  |  | SI | Visit Comments |
| EPVIS_VisitNumber | varchar |  |  | NO | Visit Number |
| EPVIS_microAerobic | varchar |  |  | SI | micro Aerobic bottle |
| EPVIS_microAnaerobic | varchar |  |  | SI | micro Anaerobic bottle |
| EPVIS_pc_DVA | varchar |  |  | SI | Department of VA |
| EPVIS_pc_FundDependant | varchar |  |  | SI | Health Fund Dependant Counter |
| EPVIS_pc_FundNumber | varchar |  |  | SI | Health Fund Number |
| EPVIS_pc_HealthFund_DR | varchar |  | FK | SI | Health Fund DR |
| EPVIS_pc_Medicare | varchar |  |  | SI | Medicare |
| EPVIS_pc_MedicareRef | varchar |  |  | SI | Medicare Ref |
| EPVIS_pc_PensionerCard | varchar |  |  | SI | Pensioner Card |
| EPVIS_pc_extra_01 | varchar |  |  | SI | EPVIS_pc_extra_01 |
| EPVIS_pc_extra_02 | varchar |  |  | SI | EPVIS_pc_extra_02 |
| EPVIS_pc_extra_03 | varchar |  |  | SI | EPVIS_pc_extra_03 |
| EPVIS_pc_extra_04 | varchar |  |  | SI | EPVIS_pc_extra_04 |
| EPVIS_pc_extra_05 | varchar |  |  | SI | EPVIS_pc_extra_05 |
| EPVIS_pc_extra_06 | varchar |  |  | SI | EPVIS_pc_extra_06 |
| EPVIS_pc_extra_07 | varchar |  |  | SI | EPVIS_pc_extra_07 |
| EPVIS_pc_extra_08 | varchar |  |  | SI | EPVIS_pc_extra_08 |
| EPVIS_pc_extra_09 | varchar |  |  | SI | EPVIS_pc_extra_09 |
| EPVIS_pc_extra_10 | varchar |  |  | SI | EPVIS_pc_extra_10 |
| EPVIS_pc_extra_11 | varchar |  |  | SI | EPVIS_pc_extra_11 |
| EPVIS_pc_extra_12 | varchar |  |  | SI | EPVIS_pc_extra_12 |
| EPVIS_pc_extra_13 | varchar |  |  | SI | EPVIS_pc_extra_13 |
| EPVIS_pc_extra_14 | varchar |  |  | SI | EPVIS_pc_extra_14 |
| EPVIS_pc_extra_15 | varchar |  |  | SI | EPVIS_pc_extra_15 |
| EPVIS_pc_extra_16 | varchar |  |  | SI | EPVIS_pc_extra_16 |
| EPVIS_pc_extra_17 | varchar |  |  | SI | EPVIS_pc_extra_17 |
| EPVIS_pc_extra_18 | varchar |  |  | SI | EPVIS_pc_extra_18 |
| EPVIS_pc_extra_19 | varchar |  |  | SI | EPVIS_pc_extra_19 |
| EPVIS_pc_extra_20 | varchar |  |  | SI | EPVIS_pc_extra_20 |
| EPVIS_pc_extra_21 | varchar |  |  | SI | EPVIS_pc_extra_21 |
| EPVIS_pc_extra_22 | varchar |  |  | SI | EPVIS_pc_extra_22 |
| EPVIS_pc_extra_23 | varchar |  |  | SI | EPVIS_pc_extra_23 |
| EPVIS_pc_extra_24 | varchar |  |  | SI | EPVIS_pc_extra_24 |
| EPVIS_pc_extra_25 | varchar |  |  | SI | EPVIS_pc_extra_25 |
| EPVIS_pc_extra_26 | varchar |  |  | SI | EPVIS_pc_extra_26 |
| EPVIS_pc_extra_27 | varchar |  |  | SI | EPVIS_pc_extra_27 |
| EPVIS_pc_extra_28 | varchar |  |  | SI | EPVIS_pc_extra_28 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*