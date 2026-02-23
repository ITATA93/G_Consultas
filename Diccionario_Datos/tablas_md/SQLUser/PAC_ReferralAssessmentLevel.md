# SQLUser.PAC_ReferralAssessmentLevel

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFASL_RowId | bigint | PK |  | NO | - |
| ChildQ22DR | - |  |  | SI | Child Reference: Skin conditions |
| Q13Q1 | - |  |  | SI | Carer name |
| Q13Q2 | - |  |  | SI | Occupation / Community status |
| Q13Q3 | - |  |  | SI | Carer willing / able to support |
| Q13Q4 | - |  |  | SI | Support |
| Q13Q5 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFASL_Code | varchar |  |  | NO | Code |
| REFASL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFASL_CreatedDate | date |  |  | SI | Created Date |
| REFASL_CreatedTime | time |  |  | SI | Created Time |
| REFASL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFASL_DateFrom | date |  |  | SI | Date From |
| REFASL_DateTo | date |  |  | SI | Date To |
| REFASL_Desc | varchar |  |  | NO | Description |
| REFASL_Owner | varchar |  |  | SI | Owner |
| REFASL_UpdatedDate | date |  |  | SI | Updated Date |
| REFASL_UpdatedTime | time |  |  | SI | Updated Time |
| REFASL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*