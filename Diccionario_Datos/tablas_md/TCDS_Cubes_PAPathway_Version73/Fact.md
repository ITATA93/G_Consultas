# TCDS_Cubes_PAPathway_Version73.Fact

**Schema:** TCDS_Cubes_PAPathway_Version73
**Columnas:** 16
**Actualizado:** 2026-01-30 15:31:40

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DXPathStatus | bigint |  |  | SI | Dimension: DXPathStatus<br/>
Source: PATHStatus |
| Dx1240578541 | bigint |  |  | SI | Dimension: Dx1240578541<br/>
Source: PATHBaseProt... |
| Dx1915940710 | date |  |  | SI | Dimension: Dx1915940710<br/>
Source: PATHBaseProt... |
| Dx2103754167 | varchar |  |  | SI | Dimension: Dx2103754167<br/>
Source: PATHBaseProt... |
| Dx2236264347 | bigint |  |  | SI | Dimension: Dx2236264347<br/>
Source: PATHBaseProt... |
| Dx3242102214 | bigint |  |  | SI | Dimension: Dx3242102214
Expression: %expression.G... |
| Dx656888017 | varchar |  |  | SI | Dimension: Dx656888017<br/>
Source: PATHPlannedSt... |
| DxCLPODescViaPATHOutcomeDR | bigint |  | FK | SI | Dimension: DxCLPODescViaPATHOutcomeDR<br/>
Source... |
| DxCLPTDescViaPATHCPWTypeDR | bigint |  | FK | SI | Dimension: DxCLPTDescViaPATHCPWTypeDR<br/>
Source... |
| DxDSSEffectiveDate | varchar |  |  | SI | Dimension: DxDSSEffectiveDate<br/>
Source: PATHCr... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: PATHParRef... |
| DxPATHCreateDate | date |  |  | SI | Dimension: DxPATHCreateDate<br/>
Source: PATHCrea... |
| DxPATHPlannedStartDate | date |  |  | SI | Dimension: DxPATHPlannedStartDate<br/>
Source: PA... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*