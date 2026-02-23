# web_Msg.UPRState

**Schema:** web_Msg
**Columnas:** 47
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AcrossEpisodes | varchar |  |  | SI | - |
| ActionContext | varchar |  |  | SI | - |
| CTLSelectedEncounter | varchar |  |  | SI | Set on load of the timeline when opened via clicki... |
| ComponentFields | varchar |  |  | SI | - |
| ContactID | varchar |  |  | SI | - |
| EncEntryParams | varchar |  |  | SI | - |
| EpisodeID | varchar |  |  | SI | - |
| EpisodeIDHome | varchar |  |  | SI | - |
| FunctionSelected | varchar |  |  | SI | - |
| HandoverDate | varchar |  |  | SI | - |
| HandoverDoctor | varchar |  |  | SI | - |
| HandoverMenuConfirmFlag | varchar |  |  | SI | - |
| HandoverMenuEntryTypeID | varchar |  |  | SI | - |
| HandoverNurse | varchar |  |  | SI | - |
| HandoverTime | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IsMinimized | bit |  |  | SI | - |
| IsRapidOrderView | varchar |  |  | SI | - |
| IsTimelineView | varchar |  |  | SI | - |
| MREncEntryID | varchar |  |  | SI | - |
| MREncounterID | varchar |  |  | SI | - |
| MREncounterIDHome | varchar |  |  | SI | - |
| NavStatus | varchar |  |  | SI | - |
| OEOrdItemID | varchar |  |  | SI | - |
| OTOActionCode | varchar |  |  | SI | Set on load of the timeline when opened via clicki... |
| OTOTabIndex | varchar |  |  | SI | - |
| OTOType | varchar |  |  | SI | - |
| OpenEncEntryAction | varchar |  |  | SI | Set by the Assistant when executing an Encounter R... |
| OpenEncEntryActionWKFL | varchar |  |  | SI | Set by the Assistant when executing an Encounter R... |
| OperationID | varchar |  |  | SI | - |
| PAPathwayID | varchar |  |  | SI | - |
| PatientID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| Reinitialize | varchar |  |  | SI | - |
| RestoreTimelineID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TimelineID | varchar |  |  | SI | - |
| UpdateButtonFlag | varchar |  |  | SI | Deprecated in TC-395071 |
| apptID | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| isDirty | bit |  |  | SI | - |
| lastEntryItemID | varchar |  |  | SI | - |
| mradm | varchar |  |  | SI | - |
| params | varchar |  |  | SI | - |
| tab | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*