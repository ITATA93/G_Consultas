# SQLUser.LBDR_ReportPage

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRRP_ParRef | varchar | PK |  | NO | Parent Reference LBDREpisode DR |
| ChildQ81DR | - |  |  | SI | Child Reference: Lenguaje |
| LBDRRP_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| LBDRRP_DepartmentFooterClass | varchar |  |  | SI | Department Footer Class
The ZEN Report to use for... |
| LBDRRP_DepartmentHeaderClass | varchar |  |  | SI | Department Header Class
The ZEN Report to use for... |
| LBDRRP_FooterClass | varchar |  |  | SI | Report Page Footer Class
This is the ZEN Report t... |
| LBDRRP_Format | varchar |  |  | SI | Format
The format of the Report Page
Currently o... |
| LBDRRP_FormatClass | varchar |  |  | SI | ZEN Report for the ReportPage Format
No longer us... |
| LBDRRP_HeaderClass | varchar |  |  | SI | Report Page Header Class
This is the ZEN Report t... |
| LBDRRP_ReportPageCode | varchar |  |  | SI | Report Page code (for readability, and as sortkey ... |
| LBDRRP_ReportPage_DR | bigint |  | FK | SI | The Report Page for the Episode |
| LBDRRP_ReportWriterClass | varchar |  |  | SI | Report Writer Class
Use this writer class for Rep... |
| LBDRRP_RowID | varchar |  |  | NO | - |
| LBDRRP_SectionFooterClass | varchar |  |  | SI | Section Footer Class
The ZEN Report to use for th... |
| LBDRRP_SectionHeaderClass | varchar |  |  | SI | Section Header Class
The ZEN Report to use for th... |
| LBDRRP_SortKey | double |  |  | SI | The Sortkey used to sort Report Pages.
Currently ... |
| LBDRRP_SubsequentHeaderClass | varchar |  |  | SI | Report Subsequent Page Header Class
This is the Z... |
| LBDRRP_TestSetFooterClass | varchar |  |  | SI | Test Set Footer Class
The ZEN Report to use for t... |
| LBDRRP_TestSetHeaderClass | varchar |  |  | SI | Test Set Header Class
The ZEN Report to use for t... |
| Q80Q1 | - |  |  | SI | Características |
| Q80Q2 | - |  |  | SI | Evaluación |
| Q80Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*