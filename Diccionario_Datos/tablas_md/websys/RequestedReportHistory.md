# websys.RequestedReportHistory

**Schema:** websys
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ARCBillProgressStatusDR | bigint |  | FK | SI | Follow Up Stage Status DR |
| AppointmentDR | varchar |  | FK | SI | Appointment DR |
| BillDR | bigint |  | FK | SI | Bill DR |
| Comment | varchar |  |  | SI | General Comment |
| CreationDate | date |  |  | SI | Creation Date |
| CreationLogonLocation | bigint |  |  | SI | Creation Logon Location |
| CreationTime | time |  |  | SI | Creation Time |
| CreationUserDR | bigint |  | FK | SI | Creation User DR |
| DateForFollowup | date |  |  | SI | Date For Followup |
| DischargeSummaryID | varchar |  |  | SI | Discharge Summary DR |
| DocumentDR | bigint |  | FK | SI | Document |
| EpisodeDR | bigint |  | FK | SI | Episode DR |
| FOLUPSEQFollowUpStageDR | varchar |  | FK | SI | Follow Up Stage |
| FollowedUpReport | bigint |  |  | SI | Followed Up Report DR |
| LastDateReprinted | date |  |  | SI | Last Date Reprinted |
| LastReprintLogonLoc | bigint |  |  | SI | Last Reprint Logon Location |
| LastReprintUserDR | bigint |  | FK | SI | Last Reprint User DR |
| LastTimeReprinted | time |  |  | SI | Last Time Reprinted |
| LastUpdateDate | date |  |  | SI | Last Update Date |
| LastUpdateLogonLoc | bigint |  |  | SI | Last Update Logon Location |
| LastUpdateTime | time |  |  | SI | Last Update Time |
| LastUpdateUserDR | bigint |  | FK | SI | Last Update User DR |
| MHDocumentDR | bigint |  | FK | SI | Mental Health Document DR |
| NoTimesPrinted | integer |  |  | SI | Number of Times Reprinted |
| PatientDR | bigint |  | FK | SI | Patient DR |
| ReportDR | bigint |  | FK | SI | - |
| ResponseDate | date |  |  | SI | Response Date |
| Status | varchar |  |  | SI | Report Status |
| WaitingListDR | bigint |  | FK | SI | Waiting List DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*