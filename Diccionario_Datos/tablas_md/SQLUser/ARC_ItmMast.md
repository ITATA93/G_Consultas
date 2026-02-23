# SQLUser.ARC_ItmMast

**Schema:** SQLUser
**Columnas:** 302
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Catalogo de **Items/Prestaciones** (Archetype Item Master).

Maestro de prestaciones del hospital:
- Examenes de laboratorio
- Procedimientos
- Imagenes
- Insumos y medicamentos

**Campos clave:**
- ARCIM_Code: Codigo de prestacion
- ARCIM_Desc: Descripcion
- ARCIM_Type: Tipo de item
- ARCIM_Category_DR: Categoria

**Uso:**
- Base para ordenes medicas
- Facturacion de prestaciones
- Estadisticas de produccion

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCIM_RowId | varchar | PK |  | NO | - |
| ARCIM_Abbrev | varchar |  |  | NO | Description |
| ARCIM_AddToDiagnosticStage | varchar |  |  | SI | Add to Diagnostic Stage |
| ARCIM_AdjustedProcedureTime | double |  |  | SI | AdjustedProcedureTime |
| ARCIM_AdminQuestionn_DR | bigint |  | FK | SI | ARCIM Administration Questionnarie Des Ref |
| ARCIM_AdminRoute_DR | bigint |  | FK | SI | Des Ref PHCAdministrationRoute  |
| ARCIM_AdmixtureRecipe_DR | bigint |  | FK | SI | Des Ref Admixture Recipe |
| ARCIM_AllowOrderWOStockCheck | varchar |  |  | SI | Allow to Order Without Stock Check |
| ARCIM_AnaestMethod_DR | bigint |  | FK | SI | Des Ref ORCAnaestMethod |
| ARCIM_AnaestProcBilling | varchar |  |  | SI | Anaesthetic Procedure Billing |
| ARCIM_AnaestProcedure | varchar |  |  | SI | Anaesthetic Procedure |
| ARCIM_Anaesthetic | varchar |  |  | SI | Anaesthetic Order Item |
| ARCIM_AuthorisingClinician | varchar |  |  | SI | Authorising Clinician |
| ARCIM_AutoOrder | varchar |  |  | SI | Order Automatically from a Clinical Pathway |
| ARCIM_BedReasonNotAvail_DR | bigint |  | FK | SI | Des Ref PACBedReasonNotAvail |
| ARCIM_BillBodyP_DR | bigint |  | FK | SI | Des Ref Billing Body Parts |
| ARCIM_BillByTariffPrices | varchar |  |  | SI | Bill by Tariff Prices |
| ARCIM_BillDescription | varchar |  |  | SI | Bill Description |
| ARCIM_BillOnAdmnstrEmerg | varchar |  |  | SI | BillOnAdmnstrEmerg |
| ARCIM_BillOnAdmnstrInpat | varchar |  |  | SI | BillOnAdmnstrInpat |
| ARCIM_BillOnAdmnstrOutpat | varchar |  |  | SI | BillOnAdmnstrOutpat |
| ARCIM_BillPartialPackEM | varchar |  |  | SI | Bill on Partial Packing Emergency |
| ARCIM_BillPartialPackIP | varchar |  |  | SI | Bill on Partial Packing Inpatients |
| ARCIM_BillPartialPackOP | varchar |  |  | SI | Bill on Partial Packing Outpatients |
| ARCIM_BillSub_DR | varchar |  | FK | NO | Des Ref to ARCSG |
| ARCIM_BillingLogic | varchar |  |  | SI | Billing Logic defined against each order item for ... |
| ARCIM_BillingUOM_DR | bigint |  | FK | SI | Des Ref UOM |
| ARCIM_CAPD | varchar |  |  | SI | CAPD Flag |
| ARCIM_CarbohydratesG | varchar |  |  | SI | CarbohydratesG |
| ARCIM_ChargePartial | varchar |  |  | SI | Charge Partial |
| ARCIM_ChgCost | double |  |  | SI | Unit Cost |
| ARCIM_ChgDispFlg | varchar |  |  | SI | Price Control Flag |
| ARCIM_ChgMaxAmt | double |  |  | SI | Maximum Amount |
| ARCIM_ChgMinAmt | double |  |  | SI | Minimum Amount |
| ARCIM_ChgOrderPerHour | varchar |  |  | SI | Charge Order per hour |
| ARCIM_ChgPostFlg | varchar |  |  | SI | Charge Posting Flag |
| ARCIM_ChgUnitFact | double |  |  | SI | Charge Unit Factor |
| ARCIM_ClinicalConditions | varchar |  |  | SI | Clinical Condition |
| ARCIM_Code | varchar |  |  | NO | Charge Code |
| ARCIM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCIM_CodeTranslated | varchar |  |  | SI | - |
| ARCIM_Commissioning | varchar |  |  | SI | Commissioning Order Item |
| ARCIM_CompService_DR | varchar |  | FK | SI | Complementary Service |
| ARCIM_ConsultDept | bigint |  |  | SI | Default Consultation Department |
| ARCIM_CreateInpatientEpisode | bit |  |  | SI | Create an Inpatient Episode when Booking An Appoin... |
| ARCIM_CreatedDate | date |  |  | SI | Created Date |
| ARCIM_CreatedTime | time |  |  | SI | Created Time |
| ARCIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCIM_CurVerFlg | varchar |  |  | SI | Current Version Flag |
| ARCIM_CurVers_DR | varchar |  | FK | SI | Current Version |
| ARCIM_DMDForm_DR | bigint |  | FK | SI | Des Ref PHCForm |
| ARCIM_DMDGeneric_DR | bigint |  | FK | SI | Des Ref PHCGeneric |
| ARCIM_DMDLevel | varchar |  |  | SI | DMDLevel |
| ARCIM_DMDStrength_DR | bigint |  | FK | SI | Des Ref PHCStrength |
| ARCIM_DMDVolumeML | double |  |  | SI | ARCIMDMDVolumeML  |
| ARCIM_DayBand1 | varchar |  |  | SI | Day Band 1 |
| ARCIM_Days | double |  |  | SI | Days |
| ARCIM_DaysCheckDuplicate | double |  |  | SI | Number of Days to CheckDuplicate |
| ARCIM_DeceasedPatientsOnly | varchar |  |  | SI | Deceased Patients Only |
| ARCIM_DeductibleItem | varchar |  |  | SI | Deductible Item |
| ARCIM_DefPriority_DR | bigint |  | FK | SI | Des Ref DefPriority |
| ARCIM_DefaultToTeleConsult | varchar |  |  | SI | DefaultToTeleConsult |
| ARCIM_DentalState_DR | bigint |  | FK | SI | Des Ref DentalState |
| ARCIM_DerFeeRules_DR | bigint |  | FK | SI | DerFeeRules |
| ARCIM_DerivedFeeItem | varchar |  |  | SI | Derived Fee Item |
| ARCIM_Desc | varchar |  |  | NO | Description |
| ARCIM_DescTranslated | varchar |  |  | SI | - |
| ARCIM_DiagnosticWaitTime | double |  |  | SI | DiagnosticWaitTime |
| ARCIM_DietryFibreG | varchar |  |  | SI | DietryFibreG |
| ARCIM_DirectlyExecute | varchar |  |  | SI | Directly Execute from a Clinical Pathway |
| ARCIM_DisableYesNo1 | varchar |  |  | SI | Disable Yes/No 1 |
| ARCIM_DisableYesNo2 | varchar |  |  | SI | Disable Yes/No 2 |
| ARCIM_DisableYesNo3 | varchar |  |  | SI | Disable Yes/No 3 |
| ARCIM_DisableYesNo4 | varchar |  |  | SI | Disable Yes/No 4 |
| ARCIM_DischPriorityBUP_DR | bigint |  | FK | SI | Des Ref DischPriority Billing Upon Packing |
| ARCIM_DisplayCumulative | varchar |  |  | SI | Display Cumulative |
| ARCIM_DoseCalcFormula | varchar |  |  | SI | Dose Calc Formula |
| ARCIM_DoseType | varchar |  |  | SI | Dose Type |
| ARCIM_DressTime | double |  |  | SI | Service Dress Time |
| ARCIM_DrgFormPack_DR | varchar |  | FK | SI | Des Ref PHCDrgFormPack |
| ARCIM_DrgMast_DR | bigint |  | FK | SI | Des Ref PHCDrgMast |
| ARCIM_ERefCompatibility | varchar |  |  | SI | E-Referral Compatibility |
| ARCIM_ERefIncludedCodes | varchar |  |  | SI | E-Referral Included Codes |
| ARCIM_ERefItemsCycle | double |  |  | SI | E-Referral Items on a Cycle  |
| ARCIM_ERefItemsCycleMin | double |  |  | SI | E-Referral items on a cycle minimum |
| ARCIM_ERefNonCompatItems | varchar |  |  | SI | E-Referral Non-compatibile Items |
| ARCIM_ERefNumericField1 | integer |  |  | SI | E-Referral Numeric Field 1 |
| ARCIM_ERefNumericField2 | integer |  |  | SI | E-Referral Numeric Field 2 |
| ARCIM_ERefNumericField3 | integer |  |  | SI | E-Referral Numeric Field 3 |
| ARCIM_ERefPrescWeighFactor | varchar |  |  | SI | E-Referral Prescription Weighting Factor |
| ARCIM_ERefTextField1 | varchar |  |  | SI | E-Referral Text Field 1 |
| ARCIM_ERefTextField2 | varchar |  |  | SI | E-Referral Text Field 2 |
| ARCIM_ERefTextField3 | varchar |  |  | SI | E-Referral Text Field 3 |
| ARCIM_ERefTextField4 | varchar |  |  | SI | E-Referral Text Field 4 |
| ARCIM_ERefTextField5 | varchar |  |  | SI | E-Referral Text Field 5 |
| ARCIM_ERefUniquePresc | varchar |  |  | SI | E-Referral Unique Prescription |
| ARCIM_EffDate | date |  |  | SI | Effective Date |
| ARCIM_EffDateTime | varchar |  |  | SI | Effective Date / Time |
| ARCIM_EffDateTo | date |  |  | SI | Effective Date To |
| ARCIM_EffTime | time |  |  | SI | Effective Time |
| ARCIM_EmergBillingLogic | varchar |  |  | SI | Billing Logic defined against each order item for ... |
| ARCIM_EnergyCal | varchar |  |  | SI | EnergyCal |
| ARCIM_EnergyKj | varchar |  |  | SI | EnergyKj |
| ARCIM_EpisodeType | varchar |  |  | SI | Episode Type |
| ARCIM_EpisodicBilling | varchar |  |  | SI | Episodic Billing |
| ARCIM_ExcludeFromGrpWarn | varchar |  |  | SI | Exclude From Grp Warn |
| ARCIM_ExpAnaestTime | double |  |  | SI | Expected Anaesthetic Time |
| ARCIM_ExpLOS | double |  |  | SI | Exp LOS |
| ARCIM_ExpiryDays | double |  |  | SI | ExpiryDays |
| ARCIM_ExternalLoanDays | double |  |  | SI | External Loan Default Days |
| ARCIM_ExternalServiceID | varchar |  |  | SI | ExternalServiceID |
| ARCIM_FileNotes | varchar |  |  | SI | File Name for patient Notes |
| ARCIM_Formulary | varchar |  |  | SI | Formulary  |
| ARCIM_GLPostToOrderDept | varchar |  |  | SI | Revenue Posting To Ordering Department |
| ARCIM_GenericDesc | varchar |  |  | SI | Generic Description |
| ARCIM_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| ARCIM_HL7ResultType | varchar |  |  | SI | HL7ResultType |
| ARCIM_Haemodal | varchar |  |  | SI | Haemodalisys Flag |
| ARCIM_IncSource_DR | bigint |  | FK | SI | Des REf to IncSource |
| ARCIM_InsCoDesc | varchar |  |  | SI | Insurance Company Description |
| ARCIM_InsSubCat_DR | varchar |  | FK | SI | Des Ref to ARC_InsSubCat |
| ARCIM_InternalLoanDays | double |  |  | SI | Internal Loan Default Days |
| ARCIM_IsDrugDBAPI | varchar |  |  | SI | Is Drug Database API |
| ARCIM_ItemCat_DR | bigint |  | FK | SI | Des Ref to ARCIC |
| ARCIM_KidneyTransp | varchar |  |  | SI | Kidney Transplant Flag |
| ARCIM_LateralityReq | varchar |  |  | SI | Laterality Required - Radiology  |
| ARCIM_LetterType_DR | bigint |  | FK | SI | Letter Type |
| ARCIM_LoanItem | varchar |  |  | SI | Loan Item Flag |
| ARCIM_Manufactured | varchar |  |  | SI | Manufactured |
| ARCIM_MaxAmt | double |  |  | SI | Maximum Amount |
| ARCIM_MaxCumDose | double |  |  | SI | MaxCumDose |
| ARCIM_MaxPrice | double |  |  | SI | Maximum Price |
| ARCIM_MaxQty | double |  |  | SI | MaxQty |
| ARCIM_MaxQtyPerDay | double |  |  | SI | MaxQtyPerDay |
| ARCIM_MaxWeeksAfterOnset | double |  |  | SI | Max Weeks After Onset Date  |
| ARCIM_MealType_DR | bigint |  | FK | SI | Des Ref MealType |
| ARCIM_MinAmt | double |  |  | SI | Minimum Amount |
| ARCIM_MinPrice | double |  |  | SI | Minimum Price |
| ARCIM_MinTime | varchar |  |  | SI | MinTime |
| ARCIM_MinWeeksAfterOnset | double |  |  | SI | Min Weeks After Onset Date |
| ARCIM_Minutes | varchar |  |  | SI | Minutes |
| ARCIM_ModifiersRequired | varchar |  |  | SI | Modifiers Required Flag |
| ARCIM_NoCharge | varchar |  |  | SI | No Charge |
| ARCIM_NoOfCumDays | double |  |  | SI | NoOfCumDays |
| ARCIM_NoTheatreReq | varchar |  |  | SI | No Theatre Required |
| ARCIM_NonMBS | varchar |  |  | SI | Non MBS (Medicare Benefits Schedule) Item |
| ARCIM_NonReviewable | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ARCIM_OEMessage | varchar |  |  | SI | Order Entry Message |
| ARCIM_ObservationGroup_DR | bigint |  | FK | SI | Observation Group DR |
| ARCIM_Ointment | double |  |  | SI | Ointment |
| ARCIM_OrdMonitorObsGroup_DR | bigint |  | FK | SI | Order Monitoring Observation Group |
| ARCIM_OrderOnItsOwn | varchar |  |  | SI | Order On Its Own |
| ARCIM_OtherG | varchar |  |  | SI | OtherG |
| ARCIM_OutPBillingLogic | varchar |  |  | SI | Billing Logic defined against each order item for ... |
| ARCIM_Owner | varchar |  |  | SI | Owner |
| ARCIM_P1ChgFact | double |  |  | SI | Period 1 Charge Factor |
| ARCIM_P1StdAddAmt | double |  |  | SI | Period 1 Standard Additional Amount |
| ARCIM_P1TypAAddAmt | double |  |  | SI | Period 1 Type A Additional Amount |
| ARCIM_P1TypBAddAmt | double |  |  | SI | Period 1 Type B Additional Amount |
| ARCIM_P2ChgFact | double |  |  | SI | Period 2 Charge Factor |
| ARCIM_P2StdAddAmt | double |  |  | SI | Period 2 Standard Additional Amount |
| ARCIM_P2TypAAddAmt | double |  |  | SI | Period 2 Type A Additional Amount |
| ARCIM_P2TypBAddAmt | double |  |  | SI | Period 2 Type B Additional Amount |
| ARCIM_P3ChgFact | double |  |  | SI | Period 3 Charge Factor |
| ARCIM_P3StdAddAmt | double |  |  | SI | Period 3 Standard Additional Amount |
| ARCIM_P3TypAAddAmt | double |  |  | SI | Period 3 Type A Additional Amount |
| ARCIM_P3TypBAddAmt | double |  |  | SI | Period 3 Type B Additional Amount |
| ARCIM_P4ChgFact | double |  |  | SI | Period 4 Charge Factor |
| ARCIM_P4StdAddAmt | double |  |  | SI | Period 4 Standard Additional Amount |
| ARCIM_P4TypAAddAmt | double |  |  | SI | Period 4 Type A Additional Amount |
| ARCIM_P4TypBAddAmt | double |  |  | SI | Period 4 Type B Additional Amount |
| ARCIM_PHCDF_DR | varchar |  | FK | SI | Des Ref to PHCDF |
| ARCIM_PHCPA_DR | bigint |  | FK | SI | Des Ref to PHCPA (Packing) |
| ARCIM_PatientOrderFile1 | varchar |  |  | SI | Patient OrderFile1 |
| ARCIM_PatientOrderFile2 | varchar |  |  | SI | Patient Order File 2 |
| ARCIM_PatientOrderFile3 | varchar |  |  | SI | Patient Order File 3 |
| ARCIM_PayorICDGroup_DR | bigint |  | FK | SI | Des Ref PayorICDGroup |
| ARCIM_PhoneOrderReviewTime | double |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ARCIM_PreRecoveryTimeMin | double |  |  | SI | PreRecoveryTimeMin |
| ARCIM_PreRecoveryTimeType | varchar |  |  | SI | PreRecoveryTimeType |
| ARCIM_PriceCostOnOrdering | varchar |  |  | SI | Price and Cost On Ordering |
| ARCIM_Procedure | varchar |  |  | SI | Procedure Order Item |
| ARCIM_ProcessingNotes | varchar |  |  | SI | Processing Notes |
| ARCIM_ProfileFlg | varchar |  |  | SI | Profile Flag |
| ARCIM_ProteinG | varchar |  |  | SI | ProteinG |
| ARCIM_QuesMandatory | varchar |  |  | SI | Question Mandatory |
| ARCIM_Questionnaire_DR | bigint |  | FK | SI | Des REf Questionnaire |
| ARCIM_RBNotes | varchar |  |  | SI | RB Notes |
| ARCIM_RMDuration_DR | bigint |  | FK | SI | Des Ref RMDuration |
| ARCIM_RMFrequency_DR | bigint |  | FK | SI | Des Ref RMFrequency |
| ARCIM_RangeFrom | varchar |  |  | SI | Range From |
| ARCIM_RangeTo | varchar |  |  | SI | Range To |
| ARCIM_RebateCode | varchar |  |  | SI | Rebate Code |
| ARCIM_RefEligibilityRule_DR | bigint |  | FK | SI | E-Referral Eligibility Rules |
| ARCIM_ReferralAccessType_DR | bigint |  | FK | SI | Default Referral Access Type |
| ARCIM_RemoteDutyType | varchar |  |  | SI | Remote Duty Order Type |
| ARCIM_ReorderOnItsOwn | varchar |  |  | SI | Reorder On Its Own |
| ARCIM_ReqApproval | varchar |  |  | SI | Requires Approval |
| ARCIM_RestrictEM | varchar |  |  | SI | Restrict to EM episode |
| ARCIM_RestrictHP | varchar |  |  | SI | Restrict HP episode |
| ARCIM_RestrictIP | varchar |  |  | SI | Restrict IP episode |
| ARCIM_RestrictOP | varchar |  |  | SI | Restrict OP episode |
| ARCIM_ResultCategories | varchar |  |  | SI | Result Categories |
| ARCIM_ResultDisplayGroupDR | bigint |  | FK | SI | Result Display Group DR |
| ARCIM_ResultGroup | varchar |  |  | SI | Result Group |
| ARCIM_ReviewRequired | varchar |  |  | SI | ReviewRequired |
| ARCIM_RiceType_DR | bigint |  | FK | SI | Des Ref RiceTyp |
| ARCIM_RoomType_DR | bigint |  | FK | SI | - |
| ARCIM_Row_Calc | varchar |  |  | SI | Row_Calc |
| ARCIM_RvpAnes | double |  |  | SI | RVP Anesthesia Unit Value |
| ARCIM_RvpFud | double |  |  | SI | RVP Follow-up Days |
| ARCIM_RvpInterimYear | double |  |  | SI | RVP Date Stamped Value |
| ARCIM_RvpUnitStat | varchar |  |  | SI | RVP Unit Status |
| ARCIM_RvpUpd | varchar |  |  | SI | RVP Update |
| ARCIM_SameDay | varchar |  |  | SI | Same Day |
| ARCIM_SaturatedFatsG | varchar |  |  | SI | SaturatedFatsG |
| ARCIM_Sensitive | varchar |  |  | SI | Sensitive |
| ARCIM_SensitiveOrder | varchar |  |  | SI | Sensitive Order |
| ARCIM_SequenceOrder | varchar |  |  | SI | SequenceOrder |
| ARCIM_ServCat_DR | bigint |  | FK | SI | Des Ref to ARCSC |
| ARCIM_ServMaterial | varchar |  |  | SI | Service/Material |
| ARCIM_ServTax_DR | bigint |  | FK | SI | Des Ref to ARCST |
| ARCIM_ServiceCharge_DR | bigint |  | FK | SI | Des Ref ServiceCharge |
| ARCIM_ServiceGroup_DR | bigint |  | FK | SI | Des Ref Service Group |
| ARCIM_ServicePriority_DR | bigint |  | FK | SI | Des Ref ServicePriority |
| ARCIM_ShortDesc | varchar |  |  | SI | ShortDesc |
| ARCIM_SingleFee | varchar |  |  | SI | Single Fee |
| ARCIM_SnackFlag | varchar |  |  | SI | Snack Flag |
| ARCIM_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| ARCIM_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| ARCIM_SodiumMg | varchar |  |  | SI | SodiumMg |
| ARCIM_StdAmt | double |  |  | SI | Standard Amount |
| ARCIM_SubMasFlg | varchar |  |  | SI | Ancillary Master Flag |
| ARCIM_Subscript | numeric |  |  | NO | ARCIM Subscript |
| ARCIM_SugarsG | varchar |  |  | SI | SugarsG |
| ARCIM_Surcharge_DR | bigint |  | FK | SI | Des Ref to ARC_Surcharge |
| ARCIM_TestItemSequnce | varchar |  |  | SI | Test Item Sequence |
| ARCIM_Text1 | varchar |  |  | SI | Text1 |
| ARCIM_Text2 | varchar |  |  | SI | Text2 |
| ARCIM_Text3 | varchar |  |  | SI | Text3 |
| ARCIM_Text4 | varchar |  |  | SI | Text4 |
| ARCIM_Text5 | varchar |  |  | SI | Text5 |
| ARCIM_TimeDepFlg | varchar |  |  | SI | Time Dependent Flag |
| ARCIM_TotalFatG | varchar |  |  | SI | TotalFatG |
| ARCIM_Type1 | varchar |  |  | SI | Type1 |
| ARCIM_Type2 | varchar |  |  | SI | Type2 |
| ARCIM_TypeAAmt | double |  |  | SI | Type A Amount |
| ARCIM_TypeBAmt | double |  |  | SI | Type B Amount |
| ARCIM_Type_Calc | varchar |  |  | SI | ARCIM_Type_Calc |
| ARCIM_UOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| ARCIM_UpdateDate | date |  |  | SI | Update Date |
| ARCIM_UpdateTime | time |  |  | SI | Update Time |
| ARCIM_UpdateUser | bigint |  |  | SI | Update User |
| ARCIM_UpdatedDate | date |  |  | SI | Updated Date |
| ARCIM_UpdatedTime | time |  |  | SI | Updated Time |
| ARCIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ARCIM_UseODBCforWord | varchar |  |  | SI | Use ODBC for Word |
| ARCIM_UserDefWindow_DR | bigint |  | FK | SI | Des Ref UserDefWindow |
| ARCIM_Version | double |  |  | NO | Version |
| ARCIM_VisibleInOrderList | varchar |  |  | SI | Visible In Order List |
| ARCIM_WordTemplate | varchar |  |  | SI | Word Template |
| Q01 | - |  |  | SI | Clasificación de Robson |
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