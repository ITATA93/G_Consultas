# SQLUser.RB_ApptScheduleCP

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ASCP_ParRef | varchar | PK |  | NO | RB_ApptSchedule Parent Reference |
| ASCP_Active | varchar |  |  | SI | Active |
| ASCP_ActualArrivalTime | time |  |  | SI | Actual arrival time |
| ASCP_AddedDate | date |  |  | SI | Added Date |
| ASCP_AddedTime | time |  |  | SI | Added Time |
| ASCP_CareProvRole | varchar |  |  | SI | CareProvRole |
| ASCP_CareProvType | varchar |  |  | SI | CareProvType |
| ASCP_CareProv_DR | varchar |  | FK | SI | Des Ref Care Prov |
| ASCP_ChildSub | double |  |  | NO | Child sub |
| ASCP_LastUpdateDate | date |  |  | SI | Last Update Date |
| ASCP_LastUpdateTime | time |  |  | SI | Last Update Time |
| ASCP_LastUpdateUser | bigint |  |  | SI | Last Update User |
| ASCP_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| ASCP_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| ASCP_Reason_DR | bigint |  | FK | SI | ReasonDR |
| ASCP_RowId | varchar |  |  | NO | - |
| ASCP_SecondSurg | varchar |  |  | SI | Second Surgeon |
| ASCP_Session_DR | varchar |  | FK | SI | Session  |
| ASCP_Status | varchar |  |  | SI | Care Provider Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*