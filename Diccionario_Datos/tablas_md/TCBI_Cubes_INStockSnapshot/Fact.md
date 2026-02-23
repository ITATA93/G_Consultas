# TCBI_Cubes_INStockSnapshot.Fact

**Schema:** TCBI_Cubes_INStockSnapshot
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx171623317 | varchar |  |  | SI | Dimension: Dx171623317<br/>
Source: STKSNAPPeriod |
| Dx3250635531 | varchar |  |  | SI | Dimension: Dx3250635531<br/>
Source: STKSNAPPerio... |
| Dx383182036 | varchar |  |  | SI | Dimension: Dx383182036<br/>
Source: STKSNAPPeriod |
| Dx3872596422 | varchar |  |  | SI | Dimension: Dx3872596422<br/>
Source: STKSNAPPerio... |
| Dx3874204838 | varchar |  |  | SI | Dimension: Dx3874204838<br/>
Source: STKSNAPDate |
| DxBaseUoM | bigint |  |  | SI | Dimension: DxBaseUoM<br/>
Source: STKSNAPBaseUOMD... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: STKSNAPHospita... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: STKSNAPLocatio... |
| DxPharmacologicalCategory | bigint |  |  | SI | Dimension: DxPharmacologicalCategory<br/>
Source:... |
| DxPharmacologicalSubCategory | bigint |  |  | SI | Dimension: DxPharmacologicalSubCategory<br/>
Sour... |
| DxPurchaseUoM | bigint |  |  | SI | Dimension: DxPurchaseUoM<br/>
Source: STKSNAPPurc... |
| DxReportingPeriodDayOfWeek | bigint |  |  | SI | Dimension: DxReportingPeriodDayOfWeek
Expression:... |
| DxSTKSNAPDate | date |  |  | SI | Dimension: DxSTKSNAPDate<br/>
Source: STKSNAPDate |
| DxSTKSNAPDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxSTKSNAPDateFxDayMonthYear<br/>
Sourc... |
| DxSTKSNAPDateFxMonthNumber | varchar |  |  | SI | Dimension: DxSTKSNAPDateFxMonthNumber<br/>
Source... |
| DxSTKSNAPDateFxMonthYear | varchar |  |  | SI | Dimension: DxSTKSNAPDateFxMonthYear<br/>
Source: ... |
| DxSTKSNAPDateFxQuarterYear | varchar |  |  | SI | Dimension: DxSTKSNAPDateFxQuarterYear<br/>
Source... |
| DxSTKSNAPDateFxYear | varchar |  |  | SI | Dimension: DxSTKSNAPDateFxYear<br/>
Source: STKSN... |
| DxSTKSNAPPeriod | date |  |  | SI | Dimension: DxSTKSNAPPeriod<br/>
Source: STKSNAPPe... |
| DxSTKSNAPPeriodFxMonthYear | varchar |  |  | SI | Dimension: DxSTKSNAPPeriodFxMonthYear<br/>
Source... |
| DxSTKSNAPPeriodFxYear | varchar |  |  | SI | Dimension: DxSTKSNAPPeriodFxYear<br/>
Source: STK... |
| DxServiceTaxRate | bigint |  |  | SI | Dimension: DxServiceTaxRate<br/>
Source: STKSNAPS... |
| DxSnapshotDayOfWeek | bigint |  |  | SI | Dimension: DxSnapshotDayOfWeek
Expression: $syste... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: STKSNAPItemDR.INC... |
| DxStockCategory | bigint |  |  | SI | Dimension: DxStockCategory<br/>
Source: STKSNAPIt... |
| DxStockCode | bigint |  |  | SI | Dimension: DxStockCode<br/>
Source: STKSNAPItemDR... |
| DxStockID | bigint |  |  | SI | Dimension: DxStockID<br/>
Source: STKSNAPItemDR |
| MxCost | double |  |  | SI | Measure: MxCost
Expression: %source.STKSNAPLogQty... |
| MxLogicalQuantity | double |  |  | SI | Measure: MxLogicalQuantity<br/>
Source: STKSNAPLo... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*