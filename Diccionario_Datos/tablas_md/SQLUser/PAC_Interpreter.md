# SQLUser.PAC_Interpreter

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTERP_RowId | bigint | PK |  | NO | - |
| ChildQ22DR | - |  |  | SI | Child Reference: Medical Officer Review |
| INTERP_Address | varchar |  |  | SI | Address |
| INTERP_Code | varchar |  |  | NO | Code |
| INTERP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INTERP_ContactMethod | varchar |  |  | SI | Contact Method |
| INTERP_CreatedDate | date |  |  | SI | Created Date |
| INTERP_CreatedTime | time |  |  | SI | Created Time |
| INTERP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INTERP_DateFrom | date |  |  | SI | Date From |
| INTERP_DateTo | date |  |  | SI | Date To |
| INTERP_Desc | varchar |  |  | NO | Description |
| INTERP_Email | varchar |  |  | SI | Email |
| INTERP_Fax | varchar |  |  | SI | Fax |
| INTERP_Owner | varchar |  |  | SI | Owner |
| INTERP_Phone | varchar |  |  | SI | Phone |
| INTERP_UpdatedDate | date |  |  | SI | Updated Date |
| INTERP_UpdatedTime | time |  |  | SI | Updated Time |
| INTERP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q21Q1 | - |  |  | SI | Assessment date |
| Q21Q10 | - |  |  | SI | Assessment comments |
| Q21Q2 | - |  |  | SI | Assessment time |
| Q21Q3 | - |  |  | SI | Care provider |
| Q21Q4 | - |  |  | SI | Type of restraint applied |
| Q21Q5 | - |  |  | SI | Restraint location |
| Q21Q6 | - |  |  | SI | Patient's behaviour |
| Q21Q7 | - |  |  | SI | Restrained limbs checked |
| Q21Q8 | - |  |  | SI | Care performed |
| Q21Q9 | - |  |  | SI | Evaluation of restraint reduction |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*