# SQLUser.MRC_EncEntryTypeGroup

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EGCT_RowId | bigint | PK |  | NO | - |
| EGCT_Code | varchar |  |  | SI | Code |
| EGCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EGCT_CreatedDate | date |  |  | SI | Created Date |
| EGCT_CreatedTime | time |  |  | SI | Created Time |
| EGCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EGCT_DateFrom | date |  |  | SI | DateFrom |
| EGCT_DateTo | date |  |  | SI | DateTo |
| EGCT_Desc | varchar |  |  | SI | Description |
| EGCT_Owner | varchar |  |  | SI | Owner |
| EGCT_UpdatedDate | date |  |  | SI | Updated Date |
| EGCT_UpdatedTime | time |  |  | SI | Updated Time |
| EGCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q54Q1 | - |  |  | SI | Ex. físico |
| Q54Q2 | - |  |  | SI | Resultado |
| Q54Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*