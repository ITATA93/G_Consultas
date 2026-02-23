# TCDS_Cubes_LBTestSetSnomedGroup.Fact

**Schema:** TCDS_Cubes_LBTestSetSnomedGroup
**Columnas:** 13
**Actualizado:** 2026-01-30 15:31:01

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1768822278 | bigint |  |  | SI | Dimension: Dx1768822278<br/>
Source: LBTSSGSnomed... |
| Dx3738575974 | bigint |  |  | SI | Dimension: Dx3738575974<br/>
Source: LBTSSGSnomed... |
| Dx733900385 | bigint |  |  | SI | Dimension: Dx733900385<br/>
Source: LBTSSGSnomedT... |
| Dx865171461 | bigint |  |  | SI | Dimension: Dx865171461<br/>
Source: LBTSSGSnomedT... |
| Dx931472779 | bigint |  |  | SI | Dimension: Dx931472779<br/>
Source: LBTSSGSnomedT... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBTSSGPa... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBTSSGPa... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBTSSGPa... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBTSSGParR... |
| DxSNOCFullID | bigint |  |  | SI | Dimension: DxSNOCFullID
Expression: %expression.G... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*