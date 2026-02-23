# TCDS_Cubes_LBSpecimenContainerComment.Fact

**Schema:** TCDS_Cubes_LBSpecimenContainerComment
**Columnas:** 9
**Actualizado:** 2026-01-30 15:30:47

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx3085791378 | bigint |  |  | SI | Dimension: Dx3085791378<br/>
Source: LBSPCCParRef... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBSPCCPa... |
| DxDSSLBTestSetID | varchar |  |  | SI | Dimension: DxDSSLBTestSetID
Expression: %expressi... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBSPCCParR... |
| DxSpecimenComment | bigint |  |  | SI | Dimension: DxSpecimenComment<br/>
Source: LBSPCCS... |
| DxSpecimenCommentGroup | bigint |  |  | SI | Dimension: DxSpecimenCommentGroup<br/>
Source: LB... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*