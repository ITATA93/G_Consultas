# web_Msg.LB_EpisodeAction

**Schema:** web_Msg
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBEPA_CloseDate | date |  |  | SI | Date of closing the action item |
| LBEPA_CloseTime | time |  |  | SI | Time of closing the action item |
| LBEPA_CloseUser_DR | bigint |  | FK | SI | Link to the user that closed the action item |
| LBEPA_Comments | varchar |  |  | SI | Free text comments |
| LBEPA_EpisodeAction_DR | bigint |  | FK | SI | Link to the code table episode action
Required by... |
| LBEPA_OpenDate | date |  |  | SI | Date of opening the action item |
| LBEPA_OpenTime | time |  |  | SI | Time of opening the action item |
| LBEPA_OpenUser_DR | bigint |  | FK | SI | Link to the user that opened the action item |
| LBEPA_ParRef | bigint |  |  | SI | - |
| LBEPA_RowID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*