# SQLUser.SS_ProfilePayModeAllowedCancel

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PMALC_ParRef | bigint | PK |  | NO | Parent table |
| PMALC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PMALC_PayModeAllowedCancel_DR | bigint |  | FK | SI | Des Ref to PayMode |
| PMALC_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*