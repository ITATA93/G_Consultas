# TCBI_Cubes_PAAdmInsurance.Fact

**Schema:** TCBI_Cubes_PAAdmInsurance
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxHasPackage | bigint |  |  | SI | Dimension: DxHasPackage
Expression: %cube.HasPack... |
| DxPackageNumber | bigint |  |  | SI | Dimension: DxPackageNumber<br/>
Source: INSPerson... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: INSParRef.PAA... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: INSInsTypeDR.INST... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: INSAuxInsTypeDR.AU... |
| RxIDViaINSParRef | bigint |  |  | SI | Relationship: RxIDViaINSParRef<br/>
Source: INSPa... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*