# SQLUser.SS_ProfilePayModeAllowedRefund

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PMALR_ParRef | bigint | PK |  | NO | Parent table |
| PMALR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PMALR_PayModeAllowedRefund_DR | bigint |  | FK | SI | Des Ref to PayMode |
| PMALR_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*