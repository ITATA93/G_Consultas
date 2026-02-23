# TCBI_Cubes_INIsTrfItm.Fact

**Schema:** TCBI_Cubes_INIsTrfItm
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
| Dx1141335126 | date |  |  | SI | Dimension: Dx1141335126<br/>
Source: INITIINITPar... |
| Dx3350513419 | varchar |  |  | SI | Dimension: Dx3350513419<br/>
Source: INITIINITPar... |
| Dx3486491694 | varchar |  |  | SI | Dimension: Dx3486491694<br/>
Source: INITIINITPar... |
| Dx354911606 | varchar |  |  | SI | Dimension: Dx354911606<br/>
Source: INITIINITParR... |
| Dx3712263164 | varchar |  |  | SI | Dimension: Dx3712263164<br/>
Source: INITIINITPar... |
| Dx4106156470 | varchar |  |  | SI | Dimension: Dx4106156470<br/>
Source: INITIINITPar... |
| Dx4191053605 | varchar |  |  | SI | Dimension: Dx4191053605<br/>
Source: INITIINITPar... |
| DxReplenishLocation | bigint |  |  | SI | Dimension: DxReplenishLocation<br/>
Source: INITI... |
| DxRequestingLocation | bigint |  |  | SI | Dimension: DxRequestingLocation<br/>
Source: INIT... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: INITIINCLBDR.INCL... |
| DxType | bigint |  |  | SI | Dimension: DxType<br/>
Source: INITIType |
| MxCost | double |  |  | SI | Measure: MxCost
Expression: %source.INITIQty * %s... |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: INITIQty |
| RxIDViaINITIINCLBDR | bigint |  | FK | SI | Relationship: RxIDViaINITIINCLBDR<br/>
Source: IN... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*