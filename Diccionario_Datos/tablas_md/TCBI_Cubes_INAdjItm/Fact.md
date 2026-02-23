# TCBI_Cubes_INAdjItm.Fact

**Schema:** TCBI_Cubes_INAdjItm
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
| Dx1968727886 | date |  |  | SI | Dimension: Dx1968727886<br/>
Source: INADIINADPar... |
| Dx203620486 | varchar |  |  | SI | Dimension: Dx203620486<br/>
Source: INADIINADParR... |
| Dx2456730825 | varchar |  |  | SI | Dimension: Dx2456730825<br/>
Source: INADIINADPar... |
| Dx2722240394 | varchar |  |  | SI | Dimension: Dx2722240394<br/>
Source: INADIINADPar... |
| Dx3561088999 | varchar |  |  | SI | Dimension: Dx3561088999<br/>
Source: INADIINADPar... |
| Dx3646336382 | varchar |  |  | SI | Dimension: Dx3646336382<br/>
Source: INADIINADPar... |
| Dx3771392725 | varchar |  |  | SI | Dimension: Dx3771392725<br/>
Source: INADIINADPar... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: INADICTLOCDR.C... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: INADICTLOCDR.C... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: INADIINCLBDR.INCL... |
| MxCost | double |  |  | SI | Measure: MxCost
Expression: %source.INADIQty * %s... |
| MxMinusAdjustment | double |  |  | SI | Measure: MxMinusAdjustment
Expression: $SELECT(%s... |
| MxPlusAdjustment | double |  |  | SI | Measure: MxPlusAdjustment
Expression: $SELECT(%so... |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: INADIQty |
| RxIDViaINADIINCLBDR | bigint |  | FK | SI | Relationship: RxIDViaINADIINCLBDR<br/>
Source: IN... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*