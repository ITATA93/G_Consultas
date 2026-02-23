# websys.MonitorQuickSQL

> "Summary of very low cost SQL query statistics collected in Cache 2017.1 and later. <br/>

**Schema:** websys
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Summary of very low cost SQL query statistics collected in Cache 2017.1 and later. <br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Hash | varchar |  |  | SI | Hash of query text |
| Namespace | varchar |  |  | SI | Namespace where queries are run |
| QueryText | varchar |  |  | SI | Text of SQL Query |
| RoutineName | varchar |  |  | SI | Routine where SQL is found |
| RunDate | date |  |  | SI | Date of data from websys.Monitor
RunDate and RunT... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| SumPTime | numeric |  |  | SI | Sum of pTime |
| TotalHits | integer |  |  | SI | Count of total hits for the time period for  |
| Variance | numeric |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*