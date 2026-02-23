# SQLUser.PHC_AllergyXSens

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALXS_RowId | bigint | PK |  | NO | - |
| ALXS_Code | varchar |  |  | NO | Code |
| ALXS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALXS_CreatedDate | date |  |  | SI | Created Date |
| ALXS_CreatedTime | time |  |  | SI | Created Time |
| ALXS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALXS_Desc | varchar |  |  | NO | Description |
| ALXS_Owner | varchar |  |  | SI | Owner |
| ALXS_UpdatedDate | date |  |  | SI | Updated Date |
| ALXS_UpdatedTime | time |  |  | SI | Updated Time |
| ALXS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*