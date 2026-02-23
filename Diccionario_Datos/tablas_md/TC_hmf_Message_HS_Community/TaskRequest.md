# TC_hmf_Message_HS_Community.TaskRequest

**Schema:** TC_hmf_Message_HS_Community
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AssigningAuthority | varchar |  |  | SI | Refers to the Assigning Authority in HSPortal.Acco... |
| Description | varchar |  |  | SI | Description of the task or task item |
| DueDate | date |  |  | SI | Due date of the task. This is when the task is exp... |
| DueTime | time |  |  | SI | Due time of the task. This is when the task is exp... |
| EpisodeID | varchar |  |  | SI | ID of the TrakCare episode associated with the tas... |
| EventDate | date |  |  | NO | Date of the event (e.g. appointment) related to th... |
| EventTime | time |  |  | SI | Time of the event (e.g. appointment) related to th... |
| ExternalTaskID | varchar |  |  | NO | Id of current task in trakcare |
| MRN | varchar |  |  | SI | MRN for this patient identifier. This is for use a... |
| ModifiedBy | varchar |  |  | SI | This is the system or effective userID who last mo... |
| Name | varchar |  |  | NO | Name of the task or task item |
| PCTaskID | varchar |  |  | SI | ID of the task in the PC system. Provide PCTaskID ... |
| Status | varchar |  |  | NO | Status of the task. Statuses include: ToDo, Remove... |
| TaskItems | varchar |  |  | SI | List of TaskItems to send |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*