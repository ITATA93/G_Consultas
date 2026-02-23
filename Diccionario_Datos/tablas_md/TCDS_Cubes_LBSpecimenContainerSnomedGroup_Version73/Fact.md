# TCDS_Cubes_LBSpecimenContainerSnomedGroup_Version73.Fact

**Schema:** TCDS_Cubes_LBSpecimenContainerSnomedGroup_Version73
**Columnas:** 13
**Actualizado:** 2026-01-30 15:30:50

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1733116764 | bigint |  |  | SI | Dimension: Dx1733116764<br/>
Source: LBSCSGSnomed... |
| Dx2315919167 | bigint |  |  | SI | Dimension: Dx2315919167<br/>
Source: LBSCSGSnomed... |
| Dx2384347825 | bigint |  |  | SI | Dimension: Dx2384347825<br/>
Source: LBSCSGSnomed... |
| Dx2394269396 | bigint |  |  | SI | Dimension: Dx2394269396
Expression: %expression.G... |
| Dx2451900763 | bigint |  |  | SI | Dimension: Dx2451900763<br/>
Source: LBSCSGSnomed... |
| Dx3505746236 | bigint |  |  | SI | Dimension: Dx3505746236<br/>
Source: LBSCSGSnomed... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBSCSGPa... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBSCSGPa... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBSCSGPa... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBSCSGParR... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*