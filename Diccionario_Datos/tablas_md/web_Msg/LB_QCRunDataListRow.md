# web_Msg.LB_QCRunDataListRow

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQCBL_Description | varchar |  |  | SI | - |
| LBQCBatchLevelGroupTestItemIDList | varchar |  |  | SI | - |
| LBQCRD_SequenceNumber | numeric |  |  | SI | - |
| LBQCR_BatchNumber | varchar |  |  | SI | - |
| LBQCR_RowID | varchar |  |  | SI | - |
| LBQCR_SequenceNumber | numeric |  |  | SI | - |
| LBQCR_StartDate | date |  |  | SI | - |
| LBQCR_StartTime | date |  |  | SI | - |
| LBQCR_ValueGroup | varchar |  |  | SI | - |
| LBQCRunDataIDList | varchar |  |  | SI | - |
| LBQCRunDataValueList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RowNumber | integer |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*