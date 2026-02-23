# web_Msg.LBTransferList

**Schema:** web_Msg
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| DateReceivedFrom | date |  |  | SI | - |
| DateReceivedTo | date |  |  | SI | - |
| DateSentTo | date |  |  | SI | - |
| DepartmentID | varchar |  |  | SI | - |
| DepartmentList | varchar |  |  | SI | - |
| FinalToRefLab | bigint |  |  | SI | - |
| FinalToSite | bigint |  |  | SI | - |
| FromCollectionSite | varchar |  |  | SI | - |
| FromSentDate | date |  |  | SI | - |
| FromSite | varchar |  |  | SI | - |
| FromSiteID | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBEpisodeNo | varchar |  |  | SI | - |
| MaterialNumber | varchar |  |  | SI | [DEPRICATED] |
| PackNumber | varchar |  |  | SI | - |
| PackingListFlag | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ShowFinalTestSetStatus | varchar |  |  | SI | - |
| SpecialHandlingIDs | varchar |  |  | SI | - |
| SpecimenNumber | varchar |  |  | SI | Searches for specimen or material number |
| Status | varchar |  |  | SI | - |
| StatusCode | varchar |  |  | SI | - |
| SubjectType | varchar |  |  | SI | - |
| TestSetIDs | varchar |  |  | SI | - |
| ToRefLab | varchar |  |  | SI | - |
| ToRefLabID | varchar |  |  | SI | - |
| ToSite | varchar |  |  | SI | - |
| ToSiteID | varchar |  |  | SI | - |
| TransferRowIDList | varchar |  |  | SI | - |
| WorkArea | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*