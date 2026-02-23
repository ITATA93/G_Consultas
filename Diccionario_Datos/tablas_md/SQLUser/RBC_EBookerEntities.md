# SQLUser.RBC_EBookerEntities

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EBENT_RowId | bigint | PK |  | NO | - |
| EBENT_Code | varchar |  |  | NO | Code |
| EBENT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EBENT_CreatedDate | date |  |  | SI | Created Date |
| EBENT_CreatedTime | time |  |  | SI | Created Time |
| EBENT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EBENT_DateFrom | date |  |  | SI | DateFrom |
| EBENT_DateTo | date |  |  | SI | DateTo |
| EBENT_Desc | varchar |  |  | NO | Description |
| EBENT_Owner | varchar |  |  | SI | Owner |
| EBENT_UpdatedDate | date |  |  | SI | Updated Date |
| EBENT_UpdatedTime | time |  |  | SI | Updated Time |
| EBENT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*