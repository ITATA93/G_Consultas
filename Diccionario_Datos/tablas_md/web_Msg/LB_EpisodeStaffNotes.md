# web_Msg.LB_EpisodeStaffNotes

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| HTMLComments | longvarchar |  |  | SI | Temporary stream that stores the comment text unti... |
| ID | varchar |  |  | NO | - |
| LBEPSN_Date | date |  |  | SI | Date of  note |
| LBEPSN_Notes_DR | bigint |  | FK | SI | Note as websys.Document  (HTML = OTHER)
HTMLRichT... |
| LBEPSN_ParRef | bigint |  |  | SI | - |
| LBEPSN_RowID | varchar |  |  | SI | - |
| LBEPSN_Time | time |  |  | SI | Time of note |
| LBEPSN_Type_DR | bigint |  | FK | SI | Link to the code table staff notes type |
| LBEPSN_User_DR | bigint |  | FK | SI | Link to the user that created the note |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*