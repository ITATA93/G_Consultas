# TCBI_Cubes_LBTestSetItemAntibiotic.Fact

**Schema:** TCBI_Cubes_LBTestSetItemAntibiotic
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
| DxLBCANTCDesc | bigint |  |  | SI | Dimension: DxLBCANTCDesc<br/>
Source: LBTSIANTAnt... |
| DxLBCANTDesc | bigint |  |  | SI | Dimension: DxLBCANTDesc<br/>
Source: LBTSIANTAnti... |
| DxLBCAPDesc | bigint |  |  | SI | Dimension: DxLBCAPDesc<br/>
Source: LBTSIANTAntib... |
| DxLBCSENSDesc | bigint |  |  | SI | Dimension: DxLBCSENSDesc<br/>
Source: LBTSIANTRes... |
| DxLBTSIANTReportable | bigint |  |  | SI | Dimension: DxLBTSIANTReportable<br/>
Source: LBTS... |
| RxLBTSIANTParRef | bigint |  |  | SI | Relationship: RxLBTSIANTParRef<br/>
Source: LBTSI... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*