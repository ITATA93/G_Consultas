# SQLUser.LBDR_Section

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRS_ParRef | varchar | PK |  | NO | Parent Reference LBDRDepartment DR |
| LBDRS_Cumulative_DR | bigint |  | FK | SI | Cumulative Header
For Format1 the Cumulative Head... |
| LBDRS_Format | varchar |  |  | SI | Section Format
See Property LBCRPFormat  |
| LBDRS_PrintSeparatePage | varchar |  |  | SI | Print New Page
Start a new page in the Doctors Re... |
| LBDRS_RowID | varchar |  |  | NO | - |
| LBDRS_SectionCode | varchar |  |  | SI | Section Code (for readability and use in ZEN Repor... |
| LBDRS_SectionDesc | varchar |  |  | SI | Section Desc (for readability and use in ZEN Repor... |
| LBDRS_SectionFooterClass | varchar |  |  | SI | Section Footer Zen Report
The Zen Report which cr... |
| LBDRS_SectionFooterExtraText | varchar |  |  | SI | Section Footer Extra Text
Extra Text (such a Phon... |
| LBDRS_SectionHeaderClass | varchar |  |  | SI | Section Header Zen Report
The Zen Report which cr... |
| LBDRS_SectionHeaderExtraText | varchar |  |  | SI | Section Header Extra Text
Extra Text (such a Phon... |
| LBDRS_Section_DR | bigint |  | FK | SI | The Section within the Department |
| LBDRS_SortKey | double |  |  | SI | The Sortkey used to sort Sections. |
| Q83Q1 | - |  |  | SI | Características |
| Q83Q2 | - |  |  | SI | Evaluación |
| Q83Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*