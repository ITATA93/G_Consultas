# websys.MonitorPageLoadSummary

> "Summary of websys.MonitorPageLoad page performance statistics. <br/>

**Schema:** websys
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Summary of websys.MonitorPageLoad page performance statistics. <br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AvgPTime | numeric |  |  | SI | Average of pTime |
| MaxPTime | integer |  |  | SI | Maximum of pTime |
| RunDate | date |  |  | SI | Date of data from websys.MonitorPageLoad |
| RunTime | time |  |  | SI | Time this run was started. |
| SumPTime | integer |  |  | SI | Sum of pTime |
| TotalHits | integer |  |  | SI | Count of total hits for the time period for pName |
| TotalHitsGT10 | integer |  |  | SI | Count of Total Hits greater than 10 seconds |
| TotalHitsGT2 | integer |  |  | SI | Count of Total Hits greater than 2 seconds |
| TotalHitsGT5 | integer |  |  | SI | Count of Total Hits greater than 5 seconds |
| pComponent | varchar |  |  | SI | Component or code section name from websys.Monitor... |
| pURL | varchar |  |  | SI | Component or code section name from websys.Monitor... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*