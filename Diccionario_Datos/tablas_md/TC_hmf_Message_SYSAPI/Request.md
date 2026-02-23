# TC_hmf_Message_SYSAPI.Request

**Schema:** TC_hmf_Message_SYSAPI
**Columnas:** 12
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
| APIOBJSTREAM | longvarchar |  |  | SI | TC API Object Stream |
| APIPARAMS | longvarchar |  |  | SI | API Params Class Object |
| APISESSIONID | varchar |  |  | SI | API SessionID |
| AdditionalInfo | varchar |  |  | SI | Add support for metadata to be added to SYSAPI req... |
| ID | varchar |  |  | SI | Class ID eg. PAPerson |
| Token | varchar |  |  | SI | TC API Logon token returned from initial TC.API.Lo... |
| tcSessionID | varchar |  |  | SI | SessionID for HMF-SYS Service |
| tcToken | varchar |  |  | SI | TC one-time security token  |
| tcUSERNAME | varchar |  |  | SI | TC User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*