# TCBI_Cubes_LBProtocol.Fact

**Schema:** TCBI_Cubes_LBProtocol
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxProtocol | bigint |  |  | SI | Dimension: DxProtocol<br/>
Source: LBPTProtocolDR... |
| RxIDViaLBPTTestSetDR | bigint |  | FK | SI | Relationship: RxIDViaLBPTTestSetDR<br/>
Source: L... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*