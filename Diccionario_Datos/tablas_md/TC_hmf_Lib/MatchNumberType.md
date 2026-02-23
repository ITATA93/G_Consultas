# TC_hmf_Lib.MatchNumberType

**Schema:** TC_hmf_Lib
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFLIBNUMTYP_Code | varchar |  |  | NO | Number Type Code |
| HMFLIBNUMTYP_DateFrom | date |  |  | SI | Date From |
| HMFLIBNUMTYP_DateTo | date |  |  | SI | Date To |
| HMFLIBNUMTYP_Desc | varchar |  |  | SI | Number Type Description |
| HMFLIBNUMTYP_Enabled | bit |  |  | SI | Enabled Flag |
| HMFLIBNUMTYP_ExtCode | varchar |  |  | SI | Number Type External Code |
| HMFLIBNUMTYP_PatientDR | varchar |  | FK | SI | Number Type Database field |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*