# web_Msg.LBSpecimenCollectionRequest

**Schema:** web_Msg
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AdmissionType | varchar |  |  | SI | - |
| CONTEXT | varchar |  |  | SI | - |
| CTSRCH | varchar |  |  | SI | - |
| CurrentPatientLocation | varchar |  |  | SI | - |
| Department | varchar |  |  | SI | - |
| EndDate | date |  |  | SI | - |
| EndTime | time |  |  | SI | - |
| EpisodeLocation | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBEpisodeNo | varchar |  |  | SI | - |
| LabSiteID | varchar |  |  | SI | - |
| MRN | varchar |  |  | SI | - |
| NODEFAULTSRCH | varchar |  |  | SI | - |
| OrderLocation | varchar |  |  | SI | - |
| OrderPriority | varchar |  |  | SI | - |
| OrderStartDate | date |  |  | SI | - |
| OrderStartTime | time |  |  | SI | - |
| PatientHospital | varchar |  |  | SI | - |
| PatientLocation | varchar |  |  | SI | - |
| PatientLocationList | varchar |  |  | SI | - |
| PatientType | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ShowCollected | varchar |  |  | SI | - |
| URN | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| hiddenSpecimenGroupIDs | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*