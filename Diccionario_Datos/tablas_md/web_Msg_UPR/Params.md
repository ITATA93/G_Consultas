# web_Msg_UPR.Params

**Schema:** web_Msg_UPR
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| UPRParamAcrossEncounters | varchar |  |  | SI | A string containing the Across Encounters checkbox... |
| UPRParamCareProviderID | varchar |  |  | SI | A string containing one or more (carat delimited) ... |
| UPRParamCareProviderTypeID | varchar |  |  | SI | A string containing one or more (carat delimited) ... |
| UPRParamDateFrom | varchar |  |  | SI | A string containing the Date From field |
| UPRParamDateTo | varchar |  |  | SI | A string containing the Date To field |
| UPRParamEntrySearch | varchar |  |  | SI | A string containing the Entry Search |
| UPRParamEntryTypeID | varchar |  |  | SI | A string containing one or more (carat delimited) ... |
| UPRParamEpisodeType | varchar |  |  | SI | A string containing  one or more Episode Type IDs |
| UPRParamMREncounterID | varchar |  |  | SI | A string containing the Encounter ID |
| UPRParamProblemList | varchar |  |  | SI | A string containing one or more (carat delimited) ... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*