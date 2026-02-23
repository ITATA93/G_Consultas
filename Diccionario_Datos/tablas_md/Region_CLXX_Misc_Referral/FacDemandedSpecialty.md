# Region_CLXX_Misc_Referral.FacDemandedSpecialty

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CreateDateTime | timestamp |  |  | NO | - |
| CreateUserNationalId | varchar |  |  | SI | - |
| Deleted | bit |  |  | SI | - |
| DeletedDateTime | timestamp |  |  | SI | - |
| DeletedUser | bigint |  |  | SI | - |
| DemandingFacility | bigint |  |  | NO | - |
| Specialty | bigint |  |  | NO | - |
| UpdateDateTime | timestamp |  |  | NO | - |
| UpdateUserNationalId | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*