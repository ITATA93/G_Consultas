# SQLUser.PAC_ClinicalSubProgram

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CSP_RowId | bigint | PK |  | NO | - |
| CSP_Code | varchar |  |  | NO | Code |
| CSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CSP_CreatedDate | date |  |  | SI | Created Date |
| CSP_CreatedTime | time |  |  | SI | Created Time |
| CSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CSP_DateFrom | date |  |  | SI | Date From |
| CSP_DateTo | date |  |  | SI | Date To |
| CSP_Desc | varchar |  |  | NO | Description |
| CSP_NationalCode | varchar |  |  | SI | National Code |
| CSP_Owner | varchar |  |  | SI | Owner |
| CSP_UpdatedDate | date |  |  | SI | Updated Date |
| CSP_UpdatedTime | time |  |  | SI | Updated Time |
| CSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ11DR | - |  |  | SI | Child Reference: Blood glucose concentration targe... |
| Q10Q1 | - |  |  | SI | Time from |
| Q10Q2 | - |  |  | SI | Time to |
| Q10Q3 | - |  |  | SI | Insulin sensitivity factor (mmol/L) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*