# SQLUser.PAC_ReferralDiagProblemKeyw

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | PAC_ReferralDiagnosticProblem Parent Reference |
| ChildQ33DR | - |  |  | SI | Child Reference: Cognitive |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| KEYW_CreatedDate | date |  |  | SI | Created Date |
| KEYW_CreatedTime | time |  |  | SI | Created Time |
| KEYW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Text |
| KEYW_UpdatedDate | date |  |  | SI | Updated Date |
| KEYW_UpdatedTime | time |  |  | SI | Updated Time |
| KEYW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q32Q1 | - |  |  | SI | Eyesight assessment for |
| Q32Q2 | - |  |  | SI | Requires reading aids |
| Q32Q3 | - |  |  | SI | Other reading aids, if applicable |
| Q32Q4 | - |  |  | SI | Able to read weigh scales |
| Q32Q5 | - |  |  | SI | Able to read PD bag labels |
| Q32Q6 | - |  |  | SI | Able to read automated PD messages |
| Q32Q7 | - |  |  | SI | Cataracts |
| Q32Q8 | - |  |  | SI | Eye review required |
| Q32Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*