# SQLUser.RBC_EventType

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVT_RowId | bigint | PK |  | NO | - |
| EVT_Code | varchar |  |  | NO | Code |
| EVT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EVT_CreatedDate | date |  |  | SI | Created Date |
| EVT_CreatedTime | time |  |  | SI | Created Time |
| EVT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EVT_DateFrom | date |  |  | SI | DateFrom |
| EVT_DateTo | date |  |  | SI | DateTo |
| EVT_Desc | varchar |  |  | NO | Description |
| EVT_Owner | varchar |  |  | SI | Owner |
| EVT_UpdatedDate | date |  |  | SI | Updated Date |
| EVT_UpdatedTime | time |  |  | SI | Updated Time |
| EVT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*