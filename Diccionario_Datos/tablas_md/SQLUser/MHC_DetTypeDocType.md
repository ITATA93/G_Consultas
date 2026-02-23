# SQLUser.MHC_DetTypeDocType

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | bigint | PK |  | NO | MHC_DetentionType Parent Reference |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOC_CreatedDate | date |  |  | SI | Created Date |
| DOC_CreatedTime | time |  |  | SI | Created Time |
| DOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOC_DocType_DR | bigint |  | FK | SI | Des Ref MHCDocumentType |
| DOC_RowId | varchar |  |  | NO | - |
| DOC_UpdatedDate | date |  |  | SI | Updated Date |
| DOC_UpdatedTime | time |  |  | SI | Updated Time |
| DOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q05Q1 | - |  |  | SI | Equipos |
| Q05Q2 | - |  |  | SI | Familiares |
| Q05Q3 | - |  |  | SI | Fechas |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*