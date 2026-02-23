# lab.HI_HistDayBookVisAccBlock

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIVAB_ParRef | varchar | PK |  | NO | HI_HistDayBookVisitAccession Parent Reference |
| HIVAB_Block | varchar |  |  | NO | Block |
| HIVAB_Code | varchar |  |  | SI | Block Code |
| HIVAB_ParentBlockOrder_DR | varchar |  | FK | SI | Parent Block Order DR |
| HIVAB_Printed | varchar |  |  | SI | Printed |
| HIVAB_RowId | varchar |  |  | NO | - |
| HIVAB_Shift | double |  |  | SI | Shift |
| HIVAB_xxx | varchar |  |  | SI | Block Description |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*