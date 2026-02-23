# SQLUser.AR_ChargesOverride

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COV_RowId | bigint | PK |  | NO | - |
| COV_AdjustPricePerc | double |  |  | SI | Adjust Price Percentage |
| COV_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| COV_Amount | double |  |  | SI | Amount |
| COV_ApplyGST | varchar |  |  | SI | Apply GST |
| COV_ApprovedQty | double |  |  | SI | Approved Quantity |
| COV_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| COV_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| COV_BenefitPackage_DR | varchar |  | FK | SI | Des Ref ARCAuxilInsurTypeBenefitPackage |
| COV_BillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| COV_BillQty | double |  |  | SI | Bill Qty |
| COV_BillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| COV_BillingStatus | varchar |  |  | SI | Billing Status  |
| COV_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| COV_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| COV_CommentDisc | varchar |  |  | SI | Discount Comment |
| COV_DateFrom | date |  |  | SI | DateFrom |
| COV_DateTo | date |  |  | SI | DateTo |
| COV_DiscType_DR | bigint |  | FK | SI | Des Ref DiscType |
| COV_DoctorPerc | double |  |  | SI | Doctor Percentage |
| COV_Exclude | varchar |  |  | SI | Exclude |
| COV_FromNoOfDays | double |  |  | SI | From No of Days |
| COV_InsAssoc_DR | bigint |  | FK | SI | Des Ref InsAssoc |
| COV_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| COV_InsuranceExclude | bigint |  |  | SI | Des Ref Insurance Type |
| COV_ItemCat_DR | bigint |  | FK | SI | Order Subcategory |
| COV_ItemCost | double |  |  | SI | Item Cost |
| COV_ItemDesc | varchar |  |  | SI | Item Description |
| COV_ItemGroup | varchar |  |  | SI | ItemGroup |
| COV_ItmMast_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| COV_Key | varchar |  |  | SI | Key |
| COV_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| COV_OrdCat_DR | bigint |  | FK | SI | Order Category |
| COV_PatDiscountAmount | double |  |  | SI | PatientDiscountAmount |
| COV_PatDiscountPercent | double |  |  | SI | PatientDiscountPercentage |
| COV_PatDiscountReason | varchar |  |  | SI | PatientDiscountReason |
| COV_PatientAmt | double |  |  | SI | PatientAmt |
| COV_PatientDiscAmount | double |  |  | SI | Patient Discount Amount |
| COV_PatientDiscPerc | double |  |  | SI | Patient Discount Percentage |
| COV_PatientPercentage | double |  |  | SI | PatientPercentage |
| COV_PayByResult | varchar |  |  | SI | Payment By Result |
| COV_PayorDiscAmount | double |  |  | SI | Payor Discount Amount |
| COV_PayorDiscPerc | double |  |  | SI | Payor Discount Percentage |
| COV_Percentage | double |  |  | SI | Percentage |
| COV_Price | double |  |  | SI | Price |
| COV_PricePercentage | double |  |  | SI | NOT USED : TC-204550 - jira was closed because it ... |
| COV_QtyPercentage | double |  |  | SI | Quantity Percentage |
| COV_QuoteItem_DR | varchar |  | FK | SI | Des Ref ARQuoteItems |
| COV_Reason | varchar |  |  | SI | Reason |
| COV_ReasonBillStatChange_DR | bigint |  | FK | SI | Des Ref ARCReasonForBillStatChange |
| COV_ReasonForOverride_DR | bigint |  | FK | SI | Des Ref BLCReasonForOverride |
| COV_ReasonNotShow_DR | bigint |  | FK | SI | Des Ref  ReasonNotShow |
| COV_RoomType_DR | bigint |  | FK | SI | Des Ref PACRoomType |
| COV_SameDayBand | varchar |  |  | SI | SameDayBand |
| COV_ServTax_DR | bigint |  | FK | SI | Des Ref ServTax |
| COV_UpdateDate | date |  |  | SI | UpdateDate |
| COV_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| COV_UpdateTime | time |  |  | SI | UpdateTime |
| COV_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q19Q1 | - |  |  | SI | Especie |
| Q19Q2 | - |  |  | SI | NUE |
| Q19Q3 | - |  |  | SI | Destino |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*