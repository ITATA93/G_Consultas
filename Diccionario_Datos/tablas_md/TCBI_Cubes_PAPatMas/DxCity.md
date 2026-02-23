# TCBI_Cubes_PAPatMas.DxCity

**Schema:** TCBI_Cubes_PAPatMas
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DxCity | varchar |  |  | NO | Dimension property: DxCity<br/>
Source: %source.P... |
| DxState | bigint |  |  | NO | Dimension property: DxState<br/>
Source: %cube.Ge... |
| PxCityName | varchar |  |  | SI | Dimension property: PxCityName<br/>
Source: %sour... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*