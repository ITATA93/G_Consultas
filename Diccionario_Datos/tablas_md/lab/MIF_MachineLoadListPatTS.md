# lab.MIF_MachineLoadListPatTS

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MILLT_ParRef | varchar | PK |  | NO | MIF_MachineLoadListPatients Parent Reference |
| MILLT_Childsub | double |  |  | NO | Childsub |
| MILLT_RowId | varchar |  |  | NO | - |
| MILLT_TestSetCounter | varchar |  |  | SI | Test Set Counter |
| MILLT_TestSet_DR | varchar |  | FK | SI | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*