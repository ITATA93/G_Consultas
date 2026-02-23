# lab.CT_SuperSetFeesConditions

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSSQ_ParRef | varchar | PK |  | NO | CT_SuperSetFees Parent Reference |
| CTSSQ_ANDOR | varchar |  |  | SI | AND OR |
| CTSSQ_ConditionNumber | varchar |  |  | NO | Condition Number |
| CTSSQ_Operator | varchar |  |  | SI | Operator |
| CTSSQ_RowID | varchar |  |  | NO | - |
| CTSSQ_TestItem_DR | varchar |  | FK | SI | Des Ref Data Item |
| CTSSQ_TestSet_DR | varchar |  | FK | SI | Test Set |
| CTSSQ_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*