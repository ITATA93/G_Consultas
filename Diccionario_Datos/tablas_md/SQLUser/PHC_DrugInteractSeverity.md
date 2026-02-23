# SQLUser.PHC_DrugInteractSeverity

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGINTS_RowId | bigint | PK |  | NO | - |
| DRGINTS_Code | varchar |  |  | NO | Code |
| DRGINTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGINTS_Color | varchar |  |  | SI | Color |
| DRGINTS_CreatedDate | date |  |  | SI | Created Date |
| DRGINTS_CreatedTime | time |  |  | SI | Created Time |
| DRGINTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGINTS_DateFrom | date |  |  | SI | DateFrom |
| DRGINTS_DateTo | date |  |  | SI | DateTo |
| DRGINTS_Desc | varchar |  |  | NO | Description |
| DRGINTS_MandatoryOverride | varchar |  |  | SI | MandatoryOverride |
| DRGINTS_Owner | varchar |  |  | SI | Owner |
| DRGINTS_Priority | double |  |  | SI | Priority |
| DRGINTS_UpdatedDate | date |  |  | SI | Updated Date |
| DRGINTS_UpdatedTime | time |  |  | SI | Updated Time |
| DRGINTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*