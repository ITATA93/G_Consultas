# SQLUser.OE_OrdItem

**Schema:** SQLUser
**Columnas:** 368
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Detalle de **Items de Ordenes**.

Cada item dentro de una orden medica:
- Examen especifico solicitado
- Cantidad y frecuencia
- Prioridad (rutina, urgente)

**Campos clave:**
- OEORI_OEORD_ParRef: FK a OE_Order
- OEORI_ItmMast_DR: Item solicitado
- OEORI_Qty: Cantidad
- OEORI_PriorityCode: Prioridad

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEORI_OEORD_ParRef | numeric | PK |  | NO | Des Ref to OEORD |
| ChildQ58DR | - |  |  | SI | Child Reference: Motor Examination |
| OEORI_APPT_DR | varchar |  | FK | SI | Des REf APPT |
| OEORI_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| OEORI_ARPBLItem_DR | varchar |  | FK | SI | Des Ref ARPBL Item |
| OEORI_Abnormal | varchar |  |  | SI | Abnormal flag |
| OEORI_AccessionNumber | varchar |  |  | SI | Accession Number |
| OEORI_Action_DR | bigint |  | FK | SI | Des Ref Action |
| OEORI_Activity | varchar |  |  | SI | Activity |
| OEORI_AdmInsurance_DR | varchar |  | FK | SI | Des Ref AdmInsurance |
| OEORI_AdmLoc_DR | bigint |  | FK | SI | Des Ref AdmLoc |
| OEORI_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| OEORI_AdministerSkinTest | varchar |  |  | SI | Administer after Skin Test |
| OEORI_AlertReason_DR | bigint |  | FK | SI | Des Ref AlertReason |
| OEORI_AllergyReason_DR | bigint |  | FK | SI | Des Ref AllergyReason |
| OEORI_AnaOper_DR | varchar |  | FK | SI | Des Ref Anaest Oper |
| OEORI_AnaestAgent_DR | varchar |  | FK | SI | Des Ref AnaestAgent |
| OEORI_Anaest_DR | varchar |  | FK | SI | Des Ref Anaest |
| OEORI_Annotation_DR | bigint |  | FK | SI | Des Ref Annotation |
| OEORI_ApplyTimeFrame | varchar |  |  | SI | Apply time frame |
| OEORI_ApprovalDate | date |  |  | SI | Approval Date  |
| OEORI_ApprovalInd | varchar |  |  | SI | Approval Indication |
| OEORI_ApprovalNo | varchar |  |  | SI | Approval Number |
| OEORI_ApprovalTime | time |  |  | SI | Approval Time |
| OEORI_ApprovedBy | varchar |  |  | SI | Approved By |
| OEORI_Assistant_DR | varchar |  | FK | SI | Des REf Assistant |
| OEORI_AttachToTextResult | bit |  |  | SI | - |
| OEORI_AuthComments | varchar |  |  | SI | AuthComments |
| OEORI_AuthoriseClinician_DR | varchar |  | FK | SI | Des Ref AuthoriseClinician |
| OEORI_AuthorisedDate | date |  |  | SI | Authorised Date |
| OEORI_AuthorisedTime | time |  |  | SI | Authorised Time |
| OEORI_AutologousBloodReq | varchar |  |  | SI | AutologousBloodReq |
| OEORI_BBExtCode | varchar |  |  | SI | BBExtCode |
| OEORI_BBStatus | varchar |  |  | SI | BBStatus |
| OEORI_BBTAG1 | varchar |  |  | SI | BBTAG1 |
| OEORI_BBTAG2 | varchar |  |  | SI | BBTAG2 |
| OEORI_BBTAG3 | varchar |  |  | SI | BBTAG3 |
| OEORI_BBTAG4 | varchar |  |  | SI | BBTAG4 |
| OEORI_BBTAG5 | varchar |  |  | SI | BBTAG5 |
| OEORI_BillDesc | varchar |  |  | SI | Bill Description |
| OEORI_Billed | varchar |  |  | SI | OEORI_Billed |
| OEORI_BodySite_DR | bigint |  | FK | SI | Des Ref BodySite |
| OEORI_BrokerageGenerated | varchar |  |  | SI | Brokerage Generated |
| OEORI_BrokerageVendorRate_DR | varchar |  | FK | SI | Des Ref VendorRates |
| OEORI_BrokerageVendor_DR | bigint |  | FK | SI | Des Ref Vendor |
| OEORI_CalcQtyFlag | varchar |  |  | SI | CalcQtyFlag  |
| OEORI_CancelReason_DR | bigint |  | FK | SI | Des ref CancelReason |
| OEORI_Carbohydrate | double |  |  | SI | Carbohydrate |
| OEORI_Categ_DR | bigint |  | FK | SI | Des Ref Categ |
| OEORI_Childsub | numeric |  |  | NO | OEORI Child Sub (New Key) |
| OEORI_ClinPathways_DR | varchar |  | FK | SI | Des Ref ClinPathways |
| OEORI_ClinicGroup_DR | bigint |  | FK | SI | Des Ref ClinicGroup |
| OEORI_ClinicallySignificant | varchar |  |  | SI | Clinically Significant |
| OEORI_CollectedBy | varchar |  |  | SI | CollectedBy |
| OEORI_CollectionDep_DR | bigint |  | FK | SI | Des Ref CTLOC |
| OEORI_Comment1 | varchar |  |  | SI | Comment1 |
| OEORI_Comment2 | varchar |  |  | SI | Comment2 |
| OEORI_Comment3 | varchar |  |  | SI | Comment3 |
| OEORI_CompXMatchReq | varchar |  |  | SI | CompXMatchReq |
| OEORI_ConsCateg_DR | bigint |  | FK | SI | Des REfConsCateg |
| OEORI_ConsentReceived | bit |  |  | SI | - |
| OEORI_ConsultDep_DR | bigint |  | FK | SI | Des Ref CTLOC |
| OEORI_ConsultDr_DR | varchar |  | FK | SI | Des Ref to CTCP |
| OEORI_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| OEORI_ContOrderAfterDischarge | varchar |  |  | SI | ContOrderAfterDischarge |
| OEORI_ContactCareProv | varchar |  |  | SI | Contact Care Prov |
| OEORI_ContrastBatchNumber | varchar |  |  | SI | Contrast Batch Number |
| OEORI_ContrastExpiryDate | date |  |  | SI | Contrast Expiry Date |
| OEORI_ContrastType_DR | bigint |  | FK | SI | Des Ref Contrast Type |
| OEORI_ContrastVolume | double |  |  | SI | Contrast Volume |
| OEORI_Cost | double |  |  | SI | Cost (to calculate price) |
| OEORI_CoverMainIns | varchar |  |  | SI | Covered by Main Insurance |
| OEORI_CurrRepeatNumber | varchar |  |  | SI | CurrRepeatNumber |
| OEORI_CurrSampleExpiry | date |  |  | SI | CurrSampleExpiry |
| OEORI_DRCross_DR | varchar |  | FK | SI | Des Ref to CTPCP (Cross Out Name) |
| OEORI_DRGOrder | varchar |  |  | SI | DRG Order |
| OEORI_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| OEORI_Date | date |  |  | SI | Date |
| OEORI_DateAuthReq | date |  |  | SI | DateAuthReq |
| OEORI_DateExecuted | date |  |  | SI | Date Executed |
| OEORI_DatePOAuthorised | date |  |  | SI | DatePOAuthorised |
| OEORI_DateRead | date |  |  | SI | Date Read |
| OEORI_DateReviewed | date |  |  | SI | Date Reviewed |
| OEORI_DateTime | varchar |  |  | SI | Date/Time Computed |
| OEORI_DateUnRead | date |  |  | SI | Date UnRead |
| OEORI_DayBookAccessionNo | varchar |  |  | SI | Day Book Accession No |
| OEORI_DayBookSpecimen | varchar |  |  | SI | DayBookSpecimen |
| OEORI_DayOfCycle | double |  |  | SI | DayOfCycle |
| OEORI_DelayMeal | varchar |  |  | SI | Delay Meal |
| OEORI_DemandNumber | varchar |  |  | SI | Demand Number |
| OEORI_DepProcNotes | varchar |  |  | SI | Notes for Processing Department |
| OEORI_DepType | varchar |  |  | SI | Department Type |
| OEORI_DerivedFrom | varchar |  |  | SI | DerivedFrom |
| OEORI_DietFlag | varchar |  |  | SI | DietFlag |
| OEORI_DiscountAmt | varchar |  |  | SI | Discount Amt |
| OEORI_DiscountDate | date |  |  | SI | Discount Date |
| OEORI_DiscountDoctor_DR | varchar |  | FK | SI | Discount Doctor |
| OEORI_DiscountPerc | varchar |  |  | SI | Discount Perc |
| OEORI_DiscountReason | varchar |  |  | SI | Discount Reason |
| OEORI_DiscountTime | time |  |  | SI | Discount Time |
| OEORI_DispensingTimes | varchar |  |  | SI | Dispensing Times |
| OEORI_DoNotDisplay | varchar |  |  | SI | DoNotDisplay |
| OEORI_DoctorExecuted_DR | varchar |  | FK | SI | Des REf Doctor Executed |
| OEORI_Doctor_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| OEORI_Dosage_DR | bigint |  | FK | SI | Des Ref to PHCDO |
| OEORI_DoseQty | varchar |  |  | SI | Dose Quantity, if ITM2MinDoseQty of User.OEOrdItem... |
| OEORI_Durat_DR | bigint |  | FK | SI | Des Ref to PHCDU |
| OEORI_EligibilityStatus | varchar |  |  | SI | EligibilityStatus |
| OEORI_EndDate | date |  |  | SI | End Date |
| OEORI_EndTime | time |  |  | SI | EndT ime |
| OEORI_Energy_DR | bigint |  | FK | SI | Des Ref Energy |
| OEORI_EnteredUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| OEORI_EpisArriveDate | date |  |  | SI | Epis Arrive Date |
| OEORI_EpisArriveTime | time |  |  | SI | Epis Arrive Time |
| OEORI_EpisDepartDate | date |  |  | SI | Epis Depart Date |
| OEORI_EpisDepartTime | time |  |  | SI | Epis Depart Time |
| OEORI_EpisReadyDate | date |  |  | SI | Epis Ready Date |
| OEORI_EpisReadyTime | time |  |  | SI | Epis Ready Time |
| OEORI_ExamAbandonReason_DR | bigint |  | FK | SI | Des Ref Exam AbandonReason |
| OEORI_ExamStartTime | time |  |  | SI | ExamStartTime |
| OEORI_ExpectedCollDate | date |  |  | SI | Expected Coll Date |
| OEORI_ExpectedCollTime | time |  |  | SI | Expected Collection Time |
| OEORI_ExpiryDate | date |  |  | SI | ExpiryDate |
| OEORI_ExposureKV | double |  |  | SI | Exposure KV |
| OEORI_Exposure_mAs | double |  |  | SI | Exposure_mAs |
| OEORI_ExtBaseUOM_DR | bigint |  | FK | SI | Des Ref UOM |
| OEORI_ExtQtyTobePacked | double |  |  | SI | ExtQtyTobePacked |
| OEORI_ExternalPrimarySpecSite | varchar |  |  | SI | ExternalPrimarySpecSite |
| OEORI_ExternalRefDoctor_DR | bigint |  | FK | SI | Des Ref ExternalRefDoctor |
| OEORI_ExternalSecondarySpecSite | varchar |  |  | SI | ExternalSecondarySpecSite |
| OEORI_Fat | double |  |  | SI | Fat |
| OEORI_FillerNo | varchar |  |  | SI | Filler No |
| OEORI_FilmReasonForRejection_DR | bigint |  | FK | SI | Des Ref Film Reason For Rejection |
| OEORI_FinDate | date |  |  | SI | Finish Date of the order |
| OEORI_FlowQty | double |  |  | SI | Flow Qty |
| OEORI_FlowRateUnit_DR | bigint |  | FK | SI | Des Ref FlowRate |
| OEORI_FreqDelay | double |  |  | SI | FreqDelay |
| OEORI_HICClaimNo | varchar |  |  | SI | HIC Claim No |
| OEORI_HL7ResultDate | date |  |  | SI | HL7ResultDate |
| OEORI_HL7ResultStatus | varchar |  |  | SI | HL7ResultStatus |
| OEORI_HL7ResultTime | time |  |  | SI | HL7ResultTime |
| OEORI_HotReportRequired | varchar |  |  | SI | HotReportRequired |
| OEORI_IVType | varchar |  |  | SI | IVType |
| OEORI_ImplantType_DR | bigint |  | FK | SI | Des Ref ImplantType |
| OEORI_IncompleteCollection | varchar |  |  | SI | Incomplete Collection |
| OEORI_IndicTransfusion_DR | bigint |  | FK | SI | Des Ref IndicTransfusion |
| OEORI_InfoSubType | varchar |  |  | SI | InfoSubType - as supplied by the user, used only f... |
| OEORI_InfoType | varchar |  |  | SI | InfoType - OrderType as supplied by the user, used... |
| OEORI_InjectionTime | time |  |  | SI | Injection Time |
| OEORI_InsBillCondit_DR | bigint |  | FK | SI | Insurance Billing Condition |
| OEORI_InsCardNoOverride | varchar |  |  | SI | InsCardNoOverride |
| OEORI_Instr_DR | bigint |  | FK | SI | Des Ref to PHCIN |
| OEORI_Interval_DR | double |  | FK | SI | Des Ref Interval |
| OEORI_IsAdHoc | varchar |  |  | SI | IsAdHoc |
| OEORI_IsBrokerage | varchar |  |  | SI | IsBrokerage  |
| OEORI_IsotopeDose | double |  |  | SI | Isotope Dose |
| OEORI_ItemGroup | varchar |  |  | SI | Item Group |
| OEORI_ItemStat_DR | bigint |  | FK | SI | Item Status |
| OEORI_ItmMast_DR | varchar |  | FK | NO | Des Ref to ARCIM |
| OEORI_LDMP | date |  |  | SI | LDMP |
| OEORI_LMPDate | date |  |  | SI | LMP Date |
| OEORI_LTSiteCode | varchar |  |  | SI | LTSiteCode |
| OEORI_LTSpecCode | varchar |  |  | SI | LTSpecCode |
| OEORI_Lab1 | varchar |  |  | SI | Lab1 |
| OEORI_Lab2 | varchar |  |  | SI | Lab2 |
| OEORI_LabAction | varchar |  |  | SI | Lab Action |
| OEORI_LabEpisodeNo | varchar |  |  | SI | Lab Episode No |
| OEORI_LabEpisodeSetup | varchar |  |  | SI | Lab Episode Setup flag |
| OEORI_LabReceiveDate | date |  |  | SI | LabReceiveDate |
| OEORI_LabReceiveTime | time |  |  | SI | LabReceiveTime |
| OEORI_LabResultDate | date |  |  | SI | LabResult Date |
| OEORI_LabResultTime | time |  |  | SI | Discount Time |
| OEORI_LabSeqNo | varchar |  |  | SI | LabSeqNo |
| OEORI_LabTestSetRow | varchar |  |  | SI | LabTestSet RowId |
| OEORI_LabVolume | varchar |  |  | SI | LabVolume |
| OEORI_LabelCopies | double |  |  | SI | LabelCopies |
| OEORI_LabelText | varchar |  |  | SI | LabelText |
| OEORI_LinkNo | varchar |  |  | SI | LinkNo |
| OEORI_LinkToOrder | varchar |  |  | SI | Link To Order |
| OEORI_LtClinicalCondition | varchar |  |  | SI | ClinicalCondition |
| OEORI_MainOeEnt_DR | varchar |  | FK | SI | Des REf MainOeEnt_DR |
| OEORI_ManufacturerOrder_DR | bigint |  | FK | SI | Des Ref Manufacturer Order |
| OEORI_MaxNumberOfRepeats | varchar |  |  | SI | Max Number Of Repeats |
| OEORI_MaxRepeats | double |  |  | SI | MaxRepeats |
| OEORI_MealType_DR | bigint |  | FK | SI | Des Ref MealType |
| OEORI_NeedleGauge_DR | bigint |  | FK | SI | Des Ref NeedleGauge |
| OEORI_NeedleType_DR | bigint |  | FK | SI | Des Ref NeedleType |
| OEORI_NoConsentOverrideReas_DR | bigint |  | FK | SI | Des Ref NoConsentOverrideReas |
| OEORI_NoOrderedBags | varchar |  |  | SI | No Ordered Bags |
| OEORI_NoOrdersLink | double |  |  | SI | No Orders Link |
| OEORI_Notify | varchar |  |  | SI | Notify |
| OEORI_NotifyClinician | varchar |  |  | SI | NotifyClinician |
| OEORI_NumberPerWeek | varchar |  |  | SI | Number Per Week |
| OEORI_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| OEORI_OEOrdItem2_DR | varchar |  | FK | SI | Des Ref OEOrdItem2 |
| OEORI_OPB_IPB_Conversion | varchar |  |  | SI | OPB to IPB Conversion |
| OEORI_OperCategory_DR | bigint |  | FK | SI | Des Ref OperCategory |
| OEORI_OrdDept_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| OEORI_OrdEnt_DR | varchar |  | FK | SI | Des Ref to OEORN |
| OEORI_OrderType_DR | bigint |  | FK | SI | Des Ref OrderType |
| OEORI_OriginalOrder_DR | varchar |  | FK | SI | Des Ref OriginalOrder |
| OEORI_PACClinic_DR | bigint |  | FK | SI | Des Ref PACClinic |
| OEORI_PARefPathwayStage_DR | varchar |  | FK | SI | Des Ref PARefPathwayStage |
| OEORI_PHFreq_DR | bigint |  | FK | SI | des ref to PHCFR |
| OEORI_PRN | varchar |  |  | SI | Patient Reg No |
| OEORI_PRNIndication | varchar |  |  | SI | PRNIndication |
| OEORI_PRNMaxDose24hrs | double |  |  | SI | PRNMaxDose24hrs |
| OEORI_PRNTotNumberDosesAll | double |  |  | SI | PRNTotal NumberDosesAllowed |
| OEORI_PackOverReason_DR | bigint |  | FK | SI | Des Ref PackOverReason |
| OEORI_Panic | varchar |  |  | SI | Panic |
| OEORI_PasterizeFood | varchar |  |  | SI | Pasterize Food |
| OEORI_PatConsentObtained | varchar |  |  | SI | PatConsentObtained |
| OEORI_PatientIDChecked | varchar |  |  | SI | Patient ID Checked |
| OEORI_PendingStatus_DR | bigint |  | FK | SI | Des Ref PendingStatus |
| OEORI_PersonInject_DR | varchar |  | FK | SI | Des Ref CTPCP |
| OEORI_Personnel | varchar |  |  | SI | Personnel |
| OEORI_PhQtyOrd | double |  |  | SI | Quantity Ordered |
| OEORI_PhSpecInstr | varchar |  |  | SI | Specialist Instruction |
| OEORI_PharmacyStatus | varchar |  |  | SI | Pharmacy Status |
| OEORI_PhoneOrder | varchar |  |  | SI | PhoneOrder |
| OEORI_PlacerNo | varchar |  |  | SI | Placer No |
| OEORI_PortEquipReq | varchar |  |  | SI | Portable Equipment Required |
| OEORI_PostExamStartTime | time |  |  | SI | Post Exam Start Time |
| OEORI_PostExamUser | varchar |  |  | SI | Post Exam User |
| OEORI_PostExamUserHospDR | bigint |  | FK | SI | Des Ref PostExamUserHospDR |
| OEORI_PreExamUser | varchar |  |  | SI | Pre Exam User |
| OEORI_PreExamUserHospDR | bigint |  | FK | SI | Des Ref PreExamUserHospDR |
| OEORI_PregnancyCheck | varchar |  |  | SI | PregnancyCheck - Standard Type YesNoUnknown |
| OEORI_Pregnant | varchar |  |  | SI | Pregnant |
| OEORI_PreparationTime | double |  |  | SI | Preparation Time |
| OEORI_PrescNo | varchar |  |  | SI | Prescription No |
| OEORI_PrescRepExpiryDate | date |  |  | SI | PrescRepExpiryDate |
| OEORI_PrescRepNumberDays | double |  |  | SI | PrescRep Number of Days |
| OEORI_PrescSeqNo | varchar |  |  | SI | Presc Seq No |
| OEORI_PrescType | varchar |  |  | SI | Prescription Type |
| OEORI_Price | double |  |  | SI | Price |
| OEORI_PrimaryOrderItem | varchar |  |  | SI | Primary Order Item Flag |
| OEORI_Priority_DR | bigint |  | FK | SI | Des Ref to OECPR |
| OEORI_ProsBatchNo | varchar |  |  | SI | ProsBatchNo |
| OEORI_ProsReceivedDate | date |  |  | SI | ProsReceivedDate |
| OEORI_ProsReceivedTime | time |  |  | SI | ProsReceivedTime |
| OEORI_ProsSerialNo | varchar |  |  | SI | ProsSerialNo |
| OEORI_ProsSupplier | varchar |  |  | SI | ProsSupplier |
| OEORI_Protein | double |  |  | SI | Protein |
| OEORI_Qty | varchar |  |  | SI | Qty |
| OEORI_QtyPackUOM | double |  |  | SI | Qty for Packing UOM |
| OEORI_Questionnaire | varchar |  |  | SI | Questionnaire |
| OEORI_RBResource_DR | bigint |  | FK | SI | Des Ref RBResource |
| OEORI_RMDurat_DR | bigint |  | FK | SI | Des Ref Durat |
| OEORI_RMFreq_DR | bigint |  | FK | SI | Des Ref to Freq |
| OEORI_RVICharge_DR | varchar |  | FK | SI | Des Ref RVICharges |
| OEORI_RadAuthDoc_DR | varchar |  | FK | SI | Des Ref RadAuthDoc |
| OEORI_RadiationDoesUnit_DR | bigint |  | FK | SI | Des Ref RadiationDoesUnit |
| OEORI_RadiologyStatus | varchar |  |  | SI | RadiologyStatus |
| OEORI_ReadyToBill | varchar |  |  | SI | ReadyToBill |
| OEORI_ReasOrdCMVNegBlood | varchar |  |  | SI | ReasOrdCMVNegBlood |
| OEORI_ReasonIncReturn_DR | bigint |  | FK | SI | Des Ref INCReasonIncReturn |
| OEORI_ReasonNotCollected | varchar |  |  | SI | Reason Not Collected |
| OEORI_ReasonRefund_DR | bigint |  | FK | SI | Des Ref ReasonForRefund |
| OEORI_ReasonRejectPresc_DR | bigint |  | FK | SI | Des Ref ReasonRejectPresc |
| OEORI_ReassessmentDate | date |  |  | SI | Pharmacy Reassessment Date |
| OEORI_ReassessmentTime | time |  |  | SI | Pharmacy Reassessment Time |
| OEORI_RecDep_DR | bigint |  | FK | SI | Des REf to CTLOC |
| OEORI_RecLocVerified | varchar |  |  | SI | RecLocVerified |
| OEORI_RefCln_DR | bigint |  | FK | SI | Des Ref RefCln |
| OEORI_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| OEORI_RefundQty | double |  |  | SI | Refund Qty |
| OEORI_RefundType | varchar |  |  | SI | Refund Type |
| OEORI_Remarks | varchar |  |  | SI | Notes for Care Provider |
| OEORI_RemoteDutyType | varchar |  |  | SI | Remote Duty Order Type |
| OEORI_RemoteDuty_DR | bigint |  | FK | SI | Des Ref OERemoteDuty - Remote Duty Order |
| OEORI_RepeatDesc | varchar |  |  | SI | Description of Repeat Interval |
| OEORI_ResultAvailable | varchar |  |  | SI | ResultAvailable |
| OEORI_ResultAvailableDate | date |  |  | SI | ResultAvailableDate |
| OEORI_ResultComments | varchar |  |  | SI | Result Comments |
| OEORI_ResultDSReportFlag | varchar |  |  | SI | ResultDSReportFlag |
| OEORI_ResultExist | varchar |  |  | SI | ResultExist |
| OEORI_ResultFlag | varchar |  |  | SI | Result Status flag |
| OEORI_ResultGroup | varchar |  |  | SI | Result Group |
| OEORI_ResultRef | varchar |  |  | SI | Result Reference |
| OEORI_ResultUpdateDate | date |  |  | SI | ResultUpdateDate |
| OEORI_ResultUpdateHospital_DR | bigint |  | FK | SI | Des Ref ResultUpdateHospital |
| OEORI_ResultUpdateTime | time |  |  | SI | ResultUpdateTime |
| OEORI_ResultUpdateUser_DR | bigint |  | FK | SI | Des Ref ResultUpdateUser |
| OEORI_RetentionDays | double |  |  | SI | Retention Days |
| OEORI_ReturnDate | date |  |  | SI | Return Date |
| OEORI_ReturnTime | time |  |  | SI | Return Time |
| OEORI_ReturnToStock | varchar |  |  | SI | Return To Stock Flag |
| OEORI_ReturnUser_DR | bigint |  | FK | SI | Des Ref ReturnUser |
| OEORI_RiceType_DR | bigint |  | FK | SI | Des Ref RiceType |
| OEORI_Route_DR | bigint |  | FK | SI | Des Ref Route |
| OEORI_RowId | varchar |  |  | NO | - |
| OEORI_ScreeningTime | double |  |  | SI | Screening Time |
| OEORI_SecondOrderingUser_DR | bigint |  | FK | SI | Des Ref SecondOrderingUser |
| OEORI_SensitivitiesSignoff | varchar |  |  | SI | SensitivitiesSignoff |
| OEORI_SentInExtract | varchar |  |  | SI | SentInExtract |
| OEORI_SeqNo | varchar |  |  | SI | Sequence No |
| OEORI_SeriesNo | varchar |  |  | SI | Radiology SeriesNo |
| OEORI_Significant | varchar |  |  | SI | Significant  |
| OEORI_Size | varchar |  |  | SI | Size |
| OEORI_SkinTestOutcome_DR | bigint |  | FK | SI | Des Ref SkinTestOutcome |
| OEORI_Specialty_DR | bigint |  | FK | SI | Des Ref Specialty |
| OEORI_SpeedFlowRate | double |  |  | SI | SpeedFlowRate |
| OEORI_SpeedFlowValue | varchar |  |  | SI | Speed Flow Rate Calc Value |
| OEORI_SterilizeUtelsis | varchar |  |  | SI | Sterilize Utelsis |
| OEORI_StockBatches | varchar |  |  | SI | StockBatches |
| OEORI_SttDat | date |  |  | SI | Order Start Date |
| OEORI_SttTim | time |  |  | SI | Order Start Time |
| OEORI_SubCateg_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| OEORI_SupplierContactedDate | date |  |  | SI | SupplierContactedDate |
| OEORI_SupplierContactedTime | time |  |  | SI | SupplierContactedTime |
| OEORI_TestSetComments | varchar |  |  | SI | TestSetComments |
| OEORI_Text1 | varchar |  |  | SI | Text1 |
| OEORI_Text1Reviewed | varchar |  |  | SI | Text1Reviewed |
| OEORI_Text2 | varchar |  |  | SI | Text2 |
| OEORI_Text2Reviewed | varchar |  |  | SI | Text2Reviewed |
| OEORI_Text3 | varchar |  |  | SI | Text3 |
| OEORI_Text4 | varchar |  |  | SI | Text4 |
| OEORI_TheatreDate | date |  |  | SI | Theatre Date |
| OEORI_TheatreRequired | varchar |  |  | SI | Theatre Required |
| OEORI_Time | double |  |  | SI | Time(No of Times) |
| OEORI_TimeAuthReq | time |  |  | SI | TimeAuthReq |
| OEORI_TimeExecuted | time |  |  | SI | Time Executed |
| OEORI_TimeOrd | time |  |  | SI | Time of Order |
| OEORI_TimePOAuthorised | time |  |  | SI | TimePOAuthorised |
| OEORI_TimeRead | time |  |  | SI | Time Read |
| OEORI_TimeReviewed | time |  |  | SI | Time Reviewed |
| OEORI_TimeUnread | time |  |  | SI | Time Unread |
| OEORI_TotalExtQtyInBaseUOM | double |  |  | SI | TotalExtQtyInBaseUOM |
| OEORI_TypeSizeOfFilmsRejected_DR | bigint |  | FK | SI | Des Ref TypeSizeOfFilmsRejected |
| OEORI_Type_SizeOfFilmsUsed_DR | bigint |  | FK | SI | Des Ref Type_SizeOfFilmsUsed |
| OEORI_Unit | varchar |  |  | SI | Unit |
| OEORI_UnitCost | double |  |  | SI | OEORI_UnitCost |
| OEORI_Unit_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| OEORI_Unit_Hrs | varchar |  |  | SI | Unit(Hrs) |
| OEORI_UnitsCollected | varchar |  |  | SI | Units Collected |
| OEORI_UpdateDate | date |  |  | SI | UpdateDate |
| OEORI_UpdateTime | time |  |  | SI | Update Time |
| OEORI_UrgentReport | varchar |  |  | SI | UrgentReport |
| OEORI_UserAdd | bigint |  |  | SI | Des Ref SS_User |
| OEORI_UserAddHospDR | bigint |  | FK | SI | Des Ref UserAddHospDR |
| OEORI_UserAuthorise | varchar |  |  | SI | User Authorise |
| OEORI_UserAuthoriseHospDR | bigint |  | FK | SI | Des Ref UserAuthoriseHospDR |
| OEORI_UserDepartment_DR | bigint |  | FK | SI | Des Ref Department |
| OEORI_UserExecuted | bigint |  |  | SI | Des Ref SSUSR |
| OEORI_UserRead_DR | bigint |  | FK | SI | Des Ref UserRead |
| OEORI_UserReviewed_DR | bigint |  | FK | SI | Des Ref SSUser |
| OEORI_UserUnRead_DR | bigint |  | FK | SI | Des Ref UserUnRead |
| OEORI_UserUpdate | bigint |  |  | SI | Des Ref UserUpdate |
| OEORI_VariableDose | varchar |  |  | SI | VariableDose |
| OEORI_VarianceReason_DR | bigint |  | FK | SI | Des Ref VarianceReason |
| OEORI_View | varchar |  |  | SI | View |
| OEORI_Volume_DR | bigint |  | FK | SI | Des Ref Volume |
| OEORI_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |
| OEORI_WeeksPregnant | double |  |  | SI | WeeksPregnant |
| OEORI_WhoGoWhere | varchar |  |  | SI | Who Goes Where |
| OEORI_XCTCP_DR | varchar |  | FK | SI | X out Doctor |
| OEORI_XDate | date |  |  | SI | Cross Out Date |
| OEORI_XTime | time |  |  | SI | Cross Out Time |
| OEORI_YesNo1 | varchar |  |  | SI | YesNo1 |
| OEORI_YesNo2 | varchar |  |  | SI | YesNo2 |
| OEORI_YesNo3 | varchar |  |  | SI | YesNo3 |
| OEORI_YesNo4 | varchar |  |  | SI | YesNo4 |
| Q17Q1 | - |  |  | SI | Body Part |
| Q17Q2 | - |  |  | SI | Symptoms |
| Q17Q3 | - |  |  | SI | Location |
| Q17Q4 | - |  |  | SI | Nature |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*