# lab.MIF_MachineMicroBugs

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIMB_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIMB_Bug_DR | varchar |  | FK | SI | Bug DR |
| MIMB_MachineBug | varchar |  |  | NO | Machine Bug |
| MIMB_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*