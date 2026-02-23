# SQLUser.SS_ProfileWaitListPriority

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLP_ParRef | bigint | PK |  | NO | Parent table |
| WLP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLP_RowID | varchar |  |  | NO | - |
| WLP_WaitListPriority_DR | bigint |  | FK | SI | Waiting List Priority |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*