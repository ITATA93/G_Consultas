# SQLUser.CT_ClassificationSystem

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCS_RowID | bigint | PK |  | NO | - |
| CTCS_Code | varchar |  |  | NO | Code |
| CTCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTCS_Comment | varchar |  |  | SI | Notes |
| CTCS_CreatedDate | date |  |  | SI | Created Date |
| CTCS_CreatedTime | time |  |  | SI | Created Time |
| CTCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCS_DateFrom | date |  |  | SI | Effective date for the record |
| CTCS_DateTo | date |  |  | SI | Last day the record is active  |
| CTCS_Desc | varchar |  |  | NO | Description |
| CTCS_Owner | varchar |  |  | SI | Owner |
| CTCS_System | varchar |  |  | SI | System Created |
| CTCS_UpdatedDate | date |  |  | SI | Updated Date |
| CTCS_UpdatedTime | time |  |  | SI | Updated Time |
| CTCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | Dimensión |
| Q01Q2 | - |  |  | SI | Resultado |
| Q01Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*