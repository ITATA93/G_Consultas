# SQLUser.MRC_BodyParts

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BODP_RowId | bigint | PK |  | NO | - |
| BODP_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| BODP_Code | varchar |  |  | NO | Code |
| BODP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BODP_CreatedDate | date |  |  | SI | Created Date |
| BODP_CreatedTime | time |  |  | SI | Created Time |
| BODP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BODP_Desc | varchar |  |  | NO | Description |
| BODP_Owner | varchar |  |  | SI | Owner |
| BODP_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| BODP_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| BODP_UpdatedDate | date |  |  | SI | Updated Date |
| BODP_UpdatedTime | time |  |  | SI | Updated Time |
| BODP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ79DR | - |  |  | SI | Child Reference: Oídos |
| Q69Q1 | - |  |  | SI | Hallazgo |
| Q69Q2 | - |  |  | SI | Ubicación |
| Q69Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*