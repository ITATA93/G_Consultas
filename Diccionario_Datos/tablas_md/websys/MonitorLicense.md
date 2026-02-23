# websys.MonitorLicense

> Monitor Cache and TrakCare/LabTrak License

**Schema:** websys
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Monitor Cache and TrakCare/LabTrak License

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CacheAvailable | integer |  |  | SI | $system.License.LUAvailable() |
| CacheConsumed | integer |  |  | SI | $system.License.LUConsumed() |
| CacheMaxNo | integer |  |  | SI | $system.License.LUMaxConsumed() |
| CacheMinNo | integer |  |  | SI | $system.License.LUMinAvailable() |
| CacheTotal | integer |  |  | SI | $system.License.KeyLicenseUnits() |
| DateTimeStamp | timestamp |  |  | SI | DateTime stamp of recorded entry |
| DistributedAuthorized | integer |  |  | SI | Distributed License Units Authorized    |
| DistributedCurrentUsed | integer |  |  | SI | Distributed Current License Units Used |
| DistributedEnforced | integer |  |  | SI | Distributed License Units Enforced |
| DistributedMaxUsed | integer |  |  | SI | Distributed Maximum License Units Used |
| DistributedTrakCare | integer |  |  | SI | TrakCare Distributed license count |
| LabInstruments | integer |  |  | SI | LabTrak instrument count |
| LabTrak | integer |  |  | SI | LabTrak license count |
| MedTrak | integer |  |  | SI | TrakCare VB (MedTrak) license count |
| MonitorDate | date |  |  | SI | Date of recorded entry |
| MonitorTime | time |  |  | SI | Time of recorded entry |
| Namespace | varchar |  |  | SI | Namespace where license monitor was run - $ZNSPACE |
| ServerName | varchar |  |  | SI | contains the name of your current system - $ZUTIL(... |
| TrakCare | integer |  |  | SI | TrakCare license count |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*