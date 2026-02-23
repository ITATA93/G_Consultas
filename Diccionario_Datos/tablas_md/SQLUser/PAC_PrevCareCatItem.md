# SQLUser.PAC_PrevCareCatItem

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPCCI_RowID | bigint | PK |  | NO | - |
| ChildQ05DR | - |  |  | SI | Child Reference: Transfer recovery |
| PACPCCI_CareCategory_DR | bigint |  | FK | SI | Preventative Care Category |
| PACPCCI_Code | varchar |  |  | NO | Code |
| PACPCCI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPCCI_CreatedDate | date |  |  | SI | Created Date |
| PACPCCI_CreatedTime | time |  |  | SI | Created Time |
| PACPCCI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPCCI_DateFrom | date |  |  | SI | Date From |
| PACPCCI_DateTo | date |  |  | SI | Date To |
| PACPCCI_Desc | varchar |  |  | NO | Description |
| PACPCCI_Diseases | varchar |  |  | SI | List of Diseases |
| PACPCCI_Owner | varchar |  |  | SI | Owner |
| PACPCCI_UpdatedDate | date |  |  | SI | Updated Date |
| PACPCCI_UpdatedTime | time |  |  | SI | Updated Time |
| PACPCCI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Micro goal |
| Q09Q2 | - |  |  | SI | Timing |
| Q09Q3 | - |  |  | SI | Outcome |
| Q09Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*