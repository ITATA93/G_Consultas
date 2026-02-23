# SQLUser.PAC_ReferralDiagnosticProblem

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFDP_RowId | bigint | PK |  | NO | - |
| Q33Q1 | - |  |  | SI | Cognitive assessment for |
| Q33Q2 | - |  |  | SI | Able to read time |
| Q33Q3 | - |  |  | SI | Able to understand numbers |
| Q33Q4 | - |  |  | SI | Identifies different colours |
| Q33Q5 | - |  |  | SI | Can read and speak English |
| Q33Q6 | - |  |  | SI | Difficulties with hearing |
| Q33Q7 | - |  |  | SI | Willing to learn |
| Q33Q8 | - |  |  | SI | Understands need for dialysis |
| Q33Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFDP_Code | varchar |  |  | NO | Code |
| REFDP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFDP_CreatedDate | date |  |  | SI | Created Date |
| REFDP_CreatedTime | time |  |  | SI | Created Time |
| REFDP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFDP_DateFrom | date |  |  | SI | DateFrom |
| REFDP_DateTo | date |  |  | SI | DateTo |
| REFDP_Desc | varchar |  |  | NO | Description |
| REFDP_Owner | varchar |  |  | SI | Owner |
| REFDP_UpdatedDate | date |  |  | SI | Updated Date |
| REFDP_UpdatedTime | time |  |  | SI | Updated Time |
| REFDP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*