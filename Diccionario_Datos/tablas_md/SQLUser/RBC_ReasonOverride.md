# SQLUser.RBC_ReasonOverride

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROV_RowId | bigint | PK |  | NO | - |
| ROV_Code | varchar |  |  | NO | Code |
| ROV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROV_CreatedDate | date |  |  | SI | Created Date |
| ROV_CreatedTime | time |  |  | SI | Created Time |
| ROV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROV_DateFrom | date |  |  | SI | Date From |
| ROV_DateTo | date |  |  | SI | Date To |
| ROV_Desc | varchar |  |  | NO | Description |
| ROV_Owner | varchar |  |  | SI | Owner |
| ROV_UpdatedDate | date |  |  | SI | Updated Date |
| ROV_UpdatedTime | time |  |  | SI | Updated Time |
| ROV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*