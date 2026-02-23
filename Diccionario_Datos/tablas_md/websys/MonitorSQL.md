# websys.MonitorSQL

> "Summary of SQL query statistics. <br/>

**Schema:** websys
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Summary of SQL query statistics. <br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AvgPGlobals | numeric |  |  | SI | Average of pGlobals |
| AvgPLines | numeric |  |  | SI | Average of pLines |
| AvgPRows | numeric |  |  | SI | Average of RowCount |
| AvgPTime | numeric |  |  | SI | Average of pTime |
| CursorName | varchar |  |  | SI | SQL Cursor Name |
| MaxPGlobals | integer |  |  | SI | Maximum of pGlobals |
| MaxPLines | integer |  |  | SI | Maximum of pLines |
| MaxPRows | integer |  |  | SI | Maximum of pRows |
| MaxPTime | numeric |  |  | SI | Maximum of pTime |
| QueryText | varchar |  |  | SI | Text of SQL Query |
| RoutineName | varchar |  |  | SI | Routine where SQL is found |
| RunDate | date |  |  | SI | Date of data from websys.Monitor
RunDate and RunT... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| SumPGlobals | integer |  |  | SI | Sum of pGlobals |
| SumPLines | integer |  |  | SI | Sum of pLines |
| SumPRows | integer |  |  | SI | Sum of RowCount |
| SumPTime | numeric |  |  | SI | Sum of pTime |
| TotalHits | integer |  |  | SI | Count of total hits for the time period for  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*