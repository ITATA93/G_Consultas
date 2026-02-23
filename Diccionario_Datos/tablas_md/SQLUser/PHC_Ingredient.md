# SQLUser.PHC_Ingredient

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGR_RowId | bigint | PK |  | NO | - |
| INGR_AllowDuplicate | double |  |  | SI | Allow Duplicate |
| INGR_Code | varchar |  |  | NO | Code |
| INGR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INGR_CreatedDate | date |  |  | SI | Created Date |
| INGR_CreatedTime | time |  |  | SI | Created Time |
| INGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INGR_Desc | varchar |  |  | NO | Description |
| INGR_MaxDose | double |  |  | SI | MaxDose |
| INGR_MaxDoseUOM_DR | bigint |  | FK | SI | MaxDose UOM |
| INGR_Owner | varchar |  |  | SI | Owner |
| INGR_UnivUOM_DR | bigint |  | FK | SI | Universal Conversion Factor |
| INGR_UpdatedDate | date |  |  | SI | Updated Date |
| INGR_UpdatedTime | time |  |  | SI | Updated Time |
| INGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*