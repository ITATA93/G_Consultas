# lab.CT_DBLabDBEntry

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBC_ParRef | varchar | PK |  | NO | CT_DayBookLaboratory Parent Reference |
| CTDBC_Description | varchar |  |  | SI | Description |
| CTDBC_Field | varchar |  |  | SI | Field |
| CTDBC_Length | varchar |  |  | SI | Length |
| CTDBC_MenuPosition | varchar |  |  | SI | Menu Position |
| CTDBC_Position | varchar |  |  | SI | Position |
| CTDBC_RowID | varchar |  |  | NO | - |
| CTDBC_Sequence | double |  |  | NO | Sequence |
| CTDBC_TabName | varchar |  |  | SI | Tab Name |
| CTDBC_Type | varchar |  |  | SI | Type |
| CTDBC_WindowFormula | varchar |  |  | SI | Window Formula |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*