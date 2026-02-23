# web_Msg.LBProtocolProcedureList

**Schema:** web_Msg
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AnatomicalSite | varchar |  |  | SI | - |
| CTSRCH | varchar |  |  | SI | - |
| CreateWorkList | bit |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| Department | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IsStoredList | bit |  |  | SI | - |
| LBEpisodeNo | varchar |  |  | SI | - |
| LabSite | varchar |  |  | SI | - |
| Lesion | varchar |  |  | SI | - |
| NODEFAULTSRCH | varchar |  |  | SI | - |
| OATTRestriction | varchar |  |  | SI | - |
| ProcedureIDs | varchar |  |  | SI | - |
| ProcedureStatus | varchar |  |  | SI | - |
| QueueAllAny | varchar |  |  | SI | - |
| QueueIDs | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SRCHMsgID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenMaterialLabSite | varchar |  |  | SI | - |
| SpecimenNumber | varchar |  |  | SI | - |
| TTRestriction | varchar |  |  | SI | - |
| TestSetIDs | varchar |  |  | SI | - |
| ToDate | date |  |  | SI | - |
| TotalRowCount | integer |  |  | SI | - |
| WorkAreaIDs | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*