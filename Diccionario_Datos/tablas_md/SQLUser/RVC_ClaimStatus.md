# SQLUser.RVC_ClaimStatus

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLST_RowId | bigint | PK |  | NO | - |
| CLST_Code | varchar |  |  | NO | Code |
| CLST_CreatedDate | date |  |  | SI | Created Date |
| CLST_CreatedTime | time |  |  | SI | Created Time |
| CLST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLST_Desc | varchar |  |  | NO | Description |
| CLST_UpdatedDate | date |  |  | SI | Updated Date |
| CLST_UpdatedTime | time |  |  | SI | Updated Time |
| CLST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*