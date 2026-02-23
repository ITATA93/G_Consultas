# SQLUser.AR_PatBillGroupCharges

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | AR_PatBillGroup Parent Reference |
| ChildQ01DR | - |  |  | SI | Child Reference: Lista de Marcas para un Episodio |
| ITM_ANAEST_Duration | double |  |  | SI | ANAEST_Duration |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_Account | varchar |  |  | SI | Account |
| ITM_ActRAPaymAmount | double |  |  | SI | Activity RA Payment amount  |
| ITM_ActivClaimStatus_DR | bigint |  | FK | SI | Des Ref ARCBillClaimStatus |
| ITM_ActivityID | varchar |  |  | SI | Activity ID |
| ITM_AdditionalDiscount | double |  |  | SI | Additional Discount |
| ITM_AdminDateFrom | date |  |  | SI | AdminDateFrom |
| ITM_AdminDateTo | date |  |  | SI | AdminDateTo |
| ITM_AdminTimeFrom | time |  |  | SI | Admin Time From |
| ITM_AdminTimeTo | time |  |  | SI | Admin Time To |
| ITM_AdvPayorInvoicetem_DR | varchar |  | FK | SI | Des Ref ARPatBillGroupCharges |
| ITM_AmountCoveredUnderPack | double |  |  | SI | Amount Covered Under Package |
| ITM_AmtPayorPaid | double |  |  | SI | Amt Payor Paid |
| ITM_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ITM_BasePrice | double |  |  | SI | Base Price |
| ITM_BaseRate | double |  |  | SI | Base Rate |
| ITM_Bed_DR | varchar |  | FK | SI | Des Ref to PACBed |
| ITM_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| ITM_BillingItem_DR | bigint |  | FK | SI | Billing Item |
| ITM_CareProvAmount | double |  |  | SI | Care Provider Proportion Amount  |
| ITM_CareProvChargeCode | varchar |  |  | SI | Care Provider Proportion Charge Code |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CopaymentAmount | double |  |  | SI | Copayment Amount |
| ITM_CopaymentAmountBeforeTax | double |  |  | SI | Copayment Amount |
| ITM_DRGAddOn_DR | varchar |  | FK | SI | DRG Add ON, Des Ref ARCItmMast |
| ITM_DRGCost | double |  |  | SI | DRG Cost |
| ITM_DRGMultiplier | double |  |  | SI | DRG Multiplier |
| ITM_DRGOutlier | varchar |  |  | SI | DRG Outlier |
| ITM_DailyQty | double |  |  | SI | Daily Qty |
| ITM_Date | date |  |  | SI | Order Date |
| ITM_DeductibleAmount | double |  |  | SI | DeductibleAmount |
| ITM_Depart_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| ITM_DiscountAmountBeforeTax | double |  |  | SI | Discount Amount Before Tax |
| ITM_DiscountBeforeTax | double |  |  | SI | Discount Before Tax |
| ITM_DiscretAmount | double |  |  | SI | Discretionary Discount Amount |
| ITM_FeeAmount | double |  |  | SI | Fee Amount |
| ITM_GrossAmount | double |  |  | SI | Gross Amount |
| ITM_HCPValue | varchar |  |  | SI | HCP Value |
| ITM_HandiShare | double |  |  | SI | Handicapped Association Share - Currently used for... |
| ITM_HighOutlierPrice | double |  |  | SI | High Outlier Price |
| ITM_InsCompanyShare | double |  |  | SI | Insurance Company Share |
| ITM_InsCoverStatus_DR | bigint |  | FK | SI | Des Ref to InsCoverStatus |
| ITM_InsSubCat_DR | varchar |  | FK | SI | Des Ref to ARC_InsSubCat |
| ITM_InsuranceType_DR | bigint |  | FK | SI | Des Ref InsuranceType |
| ITM_ItemBillingType | varchar |  |  | SI | ItemBillingType |
| ITM_ItemPriceItaly_DR | varchar |  | FK | SI | Des Ref ItemPriceItaly |
| ITM_LineTotal | double |  |  | SI | Line Total |
| ITM_LocalGovtShare | double |  |  | SI | Local Govt Share |
| ITM_LowOutlierPrice | double |  |  | SI | Low Outlier Price |
| ITM_MainOrdItem_DR | varchar |  | FK | SI | Des Ref OEORI |
| ITM_MaterialTotal | double |  |  | SI | Material Total |
| ITM_MedisaveCode | varchar |  |  | SI | MedisaveCode |
| ITM_NetAmount | double |  |  | SI | Net Amount |
| ITM_NoTimes | double |  |  | SI | No of Times |
| ITM_OEAdmixManufIngr_DR | varchar |  | FK | SI | Des Ref to OEAdmixManufIngr |
| ITM_OEAdmix_DR | bigint |  | FK | SI | Des Ref to OEOrdAdmix |
| ITM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| ITM_OrdCategGroup_DR | bigint |  | FK | SI | Des Ref OrdCategGroup |
| ITM_OrdCateg_DR | bigint |  | FK | SI | Des Ref OrdCateg |
| ITM_OrdSubCat_DR | bigint |  | FK | SI | Des Ref OrdSubCat |
| ITM_OrderCareProvClaimID | varchar |  |  | SI | Ordering Care Provider Claim ID |
| ITM_OrderTime | time |  |  | SI | Order Time |
| ITM_OutlierDiscount | double |  |  | SI | Outlier Discount |
| ITM_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| ITM_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| ITM_OverrideOrderCareProvClaimID | varchar |  |  | SI | Override Ordering Care Provider Claim ID |
| ITM_OverridePayorApprovNumber | varchar |  |  | SI | Override Payor Approval Number |
| ITM_PAADM_DR | bigint |  | FK | SI | Des Ref to PAADM |
| ITM_PADiscFactor | double |  |  | SI | Payment Agreement Discount Factor |
| ITM_PackageQtyExceeded | varchar |  |  | SI | UnSettled |
| ITM_PatInsFlag | varchar |  |  | SI | Patient Insurance Flag |
| ITM_PatientClassif | varchar |  |  | SI | Patient Classification  |
| ITM_PatientServiceTax | double |  |  | SI | Patient Service Tax |
| ITM_PatientShare | double |  |  | SI | Patient Share |
| ITM_PayorCode | varchar |  |  | SI | PayorCode |
| ITM_PersonPackageDet_DR | varchar |  | FK | SI | Des Ref PAPersonPackageDet |
| ITM_PrescNo | varchar |  |  | SI | Prescription No |
| ITM_PriceBeforeDiscBeforeTax | double |  |  | SI | Price Before Discount Before Tax |
| ITM_ProportionalAmount | double |  |  | SI | Proportional Amount |
| ITM_QuoteItemUsed_DR | varchar |  | FK | SI | Quote Item used Des Ref ARQuoteItems |
| ITM_QuoteItem_DR | varchar |  | FK | SI | Des Ref ARQuoteItems |
| ITM_RADeniedAmount | double |  |  | SI | RA Denied Amount |
| ITM_RVI_BiilGrp_DR | varchar |  | FK | SI | Des REf BiilGrp_DR |
| ITM_ReSubmission | varchar |  |  | SI | Re-Submission |
| ITM_ReasonActDenial_DR | bigint |  | FK | SI | Des Ref ARCReasonForActivityDenial |
| ITM_ReasonClaimStatChange_DR | bigint |  | FK | SI | Des Ref ARCReasonForClaimStatChange |
| ITM_RoomType_DR | bigint |  | FK | SI | Des Ref to PACRoomType |
| ITM_Room_DR | bigint |  | FK | SI | Des Ref to PACRoom |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_ServTaxAfterDiscretDisc | double |  |  | SI | Service Tax After Discretionary Discount |
| ITM_ServTax_DR | bigint |  | FK | SI | Des Ref to ARCST |
| ITM_ServiceCharge | varchar |  |  | SI | Service charge applied to this item |
| ITM_ServiceMaterial | varchar |  |  | SI | Service/Material |
| ITM_ServiceTotal | double |  |  | SI | Service Total |
| ITM_SpecialistSurcharge | double |  |  | SI | Specialist Surcharge |
| ITM_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| ITM_TotalTaxAmount | double |  |  | SI | Total Tax Amount |
| ITM_UnSettled | varchar |  |  | SI | UnSettled |
| ITM_UnderSupplyMultiplier | double |  |  | SI | Under Supply Multiplier |
| ITM_UnderSupplyRatio | double |  |  | SI | Under Supply Ratio |
| ITM_UnitPrice | double |  |  | SI | Unit Price |
| ITM_Ward_DR | bigint |  | FK | SI | Des Ref to PACWard |
| ITM_WeightRate | double |  |  | SI | Weight Rate |
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