# SQLUser.PAC_ReferralAssessmentType

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFAST_RowId | bigint | PK |  | NO | - |
| ChildQ23DR | - |  |  | SI | Child Reference: Nails / Hands |
| Q22Q1 | - |  |  | SI | Skin condition assessment for |
| Q22Q2 | - |  |  | SI | Lesions |
| Q22Q3 | - |  |  | SI | Infections |
| Q22Q4 | - |  |  | SI | Rashes |
| Q22Q5 | - |  |  | SI | Fungal |
| Q22Q6 | - |  |  | SI | Skin scrapings |
| Q22Q7 | - |  |  | SI | Chronic open wounds or skin conditions |
| Q22Q8 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFAST_Code | varchar |  |  | NO | Code |
| REFAST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFAST_CreatedDate | date |  |  | SI | Created Date |
| REFAST_CreatedTime | time |  |  | SI | Created Time |
| REFAST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFAST_DateFrom | date |  |  | SI | Date From |
| REFAST_DateTo | date |  |  | SI | Date To |
| REFAST_Desc | varchar |  |  | NO | Description |
| REFAST_Owner | varchar |  |  | SI | Owner |
| REFAST_UpdatedDate | date |  |  | SI | Updated Date |
| REFAST_UpdatedTime | time |  |  | SI | Updated Time |
| REFAST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*