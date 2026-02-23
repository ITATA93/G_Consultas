# SQLUser.PA_QuestionnaireAnswers

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANS_ParRef | varchar | PK |  | NO | PA_Questionnaire Parent Reference |
| ANS_Childsub | double |  |  | NO | Childsub |
| ANS_RowId | varchar |  |  | NO | - |
| ANS_UserWinControl_DR | varchar |  | FK | SI | Des Ref UserWinControl |
| ANS_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*