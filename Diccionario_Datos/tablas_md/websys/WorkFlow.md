# websys.WorkFlow

> Definition of a sequenced set of WorkFlowItems

**Schema:** websys
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Definition of a sequenced set of WorkFlowItems

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActionGroupWorkFlow | bit |  |  | SI | Determines whether the workflow is intended to be ... |
| ActionTypes | varchar |  |  | SI | Defines the type of Active Clinical Notes Action t... |
| ClinPathTypeOrderingWorkFlow | bit |  |  | SI | Determines whether the workflow can be used as a C... |
| CycleSelection | bit |  |  | SI | Used for cycling a workflow for a set number of se... |
| Deprecated | bit |  |  | SI | - |
| DisplayWorkFlow | bit |  |  | SI | 70886 - dictate whether the workflow bar displays ... |
| FlowsheetActionTypes | varchar |  |  | SI | Defines the types of Flowsheet Action Type this wo... |
| JumpToList | bit |  |  | SI | Determines whether the workflow should return back... |
| Loop | bit |  |  | SI | Determines whether the workflow should return back... |
| Name | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReasonDeprecated | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| URLExpression | varchar |  |  | SI | Defines the parameters passed into the workflow wh... |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |
| UseAsAction | bit |  |  | SI | Determines whether the workflow can be configured ... |
| UseAsFlowsheetAction | bit |  |  | SI | Determines whether the workflow can be configured ... |
| WorkFlowItems | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*