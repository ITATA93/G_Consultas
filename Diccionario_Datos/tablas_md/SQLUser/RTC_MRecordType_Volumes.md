# SQLUser.RTC_MRecordType_Volumes

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VOL_ParRef | bigint | PK |  | NO | RTC_MRecordType Parent Reference |
| VOL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| VOL_Childsub | double |  |  | NO | Childsub |
| VOL_Code | varchar |  |  | NO | Code |
| VOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VOL_CreatedDate | date |  |  | SI | Created Date |
| VOL_CreatedTime | time |  |  | SI | Created Time |
| VOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VOL_Desc | varchar |  |  | NO | Description |
| VOL_RowId | varchar |  |  | NO | - |
| VOL_UpdatedDate | date |  |  | SI | Updated Date |
| VOL_UpdatedTime | time |  |  | SI | Updated Time |
| VOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*