# lab.CT_BugGroupAntActCond

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGH_ParRef | varchar | PK |  | NO | CT_Bugs_Group_Antibiotics_Actions Parent Reference |
| CTBGH_AntibioticTherapy | varchar |  |  | SI | Antibiotic Therapy |
| CTBGH_Operand | varchar |  |  | SI | Operand |
| CTBGH_Order | double |  |  | NO | Order |
| CTBGH_RowID | varchar |  |  | NO | - |
| CTBGH_SensitivityResult_DR | varchar |  | FK | SI | Sensitivity Result |
| CTBGH_Table | varchar |  |  | SI | Table |
| CTBGH_TableField | varchar |  |  | SI | Table Field |
| CTBGH_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*