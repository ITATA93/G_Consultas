# websys.MonitorApp

> "Capture and store a variety of applicaton level measures.<br/>

**Schema:** websys
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Capture and store a variety of applicaton level measures.<br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActiveBedsCount | integer |  |  | SI | Count of bed having active users in SS_User |
| ActiveHospitalsCount | integer |  |  | SI | Hospital location count
Derived from active locat... |
| ActiveLocationsCount | integer |  |  | SI | Active location count |
| ActiveSecurityGroupsCount | integer |  |  | SI | Count of security groups having active users in SS... |
| ActiveUsersCount | integer |  |  | SI | Count of active users in SS_User |
| AppointmentCount | integer |  |  | SI | - |
| BillCount | integer |  |  | SI | - |
| EpisodeCountEmergency | integer |  |  | SI | - |
| EpisodeCountInpatient | integer |  |  | SI | episode type |
| EpisodeCountOutpatient | integer |  |  | SI | - |
| EpisodeCountTotal | integer |  |  | SI | - |
| EpisodeIDCounter | integer |  |  | SI | Episode ID Counter ^PAADM(0) |
| EpisodePeakPerHourCount | integer |  |  | SI | - |
| EpisodePeakPerHourTime | time |  |  | SI | - |
| EpisodePeakPerMinuteCount | integer |  |  | SI | - |
| EpisodePeakPerMinuteTime | time |  |  | SI | - |
| LETestCountTotal | integer |  |  | SI | - |
| LETestItemsCountTotal | integer |  |  | SI | - |
| LETestItemsPeakPerHourCount | integer |  |  | SI | - |
| LETestItemsPeakPerHourTime | time |  |  | SI | - |
| LETestItemsPeakPerMinuteCount | integer |  |  | SI | - |
| LETestItemsPeakPerMinuteTime | time |  |  | SI | - |
| LETestPeakPerHourCount | integer |  |  | SI | - |
| LETestPeakPerHourTime | time |  |  | SI | - |
| LETestPeakPerMinuteCount | integer |  |  | SI | - |
| LETestPeakPerMinuteTime | time |  |  | SI | - |
| LabEpisodeCountTotal | integer |  |  | SI | - |
| LabEpisodePeakPerHourCount | integer |  |  | SI | - |
| LabEpisodePeakPerHourTime | time |  |  | SI | - |
| LabEpisodePeakPerMinuteCount | integer |  |  | SI | - |
| LabEpisodePeakPerMinuteTime | time |  |  | SI | - |
| MaxConcurrentUsersCount | integer |  |  | SI | Maximum concurrent user count
Derived from websys... |
| ObservationCount | integer |  |  | SI | Count of observation entries |
| OrderCountConsulation | integer |  |  | SI | - |
| OrderCountDental | integer |  |  | SI | - |
| OrderCountDiet | integer |  |  | SI | - |
| OrderCountIV | integer |  |  | SI | - |
| OrderCountImaging | integer |  |  | SI | - |
| OrderCountLab | integer |  |  | SI | - |
| OrderCountMedication | integer |  |  | SI | - |
| OrderCountOthers | integer |  |  | SI | - |
| OrderCountPrice | integer |  |  | SI | - |
| OrderCountRehab | integer |  |  | SI | - |
| OrderCountTotal | integer |  |  | SI | - |
| OrderPeakPerHourCount | integer |  |  | SI | - |
| OrderPeakPerHourTime | time |  |  | SI | - |
| OrderPeakPerMinuteCount | integer |  |  | SI | - |
| OrderPeakPerMinuteTime | time |  |  | SI | - |
| PatientIDCounter | integer |  |  | SI | Patient ID Counter ^PAPER(0) |
| PrescriptionCount | integer |  |  | SI | - |
| PrintCountDeferred | integer |  |  | SI | Print type |
| PrintCountError | integer |  |  | SI | - |
| PrintCountPendingPrinter | integer |  |  | SI | - |
| PrintCountPreviewed | integer |  |  | SI | - |
| PrintCountPrinted | integer |  |  | SI | - |
| PrintCountSigned | integer |  |  | SI | - |
| PrintCountTotal | integer |  |  | SI | - |
| PrintCountUnsigned | integer |  |  | SI | - |
| PrintPeakPerHourCount | integer |  |  | SI | - |
| PrintPeakPerHourTime | time |  |  | SI | - |
| PrintPeakPerMinuteCount | integer |  |  | SI | - |
| PrintPeakPerMinuteTime | time |  |  | SI | - |
| ReceiptCount | integer |  |  | SI | - |
| ResultCount | integer |  |  | SI | - |
| RunDate | date |  |  | SI | Date this run was started
RunDate and RunTime uni... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*