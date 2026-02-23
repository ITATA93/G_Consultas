# SQLUser.ARC_FutureAction

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FUTACT_RowId | bigint | PK |  | NO | - |
| ChildQ83DR | - |  |  | SI | Child Reference: Reflejos Arcaicos Normales |
| FUTACT_Code | varchar |  |  | NO | Code |
| FUTACT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FUTACT_CreatedDate | date |  |  | SI | Created Date |
| FUTACT_CreatedTime | time |  |  | SI | Created Time |
| FUTACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FUTACT_DateFrom | date |  |  | SI | Date From |
| FUTACT_DateTo | date |  |  | SI | Date To |
| FUTACT_Desc | varchar |  |  | NO | Description |
| FUTACT_Owner | varchar |  |  | SI | Owner |
| FUTACT_UpdatedDate | date |  |  | SI | Updated Date |
| FUTACT_UpdatedTime | time |  |  | SI | Updated Time |
| FUTACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q05Q0 | - |  |  | SI | Lesión |
| Q05Q1 | - |  |  | SI | Localización |
| Q05Q2 | - |  |  | SI | Lateralidad |
| Q05Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*