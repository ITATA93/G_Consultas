# SQLUser.ARC_BillingScheduleRevision

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCR_RowID | bigint | PK |  | NO | - |
| ARCBSCR_BillRoundType | varchar |  |  | SI | Billing Rounding Type
Defines the type of Roundin... |
| ARCBSCR_BillRoundUnit | double |  |  | SI | Billing Rounding Unit |
| ARCBSCR_Code | varchar |  |  | NO | Code |
| ARCBSCR_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCR_Comments | varchar |  |  | SI | Comments |
| ARCBSCR_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCR_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCR_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSCR_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSCR_Desc | varchar |  |  | NO | Description |
| ARCBSCR_Number | varchar |  |  | NO | Revision Number |
| ARCBSCR_Owner | varchar |  |  | SI | Owner |
| ARCBSCR_ParRef | bigint |  |  | NO | - |
| ARCBSCR_RevisionCode | varchar |  |  | SI | Revision Code |
| ARCBSCR_RevisionDesc | varchar |  |  | SI | Revision Description
HTMLTextBox#n |
| ARCBSCR_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCR_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ69DR | - |  |  | SI | Child Reference: Pupilas / Reflejos oculares |
| Q68Q1 | - |  |  | SI | Hallazgos |
| Q68Q2 | - |  |  | SI | Ubicación |
| Q68Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*