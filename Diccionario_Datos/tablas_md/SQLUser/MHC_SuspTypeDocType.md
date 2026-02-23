# SQLUser.MHC_SuspTypeDocType

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | bigint | PK |  | NO | MHC_SuspensionType Parent Reference |
| ChildQ109DR | - |  |  | SI | Child Reference: Factores Familiares |
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
| Q108Q1 | - |  |  | SI | Fecha |
| Q108Q2 | - |  |  | SI | Registro de la Atención |
| Q108Q3 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*