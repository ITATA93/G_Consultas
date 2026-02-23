# web_Msg.LB_ProtocolProcedureListRow

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| EpisodeID | varchar |  |  | SI | Episode ID |
| ID | varchar |  |  | NO | - |
| LBEpisodeID | varchar |  |  | SI | LBEpisode ID |
| LBProtocolProcedureID | varchar |  |  | SI | ProtocolProcedure ID |
| LBSubjectID | varchar |  |  | SI | LBSubject ID |
| PatientID | varchar |  |  | SI | Patient ID |
| ReadOnly | bit |  |  | SI | - |
| RowCount | integer |  |  | SI | Row count |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*