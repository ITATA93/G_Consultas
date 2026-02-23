# TC_hmf_Lib.Message

**Schema:** TC_hmf_Lib
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFLIBMSG_Code | varchar |  |  | NO | Message code |
| HMFLIBMSG_DateFrom | date |  |  | SI | Date From |
| HMFLIBMSG_DateTo | date |  |  | SI | Date To |
| HMFLIBMSG_Desc | varchar |  |  | SI | Message description |
| HMFLIBMSG_Enabled | bit |  |  | SI | Enabled flag |
| HMFLIBMSG_ExtCode | varchar |  |  | SI | Message external code |
| HMFLIBMSG_FormatDR | bigint |  | FK | SI | Message format eg. HL7, CDA etc |
| HMFLIBMSG_InboundFlag | bit |  |  | SI | Inbound Enabled flag |
| HMFLIBMSG_OutboundFlag | bit |  |  | SI | Outbound Enabled flag |
| HMFLIBMSG_QueryRequest | varchar |  |  | SI | Query Request Message class |
| HMFLIBMSG_QueryResponse | varchar |  |  | SI | Query Response Message class |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*