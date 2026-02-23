# SQLUser.SS_ProfileLabCareProvider

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPLCP_ParRef | bigint | PK |  | NO | Parent table |
| SSPLCP_CareProvider_DR | varchar |  | FK | SI | Care Provider |
| SSPLCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPLCP_DateFrom | date |  |  | SI | Date From |
| SSPLCP_DateTo | date |  |  | SI | Date To |
| SSPLCP_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*