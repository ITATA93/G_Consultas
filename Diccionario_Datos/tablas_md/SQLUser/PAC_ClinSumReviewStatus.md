# SQLUser.PAC_ClinSumReviewStatus

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLSRS_RowId | bigint | PK |  | NO | - |
| CLSRS_Code | varchar |  |  | NO | Code |
| CLSRS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLSRS_CreatedDate | date |  |  | SI | Created Date |
| CLSRS_CreatedTime | time |  |  | SI | Created Time |
| CLSRS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLSRS_DateFrom | date |  |  | SI | Date From |
| CLSRS_DateTo | date |  |  | SI | Date To |
| CLSRS_Desc | varchar |  |  | NO | Description |
| CLSRS_DoNotAllowCStoAuthorise | varchar |  |  | SI | DoNotAllowCStoAuthorise |
| CLSRS_Owner | varchar |  |  | SI | Owner |
| CLSRS_UpdatedDate | date |  |  | SI | Updated Date |
| CLSRS_UpdatedTime | time |  |  | SI | Updated Time |
| CLSRS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q22Q1 | - |  |  | SI | Drainage present |
| Q22Q2 | - |  |  | SI | Drainage description |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*