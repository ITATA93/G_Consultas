# lab.MIF_MachineTestSet

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MITS_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MITS_AltInstrument_DR | varchar |  | FK | SI | Alt Instrument |
| MITS_RowId | varchar |  |  | NO | - |
| MITS_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*