# SQLUser.PAC_SpecialNeedsStatus

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNS_RowId | bigint | PK |  | NO | - |
| SNS_Code | varchar |  |  | NO | Code |
| SNS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SNS_CreatedDate | date |  |  | SI | Created Date |
| SNS_CreatedTime | time |  |  | SI | Created Time |
| SNS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNS_DateFrom | date |  |  | SI | DateFrom |
| SNS_DateTo | date |  |  | SI | DateTo |
| SNS_Desc | varchar |  |  | NO | Description |
| SNS_Owner | varchar |  |  | SI | Owner |
| SNS_UpdatedDate | date |  |  | SI | Updated Date |
| SNS_UpdatedTime | time |  |  | SI | Updated Time |
| SNS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*