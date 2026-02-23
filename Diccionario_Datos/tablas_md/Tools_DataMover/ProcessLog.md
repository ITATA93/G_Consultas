# Tools_DataMover.ProcessLog

**Schema:** Tools_DataMover
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ApptDateFrom | varchar |  |  | SI | - |
| ApptDateTo | varchar |  |  | SI | - |
| CareProviderCode | varchar |  |  | SI | - |
| LogonUser | varchar |  |  | SI | - |
| ProcessGUID | varchar |  |  | NO | Assigned GUID to unique identification across clie... |
| RemoteClientHostName | varchar |  |  | SI | - |
| RemoteClientSyncProcess | bigint |  |  | SI | Set when remote client finalize a sucessfull sync |
| Reseted | bit |  |  | SI | - |
| Running | bit |  |  | SI | - |
| StartDateTime | timestamp |  |  | NO | - |
| Status | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*