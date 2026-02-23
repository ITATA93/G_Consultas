# SQLUser.PHC_EPrescOverrideReason

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPROVR_RowId | bigint | PK |  | NO | - |
| EPROVR_Code | varchar |  |  | NO | Code |
| EPROVR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPROVR_CreatedDate | date |  |  | SI | Created Date |
| EPROVR_CreatedTime | time |  |  | SI | Created Time |
| EPROVR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPROVR_DateFrom | date |  |  | SI | Date From |
| EPROVR_DateTo | date |  |  | SI | Date To |
| EPROVR_Desc | varchar |  |  | NO | Description |
| EPROVR_Owner | varchar |  |  | SI | Owner |
| EPROVR_UpdatedDate | date |  |  | SI | Updated Date |
| EPROVR_UpdatedTime | time |  |  | SI | Updated Time |
| EPROVR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*