# SQLUser.PAC_SpecialOrdType

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPECORDTP_RowId | bigint | PK |  | NO | - |
| SPECORDTP_Code | varchar |  |  | NO | Code |
| SPECORDTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPECORDTP_CreatedDate | date |  |  | SI | Created Date |
| SPECORDTP_CreatedTime | time |  |  | SI | Created Time |
| SPECORDTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPECORDTP_DateFrom | date |  |  | SI | Date From |
| SPECORDTP_DateTo | date |  |  | SI | Date To |
| SPECORDTP_Desc | varchar |  |  | NO | Description |
| SPECORDTP_Owner | varchar |  |  | SI | Owner |
| SPECORDTP_UpdatedDate | date |  |  | SI | Updated Date |
| SPECORDTP_UpdatedTime | time |  |  | SI | Updated Time |
| SPECORDTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*