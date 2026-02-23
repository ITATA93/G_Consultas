# TCBI_Cubes_INGdRecItm.Fact

**Schema:** TCBI_Cubes_INGdRecItm
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1040558073 | varchar |  |  | SI | Dimension: Dx1040558073<br/>
Source: INGRIExpDate |
| Dx128659307 | varchar |  |  | SI | Dimension: Dx128659307<br/>
Source: INGRIINGRParR... |
| Dx246042281 | varchar |  |  | SI | Dimension: Dx246042281<br/>
Source: INGRIINGRParR... |
| Dx2826761882 | date |  |  | SI | Dimension: Dx2826761882<br/>
Source: INGRIINGRPar... |
| Dx3705169421 | varchar |  |  | SI | Dimension: Dx3705169421<br/>
Source: INGRIExpDate |
| Dx379479021 | varchar |  |  | SI | Dimension: Dx379479021<br/>
Source: INGRIINGRParR... |
| Dx3796086010 | varchar |  |  | SI | Dimension: Dx3796086010<br/>
Source: INGRIINGRPar... |
| Dx557466105 | varchar |  |  | SI | Dimension: Dx557466105<br/>
Source: INGRIINGRParR... |
| Dx968689886 | varchar |  |  | SI | Dimension: Dx968689886<br/>
Source: INGRIINGRParR... |
| DxExpiryRange | bigint |  |  | SI | Dimension: DxExpiryRange
Expression: %source.INGR... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INGRICTLOCDR.C... |
| DxINGRIExpDate | date |  |  | SI | Dimension: DxINGRIExpDate<br/>
Source: INGRIExpDa... |
| DxINGRIExpDateFxMonthNumber | varchar |  |  | SI | Dimension: DxINGRIExpDateFxMonthNumber<br/>
Sourc... |
| DxINGRIExpDateFxMonthYear | varchar |  |  | SI | Dimension: DxINGRIExpDateFxMonthYear<br/>
Source:... |
| DxINGRIExpDateFxQuarterYear | varchar |  |  | SI | Dimension: DxINGRIExpDateFxQuarterYear<br/>
Sourc... |
| DxINGRIExpDateFxYear | varchar |  |  | SI | Dimension: DxINGRIExpDateFxYear<br/>
Source: INGR... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INGRICTLOCDR.C... |
| DxServiceTax | bigint |  |  | SI | Dimension: DxServiceTax<br/>
Source: INGRIService... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: INGRIStkDesc |
| DxStockType | bigint |  |  | SI | Dimension: DxStockType<br/>
Source: INGRIINCGRDR.... |
| DxVendor | bigint |  |  | SI | Dimension: DxVendor<br/>
Source: INGRIINGRParRef.... |
| MxCost | double |  |  | SI | Measure: MxCost
Expression: %source.INGRIRecQty *... |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: INGRIRecQty |
| MxTaxAmount | double |  |  | SI | Measure: MxTaxAmount<br/>
Source: INGRITaxAmount |
| RxIDViaINGRIINCLBDR | bigint |  | FK | SI | Relationship: RxIDViaINGRIINCLBDR<br/>
Source: IN... |
| RxIDViaINGRIINPOIDR | bigint |  | FK | SI | Relationship: RxIDViaINGRIINPOIDR<br/>
Source: IN... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*