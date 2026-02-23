# SQLUser.RB_Resource

**Schema:** SQLUser
**Columnas:** 48
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RES_RowId | bigint | PK |  | NO | - |
| RES_Active | varchar |  |  | SI | Active |
| RES_AdmittingRights | varchar |  |  | SI | Admitting Rights |
| RES_AllocatedSchedule | varchar |  |  | SI | Allocated Schedule |
| RES_Availability | double |  |  | SI | Availability of resource-doctor load (1-free) |
| RES_BillingAgentID | varchar |  |  | SI | Billing Agent ID |
| RES_CPClinicOptions | varchar |  |  | SI | CPClinicOptions |
| RES_CPLocationNo | varchar |  |  | SI | CPLocationNo |
| RES_CTLOC_DR | bigint |  | FK | NO | RES RowID
Property RESRowId As %String(COLLATION ... |
| RES_CTPCP_DR | varchar |  | FK | SI | Des Ref to CT_CareProvider |
| RES_Code | varchar |  |  | SI | Code |
| RES_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| RES_CourierCopies | numeric |  |  | SI | The default number of copies of Lab Doctors Report... |
| RES_CurrLoadLimit | double |  |  | SI | Load limit of current session |
| RES_CurrNumPatIn | double |  |  | SI | Number of patient come into current session |
| RES_CurrNumPatOut | double |  |  | SI | Number of patient discharge in curr session |
| RES_CurrPendAppt | double |  |  | SI | Curr Session Number of Pending Appointment |
| RES_CurrSessSummary | varchar |  |  | SI | Summary of Current sess (load,PatIn,PatOut) |
| RES_CurrSession_DR | varchar |  | FK | SI | Des Ref to RB_ApptSchedule (current session) |
| RES_DateActiveFrom | date |  |  | SI | Date Active From |
| RES_DateActiveTo | date |  |  | SI | Date Active To |
| RES_DateHold | date |  |  | SI | Date on Hold |
| RES_DateTo | date |  |  | SI | Date To |
| RES_DaysOTClosed | double |  |  | SI | Days OT Closed |
| RES_Desc | varchar |  |  | SI | Description of the Resource |
| RES_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| RES_EBookNotes | varchar |  |  | SI | SISS E-Booking Notes |
| RES_EQ_DR | bigint |  | FK | SI | Des Ref to Equipment |
| RES_ExternalVenue | varchar |  |  | SI | ExternalVenue |
| RES_IgnorePubHol | varchar |  |  | SI | IgnorePubHol |
| RES_LastSchedEDate | date |  |  | SI | End Date of last schedule generation |
| RES_LastSchedSDate | date |  |  | SI | Start date of last schedule generation |
| RES_MRRequest | varchar |  |  | SI | MR Request |
| RES_MainLocation | varchar |  |  | SI | Main Location |
| RES_OperBookingMethod | varchar |  |  | SI | Oper Booking Method |
| RES_OperTheatreType_DR | bigint |  | FK | SI | Des Ref OperTheatreType |
| RES_PrincipalCPNumber | varchar |  |  | SI | Principal Care Provider Number |
| RES_QueueLen | double |  |  | SI | Len of the queue |
| RES_RefHosp_DR | bigint |  | FK | SI | Des Ref RefHosp |
| RES_Room_DR | bigint |  | FK | SI | Des REf CTLOC |
| RES_ScheduleForThisHospital | varchar |  |  | SI | Schedule For This Hospital |
| RES_ScheduleRequired | varchar |  |  | SI | Is Schedule Required |
| RES_ShowInOperWB | varchar |  |  | SI | Show In Oper theatre WorkBench |
| RES_StockLoc_DR | bigint |  | FK | SI | Stock Location |
| RES_Type | varchar |  |  | SI | Resource Type |
| RES_Venue | varchar |  |  | SI | Venue |
| RES_WLOutpatientRights | varchar |  |  | SI | WL Outpatient Rights |
| RES_WLTriageRights | varchar |  |  | SI | WL Triage Rights |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*