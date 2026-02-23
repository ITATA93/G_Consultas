# web_Msg.LBProtocolList

**Schema:** web_Msg
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| DepartmentList | varchar |  |  | SI | - |
| FailureType | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCProcedureID | varchar |  |  | SI | - |
| MaterialSpecimenLabSiteID | varchar |  |  | SI | - |
| OECPriorityID | varchar |  |  | SI | Priority ID for LBProtocolGrid.List select |
| PriorityID | varchar |  |  | SI | Priority ID for LBProtocol.WorkBench search |
| QueueAllAny | varchar |  |  | SI | - |
| QueueIDs | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TestSetID | varchar |  |  | SI | - |
| TestSetLabSiteID | varchar |  |  | SI | - |
| WorkAreaList | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*