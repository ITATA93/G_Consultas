# SQLUser.RBC_ReasonForRestriction

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESTR_RowId | bigint | PK |  | NO | - |
| RESTR_Code | varchar |  |  | NO | Code |
| RESTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESTR_CreatedDate | date |  |  | SI | Created Date |
| RESTR_CreatedTime | time |  |  | SI | Created Time |
| RESTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESTR_Desc | varchar |  |  | NO | Description |
| RESTR_Owner | varchar |  |  | SI | Owner |
| RESTR_UpdatedDate | date |  |  | SI | Updated Date |
| RESTR_UpdatedTime | time |  |  | SI | Updated Time |
| RESTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*