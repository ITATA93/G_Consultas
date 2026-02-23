# lab.PR_Report

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRPR_RowID | double | PK |  | NO | - |
| PRPR_ContentType | varchar |  |  | SI | Content Type |
| PRPR_CreatedDate | date |  |  | SI | Created Date |
| PRPR_CreatedTime | time |  |  | SI | Created Time |
| PRPR_DAYS | double |  |  | SI | No of Days |
| PRPR_Parameters | varchar |  |  | SI | Run time parameters |
| PRPR_PrintedDate | date |  |  | SI | Printed Date |
| PRPR_PrintedTime | time |  |  | SI | Printed Time |
| PRPR_REPORT_PARAMETERS | varchar |  |  | SI | Report parameters |
| PRPR_ReportID | double |  |  | NO | Report ID |
| PRPR_Report_DR | varchar |  | FK | SI | Report |
| PRPR_Stationary_DR | varchar |  | FK | SI | Stationary DR |
| PRPR_Status | varchar |  |  | SI | Status |
| PRPR_User_DR | varchar |  | FK | SI | User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*