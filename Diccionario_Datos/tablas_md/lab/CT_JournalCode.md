# lab.CT_JournalCode

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTJO_RowID | varchar | PK |  | NO | - |
| CTJO_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTJO_Code | varchar |  |  | NO | Journal code |
| CTJO_Comments | varchar |  |  | SI | Comments |
| CTJO_Desc | varchar |  |  | SI | Journal description |
| CTJO_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTJO_Refund | varchar |  |  | SI | Refund |
| CTJO_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*