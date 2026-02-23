# Region_CLXX_Utility_Log.LogEvent

**Schema:** Region_CLXX_Utility_Log
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AllVariables | varchar |  |  | SI | For errors, content of all variables available at ... |
| DataClassName | varchar |  |  | SI | Persistent data class name associated to the event |
| DataId | varchar |  |  | SI | Persistent data id associated to the event |
| DataValue | varchar |  |  | SI | Data value associated to the event when it's not a... |
| DataValueShort | varchar |  |  | SI | Short version of the data value associated to the ... |
| DateLogged | varchar |  |  | SI | Date when the event was logged (to optimize querie... |
| DateTimeLogged | varchar |  |  | SI | Date-time when the event was logged |
| EpisodeID | varchar |  |  | SI | 'EpisodeID' value in %request when log event is cr... |
| Job | varchar |  |  | SI | Identifies the job from which this event was logge... |
| LogGUID | varchar |  |  | SI | Log GUID : many events can share the same GUID (si... |
| PatientID | varchar |  |  | SI | 'PatientID' value in %request when log event is cr... |
| Stack | varchar |  |  | SI | For errors, contents of the stack at the time the ... |
| TextEvent | varchar |  |  | SI | User-supplied description of the event |
| TitleEvent | varchar |  |  | SI | User-supplied title of the event |
| TypeEvent | varchar |  |  | SI | What type of event : Error, Warning, Info, Trace, ... |
| UserAddress | varchar |  |  | SI | User address location |
| UserName | varchar |  |  | SI | Who posts this event |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*