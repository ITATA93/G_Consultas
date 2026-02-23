# web_Msg_EventSchedule.WeeklySlots

**Schema:** web_Msg_EventSchedule
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| EndTime | varchar |  |  | SI | Logical EndTime, defaults to 6:00 p.m. |
| EventURL | varchar |  |  | SI | Base URL for linking to the event edit page |
| EventURLEventIDParameter | varchar |  |  | SI | Name of the event ID parameter used by the event e... |
| ID | varchar |  |  | NO | - |
| Interval | integer |  |  | SI | Time Interval for slots in seconds, defaults to 30... |
| MinDurationLogical | integer |  |  | SI | Minimum visual duration of an event |
| PatientID | varchar |  |  | SI | Patient ID |
| ReadOnly | bit |  |  | SI | - |
| RefreshDataClassName | varchar |  |  | SI | Class name to refresh data when paging |
| RefreshDataMethodName | varchar |  |  | SI | Method name to refresh data when paging
Should re... |
| RefreshDataParams | varchar |  |  | SI | Storage for parameters to refresh data when paging |
| SelectedWeek | date |  |  | SI | SelectedWeek's start date |
| SessionId | varchar |  |  | SI | - |
| SlotURL | varchar |  |  | SI | Base URL for linking to the event booking page |
| SlotURLApptEndTimeParameter | varchar |  |  | SI | Name of the appt end time parameter used by the ev... |
| SlotURLDateParameter | varchar |  |  | SI | Name of the date parameter used by the event booki... |
| SlotURLTimeParameter | varchar |  |  | SI | Name of the time parameter used by the event booki... |
| StartTime | varchar |  |  | SI | Logical StartTime, defaults to 8:30 a.m. |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*