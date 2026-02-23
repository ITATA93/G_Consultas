# SQLUser.PHC_Strength

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCS_RowId | bigint | PK |  | NO | - |
| PHCS_Code | varchar |  |  | NO | Code |
| PHCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCS_CodeTranslated | varchar |  |  | SI | - |
| PHCS_CreatedDate | date |  |  | SI | Created Date |
| PHCS_CreatedTime | time |  |  | SI | Created Time |
| PHCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCS_Desc | varchar |  |  | NO | Description |
| PHCS_DescTranslated | varchar |  |  | SI | - |
| PHCS_Owner | varchar |  |  | SI | Owner |
| PHCS_UpdatedDate | date |  |  | SI | Updated Date |
| PHCS_UpdatedTime | time |  |  | SI | Updated Time |
| PHCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*