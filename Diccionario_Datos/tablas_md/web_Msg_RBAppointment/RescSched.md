# web_Msg_RBAppointment.RescSched

**Schema:** web_Msg_RBAppointment
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AssocOrderID | varchar |  |  | SI | Associated Order ID (Service Type Diary Only) |
| CONTEXT | varchar |  |  | SI | CONTEXT |
| Date | date |  |  | SI | Date field  |
| DiaryCount | integer |  |  | SI | Count of diaries displayed |
| HospID | varchar |  |  | SI | Hospital ID as a string |
| ID | varchar |  |  | NO | - |
| LocID | varchar |  |  | SI | Location ID as a string |
| LocationsList | varchar |  |  | SI | LocationsList |
| NextAvailable | bit |  |  | SI | Find Next Available Day (Service Type Diary Only)... |
| NoPrefs | bit |  |  | SI | NoPrefs |
| OverbookEnabled | bit |  |  | SI | OverbookEnabled  |
| PrevNextDayFlag | varchar |  |  | SI | Flag to indicate if Prev/Next buttons have been cl... |
| PrevNextDayOffset | integer |  |  | SI | PrevNextDayOffset |
| ReadOnly | bit |  |  | SI | - |
| ReasonForTransfer | varchar |  |  | SI | Reason for Transfer |
| SelectedOrderIndex | integer |  |  | SI | SelectedOrder Index - the index of the currently d... |
| SessionId | varchar |  |  | SI | - |
| WeeklyView | bit |  |  | SI | Weekly View (toggles back and forth)  |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*