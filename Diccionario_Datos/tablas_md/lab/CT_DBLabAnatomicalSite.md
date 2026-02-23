# lab.CT_DBLabAnatomicalSite

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBB_ParRef | varchar | PK |  | NO | CT_DayBookLaboratory Parent Reference |
| CTDBB_AnatomicalSite_DR | varchar |  | FK | NO | Anatomical site DR |
| CTDBB_RowId | varchar |  |  | NO | - |
| CTDBB_xxx | varchar |  |  | SI | Description |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*