# SQLUser.RVC_AdjustmentReason

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADJ_RowId | bigint | PK |  | NO | - |
| ADJ_Code | varchar |  |  | NO | Code |
| ADJ_CreatedDate | date |  |  | SI | Created Date |
| ADJ_CreatedTime | time |  |  | SI | Created Time |
| ADJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADJ_Desc | varchar |  |  | NO | Description |
| ADJ_UpdatedDate | date |  |  | SI | Updated Date |
| ADJ_UpdatedTime | time |  |  | SI | Updated Time |
| ADJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*