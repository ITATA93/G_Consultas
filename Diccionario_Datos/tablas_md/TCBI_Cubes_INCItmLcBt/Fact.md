# TCBI_Cubes_INCItmLcBt.Fact

**Schema:** TCBI_Cubes_INCItmLcBt
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1073726963 | date |  |  | SI | Dimension: Dx1073726963<br/>
Source: INCLBINCIBDR... |
| Dx1190174865 | varchar |  |  | SI | Dimension: Dx1190174865<br/>
Source: INCLBINCIBDR... |
| Dx3320207542 | varchar |  |  | SI | Dimension: Dx3320207542<br/>
Source: INCLBINCIBDR... |
| Dx3341176912 | varchar |  |  | SI | Dimension: Dx3341176912<br/>
Source: INCLBINCIBDR... |
| Dx3580575631 | varchar |  |  | SI | Dimension: Dx3580575631<br/>
Source: INCLBINCIBDR... |
| Dx3629402249 | varchar |  |  | SI | Dimension: Dx3629402249<br/>
Source: INCLBINCIBDR... |
| DxBatch | bigint |  |  | SI | Dimension: DxBatch<br/>
Source: INCLBINCIBDR.INCI... |
| DxExpiryRange | bigint |  |  | SI | Dimension: DxExpiryRange
Expression: %source.INCL... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INCLBINCILParR... |
| DxIssueTransferFlag | bigint |  |  | SI | Dimension: DxIssueTransferFlag<br/>
Source: INCLB... |
| DxItem | bigint |  |  | SI | Dimension: DxItem<br/>
Source: INCLBINCILParRef.I... |
| DxItemCode | bigint |  |  | SI | Dimension: DxItemCode<br/>
Source: INCLBINCILParR... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INCLBINCILParR... |
| DxWardStock | bigint |  |  | SI | Dimension: DxWardStock<br/>
Source: INCLBINCIBDR.... |
| MxAmount | double |  |  | SI | Measure: MxAmount
Expression: %source.INCLBPhyQty... |
| MxPhysicalQuantity | double |  |  | SI | Measure: MxPhysicalQuantity<br/>
Source: INCLBPhy... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*