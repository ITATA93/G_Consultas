# lab.MIF_MachineResultsBugs

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRB_ParRef | varchar | PK |  | NO | MIF_MachineResultHeader Parent Reference |
| MIRB_Bug_DR | varchar |  | FK | SI | Bug DR |
| MIRB_RowID | varchar |  |  | NO | - |
| MIRB_Sequence | numeric |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*