# TCBI_Cubes_ARRcptAlloc.Fact

**Schema:** TCBI_Cubes_ARRcptAlloc
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxARBILStatusViaARRALBillDR | bigint |  | FK | SI | Dimension: DxARBILStatusViaARRALBillDR<br/>
Sourc... |
| DxARBILTypeViaARRALBillDR | bigint |  | FK | SI | Dimension: DxARBILTypeViaARRALBillDR<br/>
Source:... |
| RxIDViaARRALARPBILDR | bigint |  | FK | SI | Relationship: RxIDViaARRALARPBILDR<br/>
Source: A... |
| RxIDViaARRALARRCPParRef | bigint |  |  | SI | Relationship: RxIDViaARRALARRCPParRef<br/>
Source... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*