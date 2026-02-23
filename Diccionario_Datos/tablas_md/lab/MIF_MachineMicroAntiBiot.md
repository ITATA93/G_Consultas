# lab.MIF_MachineMicroAntiBiot

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIMA_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIMA_AntiBiotic_DR | varchar |  | FK | SI | AntiBiotic DR |
| MIMA_MachineAntiBiotic | varchar |  |  | NO | Machine AntiBiotic |
| MIMA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*