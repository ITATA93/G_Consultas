# websys.MonitorPageSummary

> "Summary of websys.Monitor page performance statistics. <br/>

**Schema:** websys
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Summary of websys.Monitor page performance statistics. <br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AvgPGlobalUpdates | numeric |  |  | SI | Average of pGlobalUpdates |
| AvgPGlobals | integer |  |  | SI | Average of pGlobals |
| AvgPJournalEntries | numeric |  |  | SI | Average of pJournalEntries |
| AvgPLines | integer |  |  | SI | Average of pLines |
| AvgPPrivateGlobalUpdates | numeric |  |  | SI | Average of pPrivateGlobalUpdates |
| AvgPTime | numeric |  |  | SI | Average of pTime |
| AvgPWQMGlobals | integer |  |  | SI | Average of pWQMGlobals |
| AvgPWQMLines | integer |  |  | SI | Average of pWQMLines |
| MaxPGlobalUpdates | numeric |  |  | SI | Maximum of pGlobalUpdates |
| MaxPGlobals | integer |  |  | SI | Maximum of pGlobals |
| MaxPJournalEntries | numeric |  |  | SI | Maximum of pJournalEntries |
| MaxPLines | integer |  |  | SI | Maximum of pLines |
| MaxPPrivateGlobalUpdates | numeric |  |  | SI | Maximum of pPrivateGlobalUpdates |
| MaxPTime | numeric |  |  | SI | Maximum of pTime |
| MaxPWQMGlobals | integer |  |  | SI | Maximum of pWQMGlobals |
| MaxPWQMLines | integer |  |  | SI | Maximum of pWQMLines |
| RunDate | date |  |  | SI | Date of data from websys.Monitor
RunDate and RunT... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| SumPGlobalUpdates | numeric |  |  | SI | Sum of pGlobalUpdates |
| SumPGlobals | integer |  |  | SI | Sum of pGlobals |
| SumPJournalEntries | numeric |  |  | SI | Sum of pJournalEntries |
| SumPLines | integer |  |  | SI | Sum of pLines |
| SumPPrivateGlobalUpdates | numeric |  |  | SI | Sum of pPrivateGlobalUpdates |
| SumPTime | numeric |  |  | SI | Sum of pTime |
| SumPWQMGlobals | integer |  |  | SI | Sum of pWQMGlobals |
| SumPWQMLines | integer |  |  | SI | Sum of pWQMLines |
| TotalHits | integer |  |  | SI | Count of total hits for the time period for pName |
| TotalHitsGT10 | integer |  |  | SI | Count of Total Hits greater than 10 seconds |
| TotalHitsGT2 | integer |  |  | SI | Count of Total Hits greater than 2 seconds |
| TotalHitsGT5 | integer |  |  | SI | Count of Total Hits greater than 5 seconds |
| TotalHitsGenericSort | integer |  |  | SI | Count of Total Hits using with pGenericSort set |
| pName | varchar |  |  | SI | Component or code section name from websys.Monitor |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*