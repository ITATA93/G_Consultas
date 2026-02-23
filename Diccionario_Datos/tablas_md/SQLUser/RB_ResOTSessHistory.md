# SQLUser.RB_ResOTSessHistory

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTSH_ParRef | bigint | PK |  | NO | RB_Resource Parent Reference |
| OTSH_ActualEndTime | time |  |  | SI | OT Session Actual End Time |
| OTSH_ActualStartTime | time |  |  | SI | OT Session Actual Start Time |
| OTSH_Anaes_DR | varchar |  | FK | SI | Anaesthetist |
| OTSH_ApptScheduleText | varchar |  |  | SI | Text RBApptSchedule |
| OTSH_ApptSchedule_DR | varchar |  | FK | SI | Des Ref RBApptSchedule |
| OTSH_ChangedFromRS | varchar |  |  | SI | Changed from Resource Schedule |
| OTSH_Childsub | double |  |  | NO | Childsub |
| OTSH_Consultant_DR | varchar |  | FK | SI | Main Consultant owner |
| OTSH_Date | date |  |  | NO | OT Session Date |
| OTSH_Desc | varchar |  |  | SI | Session Description |
| OTSH_EffDateSession_DR | varchar |  | FK | SI | Des Ref RBEffDateSession |
| OTSH_EmergencyTheatre | varchar |  |  | SI | EmergencyTheatre |
| OTSH_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| OTSH_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| OTSH_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| OTSH_LongDesc | varchar |  |  | SI | Session Long Description |
| OTSH_MainSpecialty_DR | bigint |  | FK | SI | Main Specialty |
| OTSH_NoMoreBookings | varchar |  |  | SI | NoMoreBookings |
| OTSH_OTRoomStatus | varchar |  |  | SI | OTRoomStatus |
| OTSH_OTSessOriginFlag | varchar |  |  | SI | Source of OT Session Origin Flag |
| OTSH_OperBookingMethod | varchar |  |  | SI | Oper Booking Method |
| OTSH_OrigSessEndTime | time |  |  | SI | Original Session End Time |
| OTSH_OrigSessStartTime | time |  |  | SI | Original Session Start Time |
| OTSH_RSAutoGenEndDate | varchar |  |  | SI | RS Eff Date Session AutoGenEndDate |
| OTSH_RSCPClinicOptions | varchar |  |  | SI | RS Eff Date Session CPClinicOptions (SI - Single c... |
| OTSH_RSConvRoutine | varchar |  |  | SI | Conversion Routine generation flag |
| OTSH_RSIgnorePubHol | varchar |  |  | SI | RS Eff Date Session Ignore Public Holidays |
| OTSH_RSIrregularSchedulle | varchar |  |  | SI | RS Eff Date Session Irregular Schedulle (SESS spel... |
| OTSH_RSLastGenFromDate | date |  |  | SI | RS Eff Date Session Schedule Last Generated From D... |
| OTSH_RSLastWeek | varchar |  |  | SI | RS Eff Date Session Last Week |
| OTSH_RSLoad | double |  |  | SI | RS Eff Date Session Load Level |
| OTSH_RSMRVolume_DR | varchar |  | FK | SI | RS Eff Date Session Des Ref Volume_DR |
| OTSH_RSNoOverbookAllowed | double |  |  | SI | RS Eff Date Session Number Overbook Allowed |
| OTSH_RSNoSlots | double |  |  | SI | RS Eff Date Session Number of Slots/Session |
| OTSH_RSNumberOfWeeks | double |  |  | SI | RS Eff Date Session Number Of Weeks |
| OTSH_RSPatientType | varchar |  |  | SI | RS Eff Date Session Patient Type (I InPatient,O Ou... |
| OTSH_RSRSWeeklyCycle_DR | bigint |  | FK | SI | RS Eff Date Session WeeklyCycle  |
| OTSH_RSRestricted | varchar |  |  | SI | RS Eff Date Session Restricted |
| OTSH_RSSESSDOW_DR | double |  | FK | SI | RS Eff Date Session Des Ref Day of the week |
| OTSH_RSSchedGeneratedFrom | date |  |  | SI | RS Eff Date Session Schedule Generated From |
| OTSH_RSSchedGeneratedUntil | date |  |  | SI | RS Eff Date Session Schedule Generated Until |
| OTSH_RSScheduleStartDate | date |  |  | SI | RS Eff Date Session Start Date |
| OTSH_RSSlotLength | double |  |  | SI | RS Eff Date Session Slot Length in minutes |
| OTSH_RSTimeEnd | time |  |  | SI | RS Eff Date Session End Time |
| OTSH_RSTimeStart | time |  |  | SI | RS Eff Date Session Time Start |
| OTSH_RSWeek1 | varchar |  |  | SI | RS Eff Date Session Week 1 |
| OTSH_RSWeek2 | varchar |  |  | SI | RS Eff Date Session Week 2 |
| OTSH_RSWeek3 | varchar |  |  | SI | RS Eff Date Session Week 3 |
| OTSH_RSWeek4 | varchar |  |  | SI | RS Eff Date Session Week 4 |
| OTSH_RSWeek5 | varchar |  |  | SI | RS Eff Date Session Week 5 |
| OTSH_ReasSessStatChange | varchar |  |  | SI | Reason Status Change Text |
| OTSH_ReasSessStatChange_DR | bigint |  | FK | SI | Reason Status Change |
| OTSH_ReasonForDelay_DR | bigint |  | FK | SI | Des ref RBC_ReasonForVariance |
| OTSH_ReasonForOvertime_DR | bigint |  | FK | SI | DR RBC_ReasonForVariance |
| OTSH_RowId | varchar |  |  | NO | - |
| OTSH_SchedCreated | varchar |  |  | SI | OT Session Created method RS Created in Res Schedu... |
| OTSH_SchedCreatedDate | date |  |  | SI | OT Session Created Date |
| OTSH_SchedCreatedTime | time |  |  | SI | OT Session Created Time |
| OTSH_SessEndTime | time |  |  | NO | OT Session Current End Time |
| OTSH_SessStartTime | time |  |  | NO | OT Session Current Start Time |
| OTSH_SessionType_DR | bigint |  | FK | SI | Des Ref SessionType |
| OTSH_Surgeon_DR | varchar |  | FK | SI | Surgeon |
| OTSH_UpdActionType | varchar |  |  | SI | OT Session History Update upon Action Type (I Inse... |
| OTSH_UpdateAction | varchar |  |  | SI | OT Session History Update Action (Specialty, CP, S... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*