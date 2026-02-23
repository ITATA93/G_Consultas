# SQLUser.RTC_Reason_Move

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOVE_RowId | bigint | PK |  | NO | - |
| MOVE_Active | varchar |  |  | SI | Active |
| MOVE_Code | varchar |  |  | NO | Code |
| MOVE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MOVE_CreatedDate | date |  |  | SI | Created Date |
| MOVE_CreatedTime | time |  |  | SI | Created Time |
| MOVE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MOVE_DateFrom | date |  |  | SI | DateFrom |
| MOVE_DateTo | date |  |  | SI | DateTo |
| MOVE_Desc | varchar |  |  | NO | Description |
| MOVE_Owner | varchar |  |  | SI | Owner |
| MOVE_UpdatedDate | date |  |  | SI | Updated Date |
| MOVE_UpdatedTime | time |  |  | SI | Updated Time |
| MOVE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*