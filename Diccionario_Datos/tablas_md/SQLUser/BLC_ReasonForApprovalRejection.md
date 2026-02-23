# SQLUser.BLC_ReasonForApprovalRejection

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAAPPREJ_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: INDIVIDUAL |
| Q16Q1 | - |  |  | SI | Objetivos |
| Q16Q2 | - |  |  | SI | Estrategias o Actividades |
| Q16Q3 | - |  |  | SI | Responsables |
| Q16Q4 | - |  |  | SI | Plazo |
| Q16Q5 | - |  |  | SI | Indicador de Logro |
| Q16Q6 | - |  |  | SI | Cumplimiento |
| Q16Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REAAPPREJ_Code | varchar |  |  | NO | Code |
| REAAPPREJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REAAPPREJ_CreatedDate | date |  |  | SI | Created Date |
| REAAPPREJ_CreatedTime | time |  |  | SI | Created Time |
| REAAPPREJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REAAPPREJ_DateFrom | date |  |  | SI | Date From |
| REAAPPREJ_DateTo | date |  |  | SI | Date To |
| REAAPPREJ_Desc | varchar |  |  | NO | Description |
| REAAPPREJ_Owner | varchar |  |  | SI | Owner |
| REAAPPREJ_UpdatedDate | date |  |  | SI | Updated Date |
| REAAPPREJ_UpdatedTime | time |  |  | SI | Updated Time |
| REAAPPREJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*