# lab.CTQC_GroupRules

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCGR_ParRef | varchar | PK |  | NO | QC_Group Parent Reference |
| CTQCGR_Colour | varchar |  |  | SI | Colour |
| CTQCGR_Comments | varchar |  |  | SI | Comments |
| CTQCGR_OrderNo | varchar |  |  | NO | Order No |
| CTQCGR_RowID | varchar |  |  | NO | - |
| CTQCGR_RulesDR | varchar |  | FK | SI | Rules DR |
| CTQCGR_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*