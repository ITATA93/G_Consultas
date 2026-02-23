# web_Msg.LBEpisodeSearchList

**Schema:** web_Msg
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CareProvider | varchar |  |  | SI | - |
| ClosedLabEpisodeActionsList | varchar |  |  | SI | - |
| CreationDate | date |  |  | SI | - |
| CreationDateTo | date |  |  | SI | - |
| CreationTime | time |  |  | SI | - |
| ExternalReferralFrom | bigint |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LabSiteList | varchar |  |  | SI | - |
| MRN | varchar |  |  | SI | - |
| OpenLabEpisodeActionsList | varchar |  |  | SI | - |
| PatHospitalID | varchar |  |  | SI | - |
| PatientLocation | bigint |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RefDocID | varchar |  |  | SI | - |
| ReportCareProvider | varchar |  |  | SI | - |
| ReportLocation | bigint |  |  | SI | - |
| ReportRefDocID | varchar |  |  | SI | - |
| ReportThirdParty | bigint |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| URN | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*