# SQLUser.RBC_DepartmentGroup

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEP_RowId | bigint | PK |  | NO | - |
| DEP_Code | varchar |  |  | NO | Code |
| DEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEP_CreatedDate | date |  |  | SI | Created Date |
| DEP_CreatedTime | time |  |  | SI | Created Time |
| DEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEP_DateFrom | date |  |  | SI | Date From |
| DEP_DateTo | date |  |  | SI | Date To |
| DEP_DepGrHead | varchar |  |  | SI | Head of Dep Group (Division) |
| DEP_Desc | varchar |  |  | NO | Description |
| DEP_Owner | varchar |  |  | SI | Owner |
| DEP_UpdatedDate | date |  |  | SI | Updated Date |
| DEP_UpdatedTime | time |  |  | SI | Updated Time |
| DEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*