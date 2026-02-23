# lab.CT_BBActionCond

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBAC_ParRef | varchar | PK |  | NO | CT_BBAction Parent Reference |
| BBAC_CurrentEpisode | varchar |  |  | SI | Current Episode |
| BBAC_Function | varchar |  |  | SI | Function |
| BBAC_Operand | varchar |  |  | SI | Operand |
| BBAC_Order | numeric |  |  | NO | Order |
| BBAC_RowID | varchar |  |  | NO | - |
| BBAC_Table | varchar |  |  | SI | Table |
| BBAC_TableField | varchar |  |  | SI | Table Field |
| BBAC_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*