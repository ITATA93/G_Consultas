# web_Msg_RBAppointment.RescSchedSelectedOrders

**Schema:** web_Msg_RBAppointment
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ApptAssociatedFlag | bit |  |  | SI | Appointment Associated Flag (Initialized from Asso... |
| ApptID | varchar |  |  | SI | Appointment ID if this order has already been book... |
| FindParams | varchar |  |  | NO | Parent Table |
| HasAssociated | bit |  |  | SI | Has Associated Services |
| ID | varchar |  |  | NO | - |
| InterventionList | varchar |  |  | SI | Intervention List |
| LockedSlots | varchar |  |  | SI | The Locked Slots of the Order |
| OrdStatusBookable | bit |  |  | SI | The selected order(s) have a status that can be bo... |
| OrderItemID | varchar |  |  | SI | Order Item ID |
| PatientID | varchar |  |  | SI | Patient ID |
| PrevNextDayFlag | varchar |  |  | SI | Flag to indicate if Prev/Next buttons have been cl... |
| ReadOnly | bit |  |  | SI | - |
| ReasonForTransfer | varchar |  |  | SI | Reason for Transfer |
| Sequence | integer |  |  | SI | Sequence - based on the initial value of Start Dat... |
| SessionId | varchar |  |  | SI | - |
| StartDate | date |  |  | SI | Start Date |
| WaitListID | varchar |  |  | SI | Waiting List ID to link to the Appointment |
| WeeklyViewDate | date |  |  | SI | Date counter for WeeklyView is used to increment t... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*