# SQLUser.RBC_ServiceSet

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SET_RowId | bigint | PK |  | NO | - |
| SET_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| SET_Code | varchar |  |  | NO | Code |
| SET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SET_CreatedDate | date |  |  | SI | Created Date |
| SET_CreatedTime | time |  |  | SI | Created Time |
| SET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SET_DateFrom | date |  |  | SI | Date From |
| SET_DateTo | date |  |  | SI | Date To  |
| SET_Desc | varchar |  |  | NO | Description |
| SET_Owner | varchar |  |  | SI | Owner |
| SET_UpdatedDate | date |  |  | SI | Updated Date |
| SET_UpdatedTime | time |  |  | SI | Updated Time |
| SET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*