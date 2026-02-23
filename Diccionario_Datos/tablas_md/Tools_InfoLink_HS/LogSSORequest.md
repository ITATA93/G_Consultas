# Tools_InfoLink_HS.LogSSORequest

**Schema:** Tools_InfoLink_HS
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Attributes | varchar |  |  | SI | - |
| ErrorMsg | varchar |  |  | SI | - |
| FederationId | varchar |  |  | SI | - |
| HealthShareRole | varchar |  |  | SI | - |
| HospitalId | varchar |  |  | SI | - |
| PatientId | varchar |  |  | SI | - |
| RequestDate | date |  |  | SI | - |
| RequestTime | time |  |  | SI | - |
| SAMLResponse | varchar |  |  | SI | - |
| SecurityGroupId | varchar |  |  | SI | - |
| Success | bit |  |  | SI | - |
| UserId | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*