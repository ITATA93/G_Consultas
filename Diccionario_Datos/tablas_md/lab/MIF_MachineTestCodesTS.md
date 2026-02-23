# lab.MIF_MachineTestCodesTS

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIDTS_ParRef | varchar | PK |  | NO | MIF_MachineSetCodes Parent Reference |
| MIDTS_Mandatory | varchar |  |  | SI | Mandatory |
| MIDTS_RowId | varchar |  |  | NO | - |
| MIDTS_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*