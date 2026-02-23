# SQLUser.SS_Interface

**Schema:** SQLUser
**Columnas:** 43
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INT_RowId | bigint | PK |  | NO | - |
| INT_ActionOnMaxNAKSend | varchar |  |  | SI | Action on max. No. of NAK send retries |
| INT_ActionOnMaxNAKsResp | varchar |  |  | SI | Action on max. No. of NAK responses |
| INT_ActionOnMaxRead | varchar |  |  | SI | Action on max. No. of read timeouts |
| INT_ActionOnMaxResponse | varchar |  |  | SI | Action on max. no. of responses timeouts |
| INT_ActionOnNAKResponse | varchar |  |  | SI | Action on NAK response |
| INT_ActionOnNoResponse | varchar |  |  | SI | Action on no response after message is sent |
| INT_CacheScript | varchar |  |  | SI | Cache Script |
| INT_CharacterSet | varchar |  |  | SI | National Language Support |
| INT_Code | varchar |  |  | NO | Code |
| INT_ConnectionType | varchar |  |  | SI | Connection Type |
| INT_DataDirection | varchar |  |  | SI | Data Direction |
| INT_DataType | varchar |  |  | SI | Data Type |
| INT_Desc | varchar |  |  | NO | Description |
| INT_EmailNotificationFrom | varchar |  |  | SI | Email Notification From |
| INT_EmailNotificationTo | varchar |  |  | SI | Email Notification To |
| INT_ExternalHostName | varchar |  |  | SI | External Host Name |
| INT_ExternalHostPort | varchar |  |  | SI | External Host Port |
| INT_FileAction | varchar |  |  | SI | File Action |
| INT_FileDirectory | varchar |  |  | SI | File Directory |
| INT_FileMoveDirectory | varchar |  |  | SI | File Move Directory |
| INT_FileMultiRecords | varchar |  |  | SI | File Multi Records |
| INT_FileName | varchar |  |  | SI | File Name |
| INT_FilePollingInterval | double |  |  | SI | File Polling Interval |
| INT_HL7_DR | varchar |  | FK | SI | Des Ref HL7 |
| INT_InterfaceType | varchar |  |  | SI | Interface Type |
| INT_LoggingLevel | varchar |  |  | SI | Logging Level |
| INT_MaxNAKSend | double |  |  | SI | Max. No. of NAK send retries |
| INT_MaxNAKsResp | double |  |  | SI | Max. No. of NAK responses allowed |
| INT_MaxRead | double |  |  | SI | Max. No. of read timeouts allowed |
| INT_MaxResponse | double |  |  | SI | Max. No. of response timeouts allowed |
| INT_NumRecordsPerFile | double |  |  | SI | Max Number Records Per File Outbound |
| INT_TimeWaitBeforeConnect | double |  |  | SI | Time Wait Before Connect |
| INT_TimeWaitBeforeSend | double |  |  | SI | Time Wait Before Send |
| INT_TimeWaitClientConnect | double |  |  | SI | Time Wait Client Connect |
| INT_TimeWaitClientSend | double |  |  | SI | Time Wait Client Send |
| INT_TimeWaitForComplete | double |  |  | SI | Time Wait For Complete |
| INT_TimeWaitForResponse | double |  |  | SI | Time Wait For Response |
| INT_TimeWaitPortConnect | double |  |  | SI | Time Wait Port Connect |
| INT_UnixOS | varchar |  |  | SI | Unix OS used |
| INT_UpdateDate | date |  |  | SI | Update Date |
| INT_UpdateTime | time |  |  | SI | Update Time |
| INT_UpdateUser_DR | bigint |  | FK | SI | Des Ref Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*