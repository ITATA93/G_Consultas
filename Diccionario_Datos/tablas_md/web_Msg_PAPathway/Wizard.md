# web_Msg_PAPathway.Wizard

**Schema:** web_Msg_PAPathway
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ActivitiesSelected | varchar |  |  | SI | Number of  Activities selected in this session |
| EpisodeID | varchar |  |  | SI | EpisodeID |
| ID | varchar |  |  | NO | - |
| InterventionItemID | varchar |  |  | SI | Intervention PathwayItem ID |
| OutcomeID | varchar |  |  | SI | Outcome ID |
| OutcomeItemID | varchar |  |  | SI | Outcome PathwayItem ID |
| PathwayID | varchar |  |  | SI | PathwayID |
| ProblemID | varchar |  |  | SI | Problem ID |
| QuestionnaireID | varchar |  |  | SI | The ID When Questionnaire Saved |
| QuestionnaireTypeID | varchar |  |  | SI | Questionnaire Type ID: RowID from Code Table |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SwitchControl | varchar |  |  | SI | Switch Control to contain Component Name |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*