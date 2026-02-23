# SQLUser.RB_ApptOutcomeStage

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STOPST_ParRef | varchar | PK |  | NO | RB_ApptOutcome Parent Reference |
| STOPST_Childsub | double |  |  | NO | Childsub |
| STOPST_OutcomeType | varchar |  |  | SI | Outcome Type |
| STOPST_RowId | varchar |  |  | NO | - |
| STOPST_StageStop_DR | varchar |  | FK | SI | Des Ref PACRefTemplateStageType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*