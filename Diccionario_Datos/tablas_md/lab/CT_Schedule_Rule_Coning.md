# lab.CT_Schedule_Rule_Coning

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSHC_ParRef | varchar | PK |  | NO | CT_Schedule Parent Reference |
| CTSHC_Date | date |  |  | NO | Effective Date |
| CTSHC_Description | varchar |  |  | SI | Description |
| CTSHC_Item1 | varchar |  |  | NO | Item 1 |
| CTSHC_Item2 | varchar |  |  | NO | Item 2 |
| CTSHC_ItemNew | varchar |  |  | SI | Item New |
| CTSHC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*