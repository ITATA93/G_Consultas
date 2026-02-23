# TCDS_Cubes_LBProtocolMaterialSnomedGroup_Version73.Fact

**Schema:** TCDS_Cubes_LBProtocolMaterialSnomedGroup_Version73
**Columnas:** 13
**Actualizado:** 2026-01-30 15:30:35

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1252388406 | bigint |  |  | SI | Dimension: Dx1252388406<br/>
Source: LBPMSGSnomed... |
| Dx1320268728 | bigint |  |  | SI | Dimension: Dx1320268728<br/>
Source: LBPMSGSnomed... |
| Dx1453237724 | bigint |  |  | SI | Dimension: Dx1453237724<br/>
Source: LBPMSGSnomed... |
| Dx2394269396 | bigint |  |  | SI | Dimension: Dx2394269396
Expression: %expression.G... |
| Dx2750869467 | bigint |  |  | SI | Dimension: Dx2750869467<br/>
Source: LBPMSGSnomed... |
| Dx340712891 | bigint |  |  | SI | Dimension: Dx340712891<br/>
Source: LBPMSGSnomedT... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBPMSGPa... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBPMSGPa... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBPMSGPa... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBPMSGParR... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*