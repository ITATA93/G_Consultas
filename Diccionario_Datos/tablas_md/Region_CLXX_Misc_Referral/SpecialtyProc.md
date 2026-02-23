# Region_CLXX_Misc_Referral.SpecialtyProc

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Specialty | bigint | PK |  | NO | - |
| CreateDateTime | timestamp |  |  | NO | - |
| CreateUserNationalId | varchar |  |  | SI | - |
| DischargeEvent | integer |  |  | NO | Esta propiedad controla si el egreso de paciente d... |
| ID | varchar |  |  | NO | - |
| Procedure | varchar |  |  | SI | - |
| UpdateDateTime | timestamp |  |  | NO | - |
| UpdateUserNationalId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*