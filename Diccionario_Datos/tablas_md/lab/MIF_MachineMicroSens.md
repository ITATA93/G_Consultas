# lab.MIF_MachineMicroSens

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIMS_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIMS_MachineSensitivity | varchar |  |  | NO | Machine Sensitivity |
| MIMS_RowID | varchar |  |  | NO | - |
| MIMS_Sensitivity_DR | varchar |  | FK | SI | Sensitivity DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*