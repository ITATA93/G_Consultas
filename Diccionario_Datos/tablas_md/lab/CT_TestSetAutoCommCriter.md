# lab.CT_TestSetAutoCommCriter

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSR_ParRef | varchar | PK |  | NO | CT_TestSetDataItems Parent Reference |
| CTTSR_CommentItem_DR | varchar |  | FK | NO | Des Ref Comment Item |
| CTTSR_Operator | varchar |  |  | SI | Operator |
| CTTSR_ResultValue | varchar |  |  | SI | Result Value |
| CTTSR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*