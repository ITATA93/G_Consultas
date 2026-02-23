# TCBI_Cubes_INGdRetItm.Fact

**Schema:** TCBI_Cubes_INGdRetItm
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1591056850 | varchar |  |  | SI | Dimension: Dx1591056850<br/>
Source: INGRDINGRRPa... |
| Dx2959297760 | date |  |  | SI | Dimension: Dx2959297760<br/>
Source: INGRDINGRRPa... |
| Dx4115068620 | varchar |  |  | SI | Dimension: Dx4115068620<br/>
Source: INGRDINGRRPa... |
| Dx4128282653 | varchar |  |  | SI | Dimension: Dx4128282653<br/>
Source: INGRDINGRRPa... |
| Dx4229949694 | varchar |  |  | SI | Dimension: Dx4229949694<br/>
Source: INGRDINGRRPa... |
| Dx430904479 | varchar |  |  | SI | Dimension: Dx430904479<br/>
Source: INGRDINGRRPar... |
| Dx597196643 | varchar |  |  | SI | Dimension: Dx597196643<br/>
Source: INGRDINGRRPar... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INGRDINGRIDR.I... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INGRDINGRIDR.I... |
| DxReason | bigint |  |  | SI | Dimension: DxReason<br/>
Source: INGRDReasonRetur... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: INGRDINGRIDR.INGR... |
| DxVendor | bigint |  |  | SI | Dimension: DxVendor<br/>
Source: INGRDINGRIDR.ING... |
| MxAmount | double |  |  | SI | Measure: MxAmount<br/>
Source: INGRDAmount |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: INGRDQty |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*