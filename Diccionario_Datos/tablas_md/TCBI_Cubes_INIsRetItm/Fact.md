# TCBI_Cubes_INIsRetItm.Fact

**Schema:** TCBI_Cubes_INIsRetItm
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
| Dx1136218182 | varchar |  |  | SI | Dimension: Dx1136218182<br/>
Source: INIRIParRef.... |
| Dx155575337 | varchar |  |  | SI | Dimension: Dx155575337<br/>
Source: INIRIParRef.I... |
| Dx1969496189 | varchar |  |  | SI | Dimension: Dx1969496189<br/>
Source: INIRIParRef.... |
| Dx2844733898 | varchar |  |  | SI | Dimension: Dx2844733898<br/>
Source: INIRIParRef.... |
| Dx2941301269 | varchar |  |  | SI | Dimension: Dx2941301269<br/>
Source: INIRIParRef.... |
| Dx47439530 | varchar |  |  | SI | Dimension: Dx47439530<br/>
Source: INIRIParRef.IN... |
| DxCompleteStatus | bigint |  |  | SI | Dimension: DxCompleteStatus<br/>
Source: INIRIPar... |
| DxHospitalFrom | bigint |  |  | SI | Dimension: DxHospitalFrom<br/>
Source: INIRIParRe... |
| DxHospitalTo | bigint |  |  | SI | Dimension: DxHospitalTo<br/>
Source: INIRIParRef.... |
| DxINIRDateViaINIRIParRef | date |  |  | SI | Dimension: DxINIRDateViaINIRIParRef<br/>
Source: ... |
| DxLocationFrom | bigint |  |  | SI | Dimension: DxLocationFrom<br/>
Source: INIRIParRe... |
| DxLocationTo | bigint |  |  | SI | Dimension: DxLocationTo<br/>
Source: INIRIParRef.... |
| DxStock | bigint |  |  | SI | Dimension: DxStock<br/>
Source: INIRIIsItmDR.INIT... |
| MxPrice | double |  |  | SI | Measure: MxPrice
Expression: %source.INIRIQty * %... |
| MxQuantity | double |  |  | SI | Measure: MxQuantity<br/>
Source: INIRIQty |
| RxIDViaINIRIIsItmDR | bigint |  | FK | SI | Relationship: RxIDViaINIRIIsItmDR<br/>
Source: IN... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*