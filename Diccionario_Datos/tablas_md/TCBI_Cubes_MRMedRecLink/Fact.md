# TCBI_Cubes_MRMedRecLink.Fact

**Schema:** TCBI_Cubes_MRMedRecLink
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
| DxClassifiedVia | bigint |  |  | SI | Dimension: DxClassifiedVia<br/>
Source: MRLClassi... |
| DxDecision | bigint |  |  | SI | Dimension: DxDecision<br/>
Source: MRLDecision |
| DxDiscrepancy | bigint |  |  | SI | Dimension: DxDiscrepancy<br/>
Source: MRLDiscrepa... |
| DxEpisodeID | bigint |  |  | SI | Dimension: DxEpisodeID<br/>
Source: MRLParRef.MED... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: MRLParRef.MED... |
| RxIDViaMRLParRef | bigint |  |  | SI | Relationship: RxIDViaMRLParRef<br/>
Source: MRLPa... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*