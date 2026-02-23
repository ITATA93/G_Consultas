# lab.HI_HistDayBookVisAccTS

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIVAT_ParRef | varchar | PK |  | NO | HI_HistDayBookVisitAccession Parent Reference |
| HIVAT_EpisodeTestSet_DR | varchar |  | FK | NO | Episode Test Set DR |
| HIVAT_RowID | varchar |  |  | NO | - |
| HIVAT_xxx1 | varchar |  |  | SI | TCode |
| HIVAT_xxx2 | varchar |  |  | SI | Comments |
| HIVAT_xxx3 | varchar |  |  | SI | Retain sample |
| HIVAT_xxx4 | varchar |  |  | SI | Test Set |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*