# TCBI_Cubes_ARPatBillGroupCharges.Fact

**Schema:** TCBI_Cubes_ARPatBillGroupCharges
**Columnas:** 40
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxBillID | bigint |  |  | SI | Dimension: DxBillID<br/>
Source: ITMParRef.BGRPPa... |
| DxClaimStatus | bigint |  |  | SI | Dimension: DxClaimStatus<br/>
Source: ITMActivBil... |
| DxDenialReason | bigint |  |  | SI | Dimension: DxDenialReason<br/>
Source: ITMReasonA... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: ITMDepartDR.... |
| DxEpisodeID | bigint |  |  | SI | Dimension: DxEpisodeID<br/>
Source: ITMParRef.BGR... |
| DxITMDate | date |  |  | SI | Dimension: DxITMDate<br/>
Source: ITMDate |
| DxITMDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxITMDateFxDayMonthYear<br/>
Source: I... |
| DxITMDateFxMonthNumber | varchar |  |  | SI | Dimension: DxITMDateFxMonthNumber<br/>
Source: IT... |
| DxITMDateFxMonthYear | varchar |  |  | SI | Dimension: DxITMDateFxMonthYear<br/>
Source: ITMD... |
| DxITMDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxITMDateFxQuarterNumber<br/>
Source: ... |
| DxITMDateFxQuarterYear | varchar |  |  | SI | Dimension: DxITMDateFxQuarterYear<br/>
Source: IT... |
| DxITMDateFxYear | varchar |  |  | SI | Dimension: DxITMDateFxYear<br/>
Source: ITMDate |
| DxItemDescription | bigint |  |  | SI | Dimension: DxItemDescription<br/>
Source: ITMARCI... |
| DxItemType | bigint |  |  | SI | Dimension: DxItemType<br/>
Source: ITMServiceMate... |
| DxOrderID | bigint |  |  | SI | Dimension: DxOrderID<br/>
Source: ITMOEORIDR.%ID |
| DxPackage | bigint |  |  | SI | Dimension: DxPackage<br/>
Source: ITMPersonPackag... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ITMParRef.BGR... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: ITMParRef.BGRPPar... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: ITMParRef.BGRPParR... |
| DxRoom | bigint |  |  | SI | Dimension: DxRoom<br/>
Source: ITMRoomDR.ROOMDesc |
| DxRoomType | bigint |  |  | SI | Dimension: DxRoomType<br/>
Source: ITMRoomTypeDR.... |
| DxWard | bigint |  |  | SI | Dimension: DxWard<br/>
Source: ITMWardDR.WARDDesc |
| MxAmountCoveredUnderPack | double |  |  | SI | Measure: MxAmountCoveredUnderPack<br/>
Source: IT... |
| MxDiscountBeforeTax | double |  |  | SI | Measure: MxDiscountBeforeTax<br/>
Source: ITMDisc... |
| MxNumberOfTimes | double |  |  | SI | Measure: MxNumberOfTimes<br/>
Source: ITMNoTimes |
| MxPatientShare | double |  |  | SI | Measure: MxPatientShare<br/>
Source: ITMPatientSh... |
| MxPayorApprovAmount | double |  |  | SI | Measure: MxPayorApprovAmount<br/>
Source: ITMActR... |
| MxPayorShare | double |  |  | SI | Measure: MxPayorShare<br/>
Source: ITMInsCompanyS... |
| MxPriceBeforeDiscBeforeTax | double |  |  | SI | Measure: MxPriceBeforeDiscBeforeTax<br/>
Source: ... |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: ITMDailyQty |
| MxTotalAmount | double |  |  | SI | Measure: MxTotalAmount<br/>
Source: ITMLineTotal |
| MxTotalTax | double |  |  | SI | Measure: MxTotalTax<br/>
Source: ITMMaterialTotal |
| MxTotalTaxAmount | double |  |  | SI | Measure: MxTotalTaxAmount<br/>
Source: ITMTotalTa... |
| MxUnitPrice | double |  |  | SI | Measure: MxUnitPrice<br/>
Source: ITMUnitPrice |
| Rx2935563378 | bigint |  |  | SI | Relationship: Rx2935563378<br/>
Source: ITMParRef... |
| Rx529158233 | bigint |  |  | SI | Relationship: Rx529158233<br/>
Source: ITMParRef.... |
| RxIDViaITMOEORIDR | bigint |  | FK | SI | Relationship: RxIDViaITMOEORIDR<br/>
Source: ITMO... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*