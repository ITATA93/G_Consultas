# websys.PrintService

**Schema:** websys
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Active | bit |  |  | SI | Set true when the service is started
and Register... |
| CacheProcessesAllowed | integer |  |  | SI | - |
| CacheProcessesInUse | integer |  |  | SI | Current number of Cache Processes |
| CurrentConfig | varchar |  |  | SI | Receives a string from the Print Service when it i... |
| EPS | bit |  |  | SI | Flag if service is using EPS |
| GlobalCrystalLicenses | integer |  |  | SI | Is a copy of websys.Configuration.CrystalRptLicenc... |
| GroupLimited | bit |  |  | SI | Set True if the Service participates in the Total ... |
| MinCacheProcesses | integer |  |  | SI | Minimum Processes to kepp for High Priority Cache ... |
| MinCrystalProcesses | integer |  |  | SI | Minimum Processes to kepp for High Priority Crysta... |
| PrinterGroup | varchar |  |  | SI | Comma-List of Printer Group Codes that this Servic... |
| ProcessesAllowed | integer |  |  | SI | Max number of allowed (licensed) concurrent print ... |
| ProcessesInUse | integer |  |  | SI | The curernt number of processes in use for this se... |
| ServerName | varchar |  |  | SI | Host Name of the server running the print service |
| UpdateDate | date |  |  | SI | DateTime of last contact with service. Sett notes ... |
| UpdateTime | time |  |  | SI | DateTime of Last contact with service.
Use the da... |
| WordProcessesAllowed | integer |  |  | SI | Limits the number of Word processes that can run o... |
| WordProcessesInUse | integer |  |  | SI | Current Word Processes running |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*