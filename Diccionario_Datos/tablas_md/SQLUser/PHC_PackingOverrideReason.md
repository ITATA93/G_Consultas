# SQLUser.PHC_PackingOverrideReason

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKOR_RowId | bigint | PK |  | NO | - |
| PKOR_Code | varchar |  |  | NO | Code |
| PKOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PKOR_CreatedDate | date |  |  | SI | Created Date |
| PKOR_CreatedTime | time |  |  | SI | Created Time |
| PKOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKOR_Desc | varchar |  |  | NO | Description |
| PKOR_Owner | varchar |  |  | SI | Owner |
| PKOR_UpdatedDate | date |  |  | SI | Updated Date |
| PKOR_UpdatedTime | time |  |  | SI | Updated Time |
| PKOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*