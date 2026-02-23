# SQLUser.RB_ApptSchedule

**Schema:** SQLUser
**Columnas:** 46
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AS_RES_ParRef | bigint | PK |  | NO | RB_Resource Parent Reference |
| AS_ActualDate | date |  |  | SI | Actual session date |
| AS_ActualEndTime | time |  |  | SI | Actual session end time |
| AS_ActualStartTime | time |  |  | SI | Actual session start time |
| AS_ApptLocAll | varchar |  |  | SI | ApptLocAll  |
| AS_ApptLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| AS_AutoReq | varchar |  |  | SI | Auto Request Flag  |
| AS_Availability | double |  |  | SI | Availability (0-empty load, 1-full load) |
| AS_BookedSlots | double |  |  | SI | Number of slots booked/arrived/complete |
| AS_BriefNotRequired | varchar |  |  | SI | Brief Not Required |
| AS_ChildSub | double |  |  | NO | Child Sub (New Key) |
| AS_Date | date |  |  | NO | Appointment Date |
| AS_DayClinicOptions | varchar |  |  | SI | Day Clinic Options |
| AS_DontReinstateFlag | varchar |  |  | SI | Flag why slot shouldn't be reinstated (ASNotAvaila... |
| AS_EmergencyTheatre | varchar |  |  | SI | EmergencyTheatre |
| AS_GenerationDate | date |  |  | SI | GenerationDate |
| AS_GenerationTime | time |  |  | SI | GenerationTime |
| AS_IrregularFlag | varchar |  |  | SI | IrregularFlag |
| AS_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| AS_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| AS_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| AS_Load | double |  |  | NO | Load Level |
| AS_NoApptSession | double |  |  | NO | No Appt per session |
| AS_NoMoreBookings | varchar |  |  | SI | NoMoreBookings |
| AS_NotAvailableSlot | varchar |  |  | SI | NotAvailableSlot |
| AS_NumPatIn | double |  |  | NO | Number of patient came in |
| AS_NumPatOut | double |  |  | NO | Number of patient complete visit |
| AS_OPDRoom_DR | bigint |  | FK | SI | Des Ref OPDRoom |
| AS_OTRoomStatus | varchar |  |  | SI | OT RoomStatus |
| AS_OTSessOriginFlag | varchar |  |  | SI | Source of OT Session Origin Flag |
| AS_OperBookingMethod | varchar |  |  | SI | Oper Booking Method |
| AS_OrigSessEndTime | time |  |  | SI | Original Session End Time |
| AS_OrigSessStartTime | time |  |  | SI | Original Session Start Time |
| AS_QueueNoCount | varchar |  |  | SI | Queue Number start count |
| AS_RBEffDateSession_DR | varchar |  | FK | SI | Des Ref RBEffDateSession |
| AS_ReasonBriefNotRequired | varchar |  |  | SI | Reason for Brief/Debrief Not Required  |
| AS_ReasonForDelay_DR | bigint |  | FK | SI | Des ref RBC_ReasonForVariance |
| AS_ReasonForOvertime_DR | bigint |  | FK | SI | DR RBC_ReasonForVariance |
| AS_Remarks | varchar |  |  | SI | Remarks |
| AS_RowId | varchar |  |  | NO | - |
| AS_SessEndTime | time |  |  | NO | Session End Time |
| AS_SessStartTime | time |  |  | NO | Session Start Time |
| AS_Session | varchar |  |  | NO | Session |
| AS_SessionType_DR | bigint |  | FK | SI | Des Ref SessionType |
| AS_Slot | varchar |  |  | SI | Appointment Slot |
| AS_WebGenerated | varchar |  |  | SI | WebGenerated |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*