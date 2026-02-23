# websys.MonitorDatabase

> "Persist database statistics for monitoring over time<br/>

**Schema:** websys
**Columnas:** 51
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Persist database statistics for monitoring over time<br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BlockFormat | varchar |  |  | SI | From the detail of SYS.Database ##; noalert
all t... |
| BlockSize | integer |  |  | SI | - |
| Blocks | integer |  |  | SI | - |
| BlocksPerMap | integer |  |  | SI | - |
| ClusterMountMode | bit |  |  | SI | - |
| ClusterMounted | bit |  |  | SI | - |
| CurrentMaps | integer |  |  | SI | - |
| Directory | varchar |  |  | SI | - |
| DirectoryBlock | integer |  |  | SI | - |
| Encrypted | varchar |  |  | SI | - |
| EncryptedDB | varchar |  |  | SI | - |
| EncryptionKeyID | varchar |  |  | SI | - |
| Expanding | bit |  |  | SI | - |
| ExpansionSize | integer |  |  | SI | - |
| FreeBlocks | integer |  |  | SI | Deprecated in HS2015.1 so removed from monitor - a... |
| FreeSpace | integer |  |  | SI | - |
| Full | bit |  |  | SI | - |
| GlobalJournalState | varchar |  |  | SI | - |
| InActiveMirror | bit |  |  | SI | - |
| Journal | varchar |  |  | SI | - |
| LastExpansionTime | varchar |  |  | SI | - |
| MaxSize | integer |  |  | SI | - |
| MaximumSizeinGB | varchar |  |  | SI | - |
| MirrorActivationRequired | bit |  |  | SI | - |
| MirrorDBCreatedNew | bit |  |  | SI | - |
| MirrorDBName | varchar |  |  | SI | - |
| MirrorFailoverDB | bit |  |  | SI | - |
| MirrorNoWrite | bit |  |  | SI | - |
| MirrorSetName | varchar |  |  | SI | - |
| Mirrored | bit |  |  | SI | - |
| Mounted | bit |  |  | SI | - |
| Name | varchar |  |  | SI | From the query
ROWSPEC = "Name:%String,Mirror:%St... |
| NewGlobalCollation | integer |  |  | SI | - |
| NewGlobalGrowthBlock | integer |  |  | SI | - |
| NewGlobalIsKeep | varchar |  |  | SI | - |
| NewGlobalPointerBlock | integer |  |  | SI | - |
| NumberOfConfigDB | integer |  |  | SI | - |
| ReadOnly | varchar |  |  | SI | - |
| ReadOnlyMounted | bit |  |  | SI | - |
| Reinitialize | bit |  |  | SI | - |
| ResourceName | varchar |  |  | SI | - |
| RunDate | date |  |  | SI | Date this run was started
RunDate and RunTime uni... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| SFN | integer |  |  | SI | - |
| Size | integer |  |  | SI | - |
| SizeinMB | integer |  |  | SI | - |
| Skeleton | bit |  |  | SI | - |
| SparseDB | bit |  |  | SI | - |
| Status | varchar |  |  | SI | - |
| StatusInt | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*