# SQLUser.RBC_SessionLabel

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SESL_RowId | bigint | PK |  | NO | - |
| SESL_Code | varchar |  |  | NO | Code |
| SESL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SESL_CreatedDate | date |  |  | SI | Created Date |
| SESL_CreatedTime | time |  |  | SI | Created Time |
| SESL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SESL_DateFrom | date |  |  | SI | Date From |
| SESL_DateTo | date |  |  | SI | Date To |
| SESL_Desc | varchar |  |  | NO | Description |
| SESL_Owner | varchar |  |  | SI | Owner |
| SESL_UpdatedDate | date |  |  | SI | Updated Date |
| SESL_UpdatedTime | time |  |  | SI | Updated Time |
| SESL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*