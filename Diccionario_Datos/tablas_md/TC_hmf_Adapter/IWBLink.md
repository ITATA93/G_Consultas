# TC_hmf_Adapter.IWBLink

**Schema:** TC_hmf_Adapter
**Columnas:** 43
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFADAPIWB_ActionOnMaxNAKSend | varchar |  |  | SI | Action on max. No. of NAK send retries |
| HMFADAPIWB_ActionOnMaxNAKsResp | varchar |  |  | SI | Action on max. No. of NAK responses |
| HMFADAPIWB_ActionOnMaxRead | varchar |  |  | SI | Action on max. No. of read timeouts |
| HMFADAPIWB_ActionOnMaxResponse | varchar |  |  | SI | Action on max. no. of responses timeouts |
| HMFADAPIWB_ActionOnNAKResponse | varchar |  |  | SI | Action on NAK response |
| HMFADAPIWB_ActionOnNoResponse | varchar |  |  | SI | Action on no response after message is sent |
| HMFADAPIWB_CacheScript | varchar |  |  | SI | Cache Script |
| HMFADAPIWB_CharacterSet | varchar |  |  | SI | National Language Support |
| HMFADAPIWB_Code | varchar |  |  | NO | Code |
| HMFADAPIWB_ConnectionType | varchar |  |  | SI | Connection Type |
| HMFADAPIWB_DataDirection | varchar |  |  | SI | Data Direction |
| HMFADAPIWB_DataType | varchar |  |  | SI | Data Type |
| HMFADAPIWB_Desc | varchar |  |  | NO | Description |
| HMFADAPIWB_EmailNotificationFrom | varchar |  |  | SI | Email Notification From |
| HMFADAPIWB_EmailNotificationTo | varchar |  |  | SI | Email Notification To |
| HMFADAPIWB_ExternalHostName | varchar |  |  | SI | External Host Name |
| HMFADAPIWB_ExternalHostPort | varchar |  |  | SI | External Host Port |
| HMFADAPIWB_FileAction | varchar |  |  | SI | File Action |
| HMFADAPIWB_FileDirectory | varchar |  |  | SI | File Directory |
| HMFADAPIWB_FileMoveDirectory | varchar |  |  | SI | File Move Directory |
| HMFADAPIWB_FileMultiRecords | varchar |  |  | SI | File Multi Records |
| HMFADAPIWB_FileName | varchar |  |  | SI | File Name |
| HMFADAPIWB_FilePollingInterval | double |  |  | SI | File Polling Interval |
| HMFADAPIWB_HL7DR | longvarchar |  | FK | SI | Des Ref HL7 |
| HMFADAPIWB_InterfaceType | varchar |  |  | SI | Interface Type |
| HMFADAPIWB_LoggingLevel | varchar |  |  | SI | Logging Level |
| HMFADAPIWB_MaxNAKSend | double |  |  | SI | Max. No. of NAK send retries |
| HMFADAPIWB_MaxNAKsResp | double |  |  | SI | Max. No. of NAK responses allowed |
| HMFADAPIWB_MaxRead | double |  |  | SI | Max. No. of read timeouts allowed |
| HMFADAPIWB_MaxResponse | double |  |  | SI | Max. No. of response timeouts allowed |
| HMFADAPIWB_NumRecordsPerFile | double |  |  | SI | Max Number Records Per File Outbound |
| HMFADAPIWB_TimeWaitBeforeConnect | double |  |  | SI | Time Wait Before Connect |
| HMFADAPIWB_TimeWaitBeforeSend | double |  |  | SI | Time Wait Before Send |
| HMFADAPIWB_TimeWaitClientConnect | double |  |  | SI | Time Wait Client Connect |
| HMFADAPIWB_TimeWaitClientSend | double |  |  | SI | Time Wait Client Send |
| HMFADAPIWB_TimeWaitForComplete | double |  |  | SI | Time Wait For Complete |
| HMFADAPIWB_TimeWaitForResponse | double |  |  | SI | Time Wait For Response |
| HMFADAPIWB_TimeWaitPortConnect | double |  |  | SI | Time Wait Port Connect |
| HMFADAPIWB_UnixOS | varchar |  |  | SI | Unix OS used |
| HMFADAPIWB_UpdateDate | date |  |  | SI | Update Date |
| HMFADAPIWB_UpdateTime | time |  |  | SI | Update Time |
| HMFADAPIWB_UpdateUserDR | bigint |  | FK | SI | Des Ref Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*