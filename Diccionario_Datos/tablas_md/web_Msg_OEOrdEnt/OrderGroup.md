# web_Msg_OEOrdEnt.OrderGroup

**Schema:** web_Msg_OEOrdEnt
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| BookingViolatesOffsets | bit |  |  | SI | Booking Violates Offsets |
| Description | varchar |  |  | SI | Description |
| ID | varchar |  |  | NO | - |
| IsMainOrdEnt | bit |  |  | SI | Is Main Ord Ent |
| NotifyMod | varchar |  |  | SI | Notify Users of Change to Order |
| OrdEntHasSequenceData | bit |  |  | SI | Has Sequence Data |
| OrdEntID | varchar |  |  | SI | OrdEnt ID |
| OrdSetDateID | varchar |  |  | SI | Order Set Version ID |
| OrdSetID | varchar |  |  | SI | Order Set ID |
| ReadOnly | bit |  |  | SI | - |
| ReasonForMod | varchar |  |  | SI | Modification Reason |
| SaveAsTemp | bit |  |  | SI | Save As Temp |
| SequenceBooked | bit |  |  | SI | Sequence Booked |
| SessionId | varchar |  |  | SI | - |
| StartDate | date |  |  | SI | Sequence Start Date |
| StartTime | time |  |  | SI | Sequence Start Time |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*