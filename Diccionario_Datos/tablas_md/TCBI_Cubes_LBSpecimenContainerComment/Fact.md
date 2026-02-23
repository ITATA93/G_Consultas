# TCBI_Cubes_LBSpecimenContainerComment.Fact

**Schema:** TCBI_Cubes_LBSpecimenContainerComment
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
| DxSpecimenComment | bigint |  |  | SI | Dimension: DxSpecimenComment<br/>
Source: LBSPCCS... |
| DxSpecimenCommentGroup | bigint |  |  | SI | Dimension: DxSpecimenCommentGroup<br/>
Source: LB... |
| MxReportable | double |  |  | SI | Measure: MxReportable
Expression: %source.LBSPCCR... |
| RxLBSPCCParRef | bigint |  |  | SI | Relationship: RxLBSPCCParRef<br/>
Source: LBSPCCP... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*