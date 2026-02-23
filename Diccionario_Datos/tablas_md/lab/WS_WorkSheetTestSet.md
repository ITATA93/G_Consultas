# lab.WS_WorkSheetTestSet

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKSTS_ParRef | varchar | PK |  | NO | WS_WorkSheet Parent Reference |
| WKSTS_AllItems | varchar |  |  | SI | All Items |
| WKSTS_Input | varchar |  |  | SI | Input |
| WKSTS_RowId | varchar |  |  | NO | - |
| WKSTS_Sequence | double |  |  | SI | Sequence |
| WKSTS_TestItems | varchar |  |  | SI | Test Items |
| WKSTS_TestSet_DR | varchar |  | FK | NO | Des Ref Test Set |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*