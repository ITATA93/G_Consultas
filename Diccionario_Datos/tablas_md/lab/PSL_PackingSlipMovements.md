# lab.PSL_PackingSlipMovements

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PSLM_ParRef | varchar | PK |  | NO | PSL_PackingSlip Parent Reference |
| PSLM_Episode_DR | varchar |  | FK | NO | Episode DR |
| PSLM_MovementID | varchar |  |  | NO | Movement ID |
| PSLM_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*