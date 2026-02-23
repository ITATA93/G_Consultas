# SQLUser.SS_ProfileLabQueueRestriction

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPLQR_ParRef | bigint | PK |  | NO | Parent table |
| SSPLQR_Queue_DR | bigint |  | FK | SI | Lab Queue  |
| SSPLQR_ReadOnlyFlag | bit |  |  | SI | - |
| SSPLQR_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*