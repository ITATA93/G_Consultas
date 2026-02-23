# SQLUser.PHC_GenericRtFormsDefDose

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEFDOSE_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| DEFDOSE_AdminRoute_DR | bigint |  | FK | SI | Des Ref PHCAdministrationRoute |
| DEFDOSE_AgeFrom | double |  |  | SI | AgeFrom |
| DEFDOSE_AgeTo | double |  |  | SI | AgeTo |
| DEFDOSE_AgeType | varchar |  |  | SI | AgeType |
| DEFDOSE_BSAFormula | varchar |  |  | SI | BSAFormula |
| DEFDOSE_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| DEFDOSE_CalcMethod | varchar |  |  | SI | CalculationMethod |
| DEFDOSE_Childsub | double |  |  | NO | Childsub |
| DEFDOSE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEFDOSE_CreatedDate | date |  |  | SI | Created Date |
| DEFDOSE_CreatedTime | time |  |  | SI | Created Time |
| DEFDOSE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEFDOSE_DefDuration_DR | bigint |  | FK | SI | Des Ref PHCDuration |
| DEFDOSE_DefFreq_DR | bigint |  | FK | SI | Des Ref PHCFreq |
| DEFDOSE_DefMinDose | double |  |  | SI | DefMinDose |
| DEFDOSE_DurationUnit | varchar |  |  | SI |  DurationUnit |
| DEFDOSE_DurationValue | double |  |  | SI | DurationValue |
| DEFDOSE_Qty | double |  |  | SI | Quantity |
| DEFDOSE_RowId | varchar |  |  | NO | - |
| DEFDOSE_SecondSignAdm | varchar |  |  | SI | SecondSignAdm |
| DEFDOSE_UpdatedDate | date |  |  | SI | Updated Date |
| DEFDOSE_UpdatedTime | time |  |  | SI | Updated Time |
| DEFDOSE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DEFDOSE_Variance | double |  |  | SI | Varience |
| DEFDOSE_WeightFrom | double |  |  | SI | WeightFrom |
| DEFDOSE_WeightTo | double |  |  | SI | AgeTo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*