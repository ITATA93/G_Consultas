# SQLUser.RBC_ReasonUnblockHosp

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RUH_RowId | bigint | PK |  | NO | - |
| RUH_Code | varchar |  |  | NO | Code |
| RUH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RUH_CreatedDate | date |  |  | SI | Created Date |
| RUH_CreatedTime | time |  |  | SI | Created Time |
| RUH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RUH_Desc | varchar |  |  | NO | Description |
| RUH_Owner | varchar |  |  | SI | Owner |
| RUH_UpdatedDate | date |  |  | SI | Updated Date |
| RUH_UpdatedTime | time |  |  | SI | Updated Time |
| RUH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*