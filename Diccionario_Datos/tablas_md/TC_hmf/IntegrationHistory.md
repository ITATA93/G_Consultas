# TC_hmf.IntegrationHistory

**Schema:** TC_hmf
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFHIS_Action | varchar |  |  | SI | Trigger event eg. add, update, delete |
| HMFHIS_AdditionalInfo | varchar |  |  | SI | Add support for metadata to be added to message re... |
| HMFHIS_Date | date |  |  | SI | Date added to integration history |
| HMFHIS_EnsembleSessionID | varchar |  |  | SI | Ensemble Message SessionID
used to build url to v... |
| HMFHIS_ErrorDescription | varchar |  |  | SI | Error description from processing message  |
| HMFHIS_ErrorLocation | varchar |  |  | SI | Error Location |
| HMFHIS_ErrorStatus | varchar |  |  | SI | Error Status  |
| HMFHIS_Event | varchar |  |  | SI | Messages for trigger event
Contains all messages ... |
| HMFHIS_Integration_DR | bigint |  | FK | SI | Link to integration manager entry |
| HMFHIS_LinkHistory_DR | bigint |  | FK | SI | Link History ID used to create this entry |
| HMFHIS_LowPriority | bit |  |  | SI | Records low priority setting for outbound message |
| HMFHIS_Message | varchar |  |  | SI | Message direction (Outbound, Inbound, QueryOut, Qu... |
| HMFHIS_MessageID | varchar |  |  | SI | Message ControlID |
| HMFHIS_NewTriggerValues | varchar |  |  | SI | Stores new values for each property defined in the... |
| HMFHIS_OldTriggerValues | varchar |  |  | SI | Stores old values for each property defined in the... |
| HMFHIS_OriginalErrorDescription | varchar |  |  | SI | Original error description from processing message... |
| HMFHIS_PAADM_DR | bigint |  | FK | SI | Des Ref to PAADM |
| HMFHIS_PAPMI_DR | bigint |  | FK | SI | Des Ref to PAPMI |
| HMFHIS_ProcessID | varchar |  |  | SI | $JOB for the trigger event |
| HMFHIS_QueryRequestClass | varchar |  |  | SI | Query Request Class |
| HMFHIS_QueryRequestStream | longvarchar |  |  | SI | Query Request Message |
| HMFHIS_QueryResponseClass | varchar |  |  | SI | Query Response Class |
| HMFHIS_QueryResponseStream | longvarchar |  |  | SI | Query Response Message |
| HMFHIS_ResponseDate | date |  |  | SI | Date response message received |
| HMFHIS_ResponseTime | time |  |  | SI | Time response message received |
| HMFHIS_SDAContainer_DR | bigint |  | FK | SI | DEPRECATED |
| HMFHIS_SDAStream | longvarchar |  |  | SI | Current SDA stream |
| HMFHIS_SDAStreamClass | varchar |  |  | SI | Stream class name |
| HMFHIS_SchedulerID | varchar |  |  | SI | Scheduler ID from HMF-SYS processing - only activa... |
| HMFHIS_ScreenForm | varchar |  |  | SI | Trakcare trigger screenform |
| HMFHIS_Status | varchar |  |  | SI | Integration history entry status - pending, waitin... |
| HMFHIS_TableID | varchar |  |  | SI | RowID for trigger event |
| HMFHIS_TargetInterfaceList | varchar |  |  | SI | Target Interfaces |
| HMFHIS_Time | time |  |  | SI | Time added to integration history |
| HMFHIS_TriggerValues | varchar |  |  | SI | Stores specific property values for the trigger ev... |
| HMFHIS_Trigger_DR | bigint |  | FK | SI | - |
| HMFHIS_User | bigint |  |  | SI | User that triggered the message |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*