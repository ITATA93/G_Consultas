# web_Msg.WorkFlow

**Schema:** web_Msg
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ActionGroupWorkFlow | bit |  |  | SI | Determines whether the workflow is intended to be ... |
| ActionTypes | varchar |  |  | SI | Defines the type of Active Clinical Notes Action t... |
| ClinPathTypeOrderingWorkFlow | bit |  |  | SI | Determines whether the workflow can be used as a C... |
| CycleSelection | bit |  |  | SI | Used for cycling a workflow for a set number of se... |
| Deprecated | bit |  |  | SI | - |
| DisplayWorkFlow | bit |  |  | SI | 70886 - dictate whether the workflow bar displays ... |
| FlowsheetActionTypes | varchar |  |  | SI | Defines the types of Flowsheet Action Type this wo... |
| ID | varchar |  |  | NO | - |
| JumpToList | bit |  |  | SI | Determines whether the workflow should return back... |
| Loop | bit |  |  | SI | Determines whether the workflow should return back... |
| Name | varchar |  |  | SI | - |
| OriginalWorkFlowIDs | varchar |  |  | SI | A list of the original workflow IDs of each indivi... |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReadOnly | bit |  |  | SI | - |
| ReasonDeprecated | varchar |  |  | SI | - |
| RowID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| TUIDlist | varchar |  |  | SI | A list of TUIDs corresponding to the URLs for each... |
| TransitionPositions | varchar |  |  | SI | A list of the WorkFlow positions that mark the tra... |
| URLExpression | varchar |  |  | SI | Defines the parameters passed into the workflow wh... |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |
| UseAsAction | bit |  |  | SI | Determines whether the workflow can be configured ... |
| UseAsFlowsheetAction | bit |  |  | SI | Determines whether the workflow can be configured ... |
| WorkFlowItems | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*