# SQLUser.PHC_EPrescStatus

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPRST_RowId | bigint | PK |  | NO | - |
| EPRST_Code | varchar |  |  | NO | Code |
| EPRST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPRST_CreatedDate | date |  |  | SI | Created Date |
| EPRST_CreatedTime | time |  |  | SI | Created Time |
| EPRST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPRST_DateFrom | date |  |  | SI | Date From |
| EPRST_DateTo | date |  |  | SI | Date To |
| EPRST_Desc | varchar |  |  | NO | Description |
| EPRST_OverrideResReqBefoDisp | varchar |  |  | SI | Override Reason Required Before Dispensing |
| EPRST_Owner | varchar |  |  | SI | Owner |
| EPRST_UpdatedDate | date |  |  | SI | Updated Date |
| EPRST_UpdatedTime | time |  |  | SI | Updated Time |
| EPRST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*