# SQLUser.PHC_Monograph

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MGR_RowId | bigint | PK |  | NO | - |
| MGR_Code | varchar |  |  | NO | Code |
| MGR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MGR_CreatedDate | date |  |  | SI | Created Date |
| MGR_CreatedTime | time |  |  | SI | Created Time |
| MGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MGR_Desc | varchar |  |  | NO | Description |
| MGR_Desc1 | varchar |  |  | SI | Desc1 |
| MGR_Owner | varchar |  |  | SI | Owner |
| MGR_UpdatedDate | date |  |  | SI | Updated Date |
| MGR_UpdatedTime | time |  |  | SI | Updated Time |
| MGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*