# SQLUser.PAC_StandbyStatus

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STANDST_RowId | bigint | PK |  | NO | - |
| Q16Q1 | - |  |  | SI | Treatment |
| Q16Q2 | - |  |  | SI | Entered date |
| Q16Q3 | - |  |  | SI | Entered time |
| Q16Q4 | - |  |  | SI | Other treatment |
| Q16Q5 | - |  |  | SI | Treatment status |
| Q16Q6 | - |  |  | SI | Reason for ceasing |
| Q16Q7 | - |  |  | SI | Other reason for ceasing |
| Q16Q8 | - |  |  | SI | Treatment notes |
| Q16Q9 | - |  |  | SI | Entered by |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| STANDST_Code | varchar |  |  | NO | Code |
| STANDST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STANDST_CreatedDate | date |  |  | SI | Created Date |
| STANDST_CreatedTime | time |  |  | SI | Created Time |
| STANDST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STANDST_DateFrom | date |  |  | SI | Date From |
| STANDST_DateTo | date |  |  | SI | Date To |
| STANDST_Desc | varchar |  |  | NO | Description |
| STANDST_Owner | varchar |  |  | SI | Owner |
| STANDST_UpdatedDate | date |  |  | SI | Updated Date |
| STANDST_UpdatedTime | time |  |  | SI | Updated Time |
| STANDST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*