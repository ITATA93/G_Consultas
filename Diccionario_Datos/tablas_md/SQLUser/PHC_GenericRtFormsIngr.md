# SQLUser.PHC_GenericRtFormsIngr

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGR_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| INGR_Childsub | double |  |  | NO | Childsub |
| INGR_CreatedDate | date |  |  | SI | Created Date |
| INGR_CreatedTime | time |  |  | SI | Created Time |
| INGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INGR_Ingredient_DR | bigint |  | FK | SI | Des Ref PHCIngredient |
| INGR_PerStrength | double |  |  | SI | Strength Per |
| INGR_PerUOM_DR | bigint |  | FK | SI | Strength per UOM |
| INGR_RowId | varchar |  |  | NO | - |
| INGR_Strength | double |  |  | SI | Strength |
| INGR_UOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| INGR_UpdatedDate | date |  |  | SI | Updated Date |
| INGR_UpdatedTime | time |  |  | SI | Updated Time |
| INGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*