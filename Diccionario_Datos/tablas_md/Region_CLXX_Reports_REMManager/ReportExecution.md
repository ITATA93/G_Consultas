# Region_CLXX_Reports_REMManager.ReportExecution

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DataPeriod | varchar |  |  | SI | - |
| DataRef | varchar |  |  | SI | - |
| EndExecDateTime | timestamp |  |  | SI | - |
| ExecDateTime | timestamp |  |  | NO | - |
| ExecDesc | varchar |  |  | SI | - |
| ExecType | varchar |  |  | SI | - |
| GlobalFilter | varchar |  |  | SI | - |
| Log | varchar |  |  | SI | - |
| Month | integer |  |  | SI | - |
| ProcessExecutionID | numeric |  |  | SI | - |
| QueryStatus | varchar |  |  | SI | - |
| Report | bigint |  |  | SI | - |
| RptInternalVersion | varchar |  |  | SI | - |
| SQLFull | varchar |  |  | SI | - |
| Status | integer |  |  | SI | - |
| Visible | varchar |  |  | SI | - |
| Year | integer |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*