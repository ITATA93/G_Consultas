# websys.Log

> Audit Trail of component activity.

**Schema:** websys
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

*Descripción original:* Audit Trail of component activity.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AuditDate | date |  |  | SI | Date Stamp |
| AuditTime | time |  |  | SI | Time entry added to log. |
| CacheUser | varchar |  |  | SI | Cache User |
| ClientExe | varchar |  |  | SI | - |
| ClientIP | varchar |  |  | SI | Computer Identification.
Typically IP Address. |
| ClientName | varchar |  |  | SI | - |
| Context | varchar |  |  | SI | - |
| CustomURLDesc | varchar |  |  | SI | Description of the URL string if a custom url expr... |
| Description | varchar |  |  | SI | Description for layout/column audit |
| GroupDR | bigint |  | FK | SI | - |
| IHENumber | varchar |  |  | SI | IHE Number (archived Patient Registration Number w... |
| LogonLocation | bigint |  |  | SI | cjb 22/08/2005 54089 |
| ReferencedClass | varchar |  |  | SI | - |
| ReferencedId | varchar |  |  | SI | - |
| SaveLevel | varchar |  |  | SI | - |
| SaveValue | varchar |  |  | SI | - |
| SaveValueDesc | varchar |  |  | SI | - |
| SourceType | varchar |  |  | SI | - |
| Type | varchar |  |  | SI | Event Type |
| UserDR | bigint |  | FK | SI | MEDTRAK User |
| WorkFlowId | bigint |  |  | SI | - |
| WorkFlowItemId | varchar |  |  | SI | - |
| pTimeStart | double |  |  | SI | Millisecond sequence time of activity |
| requestEPISODE | bigint |  |  | SI | - |
| requestID | varchar |  |  | SI | web Request ID |
| requestLBEpisode | bigint |  |  | SI | web request Lab Episode Number |
| requestMRADM | bigint |  |  | SI | web request mradm (or MRAdmID)
Property requestMR... |
| requestPATIENT | bigint |  |  | SI | web request PatientID (or PAPersonID) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*