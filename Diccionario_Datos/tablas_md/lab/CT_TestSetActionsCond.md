# lab.CT_TestSetActionsCond

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSM_ParRef | varchar | PK |  | NO | CT_TestSetActions Parent Reference |
| CTTSM_CurrentEpisode | varchar |  |  | SI | Current Episode |
| CTTSM_Function | varchar |  |  | SI | Function |
| CTTSM_Operand | varchar |  |  | SI | Operand |
| CTTSM_Order | numeric |  |  | NO | Order |
| CTTSM_RowID | varchar |  |  | NO | - |
| CTTSM_Table | varchar |  |  | SI | Table |
| CTTSM_TableField | varchar |  |  | SI | Table Field |
| CTTSM_TestSet_DR | varchar |  | FK | SI | Test Set DR |
| CTTSM_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*