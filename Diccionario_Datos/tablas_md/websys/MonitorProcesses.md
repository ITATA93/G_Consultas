# websys.MonitorProcesses

**Schema:** websys
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CSPSessionID | varchar |  |  | SI | - |
| ClientExecutableName | varchar |  |  | SI | - |
| ClientIPAddress | varchar |  |  | SI | - |
| ClientNodeName | varchar |  |  | SI | - |
| CommandsExecuted | bigint |  |  | SI | - |
| CurrentDevice | varchar |  |  | SI | - |
| DataBlockWrites | integer |  |  | SI | - |
| DataBlockWritesDelta | integer |  |  | SI | - |
| DataBlockWritesRate | integer |  |  | SI | - |
| ExtraDetails | varchar |  |  | SI | - |
| GlobalBlocks | integer |  |  | SI | - |
| GlobalDiskReads | integer |  |  | SI | - |
| GlobalDiskReadsDelta | integer |  |  | SI | - |
| GlobalDiskReadsRate | integer |  |  | SI | - |
| GlobalReferences | bigint |  |  | SI | - |
| GlobalReferencesDelta | integer |  |  | SI | - |
| GlobalReferencesRate | integer |  |  | SI | - |
| GlobalUpdates | integer |  |  | SI | - |
| GlobalUpdatesDelta | integer |  |  | SI | - |
| GlobalUpdatesRate | integer |  |  | SI | - |
| JobNumber | integer |  |  | SI | - |
| JobType | integer |  |  | SI | - |
| JournalEntries | integer |  |  | SI | - |
| JournalEntriesDelta | integer |  |  | SI | - |
| JournalEntriesRate | integer |  |  | SI | - |
| Label | varchar |  |  | SI | - |
| LicenseUserId | varchar |  |  | SI | - |
| LinesExecuted | bigint |  |  | SI | - |
| LinesExecutedDelta | integer |  |  | SI | - |
| LinesExecutedRate | integer |  |  | SI | - |
| Location | varchar |  |  | SI | - |
| LoginRoles | varchar |  |  | SI | - |
| MemoryPeak | integer |  |  | SI | - |
| NameSpace | varchar |  |  | SI | - |
| NewProcess | bit |  |  | SI | - |
| OSUserName | varchar |  |  | SI | - |
| Pid | integer |  |  | SI | - |
| PidExternal | varchar |  |  | SI | - |
| PrincipalDevice | varchar |  |  | SI | - |
| Priority | integer |  |  | SI | - |
| PrivateGlobalBlockCount | integer |  |  | SI | - |
| PrivateGlobalReferences | bigint |  |  | SI | - |
| PrivateGlobalReferencesDelta | integer |  |  | SI | - |
| PrivateGlobalReferencesRate | integer |  |  | SI | - |
| PrivateGlobalUpdates | bigint |  |  | SI | - |
| PrivateGlobalUpdatesDelta | integer |  |  | SI | - |
| PrivateGlobalUpdatesRate | integer |  |  | SI | - |
| ProcessID | varchar |  |  | SI | - |
| Roles | varchar |  |  | SI | - |
| Routine | varchar |  |  | SI | - |
| RunDate | date |  |  | SI | - |
| RunTime | time |  |  | SI | - |
| State | varchar |  |  | SI | - |
| Switch10 | bit |  |  | SI | - |
| TimeInterval | numeric |  |  | SI | - |
| UserName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*