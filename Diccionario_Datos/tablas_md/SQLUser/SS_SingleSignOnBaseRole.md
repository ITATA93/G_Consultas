# SQLUser.SS_SingleSignOnBaseRole

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSOBR_RowId | bigint | PK |  | NO | - |
| SSOBR_Code | varchar |  |  | NO | Code |
| SSOBR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSOBR_DateFrom | date |  |  | SI | Date From |
| SSOBR_DateTo | date |  |  | SI | Date To |
| SSOBR_Desc | varchar |  |  | NO | Description |
| SSOBR_Owner | varchar |  |  | SI | Owner |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*