# lab.MIF_MachineFlags

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIFL_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIFL_Flag_DR | varchar |  | FK | SI | Flag DR |
| MIFL_MachineFlag | varchar |  |  | NO | Machine Flag |
| MIFL_RejectResult | varchar |  |  | SI | Reject result |
| MIFL_RowID | varchar |  |  | NO | - |
| MIFL_xxx | varchar |  |  | SI | not used |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*