# SQLUser.RTC_ReasonForCancel

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REACANC_RowId | bigint | PK |  | NO | - |
| REACANC_Code | varchar |  |  | NO | Code |
| REACANC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REACANC_CreatedDate | date |  |  | SI | Created Date |
| REACANC_CreatedTime | time |  |  | SI | Created Time |
| REACANC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REACANC_DateFrom | date |  |  | SI | Date From |
| REACANC_DateTo | date |  |  | SI | Date To |
| REACANC_Desc | varchar |  |  | NO | Description |
| REACANC_Owner | varchar |  |  | SI | Owner |
| REACANC_UpdatedDate | date |  |  | SI | Updated Date |
| REACANC_UpdatedTime | time |  |  | SI | Updated Time |
| REACANC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*