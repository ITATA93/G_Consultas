# TCDS_Cubes_LBProtocolObservation_Version73.Fact

**Schema:** TCDS_Cubes_LBProtocolObservation_Version73
**Columnas:** 11
**Actualizado:** 2026-01-30 15:30:38

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx3158441237 | bigint |  |  | SI | Dimension: Dx3158441237<br/>
Source: LBPTOObserva... |
| Dx3338883570 | bigint |  |  | SI | Dimension: Dx3338883570<br/>
Source: LBPTOAddOnBy... |
| Dx606233626 | bigint |  |  | SI | Dimension: Dx606233626<br/>
Source: LBPTOObservat... |
| Dx760476436 | bigint |  |  | SI | Dimension: Dx760476436<br/>
Source: LBPTOSourceDR... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBPTOPar... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBPTOPar... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBPTOPar... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBPTOParRe... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*