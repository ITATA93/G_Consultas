# SQLUser.RB_ResOTSessionDeBriefDoc

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | varchar | PK |  | NO | RB_ResOTSessionDeBrief Parent Reference |
| DOC_BriefFlag | varchar |  |  | SI | Brief/Debrief Flag |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_Doc_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| DOC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*