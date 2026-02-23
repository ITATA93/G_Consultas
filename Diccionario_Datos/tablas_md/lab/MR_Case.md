# lab.MR_Case

**Schema:** lab
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRC_RowID | varchar | PK |  | NO | - |
| MRC_BodyCondition | varchar |  |  | SI | Body Condition |
| MRC_BodyHeight | varchar |  |  | SI | Body Height |
| MRC_BodyWeight | varchar |  |  | SI | Body Weight |
| MRC_BodyWidth | varchar |  |  | SI | Body Width |
| MRC_CaseNumber | varchar |  |  | NO | Case Number |
| MRC_CaseType | varchar |  |  | SI | Case Type |
| MRC_CertificateIssuer | varchar |  |  | SI | Certificate Issuer |
| MRC_CertificateSeen | varchar |  |  | SI | Certificate Seen |
| MRC_CertificateSeenUser | varchar |  |  | SI | Certificate Seen User |
| MRC_Coroner | varchar |  |  | SI | Coroner |
| MRC_Embalming | varchar |  |  | SI | Embalming |
| MRC_Inquest | varchar |  |  | SI | Inquest |
| MRC_PlaceOfDeath | varchar |  |  | SI | Place of Death |
| MRC_PostMortem | varchar |  |  | SI | Post Mortem |
| MRC_PostMortemType | varchar |  |  | SI | Post Mortem Type |
| MRC_Registrar | varchar |  |  | SI | Registrar |
| MRC_Religion | varchar |  |  | SI | Religion |
| MRC_TissueDonor | varchar |  |  | SI | Tissue Donor |
| MRC_Transplant | varchar |  |  | SI | Transplant |
| MRC_calc_Location | varchar |  |  | SI | calc Location |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*