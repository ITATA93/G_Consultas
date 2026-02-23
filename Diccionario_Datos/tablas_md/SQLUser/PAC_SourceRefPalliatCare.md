# SQLUser.PAC_SourceRefPalliatCare

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SRPC_RowId | bigint | PK |  | NO | - |
| SRPC_Code | varchar |  |  | NO | Code |
| SRPC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SRPC_CreatedDate | date |  |  | SI | Created Date |
| SRPC_CreatedTime | time |  |  | SI | Created Time |
| SRPC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SRPC_DateFrom | date |  |  | SI | Date From |
| SRPC_DateTo | date |  |  | SI | Date To |
| SRPC_Default | varchar |  |  | SI | Default |
| SRPC_Desc | varchar |  |  | NO | Description |
| SRPC_Owner | varchar |  |  | SI | Owner |
| SRPC_UpdatedDate | date |  |  | SI | Updated Date |
| SRPC_UpdatedTime | time |  |  | SI | Updated Time |
| SRPC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*