# SQLUser.RBC_MultiDiscTeam

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MDT_RowId | bigint | PK |  | NO | - |
| MDT_Code | varchar |  |  | NO | Code |
| MDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MDT_CreatedDate | date |  |  | SI | Created Date |
| MDT_CreatedTime | time |  |  | SI | Created Time |
| MDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MDT_DateFrom | date |  |  | SI | DateFrom |
| MDT_DateTo | date |  |  | SI | DateTo |
| MDT_Desc | varchar |  |  | NO | Description |
| MDT_Owner | varchar |  |  | SI | Owner |
| MDT_UpdatedDate | date |  |  | SI | Updated Date |
| MDT_UpdatedTime | time |  |  | SI | Updated Time |
| MDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*