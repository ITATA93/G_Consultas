# SQLUser.RTC_PostDischargeStatus

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRSTAT_RowId | bigint | PK |  | NO | - |
| MRSTAT_Code | varchar |  |  | NO | Code |
| MRSTAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MRSTAT_CreatedDate | date |  |  | SI | Created Date |
| MRSTAT_CreatedTime | time |  |  | SI | Created Time |
| MRSTAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRSTAT_DateFrom | date |  |  | SI | Date From |
| MRSTAT_DateTo | date |  |  | SI | Date To |
| MRSTAT_Desc | varchar |  |  | NO | Description |
| MRSTAT_Owner | varchar |  |  | SI | Owner |
| MRSTAT_UpdatedDate | date |  |  | SI | Updated Date |
| MRSTAT_UpdatedTime | time |  |  | SI | Updated Time |
| MRSTAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*