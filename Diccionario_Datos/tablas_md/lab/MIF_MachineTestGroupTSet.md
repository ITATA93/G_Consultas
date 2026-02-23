# lab.MIF_MachineTestGroupTSet

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MITGS_ParRef | varchar | PK |  | NO | MIF_MachineTestGroup Parent Reference |
| MITGS_RowId | varchar |  |  | NO | - |
| MITGS_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*