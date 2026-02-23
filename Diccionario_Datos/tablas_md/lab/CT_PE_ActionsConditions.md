# lab.CT_PE_ActionsConditions

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPBC_ParRef | double | PK |  | NO | CT_PE_Actions Parent Reference |
| CTPBC_CurrentEpisode | varchar |  |  | SI | Current Episode |
| CTPBC_Function | varchar |  |  | SI | Function |
| CTPBC_Order | double |  |  | NO | Order |
| CTPBC_RowID | varchar |  |  | NO | - |
| CTPBC_Table | varchar |  |  | SI | Table |
| CTPBC_TableField | varchar |  |  | SI | Table Field |
| CTPBC_Value | varchar |  |  | SI | Value |
| CTPBC_xxx | varchar |  |  | SI | xxx |
| CTTBC_Operand | varchar |  |  | SI | Operand |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*