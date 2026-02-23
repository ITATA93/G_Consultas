# SQLUser.RB_ResEffDateSession

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SESS_ParRef | varchar | PK |  | NO | RB_ResEffDate Parent Reference |
| SESS_APIEnabled | varchar |  |  | SI | API Enabled |
| SESS_AutoGenEndDate | date |  |  | SI | Auto Gen End Date |
| SESS_Bed_DR | varchar |  | FK | SI | Des Ref Bed |
| SESS_BookApptFrom | date |  |  | SI | Book Appointments From Date |
| SESS_CPClinicOptions | varchar |  |  | SI | CPClinicOptions |
| SESS_ChangeFlag | varchar |  |  | SI | ChangeFlag |
| SESS_Childsub | double |  |  | NO | Childsub |
| SESS_ClinicGroup_DR | bigint |  | FK | SI | Des Ref ClinicGroup |
| SESS_ClinicPrintOption_DR | bigint |  | FK | SI | Print Package, lookup to Resource Booking code tab... |
| SESS_ClinicSessCode | varchar |  |  | SI | Unique Clinic Session Code |
| SESS_Clinic_DR | bigint |  | FK | SI | Des Ref Clinic |
| SESS_DOW_DR | double |  | FK | SI | Des Ref Day of the week |
| SESS_DateBookUntil | date |  |  | SI | Date Book Until |
| SESS_DaysDepRestr | double |  |  | SI | number of Days to ignore Dep Restr |
| SESS_Desc | varchar |  |  | SI | Description |
| SESS_EBookPriority | varchar |  |  | SI | E-Booker Priorities |
| SESS_EBooking | varchar |  |  | SI | Transmit for E Booking |
| SESS_EmergencyTheatre | varchar |  |  | SI | EmergencyTheatre |
| SESS_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| SESS_GenerateFrom | date |  |  | SI | GenerateFrom |
| SESS_GenerateTo | date |  |  | SI | GenerateTo |
| SESS_IgnorePubHol | varchar |  |  | SI | Ignore Pub Hol |
| SESS_IrregularSchedulle | varchar |  |  | SI | Irregular Schedulle |
| SESS_LastGenFromDate | date |  |  | SI | LastGenFromDate |
| SESS_LastWeek | varchar |  |  | SI | Last Week |
| SESS_Load | double |  |  | SI | Load Level |
| SESS_MRVolume_DR | varchar |  | FK | SI | Des Ref Volume_DR |
| SESS_NCTTier2CodeDR | bigint |  | FK | SI | National Tier 2 Code |
| SESS_NoApptSlot | double |  |  | SI | No of Appointments per Slot |
| SESS_NoOverbookAllowed | double |  |  | SI | Number Overbook Allowed |
| SESS_NoSlots | double |  |  | SI | Number of Slots/Session |
| SESS_NumberOfMonths | double |  |  | SI | Number Of Months |
| SESS_NumberOfWeeks | double |  |  | SI | Number Of Weeks |
| SESS_OBSettings | varchar |  |  | SI | OBSettings |
| SESS_OPEpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| SESS_OperBookingMethod | varchar |  |  | SI | Oper Booking Method |
| SESS_PatientType | varchar |  |  | SI | Patient Type |
| SESS_ProcedureClinic | varchar |  |  | SI | ProcedureClinic |
| SESS_ReasForChange | varchar |  |  | SI | Reason for Change |
| SESS_RequestMR | varchar |  |  | SI | Request MR |
| SESS_ResEBooking | varchar |  |  | SI | Do Not Transmit Resource for E Booking |
| SESS_Restricted | varchar |  |  | SI | Restricted |
| SESS_Room_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SESS_RowId | varchar |  |  | NO | - |
| SESS_ScheduleGenerFlag | varchar |  |  | SI | Sched Gener Flag |
| SESS_ScheduleGeneratedFrom | date |  |  | SI | ScheduleGeneratedFrom |
| SESS_ScheduleGeneratedUntil | date |  |  | SI | Schedule Generated Until |
| SESS_ScheduleStartDate | date |  |  | SI | Schedule Start Date |
| SESS_SessionLabels | varchar |  |  | SI | Session Labels |
| SESS_SessionNo | varchar |  |  | SI | Session Number |
| SESS_SessionType_DR | bigint |  | FK | SI | Des Ref Session Type |
| SESS_SignifFacility_DR | bigint |  | FK | SI | Des Ref SignifFacility |
| SESS_SlotLength | double |  |  | SI | Slot Length in minutes |
| SESS_TimeEnd | time |  |  | SI | Session End Time |
| SESS_TimeStart | time |  |  | SI | Session Time Start |
| SESS_UpdatedDate | date |  |  | SI | Updated Date |
| SESS_UpdatedTime | time |  |  | SI | Updated Time |
| SESS_UpdatedUser | bigint |  |  | SI | Last Updated User |
| SESS_Ward_DR | bigint |  | FK | SI | Des Ref Ward |
| SESS_Week1 | varchar |  |  | SI | Week 1 |
| SESS_Week2 | varchar |  |  | SI | Week 2 |
| SESS_Week3 | varchar |  |  | SI | Week 3 |
| SESS_Week4 | varchar |  |  | SI | Week 4 |
| SESS_Week5 | varchar |  |  | SI | Week 5 |
| SESS_WeeklyCycle_DR | bigint |  | FK | SI | Des Ref WeeklyCycle |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*