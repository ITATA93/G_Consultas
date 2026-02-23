# TCBI_Cubes_LBTestSetSnomedGroup.Fact

**Schema:** TCBI_Cubes_LBTestSetSnomedGroup
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1768822278 | bigint |  |  | SI | Dimension: Dx1768822278<br/>
Source: LBTSSGSnomed... |
| Dx281162864 | bigint |  |  | SI | Dimension: Dx281162864
Expression: ##class(web.PA... |
| Dx3738575974 | bigint |  |  | SI | Dimension: Dx3738575974<br/>
Source: LBTSSGSnomed... |
| Dx733900385 | bigint |  |  | SI | Dimension: Dx733900385<br/>
Source: LBTSSGSnomedT... |
| Dx865171461 | bigint |  |  | SI | Dimension: Dx865171461<br/>
Source: LBTSSGSnomedT... |
| Dx931472779 | bigint |  |  | SI | Dimension: Dx931472779<br/>
Source: LBTSSGSnomedT... |
| RxLBTSSGParRef | bigint |  |  | SI | Relationship: RxLBTSSGParRef<br/>
Source: LBTSSGP... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*