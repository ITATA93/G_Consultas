# SQLUser.BLC_ReasonForCancelInv

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFC_RowId | bigint | PK |  | NO | - |
| ChildQ17DR | - |  |  | SI | Child Reference: DETERMINANTES SOCIALES |
| Q03Q1 | - |  |  | SI | Objetivos |
| Q03Q2 | - |  |  | SI | Estrategias o Actividades |
| Q03Q3 | - |  |  | SI | Responsables |
| Q03Q4 | - |  |  | SI | Plazo |
| Q03Q5 | - |  |  | SI | Indicador de Logro |
| Q03Q6 | - |  |  | SI | Cumplimiento |
| Q03Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RFC_Code | varchar |  |  | NO | Code |
| RFC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFC_CreatedDate | date |  |  | SI | Created Date |
| RFC_CreatedTime | time |  |  | SI | Created Time |
| RFC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFC_DateFrom | date |  |  | SI | DateFrom |
| RFC_DateTo | date |  |  | SI | Date To |
| RFC_Default | varchar |  |  | SI | Default Flag |
| RFC_Desc | varchar |  |  | NO | Description |
| RFC_Owner | varchar |  |  | SI | Owner |
| RFC_UpdatedDate | date |  |  | SI | Updated Date |
| RFC_UpdatedTime | time |  |  | SI | Updated Time |
| RFC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*