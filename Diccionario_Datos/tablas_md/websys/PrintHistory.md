# websys.PrintHistory

> History of print jobs (and repints)

**Schema:** websys
**Columnas:** 47
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

*Descripción original:* History of print jobs (and repints)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BatchID | varchar |  |  | SI | BatchID is only set for members of a Batch Print.... |
| BatchSeq | varchar |  |  | SI | Sequence of an Item in a Batch.  |
| Computer | varchar |  |  | SI | Requesting Computer |
| DSN | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| DocumentSignID | bigint |  |  | SI | - |
| ErrorDescription | varchar |  |  | SI | Description of the error in the event that the pri... |
| FileSize | integer |  |  | SI | - |
| Filename | varchar |  |  | SI | User can request the the Report be printed to a fi... |
| HospitalDR | bigint |  | FK | SI | Log 52404 YC - Hospital |
| JobNumber | varchar |  |  | SI | Cache Job Number |
| LocationDR | bigint |  | FK | SI | Login Location of User calling print |
| MailCC | varchar |  |  | SI | For Email and Faxing |
| MailFrom | varchar |  |  | SI | For Email and Faxing |
| MailMessage | varchar |  |  | SI | - |
| MailSubject | varchar |  |  | SI | For Email and Faxing |
| MailTo | varchar |  |  | SI | For Email and Faxing |
| MethodType | varchar |  |  | SI | - |
| NoofCopies | integer |  |  | SI | - |
| P1 | varchar |  |  | SI | - |
| P1Short | varchar |  |  | SI | Short P1 |
| P2 | varchar |  |  | SI | - |
| P3 | varchar |  |  | SI | - |
| P4 | varchar |  |  | SI | - |
| P5 | varchar |  |  | SI | - |
| P6 | varchar |  |  | SI | - |
| P7 | varchar |  |  | SI | - |
| P8 | varchar |  |  | SI | - |
| P9 | varchar |  |  | SI | - |
| PrintDate | date |  |  | SI | DateTime that the report was Processed(attempted t... |
| PrintDuration | varchar |  |  | SI | Print Duration (in seconds) |
| PrintServer | integer |  |  | SI | - |
| PrintTime | time |  |  | SI | DateTime that the report was Processed(attempted t... |
| PrinterDR | bigint |  | FK | SI | - |
| Recipient | varchar |  |  | SI | - |
| ReportDR | bigint |  | FK | SI | - |
| Reprint | bit |  |  | SI | Log 51153 - AI - 13-07-2005 : Is this entry a repr... |
| RequestedDate | date |  |  | SI | - |
| RequestedReportHistoryDR | bigint |  | FK | SI | - |
| RequestedTime | time |  |  | SI | - |
| SaveOnly | bit |  |  | SI | Log 51153 - AI - 13-07-2005 : Should this entry on... |
| ServiceID | varchar |  |  | SI | MachineId of the Service that processed the Reques... |
| Status | varchar |  |  | SI | W - Waiting to Print.
I - Printing in progress,
... |
| UserDR | bigint |  | FK | SI | - |
| UserGroupDR | bigint |  | FK | SI | - |
| UserProfileDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*