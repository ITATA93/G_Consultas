# web_Msg.LB_EpisodeGroup

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBEPG_CollectionDate | date |  |  | SI | Collection Date of the episode group |
| LBEPG_CollectionTime | time |  |  | SI | Collection Time of the episode group |
| LBEPG_Facility_DR | bigint |  | FK | SI | Facility |
| LBEPG_Number | varchar |  |  | SI | Lab Episode Group Number 
Required by User.LBEpis... |
| LBEPG_ReceivedDate | date |  |  | SI | Received Date |
| LBEPG_ReceivedTime | time |  |  | SI | Received Time |
| LBEPG_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBEPG_RequestingLocation_DR | bigint |  | FK | SI | Subject Requesting Location |
| LBEPG_RowID | varchar |  |  | SI | - |
| LBEPG_SecondaryReferringDoctor_DR | bigint |  | FK | SI | Secondary Referring Doctor (used Environmental) |
| LBEPG_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBEPG_Species_DR | bigint |  | FK | SI | Species |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*