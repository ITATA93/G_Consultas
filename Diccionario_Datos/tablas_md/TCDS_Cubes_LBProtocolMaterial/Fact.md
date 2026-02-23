# TCDS_Cubes_LBProtocolMaterial.Fact

**Schema:** TCDS_Cubes_LBProtocolMaterial
**Columnas:** 14
**Actualizado:** 2026-01-30 15:30:32

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx2032382899 | bigint |  |  | SI | Dimension: Dx2032382899<br/>
Source: LBPTMComplet... |
| Dx3287712207 | bigint |  |  | SI | Dimension: Dx3287712207<br/>
Source: LBPTMAddOnBy... |
| Dx3304534130 | bigint |  |  | SI | Dimension: Dx3304534130<br/>
Source: LBPTMMateria... |
| Dx3359862286 | bigint |  |  | SI | Dimension: Dx3359862286<br/>
Source: LBPTMSourceD... |
| Dx597304267 | bigint |  |  | SI | Dimension: Dx597304267<br/>
Source: LBPTMMaterial... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBPTMPar... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBPTMPar... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBPTMPar... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBPTMParRe... |
| DxLBPTMPlanned | bigint |  |  | SI | Dimension: DxLBPTMPlanned<br/>
Source: LBPTMPlann... |
| DxLBPTMStatus | bigint |  |  | SI | Dimension: DxLBPTMStatus<br/>
Source: LBPTMStatus |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*