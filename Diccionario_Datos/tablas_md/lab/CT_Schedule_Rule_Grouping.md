# lab.CT_Schedule_Rule_Grouping

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSHG_ParRef | varchar | PK |  | NO | CT_Schedule Parent Reference |
| CTSHG_Date | date |  |  | NO | Effective Date |
| CTSHG_Description | varchar |  |  | SI | Description |
| CTSHG_ItemNew_DR | varchar |  | FK | SI | Item New DR |
| CTSHG_Item_DR | varchar |  | FK | NO | Item DR |
| CTSHG_NoOfItems | numeric |  |  | NO | No Of Items |
| CTSHG_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*