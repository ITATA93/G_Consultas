# TCBI_Cubes_LBSpecimenContainerSnomedGroup.Fact

**Schema:** TCBI_Cubes_LBSpecimenContainerSnomedGroup
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1733116764 | bigint |  |  | SI | Dimension: Dx1733116764<br/>
Source: LBSCSGSnomed... |
| Dx2315919167 | bigint |  |  | SI | Dimension: Dx2315919167<br/>
Source: LBSCSGSnomed... |
| Dx2384347825 | bigint |  |  | SI | Dimension: Dx2384347825<br/>
Source: LBSCSGSnomed... |
| Dx2451900763 | bigint |  |  | SI | Dimension: Dx2451900763<br/>
Source: LBSCSGSnomed... |
| Dx2855339409 | bigint |  |  | SI | Dimension: Dx2855339409
Expression: ##class(web.P... |
| Dx3505746236 | bigint |  |  | SI | Dimension: Dx3505746236<br/>
Source: LBSCSGSnomed... |
| Rx116053620 | bigint |  |  | SI | Relationship: Rx116053620<br/>
Source: LBSCSGTest... |
| RxLBSCSGParRef | bigint |  |  | SI | Relationship: RxLBSCSGParRef<br/>
Source: LBSCSGP... |
| RxLBSCSGSpecimenContainerDR | bigint |  | FK | SI | Relationship: RxLBSCSGSpecimenContainerDR<br/>
So... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*