# lab.CT_WBActionsCond

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTWBC_ParRef | numeric | PK |  | NO | CT_TestSetActions Parent Reference |
| CTWBC_BlockProcedure_DR | varchar |  | FK | SI | Block Procedure DR |
| CTWBC_CurrentEpisode | varchar |  |  | SI | Current Episode |
| CTWBC_Function | varchar |  |  | SI | Function |
| CTWBC_Operand | varchar |  |  | SI | Operand |
| CTWBC_Order | numeric |  |  | NO | Order |
| CTWBC_RowID | varchar |  |  | NO | - |
| CTWBC_Table | varchar |  |  | SI | Table |
| CTWBC_TableField | varchar |  |  | SI | Table Field |
| CTWBC_TestSet_DR | varchar |  | FK | SI | Test Set DR NOT USED HERE but needs to be here to ... |
| CTWBC_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*