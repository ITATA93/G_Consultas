# SQLUser.RBC_ServiceSet_ItemsMinMax

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITMX_ParRef | bigint | PK |  | NO | RBC_ServiceSet Parent Reference |
| ITMX_Childsub | double |  |  | NO | Childsub |
| ITMX_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITMX_CreatedDate | date |  |  | SI | Created Date |
| ITMX_CreatedTime | time |  |  | SI | Created Time |
| ITMX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITMX_DaysMax | double |  |  | SI | Max Days |
| ITMX_DaysMin | double |  |  | SI | Min Days |
| ITMX_HoursMax | double |  |  | SI | Max Hours |
| ITMX_HoursMin | double |  |  | SI | Min Hours |
| ITMX_Main | varchar |  |  | SI | Main Service |
| ITMX_MinutesMax | double |  |  | SI | Max Days |
| ITMX_MinutesMin | double |  |  | SI | Min Days |
| ITMX_RowId | varchar |  |  | NO | - |
| ITMX_Service_DR | bigint |  | FK | SI | Des Ref RBC_Service |
| ITMX_UpdatedDate | date |  |  | SI | Updated Date |
| ITMX_UpdatedTime | time |  |  | SI | Updated Time |
| ITMX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*