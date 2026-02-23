# Region_CLXX_Misc_Referral.Rule

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Deleted | bit |  |  | SI | - |
| DeletedDateTime | timestamp |  |  | SI | - |
| DeletedUser | bigint |  |  | SI | - |
| Diagnosis | bigint |  |  | SI | - |
| FromFacility | bigint |  |  | NO | - |
| Specialty | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*