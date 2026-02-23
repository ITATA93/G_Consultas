# lab.MIF_MachineTestGroupTCode

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MITGI_ParRef | varchar | PK |  | NO | MIF_MachineTestGroup Parent Reference |
| MITGI_Display | varchar |  |  | SI | Display |
| MITGI_Order | numeric |  |  | SI | Display order |
| MITGI_RowID | varchar |  |  | NO | - |
| MITGI_TestCode_DR | varchar |  | FK | NO | Test Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*