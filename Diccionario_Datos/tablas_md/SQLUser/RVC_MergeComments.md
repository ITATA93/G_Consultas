# SQLUser.RVC_MergeComments

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MCOM_RowId | bigint | PK |  | NO | - |
| MCOM_Code | varchar |  |  | NO | Code |
| MCOM_CreatedDate | date |  |  | SI | Created Date |
| MCOM_CreatedTime | time |  |  | SI | Created Time |
| MCOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MCOM_Desc | varchar |  |  | NO | Description |
| MCOM_UpdatedDate | date |  |  | SI | Updated Date |
| MCOM_UpdatedTime | time |  |  | SI | Updated Time |
| MCOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*