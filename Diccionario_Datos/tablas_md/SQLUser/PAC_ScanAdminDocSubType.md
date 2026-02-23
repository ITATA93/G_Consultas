# SQLUser.PAC_ScanAdminDocSubType

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SADST_RowId | bigint | PK |  | NO | - |
| ChildQ26DR | - |  |  | SI | Child Reference: Recovery / Improvement of autonom... |
| Q21Q1 | - |  |  | SI | Micro goal |
| Q21Q2 | - |  |  | SI | Timing |
| Q21Q3 | - |  |  | SI | Outcome |
| Q21Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SADST_Code | varchar |  |  | NO | Code |
| SADST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SADST_CreatedDate | date |  |  | SI | Created Date |
| SADST_CreatedTime | time |  |  | SI | Created Time |
| SADST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SADST_DateFrom | date |  |  | SI | DateFrom |
| SADST_DateTo | date |  |  | SI | DateTo |
| SADST_Desc | varchar |  |  | NO | Description |
| SADST_Owner | varchar |  |  | SI | Owner |
| SADST_UpdatedDate | date |  |  | SI | Updated Date |
| SADST_UpdatedTime | time |  |  | SI | Updated Time |
| SADST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*