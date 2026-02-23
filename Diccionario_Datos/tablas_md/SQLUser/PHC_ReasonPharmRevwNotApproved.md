# SQLUser.PHC_ReasonPharmRevwNotApproved

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCRPRNA_RowId | bigint | PK |  | NO | - |
| PHCRPRNA_Code | varchar |  |  | NO | Code |
| PHCRPRNA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCRPRNA_CreatedDate | date |  |  | SI | Created Date |
| PHCRPRNA_CreatedTime | time |  |  | SI | Created Time |
| PHCRPRNA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCRPRNA_DateFrom | date |  |  | SI | Date From |
| PHCRPRNA_DateTo | date |  |  | SI | Date To |
| PHCRPRNA_Desc | varchar |  |  | NO | Description |
| PHCRPRNA_Owner | varchar |  |  | SI | Owner |
| PHCRPRNA_UpdatedDate | date |  |  | SI | Updated Date |
| PHCRPRNA_UpdatedTime | time |  |  | SI | Updated Time |
| PHCRPRNA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*