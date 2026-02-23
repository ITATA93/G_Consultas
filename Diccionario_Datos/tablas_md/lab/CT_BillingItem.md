# lab.CT_BillingItem

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBI_RowId | varchar | PK |  | NO | - |
| CTBI_BaseItems | varchar |  |  | SI | Base Items |
| CTBI_Code | varchar |  |  | NO | Code |
| CTBI_Department_DR | varchar |  | FK | SI | Des Ref Department |
| CTBI_Description | varchar |  |  | SI | Description |
| CTBI_ExcludeFromConing | varchar |  |  | SI | Exclude From Coning |
| CTBI_ExcludeInitiationItem | varchar |  |  | SI | Exclude Initiation Item |
| CTBI_HISTO_Extra | varchar |  |  | SI | HISTO Extra fields |
| CTBI_xxx1 | varchar |  |  | SI | HISTO Number of Specimens |
| CTBI_xxx2 | varchar |  |  | SI | Second Item |
| CTBI_xxx3 | varchar |  |  | SI | Number Limit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*