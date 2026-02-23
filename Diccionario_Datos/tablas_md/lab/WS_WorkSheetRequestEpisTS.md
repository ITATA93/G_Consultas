# lab.WS_WorkSheetRequestEpisTS

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKSRT_ParRef | varchar | PK |  | NO | WS_WorkSheetRequestEpisode Parent Reference |
| WKSRT_RowID | varchar |  |  | NO | - |
| WKSRT_TestSetCounter | double |  |  | NO | Test Set Counter |
| WKSRT_TestSet_DR | varchar |  | FK | NO | Test Set DR |
| WKSRT_xxx1 | varchar |  |  | SI | TestSet Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*