# SQLUser.RB_ServiceOverride

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SOV_RowId | bigint | PK |  | NO | - |
| SOV_DOW_DR | double |  | FK | SI | Des Ref DOW |
| SOV_Date | date |  |  | SI | Date |
| SOV_DateTo | date |  |  | SI | DateTo |
| SOV_EBooking | varchar |  |  | SI | Transmit for E Booking |
| SOV_EndTime | time |  |  | SI | End Time |
| SOV_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| SOV_Message | varchar |  |  | SI | [DEPRECATED]Replaced with HTML Rich Text field SOV... |
| SOV_Message_DR | bigint |  | FK | SI | Session Message |
| SOV_NumberOfServices | double |  |  | SI | NumberOfServices |
| SOV_RBSessServ_DR | varchar |  | FK | SI | Des Ref RBSessServ |
| SOV_RBSession_DR | varchar |  | FK | SI | Des REf RBSession |
| SOV_ReasonOverride_DR | bigint |  | FK | SI | Des Ref Reason for Override |
| SOV_RefPriority_DR | bigint |  | FK | SI | Des Ref Ref Priority |
| SOV_ResEBooking | varchar |  |  | SI | Transmit Resource for E Booking |
| SOV_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| SOV_SerKeyRefPriority_DR | bigint |  | FK | SI | Des Ref Ref Priority |
| SOV_ServiceGroup_DR | bigint |  | FK | SI | Des Ref Service Group |
| SOV_ServiceKey | varchar |  |  | SI | Service Key |
| SOV_ServicePriority_DR | bigint |  | FK | SI | Des Ref ServicePriority |
| SOV_Service_DR | bigint |  | FK | SI | Des Ref Service |
| SOV_Session1_DR | varchar |  | FK | SI | Des Ref Session1 |
| SOV_StartTime | time |  |  | SI | Start Time |
| SOV_Text | varchar |  |  | SI | Text |
| SOV_UpdateDate | date |  |  | SI | Update Date |
| SOV_UpdateTime | time |  |  | SI | Update Time |
| SOV_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| SOV_WLPriority_DR | bigint |  | FK | SI | Des Ref WLPriority |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*