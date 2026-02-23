# SQLUser.PHC_AllergyGroup

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALGR_RowId | bigint | PK |  | NO | - |
| ALGR_Code | varchar |  |  | NO | Code |
| ALGR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALGR_CreatedDate | date |  |  | SI | Created Date |
| ALGR_CreatedTime | time |  |  | SI | Created Time |
| ALGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALGR_DateFrom | date |  |  | SI | Date From |
| ALGR_DateTo | date |  |  | SI | Date To |
| ALGR_Desc | varchar |  |  | NO | Description |
| ALGR_Owner | varchar |  |  | SI | Owner |
| ALGR_UpdatedDate | date |  |  | SI | Updated Date |
| ALGR_UpdatedTime | time |  |  | SI | Updated Time |
| ALGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*