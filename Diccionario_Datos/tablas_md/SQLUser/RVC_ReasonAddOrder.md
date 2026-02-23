# SQLUser.RVC_ReasonAddOrder

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RAO_RowId | bigint | PK |  | NO | - |
| RAO_Code | varchar |  |  | NO | Code |
| RAO_CreatedDate | date |  |  | SI | Created Date |
| RAO_CreatedTime | time |  |  | SI | Created Time |
| RAO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RAO_Desc | varchar |  |  | NO | Description |
| RAO_UpdatedDate | date |  |  | SI | Updated Date |
| RAO_UpdatedTime | time |  |  | SI | Updated Time |
| RAO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*