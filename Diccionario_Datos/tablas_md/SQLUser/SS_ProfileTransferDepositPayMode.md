# SQLUser.SS_ProfileTransferDepositPayMode

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TDPM_ParRef | bigint | PK |  | NO | Parent table |
| TDPM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TDPM_RowID | varchar |  |  | NO | - |
| TDPM_TransferDepositPayMode_DR | bigint |  | FK | SI | Des Ref to PayMode |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*