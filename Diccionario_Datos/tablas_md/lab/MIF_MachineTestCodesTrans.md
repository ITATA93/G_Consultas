# lab.MIF_MachineTestCodesTrans

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRT_ParRef | varchar | PK |  | NO | MIF_MachineSetCodes Parent Reference |
| MIRT_Comments | varchar |  |  | SI | Comments |
| MIRT_Result | varchar |  |  | NO | Result |
| MIRT_RowId | varchar |  |  | NO | - |
| MIRT_xxx | varchar |  |  | SI | Operand |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*