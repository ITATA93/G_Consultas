# lab.CT_PaymentCode

**Schema:** lab
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPC_RowId | varchar | PK |  | NO | - |
| CTPC_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTPC_BatchSize | varchar |  |  | SI | Batch Size |
| CTPC_CalcManual | varchar |  |  | SI | Calculate/Manual |
| CTPC_ClaimType | varchar |  |  | SI | Claim Type |
| CTPC_Client_DR | varchar |  | FK | SI | Client DR |
| CTPC_Code | varchar |  |  | NO | Code |
| CTPC_Desc | varchar |  |  | SI | Description |
| CTPC_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTPC_EPVRequired | varchar |  |  | SI | EPV Required |
| CTPC_FeeDesc | varchar |  |  | SI | Account Fee Description |
| CTPC_FeeEvent | varchar |  |  | SI | Fee Event |
| CTPC_FeeItem_DR | varchar |  | FK | SI | Account Fee Billing Item DR |
| CTPC_FeeJournal_DR | varchar |  | FK | SI | Fee Journal code DR |
| CTPC_GST_BillingItem_DR | varchar |  | FK | SI | GST Billing Item DR |
| CTPC_GST_Description | varchar |  |  | SI | GST Description |
| CTPC_GST_Percent | double |  |  | SI | GST Percent |
| CTPC_GST_StartDate | date |  |  | SI | GST Start Date |
| CTPC_Gap_BillingItem_DR | varchar |  | FK | SI | Gap Billing Item DR |
| CTPC_Gap_Inpatient | double |  |  | SI | Gap for Inpatient |
| CTPC_Gap_OutPatient | double |  |  | SI | Gap for OutPatient |
| CTPC_Gap_PayCode_DR | varchar |  | FK | SI | Gap PayCode DR |
| CTPC_HFPayeeID | varchar |  |  | SI | HF Payee ID |
| CTPC_HICAutoRebill | varchar |  |  | SI | HIC Auto Rebill |
| CTPC_HICUpdateMedicareNumber | varchar |  |  | SI | HIC Update Medicare Number |
| CTPC_HospMrnMand | varchar |  |  | SI | Hospital MRN Mandatory |
| CTPC_InvoiceMessage | varchar |  |  | SI | Invoice Message |
| CTPC_InvoiceMessage_1 | varchar |  |  | SI | Invoice Message 1 |
| CTPC_InvoiceMessage_2 | varchar |  |  | SI | Invoice Message 2 |
| CTPC_InvoiceMessage_3 | varchar |  |  | SI | Invoice Message 3 |
| CTPC_InvoiceType_DR | varchar |  | FK | SI | Invoice type |
| CTPC_ItemSchedule_DR | varchar |  | FK | SI | Des Ref Item Schedule |
| CTPC_JournalCode_DR | varchar |  | FK | SI | Journal Code DR |
| CTPC_ManualPricing | varchar |  |  | SI | Manual Pricing |
| CTPC_MedicareConing | varchar |  |  | SI | Medicare Coning |
| CTPC_MedicareItemLimits | varchar |  |  | SI | Medicare Item Limits |
| CTPC_MultiChoice | varchar |  |  | SI | Multi Choice |
| CTPC_PatEntryPopup | varchar |  |  | SI | Patient Entry popup info |
| CTPC_PatientLocations | varchar |  |  | SI | Patient Locations |
| CTPC_PayCodeAddress | varchar |  |  | SI | Pay Code Address |
| CTPC_PayCodeAddress1 | varchar |  |  | SI | Pay Code Address 1 |
| CTPC_PayCodeAddress2 | varchar |  |  | SI | Pay Code Address 2 |
| CTPC_PayCodeAddress3 | varchar |  |  | SI | Pay Code Address 3 |
| CTPC_PaymentCodeType_DR | varchar |  | FK | SI | Payment Code Type DR |
| CTPC_PercentageOfCommon | varchar |  |  | SI | Percentage Of Common |
| CTPC_Receipt | varchar |  |  | SI | Receipt |
| CTPC_RefRequired | varchar |  |  | SI | Reference Required |
| CTPC_RegionCode | varchar |  |  | SI | Region Code |
| CTPC_Remarks | varchar |  |  | SI | Remarks |
| CTPC_Reminders | varchar |  |  | SI | Reminders |
| CTPC_Rule3Ex | varchar |  |  | SI | Rule 3 Ex |
| CTPC_SingleCreditingEntry | varchar |  |  | SI | Single Crediting Entry FROM PE |
| CTPC_Type | varchar |  |  | SI | Type |
| CTPC_VisitAction_DR | varchar |  | FK | SI | Visit Action |
| CTPC_extra_01 | varchar |  |  | SI | CTPC_extra_01 |
| CTPC_extra_02 | varchar |  |  | SI | CTPC_extra_02 |
| CTPC_extra_03 | varchar |  |  | SI | CTPC_extra_03 |
| CTPC_extra_04 | varchar |  |  | SI | CTPC_extra_04 |
| CTPC_extra_05 | varchar |  |  | SI | CTPC_extra_05 |
| CTPC_extra_06 | varchar |  |  | SI | CTPC_extra_06 |
| CTPC_extra_07 | varchar |  |  | SI | CTPC_extra_07 |
| CTPC_extra_08 | varchar |  |  | SI | CTPC_extra_08 |
| CTPC_extra_09 | varchar |  |  | SI | CTPC_extra_09 |
| CTPC_extra_10 | varchar |  |  | SI | CTPC_extra_10 |
| CTPC_extra_11 | varchar |  |  | SI | CTPC_extra_11 |
| CTPC_extra_12 | varchar |  |  | SI | CTPC_extra_12 |
| CTPC_extra_13 | varchar |  |  | SI | CTPC_extra_13 |
| CTPC_extra_14 | varchar |  |  | SI | CTPC_extra_14 |
| CTPC_extra_15 | varchar |  |  | SI | CTPC_extra_15 |
| CTPC_extra_16 | varchar |  |  | SI | CTPC_extra_16 |
| CTPC_extra_17 | varchar |  |  | SI | CTPC_extra_17 |
| CTPC_extra_18 | varchar |  |  | SI | CTPC_extra_18 |
| CTPC_extra_19 | varchar |  |  | SI | CTPC_extra_19 |
| CTPC_extra_20 | varchar |  |  | SI | CTPC_extra_20 |
| CTPC_extra_21 | varchar |  |  | SI | CTPC_extra_21 |
| CTPC_extra_22 | varchar |  |  | SI | CTPC_extra_22 |
| CTPC_extra_23 | varchar |  |  | SI | CTPC_extra_23 |
| CTPC_extra_24 | varchar |  |  | SI | CTPC_extra_24 |
| CTPC_extra_25 | varchar |  |  | SI | CTPC_extra_25 |
| CTPC_extra_26 | varchar |  |  | SI | CTPC_extra_26 |
| CTPC_extra_27 | varchar |  |  | SI | CTPC_extra_27 |
| CTPC_extra_28 | varchar |  |  | SI | CTPC_extra_28 |
| CTPC_extra_29 | varchar |  |  | SI | CTPC_extra_29 |
| CTPC_extra_30 | varchar |  |  | SI | CTPC_extra_30 |
| CTPC_ref_DVA | varchar |  |  | SI | ref DVA |
| CTPC_ref_FinancialClass | varchar |  |  | SI | ref Financial Class |
| CTPC_ref_FundNumber | varchar |  |  | SI | ref Fund Number |
| CTPC_ref_FundTable | varchar |  |  | SI | ref Fund Table |
| CTPC_ref_Medicare | varchar |  |  | SI | ref Medicare |
| CTPC_ref_MedicareRef | varchar |  |  | SI | ref Medicare Ref |
| CTPC_ref_Pensioner | varchar |  |  | SI | ref Pensioner |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*