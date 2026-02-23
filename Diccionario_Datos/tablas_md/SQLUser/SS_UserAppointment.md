# SQLUser.SS_UserAppointment

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPT_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| APPT_AdmittingRights | varchar |  |  | SI | Admitting Rights |
| APPT_AppointmentNumber | varchar |  |  | SI | Appointment Number |
| APPT_CareProvNumber | varchar |  |  | SI | CareProvNumber |
| APPT_Childsub | double |  |  | NO | Childsub |
| APPT_Classification_DR | bigint |  | FK | SI | Des Ref Classification |
| APPT_Comments | varchar |  |  | SI | Comments |
| APPT_CostCenter_DR | bigint |  | FK | SI | Des Ref CostCenter |
| APPT_DateFrom | date |  |  | SI | DateFrom |
| APPT_DateTo | date |  |  | SI | DateTo |
| APPT_Discount | varchar |  |  | SI | Discount |
| APPT_DocProvNumber | varchar |  |  | SI | DocProvNumber |
| APPT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| APPT_HoursPerFortnight | double |  |  | SI | HoursPerFortnight |
| APPT_MaxNumPatients | double |  |  | SI | MaxNumPatients |
| APPT_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| APPT_RowId | varchar |  |  | NO | - |
| APPT_Title_DR | bigint |  | FK | SI | Des Ref Title |
| APPT_UpdateDate | date |  |  | SI | UpdateDate |
| APPT_UpdateTime | time |  |  | SI | UpdateTime |
| APPT_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| APPT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*