# Region_CLXX_Misc_Referral.Specialty

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Active | bit |  |  | NO | - |
| Code | varchar |  |  | NO | - |
| DefaultOfferingService | varchar |  |  | SI | Contiene la prestación por defecto, de ser una esp... |
| Description | varchar |  |  | NO | - |
| FacilityLevel | integer |  |  | SI | Can be 1 for Primary Care, 2 for Secondary Care e ... |
| SubSpecialtyOf | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*