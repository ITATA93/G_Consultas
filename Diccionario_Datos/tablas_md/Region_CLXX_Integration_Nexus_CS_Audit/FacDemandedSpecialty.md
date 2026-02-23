# Region_CLXX_Integration_Nexus_CS_Audit.FacDemandedSpecialty

**Schema:** Region_CLXX_Integration_Nexus_CS_Audit
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Nexus**. Conexión con sistema externo Nexus.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ClassName | varchar |  |  | NO | - |
| DemandingFacilityCode | varchar |  |  | NO | - |
| EventDateTime | timestamp |  |  | NO | - |
| EventDescription | varchar |  |  | SI | - |
| EventType | varchar |  |  | NO | - |
| HasProcedure | bit |  |  | NO | - |
| LastNotificationStatus | varchar |  |  | NO | - |
| Notified | varchar |  |  | NO | - |
| ObjectId | varchar |  |  | NO | - |
| SpecialtyCode | varchar |  |  | NO | - |
| UserNationalId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*