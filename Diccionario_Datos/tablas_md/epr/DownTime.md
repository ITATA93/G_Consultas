# epr.DownTime

**Schema:** epr
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DTDateFrom | date |  |  | SI | Downtime Date From |
| DTDateTo | date |  |  | SI | Downtime Date To |
| DTLocations | varchar |  |  | SI | Downtime locations |
| DTTimeFrom | time |  |  | SI | Downtime Time From |
| DTTimeTo | time |  |  | SI | Downtime Time To |
| DTUpdateDate | date |  |  | SI | - |
| DTUpdateTime | time |  |  | SI | - |
| DTUser | bigint |  |  | SI | Downtime User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*