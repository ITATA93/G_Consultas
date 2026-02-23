# web_Msg.LBEpisodeList

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CareProviders | varchar |  |  | SI | - |
| EpisodeID | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCareProvID | varchar |  |  | SI | - |
| LBEPDOB | date |  |  | SI | - |
| LBEPExternalReferralID | varchar |  |  | SI | - |
| LBEPExternalReferralNumber | varchar |  |  | SI | - |
| LBEPFirstName | varchar |  |  | SI | - |
| LBEPSex | bigint |  |  | SI | - |
| LBEPSurname | varchar |  |  | SI | - |
| LBPatLocID | varchar |  |  | SI | - |
| LBRefDocID | varchar |  |  | SI | - |
| LBSubjectID | varchar |  |  | SI | - |
| LabSites | varchar |  |  | SI | - |
| PatientID | varchar |  |  | SI | - |
| PatientLocations | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*