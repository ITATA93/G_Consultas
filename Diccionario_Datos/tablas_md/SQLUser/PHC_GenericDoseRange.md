# SQLUser.PHC_GenericDoseRange

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOSER_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| DOSER_AdminRoutes | varchar |  |  | SI | List of DOSERAdminRoutes  |
| DOSER_AgeFrom | double |  |  | SI | Age From |
| DOSER_AgeTo | double |  |  | SI | Age To |
| DOSER_AgeType | varchar |  |  | SI | Age Type  |
| DOSER_BSAFormula | varchar |  |  | SI | BSA Formula |
| DOSER_BSAFrom | double |  |  | SI | BSA From |
| DOSER_BSATo | double |  |  | SI | BSA To |
| DOSER_Childsub | double |  |  | NO | Childsub |
| DOSER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOSER_CreatedDate | date |  |  | SI | Created Date |
| DOSER_CreatedTime | time |  |  | SI | Created Time |
| DOSER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOSER_DoseCap | double |  |  | SI | Dose Cap |
| DOSER_DoseCapUOM_DR | bigint |  | FK | SI | Dose Cap UOM |
| DOSER_GenericRtForms_DR | varchar |  | FK | SI | Des Ref PHCGenericRtForms |
| DOSER_MaxDelivRate | double |  |  | SI | Maximum Delivery Rate |
| DOSER_MaxDelivRateMethod | varchar |  |  | SI | Maximum Delivery Rate Method |
| DOSER_MaxDelivRateUOM_DR | bigint |  | FK | SI | Maximum Delivery Rate UOM |
| DOSER_MaxDose | double |  |  | SI | Maximum Dose |
| DOSER_MaxDoseMethod | varchar |  |  | SI | Maximum Dose Method - except  'D - per day'  |
| DOSER_MaxDoseUOM_DR | bigint |  | FK | SI | Maximum Dose UOM |
| DOSER_MinDose | double |  |  | SI | Minimum Dose |
| DOSER_MinDoseMethod | varchar |  |  | SI | Minimum Dose Method - except  'D - per day'  |
| DOSER_MinDoseUOM_DR | bigint |  | FK | SI | Minimum Dose UOM |
| DOSER_RowId | varchar |  |  | NO | - |
| DOSER_UpdatedDate | date |  |  | SI | Updated Date |
| DOSER_UpdatedTime | time |  |  | SI | Updated Time |
| DOSER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DOSER_WeightFrom | double |  |  | SI | Weight From |
| DOSER_WeightTo | double |  |  | SI | Weight To |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*