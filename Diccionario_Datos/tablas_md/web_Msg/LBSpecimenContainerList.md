# web_Msg.LBSpecimenContainerList

**Schema:** web_Msg
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AnatomicalSite | varchar |  |  | SI | - |
| CollectionDateFrom | varchar |  |  | SI | - |
| CollectionDateTo | varchar |  |  | SI | - |
| Container | varchar |  |  | SI | - |
| DepartmentList | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LabEpisode | varchar |  |  | SI | - |
| LabSiteList | varchar |  |  | SI | - |
| Lesion | varchar |  |  | SI | - |
| MRN | varchar |  |  | SI | - |
| MaterialNumber | varchar |  |  | SI | [DEPRICATED] |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| Specimen | varchar |  |  | SI | - |
| SpecimenNumber | varchar |  |  | SI | Search by specimen or material number |
| SubjectID | varchar |  |  | SI | - |
| TablePrefix | varchar |  |  | SI | - |
| TestSetList | varchar |  |  | SI | - |
| TestSetStatusList | varchar |  |  | SI | - |
| URN | varchar |  |  | SI | - |
| UserSearch | bit |  |  | SI | - |
| WorkAreaList | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*