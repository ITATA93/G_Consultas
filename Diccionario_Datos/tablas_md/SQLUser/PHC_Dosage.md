# SQLUser.PHC_Dosage

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCDO_RowId | bigint | PK |  | NO | - |
| PHCDO_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| PHCDO_Code | varchar |  |  | NO | Dosage Code |
| PHCDO_CreatedDate | date |  |  | SI | Created Date |
| PHCDO_CreatedTime | time |  |  | SI | Created Time |
| PHCDO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCDO_Desc1 | varchar |  |  | NO | Description(Local Language) |
| PHCDO_Desc2 | varchar |  |  | SI | Description(Foreign Language) |
| PHCDO_Factor | double |  |  | NO | Factor |
| PHCDO_Qty | double |  |  | SI | Base Qty |
| PHCDO_UpdatedDate | date |  |  | SI | Updated Date |
| PHCDO_UpdatedTime | time |  |  | SI | Updated Time |
| PHCDO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*