# SQLUser.PA_ISD

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ISD1_RowId | bigint | PK |  | NO | - |
| ISD1_APPT_DR | varchar |  | FK | SI | Des Ref APPT |
| ISD1_AverageWaitingTime | double |  |  | SI | Average Waiting Time |
| ISD1_BedsAvailable | varchar |  |  | SI | Beds Available |
| ISD1_Cancelled | varchar |  |  | SI | Cancelled |
| ISD1_ConsultantType | varchar |  |  | SI | Consultant Type |
| ISD1_DNAFirstAppointment | varchar |  |  | SI | DNA First Appointment |
| ISD1_DNAReturnAppointment | varchar |  |  | SI | DNA Return Appointment |
| ISD1_Daycase | varchar |  |  | SI | Daycase |
| ISD1_EmergencyInpatient | varchar |  |  | SI | Emergency Inpatient |
| ISD1_Extract_DR | bigint |  | FK | SI | Des Ref Extract |
| ISD1_FirstAttendance | varchar |  |  | SI | First Attendance |
| ISD1_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ISD1_ISDType | varchar |  |  | SI | ISD Type |
| ISD1_Inpatient | varchar |  |  | SI | Inpatient |
| ISD1_IntentedManagement | varchar |  |  | SI | Intented Management |
| ISD1_LocumClinics | varchar |  |  | SI | Locum Clinics |
| ISD1_NoHeld | varchar |  |  | SI | No Held |
| ISD1_Others | varchar |  |  | SI | Others |
| ISD1_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ISD1_PatientFromAnotherWard | varchar |  |  | SI | Patient From Another Ward |
| ISD1_Reduced | varchar |  |  | SI | Reduced |
| ISD1_ReturnAttendance | varchar |  |  | SI | Return Attendance |
| ISD1_Specialty_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ISD1_WaitListCategory_DR | bigint |  | FK | SI | Des Ref WaitListCategory |
| ISD1_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*