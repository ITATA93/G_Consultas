# SQLUser.ORC_SpecimenType

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPETYP_RowId | bigint | PK |  | NO | - |
| SPETYP_Code | varchar |  |  | NO | Code |
| SPETYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPETYP_CreatedDate | date |  |  | SI | Created Date |
| SPETYP_CreatedTime | time |  |  | SI | Created Time |
| SPETYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPETYP_DateFrom | date |  |  | SI | Date From |
| SPETYP_DateTo | date |  |  | SI | Date To |
| SPETYP_Desc | varchar |  |  | NO | Description |
| SPETYP_Owner | varchar |  |  | SI | Owner |
| SPETYP_UpdatedDate | date |  |  | SI | Updated Date |
| SPETYP_UpdatedTime | time |  |  | SI | Updated Time |
| SPETYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*