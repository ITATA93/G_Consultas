# lab.CL_CollListNumberPatients

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLNP_ParRef | varchar | PK |  | NO | CL_CollectionListNumber Parent Reference |
| CLNP_Episode_DR | varchar |  | FK | NO | Episode DR |
| CLNP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*