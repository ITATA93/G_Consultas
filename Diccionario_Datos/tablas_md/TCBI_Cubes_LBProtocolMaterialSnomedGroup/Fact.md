# TCBI_Cubes_LBProtocolMaterialSnomedGroup.Fact

**Schema:** TCBI_Cubes_LBProtocolMaterialSnomedGroup
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1252388406 | bigint |  |  | SI | Dimension: Dx1252388406<br/>
Source: LBPMSGSnomed... |
| Dx1320268728 | bigint |  |  | SI | Dimension: Dx1320268728<br/>
Source: LBPMSGSnomed... |
| Dx1453237724 | bigint |  |  | SI | Dimension: Dx1453237724<br/>
Source: LBPMSGSnomed... |
| Dx1711019998 | bigint |  |  | SI | Dimension: Dx1711019998
Expression: ##class(web.P... |
| Dx2750869467 | bigint |  |  | SI | Dimension: Dx2750869467<br/>
Source: LBPMSGSnomed... |
| Dx340712891 | bigint |  |  | SI | Dimension: Dx340712891<br/>
Source: LBPMSGSnomedT... |
| Rx2050478392 | bigint |  |  | SI | Relationship: Rx2050478392<br/>
Source: LBPMSGSSp... |
| Rx802917900 | bigint |  |  | SI | Relationship: Rx802917900<br/>
Source: LBPMSGSSpe... |
| RxLBPMSGParRef | bigint |  |  | SI | Relationship: RxLBPMSGParRef<br/>
Source: LBPMSGP... |
| RxLBPMSGProtocolMaterialDR | bigint |  | FK | SI | Relationship: RxLBPMSGProtocolMaterialDR<br/>
Sou... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*