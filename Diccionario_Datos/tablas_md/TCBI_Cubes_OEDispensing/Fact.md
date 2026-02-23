# TCBI_Cubes_OEDispensing.Fact

**Schema:** TCBI_Cubes_OEDispensing
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxBatchNumber | bigint |  |  | SI | Dimension: DxBatchNumber<br/>
Source: DSPINCLBDR.... |
| DxCollectedTimeRange | bigint |  |  | SI | Dimension: DxCollectedTimeRange
Expression: "sour... |
| DxDSPDate | date |  |  | SI | Dimension: DxDSPDate<br/>
Source: DSPDate |
| DxDSPDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxDSPDateFxDayMonthYear<br/>
Source: D... |
| DxDSPDateFxMonthNumber | varchar |  |  | SI | Dimension: DxDSPDateFxMonthNumber<br/>
Source: DS... |
| DxDSPDateFxMonthYear | varchar |  |  | SI | Dimension: DxDSPDateFxMonthYear<br/>
Source: DSPD... |
| DxDSPDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxDSPDateFxQuarterNumber<br/>
Source: ... |
| DxDSPDateFxQuarterYear | varchar |  |  | SI | Dimension: DxDSPDateFxQuarterYear<br/>
Source: DS... |
| DxDSPDateFxYear | varchar |  |  | SI | Dimension: DxDSPDateFxYear<br/>
Source: DSPDate |
| DxDispensingQuantity | bigint |  |  | SI | Dimension: DxDispensingQuantity<br/>
Source: DSPQ... |
| DxDispensingStatus | bigint |  |  | SI | Dimension: DxDispensingStatus
Expression: %expres... |
| DxDispensingTimeRange | bigint |  |  | SI | Dimension: DxDispensingTimeRange
Expression: "sou... |
| DxDispensingUser | bigint |  |  | SI | Dimension: DxDispensingUser<br/>
Source: DSPSSUSR... |
| DxStockBatches | varchar |  |  | SI | Dimension: DxStockBatches
Expression: %cube.GetBa... |
| MxDispQty | double |  |  | SI | Measure: MxDispQty
Expression: %source.DSPQty |
| Rx1870573481 | bigint |  |  | SI | Relationship: Rx1870573481<br/>
Source: DSPOEOREP... |
| RxIDViaDSPINCLBDR | bigint |  | FK | SI | Relationship: RxIDViaDSPINCLBDR<br/>
Source: DSPI... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*