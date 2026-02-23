# SQLUser.RVC_ReclaimCode

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RECL_RowId | bigint | PK |  | NO | - |
| RECL_Code | varchar |  |  | NO | Code |
| RECL_CreatedDate | date |  |  | SI | Created Date |
| RECL_CreatedTime | time |  |  | SI | Created Time |
| RECL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RECL_Desc | varchar |  |  | NO | Description |
| RECL_UpdatedDate | date |  |  | SI | Updated Date |
| RECL_UpdatedTime | time |  |  | SI | Updated Time |
| RECL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*