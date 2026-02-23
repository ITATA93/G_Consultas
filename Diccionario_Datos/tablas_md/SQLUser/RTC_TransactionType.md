# SQLUser.RTC_TransactionType

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TT_RowId | bigint | PK |  | NO | - |
| TT_Code | varchar |  |  | NO | Code |
| TT_CreatedDate | date |  |  | SI | Created Date |
| TT_CreatedTime | time |  |  | SI | Created Time |
| TT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TT_Desc | varchar |  |  | NO | Description |
| TT_UpdatedDate | date |  |  | SI | Updated Date |
| TT_UpdatedTime | time |  |  | SI | Updated Time |
| TT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*