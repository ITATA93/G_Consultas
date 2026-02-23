# SQLUser.PAC_ReportingType

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REPTYPE_RowId | bigint | PK |  | NO | - |
| ChildQ29DR | - |  |  | SI | Child Reference: Last breast milk intake |
| Q03Q1 | - |  |  | SI | Date |
| Q03Q2 | - |  |  | SI | Time |
| Q03Q3 | - |  |  | SI | Details |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REPTYPE_Code | varchar |  |  | NO | Code |
| REPTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REPTYPE_CreatedDate | date |  |  | SI | Created Date |
| REPTYPE_CreatedTime | time |  |  | SI | Created Time |
| REPTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REPTYPE_DateFrom | date |  |  | SI | DateFrom |
| REPTYPE_DateTo | date |  |  | SI | Date To |
| REPTYPE_Desc | varchar |  |  | NO | Description |
| REPTYPE_NationCodeTableMngtInstructions | varchar |  |  | SI | NationCodeTableMngtInstructions |
| REPTYPE_NationalCode | varchar |  |  | SI | NationalCode |
| REPTYPE_Owner | varchar |  |  | SI | Owner |
| REPTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| REPTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| REPTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*