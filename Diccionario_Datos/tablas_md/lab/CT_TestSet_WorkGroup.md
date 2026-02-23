# lab.CT_TestSet_WorkGroup

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTWG_RowId | varchar | PK |  | NO | - |
| CTTWG_CODE | varchar |  |  | NO | Group code |
| CTTWG_CumReportRRHeading | varchar |  |  | SI | Cumulative Report RR Heading |
| CTTWG_CumulativeGroup | varchar |  |  | SI | Cumulative Group |
| CTTWG_CumulativeType | varchar |  |  | SI | Cumulative Type |
| CTTWG_Department_DR | varchar |  | FK | SI | Des Ref Department |
| CTTWG_Description | varchar |  |  | SI | Description |
| CTTWG_EndPrinting | varchar |  |  | SI | End Printing |
| CTTWG_PrintSeq | numeric |  |  | SI | Print Sequence |
| CTTWG_ReportName | varchar |  |  | SI | Report Name |
| CTTWG_ReportPage_Doctor_DR | varchar |  | FK | SI | ReportPage Doctor DR |
| CTTWG_ReportPage_Hospital_DR | varchar |  | FK | SI | ReportPage Hospital DR |
| CTTWG_Section_DR | varchar |  | FK | SI | Section DR |
| CTTWG_StartPrinting | varchar |  |  | SI | Start Printing |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*