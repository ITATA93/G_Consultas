# web_Msg_EventSchedule.Event

**Schema:** web_Msg_EventSchedule
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AppointmentRoom | varchar |  |  | SI | The Appointment Room for the Event |
| Duration | varchar |  |  | SI | Duration of the Event in minutes |
| EditURL | varchar |  |  | SI | URL to the event editing page for specific Event i... |
| EndTime | time |  |  | SI | Logical Event EndTime |
| EventDate | date |  |  | SI | Event Start Date |
| EventID | varchar |  |  | SI | EventID for the Event |
| ID | varchar |  |  | NO | - |
| Location | varchar |  |  | SI | Location of the Event |
| Name | varchar |  |  | SI | Name/Description for the Event |
| OtherStyle | varchar |  |  | SI | event other css style |
| PatientID | varchar |  |  | SI | PatientID for the Event |
| ReadOnly | bit |  |  | SI | - |
| Resource | varchar |  |  | SI | The Resource or the Doctor for the Event |
| Room | varchar |  |  | SI | The Room for the Event |
| SessionId | varchar |  |  | SI | - |
| StartTime | time |  |  | SI | Logical Event StartTime |
| StartTimeForCalc | varchar |  |  | SI | Logical Event StartTime for calculation, will rema... |
| Status | varchar |  |  | SI | Status for the Event, usually a single letter |
| TableName | varchar |  |  | SI | The TableName in which the Event is stored |
| childsub | bigint |  |  | NO | - |
| expression | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*