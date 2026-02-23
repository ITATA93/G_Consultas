# SQLUser.SS_ProfileSessionType

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SESS_ParRef | bigint | PK |  | NO | Parent table |
| SESS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SESS_RowID | varchar |  |  | NO | - |
| SESS_SessionType_DR | bigint |  | FK | SI | Session Type |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*