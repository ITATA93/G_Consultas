# SQLUser.RVC_OverPayment

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OVERP_RowId | bigint | PK |  | NO | - |
| OVERP_Code | varchar |  |  | NO | Code |
| OVERP_CreatedDate | date |  |  | SI | Created Date |
| OVERP_CreatedTime | time |  |  | SI | Created Time |
| OVERP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OVERP_Desc | varchar |  |  | NO | Description |
| OVERP_UpdatedDate | date |  |  | SI | Updated Date |
| OVERP_UpdatedTime | time |  |  | SI | Updated Time |
| OVERP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*