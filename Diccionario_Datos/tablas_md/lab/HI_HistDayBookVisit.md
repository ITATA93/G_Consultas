# lab.HI_HistDayBookVisit

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIDBV_RowId | varchar | PK |  | NO | - |
| HIDBV_Epis_DR | varchar |  | FK | NO | Des Ref Epis |
| HIDBV_History | varchar |  |  | SI | History |
| HIDBV_Label | varchar |  |  | SI | Label |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*