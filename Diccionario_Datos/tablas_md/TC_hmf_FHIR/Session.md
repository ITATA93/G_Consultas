# TC_hmf_FHIR.Session

**Schema:** TC_hmf_FHIR
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Expires | integer |  |  | SI | expire timestamp in seconds |
| InstanceKey | varchar |  |  | SI | The InstanceKey that identifies which FHIR endpoin... |
| PatientResourceId | varchar |  |  | SI | Patient MPIID as the FHIR Patient resource id - th... |
| Username | varchar |  |  | SI | Requesting username |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*