# TCDS_Cubes_LBTestSetItemAntibiotic_Version73.Fact

**Schema:** TCDS_Cubes_LBTestSetItemAntibiotic_Version73
**Columnas:** 17
**Actualizado:** 2026-01-30 15:30:59

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBTSIANT... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBTSIANT... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBTSIANT... |
| DxDSSLBTestSetItemID | bigint |  |  | SI | Dimension: DxDSSLBTestSetItemID<br/>
Source: LBTS... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBTSIANTPa... |
| DxLBCANTDesc | bigint |  |  | SI | Dimension: DxLBCANTDesc<br/>
Source: LBTSIANTAnti... |
| DxLBCAPDesc | bigint |  |  | SI | Dimension: DxLBCAPDesc<br/>
Source: LBTSIANTAntib... |
| DxLBCSENSDesc | bigint |  |  | SI | Dimension: DxLBCSENSDesc<br/>
Source: LBTSIANTRes... |
| DxLBTSIPathogen | bigint |  |  | SI | Dimension: DxLBTSIPathogen<br/>
Source: LBTSIANTP... |
| DxLBTSIPathogenDuplicate | bigint |  |  | SI | Dimension: DxLBTSIPathogenDuplicate
Expression: %... |
| DxLBTSIPathogenGrowthQualifier | bigint |  |  | SI | Dimension: DxLBTSIPathogenGrowthQualifier<br/>
So... |
| DxLBTSIPathogenSignificant | bigint |  |  | SI | Dimension: DxLBTSIPathogenSignificant
Expression:... |
| DxLBTSIPathogenSubTypeDR | bigint |  | FK | SI | Dimension: DxLBTSIPathogenSubTypeDR<br/>
Source: ... |
| DxTestItem | bigint |  |  | SI | Dimension: DxTestItem<br/>
Source: LBTSIANTParRef... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*