# SQLUser.LBC_Antibody

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAB_RowID | bigint | PK |  | NO | - |
| ChildQ18DR | - |  |  | SI | Child Reference: Insulin sensitivity (mmol / L per... |
| LBCAB_AdditionalBloodGroupSystem_DR | bigint |  | FK | SI | Additional Blood Group System |
| LBCAB_Code | varchar |  |  | NO | Code |
| LBCAB_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCAB_CreatedDate | date |  |  | SI | Created Date |
| LBCAB_CreatedTime | time |  |  | SI | Created Time |
| LBCAB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAB_DateFrom | date |  |  | SI | Effective date for the record |
| LBCAB_DateTo | date |  |  | SI | Last day the record is active |
| LBCAB_Desc | varchar |  |  | NO | Description
HTMLTextBox |
| LBCAB_ExcludeFromElectronicIssue | varchar |  |  | SI | Exclude from Electronic Issue |
| LBCAB_Owner | varchar |  |  | SI | Owner |
| LBCAB_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAB_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q17Q1 | - |  |  | SI | Time from |
| Q17Q2 | - |  |  | SI | Time to |
| Q17Q3 | - |  |  | SI | Ratio |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*