# SQLUser.RBC_AppointMethod

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APTM_RowId | bigint | PK |  | NO | - |
| APTM_Code | varchar |  |  | NO | Code |
| APTM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APTM_CollectMoney | varchar |  |  | SI | Collect Money |
| APTM_CreatedDate | date |  |  | SI | Created Date |
| APTM_CreatedTime | time |  |  | SI | Created Time |
| APTM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APTM_DateFrom | date |  |  | SI | Date From |
| APTM_DateTo | date |  |  | SI | Date To |
| APTM_Desc | varchar |  |  | NO | Description |
| APTM_Owner | varchar |  |  | SI | Owner |
| APTM_UpdatedDate | date |  |  | SI | Updated Date |
| APTM_UpdatedTime | time |  |  | SI | Updated Time |
| APTM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*