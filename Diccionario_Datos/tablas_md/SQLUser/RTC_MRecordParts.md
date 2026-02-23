# SQLUser.RTC_MRecordParts

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PART_RowId | bigint | PK |  | NO | - |
| PART_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PART_Code | varchar |  |  | NO | Code |
| PART_CreatedDate | date |  |  | SI | Created Date |
| PART_CreatedTime | time |  |  | SI | Created Time |
| PART_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PART_Desc | varchar |  |  | NO | Description |
| PART_UpdatedDate | date |  |  | SI | Updated Date |
| PART_UpdatedTime | time |  |  | SI | Updated Time |
| PART_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*