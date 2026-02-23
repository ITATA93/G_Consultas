# TCBI_Cubes_INPOItm.Fact

**Schema:** TCBI_Cubes_INPOItm
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1393426998 | varchar |  |  | SI | Dimension: Dx1393426998<br/>
Source: INPO.INPODat... |
| Dx226514104 | varchar |  |  | SI | Dimension: Dx226514104<br/>
Source: INPO.INPODate |
| Dx2407635129 | varchar |  |  | SI | Dimension: Dx2407635129<br/>
Source: INPO.INPODat... |
| Dx3781801707 | varchar |  |  | SI | Dimension: Dx3781801707<br/>
Source: INPO.INPODat... |
| Dx4138730671 | varchar |  |  | SI | Dimension: Dx4138730671<br/>
Source: INPO.INPODat... |
| DxApprovedStatus | bigint |  |  | SI | Dimension: DxApprovedStatus<br/>
Source: INPO.INP... |
| DxCancelFulfillReason | bigint |  |  | SI | Dimension: DxCancelFulfillReason<br/>
Source: INP... |
| DxCancelledStatus | bigint |  |  | SI | Dimension: DxCancelledStatus<br/>
Source: INPO.IN... |
| DxCompletedStatus | bigint |  |  | SI | Dimension: DxCompletedStatus
Expression: %cube.Ge... |
| DxFulfilledStatus | bigint |  |  | SI | Dimension: DxFulfilledStatus<br/>
Source: INPO.IN... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INPO.INPOHospi... |
| DxINPODateViaINPO | date |  |  | SI | Dimension: DxINPODateViaINPO<br/>
Source: INPO.IN... |
| DxINPODateViaINPOFxYear | varchar |  |  | SI | Dimension: DxINPODateViaINPOFxYear<br/>
Source: I... |
| DxItem | bigint |  |  | SI | Dimension: DxItem<br/>
Source: INPOIINCIDR.INCIDe... |
| DxItemCode | bigint |  |  | SI | Dimension: DxItemCode<br/>
Source: INPOIINCIDR.IN... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INPOICTLOCDR.C... |
| DxPurchaseOrderDayOfWeek | bigint |  |  | SI | Dimension: DxPurchaseOrderDayOfWeek
Expression: $... |
| DxUserCompletedStatus | bigint |  |  | SI | Dimension: DxUserCompletedStatus<br/>
Source: INP... |
| DxVendor | bigint |  |  | SI | Dimension: DxVendor<br/>
Source: INPO.INPOAPCVMDR... |
| MxQuantityOutstanding | double |  |  | SI | Measure: MxQuantityOutstanding<br/>
Source: INPOI... |
| MxQuantityPurchased | double |  |  | SI | Measure: MxQuantityPurchased<br/>
Source: INPOIPu... |
| MxQuantityReceived | double |  |  | SI | Measure: MxQuantityReceived
Expression: %cube.Rec... |
| MxQuantityRequested | double |  |  | SI | Measure: MxQuantityRequested<br/>
Source: INPOIRe... |
| MxQuantityReturned | double |  |  | SI | Measure: MxQuantityReturned
Expression: %cube.Ret... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*