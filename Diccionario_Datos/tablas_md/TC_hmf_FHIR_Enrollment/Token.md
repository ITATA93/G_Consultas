# TC_hmf_FHIR_Enrollment.Token

**Schema:** TC_hmf_FHIR_Enrollment
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| ActivationToken | varchar |  |  | NO | Activation token linked to TC MRN |
| TCMRN | varchar |  |  | NO | TC MRN  |
| TokenExpiryDate | date |  |  | NO | Token expiry date |
| UserDOB | date |  |  | NO | User DOB (used for verification) |
| UserEmail | varchar |  |  | NO | User Email (used for verification) |
| UserFullName | varchar |  |  | NO | User Email (used for verification) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*