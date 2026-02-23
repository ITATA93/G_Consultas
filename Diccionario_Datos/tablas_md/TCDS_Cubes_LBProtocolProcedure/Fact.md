# TCDS_Cubes_LBProtocolProcedure.Fact

**Schema:** TCDS_Cubes_LBProtocolProcedure
**Columnas:** 25
**Actualizado:** 2026-01-30 15:30:39

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1569480271 | bigint |  |  | SI | Dimension: Dx1569480271<br/>
Source: LBPTPFrozenS... |
| Dx1579843252 | bigint |  |  | SI | Dimension: Dx1579843252<br/>
Source: LBPTPSourceD... |
| Dx1583498262 | bigint |  |  | SI | Dimension: Dx1583498262<br/>
Source: LBPTPReporti... |
| Dx2181335292 | bigint |  |  | SI | Dimension: Dx2181335292<br/>
Source: LBPTPMicrosc... |
| Dx2499937908 | bigint |  |  | SI | Dimension: Dx2499937908<br/>
Source: LBPTPCutUpBy... |
| Dx2607439592 | bigint |  |  | SI | Dimension: Dx2607439592<br/>
Source: LBPTPPlatedB... |
| Dx2769701361 | bigint |  |  | SI | Dimension: Dx2769701361<br/>
Source: LBPTPMacrosc... |
| Dx2825650052 | bigint |  |  | SI | Dimension: Dx2825650052<br/>
Source: LBPTPComplet... |
| Dx2953264526 | bigint |  |  | SI | Dimension: Dx2953264526<br/>
Source: LBPTPProcedu... |
| Dx2958562682 | bigint |  |  | SI | Dimension: Dx2958562682<br/>
Source: LBPTPMacrosc... |
| Dx296127383 | bigint |  |  | SI | Dimension: Dx296127383<br/>
Source: LBPTPAddOnByD... |
| Dx3111607030 | bigint |  |  | SI | Dimension: Dx3111607030
Expression: %expression.S... |
| Dx3905750896 | bigint |  |  | SI | Dimension: Dx3905750896<br/>
Source: LBPTPFrozenS... |
| Dx3921435071 | bigint |  |  | SI | Dimension: Dx3921435071<br/>
Source: LBPTPIndicat... |
| Dx3939947831 | bigint |  |  | SI | Dimension: Dx3939947831<br/>
Source: LBPTPEmbeddi... |
| Dx39672757 | bigint |  |  | SI | Dimension: Dx39672757<br/>
Source: LBPTPProcedure... |
| Dx4056755650 | bigint |  |  | SI | Dimension: Dx4056755650<br/>
Source: LBPTPSupervi... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBPTPPar... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBPTPPar... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBPTPPar... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBPTPParRe... |
| DxLBPTPTurnaroundTimeFlag | bigint |  |  | SI | Dimension: DxLBPTPTurnaroundTimeFlag<br/>
Source:... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*