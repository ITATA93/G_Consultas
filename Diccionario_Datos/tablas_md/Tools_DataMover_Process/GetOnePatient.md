# Tools_DataMover_Process.GetOnePatient

**Schema:** Tools_DataMover_Process
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %ConfigName | varchar |  |  | SI | return the name of config item |
| %ConfigQueueName | varchar |  |  | SI | return the name of queue as returned by the config... |
| %Context | bigint |  |  | SI | This property holds the context object |
| %Counter | integer |  |  | SI | This property holds the counter for delays and tim... |
| %IsCompleted | bit |  |  | SI | - |
| %IsTerminated | bit |  |  | SI | - |
| %IsTimerInterrupted | bit |  |  | SI | - |
| %MasterPendingResponsesOld | varchar |  |  | SI | This property maps to the old storage location of ... |
| %MessagesReceivedOld | varchar |  |  | SI | This property maps to the old storage location of ... |
| %MessagesSentOld | varchar |  |  | SI | This property maps to the old storage location of ... |
| %PrimaryRequestHeader | bigint |  |  | SI | protected properties |
| %PrimaryResponseHeader | bigint |  |  | SI | - |
| %QuitTask | integer |  |  | SI | Flag for returning an error that will exit the OnT... |
| %RepliedStatus | integer |  |  | SI | - |
| %SessionId | integer |  |  | SI | The session id of the current message being proces... |
| %StatusCode | varchar |  |  | SI | - |
| %SuperSession | varchar |  |  | SI | The SuperSession id of the current message being p... |
| %Thread | bigint |  |  | SI | This property holds the instance of the initial th... |
| %TimeCompleted | timestamp |  |  | SI | - |
| %TimeCreated | timestamp |  |  | SI | - |
| %responseClassName | varchar |  |  | SI | - |
| %responseId | varchar |  |  | SI | - |
| Adapter | integer |  |  | SI | The adapter instance |
| AlertGroups | varchar |  |  | SI | The Alert Groups to which this item belongs. |
| AlertOnError | bit |  |  | SI | Send an Alert message whenever an error occurs her... |
| AlertRetryGracePeriod | numeric |  |  | SI | When AlertOnError is True and the Process is retry... |
| BusinessPartner | varchar |  |  | SI | Name of a Business Partner Profile associated with... |
| FailureTimeout | numeric |  |  | SI | How long to keep retrying before giving up and ret... |
| InactivityTimeout | numeric |  |  | SI | Send an Alert message if this number of seconds el... |
| MapName | varchar |  |  | SI | Map name |
| MapVersion | varchar |  |  | SI | Map version |
| QueueCountAlert | numeric |  |  | SI | Number of messages on this item's queue needed to ... |
| QueueWaitAlert | numeric |  |  | SI | The number of seconds a message at the front of th... |
| ReplyCodeActions | varchar |  |  | SI | <p>A comma-separated list of codes specifying what... |
| Retry | bit |  |  | SI | Set this property to 1 if you want to retry the cu... |
| RetryInterval | numeric |  |  | SI | How frequently to retry access to the output syste... |
| RuleLogging | varchar |  |  | SI | This set of flags controls the logging performed b... |
| SuspendMessage | bit |  |  | SI | Set this property to 1 if you want to mark the cur... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*