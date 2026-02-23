# TCBI_Cubes_OEOrdExec.DxOrderDescription

**Schema:** TCBI_Cubes_OEOrdExec
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DxOrderCode | bigint |  |  | NO | Dimension property: DxOrderCode<br/>
Source: OEOR... |
| DxOrderDescription | varchar |  |  | NO | Dimension property: DxOrderDescription<br/>
Sourc... |
| PxOrderDescription | varchar |  |  | SI | Dimension property: PxOrderDescription<br/>
Sourc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*