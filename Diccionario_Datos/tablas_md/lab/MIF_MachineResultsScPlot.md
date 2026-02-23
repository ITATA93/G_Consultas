# lab.MIF_MachineResultsScPlot

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRS_ParRef | varchar | PK |  | NO | MIF_MachineResultHeader Parent Reference |
| MIRS_Data | varchar |  |  | SI | Data |
| MIRS_Order | numeric |  |  | NO | Order number |
| MIRS_RowID | varchar |  |  | NO | - |
| MIRS_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*