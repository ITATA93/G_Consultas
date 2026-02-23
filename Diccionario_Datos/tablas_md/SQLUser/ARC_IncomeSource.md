# SQLUser.ARC_IncomeSource

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCS_RowId | bigint | PK |  | NO | - |
| ChildQ36DR | - |  |  | SI | Child Reference: Oídos |
| INCS_Code | varchar |  |  | NO | Code |
| INCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCS_CreatedDate | date |  |  | SI | Created Date |
| INCS_CreatedTime | time |  |  | SI | Created Time |
| INCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCS_Desc | varchar |  |  | NO | Description |
| INCS_Owner | varchar |  |  | SI | Owner |
| INCS_UpdatedDate | date |  |  | SI | Updated Date |
| INCS_UpdatedTime | time |  |  | SI | Updated Time |
| INCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q34Q1 | - |  |  | SI | Hallazgo |
| Q34Q2 | - |  |  | SI | Ubicación |
| Q34Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*