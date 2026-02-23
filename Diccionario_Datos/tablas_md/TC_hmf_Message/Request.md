# TC_hmf_Message.Request

**Schema:** TC_hmf_Message
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID1 | bigint | PK |  | NO | - |
| CurrVal1 | varchar |  |  | SI | Trigger value1 |
| CurrVal2 | varchar |  |  | SI | Trigger value2 |
| CurrVal3 | varchar |  |  | SI | Trigger value3 |
| Event | varchar |  |  | SI | Trigger Event |
| ID | varchar |  |  | SI | Trigger RowID |
| IntegrationHistoryID | varchar |  |  | SI | HMF Integration History ID assigned to this trigge... |
| Interface | varchar |  |  | SI | Allocated HMF Integration for trigger event |
| PID | varchar |  |  | SI | Trigger ProcessID - $Job value for the trigger eve... |
| PreVal1 | varchar |  |  | SI | Trigger previous value1 |
| PreVal2 | varchar |  |  | SI | Trigger previous value2 |
| PreVal3 | varchar |  |  | SI | Trigger previous value3 |
| ScreenForm | varchar |  |  | SI | Trigger Screenform |
| Table | varchar |  |  | SI | Class used by HMF to pass values from TrakCare ins... |
| Trigger | varchar |  |  | SI | HMF Trigger DR |
| User | varchar |  |  | SI | Trigger User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*