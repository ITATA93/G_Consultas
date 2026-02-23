# web_Msg_OEOrdEnt.OrderItem

**Schema:** web_Msg_OEOrdEnt
**Columnas:** 37
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ApptId | varchar |  |  | SI | Appt Id |
| Disabled | bit |  |  | SI | Disabled for editing |
| DoseAmount | varchar |  |  | SI | Dose Amount |
| DoseDesc | varchar |  |  | SI | Dose Description |
| DoseID | varchar |  |  | SI | Dose ID |
| DoseUnit | varchar |  |  | SI | Dose Unit |
| EndDate | date |  |  | SI | End Date |
| EndTime | time |  |  | SI | End Time |
| ExeNumber | integer |  |  | SI | Order Execute Number |
| ID | varchar |  |  | NO | - |
| ITMSectionDesc | varchar |  |  | SI | Section Description  |
| IsModified | bit |  |  | SI | Is Modified |
| ItemID | varchar |  |  | SI | Order Item ID |
| ItmDesc | varchar |  |  | SI | Order Item Description |
| MarkForAdd | bit |  |  | SI | Mark for Add |
| MarkForDelete | bit |  |  | SI | Mark for Delete |
| Node | varchar |  |  | SI | Node Letter |
| OffsetExec | varchar |  |  | SI | Offset Exec |
| OffsetItem | varchar |  |  | SI | Offset Item |
| OffsetStoredOnExec | bit |  |  | SI | Offsets for this item are set at the execution nod... |
| OffsetType | varchar |  |  | SI | Offset Type |
| OffsetUnit | varchar |  |  | SI | Offset Unit |
| OffsetValue | varchar |  |  | SI | Offset Value |
| OrdEntID | varchar |  |  | SI | OrdEnt ID |
| OrderStatus | varchar |  |  | SI | Order Status |
| OutsideOffsets | bit |  |  | SI | Outside Offsets |
| PlannedStartDate | date |  |  | SI | Planned Start Date |
| PlannedStartTime | time |  |  | SI | Planned Start Time |
| ReadOnly | bit |  |  | SI | - |
| Sequence | integer |  |  | SI | Display Sequence (from Order Set) |
| SessionId | varchar |  |  | SI | - |
| StartDate | date |  |  | SI | Start Date |
| StartTime | time |  |  | SI | Start Time |
| UseRequest | bit |  |  | SI | Use Request Data
Indicates that this order item h... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*