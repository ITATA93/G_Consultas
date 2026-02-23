# SQLUser.PAC_InjuryActivityStatus

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INJACTST_RowId | bigint | PK |  | NO | - |
| ChildQ33DR | - |  |  | SI | Child Reference: Orthoptist goals |
| INJACTST_Code | varchar |  |  | NO | Code |
| INJACTST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INJACTST_CreatedDate | date |  |  | SI | Created Date |
| INJACTST_CreatedTime | time |  |  | SI | Created Time |
| INJACTST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INJACTST_DateFrom | date |  |  | SI | Date From |
| INJACTST_DateTo | date |  |  | SI | Date To |
| INJACTST_Desc | varchar |  |  | NO | Description |
| INJACTST_NationalCode | varchar |  |  | SI | National Code |
| INJACTST_Owner | varchar |  |  | SI | Owner |
| INJACTST_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| INJACTST_UpdatedDate | date |  |  | SI | Updated Date |
| INJACTST_UpdatedTime | time |  |  | SI | Updated Time |
| INJACTST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q31Q1 | - |  |  | SI | Goal |
| Q31Q2 | - |  |  | SI | Timing |
| Q31Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*