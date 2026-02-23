# SQLUser.PHC_Pack

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCPA_RowId | bigint | PK |  | NO | - |
| PHCPA_Code | varchar |  |  | NO | Code |
| PHCPA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCPA_CreatedDate | date |  |  | SI | Created Date |
| PHCPA_CreatedTime | time |  |  | SI | Created Time |
| PHCPA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCPA_Desc | varchar |  |  | NO | Description |
| PHCPA_Owner | varchar |  |  | SI | Owner |
| PHCPA_UpdatedDate | date |  |  | SI | Updated Date |
| PHCPA_UpdatedTime | time |  |  | SI | Updated Time |
| PHCPA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*