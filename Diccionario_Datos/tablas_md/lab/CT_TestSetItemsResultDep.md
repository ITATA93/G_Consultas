# lab.CT_TestSetItemsResultDep

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSQ_ParRef | varchar | PK |  | NO | CT_TestSetItems Parent Reference |
| CTTSQ_ANDOR | varchar |  |  | SI | AND OR |
| CTTSQ_ConditionNumber | varchar |  |  | NO | Condition Number |
| CTTSQ_Operator | varchar |  |  | SI | Operator |
| CTTSQ_RowId | varchar |  |  | NO | - |
| CTTSQ_TestItem_DR | varchar |  | FK | SI | Des Ref Data Item |
| CTTSQ_TestSet_DR | varchar |  | FK | SI | Test Set |
| CTTSQ_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*