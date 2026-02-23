# SQLUser.RVC_OpinionCode

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPIN_RowId | bigint | PK |  | NO | - |
| OPIN_Code | varchar |  |  | NO | Code |
| OPIN_CreatedDate | date |  |  | SI | Created Date |
| OPIN_CreatedTime | time |  |  | SI | Created Time |
| OPIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPIN_Desc | varchar |  |  | NO | Description |
| OPIN_UpdatedDate | date |  |  | SI | Updated Date |
| OPIN_UpdatedTime | time |  |  | SI | Updated Time |
| OPIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*