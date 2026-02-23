# SQLUser.PHC_IngredientDoseMax

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOSEMAX_ParRef | bigint | PK |  | NO | PHC_Ingredient Parent Reference |
| DOSEMAX_AgeFrom | double |  |  | SI | Age From |
| DOSEMAX_AgeTo | double |  |  | SI | Age To |
| DOSEMAX_AgeUnit | varchar |  |  | SI | Age Unit |
| DOSEMAX_BSAFormula | varchar |  |  | SI | BSA Formula |
| DOSEMAX_Childsub | double |  |  | NO | Childsub |
| DOSEMAX_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOSEMAX_CreatedDate | date |  |  | SI | Created Date |
| DOSEMAX_CreatedTime | time |  |  | SI | Created Time |
| DOSEMAX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOSEMAX_DoseDenom | varchar |  |  | SI | Dose Denominator |
| DOSEMAX_DosingTimeFrame | varchar |  |  | SI | Dosing Time Frame |
| DOSEMAX_IncludeIngr | varchar |  |  | SI | Include Ingredients  |
| DOSEMAX_MaxDose | double |  |  | SI | Maximum Dose |
| DOSEMAX_MaxUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| DOSEMAX_RowId | varchar |  |  | NO | - |
| DOSEMAX_UpdatedDate | date |  |  | SI | Updated Date |
| DOSEMAX_UpdatedTime | time |  |  | SI | Updated Time |
| DOSEMAX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DOSEMAX_WeightFrom | double |  |  | SI | Weight From |
| DOSEMAX_WeightTo | double |  |  | SI | Weight To |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*