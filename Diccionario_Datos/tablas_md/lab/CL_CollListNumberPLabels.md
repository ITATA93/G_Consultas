# lab.CL_CollListNumberPLabels

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLNPL_ParRef | varchar | PK |  | NO | CL_CollectionListNumberPatients Parent Reference |
| CLNPL_Label_DR | varchar |  | FK | NO | Label DR |
| CLNPL_RowID | varchar |  |  | NO | - |
| CLNPL_Tests | varchar |  |  | SI | Tests |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*