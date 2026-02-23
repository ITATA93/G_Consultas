# lab.CT_BugsAntActionsCond

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBUD_ParRef | varchar | PK |  | NO | CT_BugsAntiBioticsActions Parent Reference |
| CTBUD_AntibioticTherapy | varchar |  |  | SI | Antibiotic Therapy |
| CTBUD_Operand | varchar |  |  | SI | Operand |
| CTBUD_Order | double |  |  | NO | Order number |
| CTBUD_RowID | varchar |  |  | NO | - |
| CTBUD_SensitivityResult_DR | varchar |  | FK | SI | Sensitivity Result |
| CTBUD_Table | varchar |  |  | SI | Table |
| CTBUD_TableField | varchar |  |  | SI | Table Field |
| CTBUD_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*