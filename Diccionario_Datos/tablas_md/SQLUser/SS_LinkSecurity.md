# SQLUser.SS_LinkSecurity

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSLINKSEC_RowID | bigint | PK |  | NO | - |
| SSLINKSEC_BaseURL | varchar |  |  | NO | Base URL |
| SSLINKSEC_Code | varchar |  |  | NO | Code |
| SSLINKSEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSLINKSEC_CreatedDate | date |  |  | SI | Created Date |
| SSLINKSEC_CreatedTime | time |  |  | SI | Created Time |
| SSLINKSEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSLINKSEC_DateFrom | date |  |  | SI | Date From |
| SSLINKSEC_DateTo | date |  |  | SI | Date To |
| SSLINKSEC_Desc | varchar |  |  | NO | Description |
| SSLINKSEC_KeepOpen | varchar |  |  | SI | Disconnected mode for new Window  |
| SSLINKSEC_Owner | varchar |  |  | SI | Owner |
| SSLINKSEC_UpdatedDate | date |  |  | SI | Updated Date |
| SSLINKSEC_UpdatedTime | time |  |  | SI | Updated Time |
| SSLINKSEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*