# TC_hmf_Generator_Lib_Router_Process_Inbound.Thread1

**Schema:** TC_hmf_Generator_Lib_Router_Process_Inbound
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %ActivityStack | varchar |  |  | SI | This holds the activitystack for locating an activ... |
| %HandlerStack | varchar |  |  | SI | This holds the callstack for faulthanders |
| %PendingAlarmHandle | varchar |  |  | SI | This holds the handle the pending alarm request |
| %PendingTimeout | varchar |  |  | SI | This holds the name of the pending timeout call |
| %Status | integer |  |  | SI | This holds the run status of this machine |
| %SubroutineStack | varchar |  |  | SI | This holds the callstack for compensation handlers |
| %SyncName | varchar |  |  | SI | This holds the name attribute of the <sync> tag |
| %SyncTimedOut | integer |  |  | SI | This holds the timeout status of the most recent <... |
| _SyncResponses | varchar |  |  | SI | This holds a collection of responses that this thr... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*