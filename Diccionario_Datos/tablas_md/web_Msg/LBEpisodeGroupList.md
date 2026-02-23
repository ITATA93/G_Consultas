# web_Msg.LBEpisodeGroupList

**Schema:** web_Msg
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBEPGCollectionDateFrom | date |  |  | SI | Collection Date From |
| LBEPGCollectionDateTo | date |  |  | SI | Collection Date To |
| LBEPGFacilityDR | bigint |  | FK | SI | Facility |
| LBEPGNumber | varchar |  |  | SI | Episode Group Number |
| LBEPGReceivedDateFrom | date |  |  | SI | Received Date From |
| LBEPGReceivedDateTo | date |  |  | SI | Received Date To |
| LBEPGReferringDoctors | varchar |  |  | SI | Referring Doctors |
| LBEPGRequestingLocations | varchar |  |  | SI | Subject Requesting Location |
| LBEPGSecondaryReferringDoctors | varchar |  |  | SI | Secondary Referring Doctors |
| LBEPGSpeciesBreedDR | varchar |  | FK | SI | Breed |
| LBEPGSpeciesDR | bigint |  | FK | SI | Species |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*