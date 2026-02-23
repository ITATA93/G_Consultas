# lab.CT_Schedule_Rule_XOver

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSHX_ParRef | varchar | PK |  | NO | CT_Schedule Parent Reference |
| CTSHX_Date | date |  |  | NO | Effective Date |
| CTSHX_Description | varchar |  |  | SI | Description |
| CTSHX_ItemExclude_DR | varchar |  | FK | NO | Item Exclude DR |
| CTSHX_Item_DR | varchar |  | FK | NO | Item DR |
| CTSHX_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*