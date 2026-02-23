# SQLUser.PHC_MedicationSource

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCMS_RowId | bigint | PK |  | NO | - |
| PHCMS_Code | varchar |  |  | NO | Code |
| PHCMS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCMS_CreatedDate | date |  |  | SI | Created Date |
| PHCMS_CreatedTime | time |  |  | SI | Created Time |
| PHCMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCMS_DateFrom | date |  |  | SI | Date From |
| PHCMS_DateTo | date |  |  | SI | Date To |
| PHCMS_Desc | varchar |  |  | NO | Description |
| PHCMS_Owner | varchar |  |  | SI | Owner |
| PHCMS_UpdatedDate | date |  |  | SI | Updated Date |
| PHCMS_UpdatedTime | time |  |  | SI | Updated Time |
| PHCMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*