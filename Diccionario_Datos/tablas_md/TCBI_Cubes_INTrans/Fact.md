# TCBI_Cubes_INTrans.Fact

**Schema:** TCBI_Cubes_INTrans
**Columnas:** 48
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1035805655 | varchar |  |  | SI | Dimension: Dx1035805655<br/>
Source: INTRINCLBDR.... |
| Dx1491270006 | varchar |  |  | SI | Dimension: Dx1491270006<br/>
Source: INTRINCLBDR.... |
| Dx1960805314 | varchar |  |  | SI | Dimension: Dx1960805314<br/>
Source: INTRINCLBDR.... |
| Dx3033938004 | varchar |  |  | SI | Dimension: Dx3033938004<br/>
Source: INTRINCLBDR.... |
| Dx3584512559 | varchar |  |  | SI | Dimension: Dx3584512559<br/>
Source: INTRINCLBDR.... |
| Dx4045942836 | date |  |  | SI | Dimension: Dx4045942836<br/>
Source: INTRINCLBDR.... |
| Dx961458300 | varchar |  |  | SI | Dimension: Dx961458300<br/>
Source: INTRINCLBDR.I... |
| DxBaseUoM | bigint |  |  | SI | Dimension: DxBaseUoM<br/>
Source: INTRINCIDR.INCI... |
| DxDrugRegister | bigint |  |  | SI | Dimension: DxDrugRegister
Expression: %expression... |
| DxExpiryRange | bigint |  |  | SI | Dimension: DxExpiryRange
Expression: %source.INTR... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INTRCTLOCDR.CT... |
| DxINTRDate | date |  |  | SI | Dimension: DxINTRDate<br/>
Source: INTRDate |
| DxINTRDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxINTRDateFxDayMonthYear<br/>
Source: ... |
| DxINTRDateFxMonthNumber | varchar |  |  | SI | Dimension: DxINTRDateFxMonthNumber<br/>
Source: I... |
| DxINTRDateFxMonthYear | varchar |  |  | SI | Dimension: DxINTRDateFxMonthYear<br/>
Source: INT... |
| DxINTRDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxINTRDateFxQuarterNumber<br/>
Source:... |
| DxINTRDateFxQuarterYear | varchar |  |  | SI | Dimension: DxINTRDateFxQuarterYear<br/>
Source: I... |
| DxINTRDateFxYear | varchar |  |  | SI | Dimension: DxINTRDateFxYear<br/>
Source: INTRDate |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INTRCTLOCDR.CT... |
| DxOfficialCode | bigint |  |  | SI | Dimension: DxOfficialCode<br/>
Source: INTRINCIDR... |
| DxPharmacologicalCategory | bigint |  |  | SI | Dimension: DxPharmacologicalCategory<br/>
Source:... |
| DxPharmacologicalSubCategory | bigint |  |  | SI | Dimension: DxPharmacologicalSubCategory<br/>
Sour... |
| DxScheduledDrugClass | bigint |  |  | SI | Dimension: DxScheduledDrugClass<br/>
Source: INTR... |
| DxServiceTaxRate | bigint |  |  | SI | Dimension: DxServiceTaxRate
Expression: $LG(%expr... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: INTRINCIDR.INCIDe... |
| DxStockCategory | bigint |  |  | SI | Dimension: DxStockCategory<br/>
Source: INTRINCID... |
| DxStockTakeGroup | bigint |  |  | SI | Dimension: DxStockTakeGroup<br/>
Source: INTRINCI... |
| DxTransactionHospital | bigint |  |  | SI | Dimension: DxTransactionHospital
Expression: %cub... |
| DxTransactionLocation | bigint |  |  | SI | Dimension: DxTransactionLocation
Expression: %cub... |
| DxTransactionType | bigint |  |  | SI | Dimension: DxTransactionType<br/>
Source: INTRTyp... |
| MxAmount | double |  |  | SI | Measure: MxAmount
Expression: %source.INTRAmount |
| MxCost | double |  |  | SI | Measure: MxCost
Expression: %source.INTRINCLBDR.I... |
| MxMinusAdjustment | double |  |  | SI | Measure: MxMinusAdjustment
Expression: $SELECT(%s... |
| MxPhysicalQuantity | double |  |  | SI | Measure: MxPhysicalQuantity<br/>
Source: INTRINCL... |
| MxPlusAdjustment | double |  |  | SI | Measure: MxPlusAdjustment
Expression: $SELECT(%so... |
| MxTransQuantity | double |  |  | SI | Measure: MxTransQuantity<br/>
Source: INTRQty |
| MxTransQuantityBaseUoM | double |  |  | SI | Measure: MxTransQuantityBaseUoM
Expression: %cube... |
| Rx1197743457 | bigint |  |  | SI | Relationship: Rx1197743457
Expression: %cube.GetR... |
| Rx2234043310 | bigint |  |  | SI | Relationship: Rx2234043310
Expression: %cube.GetR... |
| Rx2388589624 | bigint |  |  | SI | Relationship: Rx2388589624
Expression: %cube.GetR... |
| Rx2398398295 | bigint |  |  | SI | Relationship: Rx2398398295
Expression: %cube.GetR... |
| Rx2588605434 | bigint |  |  | SI | Relationship: Rx2588605434
Expression: %cube.GetR... |
| Rx3377865401 | bigint |  |  | SI | Relationship: Rx3377865401
Expression: %cube.GetR... |
| Rx847543140 | bigint |  |  | SI | Relationship: Rx847543140
Expression: %cube.GetRe... |
| RxIDViaINTRINCLBDR | bigint |  | FK | SI | Relationship: RxIDViaINTRINCLBDR<br/>
Source: INT... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*