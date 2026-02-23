# SQLUser.LBC_Section

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCS_RowID | bigint | PK |  | NO | - |
| LBCS_Code | varchar |  |  | NO | Code |
| LBCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCS_CodeTranslated | varchar |  |  | SI | - |
| LBCS_CreatedDate | date |  |  | SI | Created Date |
| LBCS_CreatedTime | time |  |  | SI | Created Time |
| LBCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCS_Department_DR | bigint |  | FK | SI | Department |
| LBCS_Desc | varchar |  |  | NO | Description |
| LBCS_DescTranslated | varchar |  |  | SI | - |
| LBCS_FooterClass | varchar |  |  | SI | Section Footer Class
The Zen Report which creates... |
| LBCS_HeaderClass | varchar |  |  | SI | Section Header Class
The Zen Report which creates... |
| LBCS_Owner | varchar |  |  | SI | Owner |
| LBCS_SectionFooterExtraText | varchar |  |  | SI | Section Footer Extra Text
Extra Text (such a Phon... |
| LBCS_SectionHeaderExtraText | varchar |  |  | SI | Section Header Extra Text
Extra Text (such a Phon... |
| LBCS_Sequence | double |  |  | SI | Print Sequence
The order of Sections in Doctors R... |
| LBCS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q130Q1 | - |  |  | SI | Lateralidad |
| Q130Q2 | - |  |  | SI | Motivo |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*