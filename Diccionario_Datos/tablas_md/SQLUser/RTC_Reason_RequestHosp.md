# SQLUser.RTC_Reason_RequestHosp

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOS_ParRef | bigint | PK |  | NO | RTC_Reason_Request Parent Reference |
| HOS_Childsub | double |  |  | NO | Childsub |
| HOS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOS_CreatedDate | date |  |  | SI | Created Date |
| HOS_CreatedTime | time |  |  | SI | Created Time |
| HOS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HOS_RowId | varchar |  |  | NO | - |
| HOS_UpdatedDate | date |  |  | SI | Updated Date |
| HOS_UpdatedTime | time |  |  | SI | Updated Time |
| HOS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*