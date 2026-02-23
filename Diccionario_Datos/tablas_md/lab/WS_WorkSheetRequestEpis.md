# lab.WS_WorkSheetRequestEpis

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKSRE_ParRef | varchar | PK |  | NO | WS_WorkSheetRequest Parent Reference |
| WKSRE_RowId | varchar |  |  | NO | - |
| WKSRE_Sequence | double |  |  | SI | Sequence |
| WKSRE_Visit_DR | varchar |  | FK | NO | Visit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*