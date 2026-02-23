# TC_hmf_FHIR.SyncHistory

**Schema:** TC_hmf_FHIR
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Resource | varchar |  |  | SI | TC Resource - support Patient,Location,CareProv |
| ResourceId | varchar |  |  | SI | TC Resource rowID |
| SyncData | varchar |  |  | SI | Sync data - optional sync details eg data segments... |
| SyncDateTimeH | varchar |  |  | SI | Sync date+time in $h format |
| SyncUser | varchar |  |  | SI | Requesting username |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*