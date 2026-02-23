# TC_hmf_Message_SYSAPI.Response

**Schema:** TC_hmf_Message_SYSAPI
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID1 | bigint | PK |  | NO | - |
| APIACTION | varchar |  |  | SI | API Action eg. TC.api.PAPerson.Edit
Request & Ter... |
| APICLASSNAME | varchar |  |  | SI | API Classname eg. TC.api.PAPerson.Edit |
| APIOBJSTREAM | longvarchar |  |  | SI | TC API Logon token returned from initial TC.API.Lo... |
| APISTATUS | varchar |  |  | SI | API Status |
| ID | varchar |  |  | SI | Class ID eg. PAPerson |
| INTEGRATIONHISTORYID | integer |  |  | SI | Integration History ID |
| TSESSIONID | varchar |  |  | SI | TrakCare API SessionID |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*