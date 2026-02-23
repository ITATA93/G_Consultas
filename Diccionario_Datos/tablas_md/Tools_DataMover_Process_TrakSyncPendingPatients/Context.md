# Tools_DataMover_Process_TrakSyncPendingPatients.Context

**Schema:** Tools_DataMover_Process_TrakSyncPendingPatients
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contexto**. Datos de contexto de sesión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %LastError | varchar |  |  | SI | This holds last exception |
| %LastFault | varchar |  |  | SI | This holds the last thrown fault |
| %Process | bigint |  |  | SI | This holds the reference to the process object |
| AllRegNoInSync | varchar |  |  | SI | - |
| CallResponsesList | varchar |  |  | SI | - |
| CallsNames | varchar |  |  | SI | - |
| ClearDBResp | varchar |  |  | SI | - |
| CurrentCallName | varchar |  |  | SI | - |
| EndSyncFlag | bit |  |  | SI | - |
| EpisodesList | varchar |  |  | SI | - |
| ErrorMessage | varchar |  |  | SI | - |
| ErrorPatSyncMsg | varchar |  |  | SI | - |
| IncludeEpisodeTransactions | bit |  |  | SI | - |
| Index | varchar |  |  | SI | - |
| NotifyEventCallResponse | bigint |  |  | SI | - |
| NotifySyncIniCallName | varchar |  |  | SI | - |
| PatientSyncedIndex | varchar |  |  | SI | - |
| PatientsOnlyList | varchar |  |  | SI | - |
| PatientsSynced | varchar |  |  | SI | - |
| ProcessLogIndex | integer |  |  | SI | - |
| TrakProcessGUID | varchar |  |  | SI | - |
| UpdateQueueErrorStatus | varchar |  |  | SI | - |
| clearAllProcessData | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*