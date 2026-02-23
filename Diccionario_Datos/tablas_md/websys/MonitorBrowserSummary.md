# websys.MonitorBrowserSummary

> "Summary of websys.Monitor page performance statistics UserAgentString. <br/>

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Summary of websys.Monitor page performance statistics UserAgentString. <br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Browser | varchar |  |  | SI | Browser |
| BrowserVersion | varchar |  |  | SI | BrowserVersion |
| Platform | varchar |  |  | SI | Platform |
| PlatformVersion | varchar |  |  | SI | Platform Version |
| RunDate | date |  |  | SI | Date of data from websys.Monitor
RunDate and RunT... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| TotalHits | integer |  |  | SI | Total Hits |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*