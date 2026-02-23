# Region_CLXX_Misc_Referral_Criteria.Above15Criteria

**Schema:** Region_CLXX_Misc_Referral_Criteria
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Rule | bigint | PK |  | NO | - |
| Active | bit |  |  | SI | - |
| CreateTime | timestamp |  |  | SI | - |
| CreateUser | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| Destination | bigint |  |  | NO | - |
| DestinationSpecialty | bigint |  |  | SI | - |
| Diagnosis | bigint |  |  | SI | - |
| DiagnosisControlLevel | integer |  |  | SI | 1-No GES, 2-GES, 3-Enfermedad Profesional |
| EpisodeComplexity | bigint |  |  | SI | - |
| HealthProblem | bigint |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| PatientSubscriptionFacility | bigint |  |  | SI | - |
| Procedure | varchar |  |  | SI | - |
| ProcesingPriority | integer |  |  | SI | - |
| WaitingListType | integer |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*