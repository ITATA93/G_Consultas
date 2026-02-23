# lab.CT_TestSetComActionsCond

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSV_ParRef | double | PK |  | NO | CT_TestSetComActions Parent Reference |
| CTTSV_CurrentEpisode | varchar |  |  | SI | Current Episode |
| CTTSV_Function | varchar |  |  | SI | Function |
| CTTSV_Operand | varchar |  |  | SI | Operand |
| CTTSV_Order | double |  |  | NO | Order |
| CTTSV_RowID | varchar |  |  | NO | - |
| CTTSV_Table | varchar |  |  | SI | Table |
| CTTSV_TableField | varchar |  |  | SI | Table Field |
| CTTSV_TestSet_DR | varchar |  | FK | SI | Test Set DR |
| CTTSV_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*