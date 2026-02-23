# SQLUser.LB_QCBatchLevelGroupTestItem

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCBLGTI_ParRef | varchar | PK |  | NO | Parent Value Group |
| LBQCBLGTI_Active | varchar |  |  | SI | Indicates if the test item is active or disabled |
| LBQCBLGTI_AllQCRequiredToPass | varchar |  |  | SI | QC from all other test items in the group must pas... |
| LBQCBLGTI_CalculationType | varchar |  |  | SI | Calculation Type
StandardType: LabQCCalculationTy... |
| LBQCBLGTI_Comments | varchar |  |  | SI | Comments |
| LBQCBLGTI_FloatingCV | varchar |  |  | SI | Floating Coefficent of Deviation
This will overwr... |
| LBQCBLGTI_FloatingMean | varchar |  |  | SI | Floating Mean
This will overwrite the Batch Level... |
| LBQCBLGTI_FloatingSD | varchar |  |  | SI | Floating Standard Deviation
This will overwrite t... |
| LBQCBLGTI_NumberOfSD | varchar |  |  | SI | Target Sample size |
| LBQCBLGTI_RowID | varchar |  |  | NO | - |
| LBQCBLGTI_Status | varchar |  |  | SI | Test Item Status
StandardType: LabQCTestItemStatu... |
| LBQCBLGTI_TargetCV | varchar |  |  | SI | Target Coefficent of Deviation
This will overwrit... |
| LBQCBLGTI_TargetMaximumValue | varchar |  |  | SI | Target Maximum Value |
| LBQCBLGTI_TargetMean | varchar |  |  | SI | Target Mean
This will overwrite the Batch Level D... |
| LBQCBLGTI_TargetMinimumValue | varchar |  |  | SI | Target Minimum Value |
| LBQCBLGTI_TargetSD | varchar |  |  | SI | Target Standard Deviation
This will overwrite the... |
| LBQCBLGTI_TargetValues | varchar |  |  | SI | Target Value
Non-numeric target values |
| LBQCBLGTI_TestItem_DR | bigint |  | FK | SI | Link to the code table test item |
| LBQCBLGTI_TitreFrom | varchar |  |  | SI | Titre target value from |
| LBQCBLGTI_TitreTo | varchar |  |  | SI | Titre target value to |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*