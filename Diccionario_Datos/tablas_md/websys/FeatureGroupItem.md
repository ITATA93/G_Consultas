# websys.FeatureGroupItem

> Feature Group Item

**Schema:** websys
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

*Descripción original:* Feature Group Item

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| Code | varchar |  |  | NO | Code corresponding to websys.Feature |
| ID | varchar |  |  | NO | - |
| Owner | varchar |  |  | SI | Owner - DEPRECATED - Code Table Overrides |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*