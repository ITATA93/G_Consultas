# SQLUser.PAC_RequestStatus

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REQST_RowId | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: Last clear fluids intake |
| Q29Q1 | - |  |  | SI | Date |
| Q29Q2 | - |  |  | SI | Time |
| Q29Q3 | - |  |  | SI | Details |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REQST_Code | varchar |  |  | NO | Code |
| REQST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REQST_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| REQST_CreatedDate | date |  |  | SI | Created Date |
| REQST_CreatedTime | time |  |  | SI | Created Time |
| REQST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REQST_DateFrom | date |  |  | SI | Date From |
| REQST_DateTo | date |  |  | SI | Date To |
| REQST_Desc | varchar |  |  | NO | Description |
| REQST_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| REQST_Owner | varchar |  |  | SI | Owner |
| REQST_UpdatedDate | date |  |  | SI | Updated Date |
| REQST_UpdatedTime | time |  |  | SI | Updated Time |
| REQST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*