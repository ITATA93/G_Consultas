# SQLUser.PAC_RequestType

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REQTYP_RowId | bigint | PK |  | NO | - |
| Q04Q1 | - |  |  | SI | Date |
| Q04Q2 | - |  |  | SI | Time |
| Q04Q3 | - |  |  | SI | Details |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REQTYP_Code | varchar |  |  | NO | Code |
| REQTYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REQTYP_CreatedDate | date |  |  | SI | Created Date |
| REQTYP_CreatedTime | time |  |  | SI | Created Time |
| REQTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REQTYP_DateFrom | date |  |  | SI | Date From |
| REQTYP_DateTo | date |  |  | SI | Date To |
| REQTYP_Desc | varchar |  |  | NO | Description |
| REQTYP_Owner | varchar |  |  | SI | Owner |
| REQTYP_UpdatedDate | date |  |  | SI | Updated Date |
| REQTYP_UpdatedTime | time |  |  | SI | Updated Time |
| REQTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*