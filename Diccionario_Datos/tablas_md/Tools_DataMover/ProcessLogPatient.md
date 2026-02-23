# Tools_DataMover.ProcessLogPatient

**Schema:** Tools_DataMover
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| DownloadDate | date |  |  | SI | - |
| DownloadUsername | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LastErrorMsg | varchar |  |  | SI | - |
| LastStatusUpdateTime | timestamp |  |  | SI | - |
| RemotePatientRegNo | varchar |  |  | NO | - |
| RemotePatientStatus | varchar |  |  | NO | - |
| SyncDate | date |  |  | SI | - |
| SyncFromRemoteChanges | bit |  |  | SI | - |
| SyncUsername | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*