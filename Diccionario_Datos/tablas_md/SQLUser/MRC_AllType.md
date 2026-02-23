# SQLUser.MRC_AllType

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCAT_RowId | bigint | PK |  | NO | - |
| ChildQ112DR | - |  |  | SI | Child Reference: Pulsos periféricos |
| MRCAT_Code | varchar |  |  | NO | Abbreviation |
| MRCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MRCAT_CreatedDate | date |  |  | SI | Created Date |
| MRCAT_CreatedTime | time |  |  | SI | Created Time |
| MRCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRCAT_DateFrom | date |  |  | SI | Date From |
| MRCAT_DateTo | date |  |  | SI | Date To |
| MRCAT_Desc | varchar |  |  | NO | Description |
| MRCAT_IconName | varchar |  |  | SI | Icon Name |
| MRCAT_IconPriority | double |  |  | SI | Icon Priority |
| MRCAT_IndeterminateCode | varchar |  |  | SI | Indeterminate Code |
| MRCAT_Owner | varchar |  |  | SI | Owner |
| MRCAT_Sequence | varchar |  |  | SI | Sequence |
| MRCAT_Status | varchar |  |  | SI | Status |
| MRCAT_TagDescription | varchar |  |  | SI | Tag Description |
| MRCAT_UpdatedDate | date |  |  | SI | Updated Date |
| MRCAT_UpdatedTime | time |  |  | SI | Updated Time |
| MRCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q108Q1 | - |  |  | SI | Hallazgos |
| Q108Q2 | - |  |  | SI | Extremidad superior |
| Q108Q3 | - |  |  | SI | Extremidad inferior |
| Q108Q4 | - |  |  | SI | Ubicación |
| Q108Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*