# SQLUser.SS_GroupStockTakeGroup

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STG_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| STG_Childsub | double |  |  | NO | Childsub |
| STG_RowId | varchar |  |  | NO | - |
| STG_StockTakeGroup_DR | bigint |  | FK | SI | Des Ref StockTakeGroup |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*