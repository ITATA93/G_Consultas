# SQLUser.SS_ProfileWaitListType

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLT_ParRef | bigint | PK |  | NO | Parent table |
| WLT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLT_RowID | varchar |  |  | NO | - |
| WLT_WaitListType_DR | bigint |  | FK | SI | Waiting List Type |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*