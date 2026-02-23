# SQLUser.RB_OperRoomAdditionalStaff

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBOPAS_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| RBOPAS_CPLocation_DR | bigint |  | FK | SI | DR CTLoc |
| RBOPAS_CareProvType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| RBOPAS_CareProv_DR | varchar |  | FK | SI | Des Ref CT_CareProv |
| RBOPAS_Childsub | double |  |  | NO | Childsub |
| RBOPAS_EndDate | date |  |  | SI | End Date |
| RBOPAS_EndTime | time |  |  | SI | End Time |
| RBOPAS_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| RBOPAS_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| RBOPAS_Operation_DR | bigint |  | FK | SI | Des Ref ORC_Operation  |
| RBOPAS_Remarks | varchar |  |  | SI | Remarks |
| RBOPAS_RowId | varchar |  |  | NO | - |
| RBOPAS_ShiftNumber | varchar |  |  | SI | Shift Number |
| RBOPAS_StartDate | date |  |  | SI | Start Date |
| RBOPAS_StartTime | time |  |  | SI | Start Time |
| RBOPAS_StatePPP_DR | bigint |  | FK | SI | Des Ref PAC_StatePPP |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*