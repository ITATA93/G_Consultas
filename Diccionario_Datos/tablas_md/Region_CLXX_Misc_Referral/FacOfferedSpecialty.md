# Region_CLXX_Misc_Referral.FacOfferedSpecialty

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| OfferingFacility | bigint |  |  | NO | - |
| OfferingLocation | bigint |  |  | SI | - |
| ReadyForReceiving | bit |  |  | SI | - |
| Specialty | bigint |  |  | NO | - |
| SpecialtyService | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*