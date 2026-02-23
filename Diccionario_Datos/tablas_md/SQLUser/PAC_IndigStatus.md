# SQLUser.PAC_IndigStatus

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDST_RowId | bigint | PK |  | NO | - |
| ChildQ27DR | - |  |  | SI | Child Reference: Neuro-psychomotricity therapist g... |
| INDST_Code | varchar |  |  | NO | Code |
| INDST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INDST_CreatedDate | date |  |  | SI | Created Date |
| INDST_CreatedTime | time |  |  | SI | Created Time |
| INDST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INDST_DateFrom | date |  |  | SI | Date From |
| INDST_DateTo | date |  |  | SI | Date To |
| INDST_Desc | varchar |  |  | NO | Description |
| INDST_NationalCode | varchar |  |  | SI | National Code |
| INDST_Owner | varchar |  |  | SI | Owner |
| INDST_UpdatedDate | date |  |  | SI | Updated Date |
| INDST_UpdatedTime | time |  |  | SI | Updated Time |
| INDST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q25Q1 | - |  |  | SI | Goals |
| Q25Q2 | - |  |  | SI | Timing |
| Q25Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*