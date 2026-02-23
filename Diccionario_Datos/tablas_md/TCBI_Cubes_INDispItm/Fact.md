# TCBI_Cubes_INDispItm.Fact

**Schema:** TCBI_Cubes_INDispItm
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx110017068 | varchar |  |  | SI | Dimension: Dx110017068<br/>
Source: INDSIINDSParR... |
| Dx1693942620 | varchar |  |  | SI | Dimension: Dx1693942620<br/>
Source: INDSIINDSPar... |
| Dx1703319952 | date |  |  | SI | Dimension: Dx1703319952<br/>
Source: INDSIINDSPar... |
| Dx1924587899 | varchar |  |  | SI | Dimension: Dx1924587899<br/>
Source: INDSIINDSPar... |
| Dx2283692303 | varchar |  |  | SI | Dimension: Dx2283692303<br/>
Source: INDSIINDSPar... |
| Dx3704312775 | varchar |  |  | SI | Dimension: Dx3704312775<br/>
Source: INDSIINDSPar... |
| Dx663958512 | varchar |  |  | SI | Dimension: Dx663958512<br/>
Source: INDSIINDSParR... |
| DxAdjustmentReason | bigint |  |  | SI | Dimension: DxAdjustmentReason<br/>
Source: INDSII... |
| DxConsumptionReason | bigint |  |  | SI | Dimension: DxConsumptionReason<br/>
Source: INDSI... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INDSIINCLBDR.I... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INDSIINCLBDR.I... |
| DxType | bigint |  |  | SI | Dimension: DxType<br/>
Source: INDSIINDSParRef.IN... |
| MxCost | double |  |  | SI | Measure: MxCost
Expression: %source.INDSIQty * %s... |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: INDSIQty |
| RxIDViaINDSIINCLBDR | bigint |  | FK | SI | Relationship: RxIDViaINDSIINCLBDR<br/>
Source: IN... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*