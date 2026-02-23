# SQLUser.CT_BarcodeSystem

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBS_RowID | bigint | PK |  | NO | - |
| CTBS_Code | varchar |  |  | NO | Code |
| CTBS_CodeTableTags | varchar |  |  | SI | List of code table tags |
| CTBS_CreatedDate | date |  |  | SI | Created Date |
| CTBS_CreatedTime | time |  |  | SI | Created Time |
| CTBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTBS_DateFrom | date |  |  | SI | Effective date for the record |
| CTBS_DateTo | date |  |  | SI | Last day the record is active |
| CTBS_Desc | varchar |  |  | NO | Description |
| CTBS_Owner | varchar |  |  | SI | Owner |
| CTBS_UpdatedDate | date |  |  | SI | Updated Date |
| CTBS_UpdatedTime | time |  |  | SI | Updated Time |
| CTBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02Q1 | - |  |  | SI | Alumno(s) supervisado(s) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*