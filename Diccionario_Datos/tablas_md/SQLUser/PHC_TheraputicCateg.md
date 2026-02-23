# SQLUser.PHC_TheraputicCateg

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| THC_RowId | bigint | PK |  | NO | - |
| THC_Code | varchar |  |  | NO | Code |
| THC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| THC_CreatedDate | date |  |  | SI | Created Date |
| THC_CreatedTime | time |  |  | SI | Created Time |
| THC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| THC_Desc | varchar |  |  | NO | Description |
| THC_Owner | varchar |  |  | SI | Owner |
| THC_UpdatedDate | date |  |  | SI | Updated Date |
| THC_UpdatedTime | time |  |  | SI | Updated Time |
| THC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*