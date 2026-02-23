# web_Msg.LBInstrumentScheduleList

**Schema:** web_Msg
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CareProviderLB | varchar |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| Instrument | bigint |  |  | SI | - |
| InstrumentGroup | bigint |  |  | SI | - |
| InstrumentGroupLB | varchar |  |  | SI | - |
| InstrumentLB | varchar |  |  | SI | - |
| InterfaceType | varchar |  |  | SI | - |
| InterfaceTypeLB | varchar |  |  | SI | - |
| LabEpisodeNumber | varchar |  |  | SI | - |
| LabSite | bigint |  |  | SI | - |
| LabSiteLB | varchar |  |  | SI | - |
| PatientFirstName | varchar |  |  | SI | - |
| PatientLocationLB | varchar |  |  | SI | - |
| PatientSurname | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RequestNumber | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ShowOnlyPatients | bit |  |  | SI | - |
| SpecimenNumber | varchar |  |  | SI | Searches for specimen or material number |
| Status | varchar |  |  | SI | - |
| StatusLB | varchar |  |  | SI | - |
| SubjectID | varchar |  |  | SI | - |
| SubjectType | bigint |  |  | SI | - |
| SubjectTypeLB | varchar |  |  | SI | - |
| TimeFrom | time |  |  | SI | - |
| TimeTo | time |  |  | SI | - |
| URN | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*